---
title: Förstå nodhierarki i 3D-scener
linktitle: Förstå nodhierarki i 3D-scener
second_title: Aspose.3D .NET API
description: Lås upp kraften i Aspose.3D för .NET! Dyk in i nodhierarkimanipulation med denna steg-för-steg-guide. Skapa fantastiska 3D-scener utan ansträngning.
type: docs
weight: 16
url: /sv/net/geometry-and-hierarchy/node-hierarchy/
---
## Introduktion

Välkommen till Aspose.3D för .NET-världen, ett kraftfullt bibliotek som gör det möjligt för utvecklare att arbeta sömlöst med 3D-scener och -modeller i sina .NET-applikationer. I den här handledningen kommer vi att fördjupa oss i krångligheterna med att förstå nodhierarki i 3D-scener med Aspose.3D. I slutet av den här guiden kommer du att ha ett gediget grepp om hur du manipulerar strukturen i 3D-scener genom noder, vilket gör att du kan skapa fantastiska visuella upplevelser.

## Förutsättningar

Innan vi ger oss ut på denna 3D-resa, se till att du har följande förutsättningar på plats:

-  Aspose.3D for .NET Library: Se till att du har Aspose.3D-biblioteket integrerat i ditt .NET-projekt. Om du inte har gjort detta än, gå till[dokumentation](https://reference.aspose.com/3d/net/) för vägledning.

-  Ladda ner biblioteket: Om du inte har laddat ner Aspose.3D-biblioteket, hämta den senaste versionen från[nedladdningslänk](https://releases.aspose.com/3d/net/) och följ installationsinstruktionerna i dokumentationen.

-  Skaffa en licens: För att låsa upp Aspose.3Ds fulla potential behöver du en giltig licens. Om du inte har en så kan du få den[här](https://purchase.aspose.com/buy) eller välj en[gratis provperiod](https://releases.aspose.com/) att utforska dess kapacitet.

- Support och community: Gå med i Aspose.3D-communityt på[supportforum](https://forum.aspose.com/c/3d/18) för att få kontakt med andra utvecklare, söka hjälp och hålla dig uppdaterad om den senaste utvecklingen.

-  Tillfällig licens (valfritt): Om du utforskar Aspose.3D innan du gör ett köp, överväg att skaffa en[tillfällig licens](https://purchase.aspose.com/temporary-license/) för utökad åtkomst.

Nu när vi har våra verktyg redo, låt oss dyka in i den spännande världen av manipulation av 3D-nodhierarki med Aspose.3D.

## Importera namnområden

Se till att du importerar de nödvändiga namnrymden i ditt .NET-projekt för att dra nytta av funktionaliteten som tillhandahålls av Aspose.3D. Lägg till följande rader i din kod:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

Dessa namnutrymmen ger dig tillgång till viktiga klasser och metoder för att arbeta med 3D-scener.

## Steg 1: Initiera scenobjekt

```csharp
Scene scene = new Scene();
```

 Börja med att skapa en ny 3D-scen med hjälp av`Scene` klass.

## Steg 2: Skapa underordnade noder

```csharp
Node top = scene.RootNode.CreateChildNode();
Node cube1 = top.CreateChildNode("cube1");
Node cube2 = top.CreateChildNode("cube2");
```

 Etablera en hierarkisk struktur genom att skapa förälder-barn-relationer mellan noder. I det här exemplet,`cube1` och`cube2` är barnnoder till`top` nod.

## Steg 3: Skapa och tilldela mesh

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
cube1.Entity = mesh;
cube2.Entity = mesh;
```

Generera ett nät med en lämplig metod (här,`CreateMeshUsingPolygonBuilder`) och tilldela den till barnnoderna.

## Steg 4: Ställ in översättningar

```csharp
cube1.Transform.Translation = new Vector3(-10, 0, 0);
cube2.Transform.Translation = new Vector3(10, 0, 0);
```

Definiera översättningar för varje kubnod, placera dem i 3D-utrymmet.

## Steg 5: Tillämpa rotation på överordnad nod

```csharp
top.Transform.Rotation = Quaternion.FromEulerAngle(Math.PI, 4, 0);
```

Rotera den överordnade noden (`top`), och observera hur denna transformation påverkar alla dess underordnade noder.

## Steg 6: Spara 3D-scenen

```csharp
string output = "Your Output Directory" + "NodeHierarchy.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Ange utdatakatalogen och spara 3D-scenen i önskat filformat (här, FBX7500ASCII).

## Steg 7: Visa framgångsmeddelande

```csharp
Console.WriteLine("\nNode hierarchy added successfully to document.\nFile saved at " + output);
```

Informera användaren om det framgångsrika tillägget av nodhierarkin och den sparade filplatsen.

## Slutsats

Grattis! Du har framgångsrikt navigerat i den intrikata världen av 3D-nodhierarki i Aspose.3D för .NET. Denna handledning har utrustat dig med kunskapen för att skapa, manipulera och spara 3D-scener med lätthet. När du fortsätter din resa kan du utforska fler funktioner och frigöra Aspose.3Ds fulla potential i dina .NET-projekt.

## FAQ's

### F1: Kan jag använda Aspose.3D för .NET utan licens?

S1: Medan en licens låser upp alla funktioner kan du utforska Aspose.3D med begränsade möjligheter med hjälp av den kostnadsfria provperioden.

### F2: Finns det andra filformat som stöds för att spara 3D-scener?

S2: Ja, Aspose.3D stöder olika format; se dokumentationen för en fullständig lista.

### F3: Hur kan jag bidra till Aspose.3D-communityt?

S3: Gå med i supportforumet, dela dina erfarenheter och bidra genom att hjälpa andra med deras frågor.

### F4: Är Aspose.3D lämplig för spelutveckling?

A4: Absolut! Aspose.3D är mångsidig och kan integreras i spelutvecklingsprojekt.

### F5: Vad är skillnaden mellan en tillfällig licens och en fullständig licens?

S5: En tillfällig licens ger kortsiktig åtkomst för utvärderingsändamål, medan en fullständig licens erbjuder obegränsad användning.