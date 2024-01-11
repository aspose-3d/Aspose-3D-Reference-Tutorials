---
title: Rendering Scene into Cubemap with Six Faces
linktitle: Rendering Scene into Cubemap with Six Faces
second_title: Aspose.3D .NET API
description: Create stunning cubemaps with Aspose.3D for .NET. Follow our step-by-step guide for rendering 3D scenes into captivating six-faced cubemaps.
type: docs
weight: 14
url: /net/rendering/render-scene-cubemap/
---
## Introduction
Welcome to this step-by-step guide on rendering a scene into a cubemap with six faces using Aspose.3D for .NET. In this tutorial, we'll walk you through the process of creating a stunning cubemap by rendering a 3D scene. Aspose.3D is a powerful .NET API that simplifies 3D graphics manipulation, and with this guide, you'll harness its capabilities to create captivating cubemaps.
## Prerequisites
Before we dive into the tutorial, ensure you have the following prerequisites in place:
- A working knowledge of C# and .NET development.
- Aspose.3D for .NET installed. You can download it [here](https://releases.aspose.com/3d/net/).
- A 3D scene file in GLB format (e.g., "VirtualCity.glb") for rendering.
## Import Namespaces
Start by importing the necessary namespaces for Aspose.3D in your C# code:
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
## Step 1: Load the Scene
Load the 3D scene file using the following code:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## Step 2: Create Camera and Lights
Create a camera and two lights to illuminate the scene:
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
## Step 3: Create Renderer and Render Target
Create a renderer and a cube map render target with depth texture:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
    ITextureCubemap cubemap = rt.Targets[0] as ITextureCubemap;
```
## Step 4: Save Cubemap Faces
Save each face of the cubemap to disk with specified file names:
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
## Conclusion
Congratulations! You've successfully rendered a 3D scene into a cubemap using Aspose.3D for .NET. Explore further customization options and enhance your 3D graphics projects with this powerful API.
## Frequently Asked Questions
### Q: Can I use Aspose.3D for .NET with other 3D file formats?
Yes, Aspose.3D supports various 3D file formats, providing flexibility in your projects.
### Q: How can I get support for Aspose.3D?
Visit the [Aspose.3D forum](https://forum.aspose.com/c/3d/18) for community support and discussions.
### Q: Is there a free trial available?
Yes, you can access the free trial [here](https://releases.aspose.com/).
### Q: Can I render scenes with animations using Aspose.3D?
Absolutely! Aspose.3D supports rendering animated 3D scenes.
### Q: Where can I find detailed documentation?
Refer to the official [Aspose.3D documentation](https://reference.aspose.com/3d/net/) for in-depth information.
