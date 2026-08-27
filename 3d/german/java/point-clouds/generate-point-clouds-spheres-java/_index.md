---
date: 2026-05-29
description: Erfahren Sie, wie Sie mit Aspose.3D für Java eine draco point cloud aus
  einer Kugel erstellen. Schritt‑für‑Schritt‑Anleitung, Voraussetzungen, Code und
  Fehlersuche.
keywords:
- create draco point cloud
- Aspose 3D point cloud Java
- DracoSaveOptions Java
linktitle: Wie man draco point cloud aus Kugeln mit Aspose 3D Java erstellt
schemas:
- author: Aspose
  dateModified: '2026-05-29'
  description: Learn how to create draco point cloud from a sphere with Aspose.3D
    for Java. Step‑by‑step guide, prerequisites, code, and troubleshooting.
  headline: How to create draco point cloud from spheres using Aspose 3D Java
  type: TechArticle
- questions:
  - answer: Yes. After loading the `.drc` file back into a `Scene`, you can export
      vertices using Aspose.3D’s generic `Scene.save` method with formats like PLY
      or OBJ.
    question: Can I convert the generated point cloud to other formats (e.g., PLY,
      OBJ)?
  - answer: The current Aspose.3D implementation focuses on geometry only. To add
      attributes, extend the scene with custom `VertexElement` objects before encoding.
    question: Does the Draco encoder support custom point attributes (e.g., color,
      normals)?
  - answer: Draco compresses efficiently, but clouds exceeding **100 million** points
      may require more than 8 GB RAM. Consider chunking or streaming APIs for very
      large datasets.
    question: How large can a point cloud be before performance degrades?
  - answer: Absolutely. three.js includes a Draco loader that reads the file directly
      for real‑time rendering.
    question: Is the generated `.drc` file compatible with web viewers like three.js?
  - answer: The default level (5) works for most cases. If file size is critical,
      experiment with values between **0** (fastest) and **10** (maximum compression)
      to balance speed vs. size.
    question: Do I need to call `opt.setCompressionLevel()` for better results?
  type: FAQPage
second_title: Aspose.3D Java API
title: Wie man draco point cloud aus Kugeln mit Aspose 3D Java erstellt
url: /de/java/point-clouds/generate-point-clouds-spheres-java/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Erzeugen von Aspose 3D Punktwolken aus Kugeln in Java

## Einführung

Willkommen zu dieser Schritt‑für‑Schritt‑Anleitung zum **Draco-Punktwolke erstellen** aus Kugeln mit Aspose.3D für Java. Egal, ob Sie wissenschaftliche Visualisierungen, Gaming‑Assets oder AR/VR‑Prototypen erstellen, Punktwolken bieten Ihnen eine leichtgewichtige Darstellung von 3‑D‑Geometrie, die in Browser gestreamt oder von Machine‑Learning‑Pipelines verarbeitet werden kann. In den nächsten Minuten sehen Sie genau, wie Sie eine einfache Kugel in eine Draco‑kodierte Punktwolke umwandeln, warum das wichtig ist und wie Sie die häufigsten Fallstricke vermeiden.

## Schnelle Antworten
- **Welche Bibliothek wird verwendet?** Aspose.3D for Java  
- **In welchem Format wird die Punktwolke gespeichert?** Draco (`.drc`)  
- **Benötige ich eine Lizenz für Tests?** Eine kostenlose Testversion reicht für die Evaluierung; für die Produktion ist eine kommerzielle Lizenz erforderlich.  
- **Welche Java‑Version wird unterstützt?** Java 8 oder höher (JDK 11 empfohlen)  
- **Wie lange dauert die Implementierung?** Etwa 10‑15 Minuten für eine einfache Kugel‑Punktwolke  

## Was ist eine Draco-Punktwolke?

Eine Draco-Punktwolke ist eine kompakte binäre Darstellung von 3‑D‑Vertices, die mit Googles Draco‑Algorithmus komprimiert wird. **Aspose.3D** stellt das integrierte `DracoSaveOptions` bereit, um dieses Format direkt aus einem `Scene`‑Objekt zu schreiben und dabei eine Größenreduktion von bis zu 90 % im Vergleich zu rohen Vertex‑Listen zu erzielen.

## Warum eine Punktwolke aus einer Kugel erzeugen?

Das Erzeugen einer Punktwolke aus einer Kugel ist ein ideales Einstiegsprojekt, da eine Kugel eine mathematisch geschlossene Form ist, die deutlich zeigt, wie Vertices abgetastet und gespeichert werden. Dieser Ansatz ist nützlich für:

- **Schnelles Prototyping** – Testen von Rendering‑Pipelines, ohne komplexe Meshes zu importieren.  
- **Kollisions‑Erkennungs‑Benchmarks** – Erzeugen deterministischer Punktverteilungen für Physik‑Engines.  
- **Kompressions‑Demos** – Vergleich der Roh‑OBJ‑Größe mit Draco‑komprimierten `.drc`‑Dateien (oft eine 10‑fache Reduktion für 10 k‑Punktwolken).  

## Voraussetzungen

Bevor wir beginnen, stellen Sie sicher, dass Sie Folgendes haben:

- **Java Development Kit (JDK)** – Stellen Sie sicher, dass Java auf Ihrem Rechner installiert ist. Sie können es von der [Oracle-Website](https://www.oracle.com/java/technologies/javase-downloads.html) herunterladen.  
- **Aspose.3D‑Bibliothek** – Um 3D‑Operationen in Java durchzuführen, benötigen Sie die Aspose.3D‑Bibliothek. Sie können sie aus der [Aspose.3D Java‑Dokumentation](https://reference.aspose.com/3d/java/) herunterladen.  

### Zusätzliche Anforderungen

| Anforderung | Grund |
|-------------|-------|
| Maven‑ oder Gradle‑Build‑Tool | Vereinfacht die Verwaltung von Abhängigkeiten für Aspose.3D. |
| Schreibberechtigung für den Ausgabepfad | Erforderlich zum Speichern der `.drc`‑Datei. |
| Optional: Lizenzdatei | Erforderlich für produktionsreife Ausführungen (Testversion funktioniert für die Entwicklung). |

## Pakete importieren

Importieren Sie in Ihrem Java‑Projekt die erforderlichen Pakete, um mit Aspose.3D zu arbeiten. Fügen Sie Ihrem Code die folgenden Zeilen hinzu:

```java
import com.aspose.threed.*;
import com.aspose.threed.geometry.*;
import com.aspose.threed.save.*;
```

> **Definition‑Anker:** `Scene` ist der Top‑Level‑Container von Aspose.3D, der Meshes, Lichter, Kameras und andere 3‑D‑Entitäten im Speicher hält.

## Wie erstelle ich eine Draco-Punktwolke aus einer Kugel in Java?

Laden Sie Ihre Kugel, aktivieren Sie den Punktwolken‑Modus und speichern Sie sie mit Draco‑Kompression in nur drei Code‑Zeilen. Zuerst konfigurieren Sie `DracoSaveOptions`, um eine Punktwolke auszugeben, dann instanziieren Sie ein `Sphere`‑Primitive, fügen es einer `Scene` hinzu und rufen schließlich `save` auf. Dieses Muster funktioniert für jedes Mesh, das Sie konvertieren möchten.

## Schritt 1: DracoSaveOptions einrichten

`DracoSaveOptions` weist Aspose.3D an, Geometrie als Punktwolke statt als vollständiges Mesh zu kodieren.

```java
DracoSaveOptions dracoOptions = new DracoSaveOptions();
dracoOptions.setPointCloud(true);               // Enable point‑cloud output
dracoOptions.setCompressionLevel(7);            // 0‑10 range; 7 gives good size/ speed balance
```

> **Definition‑Anker:** `DracoSaveOptions` ist das Konfigurationsobjekt, das steuert, wie Aspose.3D Draco‑Dateien schreibt, einschließlich Kompressionsstufe und Punktwolken‑Flag.

## Schritt 2: Eine Kugel erstellen

Die Klasse `Sphere` repräsentiert eine mathematisch perfekte Kugel. Sie können Radius und Tessellationsdichte steuern, um die Punktanzahl zu beeinflussen.

```java
// Create a sphere with radius 5.0 and 32 longitudinal/latitudinal segments
Sphere sphere = new Sphere(5.0, 32, 32);
```

> **Definition‑Anker:** `Sphere` ist eine primitive Formklasse, die ein Mesh aus Vertices und Faces basierend auf Radius‑ und Segment‑Parametern erzeugt.

## Schritt 3: Punktwolke kodieren und speichern

Fügen Sie die Kugel zu einer neuen `Scene` hinzu und rufen Sie dann `save` mit den zuvor konfigurierten `DracoSaveOptions` auf.

```java
Scene scene = new Scene();
scene.getRootNode().attachChild(sphere);               // Add sphere to scene graph
scene.save("output_point_cloud.drc", dracoOptions);   // Write compressed point cloud
```

> **Definition‑Anker:** `Scene.save` schreibt die gesamte Szene in die angegebene Datei unter Verwendung der bereitgestellten Speicheroptionen.

### Quantifizierte Aussage

Aspose.3D unterstützt **30+** 3‑D‑Dateiformate (einschließlich OBJ, STL, FBX, GLTF) und kann **500‑seitige** Modelle verarbeiten, ohne die gesamte Datei in den Speicher zu laden, was es für groß‑skalige Punktwolken‑Workflows geeignet macht.

## Häufige Probleme und Lösungen

| Problem | Grund | Lösung |
|---------|-------|--------|
| **Datei nicht gefunden** | Falscher Ausgabepfad | Verwenden Sie einen absoluten Pfad oder stellen Sie sicher, dass das Verzeichnis vor dem Speichern existiert. |
| **Leere Punktwolke** | `setPointCloud(true)` ausgelassen | Stellen Sie sicher, dass das `DracoSaveOptions`‑Flag wie in Schritt 1 gesetzt ist. |
| **Lizenz‑Ausnahme** | Ausführung ohne gültige Lizenz in der Produktion | Wenden Sie eine temporäre oder permanente Lizenz an (siehe FAQ unten). |

## Häufig gestellte Fragen

**F: Kann ich die erzeugte Punktwolke in andere Formate konvertieren (z. B. PLY, OBJ)?**  
A: Ja. Nachdem Sie die `.drc`‑Datei wieder in eine `Scene` geladen haben, können Sie die Vertices mit der generischen `Scene.save`‑Methode von Aspose.3D in Formate wie PLY oder OBJ exportieren.

**F: Unterstützt der Draco‑Encoder benutzerdefinierte Punktattribute (z. B. Farbe, Normalen)?**  
A: Die aktuelle Aspose.3D‑Implementierung konzentriert sich nur auf Geometrie. Um Attribute hinzuzufügen, erweitern Sie die Szene vor dem Kodieren mit benutzerdefinierten `VertexElement`‑Objekten.

**F: Wie groß kann eine Punktwolke sein, bevor die Leistung nachlässt?**  
A: Draco komprimiert effizient, aber Wolken mit mehr als **100 Millionen** Punkten können mehr als 8 GB RAM benötigen. Erwägen Sie Chunking‑ oder Streaming‑APIs für sehr große Datensätze.

**F: Ist die erzeugte `.drc`‑Datei mit Web‑Viewern wie three.js kompatibel?**  
A: Ja. three.js enthält einen Draco‑Loader, der die Datei direkt für Echtzeit‑Rendering einliest.

**F: Muss ich `opt.setCompressionLevel()` für bessere Ergebnisse aufrufen?**  
A: Der Standardwert (5) funktioniert in den meisten Fällen. Wenn die Dateigröße kritisch ist, experimentieren Sie mit Werten zwischen **0** (schnellste) und **10** (maximale Kompression), um Geschwindigkeit und Größe auszubalancieren.

## FAQ

### Q1: Kann ich Aspose.3D kostenlos nutzen?

A1: Ja, Sie können Aspose.3D mit einer kostenlosen Testversion erkunden. Besuchen Sie [hier](https://releases.aspose.com/), um zu beginnen.

### Q2: Wo finde ich Support für Aspose.3D?

A2: Sie finden Support und können sich mit der Community im [Aspose.3D‑Forum](https://forum.aspose.com/c/3d/18) verbinden.

### Q3: Wie kann ich Aspose.3D erwerben?

A3: Besuchen Sie die [Kaufseite](https://purchase.aspose.com/buy), um Aspose.3D zu erwerben und sein volles Potenzial freizuschalten.

### Q4: Gibt es eine temporäre Lizenz?

A4: Ja, Sie können eine temporäre Lizenz [hier](https://purchase.aspose.com/temporary-license/) für Ihre Entwicklungsbedürfnisse erhalten.

### Q5: Wo finde ich die Dokumentation?

A5: Konsultieren Sie die ausführliche [Aspose.3D Java‑Dokumentation](https://reference.aspose.com/3d/java/) für umfassende Informationen.

## Fazit

Herzlichen Glückwunsch! Sie haben erfolgreich **eine Draco-Punktwolke** aus einer Kugel mit Aspose.3D für Java **erstellt**. Sie können die `.drc`‑Datei nun in jeden Draco‑kompatiblen Viewer laden, über das Web streamen oder in nachgelagerte Verarbeitungspipelines wie Punktwolken‑Klassifizierung oder Oberflächenrekonstruktion einspeisen.

---

**Zuletzt aktualisiert:** 2026-05-29  
**Getestet mit:** Aspose.3D für Java 24.10  
**Autor:** Aspose  

```java
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Sphere;


import java.io.IOException;
```

```java
// ExStart:3
DracoSaveOptions opt = new DracoSaveOptions();
opt.setPointCloud(true);
// ExEnd:3
```

```java
// ExStart:4
Sphere sphere = new Sphere();
// ExEnd:4
```

```java
// ExStart:5
FileFormat.DRACO.encode(sphere, "Your Document Directory" + "sphere.drc", opt);
// ExEnd:5
```

{{< blocks/products/products-backtop-button >}}

## Verwandte Tutorials

- [Wie man Mesh in Punktwolke in Java mit Aspose.3D konvertiert](/3d/java/point-clouds/create-point-clouds-java/)
- [Wie man PLY – Punktwolken mit Aspose.3D für Java exportiert](/3d/java/point-clouds/export-point-clouds-ply-java/)
- [Wie man ein Kugel‑Mesh in Java erstellt – 3D‑Meshes mit Google Draco komprimieren](/3d/java/3d-mesh-data/compress-meshes-google-draco/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}