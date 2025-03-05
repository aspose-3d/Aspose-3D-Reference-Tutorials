---
title: Spara 3D-nät i anpassat binärt format
linktitle: Spara 3D-nät i anpassat binärt format
second_title: Aspose.3D .NET API
description: Utforska 3D-världen med Aspose.3D för .NET. Lär dig att spara maskor i anpassat binärt format.
type: docs
weight: 13
url: /sv/net/3d-scene/save-3d-meshes-binary-format/
---
## Introduktion

Välkommen till världen av Aspose.3D för .NET, ett kraftfullt bibliotek som ger utvecklare möjlighet att arbeta med 3D-filer utan ansträngning. I den här handledningen kommer vi att fördjupa oss i processen att spara 3D-nät i ett anpassat binärt format med Aspose.3D för .NET. Den här guiden förutsätter att du har en grundläggande förståelse för C# och är bekant med Aspose.3D-biblioteket.

## Förutsättningar

Innan vi går in i handledningen, se till att du har följande på plats:

-  Aspose.3D för .NET: Se till att du har Aspose.3D-biblioteket installerat. Du kan ladda ner den från[här](https://releases.aspose.com/3d/net/).

- Utvecklingsmiljö: Konfigurera din föredragna C#-utvecklingsmiljö, som Visual Studio.

- Inmatning av 3D-fil: Ha en 3D-fil (t.ex. test.fbx) som du vill konvertera till ett anpassat binärt format.

## Importera namnområden

I din C#-kod, inkludera de nödvändiga namnområdena för att komma åt Aspose.3D-funktionerna:

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

## Steg 1: Ladda en 3D-fil

Ladda din 3D-fil med Aspose.3D. I det här exemplet laddar vi en fil med namnet "test.fbx":

```csharp
Scene scene = Scene.FromFile("test.fbx");
```

## Steg 2: Definiera anpassat binärt format

Definiera strukturen för det anpassade binära formatet du vill spara dina 3D-nät i. Exemplet använder en struktur med MeshBlock, Vertex och Triangle som komponenter.

```csharp
// Minneslayouten för en vertex är
// flyta[3] position;
// flyta[3] normal;
// flyta[3] uv;
var vertexDeclaration = new VertexDeclaration();
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Position);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Normal);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.UV);

```

## Steg 3: Öppna fil för skrivning

Öppna en binär fil för skrivning, där de konverterade 3D-maskorna kommer att sparas:

```csharp
using (var writer = new BinaryWriter(new FileStream("Your Output Directory" + "Save3DMeshesInCustomBinaryFormat_out", FileMode.Create, FileAccess.Write)))
```

## Steg 4: Iterera genom noder och enheter

Besök varje nod i 3D-scenen och konvertera mesh-enheter till det anpassade binära formatet. Ignorera lampor, kameror och andra icke-mesh-enheter:

```csharp
scene.RootNode.Accept(delegate(Node node)
{
    foreach (Entity entity in node.Entities)
    {
        if (!(entity is IMeshConvertible))
            continue;
        // ... (fortsätt bearbeta)
    }
    return true;
});
```

## Steg 5: Konvertera och skriv kontrollpunkter och trianglar

För varje mesh-enhet, konvertera kontrollpunkter till världsrymden och skriv dem till den binära filen tillsammans med triangelindex:

```csharp
Mesh m = ((IMeshConvertible)entity).ToMesh();

var triMesh = TriMesh.FromMesh(vertexDeclaration, m);


//Nätets minneslayout är:
// float[16] transform_matrix;
// int vertices_count;
// int index_count;
// vertex[vertices_count] vertex;
// ushort[index_count] index;


//skriva omvandla
var transform = node.GlobalTransform.TransformMatrix.ToArray();
for(int i = 0; i < transform.Length; i++)
    writer.Write((float)transform[i]);
//skriv antal hörn/index
writer.Write(triMesh.VerticesCount);
writer.Write(triMesh.IndicesCount);
//skriva hörn och index
writer.Flush();
triMesh.WriteVerticesTo(writer.BaseStream);
triMesh.Write16bIndicesTo(writer.BaseStream);

```

## Slutsats

I den här handledningen täckte vi processen att spara 3D-nät i ett anpassat binärt format med Aspose.3D för .NET. Detta kraftfulla bibliotek ger utvecklare de verktyg som behövs för att manipulera 3D-filer sömlöst. Experimentera med olika format och inställningar för att låsa upp Aspose.3Ds fulla potential i dina projekt.

## Vanliga frågor

### F1: Kan jag använda Aspose.3D för .NET med andra programmeringsspråk?

S1: Aspose.3D stöder främst .NET-språk, men du kan utforska kompatibilitetsalternativ för andra språk.

### F2: Var kan jag hitta ytterligare exempel och resurser?

 A2: Den[Aspose.3D-forum](https://forum.aspose.com/c/3d/18)är ett bra ställe att hitta stöd, exempel och engagera sig i samhället.

### F3: Finns det en testversion tillgänglig för Aspose.3D?

 A3: Ja, du kan få en gratis provperiod från[här](https://releases.aspose.com/).

### F4: Hur får jag en tillfällig licens för Aspose.3D?

 A4: Besök[den här länken](https://purchase.aspose.com/temporary-license/) för att få en tillfällig licens för teständamål.

### F5: Kan jag köpa Aspose.3D för .NET?

 A5: Ja, du kan köpa Aspose.3D från[köpsidan](https://purchase.aspose.com/buy).