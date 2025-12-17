---
date: 2025-12-12
description: Erfahren Sie, wie Sie die Materialfarbe festlegen, während Sie Mesh‑Geometriedaten
  teilen und die Szene in Java 3D mit Aspose.3D als FBX speichern.
linktitle: Set Material Color and Share Mesh Geometry Data in Java 3D with Aspose.3D
second_title: Aspose.3D Java API
title: Materialfarbe festlegen und Mesh‑Geometriedaten in Java 3D mit Aspose.3D teilen
url: /de/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Materialfarbe festlegen und Mesh-Geometriedaten in Java 3D mit Aspose.3D teilen

## Einführung

Ein Einstieg in die Welt von Java 3D mit Aspose.3D eröffnet zahlreiche Möglichkeiten, atemberaubende Visualisierungen und immersive Erlebnisse zu schaffen. In diesem Tutorial führen wir Sie durch **wie man Mesh**-Geometriedaten in Java 3D mit Aspose.3D teilt, und zeigen Ihnen genau **wie man die Materialfarbe** für jede Mesh-Instanz festlegt. Befolgen Sie jeden Schritt sorgfältig, und am Ende können Sie Mesh-Daten nahtlos zwischen mehreren Nodes austauschen, Farben steuern und nach FBX exportieren.

## Schnelle Antworten
- **Was ist das Hauptziel?** Materialfarbe für jeden Node festlegen und Mesh-Geometriedaten teilen.  
- **Welche Bibliothek wird benötigt?** Aspose.3D für Java.  
- **Wie exportiere ich das Ergebnis?** Die Szene als FBX-Datei (FBX7400ASCII) speichern.  
- **Benötige ich eine Lizenz?** Für den Produktionseinsatz ist eine temporäre oder vollständige Lizenz erforderlich.  
- **Welche Java-Version funktioniert?** Jede Java‑8‑+ Umgebung.

## Voraussetzungen

Bevor wir mit dem Tutorial beginnen, stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind:

- Java-Entwicklungsumgebung: Stellen Sie sicher, dass auf Ihrem System eine Java-Entwicklungsumgebung eingerichtet ist.  
- Aspose.3D-Bibliothek: Laden Sie die Aspose.3D-Bibliothek herunter und installieren Sie sie. Sie finden die Bibliothek [hier](https://releases.aspose.com/3d/java/).

## Pakete importieren

Beginnen Sie damit, die erforderlichen Pakete in Ihr Java‑Projekt zu importieren. Dieser Schritt ist entscheidend, um auf die von der Aspose.3D‑Bibliothek bereitgestellten Funktionen zuzugreifen.

```java
import com.aspose.threed.*;
```

## Schritt 1: Szenenobjekt initialisieren (initialize scene java)

Starten wir den Prozess, indem wir ein Szenenobjekt initialisieren. Dieses dient als Leinwand, auf der unsere 3D‑Magie entfaltet wird.

```java
// Initialize scene object
Scene scene = new Scene();
```

## Schritt 2: Farbvektoren definieren

In diesem Schritt definieren wir ein Array von Farbvektoren, die auf verschiedene Elemente unserer 3D‑Szene angewendet werden.

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## Schritt 3: 3D-Mesh in Java mit Polygon Builder erstellen (create 3d mesh java)

Verwenden Sie die Common‑Klasse, um mit der Polygon‑Builder‑Methode ein Mesh zu erstellen. Dieses Mesh bildet die Grundlage für unsere 3D‑Elemente.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Wie legt man die Materialfarbe für jeden Node fest?

Iterieren Sie über die Farbvektoren, erstellen Sie Würfel‑Nodes und setzen Sie Attribute wie Material, **Materialfarbe festlegen** und Translation. Dies ist der Kern der Steuerung des visuellen Erscheinungsbildes jeder Mesh‑Instanz.

```java
int idx = 0;
for(Vector3 color : colors) {
    // Initialize cube node object
    Node cube = new Node("cube");
    cube.setEntity(mesh);
    LambertMaterial mat = new LambertMaterial();
    // Set color
    mat.setDiffuseColor(color);
    // Set material
    cube.setMaterial(mat);
    // Set translation
    cube.getTransform().setTranslation(new Vector3(idx++ * 20, 0, 0));
    // Add cube node
    scene.getRootNode().addChildNode(cube);
}
```

## Schritt 5: 3D‑Szene speichern (save scene fbx, convert mesh to fbx)

Geben Sie das Verzeichnis und den Dateinamen an, um die 3D‑Szene im unterstützten Dateiformat zu speichern, in diesem Fall FBX7400ASCII. Dieser Schritt demonstriert zudem **Mesh in FBX konvertieren**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Fazit

Herzlichen Glückwunsch! Sie haben erfolgreich **die Materialfarbe festgelegt**, Mesh‑Geometriedaten zwischen mehreren Nodes geteilt und das Ergebnis als FBX‑Datei mit Aspose.3D für Java exportiert. Dies eröffnet unzählige Möglichkeiten, visuell beeindruckende und interaktive 3D‑Anwendungen zu erstellen.

## FAQ

### Q1: Kann ich Aspose.3D mit anderen Java‑Frameworks verwenden?

A1: Ja, Aspose.3D ist so konzipiert, dass es nahtlos mit verschiedenen Java‑Frameworks funktioniert.

### Q2: Gibt es Lizenzoptionen für Aspose.3D?

A2: Ja, Sie können Lizenzoptionen [hier](https://purchase.aspose.com/buy) erkunden.

### Q3: Wie kann ich Support für Aspose.3D erhalten?

A3: Besuchen Sie das Aspose.3D [Forum](https://forum.aspose.com/c/3d/18) für Support und Diskussionen.

### Q4: Gibt es eine kostenlose Testversion?

A4: Ja, Sie können eine kostenlose Testversion [hier](https://releases.aspose.com/) erhalten.

### Q5: Wie erhalte ich eine temporäre Lizenz für Aspose.3D?

A5: Sie können eine temporäre Lizenz [hier](https://purchase.aspose.com/temporary-license/) erhalten.

## Zusätzliche häufig gestellte Fragen

**F: Kann ich die Szene in andere Formate als FBX exportieren?**  
A: Ja, Aspose.3D unterstützt OBJ, STL, 3MF und weitere. Ändern Sie einfach das `FileFormat`‑Enum im `save`‑Aufruf.

**F: Was, wenn ich das Material ändern muss, nachdem die Szene erstellt wurde?**  
A: Rufen Sie den Node ab, ändern Sie dessen `LambertMaterial` (z. B. `setDiffuseColor`) und speichern Sie die Szene erneut.

**F: Handhabt die Bibliothek große Meshes effizient?**  
A: Aspose.3D verwendet optimierte Datenstrukturen; bei extrem großen Meshes sollten Sie jedoch Streaming oder das Aufteilen der Szene in Betracht ziehen.

**F: Gibt es eine Möglichkeit, die Farbänderung zu animieren?**  
A: Ja, Sie können Materialeigenschaften mit der `AnimationController`‑API animieren.

---

**Last Updated:** 2025-12-12  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}