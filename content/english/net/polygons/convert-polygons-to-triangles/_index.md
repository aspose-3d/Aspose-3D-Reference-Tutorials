---
title: Polygons -  Converting Polygons to Triangles
linktitle: Polygons -  Converting Polygons to Triangles
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 10
url: /net/polygons/convert-polygons-to-triangles/
---

## Complete Source Code
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;

namespace Aspose._3D.Examples.CSharp.Polygons
{
    class ConvertPolygonsToTriangles
    {
        public static void Run()
        {
            // ExStart:ConvertPolygonsToTriangles
            // Load an existing 3D file
            Scene scene = new Scene(RunExamples.GetDataFilePath("document.fbx"));
            // Triangulate a scene
            PolygonModifier.Triangulate(scene);
            // Save 3D scene
            scene.Save("Your Output Directory"+"triangulated_out.fbx", FileFormat.FBX7400ASCII);
            // ExEnd:ConvertPolygonsToTriangles            
        }
    }
}

```
