---
title: Exporting 3D Scene as Point Cloud
linktitle: Exporting 3D Scene as Point Cloud
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 15
url: /net/working-with-point-cloud/export-3d-scene-point-cloud/
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
    public class Export3DSceneAsPointCloud
    {
        /// <summary>
        /// Gets or sets the flag whether the exporter should export the scene as point cloud(without topological structure), default value is false
        /// This method is supported by version 19.8 or greater.
        /// </summary>
        public static void Run()
        {
            // ExStart:1
            var scene = new Scene(new Sphere());
            scene.Save(RunExamples.GetDataDir() + "Export3DSceneAsPointCloud.obj", new ObjSaveOptions() { PointCloud = true });
            // ExEnd:1              
        }
    }
}

```
