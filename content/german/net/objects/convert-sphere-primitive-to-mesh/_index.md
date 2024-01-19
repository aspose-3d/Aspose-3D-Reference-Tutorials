---
title: Konvertieren eines Kugelgrundelements in ein Netz
linktitle: Konvertieren eines Kugelgrundelements in ein Netz
second_title: Aspose.3D .NET API
description: Entdecken Sie Aspose.3D für .NET und konvertieren Sie Sphere Mesh mühelos in Triangle Mesh mit benutzerdefiniertem Speicherlayout. Befolgen Sie unsere Schritt-für-Schritt-Anleitung für eine nahtlose Integration.
type: docs
weight: 16
url: /de/net/objects/convert-sphere-primitive-to-mesh/
---
## Einführung
Möchten Sie die Leistungsfähigkeit von Aspose.3D für .NET nutzen, um ein Kugelnetz in ein Dreiecksnetz mit einem benutzerdefinierten Speicherlayout umzuwandeln? Diese Schritt-für-Schritt-Anleitung führt Sie durch den Prozess und macht es auch Anfängern leicht, mitzumachen. Am Ende dieses Tutorials werden Sie ein solides Verständnis dafür haben, wie Sie dies mit Aspose.3D für .NET erreichen.
## Voraussetzungen
Bevor Sie mit dem Tutorial beginnen, stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind:
- Grundkenntnisse der .NET-Programmierung.
-  Aspose.3D für .NET-Bibliothek installiert. Sie können es hier herunterladen[Aspose.3D für .NET-Downloadseite](https://releases.aspose.com/3d/net/).
- Vertrautheit mit der Programmiersprache C#.
## Namespaces importieren
Stellen Sie in Ihrem C#-Projekt sicher, dass Sie die erforderlichen Namespaces importieren, um die Aspose.3D-Funktionalität zu nutzen:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```
## Schritt 1: Szenenobjekt initialisieren
```csharp
// Szenenobjekt initialisieren
Scene scene = new Scene();
```
## Schritt 2: Knotenklassenobjekt initialisieren
```csharp
// Node-Klassenobjekt initialisieren
Node cubeNode = new Node("sphere");
```
## Schritt 3: Konvertieren Sie das Kugelnetz in ein typisiertes TriMesh
```csharp
Mesh sphere = (new Sphere()).ToMesh();
var myMesh = TriMesh<MyVertex>.FromMesh(sphere);
```
## Schritt 4: Vertex-Daten in benutzerdefinierter Struktur abrufen
```csharp
MyVertex[] vertex = myMesh.VerticesToTypedArray();
```
## Schritt 5: Holen Sie sich 32-Bit- und 16-Bit-Indizes
```csharp
int[] indices32bit;
ushort[] indices16bit;
myMesh.IndicesToArray(out indices32bit);
myMesh.IndicesToArray(out indices16bit);
```
## Schritt 6: Vertex- und Indexdaten in den Speicherstream schreiben
```csharp
using (MemoryStream ms = new MemoryStream())
{
    myMesh.WriteVerticesTo(ms);
    myMesh.Write16bIndicesTo(ms);
    myMesh.Write32bIndicesTo(ms);
}
```
## Schritt 7: Punktknoten zur Netzgeometrie
```csharp
cubeNode.Entity = sphere;
```
## Schritt 8: Knoten zur Szene hinzufügen
```csharp
scene.RootNode.ChildNodes.Add(cubeNode);
```
## Schritt 9: 3D-Szene speichern
```csharp
string output = "Your Output Directory" + "SphereToTriangleMeshCustomMemoryLayoutScene.fbx";
scene.Save(output, FileFormat.FBX7400ASCII);
```
## Schritt 10: Ergebnisse anzeigen
```csharp
Console.WriteLine("Indices = {0}, Actual vertices = {1}, vertices before merging = {2}", myMesh.IndicesCount, myMesh.VerticesCount, myMesh.UnmergedVerticesCount);
Console.WriteLine("Total bytes of vertices in memory {0}bytes", myMesh.VerticesSizeInBytes);
Console.WriteLine("\nConverted a Sphere mesh to a triangle mesh with a custom memory layout of the vertex successfully.\nFile saved at " + output);
```

## MyVertex-Beispielquellcode
```csharp
[StructLayout(LayoutKind.Sequential)]
struct MyVertex
{
	[Semantic(VertexFieldSemantic.Position)]
	FVector3 position;
	[Semantic(VertexFieldSemantic.Normal)]
	FVector3 normal;
}
```
## Abschluss
Glückwunsch! Sie haben mit Aspose.3D für .NET erfolgreich ein Kugelnetz in ein Dreiecksnetz mit einem benutzerdefinierten Speicherlayout konvertiert. Diese leistungsstarke Bibliothek bietet eine nahtlose Möglichkeit, 3D-Objekte in Ihren .NET-Anwendungen zu bearbeiten.
## FAQs
### F: Kann ich Aspose.3D für .NET mit anderen .NET-Frameworks verwenden?
A: Ja, Aspose.3D für .NET ist mit verschiedenen .NET-Frameworks kompatibel.
### F: Wo finde ich eine ausführliche Dokumentation zu Aspose.3D für .NET?
 A: Siehe[Aspose.3D für .NET-Dokumentation](https://reference.aspose.com/3d/net/) für ausführliche Informationen.
### F: Wie kann ich eine temporäre Lizenz für Aspose.3D für .NET erhalten?
 Ein Besuch[dieser Link](https://purchase.aspose.com/temporary-license/) eine befristete Lizenz zu erhalten.
### F: Gibt es Beispielprojekte für Aspose.3D für .NET?
 A: Entdecken Sie die Aspose.3D für .NET-Dokumentation und[GitHub-Repository](https://github.com/aspose-3d/Aspose.3D-for-.NET) für Beispielprojekte.
### F: Gibt es eine aktive Community für Aspose.3D zur .NET-Unterstützung?
 A: Ja, treten Sie dem bei[Aspose.3D für .NET-Forum](https://forum.aspose.com/c/3d/18) um Hilfe von der Community zu erhalten.