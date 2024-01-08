---
title: Loading and Saving -  Creating an Empty 3D Document
linktitle: Loading and Saving -  Creating an Empty 3D Document
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 11
url: /net/loading-and-saving/create-empty-3d-document/
---

## Complete Source Code
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
namespace Aspose._3D.Examples.CSharp.Loading_Saving
{
    class CreateEmpty3DDocument
    {
        public static void Run()
        {
            // ExStart:CreateEmpty3DDocument
            // The path to the documents directory.
            var output = "Your Output Directory"+"document.fbx";

            // Create an object of the Scene class
            Scene scene = new Scene();
            // Save 3D scene document
            scene.Save(output, FileFormat.FBX7500ASCII);
            // ExEnd:CreateEmpty3DDocument

            Console.WriteLine("\nAn empty 3D document created successfully.\nFile saved at " + output);
        }
    }
}

```
