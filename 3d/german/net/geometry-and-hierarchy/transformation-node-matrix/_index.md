---
title: Knoten durch Transformationsmatrix transformieren
linktitle: Knoten durch Transformationsmatrix transformieren
second_title: Aspose.3D .NET API
description: Transformieren Sie Knoten mühelos in 3D-Szenen mit Aspose.3D für .NET. Lernen Sie Schritt-für-Schritt-Knotentransformationen mit dem Tutorial.
type: docs
weight: 21
url: /de/net/geometry-and-hierarchy/transformation-node-matrix/
---
## Einführung

Im dynamischen Bereich der 3D-Grafiken und Visualisierungen ist die Fähigkeit, Objekte innerhalb einer Szene zu manipulieren, ein entscheidender Aspekt. Aspose.3D für .NET ermöglicht Entwicklern die nahtlose Transformation von Knoten mithilfe von Transformationsmatrizen und verleiht 3D-Szenen eine Ebene der Kreativität und Kontrolle. Dieses Tutorial führt Sie Schritt für Schritt durch den Prozess der Transformation eines Knotens in einer 3D-Szene.

## Voraussetzungen

Bevor Sie mit dem Tutorial beginnen, stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind:

1.  Aspose.3D für .NET-Bibliothek: Stellen Sie sicher, dass die Aspose.3D-Bibliothek in Ihrem .NET-Projekt installiert ist. Sie können es herunterladen[Hier](https://releases.aspose.com/3d/net/).

2. Entwicklungsumgebung: Richten Sie eine funktionierende .NET-Entwicklungsumgebung ein und erstellen Sie, falls noch nicht geschehen, ein neues Projekt, in dem Sie die Transformationen implementieren.

## Namespaces importieren

Beginnen Sie mit dem Importieren der erforderlichen Namespaces in Ihr .NET-Projekt. Diese Namespaces stellen die wesentlichen Klassen und Methoden für die Manipulation von 3D-Szenen bereit.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

Nachdem wir uns nun mit den Grundlagen befasst haben, wollen wir den Transformationsprozess in einer Schritt-für-Schritt-Anleitung aufschlüsseln.

## Schritt 1: Szene initialisieren

```csharp
// ExStart:AddTransformationToNodeByTransformationMatrix
// Szenenobjekt initialisieren
Scene scene = new Scene();

```

In diesem Schritt erstellen wir eine neue leere 3D-Szene.

## Schritt 2: Netz erstellen und an Szene anhängen

```csharp
// Rufen Sie die allgemeine Klasse „Erstellen Sie ein Netz mithilfe der Polygon-Builder-Methode“ auf, um eine Netzinstanz festzulegen
Mesh mesh = (new Box()).ToMesh();

// Erstellen Sie einen Containerknoten für das Netz.
Node cubeNode = scene.RootNode.CreateChildNode(mesh);
```

Hier generieren wir mit der Polygon-Builder-Methode ein Netz und weisen es dem Knoten zu, um die Geometrie für unseren Würfel festzulegen.

## Schritt 3: Legen Sie eine benutzerdefinierte Übersetzungsmatrix fest

```csharp
// Legen Sie eine benutzerdefinierte Übersetzungsmatrix fest
cubeNode.Transform.TransformMatrix = new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
);        
```

Definieren Sie eine benutzerdefinierte Übersetzungsmatrix, um die spezifische Transformation zu bestimmen, die auf den Knoten angewendet wird. Passen Sie die Matrixwerte nach Bedarf für Ihre gewünschte Transformation an.

Fügen Sie den Würfelknoten in die Szene ein und machen Sie ihn so zu einem Teil der gesamten 3D-Umgebung.

## Schritt 4: Speichern Sie die Szene

```csharp
// Der Pfad zum Dokumentenverzeichnis.
var output = "TransformationToNode.fbx";

// Speichern Sie die 3D-Szene in den unterstützten Dateiformaten
scene.Save(output);
// ExEnd:AddTransformationToNodeByTransformationMatrix
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

Geben Sie das Ausgabeverzeichnis und den Dateinamen an und speichern Sie dann die 3D-Szene im gewünschten Dateiformat. In diesem Beispiel speichern wir es im FBX7500ASCII-Format.

## Abschluss

Glückwunsch! Sie haben einen Knoten mithilfe einer Transformationsmatrix in einer 3D-Szene mit Aspose.3D für .NET erfolgreich transformiert. Diese Fähigkeit öffnet Türen zu vielfältigen und visuell faszinierenden 3D-Anwendungen.

## FAQs

### F1: Was ist eine Transformationsmatrix in 3D-Grafiken?

A1: Eine Transformationsmatrix ist eine mathematische Darstellung, mit der verschiedene Transformationen (Translation, Rotation, Skalierung) auf Objekte im 3D-Raum angewendet werden.

### F2: Kann ich mehrere Transformationen auf einen einzelnen Knoten anwenden?

A2: Ja, Sie können mehrere Transformationen kombinieren, indem Sie ihre jeweiligen Matrizen multiplizieren und das Ergebnis auf den Knoten anwenden.

### F3: Gibt es andere unterstützte Dateiformate zum Speichern von 3D-Szenen?

 A3: Aspose.3D für .NET unterstützt verschiedene Dateiformate, darunter STL, GLTF, OBJ und mehr. Siehe die[Dokumentation](https://reference.aspose.com/3d/net/) für eine umfassende Liste.

### F4: Wie kann ich eine temporäre Lizenz für Aspose.3D für .NET erhalten?

 A4: Besuchen Sie die[temporäre Lizenzseite](https://purchase.aspose.com/temporary-license/)auf der Aspose-Website, um eine temporäre Lizenz zu Evaluierungszwecken zu erhalten.

### F5: Wo kann ich Hilfe suchen oder mich mit der Aspose.3D-Community verbinden?

 A5: Besuchen Sie die[Aspose.3D-Forum](https://forum.aspose.com/c/3d/18) um Fragen zu stellen, Erfahrungen auszutauschen und mit anderen Entwicklern über Aspose.3D in Kontakt zu treten.