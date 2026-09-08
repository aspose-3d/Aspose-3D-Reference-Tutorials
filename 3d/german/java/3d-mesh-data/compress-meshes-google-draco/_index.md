---
date: 2026-09-08
description: Wie man die Größe von 3D-Modellen reduziert, indem man in Java ein Sphären-Mesh
  erzeugt und es mit Google Draco über Aspose.3D komprimiert. Lernen Sie den kompletten
  Workflow in wenigen Minuten.
keywords:
- how to reduce 3d model size
- aspose 3d java
- draco mesh compression
- java sphere mesh
- 3d model optimization
lastmod: 2026-09-08
linktitle: Wie man die Größe von 3D-Modellen reduziert – Sphären-Mesh in Java mit
  Google Draco erstellen
og_description: Wie man die Größe von 3D-Modellen reduziert, indem man ein Sphären-Mesh
  in Java erstellt und es mit Google Draco über Aspose.3D komprimiert. Erhalten Sie
  eine .drc-Datei, die bis zu 95 % kleiner ist, in wenigen Minuten.
og_image_alt: 'Developer guide: Reduce 3d model size with Java sphere mesh and Draco
  compression'
og_title: Wie man die Größe von 3D-Modellen mit einem Java-Sphären-Mesh und Draco
  reduziert
schemas:
- author: Aspose
  dateModified: '2026-09-08'
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
title: Wie man die Größe von 3D-Modellen mit einem Java-Sphären-Mesh und Draco reduziert
url: /de/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Wie man die 3D-Modellgröße mit einem Java-Kugel-Mesh und Draco reduziert

## Einführung

Wenn Sie nach einer schnellen Möglichkeit suchen, **die 3D-Modellgröße** zu **reduzieren**, während Sie weiterhin hochqualitative Geometrie liefern, sind Sie hier genau richtig. In diesem Tutorial führen wir Sie durch die Erstellung eines Kugel‑Meshes mit **Aspose.3D for Java** und anschließend die Komprimierung dieses Meshes mit **Google Draco**. Am Ende haben Sie eine einsatzbereite `.drc`‑Datei, die dramatisch kleiner ist als das Original, ideal für webbasierte Viewer, mobile Spiele oder jede bandbreitenbeschränkte Java‑Anwendung.

## Schnelle Antworten
- **Worum geht es in diesem Tutorial?** Erstellung eines Kugel‑Meshes in Java und Komprimierung mit Google Draco über Aspose.3D.  
- **Primäre Bibliothek?** Aspose.3D for Java (wird sowohl für die Mesh‑Erstellung als auch für den Draco‑Export verwendet).  
- **Typische Implementierungszeit?** Etwa 10‑15 Minuten für eine einfache Kugel.  
- **Wichtige Voraussetzung?** Eine Java‑Entwicklungsumgebung mit den Aspose.3D‑JARs im Klassenpfad.  
- **Ergebnis?** Eine `.drc`‑Datei, die **die 3D-Modellgröße** um bis zu 95 % im Vergleich zu einem unkomprimierten Mesh **reduziert**.

## Wie man die 3D-Modellgröße reduziert?

Die Klasse `Sphere` erzeugt eine triangulierte Kugelgeometrie basierend auf dem angegebenen Radius und den Tessellations‑Parametern. Laden Sie Ihre Kugel mit `new Sphere(1.0, 32, 32)` und exportieren Sie sie direkt nach Draco mittels `scene.save("sphere.drc", SaveFormat.Draco)`. Die Methode `scene.save` schreibt die aktuelle Szene in eine Datei im angegebenen Format. Aspose.3D übernimmt die Konvertierung intern, sodass Sie manuelle Kodierungsschritte vermeiden. Der Draco‑Exporter wendet automatisch Geometrie‑Quantisierung und Vertex‑Deduplizierung an und erzeugt Dateien, die oft 80‑95 % kleiner sind, während die visuelle Treue erhalten bleibt.

## Was bedeutet „Reduzieren der 3D-Modellgröße“ im Kontext der 3D-Entwicklung?

**Reduzieren der 3D-Modellgröße** bedeutet, die Menge an Geometriedaten, die übertragen oder gespeichert werden müssen, zu verkleinern, ohne die visuelle Qualität merklich zu beeinträchtigen. Draco erreicht dies, indem es Vertex‑Positionen, Normalen und andere Attribute in einem stark kompakten Binärformat kodiert. In Kombination mit Aspose.3D bleibt der gesamte Workflow innerhalb von Java, sodass Sie nicht mit nativen Binärdateien jonglieren müssen.

## Warum Google Draco Mesh‑Kompression mit Aspose.3D verwenden?

Google Draco in Kombination mit Aspose.3D bietet eine effiziente Pipeline, die Mesh‑Dateien dramatisch verkleinert und gleichzeitig die Integration in Java‑Projekte erleichtert. Die Bibliothek übernimmt sämtliche Low‑Level‑Kodierung, sodass Entwickler sich auf die Erstellung der Geometrie konzentrieren können, ohne sich mit nativen Draco‑Binärdateien befassen zu müssen. Das führt zu schnellerer Entwicklung und kleineren Assets für Web und Mobile.

- **Massive Größenreduktion:** Draco kann Mesh‑Daten bei typischen Modellen um bis zu 95 % reduzieren und ein 5 MB OBJ in eine 0,3 MB `.drc`‑Datei verwandeln.  
- **Schnelle Laufzeit‑Dekodierung:** Engines wie Unity, Unreal und three.js dekodieren Draco nativ, was zu schnelleren Ladezeiten führt.  
- **Nahtlose Java‑Integration:** Aspose.3D abstrahiert die native Draco‑Bibliothek und ermöglicht es Ihnen, im Java‑Ökosystem zu bleiben.  
- **All‑in‑One Aspose 3D Export:** Die gleiche API, die Sie zur Erstellung der Geometrie verwenden, übernimmt auch den Export und vereinfacht die Pipeline.

## Voraussetzungen

- **Java Development Kit (JDK)** – Version 8 oder neuer.  
- **Aspose.3D for Java** – Laden Sie die neuesten JARs von der **[Aspose 3D Java releases page](https://releases.aspose.com/3d/java/)** herunter.  
- **Grundlegende Kenntnisse von Google Draco** – Sie verwenden den Wrapper von Aspose.3D, sodass keine native Draco‑Einrichtung erforderlich ist.

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

### Schritt 1: Projekt einrichten

Erstellen Sie ein neues Java‑Projekt (jede IDE funktioniert) und fügen Sie alle Aspose.3D‑JARs dem Klassenpfad hinzu. Platzieren Sie Ihre Quelldateien in einem Paket wie `com.example.draco` zur Übersichtlichkeit.

### Schritt 2: Wie man ein Kugel‑Mesh in Java erstellt

Die Klasse `Sphere` ist Aspose.3D's integrierter Geometriegenerator, der ein trianguliertes Mesh mit konfigurierbarem Radius und Tessellation erzeugt.  

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

> **Pro‑Tipp:** Die Klasse `Sphere` erzeugt ein trianguliertes Mesh mit einem Standardradius von 1.0. Sie können einen benutzerdefinierten Radius, Tessellation oder Materialparameter übergeben, wenn Sie vor der Komprimierung ein anderes Detailniveau benötigen.

### Schritt 3: Mesh in das Draco‑Format exportieren

Nachdem die Kugel zu einem `Scene`‑Objekt hinzugefügt wurde, rufen Sie `scene.save("sphere.drc", SaveFormat.Draco)` auf. Aspose.3D wählt automatisch optimale Kompressionseinstellungen, aber Sie können sie feinjustieren, indem Sie `DracoCompressionOptions` anpassen, falls Sie die kleinste mögliche Datei benötigen. `DracoCompressionOptions` ermöglicht die Anpassung von Draco‑Kompressionseinstellungen wie Quantisierung und Kompressionsgrad.

### Schritt 4: Ausgabe überprüfen

Öffnen Sie die erzeugte `.drc`‑Datei mit einem Draco‑Viewer (z. B. three.js `DRACOLoader`), um sicherzustellen, dass die Geometrie korrekt dargestellt wird. Sie werden eine dramatische Reduzierung der Dateigröße bemerken – oft ein Faktor von zehn oder mehr.

## Häufige Anwendungsfälle

| Szenario | Warum Modellgröße reduzieren? | Wie dieses Tutorial hilft |
|----------|------------------------------|---------------------------|
| Web‑basierte Produktkonfiguratoren | Schnellere Seitenladezeiten bei langsamen Verbindungen | Draco‑komprimierte `.drc`‑Dateien laden in Sekunden |
| Mobile AR/VR‑Apps | Geringerer Speicherverbrauch auf Geräten | Kleinere Meshes halten die App reaktionsfähig |
| Cloud‑gerenderte Szenen | Bandbreitenkosten senken | Ein‑Klick‑Export von Aspose.3D zu Draco |

## Häufige Probleme und Lösungen

| Problem | Grund | Lösung |
|---------|-------|--------|
| **`NoClassDefFoundError` für Draco‑Klassen** | Aspose.3D‑JARs nicht im Klassenpfad | Stellen Sie sicher, dass *alle* Aspose.3D‑JAR‑Dateien enthalten sind und die Version mit der Dokumentation übereinstimmt. |
| **Ausgabedatei ist leer** | `MyDir` verweist auf einen nicht existierenden Ordner | Erstellen Sie das Verzeichnis programmgesteuert (`Files.createDirectories(Paths.get(MyDir))`) bevor Sie die Datei schreiben. |
| **Komprimiertes Mesh sieht verzerrt aus** | Verwendung eines niedrigen Kompressionsgrades oder unzureichender Tessellation | Wechseln Sie zu `DracoCompressionLevel.OPTIMAL` und erhöhen Sie die Tessellation der Kugel (z. B. `new Sphere(1.0, 64, 64)`). `DracoCompressionLevel.OPTIMAL` wählt die höchste Kompressionsqualität für Draco‑Ausgabe. |

## Häufig gestellte Fragen

**F: Ist Aspose.3D mit verschiedenen 3D-Dateiformaten kompatibel?**  
A: Ja, Aspose.3D unterstützt OBJ, FBX, STL, GLTF und viele andere, was es zu einer vielseitigen Wahl für **Aspose 3D‑Export**‑Pipelines macht.

**F: Kann ich Google Draco zur Kompression in anderen Programmiersprachen verwenden?**  
A: Absolut. Draco bietet native Bibliotheken für C++, Python und JavaScript. Dieses Tutorial konzentriert sich auf Java, aber die Konzepte gelten für alle Sprachen.

**F: Wo finde ich weitere Aspose.3D‑Dokumentation?**  
A: Besuchen Sie die **[Aspose.3D Java documentation](https://reference.aspose.com/3d/java/)** für vollständige API‑Referenzen und weitere Beispiele.

**F: Wie erhalte ich eine temporäre Lizenz für Aspose.3D?**  
A: Erkunden Sie temporäre Lizenzoptionen auf der **[Aspose temporary license page](https://purchase.aspose.com/temporary-license/)**.

**F: Gibt es ein Community‑Forum für Aspose.3D‑Support?**  
A: Ja, beteiligen Sie sich an der Diskussion im **[Aspose.3D Forum](https://forum.aspose.com/c/3d/18)**.

## Fazit

In diesem Leitfaden haben wir gezeigt, wie man **die 3D-Modellgröße** reduziert, indem man ein Kugel‑Mesh in Java erstellt und anschließend mit Google Draco über Aspose.3D komprimiert. Durch das Befolgen dieser knappen Schritte können Sie Mesh‑Dateien dramatisch verkleinern, Ladezeiten verbessern und Ihre Java‑basierten 3D‑Anwendungen reaktionsschnell und bandbreitenfreundlich halten.

---

**Zuletzt aktualisiert:** 2026-09-08  
**Getestet mit:** Aspose.3D for Java 24.12 (latest)  
**Autor:** Aspose

## Verwandte Tutorials

- [3D-Dateigröße reduzieren – Szenen mit Aspose.3D für Java komprimieren](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [Draco-Punktwolke aus Kugeln mit Aspose.3D für Java erzeugen](/3d/java/point-clouds/generate-point-clouds-spheres-java/)
- [Erfahren Sie, wie man Meshes für optimiertes Rendering in Java mit Aspose.3D trianguliert](/3d/java/geometry/triangulate-meshes-for-optimized-rendering/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}