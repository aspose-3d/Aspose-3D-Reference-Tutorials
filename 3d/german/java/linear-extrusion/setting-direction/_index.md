---
title: Festlegen der Richtung in der linearen Extrusion mit Aspose.3D für Java
linktitle: Festlegen der Richtung in der linearen Extrusion mit Aspose.3D für Java
second_title: Aspose.3D Java-API
description: Meistern Sie die lineare Extrusion mit Aspose.3D für Java! Folgen Sie unserem Leitfaden für eine nahtlose 3D-Programmierung. Laden Sie es jetzt herunter und genießen Sie ein fesselndes Erlebnis.
type: docs
weight: 12
url: /de/java/linear-extrusion/setting-direction/
---
## Einführung

Willkommen zu unserer Schritt-für-Schritt-Anleitung zum Festlegen der Richtung bei der linearen Extrusion mit Aspose.3D für Java. Aspose.3D ist eine leistungsstarke Java-Bibliothek, die Entwicklern die nahtlose Arbeit mit 3D-Dateien und -Szenen ermöglicht. In diesem Tutorial konzentrieren wir uns auf die spezifische Aufgabe der Richtungseinstellung bei der linearen Extrusion und verbessern so Ihre Kenntnisse in der 3D-Programmierung.

## Voraussetzungen

Bevor wir uns mit dem Tutorial befassen, stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind:

- Grundkenntnisse der Programmiersprache Java.
-  Aspose.3D-Bibliothek installiert. Sie können es herunterladen unter[Hier](https://releases.aspose.com/3d/java/).
- Eine integrierte Entwicklungsumgebung (IDE) für Java, wie Eclipse oder IntelliJ.

## Pakete importieren

Stellen Sie sicher, dass Sie die erforderlichen Pakete importieren, um Ihr Projekt zu starten:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Schritt 1: Basisprofil initialisieren

 Beginnen Sie mit der Initialisierung des zu extrudierenden Basisprofils. In diesem Beispiel verwenden wir a`RectangleShape` mit einem Rundungsradius von 0,3:

```java
// Der Pfad zum Dokumentenverzeichnis.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Schritt 2: Erstellen Sie eine Szene

Erstellen Sie als Nächstes eine 3D-Szene, die die extrudierten Objekte enthält:

```java
Scene scene = new Scene();
```

## Schritt 3: Knoten erstellen

Erstellen Sie linke und rechte Knoten innerhalb der Szene:

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Schritt 4: Führen Sie eine lineare Extrusion am linken Knoten durch

 Führen Sie mit dem eine lineare Extrusion am linken Knoten durch`LinearExtrusion`Klasse mit angegebenen Parametern wie Twist und Slices:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Schritt 5: Führen Sie eine lineare Extrusion am rechten Knoten mit Richtung durch

 Führen Sie eine lineare Extrusion am rechten Knoten durch und führen Sie das ein`setDirection` Eigenschaft zum Definieren der Extrusionsrichtung:

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Schritt 6: 3D-Szene speichern

Speichern Sie die 3D-Szene im gewünschten Dateiformat. In diesem Beispiel speichern wir es als Wavefront OBJ-Datei:

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Abschluss

Glückwunsch! Sie haben erfolgreich gelernt, wie Sie mit Aspose.3D für Java die Richtung in der linearen Extrusion festlegen. Dieses Tutorial erweitert Ihre Fähigkeiten in der 3D-Programmierung und eröffnet neue Möglichkeiten für kreative Projekte.

## FAQs

### F1: Kann ich Aspose.3D mit anderen Programmiersprachen verwenden?

A1: Aspose.3D unterstützt verschiedene Programmiersprachen, darunter .NET und Java.

### Q2. Gibt es eine kostenlose Testversion für Aspose.3D?

 A2: Ja, Sie können die Funktionen von Aspose.3D mit einer kostenlosen Testversion erkunden[Hier](https://releases.aspose.com/).

### F3: Wo finde ich eine ausführliche Dokumentation für Aspose.3D für Java?

 A3: Die umfassende Dokumentation ist vorhanden[Hier](https://reference.aspose.com/3d/java/).

### F4: Wie kann ich Unterstützung für Aspose.3D erhalten?

 A4: Besuchen Sie die[Aspose.3D-Forum](https://forum.aspose.com/c/3d/18) für jegliche Hilfe oder Fragen.

### F5: Sind temporäre Lizenzen für Aspose.3D verfügbar?

 A5: Ja, Sie können eine temporäre Lizenz erhalten[Hier](https://purchase.aspose.com/temporary-license/).