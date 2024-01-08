---
title: Encoding 3D Mesh in Google Draco Format
linktitle: Encoding 3D Mesh in Google Draco Format
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 19
url: /net/objects/encode-3d-mesh-google-draco/
---

## Complete Source Code
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace Aspose._3D.Examples.CSharp.Working_with_Objects
{
    class Encode3DMeshinGoogleDraco
    {
        public static void Run()
        {
            // ExStart:Encode3DMeshinGoogleDraco
            
            // Create a sphere
            var sphere = new Sphere();
            // Encode the sphere to Google Draco raw data using optimal compression level.
            var b = FileFormat.Draco.Encode(sphere.ToMesh(), 
                new DracoSaveOptions() { CompressionLevel = DracoCompressionLevel.Optimal });
            // Save the raw bytes to file
            File.WriteAllBytes("Your Output Directory"+"SphereMeshtoDRC_Out.drc", b);
            // ExEnd:Encode3DMeshinGoogleDraco              
        }
    }
}

```
