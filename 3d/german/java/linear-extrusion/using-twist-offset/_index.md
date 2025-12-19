---
date: 2025-12-19
description: Erfahren Sie, wie Sie eine 3D‑Szene erstellen und ein 3D‑OBJ mit Twist‑Offset
  in Linear‑Extrusion mit Aspose.3D für Java exportieren.
linktitle: Create 3d scene with Twist Offset – Aspose.3D Java
second_title: Aspose.3D Java API
title: 3D‑Szene mit Twist‑Offset erstellen – Aspose.3D Java
url: /de/java/linear-extrusion/using-twist-offset/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Erstelle 3d Szene mit Twist Offset – Aspose.3D für Java

## Einführung

In der dynamischen Welt der 3D‑Grafik ist das Erlernen, **3d Szene zu erstellen** mit linearer Extrusion, ein echter Wendepunkt. Mit Aspose.3D für Java können Sie Ihre 3D‑Modellierungsfähigkeiten steigern, indem Sie die Twist‑Offset‑Funktion in Ihren linearen Extrusionsprozess integrieren. Dieses Tutorial führt Sie Schritt für Schritt durch die Nutzung von Twist Offset bei Linear Extrusion mit Aspose.3D für Java und gibt Ihnen die Werkzeuge, um beeindruckende 3D‑Szenen zu erstellen.

## Schnellantworten
- **Was bewirkt Twist Offset?** Es verschiebt den Beginn der Drehung entlang des Extrusionspfads und gibt Ihnen mehr Kontrolle über die Geometrie.  
- **Welches Dateiformat wird für den Export verwendet?** Das Beispiel speichert das Modell als Wavefront OBJ (`.obj`).  
- **Benötige ich eine Lizenz für die Entwicklung?** Eine kostenlose Testversion reicht für Tests; für die Produktion ist eine kommerzielle Lizenz erforderlich.  
- **Welche Java‑Version wird benötigt?** Java 8 oder höher.  
- **Kann ich die Anzahl der Scheiben ändern?** Ja – die Methode `setSlices` definiert die Glätte der Drehung.

## Voraussetzungen

Bevor Sie mit dem Tutorial beginnen, stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind:

- Java‑Umgebung: Stellen Sie sicher, dass eine Java‑Entwicklungsumgebung auf Ihrem System eingerichtet ist.  
- Aspose.3D für Java: Laden Sie die Aspose.3D‑Bibliothek von dem [download link](https://releases.aspose.com/3d/java/) herunter und installieren Sie sie.  
- Dokumentation: Machen Sie sich mit der [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/) vertraut.  

## Pakete importieren

In Ihrem Java‑Projekt importieren Sie die notwendigen Pakete, um Aspose.3D für Java zu nutzen. Stellen Sie sicher, dass Sie die erforderlichen Bibliotheken für eine nahtlose Integration einbinden.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Schritt 1: Umgebung einrichten

Beginnen Sie damit, Ihre Java‑Entwicklungsumgebung einzurichten und sicherzustellen, dass Aspose.3D für Java korrekt installiert ist.

## Schritt 2: Basis‑Profil initialisieren

Erstellen Sie ein Basis‑Profil für die Extrusion, in diesem Fall ein `RectangleShape` mit einem Abrundungsradius von 0.3.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
// Initialize the base profile to be extruded
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Schritt 3: 3D‑Szene erstellen

Erstellen Sie eine 3D‑Szene, um Ihre extrudierten Objekte zu beherbergen.

```java
// Create a scene
Scene scene = new Scene();
```

## Schritt 4: Knoten erstellen

Generieren Sie Knoten innerhalb der Szene, um verschiedene Entitäten darzustellen.

```java
// Create left node
Node left = scene.getRootNode().createChildNode();
// Create right node
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Schritt 5: Lineare Extrusion durchführen

Nutzen Sie lineare Extrusion sowohl für linke als auch rechte Knoten mit verschiedenen Eigenschaften.

```java
// Perform linear extrusion on left node using twist and slices property
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// Perform linear extrusion on right node using twist, twist offset, and slices property
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

## Schritt 6: 3D‑Szene speichern

Speichern Sie Ihre neu erstellte 3D‑Szene im angegebenen Dateiformat.

```java
// Save 3D scene
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Wie man 3d Modell speichert und 3d obj exportiert

Der Aufruf `scene.save` im vorherigen Schritt **speichert das 3d Modell** als OBJ‑Datei, ein weit verbreitetes **export 3d obj**‑Format. Sie können den Dateinamen ändern oder ein anderes unterstütztes Format wählen (z. B. STL, FBX), indem Sie das `FileFormat`‑Enum anpassen.

## Fazit

Herzlichen Glückwunsch! Sie haben Twist Offset in Linear Extrusion mit Aspose.3D für Java erfolgreich implementiert. Diese leistungsstarke Funktion eröffnet Ihnen ein breites Spektrum an Möglichkeiten für Ihre 3D‑Modellierungsprojekte, sodass Sie **3d Szene erstellen** können mit komplexen Drehungen und Versätzen und anschließend **3d Modell speichern** in einem Format, das für nachgelagerte Pipelines bereit ist.

## FAQ

### Q1: Kann ich Aspose.3D für Java in nicht‑kommerziellen Projekten verwenden?

A1: Ja, Aspose.3D für Java kann sowohl in kommerziellen als auch in nicht‑kommerziellen Projekten verwendet werden. Weitere Details finden Sie unter den [licensing options](https://purchase.aspose.com/buy).

### Q2: Wo finde ich Support für Aspose.3D für Java?

A2: Besuchen Sie das [Aspose.3D for Java forum](https://forum.aspose.com/c/3d/18), um Unterstützung zu erhalten und sich mit der Community zu vernetzen.

### Q3: Gibt es eine kostenlose Testversion von Aspose.3D für Java?

A3: Ja, Sie können eine kostenlose Testversion von der [releases page](https://releases.aspose.com/) ausprobieren.

### Q4: Wie erhalte ich eine temporäre Lizenz für Aspose.3D für Java?

A4: Holen Sie sich eine temporäre Lizenz für Ihr Projekt, indem Sie diesen [Link](https://purchase.aspose.com/temporary-license/) besuchen.

### Q5: Gibt es weitere Beispiele und Tutorials?

A5: Ja, siehe die [documentation](https://reference.aspose.com/3d/java/) für mehr Beispiele und ausführliche Tutorials.

## Häufig gestellte Fragen

**Q: Ist dieses Tutorial Teil einer Aspose 3d Tutorial‑Reihe?**  
A: Ja – es ist ein offizielles **aspose 3d tutorial**, das eine spezifische Funktion der Bibliothek demonstriert.

**Q: Kann ich anstelle eines Rechtecks eine andere Form verwenden?**  
A: Absolut. Jede `IProfile`‑Implementierung (z. B. `CircleShape`, benutzerdefinierte `PolygonShape`) kann extrudiert werden.

**Q: Was passiert, wenn ich `setTwistOffset` weglasse?**  
A: Die Extrusion beginnt die Drehung vom Ursprung des Profils aus, was zu einer symmetrischen Drehung führt.

**Q: Wie erhöhe ich die Glätte der Drehung?**  
A: Erhöhen Sie den an `setSlices` übergebenen Wert; höhere Scheibenanzahlen erzeugen glattere Geometrie.

**Q: Welche anderen Dateiformate kann ich neben OBJ exportieren?**  
A: Aspose.3D unterstützt STL, FBX, GLTF, 3MF und mehrere weitere über das `FileFormat`‑Enum.

---

**Last Updated:** 2025-12-19  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

## TARGET KEYWORDS:

**Primary Keyword (HIGHEST PRIORITY):**  
create 3d scene  

**Secondary Keywords (SUPPORTING):**  
save 3d model, export 3d obj, aspose 3d tutorial