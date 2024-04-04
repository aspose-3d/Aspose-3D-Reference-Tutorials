---
title: Konvertierung von Nicht-PBR-Material in PBR-Material
linktitle: Konvertierung von Nicht-PBR-Material in PBR-Material
second_title: Aspose.3D .NET API
description: Entdecken Sie Aspose.3D für .NET – Konvertieren Sie Nicht-PBR-Materialien mühelos in PBR-Materialien. Umfassendes Tutorial und leistungsstarke API.
type: docs
weight: 16
url: /de/net/loading-and-saving/gltf/non-pbr-to-pbr-material-conversion/
---
## Einführung

Willkommen zu dieser Schritt-für-Schritt-Anleitung zur Verwendung von Aspose.3D für .NET zur Konvertierung von Nicht-PBR-Materialien (Physically Based Rendering) in PBR-Materialien. Aspose.3D ist eine leistungsstarke API, die es Entwicklern ermöglicht, nahtlos mit 3D-Dateiformaten in ihren .NET-Anwendungen zu arbeiten.

## Voraussetzungen

Bevor wir uns mit dem Tutorial befassen, stellen Sie sicher, dass Sie die folgenden Voraussetzungen erfüllen:

-  Aspose.3D für .NET: Stellen Sie sicher, dass die Aspose.3D für .NET-Bibliothek installiert ist. Den Download-Link finden Sie hier[Hier](https://releases.aspose.com/3d/net/).

- Grundlegendes Verständnis von C#: In diesem Tutorial wird davon ausgegangen, dass Sie über grundlegende Kenntnisse der C#-Programmierung verfügen.

- IDE (Integrated Development Environment): Wählen Sie Ihre bevorzugte IDE für die .NET-Entwicklung, z. B. Visual Studio.

## Namespaces importieren

Beginnen Sie in Ihrem C#-Code mit dem Importieren der erforderlichen Namespaces:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Schritt 1: Initialisieren Sie eine neue 3D-Szene

Erstellen Sie zunächst eine neue 3D-Szene mit dem folgenden Code:

```csharp
// ExStart:Non_PBRtoPBRMaterial
// Initialisieren Sie eine neue 3D-Szene
var scene = new Scene();
```

## Schritt 2: Erstellen Sie ein 3D-Objekt

Als nächstes erstellen Sie ein 3D-Objekt, zum Beispiel eine Box:

```csharp
var box = new Box();
scene.RootNode.CreateChildNode("box1", box).Material = new PhongMaterial() { DiffuseColor = new Vector3(1, 0, 1) };
```

## Schritt 3: Materialkonvertierung konfigurieren

Richten Sie Materialumwandlungsoptionen für die Konvertierung von Nicht-PBR in PBR ein:

```csharp
GltfSaveOptions options = new GltfSaveOptions(FileFormat.GLTF2);
options.MaterialConverter = delegate (Material material)
{
    PhongMaterial phongMaterial = (PhongMaterial)material;
    return new PbrMaterial() { Albedo = new Vector3(phongMaterial.DiffuseColor.x, phongMaterial.DiffuseColor.y, phongMaterial.DiffuseColor.z) };
};
```

## Schritt 4: Im GLTF 2.0-Format speichern

Speichern Sie die konvertierte Szene im GLTF 2.0-Format:

```csharp
scene.Save("Your Output Directory" + "Non_PBRtoPBRMaterial_Out.gltf", options);
// ExEnd:Non_PBRtoPBRMaterial
```

Wiederholen Sie diese Schritte nach Bedarf für Ihren spezifischen Anwendungsfall und stellen Sie sicher, dass jedes Detail richtig konfiguriert ist.

## Abschluss

Glückwunsch! Sie haben erfolgreich gelernt, wie Sie mit Aspose.3D für .NET Nicht-PBR-Materialien in PBR-Materialien konvertieren. Dieses leistungsstarke Tool eröffnet endlose Möglichkeiten für die 3D-Grafikbearbeitung in Ihren .NET-Anwendungen.

## FAQs

### F1: Ist Aspose.3D mit allen 3D-Dateiformaten kompatibel?

A1: Ja, Aspose.3D unterstützt eine Vielzahl von 3D-Dateiformaten und bietet so Flexibilität bei Ihren Projekten.

### F2: Kann ich Aspose.3D für kommerzielle Anwendungen verwenden?

 A2: Auf jeden Fall! Aspose.3D ist ein kommerzielles Produkt und Sie können es kaufen[Hier](https://purchase.aspose.com/buy).

### F3: Benötige ich zum Testen eine temporäre Lizenz?

 A3: Ja, Sie können zu Testzwecken eine temporäre Lizenz erwerben[Hier](https://purchase.aspose.com/temporary-license/).

### F4: Wo finde ich Unterstützung für Aspose.3D?

 A4: Besuchen Sie die[Aspose.3D-Forum](https://forum.aspose.com/c/3d/18) für Community-Unterstützung und Diskussionen.

### F5: Gibt es eine kostenlose Testversion?

 A5: Ja, Sie können eine kostenlose Testversion ausprobieren[Hier](https://releases.aspose.com/).