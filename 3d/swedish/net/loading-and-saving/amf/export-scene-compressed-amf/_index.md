---
title: Exportera 3D-scen till komprimerat AMF-format
linktitle: Exporterar scen till komprimerad AMF
second_title: Aspose.3D .NET API
description: Lär dig hur du exporterar 3D-scener till komprimerat AMF-format med Aspose.3D för .NET. Förbättra dina utvecklingsförmåga med denna steg-för-steg-guide.
weight: 11
url: /sv/net/loading-and-saving/amf/export-scene-compressed-amf/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Exportera 3D-scen till komprimerat AMF-format

## Introduktion

den dynamiska världen av 3D-modellering och rendering är effektivitet och flexibilitet av största vikt. Aspose.3D för .NET ger utvecklare möjlighet att sömlöst exportera 3D-scener till komprimerat AMF-format (Additive Manufacturing File), vilket säkerställer optimal filstorlek utan att kompromissa med kvaliteten. Denna handledning guidar dig genom processen steg för steg, vilket gör det enkelt för både nybörjare och erfarna utvecklare att utnyttja funktionerna i Aspose.3D för .NET.

## Förutsättningar

Innan du dyker in i handledningen, se till att du har följande förutsättningar:

- Grundläggande förståelse för 3D-modelleringskoncept
- Visual Studio installerat på din dator
-  Aspose.3D för .NET-bibliotek. Du kan ladda ner den[här](https://releases.aspose.com/3d/net/)
- En önskan att förbättra dina färdigheter i 3D-utveckling!

## Importera namnområden

Se till att du importerar de nödvändiga namnområdena i ditt projekt för att dra nytta av funktionerna i Aspose.3D för .NET:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Steg 1: Ladda en 3D-scen

Börja med att ladda en 3D-scen med Aspose.3D för .NET. Skapa ett scenobjekt och lägg till enheter som rutor till det:

```csharp
Scene scene = new Scene();
var box = new Box();
var tr = scene.RootNode.CreateChildNode(box).Transform;
tr.Scale = new Vector3(12, 12, 12);
tr.Translation = new Vector3(10, 0, 0);
```

## Steg 2: Skalförvandling

Applicera sedan en skalomvandling på en annan ruta i scenen:

```csharp
tr = scene.RootNode.CreateChildNode(box).Transform;
tr.Scaling = new Vector3(5, 5, 5);
```

## Steg 3: Ställ in Euler-vinklar

Ställ in Euler-vinklar för transformationen:

```csharp
tr.EulerAngles = new Vector3(50, 10, 0);
```

## Steg 4: Spara komprimerad AMF-fil

Slutligen, spara 3D-scenen till en komprimerad AMF-fil i din önskade utdatakatalog:

```csharp
scene.Save("Your Output Directory/" + "Aspose.amf", new AmfSaveOptions() { EnableCompression = false });
```

## Slutsats

Grattis! Du har framgångsrikt exporterat en 3D-scen till ett komprimerat AMF-format med Aspose.3D för .NET. Detta kraftfulla bibliotek öppnar upp en värld av möjligheter för 3D-utvecklare, vilket gör att de kan skapa effektiva och visuellt fantastiska modeller.

## FAQ's

### F1: Är Aspose.3D kompatibel med populära 3D-modelleringsprogram?

S1: Aspose.3D stöder olika filformat, vilket gör den kompatibel med populära 3D-modelleringsverktyg.

### F2: Kan jag aktivera komprimering för andra filformat än AMF?

S2: Ja, Aspose.3D erbjuder alternativ för att aktivera komprimering för olika filformat.

### F3: Är Aspose.3D lämplig för både nybörjare och avancerade utvecklare?

A3: Absolut! Aspose.3D erbjuder enkelhet för nybörjare och avancerade funktioner för erfarna utvecklare.

### F4: Finns det några begränsningar för storleken på 3D-scener som kan exporteras?

A4: Aspose.3D är designad för att hantera scener av varierande komplexitet, och det finns inga strikta storleksbegränsningar.

### F5: Var kan jag hitta ytterligare stöd och diskussioner i samhället?

 A5: Besök[Aspose.3D-forum](https://forum.aspose.com/c/3d/18) för stöd och diskussioner.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
