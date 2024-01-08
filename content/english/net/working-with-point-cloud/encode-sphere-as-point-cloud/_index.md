---
title: Encoding Sphere as Point Cloud
linktitle: Encoding Sphere as Point Cloud
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 14
url: /net/working-with-point-cloud/encode-sphere-as-point-cloud/
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
    public class EncodeSphereAsPointCloud
    {
        public static void Run()
        {
            // ExStart:1
            FileFormat.Draco.Encode(new Sphere(), "Your Document Directory" + "sphere.drc", new DracoSaveOptions() { PointCloud = true });
            // ExEnd:1              
        }
    }
}

```
