---
title: Fånga visningsportar i 3D-scener
linktitle: Fånga visningsportar i 3D-scener
second_title: Aspose.3D .NET API
description: Lär dig att fånga fantastiska 3D-vyportar med Aspose.3D för .NET. Steg-för-steg-guide för att rendera scener med flexibilitet.
type: docs
weight: 11
url: /sv/net/3d-viewports/capture-viewport/
---
## Introduktion

När det gäller 3D-grafik och visualisering är att fånga visningsportar en viktig färdighet som förbättrar djupet och detaljerna i dina scener. Aspose.3D för .NET ger en robust lösning för att rendera och manipulera 3D-scener. Den här handledningen guidar dig genom processen att fånga visningsportar i 3D-scener med Aspose.3D, så att du enkelt kan skapa fantastiska visualiseringar.

## Förutsättningar

Innan du dyker in i handledningen, se till att du har följande förutsättningar på plats:

-  Aspose.3D for .NET Library: Se till att du har Aspose.3D-biblioteket installerat. Du kan ladda ner den från[här](https://releases.aspose.com/3d/net/).

## Importera namnområden

För att komma igång, importera nödvändiga namnområden till ditt .NET-projekt:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using System.Drawing;
using System.Drawing.Imaging;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
```

## Steg 1: Ladda en befintlig 3D-scen

Börja med att ladda en befintlig 3D-scen i ditt projekt. Följande kodavsnitt visar detta:

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

## Steg 2: Skapa en kamera

Skapa sedan en instans av kameran och ställ in dess position och mål:

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

## Steg 3: Lägg till belysning till scenen

Förbättra din scen genom att lägga till en ljuskälla. Kodavsnittet nedan visar hur man skapar ett punktljus:

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

## Steg 4: Konfigurera Renderer och Render Target

Ställ in renderaren och skapa ett renderingsmål för att fånga scenen:

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    renderer.EnableShadows = false;

    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // ... (fortsättning i nästa steg)
    }
}
```

## Steg 5: Definiera Viewports och Render

Definiera visningsportar och rendera scenen för att generera utdatabilder:

```csharp
Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-1viewports_out.png", ImageFormat.Png);
```

## Steg 6: Ändra visningsportar och rendera igen

Ändra visningsportar och återge scenen igen, vilket visar flexibiliteten hos Aspose.3D:

```csharp
vp.Area = new RelativeRectangle() { ScaleWidth = 0.5f, ScaleHeight = 1 };
rt.CreateViewport(camera, new RelativeRectangle() { ScaleX = 0.5f, ScaleWidth = 0.5f, ScaleHeight = 1 });
camera.FieldOfView = 90;
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-2viewports_out.png", ImageFormat.Png);
```

Fortsätt experimentera med olika konfigurationer för att uppnå önskade visuella effekter.

## Slutsats

I den här handledningen utforskade vi processen att fånga visningsportar i 3D-scener med Aspose.3D för .NET. Med hjälp av dess kraftfulla funktioner kan du lyfta dina 3D-grafikprojekt till nya höjder, vilket ger fängslande visuella upplevelser.

## FAQ's

### F1: Är Aspose.3D kompatibel med andra 3D-filformat?

S1: Ja, Aspose.3D stöder olika 3D-filformat, vilket säkerställer kompatibilitet med ett brett utbud av designverktyg.

### F2: Kan jag använda Aspose.3D för spelutveckling?

S2: Även om Aspose.3D främst är designad för grafik och visualisering, kan dess funktioner komplettera vissa aspekter av spelutveckling.

### F3: Var kan jag hitta ytterligare exempel och dokumentation?

 A3: Utforska det omfattande[Aspose.3D-dokumentation](https://reference.aspose.com/3d/net/) för fler exempel och detaljerad information.

### F4: Finns det en gratis provperiod?

 A4: Ja, du kan få tillgång till en gratis provperiod[här](https://releases.aspose.com/).

### F5: Hur kan jag söka hjälp eller delta i samhället?

 S5: Gå med i Aspose.3D-communityt på[supportforum](https://forum.aspose.com/c/3d/18) för hjälp och samarbete.