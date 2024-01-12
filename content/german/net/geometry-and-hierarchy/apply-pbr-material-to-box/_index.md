---
title: Anwenden von PBR-Material auf Box in 3D-Szenen
linktitle: Anwenden von PBR-Material auf Box in 3D-Szenen
second_title: Aspose.3D .NET API
description: Entdecken Sie die Welt der 3D-Grafik mit Aspose.3D für .NET. Erstellen Sie mühelos immersive Szenen mit Physically Based Rendering-Materialien.
type: docs
weight: 10
url: /de/net/geometry-and-hierarchy/apply-pbr-material-to-box/
---
## Einführung

Willkommen in der faszinierenden Welt der 3D-Grafik! In dieser Schritt-für-Schritt-Anleitung erkunden wir die leistungsstarke Bibliothek Aspose.3D für .NET und erfahren, wie Sie mithilfe von PBR-Materialien (Physically Based Rendering) atemberaubende 3D-Szenen erstellen. Aspose.3D vereinfacht den komplexen Prozess der 3D-Grafik und eröffnet Entwicklern eine Fülle neuer Möglichkeiten.

## Voraussetzungen

Bevor wir in die aufregende Welt der 3D-Grafik eintauchen, stellen wir sicher, dass Sie alles eingerichtet haben:

### Laden Sie Aspose.3D für .NET herunter und installieren Sie es

 Besuche den[Aspose.3D für .NET-Dokumentation](https://reference.aspose.com/3d/net/) Ausführliche Anweisungen zum Herunterladen und Installieren der Bibliothek finden Sie hier.

### Erwerben Sie eine Lizenz

 Um das volle Potenzial von Aspose.3D auszuschöpfen, erwerben Sie eine gültige Lizenz. Sie können eine temporäre Lizenz erhalten[Hier](https://purchase.aspose.com/temporary-license/) oder erwerben Sie eine Volllizenz[Hier](https://purchase.aspose.com/buy).

## Namespaces importieren

Stellen Sie zunächst sicher, dass Sie die erforderlichen Namespaces importieren, um die Funktionen von Aspose.3D für .NET nutzen zu können:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Schritt 1: Initialisieren Sie eine Szene

Beginnen Sie mit der Initialisierung einer 3D-Szene mit dem folgenden Codeausschnitt:

```csharp
Scene scene = new Scene();
```

## Schritt 2: PBR-Material initialisieren

Erstellen Sie ein PBR-Materialobjekt, um ein realistisches Rendering zu erzielen:

```csharp
PbrMaterial mat = new PbrMaterial();
```

## Schritt 3: Materialeigenschaften festlegen

Passen Sie die Materialeigenschaften fein an, sodass es fast metallisch und sehr rau wird:

```csharp
mat.MetallicFactor = 0.9;
mat.RoughnessFactor = 0.9;
```

## Schritt 4: Erstellen Sie eine Box

Erstellen Sie ein Feld, auf das das PBR-Material angewendet wird:

```csharp
var boxNode = scene.RootNode.CreateChildNode("box", new Box());
```

## Schritt 5: Material auf die Box auftragen

Weisen Sie das PBR-Material dem erstellten Boxknoten zu:

```csharp
boxNode.Material = mat;
```

## Schritt 6: Speichern Sie die 3D-Szene

Speichern Sie die 3D-Szene im STL-Format mit dem gewünschten Ausgabeverzeichnis:

```csharp
scene.Save("Your Output Directory" + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
```

Glückwunsch! Sie haben mit Aspose.3D für .NET erfolgreich ein PBR-Material auf eine Box in einer 3D-Szene angewendet.

## Abschluss

Der Einstieg in die 3D-Grafik mit Aspose.3D für .NET eröffnet Türen zu endlosen kreativen Möglichkeiten. Mit seiner intuitiven API und den robusten Funktionen wird die Erstellung visuell beeindruckender Szenen für Entwickler zu einem angenehmen Erlebnis.

## FAQs

### F1: Ist Aspose.3D mit anderen 3D-Dateiformaten kompatibel?

A1: Ja, Aspose.3D unterstützt verschiedene 3D-Dateiformate und sorgt so für Flexibilität bei Ihren Projekten.

### F2: Kann ich Aspose.3D für kommerzielle Anwendungen verwenden?

A2: Auf jeden Fall! Aspose.3D bietet kommerzielle Lizenzen für die nahtlose Integration in Ihre Anwendungen.

### F3: Gibt es eine Testversion?

 A3: Ja, Sie können die Funktionen von Aspose.3D erkunden, indem Sie die kostenlose Testversion herunterladen[Hier](https://releases.aspose.com/).

### F4: Wo finde ich Community-Unterstützung und Diskussionen?

 A4: Treten Sie der Aspose.3D-Community bei[Aspose.3D-Foren](https://forum.aspose.com/c/3d/18) für Unterstützung und Diskussionen.

### F5: Wie erhalte ich eine temporäre Lizenz für Aspose.3D?

 A5: Sie können eine temporäre Lizenz erhalten[Hier](https://purchase.aspose.com/temporary-license/) zu Auswertungszwecken.