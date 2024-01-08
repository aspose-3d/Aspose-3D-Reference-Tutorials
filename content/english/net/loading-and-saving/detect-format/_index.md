---
title: Loading and Saving -  Detecting Format
linktitle: Loading and Saving -  Detecting Format
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 12
url: /net/loading-and-saving/detect-format/
---

## Complete Source Code
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;

namespace Aspose._3D.Examples.CSharp.Loading_Saving
{
    class DetectFormat
    {
        public static void Run()
        {
            // ExStart:DetectFormat
            // Detect the format of a 3D file
            FileFormat inputFormat = FileFormat.Detect(RunExamples.GetDataFilePath("document.fbx"));
            // Display the file format
            Console.WriteLine("File Format: " + inputFormat.ToString());
            // ExEnd:DetectFormat            
        }
    }
}

```
