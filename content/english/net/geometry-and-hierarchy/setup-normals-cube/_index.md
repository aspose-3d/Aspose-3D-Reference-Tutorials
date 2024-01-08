---
title: Setting Up Normals on Cube in 3D Scenes
linktitle: Setting Up Normals on Cube in 3D Scenes
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 17
url: /net/geometry-and-hierarchy/setup-normals-cube/
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
    class SetupNormalsOnCube
    {
        public static void Run()
        {
            // ExStart:SetupNormalsOnCube
            // Raw normal data
            Vector4[] normals = new Vector4[]
            {
                new Vector4(-0.577350258,-0.577350258, 0.577350258, 1.0),
                new Vector4( 0.577350258,-0.577350258, 0.577350258, 1.0),
                new Vector4( 0.577350258, 0.577350258, 0.577350258, 1.0),
                new Vector4(-0.577350258, 0.577350258, 0.577350258, 1.0),
                new Vector4(-0.577350258,-0.577350258,-0.577350258, 1.0),
                new Vector4( 0.577350258,-0.577350258,-0.577350258, 1.0),
                new Vector4( 0.577350258, 0.577350258,-0.577350258, 1.0),
                new Vector4(-0.577350258, 0.577350258,-0.577350258, 1.0)
            };

            // Call Common class create mesh using polygon builder method to set mesh instance 
            Mesh mesh = Common.CreateMeshUsingPolygonBuilder(); 

            VertexElementNormal elementNormal = mesh.CreateElement(VertexElementType.Normal, MappingMode.ControlPoint, ReferenceMode.Direct) as VertexElementNormal;
            // Copy the data to the vertex element
            elementNormal.Data.AddRange(normals);
            // ExEnd:SetupNormalsOnCube

            Console.WriteLine("\nNormals has been setup successfully on cube.");
        }
    }
}

```
