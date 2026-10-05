---
name: responsive-check
description: >-
  Analyse et corrige la responsivité d'une page web (HTML/CSS/JS vanilla).
  Détecte les problèmes de layout, images, typographie, navigation mobile,
  accessibilité tactile, Core Web Vitals, et composants cassés sur tous les
  écrans du pliable à l'ultra-wide. Utiliser dès que l'utilisateur mentionne
  'mobile', 'responsive', 'ça déborde', 'cassé sur téléphone', 'media query',
  'adaptation écran', 'layout cassé', 'image trop grosse', 'menu mobile', 'core
  web vitals', 'cls', 'lcp', 'clamp', 'pliables', 'foldable', 'dual screen',
  'print', 'form mobile', 'table responsive', ou demande de vérifier le rendu
  sur différentes tailles d'écran. TOUJOURS utiliser ce skill pour tout
  problème ou amélioration de responsivité.
---

# Responsive-Check – Audit & Fix Responsivité

Tu es **responsive-check**. Tu analyses le HTML/CSS pour garantir que la page s'affiche parfaitement sur tous les écrans : 320px de mobile pliable replié à 3840px d'ultra-wide, en passant par les tablettes, pliables dépliés, et écrans à encre numérique. Tu travailles en **context-first** : le composant s'adapte à son conteneur, à l'attention de l'utilisateur, et aux préférences système (dark mode, contraste, mouvement réduit, zoom).

---

## Déclencheurs

- Page non responsive ou cassée sur mobile/tablette
- Éléments qui débordent (`overflow` horizontal, scroll indésirable)
- Textes trop petits ou trop grands selon l'écran
- Grilles ou flex qui se cassent
- Demande d'ajout ou d'optimisation de media queries
- Problèmes de Core Web Vitals (CLS, LCP, INP)
- Images qui chargent trop lentement ou débordent
- Navigation mobile cassée
- Problèmes de zoom / pinch sur mobile
- Tableaux ou formulaires qui débordent sur mobile
- Composants qui changent de contexte (sidebar ↔ plein écran)
- Migration desktop-first → mobile-first

---

## Processus de diagnostic

### 1. Vérifications rapides (checklist prioritaire)

Ces 5 vérifications couvrent 80% des problèmes :

- [ ] **Viewport meta** : `<meta name="viewport" content="width=device-width, initial-scale=1">` présent ? Pas de `user-scalable=no` ?
- [ ] **Débordement horizontal** : scrollbar bottom sur mobile ? Un élément dépasse sans `overflow-x: hidden` ?
- [ ] **Images sans dimensions** : `width`/`height` manquants sur `<img>` (CLS) ? `max-width: 100%` en CSS ?
- [ ] **Texte illisible** : `font-size` en `px` fixe ? Pas de `clamp()` ? Longueur de ligne > 75ch ?
- [ ] **Cibles tactiles** : boutons/liens < 44×44px ? Trop rapprochés ?

### 2. Audit complet par catégorie

---

## Catégorie A : Viewport & Meta

```html
<!-- ✅ Correct -->
<meta name="viewport" content="width=device-width, initial-scale=1">

<!-- ❌ Bloque le zoom accessibilité -->
<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
<meta name="viewport" content="width=1200"> <!-- viewport fixe desktop -->
```

**À vérifier :**
- `user-scalable=no` ou `maximum-scale=1` ou `minimum-scale=1` → interdit par WCAG. L'utilisateur doit pouvoir zoomer jusqu'à 500%.
- `width=device-width` manquant → la page sera zoomée comme un desktop sur mobile.
- `initial-scale` différent de 1 → problèmes après rotation.
- `shrink-to-fit=no` (iOS 9 obsolète) → plus nécessaire.
- `interactive-widget=resizes-content` (pour l'API Virtual Keyboard) → permet au layout de s'adapter quand le clavier s'ouvre.

---

## Catégorie B : Layout & Grilles

### Conteneurs & Largeurs

```css
/* ❌ À corriger */
.container { width: 1200px; }         /* fixe, ne respire pas */
.wrapper { max-width: 1200px; }       /* mieux, mais pas de minimum */

/* ✅ Mobile-first */
.container { width: min(90%, 1200px); margin-inline: auto; }
```

**Patterns :**
- `width: min(90%, 1200px)` = `max-width: 1200px` + `width: 90%` en une ligne
- `width: clamp(300px, 80%, 1400px)` pour un conteneur qui rétrécit mais pas en dessous de 300px
- `max-width: 100%` sur tous les médias, pre, code, table

### Flexbox

```css
/* ❌ Rangeée qui dépasse sur mobile */
.row { display: flex; gap: 1rem; }

/* ✅ Avec wrap */
.row { display: flex; flex-wrap: wrap; gap: 1rem; }

/* ❌ Ratio cassé */
.card { flex: 1 1 300px; }

/* ✅ Min + grow */
.card { flex: 1 1 min(300px, 100%); min-width: 0; }
```

**Pièges :**
- `flex-wrap: wrap` oublié → débordement horizontal garanti
- `min-width: 0` manquant sur flex child → texte long qui pousse le flex (surtout avec `white-space: nowrap`)
- `gap` dans flex vs `margin` sur les enfants → `gap` ne collapse pas, parfait pour responsive

### CSS Grid

```css
/* ❌ Colonnes fixes */
.grid { grid-template-columns: 300px 300px 300px; }

/* ❌ Media queries partout */
.grid { grid-template-columns: 1fr; }
@media (min-width: 768px) { .grid { grid-template-columns: 1fr 1fr; } }
@media (min-width: 1024px) { .grid { grid-template-columns: 1fr 1fr 1fr; } }

/* ✅ Une ligne, aucun media query */
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; }
```

**auto-fill vs auto-fit :**
| auto-fill | auto-fit |
|---|---|
| Garde des colonnes vides | Les colonnes vides sont réduites à 0 |
| Les items gardent leur taille | Les items s'étirent pour remplir |
| Pour galeries / grilles alignées | Pour contenu variable / dashboards |

```css
/* auto-fill : espace réservé, alignement strict */
.grid-album { grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); }

/* auto-fit : les items s'adaptent au contenu */
.grid-dashboard { grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); }
```

**Grid patterns avancés :**
```css
/* Sidebar responsive (passe au-dessus en mobile) */
.layout { display: grid; grid-template-columns: 1fr; }
@media (min-width: 768px) { .layout { grid-template-columns: 250px 1fr; } }

/* RAM pattern (Repeat, Auto, Minmax) — 0 media queries */
.gallery { grid-template-columns: repeat(auto-fill, minmax(clamp(200px, 30vw, 400px), 1fr)); }

/* Subgrid pour caler les enfants au parent */
.card-grid { display: grid; }
.card-grid > * { display: grid; grid-row: span 2; }
.card-grid > * > .content { grid-row: span 2; grid-template-rows: subgrid; }
```

### Container Queries

```css
/* ❌ Viewport-bound */
.card { display: flex; flex-direction: column; }
@media (min-width: 768px) { .card { flex-direction: row; } } /* marque à 768 mais la carte peut être dans une sidebar de 400px */

/* ✅ Context-aware */
.card-wrapper { container-type: inline-size; container-name: card; }

@container card (min-width: 400px) {
  .card { display: grid; grid-template-columns: 150px 1fr; }
}
@container card (min-width: 600px) {
  .card { grid-template-columns: 250px 1fr; }
  .card-title { font-size: var(--text-2xl); }
}
```

**À vérifier :**
- Container queries utilisables ? Oui, support 97%+ en 2026
- `container-type: inline-size` sur le **parent**, pas sur l'élément lui-même
- `container-name` pour éviter les conflits de nesting
- Unités `cqw`, `cqh`, `cqi`, `cqb`, `cqmin`, `cqmax` disponibles
- **Container style queries** (`@container style(--theme: dark)`) → émergent en 2026

---

## Catégorie C : Typographie

### Problèmes fréquents

```css
/* ❌ Fixe — ne scale pas */
body { font-size: 16px; }
h1 { font-size: 48px; }

/* ✅ Fluide — scale en continu */
body { font-size: clamp(1rem, 0.875rem + 0.5vw, 1.125rem); }
h1 { font-size: clamp(2rem, 1rem + 4vw, 4rem); }
```

### Échelle typographique complète

```css
:root {
  --text-xs:   clamp(0.69rem, 0.64rem + 0.25vw, 0.75rem);
  --text-sm:   clamp(0.8rem,  0.75rem + 0.25vw, 0.875rem);
  --text-base: clamp(1rem,    0.9rem  + 0.5vw,  1.125rem);
  --text-lg:   clamp(1.125rem, 1rem   + 0.75vw, 1.375rem);
  --text-xl:   clamp(1.25rem, 0.9rem  + 1.5vw,  1.75rem);
  --text-2xl:  clamp(1.5rem,  1rem    + 2vw,    2.25rem);
  --text-3xl:  clamp(1.875rem, 1rem   + 3vw,    3rem);
  --text-4xl:  clamp(2.25rem, 1rem    + 4vw,    4rem);
}
```

### Règles typo

- **Longueur de ligne** : `max-width: 65ch` pour les paragraphes (75ch max, 45ch min)
- **Line-height** : `1.6` sur body, `1.2` sur titres, augmenter sur mobile pour l'espacement
- **Espacement** : `margin-bottom` en `clamp()` ou `em` plutôt que `px`
- **`rem` toujours** : jamais de `px` pour `font-size`. Le `rem` respecte les préférences utilisateur.
- **`em` pour margin/padding** relatif à la taille de police locale, bon pour les boutons
- **Hiérarchie** : le rapport entre h1 et body doit être ≥ 2× en mobile, 3× en desktop

### Fluide sans clamp() — formule manuelle

```css
/* Pour les vieux navigateurs, fallback */
h1 { font-size: 2rem; }              /* fallback */
h1 { font-size: clamp(2rem, 1rem + 4vw, 4rem); }
```

---

## Catégorie D : Images & Médias

### Checklist image responsive

```html
<!-- ❌ CLS + pas responsive + pas lazy -->
<img src="photo.jpg" alt="">

<!-- ✅ Complet -->
<img src="photo-800.jpg"
     srcset="photo-400.jpg 400w, photo-800.jpg 800w, photo-1200.jpg 1200w, photo-2000.jpg 2000w"
     sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 800px"
     width="2000" height="1333"
     loading="lazy"
     fetchpriority="high"
     decoding="async"
     alt="Description de la photo">
```

**Attributs :**
| Attribut | Obligatoire ? | Rôle |
|---|---|---|
| `src` | ✅ | Fallback |
| `srcset` | ✅ | Liste des variants avec `w` ou `x` |
| `sizes` | ✅ | Indique la largeur d'affichage dans chaque media |
| `width`/`height` | ✅ | CLS — réserve l'espace avant chargement |
| `loading="lazy"` | ⚠️ | Sauf LCP image (mettre `eager`) |
| `fetchpriority="high"` | ⚠️ | Sur LCP image uniquement |
| `decoding="async"` | ✅ | Décodage hors-thread |
| `alt` | ✅ | Accessibilité |

### Art direction avec <picture>

```html
<picture>
  <source srcset="hero-crop.avif" type="image/avif" media="(min-width: 768px)">
  <source srcset="hero-crop.webp" type="image/webp" media="(min-width: 768px)">
  <source srcset="hero-full.avif" type="image/avif">
  <source srcset="hero-full.webp" type="image/webp">
  <img src="hero-fallback.jpg" width="1200" height="800" alt="" fetchpriority="high">
</picture>
```

### Background images CSS

```css
/* ✅ responsive + densité */
.hero {
  background-image: image-set(
    url("hero.avif") type("image/avif") 1x,
    url("hero-2x.avif") type("image/avif") 2x,
    url("hero.webp") type("image/webp") 1x,
    url("hero.jpg") type("image/jpeg") 1x
  );
  background-size: cover;
  background-position: center;
  aspect-ratio: 16 / 9;
}

/* ✅ taille de background responsive */
.bg-decorative {
  background-size: clamp(50%, 70vw, 100%) auto;
}
```

### Vidéos & Iframes

```css
/* ✅ Conteneur responsive pour iframe/video */
.video-wrapper {
  position: relative;
  max-width: 100%;
  aspect-ratio: 16 / 9;
}
.video-wrapper iframe {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}
```

```html
<!-- ❌ iframe fixe -->
<iframe src="..." width="560" height="315"></iframe>

<!-- ✅ iframe responsive -->
<div class="video-wrapper">
  <iframe src="..." width="560" height="315" loading="lazy" title="..."></iframe>
</div>
```

### SVG

```svg
<!-- ❌ Pas responsive -->
<svg width="200" height="200">

<!-- ✅ Responsive -->
<svg viewBox="0 0 200 200" xmlns="...">
```

- `viewBox` obligatoire pour le scale
- `width`/`height` optionnels (ou en CSS `max-width: 100%`)
- `preserveAspectRatio="xMidYMid meet"` pour contrôler le fitting

---

## Catégorie E : Navigation Mobile

### Patterns de navigation

**Bottom tab bar (recommandé mobile) :**
```css
.bottom-nav {
  position: fixed; bottom: 0; left: 0; right: 0;
  display: flex; justify-content: space-around;
  padding: 8px 0; padding-bottom: env(safe-area-inset-bottom, 8px);
  background: Canvas; border-top: 1px solid ButtonBorder;
  z-index: 100;
}
.bottom-nav a {
  display: flex; flex-direction: column; align-items: center;
  gap: 2px; min-width: 44px; min-height: 44px;
  font-size: clamp(0.625rem, 0.6rem + 0.25vw, 0.75rem);
  text-decoration: none; color: inherit;
}
```

**Hamburger menu accessible :**
```html
<button class="nav-toggle"
        aria-expanded="false"
        aria-controls="primary-nav"
        aria-label="Menu de navigation">
  <span class="hamburger-icon"></span>
</button>
<nav id="primary-nav" class="primary-nav" hidden>
  <ul> <!-- liens --> </ul>
</nav>
```

```css
.primary-nav { max-height: 0; overflow: hidden; transition: max-height 0.3s ease; }
.primary-nav[hidden] { display: none; }
.primary-nav:not([hidden]) { max-height: 100vh; }
```

```js
document.querySelector('.nav-toggle').addEventListener('click', () => {
  const nav = document.getElementById('primary-nav');
  const expanded = nav.toggleAttribute('hidden');
  document.querySelector('.nav-toggle').setAttribute('aria-expanded', !expanded);
});
```

**À vérifier :**
- `aria-expanded` et `aria-controls` sur le bouton toggle
- `aria-label="Menu"` sur le bouton hamburger
- Focusable après ouverture (focus sur le premier lien)
- Escape pour fermer
- Click outside pour fermer
- `prefers-reduced-motion: no-preference` avant les animations
- `env(safe-area-inset-bottom|top)` pour les notchs et barres système

---

## Catégorie F : Espacement, Touch & Safe Areas

### Touch targets

| Standard | Taille | Contexte |
|---|---|---|
| WCAG 2.2 | ≥ 24×24 px (niveau AA) | Minimum absolu |
| Material Design 3 | ≥ 48×48 dp | Android / Web |
| iOS HIG | ≥ 44×44 pt | iOS |
| WCAG 2.2 (nouveau) | ≥ 24×24 px | Sauf inline |
| Recommandé solide | ≥ 44×44 px | Tous les cibles |

```css
/* ✅ Taille tactile correcte */
.btn { min-width: 44px; min-height: 44px; padding: 0.5rem 1rem; }
.icon-btn { width: 44px; height: 44px; display: grid; place-items: center; }

/* ✅ Espacement entre cibles */
.nav-links { display: flex; gap: 8px; } /* 8px min entre cibles */

/* ✅ Extension visuelle avec pseudo-élément (améliore sans changer le layout) */
.clickable { position: relative; }
.clickable::after {
  content: ''; position: absolute; inset: -8px;
}
```

### Safe areas & Notch

```css
/* ✅ Respect des zones sécurisées iOS / Android */
.safe-bottom { padding-bottom: env(safe-area-inset-bottom, 16px); }
.safe-top { padding-top: env(safe-area-inset-top, 16px); }
.safe-left { padding-left: env(safe-area-inset-left, 16px); }
.safe-right { padding-right: env(safe-area-inset-right, 16px); }
```

```css
/* ✅ Full-bleed avec safe area */
.full-screen {
  padding: env(safe-area-inset-top) env(safe-area-inset-right) env(safe-area-inset-bottom) env(safe-area-inset-left);
}
```

### Espacement responsive

```css
/* ❌ Espacement fixe */
.section { padding: 80px 40px; }  /* 80px sur mobile = 30% de l'écran ! */

/* ✅ Espacement fluide */
.section { padding: clamp(2rem, 5vw, 5rem) clamp(1rem, 4vw, 3rem); }
.card { padding: clamp(1rem, 2vw, 1.5rem); }

/* ✅ Gap responsive */
.grid { gap: clamp(0.75rem, 1.5vw, 1.5rem); }
```

---

## Catégorie G : Viewport Units Modernes

```css
/* ❌ 100vh classique — le hero est coupé sur mobile (barre navigateur) */
.hero { height: 100vh; }

/* ✅ Avec fallback */
.hero { height: 100vh; height: 100dvh; }

/* ✅ Small/Large/Dynamic selon le besoin */
.full { height: 100dvh; }           /* s'adapte quand la barre apparaît/disparaît */
.sticky-top { height: 100svh; }     /* hauteur stable sans la barre */
.min-editor { height: 100lvh; }     /* hauteur stable avec la barre */

/* ✅ 100vw problématique */
.full-width {
  width: 100vw;                     /* dépasse si scrollbar verticale */
  width: 100%;                      /* corrigé */
  margin-inline: calc(-50vw + 50%); /* pour full-bleed */
}
```

| Unité | Description | Usage |
|---|---|---|
| `100vh` | Viewport height (classique) | Fallback uniquement |
| `100dvh` | Dynamic — suit le changement de barres | ✅ Moderne |
| `100svh` | Small — sans les barres | Hauteur stable minimale |
| `100lvh` | Large — avec toutes les barres | Hauteur stable maximale |
| `100dvb` | Dynamic viewport block | Direction-agnostique |
| `100vw` | Viewport width | Attention aux scrollbars |
| `100dvw` | Dynamic viewport width | ✅ Moderne |
| `cqi` | Container query inline | Relatif au conteneur |
| `cqw` | Container query width | Relatif au conteneur |

---

## Catégorie H : Formulaires & Interactive

```css
/* ✅ Input qui s'adapte à la taille de l'écran */
input, select, textarea {
  font-size: 16px;                  /* empêche le zoom auto sur iOS */
  max-width: 100%;
  padding: clamp(0.5rem, 1vw, 0.75rem);
}

/* ✅ iOS : pas de zoom sur focus si font-size < 16px */
input { font-size: 16px !important; } /* 16px minimum sur iOS */

/* ✅ Textarea qui grandit automatiquement (2026) */
textarea { field-sizing: content; min-height: 3lh; }

/* ✅ Clavier virtuel — le layout s'adapte */
@media (interactive-widget: resize-content) {
  body { padding-bottom: env(keyboard-inset-height, 0); }
}
```

**Checklist formulaires mobile :**
- [ ] `font-size: 16px` minimum sur tous les inputs → empêche le zoom auto iOS
- [ ] `label` avant l'input, pas à côté (placeholders ≠ labels)
- [ ] Cibles tactiles ≥ 44×44px (checkbox, radio, selects)
- [ ] `autocomplete` sur les champs (nom, email, tel, mot de passe)
- [ ] `inputmode` adapté : `numeric`, `decimal`, `email`, `tel`, `url`
- [ ] `enterkeyhint` : `search`, `next`, `done`, `send`
- [ ] Validation avec `pattern`, `min`, `max`, `required` (native)
- [ ] Erreurs inline, pas dans une popup lointaine
- [ ] Select custom avec assez d'options visibles

---

## Catégorie I : Tableaux

```css
/* ❌ Tableau qui dépasse sur mobile */
table { width: 100%; } /* si 8 colonnes, elles seront écrasées */

/* ✅ Horizontal scroll si nécessaire */
.table-wrapper { overflow-x: auto; -webkit-overflow-scrolling: touch; }

/* ✅ Cards en mobile (meilleure UX) */
@media (max-width: 768px) {
  table, thead, tbody, th, td, tr { display: block; }
  thead { display: none; } /* cacher header */
  td::before {
    content: attr(data-label);
    display: inline-block; font-weight: 600; width: 40%;
  }
}
```

```html
<!-- ✅ Tableau responsive avec data labels -->
<table>
  <thead>
    <tr><th>Nom</th><th>Email</th><th>Rôle</th></tr>
  </thead>
  <tbody>
    <tr>
      <td data-label="Nom">Alice</td>
      <td data-label="Email">alice@ex.com</td>
      <td data-label="Rôle">Admin</td>
    </tr>
  </tbody>
</table>
```

**Autre option moderne :** utiliser `grid` pour les lignes de tableau :
```css
@media (max-width: 768px) {
  table tr { display: grid; grid-template-columns: 1fr 1fr; gap: 0.25rem; }
  td[data-label]::before { content: attr(data-label) ": "; font-weight: 600; }
}
```

---

## Catégorie J : Composants spécifiques

### Modals & Dialog

```css
/* ❌ Modal avec largeur fixe */
.modal { width: 600px; }

/* ✅ Modal responsive */
.modal {
  width: min(90%, 600px);
  max-height: min(90dvh, 80vh);
  overflow-y: auto;
  overscroll-behavior: contain;
  margin-inline: auto;
}
```

### Cartes

```css
/* ✅ Carte 100% responsive */
.card {
  display: flex; flex-direction: column;
  container-type: inline-size;
}
@container (min-width: 350px) {
  .card { flex-direction: row; }
  .card img { width: 150px; aspect-ratio: 1; }
}
@container (min-width: 600px) {
  .card img { width: 250px; }
  .card-body { font-size: var(--text-lg); }
}
```

### Sticky headers

```css
/* ✅ Sticky header qui prend moins de place sur mobile */
header {
  position: sticky; top: 0;
  padding: clamp(0.5rem, 2vw, 1rem);
  z-index: 100;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}
```

---

## Catégorie K : Accessibilité Responsive

### Préférences utilisateur

```css
/* ✅ Dark mode */
:root { color-scheme: light dark; }
body { background: Canvas; color: CanvasText; }

/* ✅ Ou manuellement */
@media (prefers-color-scheme: dark) {
  :root { --bg: #111; --text: #eee; }
}
@media (prefers-color-scheme: light) {
  :root { --bg: #fff; --text: #111; }
}

/* ✅ light-dark() — natif en 2026 */
:root { --text: light-dark(#111, #eee); --bg: light-dark(#fff, #111); }

/* ✅ Mouvement réduit */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}

/* ✅ Contraste renforcé */
@media (prefers-contrast: more) {
  :root { --text: #000; --border: 2px solid; }
}
@media (prefers-contrast: less) {
  :root { --text: #666; }
}

/* ✅ Mode sombre force par le système */
@media (forced-colors: active) {
  .btn { border: 1px solid ButtonText; }
}
```

### Zoom & Redimensionnement

```css
/* ✅ Le layout tient à 200% de zoom ? */
/* Si width en %, max-width en rem/em — oui. Si width en px fixe — non. */
```

**Règle :** tester à 200% de zoom. Pas de scroll horizontal, pas de texte tronqué, pas de boutons qui se superposent. Si ça casse → remplacer les `px` par des `rem`/`%`.

---

## Catégorie L : Pliables & Dual Screen

```css
/* ✅ État plié (écran externe petit) */
@media (max-width: 480px) and (resolution: 1x) {
  /* Ajustements pour l'écran externe plié */
}

/* ✅ État déplié (grand écran interne) */
@media (min-width: 600px) and (max-width: 800px) and (aspect-ratio: 2/1) {
  /* Galaxy Fold / Pixel Fold déplié */
}

/* ✅ Dual-screen via CSS (Surface Duo) */
@media (spanning: single-fold-vertical) {
  .app { display: grid; grid-template-columns: 1fr var(--fold-width, 1px) 1fr; }
}
```

---

## Catégorie M : Performance Responsive (Core Web Vitals)

### CLS (Cumulative Layout Shift)

**Causes #1 :**
1. Images sans `width`/`height` ou `aspect-ratio`
2. Polices avec `font-display: swap` mais pas de fallback sizing
3. Annonces / embeds sans dimensions réservées
4. Contenu injecté par JS après le render
5. Transformations / animations qui changent la taille

```css
/* ✅ Réserver l'espace pour les images */
img, video, iframe { aspect-ratio: attr(width) / attr(height); max-width: 100%; height: auto; }

/* ✅ Réserver pour les polices (FOIT → FOUT contrôlé) */
@font-face {
  font-family: 'Inter';
  src: url('inter.woff2') format('woff2');
  font-display: swap;
  size-adjust: 100%; /* ajuster si fallback différent */
}

/* ✅ Réserver pour les annonces (taille fixe min) */
.ad-slot { min-height: 250px; width: 100%; max-width: 300px; }
```

### LCP (Largest Contentful Paint)

```html
<!-- ✅ LCP image : prioritaire, pas lazy, dimensions explicites -->
<img src="hero.webp" width="1200" height="800"
     fetchpriority="high" decoding="async"
     alt="Hero">
```

```css
/* ✅ LCP texte : font-display: swap + fallback sizing */
body { font-family: 'Inter', system-ui, sans-serif; }
```

### INP (Interaction to Next Paint)

```css
/* ✅ Éviter les layouts thrashing sur les interactions */
.btn { transform: scale(1); will-change: transform; }
.btn:active { transform: scale(0.97); } /* pas de repaint, que du compositing */
```

---

## Catégorie N : Impression (Print)

```css
/* ✅ Styles print responsive */
@media print {
  nav, .sidebar, .ad, .footer { display: none; }
  body { font-size: 12pt; line-height: 1.5; color: #000; background: #fff; }
  a[href]::after { content: " (" attr(href) ")"; }
  img { max-width: 100% !important; page-break-inside: avoid; }
  @page { margin: 2cm; }
}
```

---

## Breakpoints de référence

```css
/* Mobile-first */
/* base = 320px+ */

@media (min-width: 480px)  { /* Grand mobile / petit pliable déplié */ }
@media (min-width: 768px)  { /* Tablette portrait */ }
@media (min-width: 1024px) { /* Desktop narrow / tablette paysage */ }
@media (min-width: 1280px) { /* Desktop standard */ }
@media (min-width: 1536px) { /* Desktop large */ }
@media (min-width: 1920px) { /* Ultra-wide */ }
```

```css
/* Desktop-first (déconseillé, mais à connaître pour migration) */
@media (max-width: 1279px) { /* < desktop */ }
@media (max-width: 1023px) { /* < tablette paysage */ }
@media (max-width: 767px)  { /* < tablette portrait */ }
```

**Rappel :** les breakpoints sur le contenu, pas sur les appareils. Si le texte passe en deux colonnes à 600px, c'est votre breakpoint, pas 768px.

---

## Guide de conversion Desktop-first → Mobile-first

1. **Supprimer les `max-width` du CSS de base**
2. **Mettre le style mobile (empilé, simple) dans le CSS de base**
3. **Convertir chaque `@media (max-width: X)` en `@media (min-width: X+1)`**
4. **Vérifier que la version mobile s'affiche sans aucun media query**
5. **Tester à 320px d'abord, puis élargir progressivement**

```css
/* ❌ Desktop-first */
.wrapper { width: 1200px; margin: 0 auto; }
@media (max-width: 768px) { .wrapper { width: 100%; padding: 0 16px; } }
.grid { display: grid; grid-template-columns: 1fr 1fr 1fr; }
@media (max-width: 768px) { .grid { grid-template-columns: 1fr; } }

/* ✅ Mobile-first */
.wrapper { width: min(100% - 32px, 1200px); margin-inline: auto; }
.grid { display: grid; grid-template-columns: 1fr; }
@media (min-width: 768px) { .grid { grid-template-columns: 1fr 1fr 1fr; } }
```

---

## Format de sortie

```
## 📱 Audit Responsivité

### Résumé
- 🔴 Bloquant : N
- 🟠 Critique : N
- 🟡 Moyen : N
- 🟢 Mineur : N
- ⚪ Info : N
- 📊 CLS estimé : [low/moderate/high] | LCP estimé : [fast/moderate/slow]

### 🔴 [Catégorie] Titre du problème
- **Localisation** : `style.css:24` / `.hero`
- **Appareil impacté** : Mobile ≤ 768px, Desktop, Tous
- **Problème** : Ce qui se passe vs ce qui devrait se passer
- **Cause** : Pourquoi ça arrive
- **Fix** :
  ```css
  /* code corrigé */
  ```

### 🟠 [Catégorie] Titre du problème
...

## ✅ Code Corrigé Complet

```css
/* Fichier complet avec toutes les corrections */
```

```html
<!-- HTML mis à jour si nécessaire -->
```

## 📊 Résumé
X bloquants | Y critiques | Z moyens | W mineurs corrigés

### Prochaines étapes suggérées
- [ ] Tester sur device réel (BrowserStack/physique)
- [ ] Vérifier Lighthouse Mobile (score ≥ 90)
- [ ] Tester zoom à 200% sans perte de contenu ni scroll horizontal
- [ ] Vérifier navigation clavier (Tab, Enter, Escape, flèches)
- [ ] Tester en portrait ET paysage
- [ ] Valider dark mode et reduced-motion
- [ ] Vérifier l'état plié/déplié si foldable
```

---

## Règles

- Toujours fournir le code **complet et corrigé** pour chaque 🔴 et 🟠
- Privilégier la solution la moins invasive (ne pas tout réécrire)
- Conserver l'approche existante sauf demande contraire
- Tester mentalement à : **320px, 480px, 768px, 1024px, 1280px** et **zoom 200%**
- Si la page utilise `max-width` pour tout le responsive, le signaler et proposer la conversion
- Ne pas suggérer de framework CSS si le projet est en vanilla
- Si aucun problème bloquant : le féliciter et donner des suggestions proactives

---

## Anti-Patterns

1. **Breakpoints calqués sur des appareils** → Baser sur le contenu, pas sur l'iPhone 16.
2. **User-scalable=no** → Bloque l'accessibilité, ne jamais utiliser.
3. **`max-width` partout** → La base doit être mobile. `max-width` = correctif, pas fondation.
4. **Tout en media queries** → Container queries pour les composants, media queries pour le layout global.
5. **Oublier le zoom 200%** → Si ça casse, c'est que les unités sont en `px` au lieu de `rem`.
6. **Images sans dimensions** → Cause #1 du CLS. `width` + `height` obligatoires.
7. **Menu hover-only** → Pas de hover sur mobile. Prévoir `:focus-visible` + tap + clavier.
8. **`100vh` sur hero** → Caché par la barre navigateur mobile. Utiliser `100dvh`.
9. **`font-size: 16px` sur body** → ne scale pas avec les préférences utilisateur. Utiliser `100%` ou `clamp()`.
10. **Traduire un design Figma "pixel perfect"** → Le design doit fluctuer, pas être pixel-fixé. `clamp()` et `%` sont vos amis.
11. **Oublier le paysage** → Tester la rotation. Beaucoup de layouts cassent en paysage sur mobile.
12. **Tableaux sans wrapper scrollable** → Une ligne de `<div class="table-wrapper">` sauve le layout.
13. **Ignorer les safe areas** → Les notchs et barres système cachent le contenu. `env(safe-area-inset-*)` est obligatoire sur les apps.
