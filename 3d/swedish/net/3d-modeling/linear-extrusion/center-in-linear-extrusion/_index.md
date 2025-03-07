---
title: Center i linjär extrudering
linktitle: Center i linjär extrudering
second_title: Aspose.3D .NET API
description: Utforska världen av 3D-modellering med Aspose.3D för .NET. Centrera linjära extruderingstekniker, skapa fantastiska mönster och släpp lös din kreativitet.
weight: 10
url: /sv/net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Center i linjär extrudering

## Introduktion

Välkommen till den här omfattande guiden för att bemästra linjär extrudering med Aspose.3D för .NET. Om du vill förbättra dina färdigheter i 3D-modellering och skapa fantastiska profiler, är du på rätt plats. I den här handledningen kommer vi att fördjupa oss i linjär extruderingsteknik, speciellt med fokus på centreringsaspekten för att ta dina mönster till en helt ny nivå.

## Förutsättningar

Innan vi ger oss ut på denna spännande resa, se till att du har följande förutsättningar på plats:

- Grundläggande förståelse för programmeringsspråket C#.
- Visual Studio installerat på din dator.
-  Aspose.3D för .NET-biblioteket, som du kan ladda ner från[Aspose.3D .NET dokumentation](https://reference.aspose.com/3d/net/).
-  Se till att du har tillgång till[Aspose.3D .NET dokumentation](https://reference.aspose.com/3d/net/) för referens genom hela handledningen.

## Importera namnområden

För att sätta igång, låt oss importera de nödvändiga namnrymden. Dessa kommer att lägga grunden för vårt 3D-modelleringsmästerverk.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Steg 1: Initiera basprofilen

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Steg 2: Skapa en 3D-scen

```csharp
Scene scene = new Scene();
```

## Steg 3: Skapa vänster och höger noder

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## Steg 4: Utför linjär extrudering på vänster nod

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## Steg 5: Ställ in markplan för referens

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## Steg 6: Utför linjär extrudering på höger nod

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## Steg 7: Ställ in jordplan för referens (höger nod)

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## Steg 8: Spara 3D-scen

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Slutsats

Grattis! Du har framgångsrikt bemästrat konsten att linjär extrudering med centrering med Aspose.3D för .NET. Experimentera gärna med olika parametrar och utforska de stora möjligheter denna teknik erbjuder.

## FAQ's

### F1: Kan jag använda Aspose.3D för .NET med andra programmeringsspråk?

S1: Aspose.3D stöder främst .NET-språk som C# och VB.NET.

### F2: Var kan jag hitta stöd för Aspose.3D-relaterade frågor?

 A2: Besök[Aspose.3D Forum](https://forum.aspose.com/c/3d/18) för dedikerat stöd och diskussioner.

### F3: Finns det en gratis testversion tillgänglig för Aspose.3D för .NET?

 A3: Ja, du kan komma åt den kostnadsfria provperioden[här](https://releases.aspose.com/).

### F4: Hur kan jag få en tillfällig licens för Aspose.3D för .NET?

 S4: Du kan skaffa en tillfällig licens[här](https://purchase.aspose.com/temporary-license/).

### F5: Var kan jag köpa Aspose.3D för .NET-licensen?

 A5: Köp din licens[här](https://purchase.aspose.com/buy).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
