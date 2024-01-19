---
title: Bolgaas omzetten in driehoekig gaas met aangepaste geheugenindeling
linktitle: Bolgaas omzetten in driehoekig gaas met aangepaste geheugenindeling
second_title: Aspose.3D .NET-API
description: Verken Aspose.3D voor .NET en converteer Sphere Mesh moeiteloos naar Triangle Mesh met aangepaste geheugenindeling. Volg onze stapsgewijze handleiding voor een naadloze integratie.
type: docs
weight: 15
url: /nl/net/objects/convert-sphere-mesh-triangle-memory-layout/
---
## Invoering
Wilt u de kracht van Aspose.3D voor .NET benutten om een Sphere Mesh naar een Triangle Mesh te converteren met een aangepaste geheugenindeling? Deze stapsgewijze handleiding begeleidt u door het proces, zodat zelfs beginners het gemakkelijk kunnen volgen. Aan het einde van deze zelfstudie heeft u een goed begrip van hoe u dit kunt bereiken met Aspose.3D voor .NET.
## Vereisten
Voordat u in de zelfstudie duikt, moet u ervoor zorgen dat u aan de volgende vereisten voldoet:
- Basiskennis van .NET-programmering.
-  Aspose.3D voor .NET-bibliotheek geïnstalleerd. Je kunt het downloaden van de[Aspose.3D voor .NET-downloadpagina](https://releases.aspose.com/3d/net/).
- Kennis van de programmeertaal C#.
## Naamruimten importeren
Zorg ervoor dat u in uw C#-project de benodigde naamruimten importeert om de Aspose.3D-functionaliteit te benutten:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Utilities;
using System.Runtime.InteropServices;
```
## Stap 1: Initialiseer het scèneobject
```csharp
// Initialiseer scèneobject
Scene scene = new Scene();
```
## Stap 2: Initialiseer het knooppuntklasseobject
```csharp
// Initialiseer het knooppuntklasseobject
Node cubeNode = new Node("sphere");
```
## Stap 3: Converteer Sphere Mesh naar getypt TriMesh
```csharp
Mesh sphere = (new Sphere()).ToMesh();
var myMesh = TriMesh<MyVertex>.FromMesh(sphere);
```
## Stap 4: Vertex-gegevens in een aangepaste structuur ophalen
```csharp
MyVertex[] vertex = myMesh.VerticesToTypedArray();
```
## Stap 5: Verkrijg 32-bits en 16-bits indexen
```csharp
int[] indices32bit;
ushort[] indices16bit;
myMesh.IndicesToArray(out indices32bit);
myMesh.IndicesToArray(out indices16bit);
```
## Stap 6: Schrijf Vertex- en indexgegevens naar Memory Stream
```csharp
using (MemoryStream ms = new MemoryStream())
{
    myMesh.WriteVerticesTo(ms);
    myMesh.Write16bIndicesTo(ms);
    myMesh.Write32bIndicesTo(ms);
}
```
## Stap 7: Puntknooppunt naar mesh-geometrie
```csharp
cubeNode.Entity = sphere;
```
## Stap 8: Voeg een knooppunt toe aan een scène
```csharp
scene.RootNode.ChildNodes.Add(cubeNode);
```
## Stap 9: Bewaar 3D-scène
```csharp
string output = "Your Output Directory" + "SphereToTriangleMeshCustomMemoryLayoutScene.fbx";
scene.Save(output, FileFormat.FBX7400ASCII);
```
## Stap 10: Resultaten weergeven
```csharp
Console.WriteLine("Indices = {0}, Actual vertices = {1}, vertices before merging = {2}", myMesh.IndicesCount, myMesh.VerticesCount, myMesh.UnmergedVerticesCount);
Console.WriteLine("Total bytes of vertices in memory {0}bytes", myMesh.VerticesSizeInBytes);
Console.WriteLine("\nConverted a Sphere mesh to a triangle mesh with a custom memory layout of the vertex successfully.\nFile saved at " + output);
```
## Conclusie
Gefeliciteerd! U hebt met succes een Sphere Mesh geconverteerd naar een Triangle Mesh met een aangepaste geheugenindeling met behulp van Aspose.3D voor .NET. Deze krachtige bibliotheek biedt een naadloze manier om 3D-objecten in uw .NET-toepassingen te manipuleren.
## Veelgestelde vragen
### Vraag: Kan ik Aspose.3D voor .NET gebruiken met andere .NET-frameworks?
A: Ja, Aspose.3D voor .NET is compatibel met verschillende .NET-frameworks.
### Vraag: Waar kan ik gedetailleerde documentatie vinden voor Aspose.3D voor .NET?
 A: Raadpleeg de[Aspose.3D voor .NET-documentatie](https://reference.aspose.com/3d/net/) voor diepgaande informatie.
### Vraag: Hoe kan ik een tijdelijke licentie krijgen voor Aspose.3D voor .NET?
 Een bezoek[deze link](https://purchase.aspose.com/temporary-license/) om een tijdelijke vergunning te verkrijgen.
### Vraag: Zijn er voorbeeldprojecten beschikbaar voor Aspose.3D voor .NET?
 A: Verken de Aspose.3D voor .NET-documentatie en[GitHub-opslagplaats](https://github.com/aspose-3d/Aspose.3D-for-.NET) voor voorbeeldprojecten.
### Vraag: Is er een actieve community voor Aspose.3D voor .NET-ondersteuning?
 A: Ja, sluit je aan bij de[Aspose.3D voor .NET-forum](https://forum.aspose.com/c/3d/18) om hulp te krijgen van de gemeenschap.