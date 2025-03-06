---
title: Exportieren einer 3D-Szene in das komprimierte AMF-Format
linktitle: Szene in komprimiertes AMF exportieren
second_title: Aspose.3D .NET API
description: Erfahren Sie, wie Sie 3D-Szenen mit Aspose.3D für .NET in das komprimierte AMF-Format exportieren. Verbessern Sie Ihre Entwicklungsfähigkeiten mit dieser Schritt-für-Schritt-Anleitung.
weight: 11
url: /de/net/loading-and-saving/amf/export-scene-compressed-amf/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Exportieren einer 3D-Szene in das komprimierte AMF-Format

## Einführung

In der dynamischen Welt der 3D-Modellierung und des Renderings sind Effizienz und Flexibilität von größter Bedeutung. Mit Aspose.3D für .NET können Entwickler 3D-Szenen nahtlos in das komprimierte AMF-Format (Additive Manufacturing File) exportieren und so eine optimale Dateigröße ohne Qualitätseinbußen gewährleisten. Dieses Tutorial führt Sie Schritt für Schritt durch den Prozess und macht es sowohl Anfängern als auch erfahrenen Entwicklern leicht, die Funktionen von Aspose.3D für .NET zu nutzen.

## Voraussetzungen

Bevor Sie mit dem Tutorial beginnen, stellen Sie sicher, dass Sie die folgenden Voraussetzungen erfüllen:

- Grundlegendes Verständnis von 3D-Modellierungskonzepten
- Visual Studio ist auf Ihrem Computer installiert
-  Aspose.3D für .NET-Bibliothek. Sie können es herunterladen[Hier](https://releases.aspose.com/3d/net/)
- Der Wunsch, Ihre 3D-Entwicklungsfähigkeiten zu verbessern!

## Namespaces importieren

Stellen Sie in Ihrem Projekt sicher, dass Sie die erforderlichen Namespaces importieren, um die Funktionalität von Aspose.3D für .NET zu nutzen:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Schritt 1: Laden Sie eine 3D-Szene

Beginnen Sie mit dem Laden einer 3D-Szene mit Aspose.3D für .NET. Erstellen Sie ein Szenenobjekt und fügen Sie ihm Elemente wie Boxen hinzu:

```csharp
Scene scene = new Scene();
var box = new Box();
var tr = scene.RootNode.CreateChildNode(box).Transform;
tr.Scale = new Vector3(12, 12, 12);
tr.Translation = new Vector3(10, 0, 0);
```

## Schritt 2: Skalierungstransformation

Wenden Sie als Nächstes eine Skalierungstransformation auf ein anderes Feld in der Szene an:

```csharp
tr = scene.RootNode.CreateChildNode(box).Transform;
tr.Scaling = new Vector3(5, 5, 5);
```

## Schritt 3: Legen Sie die Euler-Winkel fest

Legen Sie die Euler-Winkel für die Transformation fest:

```csharp
tr.EulerAngles = new Vector3(50, 10, 0);
```

## Schritt 4: Komprimierte AMF-Datei speichern

Speichern Sie abschließend die 3D-Szene in einer komprimierten AMF-Datei im gewünschten Ausgabeverzeichnis:

```csharp
scene.Save("Your Output Directory/" + "Aspose.amf", new AmfSaveOptions() { EnableCompression = false });
```

## Abschluss

Glückwunsch! Sie haben mit Aspose.3D für .NET erfolgreich eine 3D-Szene in ein komprimiertes AMF-Format exportiert. Diese leistungsstarke Bibliothek eröffnet 3D-Entwicklern eine Welt voller Möglichkeiten und ermöglicht ihnen die Erstellung effizienter und visuell beeindruckender Modelle.

## FAQs

### F1: Ist Aspose.3D mit gängiger 3D-Modellierungssoftware kompatibel?

A1: Aspose.3D unterstützt verschiedene Dateiformate und ist daher mit gängigen 3D-Modellierungstools kompatibel.

### F2: Kann ich die Komprimierung für andere Dateiformate außer AMF aktivieren?

A2: Ja, Aspose.3D bietet Optionen zum Aktivieren der Komprimierung für verschiedene Dateiformate.

### F3: Ist Aspose.3D sowohl für Anfänger als auch für fortgeschrittene Entwickler geeignet?

A3: Auf jeden Fall! Aspose.3D bietet Einfachheit für Anfänger und erweiterte Funktionen für erfahrene Entwickler.

### F4: Gibt es Einschränkungen hinsichtlich der Größe von 3D-Szenen, die exportiert werden können?

A4: Aspose.3D ist für die Verarbeitung von Szenen unterschiedlicher Komplexität konzipiert und es gibt keine strengen Größenbeschränkungen.

### F5: Wo finde ich zusätzlichen Support und Community-Diskussionen?

 A5: Besuchen Sie die[Aspose.3D-Forum](https://forum.aspose.com/c/3d/18) für Unterstützung und Diskussionen.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
