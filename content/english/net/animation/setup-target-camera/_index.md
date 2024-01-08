---
title: Setting Up Targets and Cameras for Animation in 3D Scenes
linktitle: Setting Up Targets and Cameras for Animation in 3D Scenes
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 11
url: /net/animation/setup-target-camera/
---

## Complete Source Code
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;

namespace Aspose._3D.Examples.CSharp.Animation
{
    class SetupTargetAndCamera
    {
        public static void Run()
        {
            // ExStart:SetupTargetAndCamera
            // Initialize scene object
            Scene scene = new Scene();
            // Get a child node object
            Node cameraNode = scene.RootNode.CreateChildNode("camera", new Camera());
            // Set camera node translation
            cameraNode.Transform.Translation = new Vector3(100, 20, 0);
            cameraNode.GetEntity<Camera>().Target = scene.RootNode.CreateChildNode("target");
            var output = RunExamples.GetOutputFilePath("camera-test.3ds");
            scene.Save(output, FileFormat.Discreet3DS);
            // ExEnd:SetupTargetAndCamera
            Console.WriteLine("\nThe target and camera has been setup successfully.\nFile saved at " + output);
        }
    }
}

```
