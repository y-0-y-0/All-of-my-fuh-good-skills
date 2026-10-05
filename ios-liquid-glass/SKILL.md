---
name: ios-liquid-glass
description: >-
  Use ONLY when the user asks for iOS 26 Liquid Glass UI, SwiftUI glass effects, .glassEffect() modifier, glass button styles, sheet presentations with material backgrounds, tab bar glass, scroll edge effects, search with materials, glass effect container, pickers with glass, system glass components (alert, menu, confirmationDialog), fluid morphing animation, material hierarchy (ultraThin/thin/regular/thick), toolbar grouping, or any web/React transposition. Patterns: "liquid glass", "glass effect", "SwiftUI glass", "iOS 26 UI", "glass morphism", "backdrop-filter glass", "toolbar glass", "tab bar glass", "sheet verre", "glass button", "morphing animation", "ultraThinMaterial", "thinMaterial", "regularMaterial", "thickMaterial", "SF Symbol", "Chapter 1..16".
  Activate for ANY task producing iOS 26 Liquid Glass UI in SwiftUI or a faithful web/React/CSS transposition.
  If the user mentions iOS 26 glass UI without triggering the description, load it anyway.
---

# iOS 26 Liquid Glass — Design System

Source: `C:\Users\élève\Downloads\LiquidGlass-Handbook-main` (16 chapter SwiftUI demo app).
All API patterns, chapter metadata, colors, SF Symbols, animations and component code below are extracted **verbatim** from the source files. Web/React transpositions are faithful approximations of the real SwiftUI structure, not invented from scratch.

## Philosophie

Le Liquid Glass est un **matériau système natif iOS 26** qui flotte au-dessus du contenu. Il floute dynamiquement l'arrière-plan, reflète les couleurs environnantes, réagit au toucher/pointeur en temps réel, et peut morphing entre formes. Couleur neutre et caméléon : la teinte vient du fond. Utilisé pour la couche de navigation flottante, pas pour le contenu lui-même.

Test mental : *"Est-ce qu'Apple validerait cette UI dans un mockup iOS 26 ?"* Si non, refais.

## Modèle de chapitre (réel — `Models/Chapter.swift:10`)

```swift
struct Chapter: Identifiable {
    let id: Int
    let title: String
    let subtitle: String
    let icon: String        // SF Symbol
    let color: Color
}

extension Chapter: Hashable {           // SwiftUI NavigationLink(value:) requirement
    static func == (lhs: Chapter, rhs: Chapter) -> Bool { lhs.id == rhs.id }
    func hash(into hasher: inout Hasher) { hasher.combine(id) }
}

extension Chapter: Equatable {}
```

## Les 16 chapitres (réels — `Views/TableOfContentsView.swift:11`)

| # | Title | Subtitle | SF Symbol | Color |
|---|---|---|---|---|
| 1 | Toolbar with Liquid Glass | Toolbar buttons with .glass style | `menubar.rectangle` | `.blue` |
| 2 | Glass Button Styles | .glass and .glassProminent styles | `button.programmable` | `.purple` |
| 3 | Sheet Presentations | Sheets with material backgrounds | `square.on.square` | `.mint` |
| 4 | Scroll Edge Effects | Content blur under glass layers | `arrow.up.and.down.text.horizontal` | `.teal` |
| 5 | Tab Bar Glass | Tab bars with glass backgrounds | `square.split.bottomrightquarter` | `.orange` |
| 6 | Glass Effect Modifier | .glassEffect() for custom views | `wand.and.stars` | `.pink` |
| 7 | Liquid Glass Effects | Dynamic translucent glass effects | `sparkles` | `.green` |
| 8 | Search with Materials | Searchable modifier with materials | `magnifyingglass` | `.red` |
| 9 | Glass Effect Container | Group elements with unified glass | `square.stack.3d.forward.dottedline.fill` | `.blue` |
| 10 | Pickers with Glass | Selection controls with glass styling | `slider.horizontal.3` | `.pink` |
| 11 | System Glass Components | Alert, Menu, ConfirmationDialog | `square.grid.3x3.square` | `.teal` |
| 12 | Fluid Morphing Animation | PhaseAnimator with liquid glass | `waveform.path.ecg` | `.purple` |
| 13 | Glass Animations | Auto expand / rotate / merge glass | `waveform.path.ecg` | `.purple` |
| 14 | Glass Overlap | Drag / stack / intersect glass layers | `square.stack.3d.down.right` | `.indigo` |
| 15 | Material Hierarchy | ultraThin / thin / regular / thick | `square.stack.3d.up.fill` | `.cyan` |
| 16 | Toolbar Grouping | ToolbarItemGroup + ToolbarSpacer | `square.grid.3x1.below.line.grid.1x2` | `.indigo` |

## API SwiftUI natives (celles réellement utilisées dans la source)

| API | Source file:line | Usage |
|---|---|---|
| `.glassEffect()` | `Chapters/GlassEffectModifierDemo.swift:110` | Verre par défaut sur n'importe quelle vue |
| `.glassEffect(in: Shape)` | `Chapters/GlassEffectModifierDemo.swift:61` | Verre contraint à une forme |
| `.glassEffect(.regular.tint(.orange).interactive())` | `Chapters/FluidMorphingAnimationDemo.swift:139` | Verre teinté + interactif |
| `.glassEffect(.regular.tint(.blue))` | `Chapters/FluidMorphingAnimationDemo.swift:202` | Verre teinté (sans interactive) |
| `.glassEffect(in: .circle)` | `Chapters/GlassAnimationsDemo.swift:115` | Verre circulaire |
| `.glassEffect(in: RoundedRectangle(cornerRadius: 16))` | `Chapters/GlassEffectContainerDemo.swift:140` | Verre rectangulaire arrondi |
| `.glassEffect(in: .rect(cornerRadius: 16.0))` | `Chapters/FluidMorphingAnimationDemo.swift:56` | Variante statique shape |
| `GlassEffectContainer(spacing: 40.0)` | `Chapters/FluidMorphingAnimationDemo.swift:62` | Groupe unifié pour morphing |
| `GlassEffectContainer(spacing: 20.0)` | `Chapters/FluidMorphingAnimationDemo.swift:83` | Groupe union |
| `GlassEffectContainer(spacing: 12)` | `Chapters/GlassEffectContainerDemo.swift:118` | Groupe compact |
| `GlassEffectContainer(spacing: 0)` | `Chapters/GlassEffectContainerDemo.swift:161` | Liste unifiée sans espacement |
| `.glassEffectID(_:in:)` | `Chapters/FluidMorphingAnimationDemo.swift:68` | Identifie un élément pour morphing |
| `.glassEffectUnion(id:namespace:)` | `Chapters/FluidMorphingAnimationDemo.swift:90` | Union de plusieurs effets |
| `.glassEffectTransition(.matchedGeometry)` | `Chapters/FluidMorphingAnimationDemo.swift:166` | Transition morphing |
| `.buttonStyle(.glass)` | `Chapters/ToolbarGlassDemo.swift:165` | Bouton verre standard |
| `.buttonStyle(.glassProminent)` | `Chapters/SheetGlassDemo.swift:183` | Bouton verre prononcé |
| `.buttonStyle(.glass(.regular))` | `Chapters/GlassButtonStylesDemo.swift:264` | Bouton verre paramétré |
| `.buttonStyle(.borderedProminent)` | `Chapters/SystemGlassComponentsDemo.swift:129` | Bouton standard prominent |
| `.controlSize(.small/.regular/.large)` | `Chapters/GlassButtonStylesDemo.swift:184` | Contrôle de taille |
| `.tabBarMinimizeBehavior(.onScrollDown)` | `Chapters/TabBarGlassDemo.swift:54` | Tab bar se réduit au scroll |
| `.presentationBackground(.ultraThinMaterial)` | `Chapters/SheetGlassDemo.swift:187` | Fond de sheet en verre |
| `.presentationDetents([.medium, .large])` | `Chapters/SheetGlassDemo.swift:188` | Hauteurs de sheet |
| `.presentationDragIndicator(.visible)` | `Chapters/SheetGlassDemo.swift:189` | Indicateur de drag |
| `ToolbarItem(placement: .principal)` | `Chapters/ToolbarGlassDemo.swift:143` | Item central toolbar |
| `ToolbarItem(placement: .topBarTrailing)` | `Chapters/ToolbarGlassDemo.swift:168` | Item à droite toolbar |
| `ToolbarItem(placement: .cancellationAction)` | `Chapters/SheetGlassDemo.swift:172` | Action d'annulation sheet |
| `ToolbarItem(placement: .confirmationAction)` | `Chapters/SheetGlassDemo.swift:179` | Action de confirmation sheet |
| `ToolbarItemGroup(placement: .topBarTrailing)` | `Chapters/ToolbarGroupingDemo.swift:71` | Groupe d'items toolbar |
| `ToolbarSpacer(.flexible, placement:)` | `Chapters/ToolbarGroupingDemo.swift:76` | Espacement flexible |
| `ShareLink(item:)` | `Views/CodeDetailView.swift:41` | Bouton de partage natif |
| `.searchable(text: $text, prompt:)` | `Chapters/SearchGlassDemo.swift:72` | Recherche avec verre |
| `.alert(_:isPresented:)` | `Chapters/SystemGlassComponentsDemo.swift:131` | Alerte verre auto |
| `.confirmationDialog(_:isPresented:)` | `Chapters/SystemGlassComponentsDemo.swift:161` | Dialog verre auto |
| `.contextMenu` | `Chapters/SystemGlassComponentsDemo.swift:248` | Menu contextuel verre |
| `.zIndex(0/1/2)` | `Chapters/GlassAnimationsDemo.swift:166` | Ordre d'empilement glass |

### Contrôle de taille sur boutons verre (réel — `Chapters/GlassButtonStylesDemo.swift:182`)

```swift
Button("Small") {}     .buttonStyle(.glass).controlSize(.small)   // ~ 32px
Button("Regular") {}   .buttonStyle(.glass).controlSize(.regular)  // ~ 36px
Button("Large") {}     .buttonStyle(.glass).controlSize(.large)    // ~ 48px
```

### Matériaux système Apple (réels — `Chapters/MaterialHierarchyDemo.swift:92`)

| Matériau | Usage dans la source | Exemple |
|---|---|---|
| `.ultraThinMaterial` | Fonds de cartes, headers flottants, sheets, code blocks | `ChapterDetailView.swift:49`, `SheetGlassDemo.swift:187` |
| `.thinMaterial` | Boutons, barres d'action, footers flottants, demo containers | `ToolbarGlassDemo.swift:208`, `ScrollEdgeEffectDemo.swift:193` |
| `.regularMaterial` | Menus, pickers | `PickerGlassDemo.swift:136` |
| `.thickMaterial` | Alertes (rare, démo) | `MaterialHierarchyDemo.swift:95` |

## Pattern récurrent : arrière-plan verre + bordure + ombre

Trois variantes trouvées dans la source — toutes équivalentes visuellement :

### Variante A — ultraThinMaterial simple (réel — `Components/ChapterCard.swift:24`)
```swift
HStack(spacing: 16) { /* content */ }
    .padding(18)
    .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 16))
    .overlay(
        RoundedRectangle(cornerRadius: 16)
            .strokeBorder(.white.opacity(0.2), lineWidth: 0.5)
    )
    .shadow(color: .black.opacity(0.08), radius: 12, y: 4)
```

### Variante B — RoundedRectangle.fill avec gradient tint (réel — `Components/ModernChapterCard.swift:98`)
```swift
RoundedRectangle(cornerRadius: 14)
    .fill(.ultraThinMaterial)
    .overlay {
        RoundedRectangle(cornerRadius: 14)
            .fill(
                LinearGradient(
                    colors: [color.opacity(0.05), .clear],
                    startPoint: .topLeading,
                    endPoint: .bottomTrailing
                )
            )
    }
    .overlay {
        RoundedRectangle(cornerRadius: 14)
            .strokeBorder(color.opacity(0.15), lineWidth: 0.5)
    }
    .shadow(color: color.opacity(0.15), radius: 8, y: 4)
```

### Variante C — header avec bordure dégradée colorée (réel — `Views/ChapterDetailView.swift:48`)
```swift
HStack(spacing: 16) { /* content */ }
    .padding(16)
    .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 16))
    .overlay(
        RoundedRectangle(cornerRadius: 16)
            .strokeBorder(
                LinearGradient(
                    colors: [chapter.color.opacity(0.4), chapter.color.opacity(0.1)],
                    startPoint: .leading,
                    endPoint: .trailing
                ),
                lineWidth: 1.5
            )
    )
    .shadow(color: chapter.color.opacity(0.2), radius: 8, x: 0, y: 4)
```

### Variante D — container à gradient color (réel — `Components/ActionButtonsCard.swift:34`)
```swift
.padding(24)
.background(
    RoundedRectangle(cornerRadius: 24)
        .fill(.ultraThinMaterial)
)
.overlay(
    RoundedRectangle(cornerRadius: 24)
        .strokeBorder(Color.white.opacity(0.2), lineWidth: 1)
)
.shadow(color: .black.opacity(0.1), radius: 20, x: 0, y: 10)
```

## Animations issues du code source réel

| Animation | Source file:line | Contexte |
|---|---|---|
| `.spring(response: 0.6, dampingFraction: 0.7)` | `GlassAnimationsDemo.swift:116`, `FluidMorphingAnimationDemo.swift:303` | Morphing de glass / expansion |
| `.spring(response: 0.6)` | `PickerGlassDemo.swift:170` | Sélection couleur picker |
| `.spring()` (defaults) | `GlassAnimationsDemo.swift:179`, `GlassOverlapDemo.swift:105` | Reset drag / merge |
| `.smooth(duration: 0.6)` | `FluidMorphingAnimationDemo.swift:216` | Toggle smooth morphing |
| `.easeInOut(duration: 0.8)` | `GlassAnimationsDemo.swift:140` | Rotation auto |
| `.easeInOut(duration: 0.15)` | `Styles/CardButtonStyle.swift:14` | Pressed state |
| `.easeInOut(duration: 5).repeatForever(autoreverses: true)` | `Components/AnimatedGradientBackground.swift:26` | Gradient animé en boucle |
| Boucle infinie via `.task` | `GlassAnimationsDemo.swift:117`, `Chapters/FluidMorphingAnimationDemo.swift:50` | Auto expanding/merging/rotating |
| Boucle infinie via `.onAppear + withAnimation` | `AnimatedGradientBackground.swift:25` | Gradient background |

```swift
// CardButtonStyle — pattern pressed state (réel — Styles/CardButtonStyle.swift:10)
struct CardButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .scaleEffect(configuration.isPressed ? 0.97 : 1.0)
            .animation(.easeInOut(duration: 0.15), value: configuration.isPressed)
    }
}

// Auto-loop avec .task (réel — Chapters/GlassAnimationsDemo.swift:103)
@State private var isExpanded = false
Color.clear
    .frame(width: isExpanded ? 100 : 60, height: isExpanded ? 100 : 60)
    .glassEffect(in: .circle)
    .animation(.spring(response: 0.6, dampingFraction: 0.7), value: isExpanded)
    .task {
        while !Task.isCancelled {
            try? await Task.sleep(for: .seconds(1.5))
            isExpanded.toggle()
        }
    }

// Toggle smooth morphing (réel — FluidMorphingAnimationDemo.swift:215)
Button(action: {
    withAnimation(.smooth(duration: 0.6)) {
        isExpanded.toggle()
    }
}) { /* label */ }
```

## 16 chapitres — code source réel & transpositions

### Chapter 1 — Toolbar with Liquid Glass (ToolbarGlassDemo.swift)

Pattern : `NavigationStack` + `List` + `.toolbar` avec items conditionnels + `Menu` + `.buttonStyle(.glass)`.

```swift
// ToolbarGlassDemo.swift:142
.toolbar {
    ToolbarItem(placement: .principal) {
        Menu {
            Button(action: { sortOrder = .ascending }) {
                Label("Sort Ascending", systemImage: "arrow.up")
            }
            Button(action: { sortOrder = .descending }) {
                Label("Sort Descending", systemImage: "arrow.down")
            }
            Divider()
            Button(action: { selectAll() }) {
                Label("Select All", systemImage: "checkmark.circle.fill")
            }
        } label: {
            Text("Options")
        }
        .buttonStyle(.glass)
    }

    ToolbarItem(placement: .topBarTrailing) {
        Button(action: { toggleSelecting() }) {
            Label(isSelecting ? "Done" : "Select",
                  systemImage: isSelecting ? "checkmark" : "checkmark.circle")
        }
    }

    if isSelecting && !selectedItems.isEmpty {
        ToolbarItem(placement: .topBarTrailing) {
            Button(action: { starSelectedItems() }) {
                Label("Star", systemImage: "star.fill")
            }
        }
        ToolbarItem(placement: .topBarTrailing) {
            Button(action: { showDeleteAlert = true }) {
                Label("Delete", systemImage: "trash")
            }
        }
    }
}
```

### Chapter 2 — Glass Button Styles (GlassButtonStylesDemo.swift)

```swift
// GlassButtonStylesDemo.swift:147
Button("Glass Button") {}.buttonStyle(.glass)
Button("With Icon", systemImage: "star.fill") {}.buttonStyle(.glass)
Button("Prominent") {}.buttonStyle(.glassProminent)
Button("Save", systemImage: "checkmark") {}.buttonStyle(.glassProminent)

// Sizes — GlassButtonStylesDemo.swift:182
Button("Small")    {}.buttonStyle(.glass).controlSize(.small)
Button("Regular")  {}.buttonStyle(.glass).controlSize(.regular)
Button("Large")    {}.buttonStyle(.glass).controlSize(.large)

// Dynamic switch (real — GlassButtonStylesDemo.swift:264)
Button(action: { isFavorited.toggle() }) {
    Label(isFavorited ? "Favorited" : "Favorite",
          systemImage: isFavorited ? "heart.fill" : "heart")
}
.buttonStyle(isFavorited ? .glass(.regular) : .glass)
```

### Chapter 3 — Sheet Presentations (SheetGlassDemo.swift)

```swift
// SheetGlassDemo.swift:170
.navigationTitle("Glass Sheet Demo")
.navigationBarTitleDisplayMode(.inline)
.toolbar {
    ToolbarItem(placement: .cancellationAction) {
        Button(action: { dismiss() }) {
            Label("Close", systemImage: "xmark.circle.fill")
        }
        .buttonStyle(.glass)
    }
    ToolbarItem(placement: .confirmationAction) {
        Button("Save") { dismiss() }
            .buttonStyle(.glassProminent)
    }
}
.presentationBackground(.ultraThinMaterial)    // 187
.presentationDetents([.medium, .large])        // 188
.presentationDragIndicator(.visible)            // 189

// Floating action bar inside sheet (SheetGlassDemo.swift:193)
HStack(spacing: 12) {
    Button(action: {}) { Label("Favorite", systemImage: "heart") }
        .buttonStyle(.glass)
    Button(action: {}) { Label("Share", systemImage: "square.and.arrow.up") }
        .buttonStyle(.glass)
    Spacer()
    Button(action: {}) { Label("Apply", systemImage: "checkmark.circle.fill") }
        .buttonStyle(.glassProminent)
}
.padding()
.background(.thinMaterial)
.overlay(alignment: .top) {
    Rectangle()
        .fill(.quaternary.opacity(0.5))
        .frame(height: 0.5)
}
```

### Chapter 4 — Scroll Edge Effects (ScrollEdgeEffectDemo.swift)

```swift
// ScrollEdgeEffectDemo.swift:92
ZStack {
    ScrollView { /* content with safe-area padding for header/footer */ }
        .background(
            LinearGradient(
                colors: [.blue.opacity(0.1), .purple.opacity(0.05), .pink.opacity(0.08)],
                startPoint: .topLeading,
                endPoint: .bottomTrailing
            )
        )

    VStack(spacing: 0) {
        FloatingGlassHeader()   // .ultraThinMaterial
        Spacer()
        FloatingGlassFooter()   // .thinMaterial
    }
}
.frame(height: 450)
.clipShape(RoundedRectangle(cornerRadius: 20))
.overlay(
    RoundedRectangle(cornerRadius: 20)
        .strokeBorder(Color.white.opacity(0.3), lineWidth: 1)
)
.shadow(color: .black.opacity(0.1), radius: 15, x: 0, y: 8)

// Header (ScrollEdgeEffectDemo.swift:135)
HStack {
    VStack(alignment: .leading, spacing: 2) {
        Text("Scroll Edge Effect").font(.system(size: 16, weight: .semibold))
        Text("Glass header with blur").font(.system(size: 12)).foregroundStyle(.secondary)
    }
    Spacer()
    Image(systemName: "line.3.horizontal.decrease.circle")
        .font(.system(size: 20)).foregroundStyle(.blue)
}
.padding(.horizontal, 16).padding(.vertical, 12)
.background(.ultraThinMaterial)
.overlay(alignment: .bottom) {
    Rectangle().fill(.quaternary.opacity(0.5)).frame(height: 0.5)
}

// Footer (ScrollEdgeEffectDemo.swift:165)
HStack(spacing: 12) {
    Button(action: {}) { Label("Action", systemImage: "star.fill") }
        .buttonStyle(.glass).controlSize(.small)
    Button(action: {}) { Label("Options", systemImage: "ellipsis.circle") }
        .buttonStyle(.glass).controlSize(.small)
    Spacer()
    Button(action: {}) { Image(systemName: "arrow.up") }
        .buttonStyle(.glassProminent).controlSize(.small)
}
.padding(.horizontal, 16).padding(.vertical, 12)
.background(.thinMaterial)
.overlay(alignment: .top) {
    Rectangle().fill(.quaternary.opacity(0.5)).frame(height: 0.5)
}
```

### Chapter 5 — Tab Bar Glass (TabBarGlassDemo.swift)

```swift
// TabBarGlassDemo.swift:63
TabView(selection: $selectedTab) {
    TabViewContent(tab: 0, items: (1...10).map { "Home Item \($0)" })
    TabViewContent(tab: 1, items: (1...10).map { "Search Result \($0)" })
    TabViewContent(tab: 2, items: (1...10).map { "Setting \($0)" })
}
.frame(height: 400)
.clipShape(RoundedRectangle(cornerRadius: 16))

// Minimize on scroll — TabBarGlassDemo.swift:54
TabView { /* tabs */ }
    .tabBarMinimizeBehavior(.onScrollDown)
```

### Chapter 6 — Glass Effect Modifier (GlassEffectModifierDemo.swift)

```swift
// GlassEffectModifierDemo.swift:98
VStack(spacing: 8) {
    Image(systemName: icon).font(.title)
    Text(title).font(.headline)
}
.padding()
.glassEffect()                              // default shape
// ou
.glassEffect(in: .rect(cornerRadius: 16))   // shaped
```

### Chapter 7 — Liquid Glass Effects (VibrancyEffectsDemo.swift)

```swift
// VibrancyEffectsDemo.swift:95
Text("Default Glass")
    .font(.headline).padding()
    .glassEffect()

Text("Rounded Glass")
    .font(.headline).padding()
    .glassEffect(in: .rect(cornerRadius: 16))
```

### Chapter 8 — Search with Materials (SearchGlassDemo.swift)

```swift
// SearchGlassDemo.swift:66
List {
    ForEach(filteredItems, id: \.self) { item in
        SearchResultRow(item: item)
    }
}
.navigationTitle("Products")
.searchable(text: $searchText, prompt: "Search products")
.frame(maxWidth: .infinity)
.frame(height: 400)
.background(.thinMaterial, in: RoundedRectangle(cornerRadius: 16))
.clipShape(RoundedRectangle(cornerRadius: 16))
```

### Chapter 9 — Glass Effect Container (GlassEffectContainerDemo.swift)

```swift
// GlassContainerLiveDemo.swift:107
VStack(spacing: 24) { /* 3 sections */ }
    .padding(20)
    .frame(maxWidth: .infinity)
    .glassEffect()                          // container-level glass

// Individual icons (GlassEffectContainerDemo.swift:118)
GlassEffectContainer(spacing: 12) {
    HStack(spacing: 12) {
        WeatherIconGlass(icon: "sun.max.fill", color: .orange)
        WeatherIconGlass(icon: "moon.stars.fill", color: .indigo)
        WeatherIconGlass(icon: "cloud.rain.fill", color: .blue)
    }
}

// Unified list (GlassEffectContainerDemo.swift:161)
GlassEffectContainer(spacing: 0) {
    VStack(spacing: 0) {
        ActionRow(icon: "heart.fill", title: "Favorite", color: .red)
        Divider()
        ActionRow(icon: "star.fill", title: "Featured", color: .yellow)
        Divider()
        ActionRow(icon: "bookmark.fill", title: "Saved", color: .green)
    }
}
.glassEffect()

// Morphing — GlassContainerDemo.swift:274
@State private var isExpanded = false
@Namespace private var namespace
GlassEffectContainer(spacing: 40.0) {
    HStack(spacing: 40.0) {
        Image(systemName: "pencil")
            .frame(width: 80, height: 80).font(.system(size: 36))
            .foregroundStyle(.blue)
            .glassEffect()
            .glassEffectID("pencil", in: namespace)
        if isExpanded {
            Image(systemName: "eraser.fill")
                .frame(width: 80, height: 80).font(.system(size: 36))
                .foregroundStyle(.pink)
                .glassEffect()
                .glassEffectID("eraser", in: namespace)
        }
    }
}
Button {
    withAnimation(.spring(response: 0.6, dampingFraction: 0.7)) {
        isExpanded.toggle()
    }
} label: { Text(isExpanded ? "Hide Eraser" : "Show Eraser") }
.buttonStyle(.glass)
```

### Chapter 10 — Pickers with Glass (PickerGlassDemo.swift)

```swift
// Segmented (PickerGlassDemo.swift:95)
Picker("View Mode", selection: $selection) {
    Label("List", systemImage: "list.bullet").tag(0)
    Label("Grid", systemImage: "square.grid.2x2").tag(1)
    Label("Card", systemImage: "rectangle.stack").tag(2)
}
.pickerStyle(.segmented)

// Menu (PickerGlassDemo.swift:128)
Picker("Size", selection: $selectedOption) {
    ForEach(options, id: \.self) { Text(option).tag(option) }
}
.pickerStyle(.menu)

// Color picker (PickerGlassDemo.swift:154)
HStack(spacing: 16) {
    ForEach([Color.red, .blue, .green, .orange, .purple], id: \.self) { color in
        Circle()
            .fill(color)
            .frame(width: 44, height: 44)
            .overlay(
                Circle().strokeBorder(Color.white, lineWidth: selectedColor == color ? 3 : 0)
            )
            .overlay(
                Circle().strokeBorder(color.opacity(0.5), lineWidth: 2)
            )
            .shadow(color: selectedColor == color ? color.opacity(0.5) : .clear,
                   radius: selectedColor == color ? 8 : 0)
            .scaleEffect(selectedColor == color ? 1.1 : 1.0)
            .animation(.spring(response: 0.3), value: selectedColor)
            .onTapGesture { selectedColor = color }
    }
}
.frame(maxWidth: .infinity).padding()
.background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 12))
```

### Chapter 11 — System Glass Components (SystemGlassComponentsDemo.swift)

```swift
// Alert with automatic glass — SystemGlassComponentsDemo.swift:131
.alert("Automatic Glass", isPresented: $showAlert) {
    Button("OK", role: .cancel) { }
    Button("Delete", role: .destructive) { }
} message: {
    Text("This alert has automatic glass background")
}

// ConfirmationDialog — SystemGlassComponentsDemo.swift:161
.confirmationDialog("Automatic Glass Dialog", isPresented: $showDialog, titleVisibility: .visible) {
    Button("Confirm") { }
    Button("Maybe Later") { }
    Button("Cancel", role: .cancel) { }
} message: {
    Text("This dialog has built-in glass effects")
}

// Menu — SystemGlassComponentsDemo.swift:183
Menu {
    Button("Action 1", systemImage: "star") { }
    Button("Action 2", systemImage: "heart") { }
    Divider()
    Button("Delete", systemImage: "trash", role: .destructive) { }
} label: { Text("Open Menu") }
.buttonStyle(.borderedProminent)
.tint(.green)

// Slider avec glass container — SystemGlassComponentsDemo.swift:229
VStack(spacing: 16) { /* sliders */ }
    .padding()
    .glassEffect()

// ContextMenu — SystemGlassComponentsDemo.swift:248
Text("Long Press Here")
    .contextMenu {
        Button("Copy", systemImage: "doc.on.doc") { }
        Button("Share", systemImage: "square.and.arrow.up") { }
        Divider()
        Button("Delete", systemImage: "trash", role: .destructive) { }
    }
```

### Chapter 12 — Fluid Morphing Animation (FluidMorphingAnimationDemo.swift)

```swift
// Interactive glass button (FluidMorphingAnimationDemo.swift:124)
HStack(spacing: 12) {
    Image(systemName: icon).font(.system(size: 20, weight: .semibold))
    Text(title).font(.system(size: 16, weight: .semibold))
}
.foregroundStyle(.primary)
.padding(.horizontal, 24).padding(.vertical, 14)
.glassEffect(.regular.tint(color).interactive())

// Morphing via smooth animation (FluidMorphingAnimationDemo.swift:144)
@State private var isExpanded = false
@Namespace private var namespace
GlassEffectContainer(spacing: 40.0) {
    HStack(spacing: 40.0) {
        GlassSymbolView(symbol: "scribble.variable", color: .blue, id: "pencil", namespace: namespace)
        if isExpanded {
            GlassSymbolView(symbol: "eraser.fill", color: .pink, id: "eraser", namespace: namespace)
                .glassEffectTransition(.matchedGeometry)
        }
    }
}
Button(action: {
    withAnimation(.smooth(duration: 0.6)) { isExpanded.toggle() }
}) {
    Label(isExpanded ? "Hide Eraser" : "Show Eraser",
          systemImage: isExpanded ? "eye.slash.fill" : "eye.fill")
}

// Unified glass union (FluidMorphingAnimationDemo.swift:299)
GlassEffectContainer(spacing: 20.0) {
    HStack(spacing: 20.0) {
        ForEach(symbols.indices, id: \.self) { index in
            Image(systemName: symbols[index])
                .frame(width: 80, height: 80).font(.system(size: 36))
                .foregroundStyle(color)
                .glassEffect(.regular.tint(color))
                .glassEffectUnion(id: unionID, namespace: namespace)
        }
    }
}
```

### Chapter 13 — Glass Animations (GlassAnimationsDemo.swift)

```swift
// Auto expanding (GlassAnimationsDemo.swift:103)
@State private var isExpanded = false
Color.clear
    .frame(width: isExpanded ? 100 : 60, height: isExpanded ? 100 : 60)
    .glassEffect(in: .circle)
    .animation(.spring(response: 0.6, dampingFraction: 0.7), value: isExpanded)
    .task {
        while !Task.isCancelled {
            try? await Task.sleep(for: .seconds(1.5))
            isExpanded.toggle()
        }
    }

// Auto rotating (GlassAnimationsDemo.swift:127)
@State private var rotation: Double = 0
Color.clear
    .frame(width: 80, height: 80)
    .glassEffect(in: .rect(cornerRadius: 16))
    .rotationEffect(.degrees(rotation))
    .animation(.easeInOut(duration: 0.8), value: rotation)
    .task {
        while !Task.isCancelled {
            try? await Task.sleep(for: .seconds(1.2))
            rotation += 90
        }
    }

// Auto merging (GlassAnimationsDemo.swift:151)
@State private var isMerged = false
ZStack {
    Color.clear.frame(width: 60, height: 60)
        .glassEffect(in: .circle)
        .offset(x: isMerged ? 0 : -40, y: 0)
        .zIndex(0)
    Color.clear.frame(width: 60, height: 60)
        .glassEffect(in: .circle)
        .offset(x: isMerged ? 0 : 40, y: 0)
        .zIndex(1)
}
.task {
    while !Task.isCancelled {
        try? await Task.sleep(for: .seconds(1.5))
        withAnimation(.spring(response: 0.6, dampingFraction: 0.7)) {
            isMerged.toggle()
        }
    }
}
```

### Chapter 14 — Glass Overlap (GlassOverlapDemo.swift)

```swift
// Draggable (GlassOverlapDemo.swift:79)
@State private var offset = CGSize.zero
ZStack {
    Color.clear.frame(width: 100, height: 100).glassEffect(in: .circle)
    Color.clear.frame(width: 90, height: 90)
        .glassEffect(in: .circle)
        .offset(offset)
        .gesture(
            DragGesture()
                .onChanged { offset = $0.translation }
                .onEnded { _ in
                    withAnimation(.spring()) { offset = .zero }
                }
        )
        .zIndex(1)
}

// Stacked (GlassOverlapDemo.swift:117)
ZStack {
    Color.clear.frame(width: 140, height: 100)
        .glassEffect(in: .rect(cornerRadius: 16))
        .offset(x: -30, y: -20).zIndex(0)
    Color.clear.frame(width: 140, height: 100)
        .glassEffect(in: .rect(cornerRadius: 16))
        .offset(x: 0, y: 0).zIndex(1)
    Color.clear.frame(width: 140, height: 100)
        .glassEffect(in: .rect(cornerRadius: 16))
        .offset(x: 30, y: 20).zIndex(2)
}

// Intersecting (GlassOverlapDemo.swift:151)
HStack(spacing: -40) {
    Color.clear.frame(width: 80, height: 80).glassEffect(in: .circle)
    Color.clear.frame(width: 80, height: 80).glassEffect(in: .circle)
    Color.clear.frame(width: 80, height: 80).glassEffect(in: .circle)
}
```

### Chapter 15 — Material Hierarchy (MaterialHierarchyDemo.swift)

```swift
// MaterialHierarchyDemo.swift:91
VStack(spacing: 16) {
    MaterialCard(material: .ultraThinMaterial, title: "Ultra Thin")
    MaterialCard(material: .thinMaterial,      title: "Thin")
    MaterialCard(material: .regularMaterial,   title: "Regular")
    MaterialCard(material: .thickMaterial,     title: "Thick")
}
.padding()
// background: LinearGradient([.blue, .purple, .pink, .orange])

// MaterialCard.swift:10
Text(title)
    .font(.headline).foregroundStyle(.primary)
    .frame(maxWidth: .infinity).padding()
    .background(material, in: RoundedRectangle(cornerRadius: 12))
```

### Chapter 16 — Toolbar Grouping (ToolbarGroupingDemo.swift)

```swift
// ToolbarGroupingDemo.swift:70
.toolbar {
    ToolbarItemGroup(placement: .topBarTrailing) {
        Button("Draw", systemImage: "pencil") {}
        Button("Erase", systemImage: "eraser") {}
    }
    ToolbarSpacer(.flexible, placement: .topBarTrailing)
    ToolbarItem(placement: .confirmationAction) {
        Button("Save", systemImage: "checkmark") {}
    }
}
```

## Composants réutilisables (réels)

### ModernChapterCard — `Components/ModernChapterCard.swift:10`
```swift
HStack(spacing: 16) {
    IconCircle(icon: chapter.icon, color: chapter.color)        // 52x52, 0.12 bg, 0.25 border
    ContentArea(number: chapter.id, title: chapter.title, subtitle: chapter.subtitle)
    Spacer(minLength: 8)
    ChevronIcon()                                                // 14pt, .quaternary
}
.padding(.horizontal, 20).padding(.vertical, 16)
.background(RowBackground(color: chapter.color))                 // 14pt corner

// IconCircle — 52x52, fill: color.opacity(0.12), stroke: color.opacity(0.25), icon: 22pt medium
// ContentArea — ChapterBadge (11pt tertiary uppercase tracking 0.5) + title 17pt semibold + subtitle 14pt secondary
// RowBackground — RoundedRectangle(14) ultraThin + linearGradient(color.opacity(0.05)→clear) + border 0.5 + shadow(color.opacity(0.15), 8, y:4)
```

### InfoCard — `Components/InfoCard.swift:10`
```swift
HStack(alignment: .top, spacing: 12) {
    IconView(icon: icon, color: color)                            // 40px wide, .title2
    TextContent(title: title, description: description)          // .headline + .subheadline
}
.padding(16)
.background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 12))
```

### KeyPointsCard — `Components/KeyPointsCard.swift:10`
```swift
VStack(alignment: .leading, spacing: 12) {
    Label("Key Points", systemImage: "lightbulb.fill")
        .font(.headline).foregroundStyle(.orange)
    PointsList(points: points)                                    // checkmark.circle.fill green + subheadline secondary
}
.padding(16)
.background(.thinMaterial, in: RoundedRectangle(cornerRadius: 12))
```

### ActionButtonsCard — `Components/ActionButtonsCard.swift:10`
```swift
VStack(spacing: 20) {
    CardHeader(title: title, icon: icon, color: color)           // 48x48 circle (color.opacity 0.15)
    QuickDescription(description: description)                   // 15pt secondary lineLimit 3
    ActionButtons(title: title, /* ... */)                       // 2 NavigationLinks → explanation + code
}
.padding(24)
.background(RoundedRectangle(cornerRadius: 24).fill(.ultraThinMaterial))
.overlay(RoundedRectangle(24).strokeBorder(.white.opacity(0.2), 1))
.shadow(color: .black.opacity(0.1), radius: 20, x: 0, y: 10)

// LargeActionButton — ActionButtonsCard.swift:128
HStack(spacing: 16) {
    Image(systemName: icon).font(.system(size: 20, weight: .semibold))
        .foregroundStyle(.white)
        .frame(width: 44, height: 44)
        .background(LinearGradient(colors: [color, color.opacity(0.8)], startPoint: .topLeading, endPoint: .bottomTrailing))
        .clipShape(RoundedRectangle(cornerRadius: 12))
    Text(title).font(.system(size: 17, weight: .semibold))
    Spacer()
    Image(systemName: "chevron.right").font(.system(size: 14, weight: .bold))
}
.padding(.horizontal, 20).padding(.vertical, 16)
.background(RoundedRectangle(cornerRadius: 16).fill(.thinMaterial))
.overlay(RoundedRectangle(16).strokeBorder(color.opacity(0.3), 1.5))
```

### SectionTitle — `Components/DemoSection.swift:28`
```swift
HStack {
    Rectangle()
        .fill(LinearGradient(colors: [.blue, .cyan], startPoint: .leading, endPoint: .trailing))
        .frame(width: 4, height: 28)
        .clipShape(RoundedRectangle(cornerRadius: 2))
    Text(title).font(.system(size: 22, weight: .bold))
    Spacer()
}
```

### CodeBlock — `Views/CodeDetailView.swift:79`
```swift
ScrollView(.horizontal, showsIndicators: true) {
    Text(code)
        .font(.system(size: 15, design: .monospaced))
        .foregroundStyle(.primary)
        .padding(20).frame(maxWidth: .infinity, alignment: .leading)
}
.background(RoundedRectangle(cornerRadius: 20).fill(.ultraThinMaterial))
.overlay(RoundedRectangle(20).strokeBorder(Color.blue.opacity(0.3), 1.5))
.shadow(color: .black.opacity(0.1), radius: 15, x: 0, y: 8)
```

### LanguageBadge — `Views/CodeDetailView.swift:66`
```swift
Text(language.uppercased())
    .font(.caption.weight(.semibold))
    .foregroundStyle(.white)
    .padding(.horizontal, 12).padding(.vertical, 6)
    .background(.blue, in: Capsule())
```

### AnimatedGradientBackground — `Components/AnimatedGradientBackground.swift:10`
```swift
@State private var animateGradient = false
LinearGradient(
    colors: [Color.blue.opacity(0.3), Color.purple.opacity(0.3), Color.pink.opacity(0.3), Color.orange.opacity(0.3)],
    startPoint: animateGradient ? .topLeading : .bottomLeading,
    endPoint: animateGradient ? .bottomTrailing : .topTrailing
)
.ignoresSafeArea()
.onAppear {
    withAnimation(.easeInOut(duration: 5).repeatForever(autoreverses: true)) {
        animateGradient.toggle()
    }
}
```

### WaterDropletBackground — `Components/WaterDropletBackground.swift:10`
```swift
ZStack {
    LinearGradient(colors: [Color(red: 0.95, green: 0.97, blue: 1.0),
                            Color(red: 0.90, green: 0.94, blue: 0.98)],
                   startPoint: .topLeading, endPoint: .bottomTrailing)
        .ignoresSafeArea()
    if let image = UIImage(named: "water-droplets") {
        Image(uiImage: image).resizable().aspectRatio(contentMode: .fill)
            .opacity(0.08).ignoresSafeArea()
    }
}
```

## Transposition pour le Web (CSS/HTML) — fidèle à la source

Le Liquid Glass est une API système native iOS 26. La transposition Web est une **approximation esthétique**.

### Surface verre de base (transposition des 4 matériaux de MaterialHierarchyDemo.swift)

```css
/* .ultraThinMaterial — MaterialCard: titre, sheet, code, header */
.ultra-thin {
  background: rgba(255, 255, 255, 0.06);
  backdrop-filter: blur(40px) saturate(180%) brightness(115%);
  -webkit-backdrop-filter: blur(40px) saturate(180%) brightness(115%);
}

/* .thinMaterial — footer, demo container, key points */
.thin {
  background: rgba(255, 255, 255, 0.10);
  backdrop-filter: blur(20px) saturate(180%) brightness(110%);
  -webkit-backdrop-filter: blur(20px) saturate(180%) brightness(110%);
}

/* .regularMaterial — menu picker */
.regular {
  background: rgba(255, 255, 255, 0.18);
  backdrop-filter: blur(12px) saturate(160%) brightness(105%);
  -webkit-backdrop-filter: blur(12px) saturate(160%) brightness(105%);
}

/* .thickMaterial — alertes (rare) */
.thick {
  background: rgba(255, 255, 255, 0.28);
  backdrop-filter: blur(8px) saturate(150%) brightness(100%);
  -webkit-backdrop-filter: blur(8px) saturate(150%) brightness(100%);
}

@supports not (backdrop-filter: blur(1px)) {
  .ultra-thin, .thin, .regular { background: rgba(255, 255, 255, 0.78); }
  .thick { background: rgba(255, 255, 255, 0.88); }
}
```

### Recette carte verre — transposition de ModernChapterCard.swift:98

```css
.glass-card {
  position: relative;
  background: rgba(255, 255, 255, 0.06);
  backdrop-filter: blur(40px) saturate(180%) brightness(115%);
  -webkit-backdrop-filter: blur(40px) saturate(180%) brightness(115%);
  border-radius: 14px;
  box-shadow: var(--card-color, transparent) 0px 4px 8px;
  border: 0.5px solid var(--card-color-alpha-15, rgba(255, 255, 255, 0.2));
  transition: all 0.18s cubic-bezier(0.32, 0.94, 0.6, 1);
  overflow: hidden;
}
.glass-card::before {
  content: '';
  position: absolute; inset: 0; border-radius: inherit; pointer-events: none;
  background: linear-gradient(135deg, var(--card-color-alpha-05, transparent), transparent);
}
.glass-card::after {
  content: '';
  position: absolute; inset: 0; border-radius: inherit; pointer-events: none;
  box-shadow: inset 0 -0.5px 0 rgba(0, 0, 0, 0.06);
}
```

### Tab bar (transposition de TabBarGlassDemo.swift:63)

```css
.tab-bar {
  position: fixed; bottom: calc(34px + 10px); left: 50%; transform: translateX(-50%);
  display: flex; align-items: center; gap: 4px; padding: 4px 6px;
  background: rgba(255, 255, 255, 0.10);
  backdrop-filter: blur(40px) saturate(180%) brightness(115%);
  -webkit-backdrop-filter: blur(40px) saturate(180%) brightness(115%);
  border-radius: 9999px; box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
  z-index: 100;
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.tab-item {
  display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px;
  width: 56px; height: 44px; border-radius: 9999px; border: none; background: transparent;
  color: rgba(0, 0, 0, 0.55); font-family: -apple-system; font-size: 10px; font-weight: 500;
  cursor: pointer; -webkit-tap-highlight-color: transparent;
  transition: all 0.18s cubic-bezier(0.32, 0.94, 0.6, 1);
}
.tab-item.active { background: rgba(0, 122, 255, 0.20); color: #007AFF; }
```

### Sheet modal (transposition de SheetGlassDemo.swift:187)

```css
.modal-sheet {
  position: fixed; bottom: 0; left: 0; right: 0;
  padding: 20px; padding-bottom: calc(34px + 12px);
  background: rgba(255, 255, 255, 0.06);
  backdrop-filter: blur(40px) saturate(180%) brightness(115%);
  -webkit-backdrop-filter: blur(40px) saturate(180%) brightness(115%);
  border-radius: 40px 40px 0 0;
  box-shadow: 0 -2px 16px rgba(0, 0, 0, 0.06);
  animation: sheetIn 350ms cubic-bezier(0.34, 1.56, 0.64, 1);
}
@keyframes sheetIn { from { transform: translateY(100%); } to { transform: translateY(0); } }
.modal-sheet::before {
  content: ''; position: absolute; top: 6px; left: 50%; transform: translateX(-50%);
  width: 36px; height: 4px; border-radius: 9999px; background: rgba(0, 0, 0, 0.10);
}
```

### Glass overlap stack (transposition de GlassOverlapDemo.swift:151)

```css
.glass-overlap-stack {
  display: flex; justify-content: center; padding: 20px;
}
.glass-overlap-stack > * {
  width: 80px; height: 80px; border-radius: 50%;
  background: rgba(255, 255, 255, 0.10);
  backdrop-filter: blur(20px) saturate(180%) brightness(110%);
  -webkit-backdrop-filter: blur(20px) saturate(180%) brightness(110%);
  border: 0.5px solid rgba(255, 255, 255, 0.3);
  position: relative;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
  margin-left: -40px;
  transition: all 0.18s cubic-bezier(0.32, 0.94, 0.6, 1);
}
.glass-overlap-stack > *:first-child { margin-left: 0; }
```

### Transitions CSS (toutes issues du code source réel)

```css
/* GlassAnimationsDemo.swift:116 — spring morphing */
.glass-morph { transition: all 0.6s cubic-bezier(0.34, 1.56, 0.64, 1); }

/* CardButtonStyle.swift:14 — pressed state */
.glass-interactive { transition: all 0.15s ease-in-out; }

/* SheetGlassDemo.swift — sheet appearance */
.glass-spring-in { animation: springIn 0.35s cubic-bezier(0.34, 1.56, 0.64, 1); }
@keyframes springIn { from { transform: translateY(100%); } to { transform: translateY(0); } }

/* FluidMorphingAnimationDemo.swift:216 — smooth morphing */
.glass-smooth { transition: all 0.6s cubic-bezier(0.25, 0.1, 0.25, 1); }

/* GlassAnimationsDemo.swift:140 — auto rotation */
.glass-auto-rotate { animation: glass-rotate 0.8s ease-in-out infinite alternate; }
@keyframes glass-rotate { 0% { transform: rotate(0deg); } 100% { transform: rotate(90deg); } }

/* GlassAnimationsDemo.swift:103 — auto expand/contract */
.glass-auto-expand { animation: glass-expand 3s ease-in-out infinite; }
@keyframes glass-expand { 0%, 100% { scale: 1; } 50% { scale: 1.6; } }

/* GlassAnimationsDemo.swift:151 — auto merge/separate */
.glass-auto-merge-left  { animation: glass-merge 3s ease-in-out infinite; }
.glass-auto-merge-right { animation: glass-merge 3s ease-in-out infinite reverse; }
@keyframes glass-merge { 0%, 100% { transform: translateX(0); } 50% { transform: translateX(40px); } }

/* AnimatedGradientBackground.swift:26 — infinite gradient shift */
.glass-gradient-shift { animation: glass-gradient 5s ease-in-out infinite alternate; }
@keyframes glass-gradient { 0% { background-position: 0% 0%; } 100% { background-position: 100% 100%; } }

/* CardButtonStyle.swift:13 — pressed scale 0.97 */
.glass-pressed:active { transform: scale(0.97); }
```

## Composants React — transposition fidèle des composants SwiftUI réels

### ChapterCard — transposition de `ModernChapterCard.swift`

```tsx
import React from 'react';

export interface ChapterData {
  id: number;
  title: string;
  subtitle: string;
  icon: string;
  color: string; // hex ex: '#007AFF'
}

interface Props {
  chapter: ChapterData;
  onClick?: () => void;
}

const hexToRgba = (hex: string, alpha: number) => {
  const r = parseInt(hex.slice(1, 3), 16);
  const g = parseInt(hex.slice(3, 5), 16);
  const b = parseInt(hex.slice(5, 7), 16);
  return `rgba(${r}, ${g}, ${b}, ${alpha})`;
};

export const ChapterCard: React.FC<Props> = ({ chapter, onClick }) => (
  <div
    onClick={onClick}
    style={{
      position: 'relative',
      display: 'flex', alignItems: 'center', gap: 16,
      padding: '16px 20px',
      borderRadius: 14,
      cursor: 'pointer',
      background: 'rgba(255, 255, 255, 0.06)',
      backdropFilter: 'blur(40px) saturate(180%) brightness(115%)',
      WebkitBackdropFilter: 'blur(40px) saturate(180%) brightness(115%)',
      boxShadow: `${hexToRgba(chapter.color, 0.15)} 0 4px 8px`,
      border: `0.5px solid ${hexToRgba(chapter.color, 0.15)}`,
      transition: 'all 0.18s cubic-bezier(0.32, 0.94, 0.6, 1)',
      overflow: 'hidden',
    }}
  >
    <div style={{
      position: 'absolute', inset: 0, borderRadius: 14, pointerEvents: 'none',
      background: `linear-gradient(135deg, ${hexToRgba(chapter.color, 0.05)}, transparent)`,
    }} />
    <div style={{
      position: 'absolute', inset: 0, borderRadius: 14, pointerEvents: 'none',
      boxShadow: 'inset 0 -0.5px 0 rgba(0, 0, 0, 0.06)',
    }} />

    {/* IconCircle — 52x52, fill 0.12, border 0.25 */}
    <div style={{
      width: 52, height: 52, borderRadius: '50%',
      background: hexToRgba(chapter.color, 0.12),
      border: `1px solid ${hexToRgba(chapter.color, 0.25)}`,
      display: 'flex', alignItems: 'center', justifyContent: 'center',
      flexShrink: 0, position: 'relative', zIndex: 1,
    }}>
      <span style={{
        fontSize: 22, fontWeight: 500,
        background: `linear-gradient(135deg, ${chapter.color}, ${hexToRgba(chapter.color, 0.8)})`,
        WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent',
      }}>{chapter.icon}</span>
    </div>

    {/* ContentArea */}
    <div style={{ position: 'relative', zIndex: 1, flex: 1 }}>
      <div style={{
        fontSize: 11, fontWeight: 600, color: 'rgba(0, 0, 0, 0.45)',
        textTransform: 'uppercase', letterSpacing: 0.5, marginBottom: 4,
      }}>
        Chapter {chapter.id}
      </div>
      <div style={{
        fontSize: 17, fontWeight: 600, color: 'rgba(0, 0, 0, 0.85)',
        marginBottom: 2, lineHeight: 1.3,
      }}>
        {chapter.title}
      </div>
      <div style={{ fontSize: 14, color: 'rgba(0, 0, 0, 0.5)', lineHeight: 1.2 }}>
        {chapter.subtitle}
      </div>
    </div>

    {/* ChevronIcon */}
    <span style={{
      color: 'rgba(0, 0, 0, 0.25)', fontSize: 14, fontWeight: 'bold',
      flexShrink: 0, position: 'relative', zIndex: 1,
    }}>›</span>
  </div>
);
```

### InfoCard — transposition de `InfoCard.swift`

```tsx
import React from 'react';

interface InfoCardProps {
  icon: string; title: string; description: string; color?: string;
}

export const InfoCard: React.FC<InfoCardProps> = ({
  icon, title, description, color = '#007AFF',
}) => (
  <div style={{
    display: 'flex', gap: 12, padding: 16,
    borderRadius: 12, alignItems: 'flex-start',
    background: 'rgba(255, 255, 255, 0.06)',
    backdropFilter: 'blur(40px) saturate(180%) brightness(115%)',
    WebkitBackdropFilter: 'blur(40px) saturate(180%) brightness(115%)',
  }}>
    <span style={{ fontSize: 24, color, width: 40, flexShrink: 0 }}>{icon}</span>
    <div>
      <div style={{ fontSize: 17, fontWeight: 600, color: 'rgba(0, 0, 0, 0.85)', marginBottom: 6 }}>
        {title}
      </div>
      <div style={{ fontSize: 15, color: 'rgba(0, 0, 0, 0.5)', lineHeight: 1.4 }}>
        {description}
      </div>
    </div>
  </div>
);
```

### KeyPointsCard — transposition de `KeyPointsCard.swift`

```tsx
import React from 'react';

interface KeyPointsCardProps { points: string[]; }

export const KeyPointsCard: React.FC<KeyPointsCardProps> = ({ points }) => (
  <div style={{
    padding: 16, borderRadius: 12,
    background: 'rgba(255, 255, 255, 0.10)',
    backdropFilter: 'blur(20px) saturate(180%) brightness(110%)',
    WebkitBackdropFilter: 'blur(20px) saturate(180%) brightness(110%)',
  }}>
    <div style={{ display: 'flex', alignItems: 'center', gap: 6, fontSize: 17, fontWeight: 600, color: '#FF9500', marginBottom: 12 }}>
      <span style={{ fontSize: 16 }}>💡</span> Key Points
    </div>
    {points.map((p, i) => (
      <div key={i} style={{ display: 'flex', alignItems: 'flex-start', gap: 8, marginBottom: 8 }}>
        <span style={{ color: '#34C759', fontSize: 14, marginTop: 2 }}>✓</span>
        <span style={{ fontSize: 15, color: 'rgba(0, 0, 0, 0.55)', lineHeight: 1.4 }}>{p}</span>
      </div>
    ))}
  </div>
);
```

### ActionButtonsCard — transposition de `ActionButtonsCard.swift`

```tsx
import React from 'react';

interface ActionButtonsCardProps {
  title: string; description: string; code: string;
  icon: string; color?: string;
  onViewCode?: () => void; onViewExplanation?: () => void;
}

const hexToRgba = (hex: string, alpha: number) => {
  const r = parseInt(hex.slice(1, 3), 16);
  const g = parseInt(hex.slice(3, 5), 16);
  const b = parseInt(hex.slice(5, 7), 16);
  return `rgba(${r}, ${g}, ${b}, ${alpha})`;
};

export const ActionButtonsCard: React.FC<ActionButtonsCardProps> = ({
  title, description, code, icon, color = '#007AFF',
  onViewCode, onViewExplanation,
}) => (
  <div style={{
    position: 'relative', padding: 24, borderRadius: 24,
    background: 'rgba(255, 255, 255, 0.06)',
    backdropFilter: 'blur(40px) saturate(180%) brightness(115%)',
    WebkitBackdropFilter: 'blur(40px) saturate(180%) brightness(115%)',
    boxShadow: '0 10px 20px rgba(0, 0, 0, 0.10)',
    border: '1px solid rgba(255, 255, 255, 0.2)',
  }}>
    <div style={{ display: 'flex', alignItems: 'center', gap: 16, marginBottom: 16 }}>
      <div style={{
        width: 48, height: 48, borderRadius: '50%',
        background: hexToRgba(color, 0.15),
        display: 'flex', alignItems: 'center', justifyContent: 'center',
      }}>
        <span style={{ fontSize: 24, fontWeight: 600, color }}>{icon}</span>
      </div>
      <div style={{ fontSize: 20, fontWeight: 700, color: 'rgba(0, 0, 0, 0.85)' }}>{title}</div>
    </div>

    <div style={{ fontSize: 15, color: 'rgba(0, 0, 0, 0.55)', lineHeight: 1.4, marginBottom: 20 }}>
      {description}
    </div>

    <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
      <ActionButton label="View Explanation" icon="📄" onClick={onViewExplanation} />
      <ActionButton label="View Code" icon="</>" onClick={onViewCode} />
    </div>
  </div>
);

const ActionButton: React.FC<{ label: string; icon: string; onClick?: () => void }> = ({ label, icon, onClick }) => (
  <div onClick={onClick} style={{
    display: 'flex', alignItems: 'center', gap: 16,
    padding: '16px 20px', borderRadius: 16, cursor: 'pointer',
    background: 'rgba(255, 255, 255, 0.10)',
    backdropFilter: 'blur(20px) saturate(180%) brightness(110%)',
    WebkitBackdropFilter: 'blur(20px) saturate(180%) brightness(110%)',
    border: '1.5px solid rgba(0, 122, 255, 0.3)',
    transition: 'all 0.18s cubic-bezier(0.32, 0.94, 0.6, 1)',
  }}>
    <div style={{
      width: 44, height: 44, borderRadius: 12,
      background: 'linear-gradient(135deg, #007AFF, rgba(0, 122, 255, 0.8))',
      display: 'flex', alignItems: 'center', justifyContent: 'center',
      color: 'white', fontSize: 20,
    }}>{icon}</div>
    <span style={{ flex: 1, fontSize: 17, fontWeight: 600, color: 'rgba(0, 0, 0, 0.85)' }}>{label}</span>
    <span style={{ color: 'rgba(0, 0, 0, 0.35)', fontSize: 14, fontWeight: 'bold' }}>›</span>
  </div>
);
```

### FloatingGlassHeader / FloatingGlassFooter — transposition de `ScrollEdgeEffectDemo.swift:135,165`

```tsx
import React from 'react';

export const FloatingGlassHeader: React.FC<{ title: string; subtitle?: string }> = ({ title, subtitle }) => (
  <div style={{
    padding: '12px 16px',
    background: 'rgba(255, 255, 255, 0.06)',
    backdropFilter: 'blur(40px) saturate(180%) brightness(115%)',
    WebkitBackdropFilter: 'blur(40px) saturate(180%) brightness(115%)',
    borderBottom: '0.5px solid rgba(128, 128, 128, 0.3)',
    display: 'flex', alignItems: 'center', justifyContent: 'space-between',
  }}>
    <div>
      <div style={{ fontSize: 16, fontWeight: 600, color: 'rgba(0, 0, 0, 0.85)' }}>{title}</div>
      {subtitle && <div style={{ fontSize: 12, color: 'rgba(0, 0, 0, 0.45)' }}>{subtitle}</div>}
    </div>
    <span style={{ fontSize: 20, color: '#007AFF' }}>⚙</span>
  </div>
);

export const FloatingGlassFooter: React.FC<{
  actions: Array<{ label: string; icon: string; prominent?: boolean; onClick?: () => void }>;
}> = ({ actions }) => (
  <div style={{
    display: 'flex', alignItems: 'center', gap: 12, padding: '12px 16px',
    background: 'rgba(255, 255, 255, 0.10)',
    backdropFilter: 'blur(20px) saturate(180%) brightness(110%)',
    WebkitBackdropFilter: 'blur(20px) saturate(180%) brightness(110%)',
    borderTop: '0.5px solid rgba(128, 128, 128, 0.3)',
  }}>
    {actions.map((a, i) => (
      <button key={i} onClick={a.onClick} style={{
        display: 'flex', alignItems: 'center', gap: 6,
        padding: a.prominent ? '6px 16px' : '4px 12px',
        borderRadius: 9999, border: 'none', cursor: 'pointer',
        background: a.prominent ? 'rgba(0, 122, 255, 0.20)' : 'rgba(255, 255, 255, 0.10)',
        backdropFilter: 'blur(20px) saturate(180%) brightness(110%)',
        WebkitBackdropFilter: 'blur(20px) saturate(180%) brightness(110%)',
        fontSize: 14, fontWeight: 500, color: '#007AFF',
        transition: 'all 0.15s ease-in-out',
      }}>
        <span>{a.icon}</span>
        <span>{a.label}</span>
      </button>
    ))}
    <div style={{ flex: 1 }} />
  </div>
);
```

### SheetModal — transposition de `SheetGlassDemo.swift:120`

```tsx
import React from 'react';

export const SheetModal: React.FC<{ open: boolean; onClose: () => void; children: React.ReactNode }> = ({
  open, onClose, children,
}) => {
  if (!open) return null;
  return (
    <div style={{
      position: 'fixed', inset: 0, zIndex: 1000,
      background: 'rgba(0, 0, 0, 0.20)',
      display: 'flex', alignItems: 'flex-end', justifyContent: 'center',
    }} onClick={onClose}>
      <div onClick={e => e.stopPropagation()} style={{
        width: '100%', maxWidth: 600,
        padding: 20, paddingBottom: 'calc(34px + 12px)',
        background: 'rgba(255, 255, 255, 0.06)',
        backdropFilter: 'blur(40px) saturate(180%) brightness(115%)',
        WebkitBackdropFilter: 'blur(40px) saturate(180%) brightness(115%)',
        borderRadius: '40px 40px 0 0',
        boxShadow: '0 -2px 16px rgba(0, 0, 0, 0.06)',
        animation: 'sheetIn 350ms cubic-bezier(0.34, 1.56, 0.64, 1)',
        position: 'relative',
      }}>
        <div style={{
          position: 'absolute', top: 6, left: '50%', transform: 'translateX(-50%)',
          width: 36, height: 4, borderRadius: 9999, background: 'rgba(0, 0, 0, 0.10)',
        }} />
        {children}
      </div>
    </div>
  );
};
```

### GlassMaterialCard — transposition de `MaterialCard.swift:10`

```tsx
import React from 'react';

type Material = 'ultraThin' | 'thin' | 'regular' | 'thick';

const BG: Record<Material, string> = {
  ultraThin: 'rgba(255, 255, 255, 0.06)',
  thin:      'rgba(255, 255, 255, 0.10)',
  regular:   'rgba(255, 255, 255, 0.18)',
  thick:     'rgba(255, 255, 255, 0.28)',
};
const BLUR: Record<Material, string> = {
  ultraThin: 'blur(40px) saturate(180%) brightness(115%)',
  thin:      'blur(20px) saturate(180%) brightness(110%)',
  regular:   'blur(12px) saturate(160%) brightness(105%)',
  thick:     'blur(8px)  saturate(150%) brightness(100%)',
};

export const MaterialCard: React.FC<{ material: Material; title: string }> = ({ material, title }) => (
  <div style={{
    padding: 16, borderRadius: 12, textAlign: 'center',
    fontSize: 17, fontWeight: 600, color: 'white',
    background: BG[material],
    backdropFilter: BLUR[material],
    WebkitBackdropFilter: BLUR[material],
  }}>
    {title}
  </div>
);

export const MaterialHierarchy: React.FC = () => (
  <div style={{
    background: 'linear-gradient(135deg, #007AFF, #AF52DE, #FF2D55, #FF9500)',
    borderRadius: 16, padding: 16, display: 'flex', flexDirection: 'column', gap: 16,
  }}>
    <MaterialCard material="ultraThin" title="Ultra Thin" />
    <MaterialCard material="thin"      title="Thin" />
    <MaterialCard material="regular"   title="Regular" />
    <MaterialCard material="thick"     title="Thick" />
  </div>
);
```

### CodeBlock — transposition de `CodeDetailView.swift:79`

```tsx
import React from 'react';

export const CodeBlock: React.FC<{ code: string }> = ({ code }) => (
  <div style={{
    overflowX: 'auto',
    background: 'rgba(255, 255, 255, 0.06)',
    backdropFilter: 'blur(40px) saturate(180%) brightness(115%)',
    WebkitBackdropFilter: 'blur(40px) saturate(180%) brightness(115%)',
    borderRadius: 20,
    border: '1.5px solid rgba(0, 122, 255, 0.3)',
    boxShadow: '0 8px 15px rgba(0, 0, 0, 0.1)',
  }}>
    <pre style={{
      margin: 0, padding: 20,
      fontFamily: 'ui-monospace, SFMono-Regular, monospace',
      fontSize: 15, color: 'rgba(0, 0, 0, 0.85)',
      whiteSpace: 'pre', lineHeight: 1.4,
    }}>{code}</pre>
  </div>
);

export const LanguageBadge: React.FC<{ language: string }> = ({ language }) => (
  <span style={{
    display: 'inline-block',
    padding: '6px 12px', borderRadius: 9999,
    fontSize: 11, fontWeight: 600, color: 'white',
    background: '#007AFF', textTransform: 'uppercase',
    letterSpacing: 0.5,
  }}>
    {language}
  </span>
);
```

### PressableScale — transposition de `CardButtonStyle.swift:10`

```tsx
import React, { useState } from 'react';

export const PressableScale: React.FC<{
  onClick?: () => void; children: React.ReactNode; style?: React.CSSProperties;
}> = ({ onClick, children, style }) => {
  const [pressed, setPressed] = useState(false);
  return (
    <div
      onClick={onClick}
      onMouseDown={() => setPressed(true)}
      onMouseUp={() => setPressed(false)}
      onMouseLeave={() => setPressed(false)}
      onTouchStart={() => setPressed(true)}
      onTouchEnd={() => setPressed(false)}
      style={{
        transform: pressed ? 'scale(0.97)' : 'scale(1)',
        transition: 'all 0.15s ease-in-out',
        cursor: 'pointer', ...style,
      }}
    >
      {children}
    </div>
  );
};
```

## Workflow de conception

1. Détermine le **contexte** : navigation flottante (tab bar, toolbar, sheet) ou contenu (cartes, listes — *éviter le verre ici*)
2. Choisis le **matériau** Apple équivalent : `.ultraThinMaterial` (fond général), `.thinMaterial` (boutons, barres), `.regularMaterial` (menus, pickers)
3. Choisis l'**intensité CSS** : ultraThin = blur(40px) / thin = blur(20px) / regular = blur(12px)
4. Ajoute les **coins arrondis** : 12px (mini), 14px (cartes ModernChapterCard), 16px (cartes ChapterCard), 20px (conteneurs), 24px (ActionButtonsCard), 40px (sheets), 9999px (pills)
5. Ajoute la **double couche** : highlight spéculaire (::before) + shadow interne (::after)
6. Ajoute les **états interactifs** : hover (scale 1.02), pressed (scale 0.97), disabled (opacity 0.4)
7. **Dark mode** : baisser background rgba de ~40%, garder highlight spéculaire plus subtil
8. **Performance** : utiliser `will-change: transform` sur les éléments animés
9. **Composition de carte verre** (pattern récurrent) : `.background(material)` + `.overlay(strokeBorder)` + `.shadow(color.opacity)`
10. **Groupement toolbar** : `ToolbarItemGroup` pour les actions liées, `ToolbarSpacer` pour la séparation
11. **Auto-animations** : utiliser `.task` avec boucle `while !Task.isCancelled` + `Task.sleep`

## Anti-Patterns

| # | ❌ Incorrect | ✅ Correct |
|---|---|---|
| 1 | `blur(40px)` comme valeur absolue Apple | C'est une transposition web — Apple utilise `.ultraThinMaterial` |
| 2 | SVG Filters avec feDisplacementMap | Apple utilise le rendu système natif, pas de SVG impliqué |
| 3 | Verre appliqué au contenu (listes, media) | Verre réservé à la couche de navigation flottante |
| 4 | Ignorer les materials Apple | `ultraThinMaterial` / `thinMaterial` / `regularMaterial` sont la base |
| 5 | `.glassEffect()` sans forme définie | Toujours spécifier `.glassEffect(in: .rect(cornerRadius: 16))` ou utiliser Material |
| 6 | Animation linéaire | Toujours spring : `.spring(response: 0.6, dampingFraction: 0.7)` |
| 7 | Pas de dark mode | Toujours `@media (prefers-color-scheme: dark)` |
| 8 | Coins droits (< 12px) | Rayon minimum 12px sur les surfaces (14px pour cartes modernes) |
| 9 | Verre sur verre | Grouper avec `GlassEffectContainer` ou espacement suffisant |
| 10 | Oublier `.interactive()` sur éléments tactiles | Toujours ajouter `.interactive()` pour retour tactile |
| 11 | Pas de border subtile | Toujours ajouter `.strokeBorder(.white.opacity(0.2))` |
| 12 | Ignorer les états pressed | Toujours ajouter `scaleEffect(0.97)` sur pressed (CardButtonStyle) |
| 13 | Verre sans background content | Le verre a besoin de contenu derrière pour briller |
| 14 | Toolbar items dispersés | Grouper avec `ToolbarItemGroup` et `ToolbarSpacer(.flexible)` |
| 15 | Auto-anim avec Timer | Utiliser `.task` + `Task.sleep(for: .seconds(1.5))` |
| 16 | Oublier Equatable | Implémenter `Equatable` sur toutes les vues SwiftUI pour diffing optimal |

## Checklist de livraison

- [ ] Matériau choisi : ultraThin / thin / regular / thick (Apple) ou transposition CSS correspondante
- [ ] `.glassEffect()` utilisé sur la couche de navigation, pas sur le contenu
- [ ] Forme définie : `.rect(cornerRadius: 16)` ou `.circle` ou `RoundedRectangle`
- [ ] Transitions en spring : `.spring(response: 0.6, dampingFraction: 0.7)` ou CSS équivalent
- [ ] Tous les états : default / hover / pressed / disabled
- [ ] Dark mode natif
- [ ] Contraste texte ≥ 90% sur fond verre
- [ ] `safe-area-inset` respecté (bottom = `calc(34px + 10px)`)
- [ ] Fallback `@supports not (backdrop-filter)`
- [ ] `will-change: transform` sur éléments animés (performance)
- [ ] Bordure subtile : `.overlay(strokeBorder(.white.opacity(0.2)))`
- [ ] Ombre portée : `.shadow(color: .black.opacity(0.08), radius: 12, y: 4)`
- [ ] Composition vérifiée : material + border + shadow + highlight
- [ ] Groupement toolbar si plusieurs actions (`ToolbarItemGroup` + `ToolbarSpacer`)
- [ ] Vue SwiftUI conforme `Equatable` pour diffing optimal
- [ ] Auto-animations via `.task` + `Task.sleep`, pas via `Timer`

## Matériaux Apple — tableau de transposition

| Apple Material | CSS background | CSS backdrop-filter | Usage source |
|---|---|---|---|
| `.ultraThinMaterial` | `rgba(255,255,255,0.06)` | `blur(40px) saturate(180%) brightness(115%)` | `ChapterDetailView.swift:49`, `MaterialHierarchyDemo.swift:92` |
| `.thinMaterial` | `rgba(255,255,255,0.10)` | `blur(20px) saturate(180%) brightness(110%)` | `ToolbarGlassDemo.swift:208`, `KeyPointsCard.swift:22` |
| `.regularMaterial` | `rgba(255,255,255,0.18)` | `blur(12px) saturate(160%) brightness(105%)` | `PickerGlassDemo.swift:136` |
| `.thickMaterial` | `rgba(255,255,255,0.28)` | `blur(8px) saturate(150%) brightness(100%)` | `MaterialHierarchyDemo.swift:95` |
