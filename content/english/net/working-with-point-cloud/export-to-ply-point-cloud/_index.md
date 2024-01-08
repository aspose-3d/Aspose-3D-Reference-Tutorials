---
title: Exporting to PLY Format as Point Cloud
linktitle: Exporting to PLY Format as Point Cloud
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 16
url: /net/working-with-point-cloud/export-to-ply-point-cloud/
---

## Complete Source Code
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Aspose._3D.Examples.CSharp.WorkingWithPointCloud
{
    public class ExportToPlyAsPointCloud
    {
        public static void Run()
        {
            // ExStart:1
            FileFormat.PLY.Encode(new Sphere(), RunExamples.GetDataDir() + "sphere.ply", new PlySaveOptions() { PointCloud = true });

            // ExEnd:1              
        }
    }
}

```
