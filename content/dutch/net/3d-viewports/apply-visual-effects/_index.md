---
title: Visuele effecten toepassen in 3D-viewports
linktitle: Visuele effecten toepassen in 3D-viewports
second_title: Aspose.3D .NET-API
description: Ontdek de wereld van 3D-visualisatie met Aspose.3D voor .NET. Leer hoe u boeiende visuele effecten op uw scènes kunt toepassen met behulp van stapsgewijze zelfstudies. Verbeter uw projecten met pixelvorming, grijstinten, randdetectie en vervagingseffecten.
type: docs
weight: 10
url: /nl/net/3d-viewports/apply-visual-effects/
---
## Invoering

Het verbeteren van de visuele aantrekkingskracht van 3D-scènes is een cruciaal aspect bij het creëren van meeslepende ervaringen. Aspose.3D voor .NET biedt een krachtige set tools om visuele effecten toe te passen op 3D-viewports. In deze zelfstudie doorlopen we het proces van het toepassen van verschillende effecten op een 3D-scène, waaronder pixelvorming, grijstinten, randdetectie en vervaging.

## Vereisten

Voordat u in de zelfstudie duikt, moet u ervoor zorgen dat u over het volgende beschikt:

- Een praktische kennis van C# en .NET-ontwikkeling.
- Aspose.3D voor .NET-bibliotheek geïnstalleerd. Je kunt het downloaden van[hier](https://releases.aspose.com/3d/net/).
- Een 3D-scènebestand (bijvoorbeeld "scene.obj") voor experimenten.

## Naamruimten importeren

Importeer om te beginnen de benodigde naamruimten voor Aspose.3D en andere afhankelijkheden. Voeg de volgende regels toe aan uw code:

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

## Stap 1: Laad een bestaande 3D-scène

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

 Laad uw 3D-scène met behulp van de`Scene` klas.

## Stap 2: Maak een camera

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

Maak een camera-instantie en stel de positie en het doel ervan in.

## Stap 3: Voeg licht toe aan de scène

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

Introduceer verlichting om de visuele effecten te versterken.

## Stap 4: Maak een renderer en renderdoel

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    // Configureer de rendererinstellingen
    renderer.EnableShadows = false;

    // Maak een renderdoel
    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // Configureer kijkvenster
        Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });

        // Render de scène naar textuur
        renderer.Render(rt);

        // Sla de gerenderde textuur op in een bestand
        ((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "Original_viewport_out.png", ImageFormat.Png);

        // Ga door met nabewerkingseffecten...
    }
}
```

Maak een renderer en een renderdoel om de scène vast te leggen.

## Stap 5: Pas nabewerkingseffecten toe

### Stap 5.1 Pixeleffect

```csharp
//Creëer een pixeleffect
PostProcessing pixelation = renderer.GetPostProcessing("pixelation");
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_pixelation_out.png", ImageFormat.Png);
```

Pas het pixeleffect toe en sla het resultaat op.

### Stap 5.2 Grijswaardeneffect

```csharp
// Creëer een grijswaardeneffect
PostProcessing grayscale = renderer.GetPostProcessing("grayscale");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale_out.png", ImageFormat.Png);
```

Pas het grijswaardeneffect toe en sla het resultaat op.

### Stap 5.3 Combineer effecten

```csharp
// Combineer grijswaarden- en pixeleffecten
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale+pixelation_out.png", ImageFormat.Png);
```

Combineer meerdere effecten voor unieke resultaten.

### Stap 5.4 Randdetectie-effect

```csharp
// Creëer een randdetectie-effect
PostProcessing edgedetection = renderer.GetPostProcessing("edge-detection");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(edgedetection);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_edgedetection_out.png", ImageFormat.Png);
```

Pas het randdetectie-effect toe en sla het resultaat op.

### Stap 5.5 Vervagingseffect

```csharp
// Creëer een vervagingseffect
PostProcessing blur = renderer.GetPostProcessing("blur");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(blur);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_blur_out.png", ImageFormat.Png);
```

Pas het vervagingseffect toe en sla het resultaat op.

## Conclusie

Experimenteren met visuele effecten in 3D-viewports voegt diepte en creativiteit toe aan uw scènes. Aspose.3D voor .NET vereenvoudigt dit proces en biedt een reeks nabewerkingseffecten om uw projecten naar een hoger niveau te tillen.

## Veelgestelde vragen

### Vraag 1: Kan ik meerdere effecten tegelijkertijd toepassen?

A1: Ja, u kunt verschillende nabewerkingseffecten combineren voor unieke en complexe resultaten.

### Vraag 2: Hoe kan ik de intensiteit van visuele effecten aanpassen?

A2: Elk effect kan parameters hebben die u kunt aanpassen om de intensiteit ervan te regelen. Raadpleeg de documentatie voor specifieke details.

### Vraag 3: Is Aspose.3D geschikt voor game-ontwikkeling?

A3: Hoewel Aspose.3D in de eerste plaats is ontworpen voor 3D-modellering en -weergave, kan het in bepaalde aspecten van de game-ontwikkeling worden gebruikt.

### Vraag 4: Zijn er aanvullende nabewerkingseffecten beschikbaar?

A4: Aspose.3D biedt een verscheidenheid aan ingebouwde nabewerkingseffecten en u kunt aangepaste effecten maken met behulp van de bibliotheek.

### Vraag 5: Kan ik Aspose.3D gebruiken voor commerciële projecten?

 A5: Ja, u kunt Aspose.3D voor commerciële doeleinden gebruiken. Verwijs naar de[aankooppagina](https://purchase.aspose.com/buy) voor licentiegegevens.