---
title: Applying PBR Material to Box in 3D Scenes
linktitle: Applying PBR Material to Box in 3D Scenes
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 10
url: /net/geometry-and-hierarchy/apply-pbr-material-to-box/
---

## Complete Source Code
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Aspose._3D.Examples.CSharp.Geometry_and_Hierarchy
{
    class ApplyPBRMaterialToBox
    {
        public static void Run()
        {
            // ExStart:ApplyPBRMaterialToBox
            // initialize a scene
            Scene scene = new Scene();
            // initialize PBR material object
            PbrMaterial mat = new PbrMaterial();
            // an almost metal material
            mat.MetallicFactor = 0.9;
            // material surface is very rough
            mat.RoughnessFactor = 0.9;
            // create a box to which the material will be applied
            var boxNode = scene.RootNode.CreateChildNode("box", new Box());
            boxNode.Material = mat;
            // save 3d scene into STL format
            scene.Save("Your Output Directory"+"PBR_Material_Box_Out.stl", FileFormat.STLASCII);
            // ExEnd:ApplyPBRMaterialToBox  
        }
    }
}

```
