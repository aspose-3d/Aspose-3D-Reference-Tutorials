---
date: 2026-02-25
description: Erfahren Sie, wie Sie das Koordinatensystem umkehren und den 3D‑Import
  mit Aspose.3D LoadOptions in Java anpassen. Schritt‑für‑Schritt‑Anleitung für 3DS,
  OBJ, STL, U3D, glTF, PLY, X und optional FBX.
linktitle: Customize 3D File Loading in Java with Aspose.3D LoadOptions
second_title: Aspose.3D Java API
title: Koordinatensystem umkehren – Laden von 3D‑Dateien in Java mit Aspose.3D anpassen
url: /de/java/load-and-save/customize-3d-file-loading/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Koordinatensystem umkehren – 3D-Dateiladen in Java mit Aspose.3D anpassen

In der sich ständig weiterentwickelnden Landschaft von 3D-Design und -Entwicklung ist das **Umkehren des Koordinatensystems** beim Importieren von Modellen ein häufiges Anliegen. Egal, ob Sie Assets von einem rechtshändigen zu einem linkshändigen System konvertieren oder Modelle an die Achsenkonventionen Ihrer Engine anpassen müssen, Aspose.3D für Java bietet Ihnen feinkörnige Kontrolle. Dieses Tutorial führt Sie Schritt für Schritt, wie Sie den **3D-Import anpassen** können, indem Sie Aspose.3D’s `LoadOptions` verwenden, und deckt die beliebtesten Formate wie 3DS, OBJ, STL, U3D, glTF, PLY, X und das optionale FBX ab.

## Schnelle Antworten
- **Was bewirkt das „Koordinatensystem umkehren“?** Es vertauscht die X/Y/Z-Achsen, um der Zielkoordinatenkonvention zu entsprechen.  
- **Welche Formate unterstützen das Umkehren?** Alle gängigen Formate (3DS, OBJ, STL, U3D, glTF, PLY, X, FBX) stellen eine `setFlipCoordinateSystem`‑Option bereit.  
- **Benötige ich zusätzliche Bibliotheken?** Nur das Aspose.3D für Java JAR; externe Konverter sind nicht erforderlich.  
- **Kann ich gleichzeitig Materialien laden?** Ja – verwenden Sie `setEnableMaterials(true)` für OBJ‑Dateien.  
- **Wird für die Produktion eine Lizenz benötigt?** Eine gültige Aspose.3D‑Lizenz ist für Nicht‑Test‑Einsätze erforderlich.

## Was ist das „Koordinatensystem umkehren“?
Das Umkehren des Koordinatensystems ändert die Orientierung der Achsen, die vom importierten Modell verwendet werden. Dies ist entscheidend, wenn die Quelldatei eine andere Händigkeit (rechtshändig vs. linkshändig) als Ihre Rendering‑Engine nutzt, um zu verhindern, dass Modelle gespiegelt oder invertiert erscheinen.

## Warum den 3D-Import anpassen?
- Animationstransformationen beibehalten (`setApplyAnimationTransform`).  
- Korrekte Farbbearbeitung (`setGammaCorrectedColor`).  
- Auflösung externer Ressourcenpfade über `getLookupPaths()`.  
- Speichernutzung optimieren, indem nur das Notwendige geladen wird.

## Voraussetzungen

- Grundlegendes Verständnis der Java-Programmierung.  
- Installiertes Java Development Kit (JDK).  
- Aspose.3D für Java Bibliothek heruntergeladen. Sie können sie [hier](https://releases.aspose.com/3d/java/) erhalten.  
- Vertrautheit mit 3D-Dateiformaten wie 3DS, OBJ, STL, U3D, glTF, PLY, X und FBX.

## Importieren von Paketen

In Ihrem Java‑Projekt stellen Sie sicher, dass Sie die erforderlichen Aspose.3D‑Pakete importieren:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Wie man den 3D-Import mit LoadOptions anpasst

Im Folgenden finden Sie Schritt‑für‑Schritt‑Code‑Snippets, die zeigen, wie Sie die **flip coordinate system**‑Option für jedes unterstützte Format aktivieren. Die Snippets können direkt in Ihr Projekt kopiert werden; ersetzen Sie einfach `"Your Document Directory"` durch den tatsächlichen Pfad zu Ihren Assets.

### Schritt 1: Anpassen des 3DS‑Dateiladens

```java
public static void discreet3DSLoadOption() {
    String MyDir = "Your Document Directory";
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();
    loadOpts.setApplyAnimationTransform(true);
    loadOpts.setFlipCoordinateSystem(true);
    loadOpts.setGammaCorrectedColor(true);
    loadOpts.getLookupPaths().add(MyDir);
}
```

### Schritt 2: Anpassen des OBJ‑Dateiladens

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### Schritt 3: Anpassen des STL‑Dateiladens

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### Schritt 4: Anpassen des U3D‑Dateiladens

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### Schritt 5: Anpassen des glTF‑Dateiladens

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### Schritt 6: Anpassen des PLY‑Dateiladens

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### Schritt 7: Anpassen des X‑Dateiladens

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### Schritt 8: Anpassen des FBX‑Dateiladens (Optional)

```java
private static void FBXLoadOptions() throws IOException {
    String dataDir = "Your Document Directory";
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions();
    opt.setKeepBuiltinGlobalSettings(true);
    scene.open(dataDir + "test.FBX", opt);
    for(Property property:scene.getRootNode().getAssetInfo().getProperties()) {
        System.out.println(property);
    }
}
```

## Häufige Probleme und Lösungen
- **Modell erscheint nach dem Laden gespiegelt** – Stellen Sie sicher, dass `setFlipCoordinateSystem(true)` für das richtige Format gesetzt ist.  
- **Materialien fehlen** – Für OBJ‑Dateien stellen Sie sicher, dass `setEnableMaterials(true)` gesetzt ist und dass die Materialdateien (.mtl) in einem der Lookup‑Pfade liegen.  
- **Texturkoordinaten sind umgekehrt** – Für glTF benötigen Sie möglicherweise `setFlipTexCoordV(true)` zusätzlich zum Umkehren der Achsen.  
- **Datei‑nicht‑gefunden‑Fehler** – Fügen Sie das Verzeichnis, das externe Ressourcen (Texturen, Hilfsdateien) enthält, zu `loadOpts.getLookupPaths()` hinzu.

## Fazit

Durch die Nutzung von Aspose.3D’s `LoadOptions` können Sie das **Koordinatensystem umkehren** und den **3D-Import anpassen** für praktisch jedes gängige Format. Dieses Maß an Kontrolle eliminiert die Notwendigkeit von Nachbearbeitungsskripten und stellt sicher, dass Ihre Assets beim ersten Mal korrekt gerendert werden.

## Häufig gestellte Fragen

### Q1: Wo finde ich die Aspose.3D für Java Dokumentation?
A1: Die Dokumentation ist [hier](https://reference.aspose.com/3d/java/) verfügbar.

### Q2: Wie kann ich Aspose.3D für Java herunterladen?
A2: Sie können es [hier](https://releases.aspose.com/3d/java/) herunterladen.

### Q3: Gibt es eine kostenlose Testversion?
A3: Ja, Sie können die kostenlose Testversion [hier](https://releases.aspose.com/) nutzen.

### Q4: Wo bekomme ich Support für Aspose.3D für Java?
A4: Besuchen Sie das Support‑Forum [hier](https://forum.aspose.com/c/3d/18).

### Q5: Benötige ich eine temporäre Lizenz für Tests?
A5: Ja, erhalten Sie eine temporäre Lizenz [hier](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2026-02-25  
**Tested With:** Aspose.3D for Java 24.11 (latest)  
**Author:** Aspose