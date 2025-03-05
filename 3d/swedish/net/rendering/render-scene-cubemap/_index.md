---
title: Återge scen till Cubemap med sex ansikten
linktitle: Återge scen till Cubemap med sex ansikten
second_title: Aspose.3D .NET API
description: Skapa fantastiska kubkartor med Aspose.3D för .NET. Följ vår steg-för-steg-guide för att återge 3D-scener till fängslande kubkartor med sex ansikten.
type: docs
weight: 14
url: /sv/net/rendering/render-scene-cubemap/
---
## Introduktion
Välkommen till den här steg-för-steg-guiden om hur du renderar en scen till en kubkarta med sex ansikten med Aspose.3D för .NET. I den här handledningen går vi igenom processen att skapa en fantastisk kubkarta genom att rendera en 3D-scen. Aspose.3D är ett kraftfullt .NET API som förenklar manipulation av 3D-grafik, och med den här guiden kommer du att utnyttja dess möjligheter för att skapa fängslande kubkartor.
## Förutsättningar
Innan vi dyker in i handledningen, se till att du har följande förutsättningar på plats:
- En praktisk kunskap om C# och .NET utveckling.
-  Aspose.3D för .NET installerat. Du kan ladda ner den[här](https://releases.aspose.com/3d/net/).
- En 3D-scenfil i GLB-format (t.ex. "VirtualCity.glb") för rendering.
## Importera namnområden
Börja med att importera de nödvändiga namnrymden för Aspose.3D i din C#-kod:
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
## Steg 1: Ladda scenen
Ladda 3D-scenfilen med följande kod:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## Steg 2: Skapa kamera och lampor
Skapa en kamera och två lampor för att lysa upp scenen:
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
## Steg 3: Skapa Renderer och Render Target
Skapa en renderare och en kubkarta som renderar mål med djupstruktur:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
    ITextureCubemap cubemap = rt.Targets[0] as ITextureCubemap;
```
## Steg 4: Spara Cubemap Faces
Spara varje sida av kubkartan på disk med specificerade filnamn:
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
## Slutsats
Grattis! Du har framgångsrikt renderat en 3D-scen till en kubkarta med Aspose.3D för .NET. Utforska ytterligare anpassningsalternativ och förbättra dina 3D-grafikprojekt med detta kraftfulla API.
## Vanliga frågor
### F: Kan jag använda Aspose.3D för .NET med andra 3D-filformat?
Ja, Aspose.3D stöder olika 3D-filformat, vilket ger flexibilitet i dina projekt.
### F: Hur kan jag få support för Aspose.3D?
 Besök[Aspose.3D-forum](https://forum.aspose.com/c/3d/18) för samhällsstöd och diskussioner.
### F: Finns det en gratis provperiod?
 Ja, du kan komma åt den kostnadsfria provperioden[här](https://releases.aspose.com/).
### F: Kan jag rendera scener med animationer med Aspose.3D?
Absolut! Aspose.3D stöder rendering av animerade 3D-scener.
### F: Var kan jag hitta detaljerad dokumentation?
 Referera till[Aspose.3D-dokumentation](https://reference.aspose.com/3d/net/) för fördjupad information.