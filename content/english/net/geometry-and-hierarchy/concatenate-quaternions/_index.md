---
title: Concatenating Quaternions in 3D Scenes
linktitle: Concatenating Quaternions in 3D Scenes
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 11
url: /net/geometry-and-hierarchy/concatenate-quaternions/
---

## Complete Source Code
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;

namespace Aspose._3D.Examples.CSharp.Geometry_Hierarchy
{
    class ConcatenateQuaternions 
    {
        public static void Run()
        {
            // ExStart:ConcatenateQuaternions     

            Scene scene = new Scene();

            Quaternion q1 = Quaternion.FromEulerAngle(Math.PI * 0.5, 0, 0);
            Quaternion q2 = Quaternion.FromAngleAxis(-Math.PI * 0.5, Vector3.XAxis);
            // Concatenate q1 and q2. q1 and q2 rotate alone x-axis with same angle but different direction,
            // So the concatenated result will be identity quaternion.
            Quaternion q3 = q1.Concat(q2);

            // Create 3 cylinders to represent each quaternion
            Node cylinder = scene.RootNode.CreateChildNode("cylinder-q1", new Cylinder(0.1, 1, 2));
            cylinder.Transform.Rotation = q1;
            cylinder.Transform.Translation = new Vector3(-5, 2, 0);

            cylinder = scene.RootNode.CreateChildNode("cylinder-q2", new Cylinder(0.1, 1, 2));
            cylinder.Transform.Rotation = q2;
            cylinder.Transform.Translation = new Vector3(0, 2, 0);

            cylinder = scene.RootNode.CreateChildNode("cylinder-q3", new Cylinder(0.1, 1, 2));
            cylinder.Transform.Rotation = q3;
            cylinder.Transform.Translation = new Vector3(5, 2, 0);
            var output = "Your Output Directory"+"test_out.fbx";
            // Save to file
            scene.Save(output, FileFormat.FBX7400ASCII);
            // ExEnd:ConcatenateQuaternions

            Console.WriteLine("\nQuaternions concatenated successfully.\nFile saved at " + output);

        }
    }
}

```
