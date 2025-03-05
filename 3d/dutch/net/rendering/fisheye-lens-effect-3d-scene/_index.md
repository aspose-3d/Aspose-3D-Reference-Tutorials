---
title: Fisheye-lenseffect toepassen met Aspose.3D voor .NET
linktitle: Fisheye-lenseffect toepassen op 3D-scène
second_title: Aspose.3D .NET-API
description: Verbeter uw 3D-scènes met Aspose.3D voor .NET! Leer stap voor stap hoe u een boeiend fisheye-lenseffect kunt toepassen. Download nu!
type: docs
weight: 12
url: /nl/net/rendering/fisheye-lens-effect-3d-scene/
---
## Invoering
Wilt u de visuele aantrekkingskracht van uw 3D-scènes verbeteren? Duik in de fascinerende wereld van fisheye-lenseffecten met Aspose.3D voor .NET. Deze tutorial begeleidt u stap voor stap bij het toepassen van een fisheye-lenseffect op uw 3D-scènes, waardoor ze een uniek en boeiend perspectief krijgen.
## Vereisten
Voordat we beginnen, zorg ervoor dat u aan de volgende vereisten voldoet:
-  Aspose.3D voor .NET: Zorg ervoor dat de Aspose.3D-bibliotheek voor .NET is geïnstalleerd. Zo niet, dan kunt u deze downloaden[hier](https://releases.aspose.com/3d/net/).
-  Voorbeeld van een 3D-scène: we gaan werken met een voorbeeld van een 3D-scènebestand (VirtualCity.glb). U kunt uw eigen scène gebruiken of het voorbeeld downloaden van de[Aspose.3D-documentatie](https://reference.aspose.com/3d/net/).
## Naamruimten importeren
Neem in uw .NET-project de benodigde naamruimten op om toegang te krijgen tot de Aspose.3D-functionaliteiten. Voeg de volgende naamruimten toe aan het begin van uw code:
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
## Stap 1: Laad de 3D-scène
Laad het 3D-scènebestand in uw project met behulp van de volgende code:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## Stap 2: Camera en verlichting instellen
Creëer een camera en verlichting om de visuele aspecten van uw scène te verbeteren. Pas indien nodig parameters zoals NearPlane, FarPlane en RotationMode aan:
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light() { Color = new Vector3(Color.CadetBlue) }).Transform.Translation = new Vector3(49, 0, 49);
```
## Stap 3: Maak Renderer en Renderdoelen
Stel de renderer in en maak renderdoelen voor kubuskaart en 2D-textuur:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    IRenderTexture final = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(false, 32, 0, 0), 1024, 1024);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
```
## Stap 4: Fisheye-lenseffect toepassen
Voer de nabewerking van het fisheye-lenseffect uit op de gerenderde kubuskaart:
```csharp
PostProcessing fisheye = renderer.GetPostProcessing("fisheye");
fisheye.FindProperty("fov").Value = 360.0;
fisheye.Input = rt.Targets[0];
renderer.Execute(fisheye, final);
((ITexture2D)final.Targets[0]).Save("Your Output Directory" + "fisheye.png", ImageFormat.Png);
```
## Conclusie
Gefeliciteerd! U hebt met succes een fisheye-lenseffect op uw 3D-scène toegepast met Aspose.3D voor .NET. Experimenteer met verschillende scènes en parameters om je creativiteit de vrije loop te laten.
## Veel Gestelde Vragen
### Kan ik het fisheye-effect op elke 3D-scène toepassen?
Ja, u kunt het fisheye-effect op elke 3D-scène toepassen. Zorg ervoor dat de scène correct is geladen en verlicht voor optimale resultaten.
### Wat is de betekenis van het aanpassen van het gezichtsveld (Fov) tot 360 graden?
Een gezichtsveld van 360 graden zorgt voor een volledige sferische projectie, waardoor een verbluffend fisheye-effect ontstaat.
### Hoe kan ik de verlichting in mijn 3D-scène aanpassen?
Je kunt de eigenschappen van de lampen, zoals positie, type en kleur, aanpassen om de gewenste lichteffecten te bereiken.
### Is er een limiet aan de grootte van de 3D-scène die kan worden verwerkt?
De grootte van de 3D-scène wordt voornamelijk beperkt door systeembronnen. Zorg ervoor dat uw hardware de grootte van uw scène aankan.
### Kan ik een ander uitvoerformaat gebruiken in plaats van PNG voor het resultaat van het fisheye-effect?
Ja, u kunt de code wijzigen om de uitvoer in verschillende afbeeldingsformaten op te slaan, afhankelijk van uw vereisten.