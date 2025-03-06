---
title: Tillämpa visuella effekter i 3D-vyportar
linktitle: Tillämpa visuella effekter i 3D-vyportar
second_title: Aspose.3D .NET API
description: Utforska en värld av 3D-visualisering med Aspose.3D för .NET. Lär dig att applicera fängslande visuella effekter på dina scener med hjälp av steg-för-steg handledning. Lyft dina projekt med pixelering, gråskala, kantdetektering och oskärpa effekter.
weight: 10
url: /sv/net/rendering/apply-visual-effects/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Tillämpa visuella effekter i 3D-vyportar

## Introduktion

Att förbättra 3D-scenernas visuella tilltalande är en avgörande aspekt för att skapa uppslukande upplevelser. Aspose.3D för .NET tillhandahåller en kraftfull uppsättning verktyg för att applicera visuella effekter på 3D-vyportar. I den här handledningen går vi igenom processen att applicera olika effekter på en 3D-scen, inklusive pixelering, gråskala, kantdetektering och oskärpa.

## Förutsättningar

Innan du dyker in i handledningen, se till att du har följande:

- En praktisk kunskap om C# och .NET utveckling.
-  Aspose.3D för .NET-biblioteket installerat. Du kan ladda ner den från[här](https://releases.aspose.com/3d/net/).
- En 3D-scenfil (t.ex. "scene.obj") för experiment.

## Importera namnområden

För att komma igång, importera nödvändiga namnområden för Aspose.3D och andra beroenden. Lägg till följande rader i din kod:

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

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

 Ladda din 3D-scen med hjälp av`Scene` klass.

## Steg 2: Skapa en kamera

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

Skapa en kamerainstans och ställ in dess position och mål.

## Steg 3: Lägg till ljus till scenen

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

Inför belysning för att förstärka de visuella effekterna.

## Steg 4: Skapa en renderare och rendera mål

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    // Konfigurera renderingsinställningar
    renderer.EnableShadows = false;

    // Skapa ett renderingsmål
    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // Konfigurera viewport
        Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });

        // Gör scenen till struktur
        renderer.Render(rt);

        // Spara den renderade texturen till en fil
        ((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "Original_viewport_out.png", ImageFormat.Png);

        // Fortsätt med efterbehandlingseffekter...
    }
}
```

Skapa en renderare och ett rendermål för att fånga scenen.

## Steg 5: Applicera effekter efter bearbetning

### Steg 5.1 Pixeleringseffekt

```csharp
// Skapa pixeleringseffekt
PostProcessing pixelation = renderer.GetPostProcessing("pixelation");
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_pixelation_out.png", ImageFormat.Png);
```

Använd pixeleringseffekt och spara resultatet.

### Steg 5.2 Gråskaleeffekt

```csharp
// Skapa gråskaleeffekt
PostProcessing grayscale = renderer.GetPostProcessing("grayscale");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale_out.png", ImageFormat.Png);
```

Använd gråskaleeffekt och spara resultatet.

### Steg 5.3 Kombinera effekter

```csharp
// Kombinera gråskala och pixeleringseffekter
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale+pixelation_out.png", ImageFormat.Png);
```

Kombinera flera effekter för unika resultat.

### Steg 5.4 Kantdetekteringseffekt

```csharp
// Skapa kantdetekteringseffekt
PostProcessing edgedetection = renderer.GetPostProcessing("edge-detection");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(edgedetection);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_edgedetection_out.png", ImageFormat.Png);
```

Använd kantdetekteringseffekt och spara resultatet.

### Steg 5.5 Blur Effect

```csharp
// Skapa oskärpa effekt
PostProcessing blur = renderer.GetPostProcessing("blur");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(blur);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_blur_out.png", ImageFormat.Png);
```

Använd oskärpa effekt och spara resultatet.

## Slutsats

Att experimentera med visuella effekter i 3D-vyportar ger djup och kreativitet till dina scener. Aspose.3D för .NET förenklar denna process och erbjuder en rad efterbehandlingseffekter för att lyfta dina projekt.

## FAQ's

### F1: Kan jag använda flera effekter samtidigt?

S1: Ja, du kan kombinera olika efterbehandlingseffekter för unika och komplexa resultat.

### F2: Hur kan jag justera intensiteten för visuella effekter?

S2: Varje effekt kan ha parametrar som du kan justera för att kontrollera dess intensitet. Se dokumentationen för specifik information.

### F3: Är Aspose.3D lämplig för spelutveckling?

S3: Även om Aspose.3D främst är designad för 3D-modellering och rendering, kan den användas i vissa aspekter av spelutveckling.

### F4: Finns det ytterligare efterbehandlingseffekter tillgängliga?

S4: Aspose.3D tillhandahåller en mängd inbyggda efterbehandlingseffekter, och du kan skapa anpassade effekter med hjälp av biblioteket.

### F5: Kan jag använda Aspose.3D för kommersiella projekt?

 S5: Ja, du kan använda Aspose.3D för kommersiella ändamål. Referera till[köpsidan](https://purchase.aspose.com/buy) för licensinformation.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
