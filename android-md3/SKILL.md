---
name: android-md3
description: >-
  Use ONLY when the user asks for Android Material Design 3 Expressive (MD3E) UI,
  Material 3 theming, dynamic color, HCT color space, tonal palettes, Material You,
  MotionScheme, spring physics, expressive motion, fluid navigation, M3 Shapes API,
  material shape system, expressive typography, Adaptive layout, FAB Menu, ButtonGroup,
  FloatingToolbar, Carousel, LoadingIndicator, Split button, Branded surface,
  Modal navigation bar, MaterialExpressiveTheme,
  or any Android 16 MD3E Compose UI design system.
  Activate for ANY task producing Android MD3E UI in Jetpack Compose or a faithful
  web/React/Kotlin transposition of Material Design 3 Expressive.
  If the user mentions Material 3, Material You, or Android expressive UI without
  triggering the description, load it anyway.
---

# Android Material Design 3 Expressive (MD3E) — Design System

Sources (official, fetched live):

Primary sources provided by user:
- **https://m3.material.io/** — Material Design 3 official guidelines & expressive overview
- **https://m3.material.io/components** — Complete component catalog with specs

Additional official references:
- developer.android.com/reference/kotlin/androidx/compose/material3/MaterialExpressiveTheme — API reference (added 1.5.0-alpha19)
- developer.android.com/reference/kotlin/androidx/compose/material3/MotionScheme — MotionScheme API
- developer.android.com/develop/ui/compose/designsystems/material3 — Compose M3 guide
- m3.material.io/blog/m3-expressive-motion-theming — Motion physics blog post
- developer.android.com/jetpack/androidx/releases/compose-material3 — Compose Material 3 releases
- Google I/O 2025: "Material Design 3 Expressive" announcements
- MD3E ships with Android 16 + Wear OS 6.
- **Compose-first**: MDC-Android 1.14 (May 2026) is the final stable release for Android Views. All future M3 features are Compose-only.

## Core Philosophy

MD3E builds on Material 3 (Material You) with **emotion-driven design**:
1. **Emotion-driven color** — dynamic, tonal, context-aware
2. **Physics-based motion** — spring animations replacing duration-based curves
3. **Flexible typography** — scalable, emotional, expressive
4. **Contrasting shapes** — 35 new shapes, bolder geometry
5. **Adaptive components** — morph between conformations based on context

Mental model: *"Would Google approve this as part of Android 16's design language?"* If no, redo.

## Color System

### HCT Color Space (Hue / Chroma / Tone)

Replaces HSL/hue-based systems. Every color is (H, C, T):

| Component | Range | Description |
|-----------|-------|-------------|
| Hue | 0–360 | Perceptual hue angle |
| Chroma | 0–~120 | Colorfulness/saturation (content-specific max) |
| Tone | 0–100 | Perceived lightness (0=black, 100=white) |

### 5 Key Colors (Max 5 for harmony)

| Role | Tonal Palette Range | Light Scheme | Dark Scheme |
|------|-------------------|-------------|-------------|
| Primary | Tone 40–100 | Tone 40 | Tone 80 |
| Secondary | Tone 40–100 | Tone 40 | Tone 80 |
| Tertiary | Tone 40–100 | Tone 40 | Tone 80 |
| Neutral | Tone 0–100 | Tone 99 bg / 10 on-bg | Tone 10 bg / 90 on-bg |
| Neutral Variant | Tone 30–100 | Tone 95 bg / 30 on-bg | Tone 30 bg / 80 on-bg |

### Tonal Palette (13 tones per key color)

```
Tone  0: #000000
Tone 10: darkest surface
Tone 20: darkest container
Tone 30: on-tertiary container
Tone 40: primary / secondary / tertiary
Tone 50: 
Tone 60: 
Tone 70: 
Tone 80: primary (dark)
Tone 90: surface container
Tone 95: surface
Tone 99: background
Tone 100: #FFFFFF
```

### Light Scheme — Role to Tone Assignment

| Role | Tone | Hex Example (Default Blue) |
|------|------|---------------------------|
| `primary` | 40 | `#0061A4` |
| `onPrimary` | 100 | `#FFFFFF` |
| `primaryContainer` | 90 | `#D0E4FF` |
| `onPrimaryContainer` | 10 | `#001D36` |
| `secondary` | 40 | `#535F70` |
| `onSecondary` | 100 | `#FFFFFF` |
| `secondaryContainer` | 90 | `#D6E3F7` |
| `onSecondaryContainer` | 10 | `#101C2B` |
| `tertiary` | 40 | `#6B5778` |
| `onTertiary` | 100 | `#FFFFFF` |
| `tertiaryContainer` | 90 | `#F2DAFF` |
| `onTertiaryContainer` | 10 | `#251431` |
| `error` | 40 | `#BA1A1A` |
| `onError` | 100 | `#FFFFFF` |
| `errorContainer` | 90 | `#FFDAD6` |
| `onErrorContainer` | 10 | `#410002` |
| `background` | 99 | `#FDFCFF` |
| `onBackground` | 10 | `#1A1C1E` |
| `surface` | 99 | `#FDFCFF` |
| `onSurface` | 10 | `#1A1C1E` |
| `surfaceVariant` | 90 | `#E0E2EC` |
| `onSurfaceVariant` | 30 | `#44474E` |
| `outline` | 50 | `#74777F` |
| `outlineVariant` | 80 | `#C4C6D0` |
| `inverseSurface` | 20 | `#2F3033` |
| `inverseOnSurface` | 95 | `#F1F0F4` |
| `inversePrimary` | 80 | `#9ECAFF` |
| `surfaceTint` | 40 | `#0061A4` |

### Dark Scheme — Role to Tone Assignment

| Role | Tone | Hex Example (Default Blue) |
|------|------|---------------------------|
| `primary` | 80 | `#9ECAFF` |
| `onPrimary` | 20 | `#003258` |
| `primaryContainer` | 30 | `#00497D` |
| `onPrimaryContainer` | 90 | `#D0E4FF` |
| `secondary` | 80 | `#BBC7DB` |
| `onSecondary` | 20 | `#253140` |
| `secondaryContainer` | 30 | `#3B4858` |
| `onSecondaryContainer` | 90 | `#D6E3F7` |
| `tertiary` | 80 | `#D6BEE4` |
| `onTertiary` | 20 | `#3B2948` |
| `tertiaryContainer` | 30 | `#523F5F` |
| `onTertiaryContainer` | 90 | `#F2DAFF` |
| `error` | 80 | `#FFB4AB` |
| `onError` | 20 | `#690005` |
| `errorContainer` | 30 | `#93000A` |
| `onErrorContainer` | 90 | `#FFDAD6` |
| `background` | 10 | `#1A1C1E` |
| `onBackground` | 90 | `#E2E2E6` |
| `surface` | 10 | `#1A1C1E` |
| `onSurface` | 90 | `#E2E2E6` |
| `surfaceVariant` | 30 | `#44474E` |
| `onSurfaceVariant` | 80 | `#C4C6D0` |
| `outline` | 50 | `#74777F` |
| `outlineVariant` | 80 | `#C4C6D0` |
| `inverseSurface` | 90 | `#E2E2E6` |
| `inverseOnSurface` | 20 | `#2F3033` |
| `inversePrimary` | 40 | `#0061A4` |

### Expanded M3 Color Tokens (MD3E New)

| Token | Description | Example Tone |
|-------|-------------|-------------|
| `fixedPrimary` | Primary that stays same tone in both schemes (Tone 40) | 40 |
| `fixedOnPrimary` | On-primary for `fixedPrimary` (Tone 100) | 100 |
| `fixedPrimaryContainer` | Container for `fixedPrimary` (Tone 90) | 90 |
| `fixedOnPrimaryContainer` | On-container (Tone 10) | 10 |
| `fixedSecondary` / `fixedTertiary` | Same pattern for secondary/tertiary | 40/100/90/10 |
| `dimPrimary` | Lower-chroma version of `primary` for spacious layouts | ~Tone 50, C-20% |
| `dimOnPrimary` | On-color for dim primary | 100 |
| `dimPrimaryContainer` | Container for dim primary | ~Tone 95, C-50% |
| `dimSecondary` / `dimTertiary` | Same for secondary/tertiary | — |
| `surfaceDim` | Surface variant for fab/dialogs (Tone 87 light) | 87 |
| `surfaceBright` | Brighter surface (Tone 98 light) | 98 |
| `surfaceContainerLowest` | Surface container (Tone 96) | 96 |
| `surfaceContainerLow` | (Tone 94) | 94 |
| `surfaceContainer` | (Tone 92) | 92 |
| `surfaceContainerHigh` | (Tone 88) | 88 |
| `surfaceContainerHighest` | (Tone 84) | 84 |

### Contrast Levels (3 levels)

| Level | Description | Effect |
|-------|-------------|--------|
| 0.0 | Standard (default) | Normal accessibility |
| 0.5 | Medium contrast | Tone shifts +2 for surfaces, -2 for on-colors |
| 1.0 | High contrast | Tone shifts +4 for surfaces, -4 for on-colors |

Set via `contrastLevel` in `dynamicLightColorScheme` / `dynamicDarkColorScheme`.

### Dynamic Color — from Wallpaper

```kotlin
// Extract color from wallpaper (Android 12+)
val scheme = dynamicLightColorScheme(context)
// Or for dark scheme:
// val scheme = dynamicDarkColorScheme(context)
// scheme.primary, scheme.secondary, scheme.tertiary, scheme.neutral, ...

// MD3E adds expressiveLightColorScheme (enhanced tonal palettes):
// @OptIn(ExperimentalMaterial3ExpressiveApi::class)
// val scheme = expressiveLightColorScheme()
```

### Dynamic Color — from Image (MD3E New)

```kotlin
// Extract from any image (apps can set their own accent)
val colors = image.toColorResults()
val primary = colors[0].toArgb()
// Then build tonal palette from primary
```

## Typography

### Type Scale (Material 3)

| Style | Font Size | Line Height | Weight | Tracking |
|-------|-----------|-------------|--------|----------|
| `displayLarge` | 57sp | 64sp | 400 | -0.25 |
| `displayMedium` | 45sp | 52sp | 400 | 0 |
| `displaySmall` | 36sp | 44sp | 400 | 0 |
| `headlineLarge` | 32sp | 40sp | 400 | 0 |
| `headlineMedium` | 28sp | 36sp | 400 | 0 |
| `headlineSmall` | 24sp | 32sp | 400 | 0 |
| `titleLarge` | 22sp | 28sp | 500 | 0 |
| `titleMedium` | 16sp | 24sp | 500 | 0.15 |
| `titleSmall` | 14sp | 20sp | 500 | 0.1 |
| `bodyLarge` | 16sp | 24sp | 400 | 0.5 |
| `bodyMedium` | 14sp | 20sp | 400 | 0.25 |
| `bodySmall` | 12sp | 16sp | 400 | 0.4 |
| `labelLarge` | 14sp | 20sp | 500 | 0.1 |
| `labelMedium` | 12sp | 16sp | 500 | 0.5 |
| `labelSmall` | 11sp | 16sp | 500 | 0.5 |

### Emphasized Variants (MD3E New — Emotional Role)

Each text style has an **Emphasized** variant with increased weight + tracking:

| Base Style | Emphasized Weight | Emphasized Line Height | Emphasized Letter Spacing | Suggested Font |
|------------|------------------|----------------------|--------------------------|----------------|
| `displayLarge` | 600 | 64sp | -0.5 | Google Sans Display |
| `displayMedium` | 600 | 56sp | -0.25 | Google Sans Display |
| `displaySmall` | 600 | 48sp | -0.25 | Google Sans Display |
| `headlineLarge` | 600 | 44sp | -0.25 | Google Sans Display |
| `headlineMedium` | 600 | 40sp | -0.25 | Google Sans Display |
| `headlineSmall` | 600 | 36sp | -0.25 | Google Sans Display |
| `titleLarge` | 600 | 32sp | 0 | Google Sans Text |
| `titleMedium` | 600 | 28sp | 0.15 | Google Sans Text |
| `titleSmall` | 600 | 24sp | 0.1 | Google Sans Text |
| `bodyLarge` | 500 | 28sp | 0.5 | Google Sans Text |
| `bodyMedium` | 500 | 24sp | 0.25 | Google Sans Text |
| `bodySmall` | 500 | 20sp | 0.4 | Google Sans Text |
| `labelLarge` | 600 | 24sp | 0.1 | Google Sans Text |
| `labelMedium` | 600 | 20sp | 0.5 | Google Sans Text |
| `labelSmall` | 600 | 20sp | 0.5 | Google Sans Text |

Use **Emphasized** for:
- Emotionally charged moments (onboarding, congratulations, alerts)
- First word/phrase in a paragraph (drop cap equivalent)
- Primary action labels
- Data highlights

### Font Family System

```
Display → Google Sans Display (rounded, friendly)
Headline → Google Sans Display or Google Sans Text
Title → Google Sans Text
Body → Google Sans Text
Label → Google Sans Text
Monospace → Google Sans Mono
```

If Google Sans is unavailable, fallback:
- Sans-serif → `sans-serif` (Roboto)
- Sans-serif Medium → `sans-serif-medium`
- Monospace → `monospace`

## Shape

### Shape Scale (Material 3 + MD3E — 10 levels)

Source: `ShapeDefaults` / `ShapeDemos.kt` from AOSP source (official).

| Token | Default Value | Usage |
|-------|--------------|-------|
| `none` | 0dp | No rounding |
| `extraSmall` | 4dp | Chips, badges |
| `small` | 8dp | Cards, dialogs, sheets |
| `medium` | 12dp | FAB, larger cards |
| `large` | 16dp | Bottom sheets, navigation drawer |
| `largeIncreased` ✦ | **20dp** | Expressive hero cards, toolbars (MD3E new) |
| `extraLarge` | 28dp | Dialog, full-screen card |
| `extraLargeIncreased` ✦ | **32dp** | Expressive dialogs, hero containers (MD3E new) |
| `extraExtraLarge` ✦ | **48dp** | FloatingToolbar, hero sections (MD3E new) |
| `full` | ∞ | Circular / pill |

✦ = MD3E expressive-only tokens (not in base M3).

```kotlin
// Expressive Shapes (MD3E)
private val ExpressiveShapes = Shapes(
    extraSmall = RoundedCornerShape(4.dp),
    small = RoundedCornerShape(8.dp),
    medium = RoundedCornerShape(12.dp),
    large = RoundedCornerShape(16.dp),
    largeIncreased = RoundedCornerShape(20.dp),   // MD3E expressive token
    extraLarge = RoundedCornerShape(28.dp),
    extraLargeIncreased = RoundedCornerShape(32.dp), // MD3E expressive token
    extraExtraLarge = RoundedCornerShape(48.dp)       // MD3E expressive token
)
```

### 35 MaterialShapes (MD3E — `MaterialShapes` API)

`MaterialShapes` is a companion object in `androidx.compose.material3` (requires `@OptIn(ExperimentalMaterial3ExpressiveApi::class)`). Each shape is a `RoundedPolygon` — a polygon with rounded vertices. Use them via `MaterialTheme.materialShapes`:

```kotlin
MaterialTheme.materialShapes.hexagon  // shaped for a Hexagon
MaterialTheme.materialShapes.puffy     // shaped for Puffy
```

All available shapes:

| # | Shape | Description |
|---|-------|-------------|
| 1 | `Circle` | Perfect circle |
| 2 | `Square` | Perfect square |
| 3 | `Oval` | Elliptical |
| 4 | `Pill` | Capsule / stadium |
| 5 | `Triangle` | Equilateral triangle |
| 6 | `Diamond` | 45° rotated square |
| 7 | `Pentagon` | 5-sided regular polygon |
| 8 | `Hexagon` | 6-sided regular polygon |
| 9 | `Octagon` | 8-sided regular polygon |
| 10 | `Arrow` | Chevron / arrowhead |
| 11 | `SemiCircle` | Half-circle |
| 12 | `Arch` | Arched top edge |
| 13 | `Fan` | Pie-slice quadrant |
| 14 | `Gem` | Faceted diamond shape |
| 15 | `ClamShell` | Scalloped semicircle |
| 16 | `Flower` | 6-petal flower outline |
| 17 | `Clover4Leaf` | 4-lobed clover |
| 18 | `Clover8Leaf` | 8-lobed clover |
| 19 | `Cookie4Sided` | Pinched 4-sided blob |
| 20 | `Cookie6Sided` | Pinched 6-sided blob |
| 21 | `Cookie7Sided` | Pinched 7-sided blob |
| 22 | `Cookie9Sided` | Pinched 9-sided blob |
| 23 | `Cookie12Sided` | Pinched 12-sided blob |
| 24 | `Bun` | Rounded dome |
| 25 | `Slanted` | Parallelogram lean |
| 26 | `Ghostish` | Soft organic blob |
| 27 | `Burst` | Spiky starburst |
| 28 | `SoftBurst` | Rounded starburst |
| 29 | `Boom` | Explosive spiky shape |
| 30 | `SoftBoom` | Rounded explosive shape |
| 31 | `Puffy` | Inflated rounded rect |
| 32 | `PuffyDiamond` | Inflated diamond |
| 33 | `PixelCircle` | Pixelated circle approximation |
| 34 | `PixelTriangle` | Pixelated triangle approximation |
| 35 | `Sunny` | Sun-like with rays |
| 36 | `VerySunny` | Sun with longer/extended rays |
| 37 | `Heart` | Classic heart shape |

While the API is named "35 Shapes", the official companion object actually exposes **37** entries — the original 35 plus `VerySunny` and `Heart` added later.

Each `MaterialShapes` shape has a `cornerRadius` parameter:
```kotlin
MaterialShapes.hexagon(cornerRadius = 8.dp)  // Hexagon with rounded vertices
```

Access via `MaterialTheme.materialShapes`:
```kotlin
@OptIn(ExperimentalMaterial3ExpressiveApi::class)
@Composable
fun HexagonCard() {
    Card(
        shape = MaterialTheme.materialShapes.hexagon(cornerRadius = 12.dp)
    ) { /* content */ }
}
```

## Motion

### Spring Physics (MD3E Core Paradigm)

Replaces duration-based `tween()` as default. Built on `spring()`:

```kotlin
import androidx.compose.animation.core.spring

// Default spring (expressive):
val springSpec = spring<Float>(
    stiffness = Spring.StiffnessMediumLow,  // 300.0
    dampingRatio = Spring.DampingRatioMediumBouncy  // 0.5
)

// Standard spring (subdued):
val standardSpring = spring<Float>(
    stiffness = Spring.StiffnessMedium,  // 600.0
    dampingRatio = Spring.DampingRatioNoBouncy  // 1.0
)
```

| Token | Stiffness | Damping Ratio | Character |
|-------|-----------|---------------|-----------|
| `StiffnessHigh` | 10000 | — | Snappy, instant |
| `StiffnessMedium` | 600 | — | Standard transition |
| `StiffnessMediumLow` | 300 | — | Bouncy, expressive |
| `StiffnessLow` | 100 | — | Very bouncy, playful |
| `DampingRatioNoBouncy` | — | 1.0 | Critically damped |
| `DampingRatioMediumBouncy` | — | 0.5 | Moderate bounce |
| `DampingRatioLowBouncy` | — | 0.25 | Lots of bounce |

### MotionScheme (MD3E — Expressive vs Standard)

From official source code (`MotionScheme.standard()` and `MotionScheme.expressive()` in Compose Material 3, graduated from experimental):

```kotlin
import androidx.compose.material3.MotionScheme
// Requires: @OptIn(ExperimentalMaterial3ExpressiveApi::class)

// Standard — linear motion, utilitarian UI elements, recurring interactions
val standard = MotionScheme.standard()
// Expressive — bouncy, playful, for prominent UI elements and hero interactions
val expressive = MotionScheme.expressive()
```

#### Internal spring parameters (from source code)

| Scheme | Token | Stiffness | Damping Ratio | Character |
|--------|-------|-----------|---------------|-----------|
| Standard | defaultSpatialSpec | `600.0` | `1.0` (no bounce) | Linear, functional |
| Standard | defaultEffectSpec | `400.0` | — | Quick color/opacity |
| Expressive | defaultSpatialSpec | `300.0` | `0.5` (medium bouncy) | Bouncy, playful |
| Expressive | defaultEffectSpec | `400.0` | — | Quick color/opacity |

```kotlin
// Wrapping entire app in expressive theme:
@OptIn(ExperimentalMaterial3ExpressiveApi::class)
MaterialExpressiveTheme(
    colorScheme = colorScheme,
    motionScheme = MotionScheme.expressive(),
    shapes = Shapes(),
    typography = Typography()
) {
    // All M3 components automatically use spring physics
}

// Standard motion (subdued, M3 baseline):
MaterialExpressiveTheme(
    motionScheme = MotionScheme.standard()
) {
    // Utilitarian transitions
}
```

Components now respect `MaterialTheme.motionScheme` for:
- Nested scroll gestures (BottomSheet, etc.)
- Drag gestures
- All enter/exit transitions
- Indicator animations

### Easing & Duration (fallback — m3.material.io official)

The easing/duration system is still used for transitions but **no longer maintained** (spring physics is the new default). From m3.material.io/styles/motion/easing-and-duration:

| Easing | Duration | Transition type |
|--------|----------|----------------|
| Emphasized | 500ms | Begin and end on screen |
| Emphasized decelerate | 400ms | Enter the screen |
| Emphasized accelerate | 200ms | Exit the screen |
| Standard | 300ms | Begin and end on screen |
| Standard decelerate | 250ms | Enter the screen |
| Standard accelerate | 200ms | Exit the screen |

"M3 easing is more expressive. Transitions have snappy take-offs and very soft landings."

### Motion Tokens — Spatial & Effect

Spatial tokens (position, size, shape) — affect layout:

| Token | Expressive Duration | Standard Duration |
|-------|-------------------|-------------------|
| `spatialFast` | 200ms | 200ms |
| `spatialDefault` | 400ms | 300ms |
| `spatialSlow` | 600ms | 400ms |

Effect tokens (color, opacity) — affect appearance:

| Token | Expressive Duration | Standard Duration |
|-------|-------------------|-------------------|
| `effectFast` | 150ms | 150ms |
| `effectDefault` | 250ms | 200ms |
| `effectSlow` | 350ms | 300ms |

### Elevation Motion

Elevation changes animate via spring:
```kotlin
// Card elevation on press
@Composable
fun Modifier.elevatedOnPress(
    targetElevation: Dp = 4.dp
): Modifier = composed {
    val interactionSource = remember { MutableInteractionSource() }
    val pressed by interactionSource.collectIsPressedAsState()
    val elevation by animateDpAsState(
        targetValue = if (pressed) targetElevation else 0.dp,
        animationSpec = spring(
            dampingRatio = Spring.DampingRatioMediumBouncy,
            stiffness = Spring.StiffnessMediumLow
        )
    )
    this.shadow(elevation).then(Modifier.clickable(interactionSource, null) {})
}
```

## Components (14 New/Updated in MD3E)

Official catalog: m3.material.io/components.
Key quote: *"New: Toolbars — Flexible component to display frequently used actions. Toolbars hold a variety of controls like buttons, and can also be paired with a FAB."*
*"New: Split button — Pair a button with related actions in a connected menu. Split buttons leverage expressive shape and motion strategies."*
*"New: Button groups — A new way to organize related buttons—with shape-shifting buttons that bump and react to each other."*
*"Loading indicator — New component (May 2025) designed to show progress that loads in under five seconds. Replaces most uses of the indeterminate circular progress indicator."*

### 1. FAB Menu

```kotlin
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Add
import androidx.compose.material.icons.filled.Close

data class FABMenuItem(
    val icon: ImageVector,
    val label: String,
    val onClick: () -> Unit
)

@Composable
fun FABMenu(
    expanded: Boolean,
    onToggle: () -> Unit,
    items: List<FABMenuItem>
) {
    Column(horizontalAlignment = Alignment.End) {
        AnimatedVisibility(
            visible = expanded,
            enter = fadeIn(animationSpec = spring()) +
                slideInVertically(animationSpec = spring(), initialOffsetY = { it }),
            exit = fadeOut() + slideOutVertically(targetOffsetY = { it })
        ) {
            Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
                items.forEach { item ->
                    SmallFloatingActionButton(onClick = item.onClick) {
                        Icon(item.icon, contentDescription = item.label)
                    }
                }
            }
        }
        LargeFloatingActionButton(onClick = onToggle) {
            Icon(
                imageVector = if (expanded) Icons.Default.Close else Icons.Default.Add,
                contentDescription = if (expanded) "Close menu" else "Open menu"
            )
        }
    }
}
```

### 2. ButtonGroup

```kotlin
@Composable
fun ButtonGroup(
    buttons: List<ButtonGroupItem>,
    selectedIndex: Int,
    onSelected: (Int) -> Unit
) {
    Row(
        modifier = Modifier
            .clip(RoundedCornerShape(12.dp))
            .background(MaterialTheme.colorScheme.surfaceVariant),
        horizontalArrangement = Arrangement.spacedBy(0.dp)
    ) {
        buttons.forEachIndexed { index, item ->
            TextButton(
                onClick = { onSelected(index) },
                colors = ButtonDefaults.textButtonColors(
                    containerColor = if (index == selectedIndex)
                        MaterialTheme.colorScheme.surface
                    else Color.Transparent
                )
            ) {
                Text(item.label, style = MaterialTheme.typography.labelLarge)
            }
        }
    }
}
```

### 3. FloatingToolbar

```kotlin
@Composable
fun FloatingToolbar(
    modifier: Modifier = Modifier,
    actions: @Composable RowScope.() -> Unit
) {
    Surface(
        modifier = modifier
            .clip(RoundedCornerShape(28.dp))
            .shadow(4.dp, RoundedCornerShape(28.dp)),
        color = MaterialTheme.colorScheme.surfaceContainerHigh,
        tonalElevation = 3.dp
    ) {
        Row(
            modifier = Modifier.padding(horizontal = 8.dp, vertical = 4.dp),
            horizontalArrangement = Arrangement.spacedBy(4.dp),
            content = actions
        )
    }
}
```

### 4. Carousel

```kotlin
@OptIn(ExperimentalFoundationApi::class)
@Composable
fun Carousel(
    items: List<Any>,
    modifier: Modifier = Modifier
) {
    LazyRow(
        modifier = modifier,
        horizontalArrangement = Arrangement.spacedBy(12.dp),
        contentPadding = PaddingValues(horizontal = 16.dp),
        flingBehavior = rememberSnapFlingBehavior()
    ) {
        items(items) { item ->
            Card(
                modifier = Modifier
                    .width(280.dp)
                    .fillMaxHeight(),
                shape = RoundedCornerShape(16.dp)
            ) {
                // item content
            }
        }
    }
}
```

### 5. LoadingIndicator (New in MD3E — May 2025)

Replaces indeterminate `CircularProgressIndicator`. Designed for progress <5s. Use for pull-to-refresh. Supports contained/uncontained variants, shape + motion, and scales in size. Customize waveform and thickness.

```kotlin
// Contained loading indicator (MD3E new — eye-catching waveform)
@OptIn(ExperimentalMaterial3ExpressiveApi::class)
@Composable
fun WavyLoadingIndicator(
    progress: Float,
    modifier: Modifier = Modifier
) {
    LoadingIndicator(
        progress = progress,
        modifier = modifier
            .fillMaxWidth()
            .height(4.dp),
        // Uses spring animation via MotionScheme.expressive() by default
    )
}

// Uncontained — for pull-to-refresh
@OptIn(ExperimentalMaterial3ExpressiveApi::class)
@Composable
fun PullToRefreshIndicator(
    isRefreshing: Boolean,
    onRefresh: () -> Unit
) {
    PullToRefreshBox(
        isRefreshing = isRefreshing,
        onRefresh = onRefresh
    ) {
        // content
    }
}
```

### 6. Split Button

```kotlin
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowDropDown

data class SplitButtonItem(
    val label: String,
    val onClick: () -> Unit
)

@Composable
fun SplitButton(
    label: String,
    onClick: () -> Unit,
    menuItems: List<SplitButtonItem>,
    expanded: Boolean = false,
    onExpandedChange: (Boolean) -> Unit = {},
    modifier: Modifier = Modifier
) {
    Row(modifier) {
        Button(
            onClick = onClick,
            modifier = Modifier.weight(1f),
            shape = RoundedCornerShape(
                topStart = 20.dp,
                bottomStart = 20.dp,
                topEnd = 0.dp,
                bottomEnd = 0.dp
            )
        ) {
            Text(label)
        }
        Button(
            onClick = { onExpandedChange(!expanded) },
            shape = RoundedCornerShape(
                topStart = 0.dp,
                bottomStart = 0.dp,
                topEnd = 20.dp,
                bottomEnd = 20.dp
            ),
            colors = ButtonDefaults.buttonColors(
                containerColor = MaterialTheme.colorScheme.primaryContainer,
                contentColor = MaterialTheme.colorScheme.onPrimaryContainer
            )
        ) {
            Icon(Icons.Default.ArrowDropDown, contentDescription = "More options")
        }
    }
    DropdownMenu(
        expanded = expanded,
        onDismissRequest = { onExpandedChange(false) }
    ) {
        menuItems.forEach { item ->
            DropdownMenuItem(
                text = { Text(item.label) },
                onClick = {
                    item.onClick()
                    onExpandedChange(false)
                }
            )
        }
    }
}
```

### 7–14. Other MD3E Components (Quick Reference)

| # | Component | Description |
|---|-----------|-------------|
| 7 | **Branded Surface** | Surface with brand gradient overlay for hero sections |
| 8 | **Modal Navigation Bar** | Bottom nav overlay with glass background for modals |
| 9 | **Enhanced Card** | Card with expandable footer + motion preview |
| 10 | **Search Scrim** | Full-screen search with dynamic background dim |
| 11 | **Docked Sheet** | Sheet that stays docked at bottom with peek height |
| 12 | **Pager with Tabs** | HorizontalPager with animated tab indicator spring |
| 13 | **Progress with Label** | Progress indicator with animated percentage label |
| 14 | **Date/Time Picker** | Scrollable picker with spring fling + haptic feedback |

## Compose Implementation — Theme Setup

### Dependency

```kotlin
// build.gradle.kts (Module :app)
dependencies {
    implementation(platform("androidx.compose:compose-bom:2025.06.00"))
    implementation("androidx.compose.material3:material3")
}
```

### MaterialExpressiveTheme (official API — added 1.5.0-alpha19)

```kotlin
@OptIn(ExperimentalMaterial3ExpressiveApi::class)
// Starting from 1.5.0 stable, the annotation may not be required
// Check release notes: developer.android.com/jetpack/androidx/releases/compose-material3

@Composable
fun MD3ETheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    contrastLevel: Float = 0f,
    dynamicColor: Boolean = true,
    content: @Composable () -> Unit
) {
    val colorScheme = when {
        dynamicColor && Build.VERSION.SDK_INT >= Build.VERSION_CODES.S -> {
            val context = LocalContext.current
            if (darkTheme) dynamicDarkColorScheme(context, contrastLevel = contrastLevel)
            else dynamicLightColorScheme(context, contrastLevel = contrastLevel)
        }
        darkTheme -> darkColorScheme()
        else -> lightColorScheme()
    }

    // MaterialExpressiveTheme wraps MaterialTheme, providing motionScheme
    MaterialExpressiveTheme(
        colorScheme = colorScheme,
        typography = ExpressiveTypography,
        shapes = ExpressiveShapes,
        motionScheme = MotionScheme.expressive()
    ) {
        content()
    }
}

// MaterialExpressiveTheme signature (from official API reference):
// fun MaterialExpressiveTheme(
//     colorScheme: ColorScheme? = null,
//     motionScheme: MotionScheme? = null,
//     shapes: Shapes? = null,
//     typography: Typography? = null,
//     content: @Composable () -> Unit
// )
// Any values not set fall back to defaults.
// To inherit current theme values, call MaterialTheme within the subtree.

// Emphasized Typography (MD3E — emotional weight)
// Emphasized variants are NOT in the Typography class —
// applied inline with TextStyle.copy() for emotional moments:
//   Text("Hello", style = MaterialTheme.typography.displayLarge.copy(
//       fontWeight = FontWeight.SemiBold,
//       letterSpacing = (-0.5).sp
//   ))
private val ExpressiveTypography = Typography(
    displayLarge = TextStyle(
        fontWeight = FontWeight.Normal,
        fontSize = 57.sp,
        lineHeight = 64.sp,
        letterSpacing = (-0.25).sp
    ),
    headlineLarge = TextStyle(
        fontWeight = FontWeight.Normal,
        fontSize = 32.sp,
        lineHeight = 40.sp,
        letterSpacing = 0.sp
    ),
    // ... repeat for all 15 styles
)

// Expressive Shapes (with MD3E expressive tokens)
private val ExpressiveShapes = Shapes(
    extraSmall = RoundedCornerShape(4.dp),
    small = RoundedCornerShape(8.dp),
    medium = RoundedCornerShape(12.dp),
    large = RoundedCornerShape(16.dp),
    largeIncreased = RoundedCornerShape(20.dp),  // MD3E expressive token
    extraLarge = RoundedCornerShape(28.dp),
    extraLargeIncreased = RoundedCornerShape(32.dp), // MD3E expressive token
    extraExtraLarge = RoundedCornerShape(48.dp)       // MD3E expressive token
)
```

## Motion in Compose — Spring API

```kotlin
import androidx.compose.animation.core.*

// 1. animateXxxAsState with spring
val offset by animateFloatAsState(
    targetValue = if (expanded) 100f else 0f,
    animationSpec = spring(
        dampingRatio = 0.5f,    // 0.5 = medium bouncy, 1.0 = no bounce
        stiffness = 300f        // 300 = medium-low, 600 = medium, 10000 = high
    )
)

// 2. Animatable with spring
val scale = remember { Animatable(1f) }
LaunchedEffect(Unit) {
    scale.animateTo(
        targetValue = 1.2f,
        animationSpec = spring(
            dampingRatio = Spring.DampingRatioMediumBouncy,
            stiffness = Spring.StiffnessMediumLow
        )
    )
}

// 3. AnimatedVisibility with spring
AnimatedVisibility(
    visible = expanded,
    enter = fadeIn(animationSpec = spring(
        dampingRatio = 0.5f,
        stiffness = 300f
    )) + slideInVertically(animationSpec = spring(
        dampingRatio = 0.5f,
        stiffness = 300f
    )),
    exit = fadeOut() + slideOutVertically()
) {
    // content
}

// 4. ContentTransform
AnimatedContent(
    targetState = page,
    transitionSpec = {
        ContentTransform(
            targetContentEnter = fadeIn(animationSpec = spring()) +
                slideInHorizontally(animationSpec = spring()),
            initialContentExit = fadeOut(animationSpec = spring()) +
                slideOutHorizontally(animationSpec = spring())
        )
    }
) { currentPage ->
    PageContent(currentPage)
}
```

## Interactive Patterns

### Interactive Motion — MD3E + Compose

```kotlin
// Surface elevation reacts to press
@Composable
fun Modifier.interactiveElevation(
    defaultElevation: Dp = 0.dp,
    pressedElevation: Dp = 4.dp
): Modifier = composed {
    val interactionSource = remember { MutableInteractionSource() }
    val isPressed by interactionSource.collectIsPressedAsState()
    val elevation by animateDpAsState(
        targetValue = if (isPressed) pressedElevation else defaultElevation,
        animationSpec = spring(
            dampingRatio = Spring.DampingRatioMediumBouncy,
            stiffness = Spring.StiffnessMediumLow
        )
    )
    this.shadow(elevation)
        .clickable(interactionSource = interactionSource, indication = null) { }
}

// Scale motion on press
@Composable
fun Modifier.scaleOnPress(
    defaultScale: Float = 1f,
    pressedScale: Float = 0.97f
): Modifier = composed {
    val interactionSource = remember { MutableInteractionSource() }
    val isPressed by interactionSource.collectIsPressedAsState()
    val scale by animateFloatAsState(
        targetValue = if (isPressed) pressedScale else defaultScale,
        animationSpec = spring(
            dampingRatio = Spring.DampingRatioNoBouncy,
            stiffness = Spring.StiffnessHigh
        ),
        label = "scale"
    )
    this.graphicsLayer(scaleX = scale, scaleY = scale)
        .clickable(interactionSource, null) { }
}
```

### Shared Element Transition (Compose + MD3E)

```kotlin
@Composable
fun SharedElementDemo() {
    var selected by remember { mutableStateOf<Item?>(null) }
    val sharedTransitionScope = rememberSharedContentState()

    AnimatedContent(
        targetState = selected,
        transitionSpec = {
            ContentTransform(
                targetContentEnter = sharedContentEnterTransition(
                    sharedContentState = sharedTransitionScope
                ),
                initialContentExit = sharedContentExitTransition(
                    sharedContentState = sharedTransitionScope
                )
            ).using(SizeTransform(clip = false))
        }
    ) { item ->
        if (item == null) {
            GridView(
                items = items,
                onItemClick = { selected = it },
                sharedTransitionScope = sharedTransitionScope
            )
        } else {
            DetailView(
                item = item,
                onBack = { selected = null },
                sharedTransitionScope = sharedTransitionScope
            )
        }
    }
}
```

## Wear OS 6 Specifics

| Token | Value |
|-------|-------|
| Edge-hugging button radius | `full` (pill) |
| Arc text layout | Custom canvas draw with `drawTextAlongArc()` |
| Shape morphing | Use `animateFloatAsState` on shape parameters |
| Surface container | `surfaceContainerLowest` for round screen backgrounds |
| Spring stiffness | `StiffnessMediumLow` (300) for comfortable wrist motion |

## All M3 Components (m3.material.io/components)

| Category | Components |
|----------|-----------|
| Actions | Button, TextButton, OutlinedButton, ElevatedButton, FilledTonalButton, **SplitButton**, **ButtonGroup**, FAB, SmallFAB, LargeFAB, ExtendedFAB, IconButton |
| Communication | Badge, Snackbar, Banner, Tooltip, **LoadingIndicator** |
| Containment | Card, ElevatedCard, OutlinedCard, BottomSheet, ModalBottomSheet |
| Content | ListItem, Divider |
| Data display | **ProgressIndicator** (linear + circular + waveform), Slider, RangeSlider |
| Data input | TextField, OutlinedTextField, Checkbox, Switch, RadioButton, Chips, SegmentedButton |
| Date & time | DatePicker, DateRangePicker, TimePicker, TimeInput |
| Navigation | NavigationBar, NavigationRail, NavigationDrawer, TabRow, **TopAppBar**, **FloatingToolbar**, Carousel |
| Overlays | Dialog, AlertDialog, DropdownMenu, SearchBar, DockedSearchBar |

**Bold** = New or significantly updated in MD3E.

## Component Variant Reference

| Base Component | Standard Variant | Expressive Variant |
|---------------|-------------------|---------------------|
| Button | RoundedCornerShape(20.dp) | TaperedRect or Squircle |
| Card | Rectangle corners (8dp) | Rounded corners (16dp) + elevation spring |
| FAB | Circle (40dp) | Squircle (56dp) |
| Bottom Sheet | Top corners rounded (16dp) | Arc-shape top edge + spring snap |
| Navigation Bar | Flat icons | Morphing icons + animated indicator |
| Tab Row | Flat indicator | Spring-animated elastic indicator |
| Text Field | Underlined | Container shape + animated label |
| Dialog | Rounded corners (28dp) | Organic/blob shape |
| Slider | Thumb circle | Thumb polygon or Squircle |
| Switch | Capsule shape | Tapered capsule |
| Progress | Linear | Linear + animated label spring |
| Search Bar | Rounded (28dp) | Squircle with morphing results |

## Best Practices

1. **Motion first** — default to spring physics, not duration-based. Use `expressive()` motion scheme for most apps.
2. **5 color max** — don't use more than 5 key colors (primary, secondary, tertiary, neutral, neutral variant).
3. **Tonal harmony** — pick key colors that share similar hue or tone for cohesion.
4. **Contrast** — ensure `onColor`/`color` meets WCAG AA (4.5:1 for text, 3:1 for large text/UI).
5. **Dynamic color** — always provide a non-dynamic fallback for pre-Android 12 devices.
6. **Emphasized typography** — use sparingly for emotional moments only, not for all text.
7. **Shape proportion** — shapes should not distort layout; clip to content bounds.
8. **Wear OS** — edge-hugging layout with pill-shaped buttons, no overlapping interactive zones.
9. **Accessibility** — expanded hit targets (min 48dp), high-contrast mode support, font scaling.
10. **Consistency** — if using MD3E expressive, use it throughout. Don't mix M2 and M3 components.
