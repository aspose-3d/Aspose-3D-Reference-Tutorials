---
title: Decoding Mesh
linktitle: Decoding Mesh
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 10
url: /net/working-with-point-cloud/decode-mesh/
---

## Complete Source Code
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Aspose._3D.Examples.CSharp.WorkingWithPointCloud
{
    public class DecodeMesh
    {
        public static void Run()
        {
            // ExStart:1
            var pointCloud = (PointCloud)FileFormat.Draco.Decode(RunExamples.GetDataDir() + "point_cloud_no_qp.drc");
            // ExEnd:1              
        }
    }
}

```
