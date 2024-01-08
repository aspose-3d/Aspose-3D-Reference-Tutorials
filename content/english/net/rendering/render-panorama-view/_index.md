---
title: Rendering -  Rendering Panorama View of 3D Scene
linktitle: Rendering -  Rendering Panorama View of 3D Scene
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 13
url: /net/rendering/render-panorama-view/
---

## Complete Source Code
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

namespace Aspose._3D.Examples.CSharp.Rendering
{
    class RenderPanaromaViewof3DScene
    {
        public static void Run()
        {
            try
            {
                // ExStart:RenderPanaromaViewof3DScene

                //load the scene
                Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
                //create a camera for capturing the cube map
                Camera cam = new Camera(ProjectionType.Perspective)
                {
                    NearPlane = 0.1,
                    FarPlane = 200,
                    RotationMode = RotationMode.FixedDirection
                };
                scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);

                //create two lights to illuminate the scene
                scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
                scene.RootNode.CreateChildNode(new Light()
                {
                    Color = new Vector3(Color.CadetBlue)
                }).Transform.Translation = new Vector3(49, 0, 49);
                //create a renderer
                using (var renderer = Renderer.CreateRenderer())
                {
                    //Create a cube map render target with depth texture, depth is required when rendering a scene.
                    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
                    //create a 2D texture render target with no depth texture used for image processing
                    IRenderTexture final = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(false, 32, 0, 0), 1024 * 3, 1024);

                    //a viewport is required on the render target
                    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
                    renderer.Render(rt);

                    //execute the equirectangular projection post-processing with the previous rendered cube map as input
                    PostProcessing equirectangular = renderer.GetPostProcessing("equirectangular");
                    //Specify the cube map rendered from the scene as this post processing's input
                    equirectangular.Input = rt.Targets[0];
                    //Execute the post processing effect and save the result to render target final
                    renderer.Execute(equirectangular, final);
                    //save the texture into disk
                    ((ITexture2D)final.Targets[0]).Save("Your Output Directory"+"panaroma.png", ImageFormat.Png);
                }
                // ExEnd:RenderPanaromaViewof3DScene

            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
    }
}

```
