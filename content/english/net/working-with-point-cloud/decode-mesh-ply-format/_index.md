---
title: Decoding Mesh from PLY Format
linktitle: Decoding Mesh from PLY Format
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 11
url: /net/working-with-point-cloud/decode-mesh-ply-format/
---

## Complete Source Code
```csharp
using Aspose.ThreeD;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Aspose._3D.Examples.CSharp.WorkingWithPointCloud
{
    public class DecodeMeshToPly
    {
        public static void Run()
        {
            // ExStart:1
            var geom = FileFormat.PLY.Decode("Your Document Directory" + "sphere.ply");
            // ExEnd:1              
        }
    }
}

```
