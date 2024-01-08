---
title: Loading and Saving -  Saving 3D in PDF
linktitle: Loading and Saving -  Saving 3D in PDF
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 19
url: /net/loading-and-saving/save-3d-in-pdf/
---

## Complete Source Code
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Formats;
using System.Drawing;

namespace Aspose._3D.Examples.CSharp.Loading_Saving
{
    class Save3DInPdf
    {
        public static void Run()
        {
            // ExStart:Save3DInPdf

            // Create a new scene
            Scene scene = new Scene();
            // Create a cylinder child node
            scene.RootNode.CreateChildNode("cylinder", new Cylinder()).Material = new PhongMaterial() { DiffuseColor = new Vector3(Color.DarkCyan) };
            // Set rendering mode and lighting scheme
            PdfSaveOptions opt = new PdfSaveOptions();
            opt.LightingScheme = PdfLightingScheme.CAD;
            opt.RenderMode = PdfRenderMode.ShadedIllustration;
            // Save in the PDF format
            scene.Save(RunExamples.GetOutputFilePath("output_out.pdf"), opt);
            // ExEnd:Save3DInPdf           
        }
    }
}

```
