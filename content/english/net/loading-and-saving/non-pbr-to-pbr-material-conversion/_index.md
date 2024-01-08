---
title: Loading and Saving -  Non-PBR to PBR Material Conversion
linktitle: Loading and Saving -  Non-PBR to PBR Material Conversion
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 16
url: /net/loading-and-saving/non-pbr-to-pbr-material-conversion/
---

## Complete Source Code
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Aspose._3D.Examples.CSharp.Loading_and_Saving
{
    class Non_PBRtoPBRMaterial
    {
        public static void Run()
        {
            // ExStart:Non_PBRtoPBRMaterial
            // initialize a new 3D scene
            var s = new Scene();
            var box = new Box();
            s.RootNode.CreateChildNode("box1", box).Material = new PhongMaterial() { DiffuseColor = new Vector3(1, 0, 1) };
            GltfSaveOptions opt = new GltfSaveOptions(FileFormat.GLTF2);
            //Custom material converter to convert PhongMaterial to PbrMaterial
            opt.MaterialConverter = delegate (Material material)
            {
                PhongMaterial m = (PhongMaterial)material;
                return new PbrMaterial() { Albedo = new Vector3(m.DiffuseColor.x, m.DiffuseColor.y, m.DiffuseColor.z) };
            };
            // save in GLTF 2.0 format
            s.Save("Your Output Directory"+"Non_PBRtoPBRMaterial_Out.gltf", opt);
            // ExEnd:Non_PBRtoPBRMaterial
        }
    }
}

```
