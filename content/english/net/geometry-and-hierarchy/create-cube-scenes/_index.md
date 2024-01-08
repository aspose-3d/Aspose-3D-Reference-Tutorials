---
title: Creating Cube Scenes in 3D
linktitle: Creating Cube Scenes in 3D
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 12
url: /net/geometry-and-hierarchy/create-cube-scenes/
---

## Complete Source Code
```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;

namespace Aspose._3D.Examples.CSharp.Geometry_Hierarchy
{
    class CubeScene
    {
        public static void Run()
        {
            // ExStart:CreateCubeScene           
            // Initialize scene object
            Scene scene = new Scene();
            
            // Initialize Node class object
            Node cubeNode = new Node("cube");

            // Call Common class create mesh using polygon builder method to set mesh instance 
            Mesh mesh = Common.CreateMeshUsingPolygonBuilder();           

            // Point node to the Mesh geometry
            cubeNode.Entity = mesh;
            
            // Add Node to a scene
            scene.RootNode.ChildNodes.Add(cubeNode);           
            
            // The path to the documents directory.
            var output = "Your Output Directory"+"CubeScene.fbx";          

            // Save 3D scene in the supported file formats
            scene.Save(output, FileFormat.FBX7400ASCII);           
            // ExEnd:CreateCubeScene

            Console.WriteLine("\nCube Scene created successfully.\nFile saved at " + output);

        }
    }
}

```
