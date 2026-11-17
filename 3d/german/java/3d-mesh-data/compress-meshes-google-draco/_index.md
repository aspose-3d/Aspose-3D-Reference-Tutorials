---
date: 2026-11-17
description: Wie man die Größe von 3D-Modellen reduziert, indem man in Java ein Sphären‑Mesh
  erzeugt und es mit Google Draco über Aspose.3D komprimiert. Lernen Sie den kompletten
  Workflow in wenigen Minuten.
images:
- /java/3d-mesh-data/compress-meshes-google-draco/og-image.png
keywords:
- create sphere mesh
- how to compress 3d
- reduce 3d model size
- aspose 3d java
- compress 3d mesh
lastmod: 2026-11-17
linktitle: Wie man die Größe von 3D-Modellen reduziert – Sphären‑Mesh in Java mit
  Google Draco erstellen
og_description: Sphären‑Mesh erstellen und 3D-Modell mit Java mittels Aspose.3D und
  Google Draco komprimieren. Dieses Tutorial zeigt, wie man eine Kugel erzeugt, in
  .drc exportiert und in wenigen Minuten eine Größenreduktion von bis zu 95 % erzielt.
og_image_alt: 'Developer guide: Reduce 3d model size with Java sphere mesh and Draco
  compression'
og_title: Sphären‑Mesh erstellen und 3D-Modell mit Java und Draco komprimieren
schemas:
- author: Aspose
  dateModified: '2026-11-17'
  description: How to reduce 3d model size by generating a sphere mesh in Java and
    compressing it with Google Draco via Aspose.3D. Learn the full workflow in minutes.
  headline: How to reduce 3d model size with a Java sphere mesh and Draco
  type: TechArticle
- description: How to reduce 3d model size by generating a sphere mesh in Java and
    compressing it with Google Draco via Aspose.3D. Learn the full workflow in minutes.
  name: How to reduce 3d model size with a Java sphere mesh and Draco
  steps:
  - name: set up the project
    text: Create a new Java project (any IDE works) and add all Aspose.3D JARs to
      the classpath. Keep your source files in a package such as `com.example.draco`
      for clarity.
  - name: how to create sphere mesh in Java
    text: 'The `Sphere` class is Aspose.3D''s built‑in geometry generator that produces
      a triangulated mesh with a configurable radius and tessellation. > **Pro tip:**
      The `Sphere` class generates a triangulated mesh with a default radius of 1.0.
      You can pass custom radius, tessellation, or material parameters '
  - name: export the mesh to Draco format
    text: After the sphere is added to a `Scene` object, call `scene.save("sphere.drc",
      SaveFormat.Draco)`. Aspose.3D automatically selects optimal compression settings,
      but you can fine‑tune them by adjusting `DracoCompressionOptions` if you need
      the smallest possible file. `DracoCompressionOptions` lets you
  - name: verify the output
    text: Open the generated `.drc` file with a Draco viewer (e.g., three.js `DRACOLoader`)
      to ensure the geometry renders correctly. You’ll notice a dramatic reduction
      in file size—often a factor of ten or more.
  type: HowTo
- questions:
  - answer: Yes, Aspose.3D supports OBJ, FBX, STL, GLTF, and many others, making it
      a versatile choice for **Aspose 3d export** pipelines.
    question: Is Aspose.3D compatible with different 3d file formats?
  - answer: Absolutely. Draco offers native libraries for C++, Python, and JavaScript.
      This tutorial focuses on Java, but the concepts apply across languages.
    question: Can I use Google Draco for compression in other programming languages?
  - answer: Visit the **[Aspose.3D Java documentation](https://reference.aspose.com/3d/java/)**
      for full API references and more examples.
    question: Where can I find additional Aspose.3D documentation?
  - answer: Explore temporary licensing options on the **[Aspose temporary license
      page](https://purchase.aspose.com/temporary-license/)**.
    question: How do I obtain a temporary license for Aspose.3D?
  - answer: Yes, join the discussion at the **[Aspose.3D Forum](https://forum.aspose.com/c/3d/18)**.
    question: Is there a community forum for Aspose.3D support?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- reduce 3d model size
- Aspose.3D
- Java 3D compression
- Google Draco
- sphere mesh
title: Wie man die Größe von 3D-Modellen mit einem Java‑Sphären‑Mesh und Draco reduziert
url: /de/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Wie man die Größe von 3D-Modellen mit einem Java‑Kugel‑Mesh und Draco reduziert

## Einführung

Aspose.3D for Java ist eine Bibliothek, die die Erstellung, Manipulation und Konvertierung von 3‑D‑Modellen direkt aus Java‑Code ermöglicht. Wenn Sie nach einer schnellen Möglichkeit suchen, **die Größe von 3D‑Modellen zu reduzieren**, ohne dabei die hohe Geometrie‑Qualität zu verlieren, sind Sie hier genau richtig. In diesem Tutorial zeigen wir, wie man ein Kugel‑Mesh mit **Aspose.3D for Java** erzeugt und dieses Mesh anschließend mit **Google Draco** komprimiert. Am Ende haben Sie eine einsatzbereite `.drc`‑Datei, die dramatisch kleiner ist als das Original und sich perfekt für webbasierte Viewer, mobile Spiele oder jede bandbreiten‑beschränkte Java‑Anwendung eignet.

## Schnelle Antworten
- **Was behandelt dieses Tutorial?** Erstellung eines Kugel‑Meshes in Java und Komprimierung mit Google Draco über Aspose.3D.  
- **Primäre Bibliothek?** Aspose.3D for Java (wird sowohl für die Mesh‑Erstellung als auch für den Draco‑Export verwendet).  
- **Typische Implementierungszeit?** Etwa 10‑15 Minuten für eine einfache Kugel.  
- **Wichtige Voraussetzung?** Eine Java‑Entwicklungsumgebung mit den Aspose.3D‑JARs im Klassenpfad.  
- **Ergebnis?** Eine `.drc`‑Datei, die **die Größe von 3D‑Modellen** um bis zu 95 % im Vergleich zu einem unkomprimierten Mesh reduziert.

## Wie reduziert man die Größe von 3D-Modellen?

Laden Sie Ihre Kugel und komprimieren Sie sie in zwei einfachen Schritten. Zuerst **erstellen Sie das Kugel‑Mesh** mit `new Sphere(1.0, 32, 32)`. Dann exportieren Sie die Szene direkt nach Draco mit `scene.save("sphere.drc", SaveFormat.Draco)`. Aspose.3D übernimmt die Geometrie‑Quantisierung und Vertex‑Deduplizierung automatisch und liefert Dateien, die typischerweise 80‑95 % kleiner sind, während die visuelle Treue erhalten bleibt.

Die Klasse `Sphere` ist Aspose.3D's integrierter Geometrie‑Generator, der ein trianguliertes Kugel‑Mesh erzeugt. Sie akzeptiert einen Radius und Tessellations‑Parameter, sodass Sie das Detailniveau vor der Komprimierung steuern können.

## Was bedeutet „reduce 3d model size“ im Kontext der 3D‑Entwicklung?

**Die Größe von 3D‑Modellen zu reduzieren** bedeutet, die Menge an Geometriedaten, die übertragen oder gespeichert werden müssen, zu verkleinern, ohne die visuelle Qualität merklich zu beeinträchtigen. Draco erreicht dies, indem es Vertex‑Positionen, Normalen und andere Attribute in einem stark kompakten Binärformat kodiert. In Kombination mit Aspose.3D bleibt der gesamte Workflow innerhalb von Java, sodass Sie keine nativen Binärdateien jonglieren müssen.

## Warum Google Draco Mesh‑Kompression mit Aspose.3D verwenden?

Google Draco in Verbindung mit Aspose.3D bietet eine effiziente Pipeline, die Mesh‑Dateien dramatisch verkleinert und gleichzeitig die Integration in Java‑Projekte erleichtert. Die Bibliothek übernimmt das gesamte Low‑Level‑Encoding, sodass Entwickler sich auf die Geometrieerstellung konzentrieren können, ohne native Draco‑Binärdateien zu handhaben. Das führt zu schnellerer Entwicklung und kleineren Assets für Web und Mobile.

- **Massive Größenreduktion:** Draco kann Mesh‑Daten um bis zu 95 % reduzieren, sodass ein 5 MB OBJ zu einer 0,3 MB `.drc` wird.  
- **Schnelle Laufzeit‑Dekodierung:** Engines wie Unity, Unreal und three.js dekodieren Draco nativ, was zu kürzeren Ladezeiten führt.  
- **Nahtlose Java‑Integration:** Aspose.3D abstrahiert die native Draco‑Bibliothek, sodass Sie im Java‑Ökosystem bleiben können.  
- **All‑in‑One Aspose‑3D‑Export:** Die gleiche API, die Sie zur Geometrieerstellung nutzen, übernimmt auch den Export und vereinfacht die Pipeline.  

Aspose.3D unterstützt **mehr als 50 Eingabe‑ und Ausgabeformate** — darunter OBJ, FBX, STL, GLTF und viele weitere — und kann Modelle mit mehreren hundert Seiten verarbeiten, ohne die gesamte Datei in den Speicher zu laden.

## Voraussetzungen

- **Java Development Kit (JDK)** – Version 8 oder neuer.  
- **Aspose.3D for Java** – laden Sie die neuesten JARs von der **[Aspose 3D Java releases page](https://releases.aspose.com/3d/java/)** herunter.  
- **Grundlegende Kenntnisse zu Google Draco** – Sie verwenden den Wrapper von Aspose.3D, sodass keine native Draco‑Installation erforderlich ist.

## Pakete importieren

```java
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Sphere;


import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

## Schritt‑für‑Schritt‑Anleitung

### Schritt 1: Projekt einrichten

Erstellen Sie ein neues Java‑Projekt (jede IDE funktioniert) und fügen Sie alle Aspose.3D‑JARs dem Klassenpfad hinzu. Legen Sie Ihre Quell‑Dateien in einem Paket wie `com.example.draco` ab, um Klarheit zu schaffen.

### Schritt 2: Wie man ein Kugel‑Mesh in Java erstellt

Die Klasse `Sphere` ist Aspose.3D's integrierter Geometrie‑Generator, der ein trianguliertes Kugel‑Mesh erzeugt.  

```java
import java.nio.file.Files;
import java.nio.file.Paths;
import com.aspose.threed.Sphere;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.FileFormat;

// ExStart:Encode3DMeshinGoogleDraco
// The path to the documents directory.
String MyDir = "Your Document Directory";

// Create a sphere
Sphere sphere = new Sphere();

// Encode the sphere to Google Draco raw data using optimal compression level.
DracoSaveOptions opt = new DracoSaveOptions();
opt.setCompressionLevel(DracoCompressionLevel.OPTIMAL);
byte[] b = FileFormat.DRACO.encode(sphere.toMesh(), opt);

// Save the raw bytes to file
Files.write(Paths.get(MyDir, "SphereMeshtoDRC_Out.drc"), b);
// ExEnd:Encode3DMeshinGoogleDraco
```

> **Pro‑Tipp:** Die Klasse `Sphere` erzeugt ein trianguliertes Mesh mit einem Standard‑Radius von 1.0. Sie können einen benutzerdefinierten Radius, Tessellation oder Material‑Parameter übergeben, wenn Sie vor der Komprimierung ein anderes Detailniveau benötigen.

### Schritt 3: Export des Meshes ins Draco‑Format

Die Klasse `Scene` repräsentiert eine komplette 3‑D‑Szene, die Meshes, Lichter und Kameras enthalten kann. Die Klasse `DracoCompressionOptions` ermöglicht die Anpassung der Draco‑Kompressionseinstellungen wie Quantisierung und Kompressionsgrad. Nachdem die Kugel zu einem `Scene`‑Objekt hinzugefügt wurde, rufen Sie `scene.save("sphere.drc", SaveFormat.Draco)` auf. Aspose.3D wählt automatisch optimale Kompressionseinstellungen, Sie können sie jedoch feinjustieren, indem Sie `DracoCompressionOptions` anpassen, falls Sie die kleinste mögliche Datei benötigen. `DracoCompressionOptions` lässt Sie

### Schritt 4: Ausgabe überprüfen

Der `DRACOLoader` ist ein three.js‑Utility, das Draco‑komprimierte `.drc`‑Dateien lädt und in WebGL‑kompatible Geometrie umwandelt. Öffnen Sie die erzeugte `.drc`‑Datei mit einem Draco‑Viewer (z. B. three.js `DRACOLoader`), um sicherzustellen, dass die Geometrie korrekt gerendert wird. Sie werden eine dramatische Reduktion der Dateigröße bemerken – häufig ein Faktor von zehn oder mehr.

## Häufige Anwendungsfälle

| Szenario | Warum Modellgröße reduzieren? | Wie dieses Tutorial hilft |
|----------|------------------------------|---------------------------|
| Web‑basierte Produktkonfiguratoren | Schnellere Seitenladezeiten bei langsamen Verbindungen | Draco‑komprimierte `.drc`‑Dateien laden in Sekunden |
| Mobile AR/VR‑Apps | Geringerer Speicherverbrauch auf Geräten | Kleinere Meshes halten die App reaktionsfähig |
| Cloud‑gerenderte Szenen | Bandbreitenkosten senken | Ein‑Klick‑Export von Aspose.3D nach Draco |

## Häufige Probleme und Lösungen

| Problem | Grund | Lösung |
|---------|-------|--------|
| **`NoClassDefFoundError` für Draco‑Klassen** | Aspose.3D‑JARs nicht im Klassenpfad | Vergewissern Sie sich, dass *alle* Aspose.3D‑JAR‑Dateien eingebunden sind und die Version zur Dokumentation passt. |
| **Ausgabedatei ist leer** | `MyDir` verweist auf einen nicht‑existierenden Ordner | Erstellen Sie das Verzeichnis programmgesteuert (`Files.createDirectories(Paths.get(MyDir))`), bevor Sie die Datei schreiben. |
| **Komprimiertes Mesh sieht verzerrt aus** | Verwendung eines niedrigen Kompressionsgrades oder unzureichende Tessellation | Wechseln Sie zu `DracoCompressionLevel.OPTIMAL` und erhöhen Sie die Tessellation der Kugel (z. B. `new Sphere(1.0, 64, 64)`). `DracoCompressionLevel.OPTIMAL` wählt die höchste Kompressionsqualität für Draco‑Ausgaben. |

## Häufig gestellte Fragen

**F: Ist Aspose.3D mit verschiedenen 3D‑Dateiformaten kompatibel?**  
A: Ja, Aspose.3D unterstützt OBJ, FBX, STL, GLTF und viele andere Formate und ist damit eine vielseitige Wahl für **Aspose 3D‑Export**‑Pipelines.

**F: Kann ich Google Draco zur Kompression in anderen Programmiersprachen verwenden?**  
A: Absolut. Draco bietet native Bibliotheken für C++, Python und JavaScript. Dieses Tutorial konzentriert sich auf Java, aber die Konzepte gelten sprachübergreifend.

**F: Wo finde ich zusätzliche Aspose.3D‑Dokumentation?**  
A: Besuchen Sie die **[Aspose.3D Java documentation](https://reference.aspose.com/3d/java/)** für vollständige API‑Referenzen und weitere Beispiele.

**F: Wie erhalte ich eine temporäre Lizenz für Aspose.3D?**  
A: Erkunden Sie temporäre Lizenzierungsoptionen auf der **[Aspose temporary license page](https://purchase.aspose.com/temporary-license/)**.

**F: Gibt es ein Community‑Forum für Aspose.3D‑Support?**  
A: Ja, treten Sie der Diskussion im **[Aspose.3D Forum](https://forum.aspose.com/c/3d/18)** bei.

## Fazit

In diesem Leitfaden haben wir gezeigt, wie man **die Größe von 3D‑Modellen** reduziert, indem man ein Kugel‑Mesh in Java erstellt und es anschließend mit Google Draco über Aspose.3D komprimiert. Durch Befolgen dieser knappen Schritte können Sie Mesh‑Dateien dramatisch verkleinern, Ladezeiten verbessern und Ihre Java‑basierten 3D‑Anwendungen reaktionsschnell und bandbreitenfreundlich halten.

---

**Last Updated:** 2026-11-17  
**Tested With:** Aspose.3D for Java 24.12 (latest)  
**Author:** Aspose

## Verwandte Tutorials

- [3D-Dateigröße reduzieren – Szenen mit Aspose.3D für Java komprimieren](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [Erzeugen einer Draco-Punktwolke aus Kugeln mit Aspose.3D für Java](/3d/java/point-clouds/generate-point-clouds-spheres-java/)
- [Erfahren Sie, wie man Meshes für optimiertes Rendering in Java trianguliert mit Aspose.3D](/3d/java/geometry/triangulate-meshes-for-optimized-rendering/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}