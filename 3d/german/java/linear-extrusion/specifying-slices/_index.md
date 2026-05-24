---
date: 2026-05-24
description: Erfahren Sie, wie Sie mit Aspose.3D for Java 3D-Extrusion mit Schnitten
  erstellen. Diese Schritt‑für‑Schritt‑Anleitung behandelt lineare Extrusion, das
  Festlegen des Rundungsradius und das Exportieren von OBJ.
keywords:
- create 3d extrusion java
- Aspose 3D slices
- linear extrusion Java
linktitle: 3D-Extrusion mit Schnitten erstellen – Aspose.3D for Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  headline: Create 3D Extrusion with Slices – Aspose.3D for Java
  type: TechArticle
- description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  name: Create 3D Extrusion with Slices – Aspose.3D for Java
  steps:
  - name: Set up the scene and define the profile
    text: '`RectangleShape` is a class that defines a 2‑D rectangle profile. First
      we create a `RectangleShape` and give it a **rounding radius** so the corners
      are smooth. `Scene` is the root container for all nodes and geometry. Then we
      initialise a new `Scene` that will hold all geometry.'
  - name: Create child node objects for each extrusion
    text: '`Node` represents an element in the scene graph that can hold geometry
      and transformations. Every piece of geometry lives under a `Node`. Here we generate
      two sibling nodes – one for a low‑slice extrusion and another for a high‑slice
      extrusion – and move the left node a little to the side so the res'
  - name: Perform linear extrusion and set slices
    text: '`LinearExtrusion` is the class that creates a solid by sweeping a profile
      linearly. `LinearExtrusion` is Aspose.3D''s class that generates a solid by
      extruding a 2‑D profile along a straight line. Using an **anonymous inner class**
      we call `setSlices` to control the smoothness. The left node gets onl'
  - name: Export OBJ – save the scene
    text: Finally we write the scene to a Wavefront OBJ file, a format widely supported
      by 3‑D editors and game engines. This demonstrates the **export OBJ Java** capability
      of Aspose.3D.
  type: HowTo
- questions:
  - answer: You can download the library [here](https://releases.aspose.com/3d/java/).
    question: How can I download Aspose.3D for Java?
  - answer: Refer to the documentation [here](https://reference.aspose.com/3d/java/).
    question: Where can I find the documentation for Aspose.3D?
  - answer: Yes, you can explore a free trial [here](https://releases.aspose.com/).
    question: Is there a free trial available?
  - answer: Visit the support forum [here](https://forum.aspose.com/c/3d/18).
    question: How can I get support for Aspose.3D?
  - answer: Yes, a temporary license can be obtained [here](https://purchase.aspose.com/temporary-license/).
    question: Can I purchase a temporary license?
  type: FAQPage
second_title: Aspose.3D Java API
title: 3D-Extrusion mit Schnitten erstellen – Aspose.3D for Java
url: /de/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D-Extrusion mit Scheiben erstellen – Aspose.3D für Java

## Einleitung

Wenn Sie **3D-Extrusion erstellen**‑Objekte erstellen müssen, die glatt und präzise aussehen, ist die Steuerung der Anzahl der Scheiben entscheidend. In diesem Tutorial führen wir Sie durch die Angabe von Scheiben bei einer linearen Extrusion mit Aspose.3D für Java. Sie werden sehen, warum die Scheibenanzahl wichtig ist, wie man einen Abrundungsradius festlegt und wie man das Ergebnis als OBJ‑Datei exportiert, die in jeder 3‑D‑Pipeline verwendet werden kann.

## Schnelle Antworten
- **Was steuert “slices”?** Die Anzahl der Zwischen‑Querschnitte, die zur Annäherung an die Extrusionsoberfläche verwendet werden.  
- **Welche Methode legt die Scheibenanzahl fest?** `LinearExtrusion.setSlices(int)`  
- **Kann ich den Abrundungsradius des Profils ändern?** Ja, über `RectangleShape.setRoundingRadius(double)`  
- **Welches Dateiformat wird in diesem Beispiel verwendet?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **Benötige ich eine Lizenz, um den Code auszuführen?** Eine kostenlose Testversion reicht für die Evaluierung; für die Produktion ist eine kommerzielle Lizenz erforderlich.

`LinearExtrusion.setSlices(int)` legt fest, wie viele Zwischen‑Scheiben die Extrusion erzeugt.  
`RectangleShape.setRoundingRadius(double)` definiert den Eckradius eines rechteckigen Profils.

## Wie erstelle ich 3D-Extrusion in Java mit Scheiben?

Laden Sie Ihr 2‑D‑Profil, wählen Sie eine Scheibenanzahl, setzen Sie den Abrundungsradius und rufen Sie `save` auf – der gesamte Arbeitsablauf passt in ein paar Zeilen. Aspose.3D für Java übernimmt die Geometrieerstellung, Scheibeninterpolation und den OBJ‑Export automatisch, sodass Sie sich auf die visuelle Qualität statt auf niedrig‑stufige Mesh‑Berechnungen konzentrieren können.

## Was ist eine lineare Extrusion mit Scheiben?

Eine lineare Extrusion mit Scheiben verwandelt eine flache 2‑D‑Form in einen 3‑D‑Körper, indem sie entlang einer geraden Linie verschoben wird, während eine konfigurierbare Anzahl von Zwischen‑Querschnitten erzeugt wird. Die Scheibenanzahl beeinflusst direkt, wie glatt gekrümmte Kanten, wie abgerundete Ecken, dargestellt werden.

## Warum Aspose.3D für Java zur Erstellung von 3D-Extrusion verwenden?

Aspose.3D bietet **vollständige programmgesteuerte Kontrolle** über jeden Extrusionsparameter, unterstützt **mehr als 50 Eingabe‑ und Ausgabeformate** (einschließlich OBJ, FBX, STL und GLTF) und kann **Modelle mit mehreren hundert Seiten** verarbeiten, ohne die gesamte Datei in den Speicher zu laden. Es läuft auf jeder Java‑fähigen Plattform, erfordert keine nativen DLLs und garantiert deterministische Ergebnisse unter Windows, Linux und macOS.

## Voraussetzungen

1. **Java Development Kit** – JDK 8 oder höher installiert.  
2. **Aspose.3D for Java** – Laden Sie die Bibliothek von der offiziellen Seite [hier](https://releases.aspose.com/3d/java/) herunter.  
3. Eine IDE oder ein Texteditor Ihrer Wahl.

## Pakete importieren

Fügen Sie Ihrem Projekt den Aspose.3D‑Namensraum hinzu, damit Sie auf die 3‑D‑Modellierungsklassen zugreifen können.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Schritt‑für‑Schritt‑Anleitung

### Schritt 1: Szene einrichten und Profil definieren

`RectangleShape` ist eine Klasse, die ein 2‑D‑Rechteckprofil definiert.  
Zuerst erstellen wir ein `RectangleShape` und geben ihm einen **Abrundungsradius**, damit die Ecken glatt sind.  
`Scene` ist der Root‑Container für alle Knoten und Geometrien.  
Dann initialisieren wir ein neues `Scene`, das alle Geometrien enthalten wird.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Schritt 2: Kind‑Knoten‑Objekte für jede Extrusion erstellen

`Node` stellt ein Element im Szenengraphen dar, das Geometrie und Transformationen halten kann.  
Jedes Geometrie‑Element befindet sich unter einem `Node`. Hier erzeugen wir zwei Schwester‑Knoten – einen für eine Extrusion mit wenigen Scheiben und einen für eine Extrusion mit vielen Scheiben – und verschieben den linken Knoten leicht zur Seite, damit die Ergebnisse leicht zu vergleichen sind.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Schritt 3: Lineare Extrusion durchführen und Scheiben festlegen

`LinearExtrusion` ist die Klasse, die einen Festkörper erzeugt, indem sie ein Profil linear sweepet.  
`LinearExtrusion` ist die Klasse von Aspose.3D, die einen Festkörper erzeugt, indem sie ein 2‑D‑Profil entlang einer geraden Linie extrudiert. Mit einer **anonymen inneren Klasse** rufen wir `setSlices` auf, um die Glätte zu steuern. Der linke Knoten erhält nur 2 Scheiben (grob), während der rechte Knoten 10 Scheiben (glatt) bekommt.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Schritt 4: OBJ exportieren – Szene speichern

Abschließend schreiben wir die Szene in eine Wavefront‑OBJ‑Datei, ein Format, das von vielen 3‑D‑Editoren und Spiel‑Engines unterstützt wird. Dies demonstriert die **export OBJ Java**‑Fähigkeit von Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Häufige Probleme und Lösungen

| Problem | Warum es passiert | Lösung |
|---------|-------------------|--------|
| **Extrusion erscheint flach** | Scheibenanzahl ist auf 1 oder 0 gesetzt | Stellen Sie sicher, dass `setSlices` mit einem Wert ≥ 2 aufgerufen wird. |
| **Abgerundete Ecken sehen gezackt aus** | Abrundungsradius ist im Verhältnis zur Scheibenanzahl zu klein | Erhöhen Sie entweder den Radius oder die Scheibenanzahl für glattere Kurven. |
| **Datei beim Speichern nicht gefunden** | `MyDir` verweist auf einen nicht existierenden Ordner | Erstellen Sie das Verzeichnis vorher oder verwenden Sie einen absoluten Pfad. |

## Häufig gestellte Fragen

**F: Wie kann ich Aspose.3D für Java herunterladen?**  
A: Sie können die Bibliothek [hier](https://releases.aspose.com/3d/java/) herunterladen.

**F: Wo finde ich die Dokumentation für Aspose.3D?**  
A: Sie finden die Dokumentation [hier](https://reference.aspose.com/3d/java/).

**F: Gibt es eine kostenlose Testversion?**  
A: Ja, Sie können eine kostenlose Testversion [hier](https://releases.aspose.com/) erkunden.

**F: Wie kann ich Support für Aspose.3D erhalten?**  
A: Besuchen Sie das Support‑Forum [hier](https://forum.aspose.com/c/3d/18).

**F: Kann ich eine temporäre Lizenz erwerben?**  
A: Ja, eine temporäre Lizenz kann [hier](https://purchase.aspose.com/temporary-license/) erworben werden.

---

**Zuletzt aktualisiert:** 2026-05-24  
**Getestet mit:** Aspose.3D for Java 24.11 (latest at time of writing)  
**Autor:** Aspose

## Verwandte Tutorials

- [3D-Extrusion in Java mit Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Wie man die Richtung bei linearer Extrusion mit Aspose.3D für Java festlegt](/3d/java/linear-extrusion/setting-direction/)
- [3D‑Szene mit Twist bei linearer Extrusion erstellen – Aspose.3D für Java](/3d/java/linear-extrusion/applying-twist/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}