---
date: 2026-10-03
description: Erfahren Sie, wie Sie eine Kugel in Java erstellen und eine OBJ‑Datei
  mit Aspose.3D exportieren, der führenden Java‑3D‑Bibliothek zum Konvertieren von
  3D‑Modellen.
images:
- /java/3d-objects-and-scenes/modify-sphere-radius/og-image.png
keywords:
- create sphere java
- save 3d as obj
- java convert 3d model
- write obj file java
lastmod: 2026-10-03
linktitle: 'Erstelle Kugel in Java: Konvertiere 3D zu OBJ mit Aspose.3D'
og_description: Erfahren Sie, wie Sie eine Kugel in Java erstellen und eine OBJ‑Datei
  mit Aspose.3D exportieren. Diese Schritt‑für‑Schritt‑Anleitung zeigt, wie man eine
  Kugel hinzufügt, ihren Radius ändert und als OBJ speichert.
og_image_alt: 'Guide: create sphere java and export OBJ using Aspose.3D'
og_title: Kugel in Java erstellen – OBJ mit Aspose.3D exportieren
schemas:
- author: Aspose
  dateModified: '2026-10-03'
  description: Learn how to create sphere java and export OBJ file using Aspose.3D,
    the leading Java 3D library for converting 3D models.
  headline: 'Create sphere java: Convert 3D to OBJ with Aspose.3D'
  type: TechArticle
- description: Learn how to create sphere java and export OBJ file using Aspose.3D,
    the leading Java 3D library for converting 3D models.
  name: 'Create sphere java: Convert 3D to OBJ with Aspose.3D'
  steps:
  - name: Initialize a Scene
    text: '**Definition anchor:** The `Scene` class is Aspose.3D''s top‑level container
      that holds geometry, lights, and cameras for a 3D model. Creating a `Scene`
      gives you a workspace where you can add and manipulate objects. Creating a `Scene`
      gives you a container for all geometry, lights, and cameras. This'
  - name: Initialize a Sphere
    text: '**Definition anchor:** The `Sphere` class represents a geometric sphere
      primitive with a configurable radius, center, and material. By default it starts
      with a radius of 1.0. A `Sphere` object starts with a default radius of 1.0.
      Think of it as a blank canvas for the shape you want to export.'
  - name: Set the Desired Radius
    text: The `setRadius(double)` method updates the sphere’s size by assigning a
      new radius value in the same units used by the scene. Here we **write obj file
      java**‑style code that sets the exact radius. Replace `10` with any `double`
      value that matches your design requirements.
  - name: Add Sphere to the Scene
    text: This line **adds sphere to scene** by creating a child node under the root
      node. It’s the moment the geometry becomes part of the scene graph.
  - name: Export the Model as OBJ
    text: The `save(String, FileFormat)` method writes the entire scene to the specified
      file using the chosen format, such as OBJ. Calling `scene.save` **exports obj
      file java**‑style, effectively **save scene as obj**. The generated `sphere.obj`
      can be opened in any standard 3D viewer.
  type: HowTo
- questions:
  - answer: You can refer to the [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/)
      for comprehensive guidance.
    question: Where can I find the documentation for Aspose.3D for Java?
  - answer: 'Download the library from the releases page: [Download Aspose.3D for
      Java](https://releases.aspose.com/3d/java/).'
    question: How do I download Aspose.3D for Java?
  - answer: Yes, explore the features with a free trial by visiting [Aspose.3D Free
      Trial](https://releases.aspose.com/).
    question: Is there a free trial available for Aspose.3D for Java?
  - answer: Join the Aspose community at [Aspose.3D Support Forum](https://forum.aspose.com/c/3d/18)
      for assistance and discussions.
    question: Where can I get support for Aspose.3D for Java?
  - answer: Get a temporary license by visiting [Temporary License](https://purchase.aspose.com/temporary-license/).
    question: How can I obtain a temporary license for Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- modify sphere radius
- export OBJ
- aspose.3d
- java 3d
- 3d conversion
title: 'Erstelle Kugel in Java: Konvertiere 3D zu OBJ mit Aspose.3D'
url: /de/java/3d-objects-and-scenes/modify-sphere-radius/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Kugel in Java erstellen und als OBJ exportieren

## Einführung

In diesem Tutorial lernen Sie, wie man **Kugel in Java erstellt**, ihren Radius anpasst und dann **3D als OBJ speichert** mit der Aspose.3D Java-Bibliothek. Wir gehen jede Codezeile durch, erklären, warum jeder Schritt wichtig ist, und geben Ihnen praktische Tipps, damit Sie diesen Workflow mit Vertrauen in Spiele, CAD‑Tools oder wissenschaftliche Visualisierungen einbetten können.

## Schnelle Antworten
- **Was ist das Hauptziel dieses Tutorials?** Um zu demonstrieren, wie man Kugel in Java erstellt, ihre Größe ändert und das Modell mit Java als OBJ exportiert.
- **Welche Bibliothek liefert die 3D‑Funktionalität?** Aspose.3D, ein vollwertiges **java 3d library tutorial**.
- **Wie ändere ich die Größe der Kugel?** Rufen Sie `sphere.setRadius(double)` auf der `Sphere`‑Instanz auf.
- **Kann ich die OBJ‑Datei direkt aus Java schreiben?** Ja – verwenden Sie `scene.save("file.obj", FileFormat.WAVEFRONTOBJ)`.
- **Benötige ich eine Lizenz für die Produktion?** Eine kostenlose Testversion reicht für die Entwicklung; für die kommerzielle Nutzung ist eine permanente Lizenz erforderlich.

## Was ist Aspose.3D für Java?

Aspose.3D für Java ist eine umfassende **java 3d library**, die Entwicklern ermöglicht, 3D‑Dateien zu erstellen, zu bearbeiten und zu konvertieren, ohne externe Abhängigkeiten. Sie unterstützt mehr als **50 Eingabe‑ und Ausgabeformate** – darunter OBJ, FBX, STL und GLTF – und ermöglicht eine nahtlose Integration in jede 3‑D‑Pipeline.

## Warum 3D nach OBJ konvertieren?

Die Konvertierung zu OBJ liefert Ihnen eine universell unterstützte, reine Textdarstellung von Geometrie, die von jedem 3D‑Tool gelesen werden kann. Das macht sie ideal für schnelles Prototyping, plattformübergreifenden Asset‑Austausch und einfaches Debugging von Vertex‑Daten. Da OBJ‑Dateien leichtgewichtig und menschenlesbar sind, können Sie sie bei Bedarf mit einem einfachen Texteditor inspizieren oder ändern.

## Voraussetzungen

- Grundkenntnisse in Java‑Programmierung.  
- Aspose.3D‑Bibliothek installiert – laden Sie sie von der [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/) herunter.  
- JDK 8 oder höher auf Ihrer Entwicklungsmaschine installiert.

## Pakete importieren

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Sphere;

import java.io.IOException;
```

## Wie man den Kugelradius in Java ändert?

`Sphere` ist ein geometrisches Primitive, das eine Kugel in Aspose.3D darstellt.

Laden Sie das `Sphere`‑Objekt, rufen Sie `setRadius` mit dem gewünschten Wert auf und speichern Sie dann die Szene als OBJ – dieser gesamte Workflow kann in fünf knappen Schritten durchgeführt werden. Der Ansatz funktioniert für jeden numerischen Radius und stellt sicher, dass das exportierte OBJ exakt die von Ihnen angegebene Größe widerspiegelt.

### Schritt 1: Szene initialisieren

```java
// ExStart:WorkingWithSphereRadius

// initialize a scene
Scene scene = new Scene();
```

**Definition anchor:** Die `Scene`‑Klasse ist Aspose.3D's Top‑Level‑Container, der Geometrie, Lichter und Kameras für ein 3D‑Modell hält. Das Erstellen einer `Scene` gibt Ihnen einen Arbeitsbereich, in dem Sie Objekte hinzufügen und manipulieren können.

Das Erstellen einer `Scene` liefert Ihnen einen Container für alle Geometrien, Lichter und Kameras. Hier werden wir später **add sphere to scene** hinzufügen.

### Schritt 2: Kugel initialisieren

```java
// initialize a Sphere
Sphere sphere = new Sphere();
```

**Definition anchor:** Die `Sphere`‑Klasse repräsentiert ein geometrisches Kugel‑Primitive mit konfigurierbarem Radius, Zentrum und Material. Standardmäßig startet sie mit einem Radius von 1,0.

Ein `Sphere`‑Objekt startet mit einem Standardradius von 1,0. Betrachten Sie es als leere Leinwand für die Form, die Sie exportieren möchten.

### Schritt 3: Gewünschten Radius festlegen

**Definition anchor:** Die Methode `setRadius(double)` legt den Radius der Kugel in denselben Einheiten fest, die von der Szene verwendet werden.  

```java
// set radius
sphere.setRadius(10);
```

Hier schreiben wir **write obj file java**‑stiligen Code, der den genauen Radius festlegt. Ersetzen Sie `10` durch einen beliebigen `double`‑Wert, der Ihren Designanforderungen entspricht.

### Schritt 4: Kugel zur Szene hinzufügen

```java
// add sphere to the scene
scene.getRootNode().createChildNode(sphere);
```

Diese Zeile **adds sphere to scene** erstellt einen Kindknoten unter dem Wurzelknoten. Es ist der Moment, in dem die Geometrie Teil des Szenengraphen wird.

### Schritt 5: Modell als OBJ exportieren

```java
// save scene
scene.save("sphere.obj", FileFormat.WAVEFRONTOBJ);
```

Die Methode `save(String, FileFormat)` schreibt die gesamte Szene in die angegebene Datei im gewählten Format, z. B. OBJ. Der Aufruf von `scene.save` **exports obj file java**‑stil, effektiv **save scene as obj**. Die erzeugte `sphere.obj` kann in jedem gängigen 3D‑Betrachter geöffnet werden.

## Häufige Probleme und Lösungen

| Problem | Lösung |
|-------|----------|
| **Kugel erscheint zu klein im Viewer** | Überprüfen Sie, ob der Radiuswert korrekt gesetzt ist; denken Sie daran, dass Einheiten willkürlich sind, sofern Sie keine Skalierungstransformation anwenden. |
| **Exportiertes OBJ hat kein Material** | Aspose.3D schreibt nur Geometrie; fügen Sie der Kugel ein Material hinzu, wenn Sie Texturen benötigen (`sphere.setMaterial(...)`). |
| **Lizenzausnahme zur Laufzeit** | Stellen Sie sicher, dass Sie entweder eine temporäre oder permanente Lizenzdatei geladen haben, bevor Sie die `Scene` erstellen. |

## Häufig gestellte Fragen

**Q: Wo finde ich die Dokumentation für Aspose.3D für Java?**  
A: Sie können die [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/) für umfassende Anleitungen konsultieren.

**Q: Wie lade ich Aspose.3D für Java herunter?**  
A: Laden Sie die Bibliothek von der Release‑Seite herunter: [Download Aspose.3D for Java](https://releases.aspose.com/3d/java/).

**Q: Gibt es eine kostenlose Testversion für Aspose.3D für Java?**  
A: Ja, erkunden Sie die Funktionen mit einer kostenlosen Testversion, indem Sie [Aspose.3D Free Trial](https://releases.aspose.com/) besuchen.

**Q: Wo kann ich Unterstützung für Aspose.3D für Java erhalten?**  
A: Treten Sie der Aspose‑Community im [Aspose.3D Support Forum](https://forum.aspose.com/c/3d/18) für Hilfe und Diskussionen bei.

**Q: Wie kann ich eine temporäre Lizenz für Aspose.3D erhalten?**  
A: Holen Sie sich eine temporäre Lizenz, indem Sie [Temporary License](https://purchase.aspose.com/temporary-license/) besuchen.

**Q: Kann ich diesen Code mit anderen 3D‑Formaten wie STL verwenden?**  
A: Absolut – ändern Sie einfach das `FileFormat`‑Enum beim Aufruf von `scene.save`, z. B. `FileFormat.STL`.

---

**Zuletzt aktualisiert:** 2026-10-03  
**Getestet mit:** Aspose.3D for Java 24.11  
**Autor:** Aspose

## Verwandte Tutorials

- [Wie man Normalen auf 3D‑Objekten in Java mit Aspose.3D Java API setzt](/3d/java/geometry/set-up-normals-on-3d-objects/)
- [Wie man Textur in FBX mit Java einbettet – Materialien auf 3D‑Objekte mit Aspose.3D anwendet](/3d/java/geometry/apply-materials-to-3d-objects/)
- [Wie man die Ebenenorientierung ändert und OBJ in Java exportiert](/3d/java/3d-scenes-and-models/change-plane-orientation/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}