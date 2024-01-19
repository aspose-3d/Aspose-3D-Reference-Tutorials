---
title: Laddar och sparar - Omvandling av icke-PBR till PBR-material
linktitle: Laddar och sparar - Omvandling av icke-PBR till PBR-material
second_title: Aspose.3D .NET API
description: Utforska Aspose.3D för .NET - Konvertera icke-PBR till PBR-material utan ansträngning. Omfattande handledning och kraftfullt API.
type: docs
weight: 16
url: /sv/net/loading-and-saving/non-pbr-to-pbr-material-conversion/
---
## Introduktion

Välkommen till den här steg-för-steg-guiden om hur du använder Aspose.3D för .NET för att konvertera icke-PBR (fysiskt baserad rendering) till PBR-material. Aspose.3D är ett kraftfullt API som gör att utvecklare kan arbeta sömlöst med 3D-filformat i sina .NET-applikationer.

## Förutsättningar

Innan vi dyker in i handledningen, se till att du har följande förutsättningar:

-  Aspose.3D for .NET: Se till att du har Aspose.3D for .NET-biblioteket installerat. Du hittar nedladdningslänken[här](https://releases.aspose.com/3d/net/).

- Grundläggande förståelse för C#: Denna handledning förutsätter att du har en grundläggande förståelse för C#-programmering.

- IDE (Integrated Development Environment): Välj din föredragna IDE för .NET-utveckling, till exempel Visual Studio.

## Importera namnområden

Börja med att importera de nödvändiga namnrymden i din C#-kod:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Steg 1: Initiera en ny 3D-scen

Börja med att skapa en ny 3D-scen med följande kod:

```csharp
// ExStart:Non_PBRtoPBRMerial
// initiera en ny 3D-scen
var scene = new Scene();
```

## Steg 2: Skapa ett 3D-objekt

Skapa sedan ett 3D-objekt, till exempel en ruta:

```csharp
var box = new Box();
scene.RootNode.CreateChildNode("box1", box).Material = new PhongMaterial() { DiffuseColor = new Vector3(1, 0, 1) };
```

## Steg 3: Konfigurera materialkonvertering

Ställ in materialkonverteringsalternativ för konvertering från icke-PBR till PBR:

```csharp
GltfSaveOptions options = new GltfSaveOptions(FileFormat.GLTF2);
options.MaterialConverter = delegate (Material material)
{
    PhongMaterial phongMaterial = (PhongMaterial)material;
    return new PbrMaterial() { Albedo = new Vector3(phongMaterial.DiffuseColor.x, phongMaterial.DiffuseColor.y, phongMaterial.DiffuseColor.z) };
};
```

## Steg 4: Spara i GLTF 2.0-format

Spara den konverterade scenen i GLTF 2.0-format:

```csharp
scene.Save("Your Output Directory" + "Non_PBRtoPBRMaterial_Out.gltf", options);
// ExEnd:Non_PBRtoPBRMerial
```

Upprepa dessa steg efter behov för ditt specifika användningsfall, och se till att varje detalj är korrekt konfigurerad.

## Slutsats

Grattis! Du har framgångsrikt lärt dig hur man konverterar icke-PBR till PBR-material med Aspose.3D för .NET. Detta kraftfulla verktyg öppnar upp oändliga möjligheter för 3D-grafikmanipulation i dina .NET-applikationer.

## FAQ's

### F1: Är Aspose.3D kompatibel med alla 3D-filformat?

S1: Ja, Aspose.3D stöder ett brett utbud av 3D-filformat, vilket ger flexibilitet i dina projekt.

### F2: Kan jag använda Aspose.3D för kommersiella tillämpningar?

 A2: Absolut! Aspose.3D är en kommersiell produkt och du kan köpa den[här](https://purchase.aspose.com/buy).

### F3: Behöver jag en tillfällig licens för att testa?

S3: Ja, du kan få en tillfällig licens för teständamål[här](https://purchase.aspose.com/temporary-license/).

### F4: Var kan jag hitta support för Aspose.3D?

 A4: Besök[Aspose.3D-forum](https://forum.aspose.com/c/3d/18) för samhällsstöd och diskussioner.

### F5: Finns det en gratis provperiod?

 A5: Ja, du kan utforska en gratis testversion[här](https://releases.aspose.com/).