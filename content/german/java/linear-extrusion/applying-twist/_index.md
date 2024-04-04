---
title: Anwenden von Twist in der linearen Extrusion mit Aspose.3D für Java
linktitle: Anwenden von Twist in der linearen Extrusion mit Aspose.3D für Java
second_title: Aspose.3D Java-API
description: Erfahren Sie, wie Sie Ihren 3D-Modellen mit Aspose.3D für Java eine besondere Note verleihen. Befolgen Sie unsere Schritt-für-Schritt-Anleitung für verbesserte lineare Extrusionseffekte.
type: docs
weight: 14
url: /de/java/linear-extrusion/applying-twist/
---
## Einführung

Willkommen zu dieser Schritt-für-Schritt-Anleitung zum Anwenden einer Drehung in der linearen Extrusion mit Aspose.3D für Java. Aspose.3D ist eine leistungsstarke Java-Bibliothek, die Entwicklern die Arbeit mit 3D-Dateiformaten ermöglicht und robuste Funktionen zum Erstellen, Bearbeiten und Rendern von 3D-Szenen bietet. In diesem Tutorial erfahren Sie, wie Sie während des linearen Extrusionsprozesses einen Verdrehungseffekt anwenden, um Ihre 3D-Modelle zu verbessern.

## Voraussetzungen

Bevor Sie mit dem Tutorial beginnen, stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind:

- Java-Entwicklungsumgebung: Stellen Sie sicher, dass Java auf Ihrem System installiert ist.
-  Aspose.3D-Bibliothek: Laden Sie die Aspose.3D-Bibliothek für Java von herunter und installieren Sie sie[Download-Link](https://releases.aspose.com/3d/java/).
-  Dokumentation: Siehe[Aspose.3D-Dokumentation](https://reference.aspose.com/3d/java/) für eine umfassende Beratung.

## Pakete importieren

Bevor Sie mit dem Codierungsprozess beginnen, importieren Sie die erforderlichen Pakete in Ihr Java-Projekt. Hier ist ein Beispiel dafür:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Schritt 1: Dokumentverzeichnis festlegen

Legen Sie zunächst das Dokumentverzeichnis fest, in dem Ihre 3D-Szene gespeichert wird.

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## Schritt 2: Basisprofil initialisieren

Initialisieren Sie das zu extrudierende Basisprofil. In diesem Beispiel verwenden wir eine Rechteckform mit einem Rundungsradius.

```java
// ExStart:InitializeBaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:InitializeBaseProfile
```

## Schritt 3: Erstellen Sie eine Szene

Erstellen Sie eine 3D-Szene als Host für die extrudierten Knoten.

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
```

## Schritt 4: Knoten erstellen

Erstellen Sie linke und rechte Knoten innerhalb der Szene. Passen Sie die Übersetzung des linken Knotens an.

```java
// ExStart:CreateNodes
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CreateNodes
```

## Schritt 5: Führen Sie eine lineare Extrusion mit Drehung durch

Führen Sie eine lineare Extrusion sowohl am linken als auch am rechten Knoten durch und wenden Sie dabei die Eigenschaften „Drehung“ und „Scheiben“ an.

```java
// ExStart:LinearExtrusionWithTwist
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd:LinearExtrusionWithTwist
```

## Schritt 6: 3D-Szene speichern

Speichern Sie die 3D-Szene im Wavefront OBJ-Dateiformat.

```java
// ExStart:Save3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
//ExEnd:Save3DScene
```

## Abschluss

Glückwunsch! Sie haben mit Aspose.3D für Java erfolgreich eine Drehung in der linearen Extrusion angewendet. Dieses Tutorial bietet eine detaillierte Schritt-für-Schritt-Anleitung, die Ihnen dabei hilft, Ihre 3D-Modellierungsfunktionen zu verbessern.

## FAQs

### F1: Kann ich Aspose.3D für Java verwenden, um mit anderen 3D-Dateiformaten zu arbeiten?

A1: Ja, Aspose.3D unterstützt verschiedene 3D-Dateiformate, sodass Sie verschiedene Dateitypen importieren, exportieren und bearbeiten können.

### F2: Wo finde ich Unterstützung für Aspose.3D für Java?

 A2: Besuchen Sie die[Aspose.3D-Forum](https://forum.aspose.com/c/3d/18) für Community-Unterstützung und Diskussionen.

### F3: Gibt es eine kostenlose Testversion für Aspose.3D für Java?

 A3: Ja, Sie können auf die kostenlose Testversion zugreifen[Hier](https://releases.aspose.com/).

### F4: Wie kann ich eine temporäre Lizenz für Aspose.3D für Java erhalten?

 A4: Holen Sie sich eine temporäre Lizenz vom[temporäre Lizenzseite](https://purchase.aspose.com/temporary-license/).

### F5: Wo kann ich Aspose.3D für Java kaufen?

 A5: Kaufen Sie Aspose.3D für Java bei[Kaufseite](https://purchase.aspose.com/buy).