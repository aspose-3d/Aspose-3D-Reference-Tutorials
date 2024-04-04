---
title: Kontrollzentrum in der linearen Extrusion mit Aspose.3D für Java
linktitle: Kontrollzentrum in der linearen Extrusion mit Aspose.3D für Java
second_title: Aspose.3D Java-API
description: Entdecken Sie die Welt der 3D-Grafiken in Java mit Aspose.3D. Steuern Sie mühelos die Mitte bei der linearen Extrusion.
type: docs
weight: 11
url: /de/java/linear-extrusion/controlling-center/
---
## Einführung

In der Welt der 3D-Grafik und der Java-Programmierung spielt die Steuerung des Zentrums bei der linearen Extrusion eine entscheidende Rolle, um die gewünschten Effekte in Ihren Projekten zu erzielen. Aspose.3D für Java bietet ein leistungsstarkes Toolkit zur nahtlosen Bewältigung solcher Aufgaben. In diesem Tutorial tauchen wir in den Prozess der Steuerung des Zentrums bei der linearen Extrusion mit Aspose.3D für Java ein und schlüsseln jeden Schritt auf, um ein reibungsloses und umfassendes Verständnis zu gewährleisten.

## Voraussetzungen

Bevor wir mit dieser Tutorial-Reise beginnen, stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind:

1. Java-Entwicklungsumgebung: Stellen Sie sicher, dass auf Ihrem Computer eine Java-Entwicklungsumgebung eingerichtet ist.

2.  Aspose.3D für Java: Laden Sie die Aspose.3D-Bibliothek herunter und installieren Sie sie. Hier finden Sie die Bibliothek und ihre Dokumentation[Hier](https://reference.aspose.com/3d/java/).

3. Dokumentenverzeichnis: Erstellen Sie ein Verzeichnis zum Speichern Ihrer Java-Dokumente. Nennen wir es „Ihr Dokumentenverzeichnis“.

## Pakete importieren

Importieren Sie in Ihrer Java-Entwicklungsumgebung die erforderlichen Pakete für Aspose.3D. Dadurch wird sichergestellt, dass Ihr Code Zugriff auf die von der Bibliothek bereitgestellten Funktionalitäten hat.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Schritt 1: Richten Sie das Basisprofil ein

Initialisieren Sie das zu extrudierende Basisprofil. In diesem Beispiel verwenden wir eine Rechteckform mit einem Rundungsradius von 0,3.

```java
// Der Pfad zum Dokumentenverzeichnis.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Schritt 2: Erstellen Sie eine 3D-Szene

Schaffen Sie die Grundlage Ihrer 3D-Welt, indem Sie eine Szene erstellen.

```java
Scene scene = new Scene();
```

## Schritt 3: Erstellen Sie linke und rechte Knoten

Richten Sie in Ihrer Szene linke und rechte Knoten ein. Diese Knoten dienen als Leinwand für Ihre 3D-Objekte.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Schritt 4: Lineare Extrusion mit Center-Eigenschaft

Führen Sie eine lineare Extrusion am linken Knoten ohne Zentrierung durch und legen Sie die Anzahl der Slices auf 3 fest.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## Schritt 5: Grundebene als Referenz festlegen

Verbessern Sie die visuelle Darstellung, indem Sie dem linken Knoten eine Grundebene hinzufügen.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## Schritt 6: Lineare Extrusion mit Center-Eigenschaft (rechter Knoten)

Führen Sie eine lineare Extrusion am rechten Knoten durch, wobei Sie dieses Mal die Extrusion zentrieren, und legen Sie die Anzahl der Slices erneut auf 3 fest.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## Schritt 7: Grundebene als Referenz festlegen (rechter Knoten)

Fügen Sie ähnlich wie beim linken Knoten als Referenz eine Grundebene zum rechten Knoten hinzu.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## Schritt 8: Speichern Sie die 3D-Szene

Speichern Sie Ihre 3D-Szene im Wavefront OBJ-Format.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Abschluss

Die Steuerung des Zentrums bei der linearen Extrusion mit Aspose.3D für Java eröffnet spannende Möglichkeiten in der 3D-Grafikentwicklung. Durch Befolgen dieser Schritt-für-Schritt-Anleitung haben Sie gelernt, wie Sie die Center-Eigenschaft manipulieren und so die gewünschten visuellen Effekte in Ihren Java-Projekten erzielen.

## FAQs

### F1: Kann ich Aspose.3D für Java in kommerziellen Projekten verwenden?

 A1: Ja, Aspose.3D für Java ist für die kommerzielle Nutzung verfügbar. Einzelheiten zur Lizenzierung finden Sie unter[Hier](https://purchase.aspose.com/buy).

### F2: Gibt es eine kostenlose Testversion?

 A2: Ja, Sie können eine kostenlose Testversion von Aspose.3D für Java ausprobieren[Hier](https://releases.aspose.com/).

### F3: Wo finde ich Unterstützung für Aspose.3D für Java?

 A3: Das Aspose.3D-Community-Forum ist ein großartiger Ort, um Unterstützung zu suchen und Ihre Erfahrungen auszutauschen. Besuchen Sie das Forum[Hier](https://forum.aspose.com/c/3d/18).

### F4: Benötige ich zum Testen eine temporäre Lizenz?

A4: Ja, wenn Sie zu Testzwecken eine temporäre Lizenz benötigen, können Sie eine erwerben[Hier](https://purchase.aspose.com/temporary-license/).

### F5: Wo finde ich die Dokumentation?

 A5: Die Dokumentation für Aspose.3D für Java ist verfügbar[Hier](https://reference.aspose.com/3d/java/).