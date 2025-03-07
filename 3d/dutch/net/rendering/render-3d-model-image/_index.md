---
title: Rendering van 3D-modelafbeelding van camera
linktitle: Rendering van 3D-modelafbeelding van camera
second_title: Aspose.3D .NET-API
description: Ontdek de wereld van 3D-rendering met Aspose.3D voor .NET. Leer hoe u moeiteloos boeiende visualisaties kunt maken met behulp van onze stapsgewijze handleiding.
weight: 11
url: /nl/net/rendering/render-3d-model-image/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Rendering van 3D-modelafbeelding van camera

## Invoering
Het creëren van verbluffende 3D-visualisaties is een spannend aspect van softwareontwikkeling, en met Aspose.3D voor .NET kunt u uw 3D-modellen tot leven brengen. In deze zelfstudie begeleiden we u bij het renderen van een 3D-modelafbeelding vanaf een camera met behulp van Aspose.3D, met stapsgewijze instructies en waardevolle inzichten.
## Vereisten
Voordat we ingaan op het weergaveproces, moet u ervoor zorgen dat u aan de volgende vereisten voldoet:
-  Aspose.3D voor .NET-bibliotheek: Download en installeer de bibliotheek van de .NET-bibliotheek[download link](https://releases.aspose.com/3d/net/).
- 3D-model: bereid een 3D-modelbestand voor (bijvoorbeeld Aspose3D.obj) dat u wilt renderen.
- .NET-ontwikkelomgeving: Zorg ervoor dat u over een werkende .NET-ontwikkelomgeving beschikt.
## Naamruimten importeren
Neem in uw .NET-project de benodigde naamruimten voor Aspose.3D op:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Utilities;
using System.Drawing;
using System.Drawing.Imaging;
```
## Stap 1: Laad de 3D-scène
```csharp
Scene scene = new Scene();
var path = RunExamples.GetDataFilePath("Aspose3D.obj");
scene.Open(path);
```
## Stap 2: Maak een camera
```csharp
Camera cam = new Camera(ProjectionType.Perspective);
cam.NearPlane = 1;
cam.FarPlane = 500;
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(170, 16, 130);
cam.LookAt = new Vector3(28, 0, -30);
```
## Stap 3: Voeg lichten toe aan de scène
```csharp
scene.RootNode.CreateChildNode(new Light()
{
    LightType = LightType.Point,
    ConstantAttenuation = 0.3,
    Color = new Vector3(Color.White)
}).Transform.Translation = new Vector3(30, 10, 10);
scene.RootNode.CreateChildNode(new Light()
{
    LightType = LightType.Directional,
    ConstantAttenuation = 0.3,
    Direction = new Vector3(-0.3, -0.4, 0.3),
    Color = new Vector3(Color.White)
});
scene.RootNode.CreateChildNode(new Light()
{
    LightType = LightType.Spot,
    CastShadows = true,
    LookAt = new Vector3(28, 10, -30),
    Color = new Vector3(Color.White)
}).Transform.Translation = new Vector3(40, 10, 50);
```
## Stap 4: Geef opties voor afbeeldingsweergave op
```csharp
ImageRenderOptions opt = new ImageRenderOptions();
opt.BackgroundColor = Color.AliceBlue;
opt.AssetDirectories.Add("Your Document Directory" + "textures");
opt.EnableShadows = true;
```
## Stap 5: Render de scène
```csharp
scene.Render(cam, "Your Output Directory" + "Render3DModelImageFromCamera.png", new Size(1024, 1024), ImageFormat.Png, opt);
```
## Conclusie
Gefeliciteerd! U hebt met succes een 3D-modelafbeelding van een camera gerenderd met behulp van Aspose.3D voor .NET. Experimenteer gerust met verschillende modellen, camerahoeken en verlichtingsopstellingen om uw 3D-visualisaties te verbeteren.
## Veelgestelde vragen
### Vraag: Kan ik Aspose.3D voor .NET gebruiken met andere 3D-modelleringstools?
A: Aspose.3D ondersteunt verschillende 3D-modelformaten, waardoor het compatibel is met veel populaire modelleringstools.
### Vraag: Hoe kan ik weergaveproblemen oplossen?
 A: Controleer Aspose.3D[forum](https://forum.aspose.com/c/3d/18) voor ondersteuning en oplossingen voor veelvoorkomende weergaveproblemen.
### Vraag: Is er een gratis proefversie beschikbaar?
A: Ja, u kunt de functies van Aspose.3D verkennen door een[gratis proefperiode](https://releases.aspose.com/).
### Vraag: Waar kan ik uitgebreide documentatie vinden?
 A: Raadpleeg de[documentatie](https://reference.aspose.com/3d/net/) voor diepgaande begeleiding over Aspose.3D voor .NET.
### Vraag: Hoe koop ik Aspose.3D voor .NET?
 A: Bezoek de[aankooppagina](https://purchase.aspose.com/buy) om de licentie te verkrijgen die het beste bij uw behoeften past.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
