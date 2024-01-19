---
title: Laddar och sparar - anpassade sparalternativ
linktitle: Laddar och sparar - anpassade sparalternativ
second_title: Aspose.3D .NET API
description: Utforska kraften i Aspose.3D för .NET. Lär dig hur du anpassar ditt 3D-scensparande med steg-för-steg-guider för formaten Collada, 3DS, FBX, OBJ, STL, U3D, glTF, DRC och RVM.
type: docs
weight: 21
url: /sv/net/loading-and-saving/custom-save-options/
---
## Introduktion

Välkommen till Aspose.3Ds värld för .NET! Om du vill förbättra dina 3D-utvecklingsmöjligheter är du på rätt plats. I den här handledningen kommer vi att dyka in i funktionerna för att ladda och spara, speciellt med fokus på anpassade sparaalternativ. Aspose.3D för .NET är ett kraftfullt bibliotek som ger utvecklare möjlighet att manipulera och spara 3D-scener effektivt.

## Förutsättningar

Innan vi börjar utforska de spännande funktionerna i Aspose.3D, se till att du har följande förutsättningar:

- Grundläggande förståelse för C# och .NET utveckling.
-  Aspose.3D för .NET-biblioteket installerat. Du kan ladda ner den från[släpp sida](https://releases.aspose.com/3d/net/).
- En utvecklingsmiljö inrättad med Visual Studio eller någon annan föredragen C# IDE.

## Importera namnområden

För att komma igång, låt oss importera de nödvändiga namnrymden:

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose.ThreeD.Shading;
using System.Drawing;
```

Nu när vi har satt scenen låt oss dela upp handledningen i flera steg.

## Steg 1: Spara alternativet Collada

Låt oss börja med Collada, ett populärt 3D-filformat. Följ dessa steg för att anpassa Colladas sparalternativ:

### 1. Konfigurera katalogen:
   ```csharp
   string dataDir = "Your Document Directory";
   ```

### 2. Initiera Collada-sparalternativ:
   ```csharp
   ColladaSaveOptions saveColladaOpts = new ColladaSaveOptions();
   ```

### 3. Konfigurera alternativ:
   ```csharp
   saveColladaOpts.Indented = true;
   saveColladaOpts.TransformStyle = ColladaTransformStyle.Matrix;
   saveColladaOpts.LookupPaths = new List<string>(new string[] { dataDir });
   ```

## Steg 2: Diskret 3DS-sparalternativ

Låt oss nu utforska Discreet 3DS och dess anpassningsalternativ:

### 1. Konfigurera katalogen:
   ```csharp
   string dataDir = "Your Document Directory";
   ```

### 2. Initiera 3DS-sparalternativ:
   ```csharp
   Discreet3dsSaveOptions saveOpts = new Discreet3dsSaveOptions();
   ```

### 3. Konfigurera alternativ:
   ```csharp
   saveOpts.DuplicatedNameCounterBase = 2;
   // Ytterligare konfigurationsalternativ...
   ```

Fortsätt denna steg-för-steg-strategi för FBX, OBJ, STL, U3D, glTF och DRC spara alternativ, anpassa var och en efter dina krav.

## Steg 3: glTF Spara alternativ

Låt oss nu fokusera på glTF, ett format som används ofta i webb- och mobilapplikationer. Anpassa dina glTF-sparalternativ med dessa steg:

### 1. Initiera scenobjekt:
   ```csharp
   Scene scene = new Scene();
   scene.RootNode.CreateChildNode("sphere", new Sphere());
   ```

### 2. Ställ in glTF-sparalternativ:
   ```csharp
   GltfSaveOptions opt = new GltfSaveOptions(FileContentType.ASCII);
   opt.EmbedAssets = true;
   opt.UseCommonMaterials = true;
   opt.BufferFile = "mybuf.bin";
   ```

### 3. Spara glTF-fil:
   ```csharp
   scene.Save("Your Output Directory" + "glTFSaveOptions_out.gltf", opt);
   ```

Följ en liknande struktur för andra sparalternativ som DRC och RVM.

## Slutsats

Grattis! Du har framgångsrikt utforskat de anpassade sparalternativen i Aspose.3D för .NET. Detta kraftfulla bibliotek ger en mängd alternativ för att skräddarsy din 3D-scensparningsprocess.

## FAQ's

### F1: Kan jag använda Aspose.3D för .NET med andra .NET-ramverk?

S1: Ja, Aspose.3D är kompatibel med olika .NET-ramverk, vilket säkerställer flexibilitet i din utvecklingsmiljö.

### F2: Finns det några licensalternativ för Aspose.3D?

 S2: Ja, du kan utforska licensalternativ[här](https://purchase.aspose.com/buy).

### F3: Var kan jag hitta stöd för Aspose.3D-relaterade frågor?

 A3: Du kan söka stöd på[Aspose.3D-forum](https://forum.aspose.com/c/3d/18).

### F4: Finns det en gratis provperiod?

 A4: Ja, du kan få tillgång till en gratis provperiod[här](https://releases.aspose.com/).

### F5: Hur kan jag få en tillfällig licens för Aspose.3D?

 A5: Skaffa en tillfällig licens[här](https://purchase.aspose.com/temporary-license/).