---
title: Loading and Saving -  Extracting Raw 3D Contents from PDF
linktitle: Loading and Saving -  Extracting Raw 3D Contents from PDF
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 14
url: /net/loading-and-saving/extract-raw-3d-contents-pdf/
---

## Complete Source Code
```csharp
using System;
using System.IO;
using System.Text;
using System.Collections.Generic;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;

namespace Aspose._3D.Examples.CSharp.Loading_Saving
{
    class ExtractRaw3DContentsFromPdf
    {
        public static void Run()
        {
            // ExStart:ExtractRaw3DContentsFromPdf
            // The path to the documents directory.
            byte[] password = null;
            // Extract 3D contents
            List<byte[]> contents = FileFormat.PDF.Extract(RunExamples.GetDataFilePath("House_Design.pdf"), password);
            int i = 1;
            // Iterate through the contents and in separate 3D files
            foreach (byte[] content in contents)
            {
                string fileName = "3d-" + (i++);
                File.WriteAllBytes(fileName, content);
            }
            // ExEnd:ExtractRaw3DContentsFromPdf            
        }
    }
}

```
