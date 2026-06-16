---
date: 2026-06-03
description: Erfahren Sie, wie Sie die Szene als FBX exportieren und 3D‑Zylinder,
  -Boxen und andere primitive Modelle mit Aspose.3D für Java erstellen.
keywords:
- export scene as fbx
- convert 3d model fbx
- Aspose 3D primitives
- Java 3D modeling
linktitle: Erstellung primitiver 3D‑Modelle mit Aspose.3D für Java
schemas:
- author: Aspose
  dateModified: '2026-06-03'
  description: Learn how to export scene as FBX and create 3D cylinder, box, and other
    primitive models using Aspose.3D for Java.
  headline: Export scene as FBX and build cylinder with Aspose.3D Java
  type: TechArticle
- description: Learn how to export scene as FBX and create 3D cylinder, box, and other
    primitive models using Aspose.3D for Java.
  name: Export scene as FBX and build cylinder with Aspose.3D Java
  steps:
  - name: Initialize a Scene Object
    text: The `Scene` class is Aspose.3D's top‑level container that holds all nodes,
      lights, cameras, and materials in memory.
  - name: Build a 3D box model
    text: The `Box` class represents a rectangular prism and is useful for testing
      the coordinate system. Adding it as a child of the scene’s root node positions
      it at the origin.
  - name: Create a 3D cylinder model
    text: The `Cylinder` class is Aspose.3D's built‑in cylinder primitive. It comes
      with default dimensions (radius = 1, height = 2) but you can customise them
      via its constructor.
  - name: Save the drawing in the FBX format
    text: After assembling the scene, export it so other tools (e.g., Unity, Blender)
      can read it. We use the `FBX7500ASCII` format, which is widely supported and
      human‑readable.
  type: HowTo
- questions:
  - answer: Aspose.3D primarily supports Java, but there are versions available for
      .NET and C++ as well.
    question: Can I use Aspose.3D for Java with other programming languages?
  - answer: Absolutely. It provides a comprehensive set of features—including mesh
      manipulation, material assignment, and animation—making it suitable for both
      simple primitives and intricate models.
    question: Is Aspose.3D suitable for complex 3D modeling tasks?
  - answer: Visit the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) for community
      support and discussions.
    question: Where can I find additional help and support?
  - answer: Yes, you can explore a [free trial](https://releases.aspose.com/) before
      making a purchase decision.
    question: Can I try Aspose.3D before purchasing?
  - answer: You can obtain a [temporary license](https://purchase.aspose.com/temporary-license/)
      for Aspose.3D through the website.
    question: How do I obtain a temporary license for Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
title: Exportieren Sie die Szene als FBX und erstellen Sie einen Zylinder mit Aspose.3D
  Java
url: /de/java/primitive-3d-models/building-primitive-3d-models/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Exportieren einer Szene als FBX und Erstellen eines Zylinders mit Aspose.3D Java

## Einführung

Falls Sie jemals **einen 3D-Zylinder** (oder eine andere Grundform) direkt aus Java-Code erstellen mussten, macht Aspose.3D die Aufgabe mühelos. In diesem Tutorial führen wir Sie durch den gesamten Workflow – vom Einrichten der Umgebung bis zum **Exportieren der Szene als FBX** – sodass Sie sofort programmatisch 3D-Geometrie erzeugen können. Sie sehen, wie die Bibliothek Primitive verarbeitet, wie Sie sie in einem Szenengraphen organisieren und wie Sie das Ergebnis in einem Format speichern, das Unity, Blender oder jedes andere 3D‑Tool lesen kann.

## Schnelle Antworten
- **Welche Bibliothek ermöglicht mir das Erstellen eines 3D-Zylinders in Java?** Aspose.3D for Java.  
- **In welches Format kann ich die Szene exportieren?** FBX (ASCII 7500) using `FileFormat.FBX7500ASCII`.  
- **Benötige ich eine Lizenz für die Entwicklung?** A free trial works for testing; a permanent license is required for production.  
- **Was sind die wichtigsten unterstützten Primitive?** Box, Cylinder, Sphere, Cone, and more than 10 additional shapes.  
- **Ist der Code mit Java 8 und höher kompatibel?** Yes, Aspose.3D targets JDK 8+.

## Was ist ein 3D‑Zylinder‑Primitive?

Ein Zylinder‑Primitive ist eine grundlegende geometrische Form, die durch einen Radius und eine Höhe definiert ist. In vielen 3D‑Pipelines dient es als Baustein für komplexere Modelle wie Rohre, Räder oder architektonische Säulen. Aspose.3D stellt eine fertige `Cylinder`‑Klasse bereit, sodass Sie die Eckpunkte nicht manuell berechnen müssen.

## Warum Aspose.3D für Java verwenden?

Aspose.3D für Java bietet eine umfassende, reine Java‑3D‑Engine, die die Notwendigkeit nativer Bibliotheken eliminiert und sie ideal für plattformübergreifende Entwicklung macht. Sie unterstützt eine breite Palette von Import‑ und Exportformaten, bietet einen robusten Szenengraphen für hierarchische Organisation und enthält integrierte Primitive, mit denen Sie Geometrie mit minimalem Code erstellen können. Diese Funktionen beschleunigen zusammen die Entwicklung und reduzieren den Wartungsaufwand.

- **Voll ausgestattete 3D-Engine** – supports import/export of **over 30** popular formats (FBX, OBJ, STL, GLTF, 3DS, etc.).  
- **Pure Java API** – no native dependencies, perfect for cross‑platform projects.  
- **Robuster Szenengraph** – lets you organise objects hierarchically, making large scenes easy to manage.  
- **Einfache Lizenzierung** – start with a free trial, then upgrade to a permanent license when you go live.

## Voraussetzungen

Bevor Sie in den Code eintauchen, stellen Sie sicher, dass Sie Folgendes haben:

1. **Java Development Kit (JDK)** – JDK 8 oder neuer auf Ihrem Rechner installiert.  
2. **Aspose.3D for Java library** – laden Sie sie von der [download page](https://releases.aspose.com/3d/java/) herunter und installieren Sie sie.

## Pakete importieren

Beginnen Sie mit dem Import des Kern‑Namespaces von Aspose.3D. Dadurch erhalten Sie Zugriff auf `Scene`, `Box`, `Cylinder` und Dateiformat‑Konstanten.

```java
import com.aspose.threed.*;
```

Jetzt, da die Bibliothek referenziert ist, erstellen wir eine Szene und fügen einige Primitive‑Geometrie hinzu.

## Wie exportiere ich eine Szene als FBX und erstelle 3D‑Primitive?

Laden Sie ein neues `Scene`‑Objekt, fügen Sie Primitive‑Knoten (Box, Cylinder usw.) hinzu und rufen Sie dann `save` mit dem FBX7500ASCII‑Format auf. In nur wenigen Zeilen erhalten Sie eine voll ausgestattete FBX‑Datei, die in jedem gängigen 3D‑Editor geöffnet werden kann und eine nahtlose Integration mit Spiel‑Engines, Rendering‑Pipelines oder AR/VR‑Anwendungen ermöglicht.

### Schritt 1: Szenenobjekt initialisieren

Die Klasse `Scene` ist der oberste Container von Aspose.3D, der alle Knoten, Lichter, Kameras und Materialien im Speicher hält.

```java
// The path to the documents directory.
String myDir = "Your Document Directory";

// Initialize a Scene object
Scene scene = new Scene();
```

### Schritt 2: 3D‑Box‑Modell erstellen

Die Klasse `Box` stellt ein rechteckiges Prisma dar und ist nützlich, um das Koordinatensystem zu testen. Wenn Sie sie als Kind des Wurzelknotens der Szene hinzufügen, wird sie am Ursprung positioniert.

```java
// Create a Box model
scene.getRootNode().createChildNode("box", new Box());
```

### Schritt 3: 3D‑Zylinder‑Modell erstellen

Die Klasse `Cylinder` ist das integrierte Zylinder‑Primitive von Aspose.3D. Sie wird mit Standardmaßen geliefert (Radius = 1, Höhe = 2), kann jedoch über ihren Konstruktor angepasst werden.

```java
// Create a Cylinder model
scene.getRootNode().createChildNode("cylinder", new Cylinder());
```

### Schritt 4: Zeichnung im FBX‑Format speichern

Nachdem die Szene zusammengesetzt wurde, exportieren Sie sie, damit andere Werkzeuge (z. B. Unity, Blender) sie lesen können. Wir verwenden das `FBX7500ASCII`‑Format, das weit verbreitet und menschenlesbar ist.

```java
// Save drawing in the FBX format
myDir = myDir + "test.fbx";
scene.save(myDir, FileFormat.FBX7500ASCII);
```

## Häufige Probleme und Lösungen

| Issue | Why it Happens | Fix |
|-------|----------------|-----|
| **Datei nicht gefunden** beim Speichern | `myDir` verweist auf einen nicht existierenden Ordner | Ensure the directory exists or create it with `new File(myDir).mkdirs();` |
| **Leere Szene** nach dem Export | No nodes were added before calling `save` | Verify that `createChildNode` calls are executed (debug with `scene.getRootNode().getChildCount()` ) |
| **Lizenzausnahme** | Running without a valid license in production | Apply a temporary or permanent license using `License license = new License(); license.setLicense("Aspose.3D.Java.lic");` |

## Häufig gestellte Fragen

**Q: Kann ich Aspose.3D für Java mit anderen Programmiersprachen verwenden?**  
A: Aspose.3D primarily supports Java, but there are versions available for .NET and C++ as well.

**Q: Ist Aspose.3D für komplexe 3D‑Modellierungsaufgaben geeignet?**  
A: Absolutely. It provides a comprehensive set of features—including mesh manipulation, material assignment, and animation—making it suitable for both simple primitives and intricate models.

**Q: Wo finde ich zusätzliche Hilfe und Support?**  
A: Visit the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) for community support and discussions.

**Q: Kann ich Aspose.3D vor dem Kauf testen?**  
A: Yes, you can explore a [free trial](https://releases.aspose.com/) before making a purchase decision.

**Q: Wie erhalte ich eine temporäre Lizenz für Aspose.3D?**  
A: You can obtain a [temporary license](https://purchase.aspose.com/temporary-license/) for Aspose.3D through the website.

## Fazit

Sie haben nun gelernt, wie man **die Szene als FBX exportiert** und wie man **3D‑Zylinder**, Boxen und andere Primitive‑Modelle mit Aspose.3D für Java erstellt. Experimentieren Sie gern mit zusätzlichen Primitiven wie Sphere, Cone oder Torus und erkunden Sie Materialzuweisungen, um Ihren Modellen ein realistisches Aussehen zu verleihen. Sobald Sie sich sicher fühlen, können Sie die erzeugten FBX‑Dateien in Spiel‑Engines, AR/VR‑Pipelines oder jeden nachgelagerten 3D‑Workflow integrieren.

---

**Zuletzt aktualisiert:** 2026-06-03  
**Getestet mit:** Aspose.3D for Java 24.11 (latest at time of writing)  
**Autor:** Aspose

## Verwandte Tutorials

- [Wie man Szene zu FBX exportiert und 3D‑Szeneninformationen in Java abruft](/3d/java/3d-scenes-and-models/get-scene-information/)
- [Wie man FBX exportiert und Knotenhierarchien in Java erstellt](/3d/java/geometry/build-node-hierarchies/)
- [Wie man Zylinder‑Modelle mit Aspose.3D für Java erstellt](/3d/java/cylinders/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< blocks/products/products-backtop-button >}}
{{< /blocks/products/pf/main-wrap-class >}}