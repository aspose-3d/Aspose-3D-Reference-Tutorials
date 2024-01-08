---
title: Opening VRML File
linktitle: Opening VRML File
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 10
url: /net/working-with-vrml/opening-vrml-file/
---

## Complete Source Code
```csharp
using Aspose.ThreeD;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Aspose._3D.Examples.CSharp.WorkingWithVRML
{
    public class OpenVRML
    {
        public static void Run()
        {
            // ExStart:OpenVRML
            // Create a Scene
            Scene scene = new Scene();
            // Open Virtual Reality Modeling Language (VRML) file format
            scene.Open(RunExamples.GetDataDir() + "test.wrl");
            // Work with VRML file format...

            // ExEnd:OpenVRML              
        }
    }
}

```
