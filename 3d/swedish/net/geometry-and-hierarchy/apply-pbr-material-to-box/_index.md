---
title: Applicera PBR-material på lådan
linktitle: Applicera PBR-material på lådan
second_title: Aspose.3D .NET API
description: Utforska en värld av 3D-grafik med Aspose.3D för .NET. Skapa uppslukande scener utan ansträngning med fysiskt baserad renderingsmaterial.
weight: 10
url: /sv/net/geometry-and-hierarchy/apply-pbr-material-to-box/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Applicera PBR-material på lådan

## Introduktion

Välkommen till den fascinerande världen av 3D-grafik! I den här steg-för-steg-guiden kommer vi att utforska det kraftfulla Aspose.3D för .NET-biblioteket och lära oss hur du skapar fantastiska 3D-scener med hjälp av material för fysiskt baserad rendering (PBR). Aspose.3D förenklar den komplexa processen med 3D-grafik och öppnar upp ett rike av möjligheter för utvecklare.

## Förutsättningar

Innan vi dyker in i den spännande världen av 3D-grafik, låt oss se till att du har allt inrättat:

### Ladda ner och installera Aspose.3D för .NET

 Besök[Aspose.3D för .NET-dokumentation](https://reference.aspose.com/3d/net/) för detaljerade instruktioner om nedladdning och installation av biblioteket.

### Skaffa en licens

Skaffa en giltig licens för att låsa upp Aspose.3Ds fulla potential. Du kan få en tillfällig licens[här](https://purchase.aspose.com/temporary-license/) eller köp en fullständig licens[här](https://purchase.aspose.com/buy).

## Importera namnområden

Se först till att importera de nödvändiga namnområdena för att utnyttja funktionerna i Aspose.3D för .NET:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Steg 1: Initiera en scen

Börja med att initiera en 3D-scen med hjälp av följande kodavsnitt:

```csharp
Scene scene = new Scene();
```

## Steg 2: Initiera PBR-material

Skapa ett PBR-materialobjekt för att uppnå realistisk rendering:

```csharp
PbrMaterial mat = new PbrMaterial();
```

## Steg 3: Ställ in materialegenskaper

Finjustera materialegenskaperna, vilket gör det nästan metalliskt och mycket grovt:

```csharp
mat.MetallicFactor = 0.9;
mat.RoughnessFactor = 0.9;
```

## Steg 4: Skapa en box

Skapa en ruta som PBR-materialet kommer att appliceras på:

```csharp
var boxNode = scene.RootNode.CreateChildNode("box", new Box());
```

## Steg 5: Applicera material på lådan

Tilldela PBR-materialet till den skapade boxnoden:

```csharp
boxNode.Material = mat;
```

## Steg 6: Spara 3D-scenen

Spara 3D-scenen i STL-format med önskad utdatakatalog:

```csharp
scene.Save("Your Output Directory" + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
```

Grattis! Du har framgångsrikt applicerat ett PBR-material på en box i en 3D-scen med Aspose.3D för .NET.

## Slutsats

Att våga sig på 3D-grafik med Aspose.3D för .NET öppnar dörrar till oändliga kreativa möjligheter. Med sitt intuitiva API och robusta funktioner blir det en njutbar upplevelse för utvecklare att skapa visuellt fantastiska scener.

## FAQ's

### F1: Är Aspose.3D kompatibel med andra 3D-filformat?

S1: Ja, Aspose.3D stöder olika 3D-filformat, vilket säkerställer flexibilitet i dina projekt.

### F2: Kan jag använda Aspose.3D för kommersiella tillämpningar?

A2: Absolut! Aspose.3D tillhandahåller kommersiella licenser för sömlös integration i dina applikationer.

### F3: Finns det en testversion tillgänglig?

 S3: Ja, du kan utforska Aspose.3D:s möjligheter genom att ladda ner den kostnadsfria testversionen[här](https://releases.aspose.com/).

### F4: Var kan jag hitta gemenskapsstöd och diskussioner?

 A4: Gå med i Aspose.3D-communityt på[Aspose.3D-forum](https://forum.aspose.com/c/3d/18) för stöd och diskussioner.

### F5: Hur får jag en tillfällig licens för Aspose.3D?

 A5: Du kan få en tillfällig licens[här](https://purchase.aspose.com/temporary-license/) i utvärderingssyfte.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
