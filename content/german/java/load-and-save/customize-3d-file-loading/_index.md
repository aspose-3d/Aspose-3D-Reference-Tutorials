---
title: Passen Sie das Laden von 3D-Dateien in Java mit Aspose.3D LoadOptions an
linktitle: Passen Sie das Laden von 3D-Dateien in Java mit Aspose.3D LoadOptions an
second_title: Aspose.3D Java-API
description: Verbessern Sie das Laden Ihrer 3D-Dateien in Java mit den anpassbaren LoadOptions von Aspose.3D. Erfahren Sie Schritt-für-Schritt-Anpassungen für 3DS, OBJ, STL, U3D, glTF, PLY, X und optionales FBX.
type: docs
weight: 12
url: /de/java/load-and-save/customize-3d-file-loading/
---
## Einführung

In der sich ständig weiterentwickelnden Landschaft des 3D-Designs und der 3D-Entwicklung ist der effiziente Umgang mit 3D-Dateiformaten von entscheidender Bedeutung. Aspose.3D für Java bietet eine leistungsstarke Lösung zum Anpassen des Ladens verschiedener 3D-Dateiformate. Dieses Tutorial führt Sie durch den Prozess der Anpassung des Ladens von 3D-Dateien in Java mithilfe der LoadOptions von Aspose.3D.

## Voraussetzungen

Bevor Sie mit dem Anpassungsprozess beginnen, stellen Sie sicher, dass Sie über Folgendes verfügen:

- Grundlegendes Verständnis der Java-Programmierung.
- Installiertes Java Development Kit (JDK).
-  Aspose.3D für Java-Bibliothek heruntergeladen. Sie können es erhalten[Hier](https://releases.aspose.com/3d/java/).
- Vertrautheit mit 3D-Dateiformaten wie 3DS, OBJ, STL, U3D, glTF, PLY, X und FBX.

## Pakete importieren

Stellen Sie in Ihrem Java-Projekt sicher, dass Sie die erforderlichen Aspose.3D-Pakete importieren:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Passen Sie das Laden von 3D-Dateien an

### Schritt 1: Passen Sie das Laden der 3DS-Datei an

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

### Schritt 2: Passen Sie das Laden der OBJ-Datei an

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### Schritt 3: Passen Sie das Laden der STL-Datei an

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### Schritt 4: Passen Sie das Laden der U3D-Datei an

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### Schritt 5: Passen Sie das Laden der glTF-Datei an

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### Schritt 6: Passen Sie das Laden der PLY-Datei an

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### Schritt 7: Passen Sie das Laden der X-Datei an

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### Schritt 8: Anpassen des FBX-Dateiladens (optional)

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

## Abschluss

Durch das Anpassen des Ladens von 3D-Dateien in Java mit LoadOptions von Aspose.3D können Entwickler den Importvorgang an spezifische Anforderungen anpassen. Ob es darum geht, Animationstransformationen anzupassen, Koordinatensysteme umzudrehen oder externe Abhängigkeiten zu handhaben, Aspose.3D bietet die Flexibilität, die für eine nahtlose Integration erforderlich ist.

## FAQs

### F1: Wo finde ich die Dokumentation zu Aspose.3D für Java?

 A1: Die Dokumentation ist verfügbar[Hier](https://reference.aspose.com/3d/java/).

### F2: Wie kann ich Aspose.3D für Java herunterladen?

 A2: Sie können es herunterladen[Hier](https://releases.aspose.com/3d/java/).

### F3: Gibt es eine kostenlose Testversion?

 A3: Ja, Sie können auf die kostenlose Testversion zugreifen[Hier](https://releases.aspose.com/).

### F4: Wo erhalte ich Unterstützung für Aspose.3D für Java?

 A4: Besuchen Sie das Support-Forum[Hier](https://forum.aspose.com/c/3d/18).

### F5: Benötige ich zum Testen eine temporäre Lizenz?

 A5: Ja, besorgen Sie sich eine temporäre Lizenz[Hier](https://purchase.aspose.com/temporary-license/).