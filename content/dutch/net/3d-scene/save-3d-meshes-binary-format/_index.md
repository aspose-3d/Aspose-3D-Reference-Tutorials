---
title: 3D-mazen opslaan in aangepast binair formaat
linktitle: 3D-mazen opslaan in aangepast binair formaat
second_title: Aspose.3D .NET-API
description: Ontdek de wereld van 3D met Aspose.3D voor .NET. Leer hoe u meshes kunt opslaan in een aangepast binair formaat.
type: docs
weight: 13
url: /nl/net/3d-scene/save-3d-meshes-binary-format/
---
## Invoering

Welkom in de wereld van Aspose.3D voor .NET, een krachtige bibliotheek waarmee ontwikkelaars moeiteloos met 3D-bestanden kunnen werken. In deze zelfstudie verdiepen we ons in het proces van het opslaan van 3D-meshes in een aangepast binair formaat met behulp van Aspose.3D voor .NET. In deze handleiding wordt ervan uitgegaan dat u basiskennis heeft van C# en bekend bent met de Aspose.3D-bibliotheek.

## Vereisten

Voordat we met de tutorial beginnen, moet je ervoor zorgen dat je over het volgende beschikt:

-  Aspose.3D voor .NET: Zorg ervoor dat de Aspose.3D-bibliotheek is geïnstalleerd. Je kunt het downloaden van[hier](https://releases.aspose.com/3d/net/).

- Ontwikkelomgeving: Stel uw favoriete C#-ontwikkelomgeving in, zoals Visual Studio.

- Invoer 3D-bestand: Zorg dat u een 3D-bestand heeft (bijvoorbeeld test.fbx) dat u wilt converteren naar een aangepast binair formaat.

## Naamruimten importeren

Neem in uw C#-code de benodigde naamruimten op om toegang te krijgen tot de Aspose.3D-functionaliteiten:

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

## Stap 1: Laad een 3D-bestand

Laad uw 3D-bestand met Aspose.3D. In dit voorbeeld laden we een bestand met de naam "test.fbx":

```csharp
Scene scene = Scene.FromFile("test.fbx");
```

## Stap 2: Definieer een aangepast binair formaat

Definieer de structuur van het aangepaste binaire formaat waarin u uw 3D-meshes wilt opslaan. In het voorbeeld wordt een structuur gebruikt met MeshBlock, Vertex en Triangle als componenten.

```csharp
// De geheugenindeling van een hoekpunt is
// zweefstand[3];
// zweef[3] normaal;
// zweven[3] uv;
var vertexDeclaration = new VertexDeclaration();
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Position);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Normal);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.UV);

```

## Stap 3: Open het bestand om te schrijven

Open een binair bestand om te schrijven, waar de geconverteerde 3D-meshes worden opgeslagen:

```csharp
using (var writer = new BinaryWriter(new FileStream("Your Output Directory" + "Save3DMeshesInCustomBinaryFormat_out", FileMode.Create, FileAccess.Write)))
```

## Stap 4: Herhaal de knooppunten en entiteiten

Bezoek elk knooppunt in de 3D-scène en converteer mesh-entiteiten naar het aangepaste binaire formaat. Negeer lichten, camera's en andere niet-mesh-entiteiten:

```csharp
scene.RootNode.Accept(delegate(Node node)
{
    foreach (Entity entity in node.Entities)
    {
        if (!(entity is IMeshConvertible))
            continue;
        // ... (verder verwerken)
    }
    return true;
});
```

## Stap 5: Converteer en schrijf controlepunten en driehoeken

Converteer voor elke mesh-entiteit controlepunten naar de wereldruimte en schrijf ze naar het binaire bestand, samen met driehoekige indices:

```csharp
Mesh m = ((IMeshConvertible)entity).ToMesh();

var triMesh = TriMesh.FromMesh(vertexDeclaration, m);


//De geheugenindeling van de mesh is:
// float[16] transformatiematrix;
// int hoekpunten_count;
// int index_count;
// hoekpunt[hoekpunten_telling] hoekpunten;
// ushort[indices_count] indices;


//schrijf transformatie
var transform = node.GlobalTransform.TransformMatrix.ToArray();
for(int i = 0; i < transform.Length; i++)
    writer.Write((float)transform[i]);
//schrijf het aantal hoekpunten/indices
writer.Write(triMesh.VerticesCount);
writer.Write(triMesh.IndicesCount);
//schrijf hoekpunten en indices
writer.Flush();
triMesh.WriteVerticesTo(writer.BaseStream);
triMesh.Write16bIndicesTo(writer.BaseStream);

```

## Conclusie

In deze zelfstudie hebben we het proces besproken van het opslaan van 3D-meshes in een aangepast binair formaat met behulp van Aspose.3D voor .NET. Deze krachtige bibliotheek biedt ontwikkelaars de tools die nodig zijn om 3D-bestanden naadloos te manipuleren. Experimenteer met verschillende formaten en instellingen om het volledige potentieel van Aspose.3D in uw projecten te benutten.

## Veelgestelde vragen

### V1: Kan ik Aspose.3D voor .NET gebruiken met andere programmeertalen?

A1: Aspose.3D ondersteunt voornamelijk .NET-talen, maar u kunt compatibiliteitsopties voor andere talen verkennen.

### Vraag 2: Waar kan ik aanvullende voorbeelden en bronnen vinden?

 A2: De[Aspose.3D-forum](https://forum.aspose.com/c/3d/18)is een geweldige plek om ondersteuning en voorbeelden te vinden en contact te maken met de gemeenschap.

### V3: Is er een proefversie beschikbaar voor Aspose.3D?

 A3: Ja, u kunt een gratis proefperiode krijgen van[hier](https://releases.aspose.com/).

### V4: Hoe verkrijg ik een tijdelijke licentie voor Aspose.3D?

 A4: Bezoek[deze link](https://purchase.aspose.com/temporary-license/) om een tijdelijke licentie te verkrijgen voor testdoeleinden.

### V5: Kan ik Aspose.3D voor .NET kopen?

 A5: Ja, u kunt Aspose.3D kopen bij de[aankooppagina](https://purchase.aspose.com/buy).