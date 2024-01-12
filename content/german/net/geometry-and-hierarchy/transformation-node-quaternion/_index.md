---
title: Transformieren von Knoten durch Quaternion in 3D-Szenen
linktitle: Transformieren von Knoten durch Quaternion in 3D-Szenen
second_title: Aspose.3D .NET API
description: Erfahren Sie, wie Sie mit Aspose.3D für .NET 3D-Knoten mit Quaternionen transformieren. Schritt-für-Schritt-Anleitung für Anfänger.
type: docs
weight: 20
url: /de/net/geometry-and-hierarchy/transformation-node-quaternion/
---
## Einführung

Willkommen zu einer Schritt-für-Schritt-Anleitung zum Transformieren eines Knotens durch Quaternion in 3D-Szenen mit Aspose.3D für .NET. In diesem Tutorial erkunden wir die leistungsstarken Funktionen von Aspose.3D für .NET und gehen durch den Prozess des Hinzufügens von Transformationen zu einem 3D-Knoten mithilfe von Quaternionen.

## Voraussetzungen

Bevor wir uns mit dem Tutorial befassen, stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind:

-  Aspose.3D für .NET: Stellen Sie sicher, dass die Aspose.3D-Bibliothek installiert ist. Sie können es hier herunterladen[Release-Seite](https://releases.aspose.com/3d/net/).

- Entwicklungsumgebung: Richten Sie Ihre .NET-Entwicklungsumgebung mit den erforderlichen Tools und Konfigurationen ein.

- Grundlegendes Verständnis von 3D-Konzepten: Vertrautheit mit 3D-Grafiken und -Konzepten ist hilfreich.

## Namespaces importieren

Fügen Sie in Ihr .NET-Projekt die erforderlichen Namespaces für Aspose.3D ein:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

## Schritt 1: Initialisieren Sie das Szenenobjekt

```csharp
// ExStart:AddTransformationToNodeByQuaternion
// Szenenobjekt initialisieren
Scene scene = new Scene();
```

## Schritt 2: Knotenklassenobjekt initialisieren

```csharp
// Node-Klassenobjekt initialisieren
Node cubeNode = new Node("cube");
```

## Schritt 3: Erstellen Sie ein Netz mit Polygon Builder

```csharp
// Rufen Sie die allgemeine Klasse „Erstellen Sie ein Netz mithilfe der Polygon-Builder-Methode“ auf, um eine Netzinstanz festzulegen
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## Schritt 4: Punktknoten auf die Netzgeometrie

```csharp
// Punktknoten zur Mesh-Geometrie
cubeNode.Entity = mesh;
```

## Schritt 5: Legen Sie die Rotation mithilfe von Quaternion fest

```csharp
// Rotation einstellen
cubeNode.Transform.Rotation = Quaternion.FromRotation(new Vector3(0, 1, 0), new Vector3(0.3, 0.5, 0.1));            
```

## Schritt 6: Übersetzung festlegen

```csharp
// Übersetzung festlegen
cubeNode.Transform.Translation = new Vector3(0, 0, 20);            
```

## Schritt 7: Würfel zur Szene hinzufügen

```csharp
// Fügen Sie der Szene einen Würfel hinzu
scene.RootNode.ChildNodes.Add(cubeNode);
```

## Schritt 8: 3D-Szene speichern

```csharp
// Der Pfad zum Dokumentenverzeichnis.
var output = "Your Output Directory" + "TransformationToNode.fbx";

// Speichern Sie die 3D-Szene in den unterstützten Dateiformaten
scene.Save(output, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByQuaternion
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

## Abschluss

Glückwunsch! Sie haben erfolgreich gelernt, wie Sie mit Aspose.3D für .NET einen Knoten durch Quaternion in 3D-Szenen transformieren. Entdecken Sie weitere Funktionen und Möglichkeiten, indem Sie sich auf die beziehen[Dokumentation](https://reference.aspose.com/3d/net/).

## FAQs

### F1: Was ist ein Quaternion in 3D-Grafiken?

A1: Quaternionen sind mathematische Einheiten, die zur Darstellung von Rotationen im 3D-Raum verwendet werden.

### F2: Wie kann ich Aspose.3D für .NET herunterladen?

 A2: Sie können die Bibliothek von herunterladen[Release-Seite](https://releases.aspose.com/3d/net/).

### F3: Gibt es eine kostenlose Testversion für Aspose.3D für .NET?

 A3: Ja, Sie können eine kostenlose Testversion von erhalten[Hier](https://releases.aspose.com/).

### F4: Wo finde ich Unterstützung für Aspose.3D für .NET?

 A4: Besuchen Sie die[Aspose.3D-Forum](https://forum.aspose.com/c/3d/18) für Unterstützung und Diskussionen.

### F5: Wie erhalte ich eine temporäre Lizenz für Aspose.3D?

 A5: Besorgen Sie sich eine temporäre Lizenz[Hier](https://purchase.aspose.com/temporary-license/).
