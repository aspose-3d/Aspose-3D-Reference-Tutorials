---
title: Scène renderen in Cubemap met zes gezichten
linktitle: Scène renderen in Cubemap met zes gezichten
second_title: Aspose.3D .NET-API
description: Maak verbluffende cubemaps met Aspose.3D voor .NET. Volg onze stapsgewijze handleiding voor het renderen van 3D-scènes in boeiende kubuskaarten met zes gezichten.
weight: 14
url: /nl/net/rendering/render-scene-cubemap/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Scène renderen in Cubemap met zes gezichten

## Invoering
Welkom bij deze stapsgewijze handleiding voor het renderen van een scène in een kubuskaart met zes vlakken met behulp van Aspose.3D voor .NET. In deze zelfstudie leiden we u door het proces van het maken van een verbluffende cubemap door een 3D-scène weer te geven. Aspose.3D is een krachtige .NET API die de manipulatie van 3D-afbeeldingen vereenvoudigt, en met deze handleiding kunt u de mogelijkheden ervan benutten om boeiende cubemaps te maken.
## Vereisten
Voordat we in de tutorial duiken, moet je ervoor zorgen dat je aan de volgende vereisten voldoet:
- Een praktische kennis van C# en .NET-ontwikkeling.
-  Aspose.3D voor .NET geïnstalleerd. Je kunt het downloaden[hier](https://releases.aspose.com/3d/net/).
- Een 3D-scènebestand in GLB-indeling (bijvoorbeeld "VirtualCity.glb") voor weergave.
## Naamruimten importeren
Begin met het importeren van de benodigde naamruimten voor Aspose.3D in uw C#-code:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Imaging;
using System.Linq;
using System.Text;
```
## Stap 1: Laad de scène
Laad het 3D-scènebestand met de volgende code:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## Stap 2: Maak camera en verlichting
Maak een camera en twee lampen om de scène te verlichten:
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light()
{
    Color = new Vector3(Color.CadetBlue)
}).Transform.Translation = new Vector3(49, 0, 49);
```
## Stap 3: Maak Renderer en Render Target
Maak een renderer en een renderdoel voor een kubuskaart met dieptetextuur:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
    ITextureCubemap cubemap = rt.Targets[0] as ITextureCubemap;
```
## Stap 4: Bewaar Cubemap-gezichten
Bewaar elk vlak van de cubemap op schijf met gespecificeerde bestandsnamen:
```csharp
CubeFaceData<string> fileNames = new CubeFaceData<string>()
{
    Right = "Your Output Directory" + "right.png",
    Left = "Your Output Directory" + "left.png",
    Back = "Your Output Directory" + "back.png",
    Front = "Your Output Directory" + "front.png",
    Bottom = "Your Output Directory" + "bottom.png",
    Top = "Your Output Directory" + "top.png"
};
cubemap.Save(fileNames, ImageFormat.Png);
```
## Conclusie
Gefeliciteerd! U hebt met succes een 3D-scène omgezet in een cubemap met behulp van Aspose.3D voor .NET. Ontdek verdere aanpassingsopties en verbeter uw grafische 3D-projecten met deze krachtige API.
## Veel Gestelde Vragen
### Vraag: Kan ik Aspose.3D voor .NET gebruiken met andere 3D-bestandsindelingen?
Ja, Aspose.3D ondersteunt verschillende 3D-bestandsformaten, waardoor u flexibiliteit in uw projecten krijgt.
### Vraag: Hoe kan ik ondersteuning krijgen voor Aspose.3D?
 Bezoek de[Aspose.3D-forum](https://forum.aspose.com/c/3d/18) voor gemeenschapsondersteuning en discussies.
### Vraag: Is er een gratis proefversie beschikbaar?
 Ja, u heeft toegang tot de gratis proefperiode[hier](https://releases.aspose.com/).
### Vraag: Kan ik scènes met animaties renderen met Aspose.3D?
Absoluut! Aspose.3D ondersteunt het weergeven van geanimeerde 3D-scènes.
### Vraag: Waar kan ik gedetailleerde documentatie vinden?
 Verwijs naar de[Aspose.3D-documentatie](https://reference.aspose.com/3d/net/) voor diepgaande informatie.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
