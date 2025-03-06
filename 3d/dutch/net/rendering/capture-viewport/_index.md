---
title: Viewports vastleggen in 3D-scènes
linktitle: Viewports vastleggen in 3D-scènes
second_title: Aspose.3D .NET-API
description: Leer verbluffende 3D-viewports vast te leggen met Aspose.3D voor .NET. Stapsgewijze handleiding voor het flexibel renderen van scènes.
weight: 11
url: /nl/net/rendering/capture-viewport/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Viewports vastleggen in 3D-scènes

## Invoering

Op het gebied van 3D-graphics en visualisatie is het vastleggen van viewports een essentiële vaardigheid die de diepte en details van uw scènes verbetert. Aspose.3D voor .NET biedt een robuuste oplossing voor het renderen en manipuleren van 3D-scènes. Deze tutorial leidt u door het proces van het vastleggen van zichtvensters in 3D-scènes met behulp van Aspose.3D, zodat u eenvoudig verbluffende visualisaties kunt maken.

## Vereisten

Voordat u in de zelfstudie duikt, moet u ervoor zorgen dat u aan de volgende vereisten voldoet:

-  Aspose.3D voor .NET-bibliotheek: Zorg ervoor dat de Aspose.3D-bibliotheek is geïnstalleerd. Je kunt het downloaden van[hier](https://releases.aspose.com/3d/net/).

## Naamruimten importeren

Importeer om te beginnen de benodigde naamruimten in uw .NET-project:

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

Begin met het laden van een bestaande 3D-scène in uw project. Het volgende codefragment laat dit zien:

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

## Stap 2: Maak een camera

Maak vervolgens een exemplaar van de camera en stel de positie en het doel in:

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

## Stap 3: Voeg verlichting toe aan de scène

Verbeter uw scène door een lichtbron toe te voegen. Het onderstaande codefragment laat zien hoe u een puntlicht kunt maken:

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

## Stap 4: Configureer Renderer en Render Target

Stel de renderer in en maak een renderdoel voor het vastleggen van de scène:

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    renderer.EnableShadows = false;

    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // ... (vervolg in de volgende stappen)
    }
}
```

## Stap 5: Viewports definiëren en renderen

Definieer zichtvensters en render de scène om uitvoerafbeeldingen te genereren:

```csharp
Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-1viewports_out.png", ImageFormat.Png);
```

## Stap 6: Wijzig de viewports en render opnieuw

Pas viewports aan en render de scène opnieuw, wat de flexibiliteit van Aspose.3D demonstreert:

```csharp
vp.Area = new RelativeRectangle() { ScaleWidth = 0.5f, ScaleHeight = 1 };
rt.CreateViewport(camera, new RelativeRectangle() { ScaleX = 0.5f, ScaleWidth = 0.5f, ScaleHeight = 1 });
camera.FieldOfView = 90;
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-2viewports_out.png", ImageFormat.Png);
```

Blijf experimenteren met verschillende configuraties om de gewenste visuele effecten te bereiken.

## Conclusie

In deze zelfstudie hebben we het proces van het vastleggen van zichtvensters in 3D-scènes onderzocht met behulp van Aspose.3D voor .NET. Door gebruik te maken van de krachtige functies kunt u uw grafische 3D-projecten naar nieuwe hoogten tillen en boeiende visuele ervaringen bieden.

## Veelgestelde vragen

### V1: Is Aspose.3D compatibel met andere 3D-bestandsformaten?

A1: Ja, Aspose.3D ondersteunt verschillende 3D-bestandsformaten, waardoor compatibiliteit met een breed scala aan ontwerptools wordt gegarandeerd.

### Vraag 2: Kan ik Aspose.3D gebruiken voor game-ontwikkeling?

A2: Hoewel Aspose.3D in de eerste plaats is ontworpen voor graphics en visualisatie, kunnen de functionaliteiten ervan bepaalde aspecten van game-ontwikkeling aanvullen.

### V3: Waar kan ik aanvullende voorbeelden en documentatie vinden?

 A3: Ontdek het uitgebreide[Aspose.3D-documentatie](https://reference.aspose.com/3d/net/) voor meer voorbeelden en gedetailleerde informatie.

### Vraag 4: Is er een gratis proefversie beschikbaar?

 A4: Ja, u heeft toegang tot een gratis proefperiode[hier](https://releases.aspose.com/).

### Vraag 5: Hoe kan ik hulp zoeken of deelnemen aan de gemeenschap?

 A5: Sluit u aan bij de Aspose.3D-gemeenschap op de[Helpforum](https://forum.aspose.com/c/3d/18) voor hulp en samenwerking.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
