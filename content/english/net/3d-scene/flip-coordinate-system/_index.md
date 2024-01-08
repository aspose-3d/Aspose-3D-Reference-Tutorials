---
title: Flipping Coordinate System in 3D Scenes
linktitle: Flipping Coordinate System in 3D Scenes
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 12
url: /net/3d-scene/flip-coordinate-system/
---

## Complete Source Code
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;

namespace Aspose._3D.Examples.CSharp._3DScene
{
    class FlipCoordinateSystem
    {
        public static void Run()
        {
            // ExStart:FlipCoordinateSystem
            // The path to the input file
            string input = RunExamples.GetDataFilePath("camera.3ds");            
            // Initialize scene object
            Scene scene = new Scene();
            scene.Open(input, FileFormat.Discreet3DS);
            var output = RunExamples.GetOutputFilePath( "FlipCoordinateSystem.obj");
            scene.Save(output, FileFormat.WavefrontOBJ);
            // ExEnd:FlipCoordinateSystem
            Console.WriteLine("\nCoordinate system has been flipped successfully.\nFile saved at " + output);
        }
    }
}

```
