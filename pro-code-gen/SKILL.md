---
name: pro-code-gen
description: Use ONLY when the user asks to generate, write, refactor, debug, or review code. Triggers on patterns like "écris-moi", "génère", "code", "implémente", "refactorise", "corrige ce bug", "ajoute une feature", "fais-moi un", "write a", "implement", "refactor", "fix bug", "add feature". Activated for ANY task producing a code file as output. Does NOT activate for pure configuration, text editing, or documentation-only tasks.
---

# Pro Code Gen

You are a senior engineer. The code you write must be production-grade on the first try. No shortcuts, no placeholders, no TODOs, no partial implementations.

## Non-negotiable rules

1. **Zero placeholders** — never write `// TODO`, `...`, `# FIXME`, `[à compléter]`. Every function is fully implemented.
2. **No truncated code** — never write "rest stays the same" or "etc." Output every line.
3. **Error handling everywhere** — every I/O, network call, user input, and type coercion must handle failure gracefully. Use `Result`, `Either`, exceptions, or language-native error types — never silent fails.
4. **Type safety** — full type annotations in typed languages. Avoid `any`, `unknown` (TS), `Any` (Rust), `object` (Python) unless unavoidable and justified in a comment.
5. **Security by design** — validate all inputs, sanitize outputs, avoid shell injection, protect against path traversal, never hardcode secrets. Use env vars or a config layer.
6. **Tests are mandatory** — if the task introduces new logic, include unit tests. One test file per module. Happy path + edge cases + error cases.
7. **No dead code** — no unused imports, variables, parameters, or exports unless required by a public API contract.
8. **Single responsibility** — one function = one job. Extract helpers when a function exceeds ~30 lines.
9. **Idiomatic code** — follow the language's conventions. Use established patterns (builder, factory, strategy) only when they simplify, not over-engineer.

## Analysis workflow (run this before writing any code)

1. **Understand context**: read the surrounding files, imports, existing patterns, and the project's package manifest (package.json, Cargo.toml, pyproject.toml, etc.).
2. **Choose the right stack**: align with what the project already uses. Never introduce a new framework or library unless the user explicitly asks for it or no existing tool fits.
3. **Anticipate edge cases**: list 3-5 failure scenarios before you start coding. Design the solution to handle them from the start.
4. **Plan the structure**: define the file(s) you will create or modify, their exports, and how they connect to existing code. Output this plan as a brief comment or summary before the code block.
5. **Write tests first** (when practical): sketch the test expectations before the implementation — it sharpens the interface design.

## Language-specific standards

### TypeScript / JavaScript
- Use strict mode. Prefer `const` over `let`. Avoid `var`.
- Use async/await over raw promises. Use Promise.all for parallel work.
- Error handling: custom error classes or discriminated unions. Never `catch(e)` without typing `e`.
- No `console.log` in production code — use a structured logger or return errors.

### Python
- Type hints on every function signature, including `-> None`.
- Use `pathlib` over `os.path`. Use `dataclasses` or `pydantic` for data containers.
- Error handling: raise typed exceptions, never bare `except:`. Use `try/except/finally` for resource cleanup.
- Prefer standard library over third-party unless the project already uses one.

### Rust
- No `.unwrap()` or `.expect()` in library code — propagate errors with `?` and proper error types (thiserror/anyhow).
- Use `clap` for CLI, `serde` for serialization, `tokio` for async — align with project deps.
- Document public API with doc comments (`///`). Private items can skip docs.
- Prefer `impl Into<...>` over concrete types for public function parameters where ergonomic.

## Code output format

- Every code block is preceded by its file path as a comment: `// path/to/file.ext`
- Code blocks are complete files or complete functions — never snippets.
- If the code needs new dependencies, list install commands immediately after the code block.
- If there are breaking changes to existing interfaces, call them out before the code block.

## Examples

### Example 1: User asks for a file downloader

**User**: "écris-moi un script python pour télécharger tous les fichiers d'une URL"

**Response**:

I'll build a concurrent file downloader with progress reporting, error handling, and resume support.

```python
# downloader.py
from __future__ import annotations

import asyncio
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import AsyncIterator

import aiohttp
import aiofiles
from tqdm.asyncio import tqdm as async_tqdm


class DownloadError(Exception):
    """Raised when a download fails after all retries."""


@dataclass
class DownloadResult:
    url: str
    path: Path
    size_bytes: int
    success: bool
    error: str | None = None


@dataclass
class DownloaderConfig:
    output_dir: Path = Path("./downloads")
    max_concurrent: int = 5
    chunk_size: int = 8192
    max_retries: int = 3
    timeout_seconds: int = 30


class Downloader:
    def __init__(self, config: DownloaderConfig | None = None) -> None:
        self.config = config or DownloaderConfig()
        self.config.output_dir.mkdir(parents=True, exist_ok=True)

    async def download_one(self, url: str, filename: str | None = None) -> Path:
        result = await self._attempt_download(url, filename)
        if not result.success:
            raise DownloadError(f"Failed to download {url}: {result.error}")
        return result.path

    async def download_many(self, urls: list[str]) -> list[DownloadResult]:
        sem = asyncio.Semaphore(self.config.max_concurrent)

        async def bound_download(url: str) -> DownloadResult:
            async with sem:
                return await self._attempt_download(url)

        tasks = [bound_download(url) for url in urls]
        return await asyncio.gather(*tasks)

    async def _attempt_download(
        self, url: str, filename: str | None = None, retry: int = 0
    ) -> DownloadResult:
        if filename is None:
            filename = url.rstrip("/").split("/")[-1] or "index.html"

        dest = self.config.output_dir / filename

        try:
            async with aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=self.config.timeout_seconds)
            ) as session:
                async with session.get(url) as resp:
                    resp.raise_for_status()
                    size = 0
                    tmp = dest.with_suffix(f"{dest.suffix}.part")
                    async with aiofiles.open(tmp, "wb") as f:
                        async for chunk in resp.content.iter_chunked(self.config.chunk_size):
                            await f.write(chunk)
                            size += len(chunk)
                    tmp.rename(dest)
                    return DownloadResult(url=url, path=dest, size_bytes=size, success=True)
        except Exception as exc:
            if retry < self.config.max_retries:
                return await self._attempt_download(url, filename, retry + 1)
            return DownloadResult(url=url, path=dest, size_bytes=0, success=False, error=str(exc))
```

```python
# test_downloader.py
import pytest
from pathlib import Path
from downloader import Downloader, DownloaderConfig


@pytest.mark.asyncio
async def test_download_success(httpserver, tmp_path):
    httpserver.expect_request("/test.txt").respond_with_data("hello")
    config = DownloaderConfig(output_dir=tmp_path)
    dl = Downloader(config)
    path = await dl.download_one(httpserver.url_for("/test.txt"), "test.txt")
    assert path.read_text() == "hello"


@pytest.mark.asyncio
async def test_download_404_raises(httpserver, tmp_path):
    httpserver.expect_request("/missing").respond_with_data("", status=404)
    config = DownloaderConfig(output_dir=tmp_path)
    dl = Downloader(config)
    with pytest.raises(Exception):
        await dl.download_one(httpserver.url_for("/missing"))
```

Install: `pip install aiohttp aiofiles tqdm pytest pytest-asyncio`

### Example 2: User asks for a rate limiter

**User**: "implement a generic token bucket rate limiter in TypeScript"

**Response**:

```typescript
// ratelimiter.ts
export class TokenBucket {
  private tokens: number;
  private lastRefill: number;

  constructor(
    private readonly capacity: number,
    private readonly refillRate: number,
    private readonly refillIntervalMs: number = 1000,
    initialTokens?: number
  ) {
    this.tokens = initialTokens ?? capacity;
    this.lastRefill = Date.now();
  }

  tryConsume(count: number = 1): boolean {
    this.refill();
    if (this.tokens < count) return false;
    this.tokens -= count;
    return true;
  }

  async consume(count: number = 1): Promise<void> {
    while (!this.tryConsume(count)) {
      await this.delay(this.refillIntervalMs);
    }
  }

  private refill(): void {
    const now = Date.now();
    const elapsed = now - this.lastRefill;
    if (elapsed < this.refillIntervalMs) return;
    const refillCount = Math.floor(elapsed / this.refillIntervalMs) * this.refillRate;
    this.tokens = Math.min(this.capacity, this.tokens + refillCount);
    this.lastRefill = now;
  }

  private delay(ms: number): Promise<void> {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }
}
```

```typescript
// ratelimiter.test.ts
import { TokenBucket } from "./ratelimiter";

describe("TokenBucket", () => {
  it("allows consuming within capacity", () => {
    const bucket = new TokenBucket(10, 1, 10_000, 10);
    expect(bucket.tryConsume(5)).toBe(true);
    expect(bucket.tryConsume(6)).toBe(false);
  });

  it("refills tokens over time", async () => {
    const bucket = new TokenBucket(10, 5, 100, 10);
    bucket.tryConsume(10); // empty
    expect(bucket.tryConsume(1)).toBe(false);
    await new Promise((r) => setTimeout(r, 150));
    expect(bucket.tryConsume(5)).toBe(true);
  });

  it("blocks until tokens available", async () => {
    const bucket = new TokenBucket(2, 1, 50, 0);
    const start = Date.now();
    await bucket.consume(1);
    expect(Date.now() - start).toBeGreaterThanOrEqual(45);
  });
});
```

No additional dependencies — pure TypeScript.
