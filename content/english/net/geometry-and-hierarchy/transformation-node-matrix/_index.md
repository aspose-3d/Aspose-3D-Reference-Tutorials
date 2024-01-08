---
title: Transforming Node by Transformation Matrix in 3D Scenes
linktitle: Transforming Node by Transformation Matrix in 3D Scenes
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 21
url: /net/geometry-and-hierarchy/transformation-node-matrix/
---

## Complete Source Code
```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
namespace Aspose._3D.Examples.CSharp.Geometry_Hierarchy
{
    class TransformationToNodeByTransformationMatrix
    {
        public static void Run()
        {
            // ExStart:AddTransformationToNodeByTransformationMatrix            
            // Initialize scene object
            Scene scene = new Scene();

            // Initialize Node class object
            Node cubeNode = new Node("cube");

            // Call Common class create mesh using polygon builder method to set mesh instance 
            Mesh mesh = Common.CreateMeshUsingPolygonBuilder(); 
           
            // Point node to the Mesh geometry
            cubeNode.Entity = mesh;
            // Set custom translation matrix
            cubeNode.Transform.TransformMatrix = new Matrix4(
            1, -0.3, 0, 0,
            0.4, 1, 0.3, 0,
            0, 0, 1, 0,
            0, 20, 0, 1
            );        
            // Add cube to the scene
            scene.RootNode.ChildNodes.Add(cubeNode);            

            // The path to the documents directory.
            var output = "Your Output Directory"+"TransformationToNode.fbx";
   
            // Save 3D scene in the supported file formats
            scene.Save(output, FileFormat.FBX7500ASCII);
            // ExEnd:AddTransformationToNodeByTransformationMatrix
            Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);

        }
    }
}

```
