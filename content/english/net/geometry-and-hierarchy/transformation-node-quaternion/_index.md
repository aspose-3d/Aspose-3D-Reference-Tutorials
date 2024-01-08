---
title: Transforming Node by Quaternion in 3D Scenes
linktitle: Transforming Node by Quaternion in 3D Scenes
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 20
url: /net/geometry-and-hierarchy/transformation-node-quaternion/
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
    class TransformationToNodeByQuaternion
    {
        public static void Run()
        {
            // ExStart:AddTransformationToNodeByQuaternion            
            // Initialize scene object
            Scene scene = new Scene();

            // Initialize Node class object
            Node cubeNode = new Node("cube");

            // Call Common class create mesh using polygon builder method to set mesh instance 
            Mesh mesh = Common.CreateMeshUsingPolygonBuilder(); 
           
            // Point node to the Mesh geometry
            cubeNode.Entity = mesh;
            // Set rotation
            cubeNode.Transform.Rotation = Quaternion.FromRotation(new Vector3(0, 1, 0), new Vector3(0.3, 0.5, 0.1));            
            // Set translation
            cubeNode.Transform.Translation = new Vector3(0, 0, 20);            
            // Add cube to the scene
            scene.RootNode.ChildNodes.Add(cubeNode);            

            // The path to the documents directory.
            var output = RunExamples.GetOutputFilePath("TransformationToNode.fbx");
   
            // Save 3D scene in the supported file formats
            scene.Save(output, FileFormat.FBX7500ASCII);
            // ExEnd:AddTransformationToNodeByQuaternion
            Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);

        }
    }
}

```
