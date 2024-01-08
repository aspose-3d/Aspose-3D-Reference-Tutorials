---
title: Encoding Mesh to PLY Format
linktitle: Encoding Mesh to PLY Format
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 13
url: /net/working-with-point-cloud/encode-mesh-ply-format/
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
    class EncodeMeshToPly
    {
        public static void Run()
        {
            // ExStart:1
            FileFormat.PLY.Encode(new Sphere(), "sphere.ply");
            // ExEnd:1              
        }
    }
}

```
