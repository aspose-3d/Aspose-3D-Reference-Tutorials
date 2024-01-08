---
title: Applying Material to Cube in 3D Scenes
linktitle: Applying Material to Cube in 3D Scenes
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 14
url: /net/geometry-and-hierarchy/material-to-cube/
---

## Complete Source Code
```csharp
using System;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose.ThreeD.Shading;
using System.Drawing;
using System.IO;

namespace Aspose._3D.Examples.CSharp.Geometry_Hierarchy
{
    class MaterialToCube
    {
        public static void Run()
        {
            // ExStart:AddMaterialToCube                      
            // Initialize scene object
            Scene scene = new Scene();
            
            // Initialize cube node object
            Node cubeNode = new Node("cube");

            // Call Common class create mesh using polygon builder method to set mesh instance 
            Mesh mesh = Common.CreateMeshUsingPolygonBuilder(); 
         
            // Point node to the mesh
            cubeNode.Entity = mesh;
            
            // Add cube to the scene
            scene.RootNode.ChildNodes.Add(cubeNode);
            
            // Initiallize PhongMaterial object
            PhongMaterial mat = new PhongMaterial();
            
            // Initiallize Texture object
            Texture diffuse = new Texture();
            
            // The path to the documents directory.
            
            // Set local file path
            diffuse.FileName = "Your Output Directory"+"surface.dds";

            // Set Texture of the material
            mat.SetTexture("DiffuseColor", diffuse);

            // Embed raw content data to FBX (only for FBX and optional)
            // Set file name
            diffuse.FileName = "embedded-texture.png";
            // Set binary content
            diffuse.Content = File.ReadAllBytes(RunExamples.GetDataFilePath("aspose-logo.jpg"));

            // Set color
            mat.SpecularColor = new Vector3(Color.Red);

            // Set brightness
            mat.Shininess = 100;

            // Set material property of the cube object
            cubeNode.Material = mat;
            
            var output = "Your Output Directory"+"MaterialToCube.fbx";

            // Save 3D scene in the supported file formats
            scene.Save(output, FileFormat.FBX7400ASCII);
            // ExEnd:AddMaterialToCube

            Console.WriteLine("\nMaterial added successfully to cube.\nFile saved at " + output);

        }
    }
}

```
