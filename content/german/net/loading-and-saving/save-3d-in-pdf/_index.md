---
title: Laden und Speichern – 3D als PDF speichern
linktitle: Laden und Speichern – 3D als PDF speichern
second_title: Aspose.3D .NET API
description: Entdecken Sie Aspose.3D für .NET. Ihre Go-to-Bibliothek für nahtlose 3D-Modellierung und -Rendering. Speichern Sie 3D-Modelle mühelos als PDF.
type: docs
weight: 19
url: /de/net/loading-and-saving/save-3d-in-pdf/
---
## Einführung

Willkommen zu unserem umfassenden Leitfaden zur Verwendung von Aspose.3D für .NET! In diesem Tutorial führen wir Sie durch den Prozess des Ladens und Speicherns von 3D-Modellen und konzentrieren uns dabei auf die spezifische Aufgabe des Speicherns eines 3D-Modells im PDF-Format. Aspose.3D für .NET ist eine leistungsstarke Bibliothek, die effiziente Tools für die Arbeit mit 3D-Dateien bereitstellt und sie zu einer unverzichtbaren Ressource für Entwickler und Enthusiasten auf diesem Gebiet macht.

## Voraussetzungen

Bevor wir uns mit dem Tutorial befassen, stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind:

-  Aspose.3D für .NET: Stellen Sie sicher, dass Sie die Bibliothek installiert haben. Wenn nicht, können Sie es hier herunterladen[Aspose.3D für .NET-Dokumentation](https://reference.aspose.com/3d/net/).

- Entwicklungsumgebung: Richten Sie Ihre bevorzugte .NET-Entwicklungsumgebung ein.

- Grundlegendes Verständnis von 3D-Konzepten: Machen Sie sich mit grundlegenden 3D-Konzepten vertraut, da dieser Leitfaden grundlegende Kenntnisse der 3D-Modellierung voraussetzt.

## Namespaces importieren

Stellen Sie in Ihrem .NET-Projekt sicher, dass Sie die erforderlichen Namespaces importieren, um auf die von Aspose.3D bereitgestellten Funktionen zuzugreifen:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Formats;
using System.Drawing;
```

## Schritt 1: Erstellen Sie eine neue Szene

Beginnen Sie mit der Initialisierung einer neuen 3D-Szene mithilfe der Aspose.3D-Bibliothek. Dies dient als Grundlage für Ihr 3D-Modell.

```csharp
Scene scene = new Scene();
```

## Schritt 2: Fügen Sie einen untergeordneten Zylinderknoten hinzu

Um den Speichervorgang zu demonstrieren, erstellen wir ein einfaches 3D-Modell – einen Zylinder. Fügen Sie der Szene einen Zylinder als untergeordneten Knoten hinzu.

```csharp
scene.RootNode.CreateChildNode("cylinder", new Cylinder()).Material = new PhongMaterial() { DiffuseColor = new Vector3(Color.DarkCyan) };
```

## Schritt 3: Legen Sie den Rendering-Modus und das Beleuchtungsschema fest

Definieren Sie den Rendering-Modus und das Beleuchtungsschema für Ihre 3D-Szene. Mit diesem Schritt können Sie das optische Erscheinungsbild Ihres Modells anpassen.

```csharp
PdfSaveOptions opt = new PdfSaveOptions();
opt.LightingScheme = PdfLightingScheme.CAD;
opt.RenderMode = PdfRenderMode.ShadedIllustration;
```

## Schritt 4: Im PDF-Format speichern

Führen Sie abschließend den Speichervorgang durch, indem Sie das Ausgabeverzeichnis und den Dateinamen angeben. In diesem Fall speichern wir das 3D-Modell im PDF-Format.

```csharp
scene.Save("Your Output Directory" + "output_out.pdf", opt);
```

Stellen Sie sicher, dass Sie „Ihr Ausgabeverzeichnis“ durch den gewünschten Pfad ersetzen.

## Abschluss

 Glückwunsch! Sie haben erfolgreich gelernt, wie Sie mit Aspose.3D für .NET ein einfaches 3D-Modell erstellen und es im PDF-Format speichern. Dies ist nur der Anfang dessen, was Sie mit dieser leistungsstarken Bibliothek erreichen können. Entdecken Sie weitere Funktionen und Möglichkeiten im[Aspose.3D-Dokumentation](https://reference.aspose.com/3d/net/).

## FAQs

### F1: Ist Aspose.3D für .NET mit allen 3D-Dateiformaten kompatibel?

A1: Ja, Aspose.3D für .NET unterstützt eine Vielzahl von 3D-Dateiformaten und gewährleistet so die Kompatibilität mit verschiedenen Industriestandards.

### F2: Kann ich die visuellen Aspekte meines 3D-Modells während des Speichervorgangs anpassen?

A2: Auf jeden Fall! Wie im Tutorial gezeigt, können Sie Rendering-Modi, Beleuchtungsschemata und mehr anpassen, um das gewünschte visuelle Ergebnis zu erzielen.

### F3: Wo finde ich Unterstützung für Aspose.3D für .NET?

 A3: Besuchen Sie die[Aspose.3D-Forum](https://forum.aspose.com/c/3d/18) für Community-Unterstützung und Diskussionen im Zusammenhang mit Aspose.3D für .NET.

### F4: Gibt es eine kostenlose Testversion für Aspose.3D für .NET?

 A4: Ja, Sie können darauf zugreifen[Kostenlose Testphase](https://releases.aspose.com/) um die Möglichkeiten von Aspose.3D für .NET zu erkunden, bevor Sie einen Kauf tätigen.

### F5: Wie kann ich eine temporäre Lizenz für Aspose.3D für .NET erhalten?

 A5: Um eine temporäre Lizenz zu erhalten, besuchen Sie[dieser Link](https://purchase.aspose.com/temporary-license/) und befolgen Sie die bereitgestellten Anweisungen.