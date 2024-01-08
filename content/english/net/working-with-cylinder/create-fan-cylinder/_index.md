---
title: Creating Fan Cylinder
linktitle: Creating Fan Cylinder
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 10
url: /net/working-with-cylinder/create-fan-cylinder/
---

## Complete Source Code
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Aspose._3D.Examples.CSharp.WorkingWithCylinder
{
    public class CreateFanCylinder
    {
        public static void Run()
        {
            // ExStart:1
            // Create a Scene
            Scene scene = new Scene();
            // Create a cylinder
            var fan = new Cylinder(2, 2, 10, 20, 1, false);
            // Set GenerateGanCylinder to true
            fan.GenerateFanCylinder = true;
            // Set ThetaLength
            fan.ThetaLength = MathUtils.ToRadian(270);
            // Create ChildNode
            scene.RootNode.CreateChildNode(fan).Transform.Translation = new Vector3(10, 0, 0);
            // Create a cylinder without a fan
            var nonfan = new Cylinder(2, 2, 10, 20, 1, false);
            // Set GenerateGanCylinder to false
            nonfan.GenerateFanCylinder = false;
            // Set ThetaLengeth 
            nonfan.ThetaLength = MathUtils.ToRadian(270);
            // Create ChildNode
            scene.RootNode.CreateChildNode(nonfan);
            // Save scene
            scene.Save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WavefrontOBJ);
            // ExEnd:1              
        }
    }
}

```
