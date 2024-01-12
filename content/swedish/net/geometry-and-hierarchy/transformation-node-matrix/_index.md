---
title: Transformera nod med transformationsmatris i 3D-scener
linktitle: Transformera nod med transformationsmatris i 3D-scener
second_title: Aspose.3D .NET API
description: Förvandla noder utan ansträngning i 3D-scener med Aspose.3D för .NET. Lär dig steg-för-steg-nodtransformationer med handledning.
type: docs
weight: 21
url: /sv/net/geometry-and-hierarchy/transformation-node-matrix/
---
## Introduktion

I den dynamiska sfären av 3D-grafik och visualiseringar är förmågan att manipulera objekt inom en scen en avgörande aspekt. Aspose.3D för .NET ger utvecklare möjlighet att sömlöst transformera noder med hjälp av transformationsmatriser, vilket lägger till ett lager av kreativitet och kontroll till 3D-scener. Denna handledning guidar dig genom processen att transformera en nod i en 3D-scen steg för steg.

## Förutsättningar

Innan du dyker in i handledningen, se till att du har följande förutsättningar på plats:

1. Aspose.3D for .NET Library: Se till att du har Aspose.3D-biblioteket installerat i ditt .NET-projekt. Du kan ladda ner den[här](https://releases.aspose.com/3d/net/).

2. Utvecklingsmiljö: Skapa en fungerande .NET-utvecklingsmiljö, och om du inte redan har gjort det, skapa ett nytt projekt där du ska implementera omvandlingarna.

## Importera namnområden

Börja med att importera de nödvändiga namnområdena till ditt .NET-projekt. Dessa namnområden tillhandahåller de väsentliga klasserna och metoderna för manipulation av 3D-scener.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

Nu när vi har täckt grunderna, låt oss dela upp omvandlingsprocessen i en steg-för-steg-guide.

## Steg 1: Initiera scen och nod

```csharp
// ExStart: AddTransformationToNodeByTransformationMatrix
// Initiera scenobjekt
Scene scene = new Scene();

// Initiera Node-klassobjekt
Node cubeNode = new Node("cube");
```

I det här steget skapar vi en ny 3D-scen och en nod som heter "kub" inom den scenen.

## Steg 2: Skapa nät och ställ in geometri

```csharp
// Anrop Common class skapa mesh med polygonbyggarmetoden för att ställa in mesh-instans
Mesh mesh = Common.CreateMeshUsingPolygonBuilder(); 

// Peka noden på Mesh-geometrin
cubeNode.Entity = mesh;
```

Här genererar vi ett nät med polygonbyggarmetoden och tilldelar det till noden och etablerar geometrin för vår kub.

## Steg 3: Ställ in anpassad översättningsmatris

```csharp
//Ställ in anpassad översättningsmatris
cubeNode.Transform.TransformMatrix = new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
);        
```

Definiera en anpassad översättningsmatris för att bestämma den specifika transformationen som tillämpas på noden. Justera matrisvärdena efter behov för din önskade transformation.

## Steg 4: Lägg till nod till scenen

```csharp
// Lägg till en kub i scenen
scene.RootNode.ChildNodes.Add(cubeNode);            
```

Inkludera kubnoden i scenen, vilket gör den till en del av den övergripande 3D-miljön.

## Steg 5: Spara scenen

```csharp
// Sökvägen till dokumentkatalogen.
var output = "Your Output Directory" + "TransformationToNode.fbx";

// Spara 3D-scen i de filformat som stöds
scene.Save(output, FileFormat.FBX7500ASCII);
// ExEnd: AddTransformationToNodeByTransformationMatrix
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

Ange utdatakatalog och filnamn och spara sedan 3D-scenen i önskat filformat. I det här exemplet sparar vi det i formatet FBX7500ASCII.

## Slutsats

Grattis! Du har framgångsrikt transformerat en nod med hjälp av en transformationsmatris i en 3D-scen med Aspose.3D för .NET. Denna förmåga öppnar dörrar till olika och visuellt fängslande 3D-applikationer.

## FAQ's

### F1: Vad är en transformationsmatris i 3D-grafik?

A1: En transformationsmatris är en matematisk representation som används för att tillämpa olika transformationer (översättning, rotation, skalning) på objekt i 3D-rymden.

### F2: Kan jag tillämpa flera transformationer på en enda nod?

S2: Ja, du kan kombinera flera transformationer genom att multiplicera deras respektive matriser och applicera resultatet på noden.

### F3: Finns det andra filformat som stöds för att spara 3D-scener?

 S3: Aspose.3D för .NET stöder olika filformat, inklusive STL, GLTF, OBJ och mer. Referera till[dokumentation](https://reference.aspose.com/3d/net/) för en omfattande lista.

### F4: Hur kan jag få en tillfällig licens för Aspose.3D för .NET?

 A4: Besök[sida för tillfällig licens](https://purchase.aspose.com/temporary-license/) på Asposes webbplats för att få en tillfällig licens för utvärderingsändamål.

### F5: Var kan jag söka hjälp eller få kontakt med Aspose.3D-communityt?

 A5: Besök[Aspose.3D-forum](https://forum.aspose.com/c/3d/18) att ställa frågor, dela erfarenheter och få kontakt med andra utvecklare som använder Aspose.3D.