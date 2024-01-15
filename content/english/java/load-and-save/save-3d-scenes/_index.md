---
title: Save 3D Scenes in Various Formats with Aspose.3D for Java
linktitle: Save 3D Scenes in Various Formats with Aspose.3D for Java
second_title: Aspose.3D Java API
description: 
type: docs
weight: 15
url: /java/load-and-save/save-3d-scenes/
---

## Complete Source Code
```java
package examples.loadsave;

import com.aspose.threed.*;
import com.aspose.threed.utils.MemoryStream;
import examples.RunExamples;

public class Save3DScene {

        public static void run() throws Exception {
            // ExStart:Save3DScene
            // The path to the documents directory.
            String MyDir = RunExamples.getDataDir();

            // Load a 3D document into Aspose.3D
            Scene scene = new Scene();

            // Open an existing 3D scene
            scene.open(MyDir + "document.fbx");

            // Save Scene to a stream
            try (MemoryStream dstStream = new MemoryStream()) {
                scene.save(dstStream, FileFormat.FBX7500ASCII);
            }
            // Save Scene to a local path
            scene.save(MyDir + "output_out.fbx", FileFormat.FBX7500ASCII);
            // ExEnd:Save3DScene

            System.out.println("\nConverted 3D document to stream successfully.");
        }
}

```
