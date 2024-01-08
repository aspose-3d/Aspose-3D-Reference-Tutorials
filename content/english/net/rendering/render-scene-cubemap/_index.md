---
title: Rendering -  Rendering Scene into Cubemap with Six Faces
linktitle: Rendering -  Rendering Scene into Cubemap with Six Faces
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 14
url: /net/rendering/render-scene-cubemap/
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
    class RenderSceneIntoCubemapwithsixfaces
    {
        public static void Run()
        {
            try
            {
                // ExStart:RenderSceneIntoCubemapwithsixfaces
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
                    //create a cube map render target with depth texture, depth is required when rendering a scene.
                    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
                    //a viewport is required on the render target
                    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
                    renderer.Render(rt);
                    //now lets get the cubemap texture
                    ITextureCubemap cubemap = rt.Targets[0] as ITextureCubemap;
                    //we can directly save each face to disk by specifing the file name
                    CubeFaceData<string> fileNames = new CubeFaceData<string>()
                    {
                        Right = "Your Output Directory"+"right.png",
                        Left = "Your Output Directory"+"left.png",
                        Back = "Your Output Directory"+"back.png",
                        Front = "Your Output Directory"+"front.png",
                        Bottom = "Your Output Directory"+"bottom.png",
                        Top = "Your Output Directory"+"top.png"
                    };
                    //and call Save method
                    cubemap.Save(fileNames, ImageFormat.Png);
                    //or we just need to use the render result in memory, we can save it to CubeFaceData<Bitmap>
                    //CubeFaceData<Bitmap> bitmaps = new CubeFaceData<Bitmap>();
                    //cubemap.Save(bitmaps);
                    //bitmaps.Back.Save("back.bmp", ImageFormat.Bmp);
                }
                // ExEnd:RenderSceneIntoCubemapwithsixfaces

            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
    }
}

```
