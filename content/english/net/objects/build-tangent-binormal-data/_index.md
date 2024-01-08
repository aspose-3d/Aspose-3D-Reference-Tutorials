---
title: Building Tangent and Binormal Data
linktitle: Building Tangent and Binormal Data
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 10
url: /net/objects/build-tangent-binormal-data/
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
    class BuildTangentAndBinormalData
    {
        public static void Run()
        {
            // ExStart:BuildTangentAndBinormalData
            // Load an existing 3D file
            Scene scene = new Scene(RunExamples.GetDataFilePath("document.fbx"));
            // Triangulate a scene
            PolygonModifier.BuildTangentBinormal(scene);
            // Save 3D scene
            scene.Save(RunExamples.GetOutputFilePath("BuildTangentAndBinormalData_out.fbx"), FileFormat.FBX7400ASCII);
            // ExEnd:BuildTangentAndBinormalData              
        }
    }
}

```
