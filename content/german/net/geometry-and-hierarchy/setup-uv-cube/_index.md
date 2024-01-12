---
title: Einrichten von UV auf Cube in 3D-Szenen
linktitle: Einrichten von UV auf Cube in 3D-Szenen
second_title: Aspose.3D .NET API
description: Erfahren Sie, wie Sie mit Aspose.3D für .NET UV-Mapping auf einem 3D-Würfel einrichten. Erstellen Sie visuell beeindruckende Szenen mit präziser Texturzuordnung.
type: docs
weight: 18
url: /de/net/geometry-and-hierarchy/setup-uv-cube/
---
## Einführung

Die Erstellung fesselnder und optisch ansprechender 3D-Szenen erfordert oft den sorgfältigen Prozess der Einrichtung von UV-Mapping auf geometrischen Formen. In diesem Tutorial erfahren Sie, wie Sie mit Aspose.3D für .NET UV auf einem Würfel einrichten. Aspose.3D ist eine leistungsstarke .NET-Bibliothek, die umfassende Funktionen für die 3D-Modellierung und -Bearbeitung bietet.

## Voraussetzungen

Bevor Sie mit dem Tutorial beginnen, stellen Sie sicher, dass Sie die folgenden Voraussetzungen erfüllen:

1.  Aspose.3D für .NET-Bibliothek: Stellen Sie sicher, dass Sie die Aspose.3D-Bibliothek installiert haben. Sie können es herunterladen[Hier](https://releases.aspose.com/3d/net/).

2. Entwicklungsumgebung: Richten Sie eine .NET-Entwicklungsumgebung mit den erforderlichen Tools ein.

Fahren wir nun mit dem Tutorial fort.

## Namespaces importieren

Importieren Sie zunächst die erforderlichen Namespaces, um auf die Aspose.3D-Funktionen in Ihrer .NET-Anwendung zuzugreifen.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

## Schritt 1: Definieren Sie UVs für den Würfel

Definieren Sie die UV-Koordinaten für jeden Scheitelpunkt des Würfels. Dazu müssen die U- und V-Werte für jede Ecke des Würfels angegeben werden.

```csharp
// ExStart:UVs definieren
Vector4[] uvs = new Vector4[]
{
    new Vector4(0.0, 1.0, 0.0, 1.0),
    new Vector4(1.0, 0.0, 0.0, 1.0),
    new Vector4(0.0, 0.0, 0.0, 1.0),
    new Vector4(1.0, 1.0, 0.0, 1.0)
};
// ExEnd:UVs definieren
```

## Schritt 2: UV-Indizes definieren

Geben Sie die Indizes der UV-Koordinaten für jedes Polygon des Würfels an. Dies definiert, wie die UVs auf die Oberflächen des Würfels abgebildet werden.

```csharp
// ExStart: UV-Indizes definieren
int[] uvsId = new int[]
{
    0, 1, 3, 2, 2, 3, 5, 4, 4, 5, 7, 6, 6, 7, 9, 8, 1, 10, 11, 3, 12, 0, 2, 13
};
// ExEnd:DefineUVIndices
```

## Schritt 3: Erstellen Sie ein Netz

Nutzen Sie die Aspose.3D-Bibliothek, um ein Netz mithilfe einer Polygon-Builder-Methode zu erstellen. Dies dient als Grundlage für unseren 3D-Würfel.

```csharp
// ExStart:CreateMesh
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
// ExEnd:CreateMesh
```

## Schritt 4: UV-Element erstellen

Erstellen Sie ein UV-Element im Netz, um die UV-Mapping-Daten zu speichern.

```csharp
// ExStart:UVElement erstellen
VertexElementUV elementUV = mesh.CreateElementUV(TextureMapping.Diffuse, MappingMode.PolygonVertex, ReferenceMode.IndexToDirect);
// ExEnd:CreateUVElement
```

## Schritt 5: UV-Daten in Mesh kopieren

Kopieren Sie die zuvor definierten UV-Koordinaten und -Indizes in das UV-Scheitelpunktelement des Netzes.

```csharp
// ExStart:UVData kopieren
elementUV.Data.AddRange(uvs);
elementUV.Indices.AddRange(uvsId);
// ExEnd:UVData kopieren
```

## Abschluss

Glückwunsch! Sie haben die UV-Zuordnung für einen Cube mit Aspose.3D für .NET erfolgreich eingerichtet. Dies eröffnet Möglichkeiten zur Erstellung komplexer und visuell beeindruckender 3D-Szenen mit präziser Texturzuordnung.

## FAQs

### F1: Was ist Aspose.3D für .NET?

A1: Aspose.3D für .NET ist eine leistungsstarke Bibliothek für die 3D-Modellierung und -Bearbeitung in .NET-Anwendungen.

### F2: Wo finde ich die Aspose.3D-Dokumentation?

 A2: Die Dokumentation ist verfügbar[Hier](https://reference.aspose.com/3d/net/).

### F3: Gibt es eine kostenlose Testversion?

 A3: Ja, Sie können auf die kostenlose Testversion zugreifen[Hier](https://releases.aspose.com/).

### F4: Wie kann ich Unterstützung für Aspose.3D erhalten?

 A4: Besuchen Sie das Support-Forum[Hier](https://forum.aspose.com/c/3d/18).

### F5: Sind temporäre Lizenzen verfügbar?

 A5: Ja, Sie können eine temporäre Lizenz erhalten[Hier](https://purchase.aspose.com/temporary-license/).