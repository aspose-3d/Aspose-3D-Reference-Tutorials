---
title: Encoding Mesh
linktitle: Encoding Mesh
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 12
url: /net/working-with-point-cloud/encode-mesh/
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
    public class EncodeMesh
    {
        public static void Run()
        {
            // ExStart:1
            FileFormat.Draco.Encode(new Sphere(), "Your Document Directory" + "sphere.drc");
            // ExEnd:1              
        }
    }
}

```
