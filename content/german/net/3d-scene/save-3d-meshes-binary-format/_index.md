---
title: Speichern von 3D-Netzen im benutzerdefinierten Binärformat
linktitle: Speichern von 3D-Netzen im benutzerdefinierten Binärformat
second_title: Aspose.3D .NET API
description: Entdecken Sie die Welt von 3D mit Aspose.3D für .NET. Erfahren Sie, wie Sie Netze im benutzerdefinierten Binärformat speichern.
type: docs
weight: 13
url: /de/net/3d-scene/save-3d-meshes-binary-format/
---
## Einführung

Willkommen in der Welt von Aspose.3D für .NET, einer leistungsstarken Bibliothek, die Entwicklern die mühelose Arbeit mit 3D-Dateien ermöglicht. In diesem Tutorial befassen wir uns mit dem Prozess des Speicherns von 3D-Netzen in einem benutzerdefinierten Binärformat mit Aspose.3D für .NET. In diesem Handbuch wird davon ausgegangen, dass Sie über grundlegende Kenntnisse von C# verfügen und mit der Aspose.3D-Bibliothek vertraut sind.

## Voraussetzungen

Bevor wir mit dem Tutorial beginnen, stellen Sie sicher, dass Sie Folgendes eingerichtet haben:

-  Aspose.3D für .NET: Stellen Sie sicher, dass die Aspose.3D-Bibliothek installiert ist. Sie können es herunterladen unter[Hier](https://releases.aspose.com/3d/net/).

- Entwicklungsumgebung: Richten Sie Ihre bevorzugte C#-Entwicklungsumgebung ein, z. B. Visual Studio.

- Eingabe-3D-Datei: Sie verfügen über eine 3D-Datei (z. B. test.fbx), die Sie in ein benutzerdefiniertes Binärformat konvertieren möchten.

## Namespaces importieren

Fügen Sie in Ihren C#-Code die erforderlichen Namespaces ein, um auf die Aspose.3D-Funktionen zuzugreifen:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
```

## Schritt 1: Laden Sie eine 3D-Datei

Laden Sie Ihre 3D-Datei mit Aspose.3D. In diesem Beispiel laden wir eine Datei namens „test.fbx“:

```csharp
Scene scene = Scene.FromFile("test.fbx");
```

## Schritt 2: Definieren Sie ein benutzerdefiniertes Binärformat

Definieren Sie die Struktur des benutzerdefinierten Binärformats, in dem Sie Ihre 3D-Netze speichern möchten. Das Beispiel verwendet eine Struktur mit MeshBlock, Vertex und Triangle als Komponenten.

```csharp
// Das Speicherlayout eines Scheitelpunkts ist
// float[3] Position;
// float[3] normal;
// float[3] uv;
var vertexDeclaration = new VertexDeclaration();
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Position);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Normal);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.UV);

```

## Schritt 3: Datei zum Schreiben öffnen

Öffnen Sie eine Binärdatei zum Schreiben, in der die konvertierten 3D-Netze gespeichert werden:

```csharp
using (var writer = new BinaryWriter(new FileStream("Your Output Directory" + "Save3DMeshesInCustomBinaryFormat_out", FileMode.Create, FileAccess.Write)))
```

## Schritt 4: Durchlaufen Sie Knoten und Entitäten

Besuchen Sie jeden Knoten in der 3D-Szene und konvertieren Sie Netzelemente in das benutzerdefinierte Binärformat. Ignorieren Sie Lichter, Kameras und andere Nicht-Mesh-Elemente:

```csharp
scene.RootNode.Accept(delegate(Node node)
{
    foreach (Entity entity in node.Entities)
    {
        if (!(entity is IMeshConvertible))
            continue;
        // ... (Verarbeitung fortsetzen)
    }
    return true;
});
```

## Schritt 5: Konvertieren und schreiben Sie Kontrollpunkte und Dreiecke

Konvertieren Sie für jedes Netzelement Kontrollpunkte in den Weltraum und schreiben Sie sie zusammen mit den Dreiecksindizes in die Binärdatei:

```csharp
Mesh m = ((IMeshConvertible)entity).ToMesh();

var triMesh = TriMesh.FromMesh(vertexDeclaration, m);


//Das Speicherlayout des Netzes ist:
// float[16] transform_matrix;
// int vertices_count;
// int indices_count;
// vertex[vertices_count] vertices;
// ushort[indices_count] Indizes;


//Transformation schreiben
var transform = node.GlobalTransform.TransformMatrix.ToArray();
for(int i = 0; i < transform.Length; i++)
    writer.Write((float)transform[i]);
//Anzahl der Eckpunkte/Indizes schreiben
writer.Write(triMesh.VerticesCount);
writer.Write(triMesh.IndicesCount);
//Schreiben Sie Scheitelpunkte und Indizes
writer.Flush();
triMesh.WriteVerticesTo(writer.BaseStream);
triMesh.Write16bIndicesTo(writer.BaseStream);

```

## Abschluss

In diesem Tutorial haben wir den Prozess des Speicherns von 3D-Netzen in einem benutzerdefinierten Binärformat mit Aspose.3D für .NET behandelt. Diese leistungsstarke Bibliothek stellt Entwicklern die Werkzeuge zur Verfügung, die sie zur nahtlosen Bearbeitung von 3D-Dateien benötigen. Experimentieren Sie mit verschiedenen Formaten und Einstellungen, um das volle Potenzial von Aspose.3D in Ihren Projekten auszuschöpfen.

## FAQs

### F1: Kann ich Aspose.3D für .NET mit anderen Programmiersprachen verwenden?

A1: Aspose.3D unterstützt hauptsächlich .NET-Sprachen, Sie können jedoch Kompatibilitätsoptionen für andere Sprachen erkunden.

### F2: Wo finde ich zusätzliche Beispiele und Ressourcen?

 A2: Die[Aspose.3D-Forum](https://forum.aspose.com/c/3d/18)ist ein großartiger Ort, um Unterstützung und Beispiele zu finden und mit der Community in Kontakt zu treten.

### F3: Gibt es eine Testversion für Aspose.3D?

 A3: Ja, Sie können eine kostenlose Testversion von erhalten[Hier](https://releases.aspose.com/).

### F4: Wie erhalte ich eine temporäre Lizenz für Aspose.3D?

 A4: Besuchen[dieser Link](https://purchase.aspose.com/temporary-license/) um eine temporäre Lizenz zu Testzwecken zu erhalten.

### F5: Kann ich Aspose.3D für .NET kaufen?

 A5: Ja, Sie können Aspose.3D bei kaufen[Kaufseite](https://purchase.aspose.com/buy).