---
title: Converting Box Mesh to Triangle Mesh with Custom Memory Layout
linktitle: Converting Box Mesh to Triangle Mesh with Custom Memory Layout
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 11
url: /net/objects/convert-box-mesh-triangle-memory-layout/
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
using Aspose.ThreeD.Utilities;
using System.Runtime.InteropServices;

namespace Aspose._3D.Examples.CSharp._Working_with_Objects
{
    class ConvertBoxMeshtoTriangleMeshCustomMemoryLayout
    {
        public static void Run()
        {
            // Initialize scene object
            Scene scene = new Scene();

            // Initialize Node class object
            Node cubeNode = new Node("box");

            // ExStart:ConvertBoxMeshtoTriangleMeshCustomMemoryLayout
            // Get mesh of the Box
            Mesh box = (new Box()).ToMesh();
            // Create a customized vertex layout
            VertexDeclaration vd = new VertexDeclaration();
            VertexField position = vd.AddField(VertexFieldDataType.FVector4, VertexFieldSemantic.Position);
            vd.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Normal);
            // Get a triangle mesh
            TriMesh triMesh = TriMesh.FromMesh(box);
            // ExEnd:ConvertBoxMeshtoTriangleMeshCustomMemoryLayout

            // Point node to the Mesh geometry
            cubeNode.Entity = box;

            // Add Node to a scene
            scene.RootNode.ChildNodes.Add(cubeNode);

            // The path to the documents directory.
            string output = "Your Output Directory"+"BoxToTriangleMeshCustomMemoryLayoutScene.fbx";

            // Save 3D scene in the supported file formats
            scene.Save(output, FileFormat.FBX7400ASCII);

            Console.WriteLine("\n Converted a Box mesh to triangle mesh with custom memory layout of the vertex successfully.\nFile saved at " + output);
        }
    }
}

```
