---
title: Verwenden von Twist Offset in der linearen Extrusion mit Aspose.3D für Java
linktitle: Verwenden von Twist Offset in der linearen Extrusion mit Aspose.3D für Java
second_title: Aspose.3D Java-API
description: Verbessern Sie Ihre 3D-Modellierungskenntnisse mit Aspose.3D für Java. Erfahren Sie in diesem umfassenden Tutorial, wie Sie den Verdrehungsversatz in der linearen Extrusion verwenden.

weight: 15
url: /de/java/linear-extrusion/using-twist-offset/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Verwenden von Twist Offset in der linearen Extrusion mit Aspose.3D für Java

## Einführung

In der dynamischen Welt der 3D-Grafik ist die Beherrschung der Kunst der linearen Extrusion von entscheidender Bedeutung. Mit Aspose.3D für Java können Sie Ihre 3D-Modellierungsfähigkeiten verbessern, indem Sie die Twist-Offset-Funktion in Ihren linearen Extrusionsprozess integrieren. Dieses Tutorial führt Sie durch die Schritte der Verwendung von Twist Offset in der linearen Extrusion mit Aspose.3D für Java und stellt Ihnen die Werkzeuge zur Verfügung, um atemberaubende 3D-Szenen zu erstellen.

## Voraussetzungen

Bevor Sie mit dem Tutorial beginnen, stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind:

- Java-Umgebung: Stellen Sie sicher, dass auf Ihrem System eine Java-Entwicklungsumgebung eingerichtet ist.
-  Aspose.3D für Java: Laden Sie die Aspose.3D-Bibliothek von herunter und installieren Sie sie[Download-Link](https://releases.aspose.com/3d/java/).
-  Dokumentation: Machen Sie sich mit dem vertraut[Aspose.3D für Java-Dokumentation](https://reference.aspose.com/3d/java/).

## Pakete importieren

Importieren Sie in Ihrem Java-Projekt die erforderlichen Pakete, um mit der Verwendung von Aspose.3D für Java zu beginnen. Stellen Sie sicher, dass Sie die erforderlichen Bibliotheken für eine nahtlose Integration einbinden.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Schritt 1: Umgebung einrichten

Beginnen Sie mit der Einrichtung Ihrer Java-Entwicklungsumgebung und stellen Sie sicher, dass Aspose.3D für Java korrekt installiert ist.

## Schritt 2: Initialisieren Sie das Basisprofil

Erstellen Sie ein Basisprofil für die Extrusion, in diesem Fall eine „RectangleShape“ mit einem Rundungsradius von 0,3.

```java
// Der Pfad zum Dokumentenverzeichnis.
String MyDir = "Your Document Directory";
// Initialisieren Sie das zu extrudierende Basisprofil
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Schritt 3: Erstellen Sie eine 3D-Szene

Erstellen Sie eine 3D-Szene, um Ihre extrudierten Objekte unterzubringen.

```java
// Erstellen Sie eine Szene
Scene scene = new Scene();
```

## Schritt 4: Knoten erstellen

Generieren Sie Knoten innerhalb der Szene, um verschiedene Entitäten darzustellen.

```java
// Linken Knoten erstellen
Node left = scene.getRootNode().createChildNode();
// Erstellen Sie den rechten Knoten
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Schritt 5: Führen Sie eine lineare Extrusion durch

Nutzen Sie die lineare Extrusion sowohl für den linken als auch für den rechten Knoten mit verschiedenen Eigenschaften.

```java
// Führen Sie eine lineare Extrusion am linken Knoten mithilfe der Twist- und Slices-Eigenschaft durch
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// Führen Sie eine lineare Extrusion am rechten Knoten mithilfe der Eigenschaft „Drehung“, „Drehungsversatz“ und „Slices“ durch
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

## Schritt 6: Speichern Sie die 3D-Szene

Speichern Sie Ihre neu erstellte 3D-Szene im angegebenen Dateiformat.

```java
// 3D-Szene speichern
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Abschluss

Glückwunsch! Sie haben Twist Offset in der linearen Extrusion mit Aspose.3D für Java erfolgreich implementiert. Diese leistungsstarke Funktion eröffnet eine Welt voller Möglichkeiten für Ihre 3D-Modellierungsbemühungen und ermöglicht Ihnen die Erstellung komplexer und fesselnder Szenen.

## FAQs

### F1: Kann ich Aspose.3D für Java in nichtkommerziellen Projekten verwenden?

 A1: Ja, Aspose.3D für Java kann sowohl in kommerziellen als auch nichtkommerziellen Projekten verwendet werden. Überprüf den[Lizenzoptionen](https://purchase.aspose.com/buy) für mehr Details.

### F2: Wo finde ich Unterstützung für Aspose.3D für Java?

 A2: Besuchen Sie die[Aspose.3D für Java-Forum](https://forum.aspose.com/c/3d/18) um Hilfe zu erhalten und mit der Community in Kontakt zu treten.

### F3: Gibt es eine kostenlose Testversion für Aspose.3D für Java?

 A3: Ja, Sie können eine kostenlose Testversion unter herunterladen[Veröffentlichungsseite](https://releases.aspose.com/).

### F4: Wie erhalte ich eine temporäre Lizenz für Aspose.3D für Java?

 A4: Holen Sie sich eine temporäre Lizenz für Ihr Projekt, indem Sie hier vorbeischauen[dieser Link](https://purchase.aspose.com/temporary-license/).

### F5: Gibt es zusätzliche Beispiele und Tutorials?

 A5: Ja, siehe[Dokumentation](https://reference.aspose.com/3d/java/) Weitere Beispiele und ausführliche Tutorials finden Sie hier.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
