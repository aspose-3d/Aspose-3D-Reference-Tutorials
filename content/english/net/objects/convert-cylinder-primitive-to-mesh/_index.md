---
title: Converting Cylinder Primitive to Mesh
linktitle: Converting Cylinder Primitive to Mesh
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 13
url: /net/objects/convert-cylinder-primitive-to-mesh/
---

## Complete Source Code
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;

namespace Aspose._3D.Examples.CSharp._Working_with_Objects
{
    class ConvertCylinderPrimitivetoMesh
    {
        public static void Run()
        {
            // Initialize scene object
            Scene scene = new Scene();
            
            // Initialize Node class object
            Node cubeNode = new Node("cylinder");

            // ExStart:ConvertCylinderPrimitivetoMesh
            // Initialize object by Cylinder class
            IMeshConvertible convertible = new Cylinder();
            
            // Convert a Cylinder to Mesh
            Mesh mesh = convertible.ToMesh();
            // ExEnd:ConvertCylinderPrimitivetoMesh

            // Point node to the Mesh geometry
            cubeNode.Entity = mesh;

            // Add Node to a scene
            scene.RootNode.ChildNodes.Add(cubeNode);

            // The path to the documents directory.
            string output = RunExamples.GetOutputFilePath("CylinderToMeshScene.fbx");

            // Save 3D scene in the supported file formats
            scene.Save(output, FileFormat.FBX7400ASCII);

            Console.WriteLine("\n Converted the primitive Cylinder to a mesh successfully.\nFile saved at " + output);
        }
    }
}

```
