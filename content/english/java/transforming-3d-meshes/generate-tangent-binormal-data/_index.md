---
title: Generate Tangent and Binormal Data for 3D Meshes in Java
linktitle: Generate Tangent and Binormal Data for 3D Meshes in Java
second_title: Aspose.3D Java API
description: 
type: docs
weight: 11
url: /java/transforming-3d-meshes/generate-tangent-binormal-data/
---

## Complete Source Code
```java
package examples.objects;

import com.aspose.threed.FileFormat;
import com.aspose.threed.PolygonModifier;
import com.aspose.threed.Scene;
import examples.RunExamples;

import java.io.IOException;

public class BuildTangentAndBinormalData {

        public static void run() throws Exception {
            // ExStart:BuildTangentAndBinormalData
            // The path to the documents directory.
            String MyDir = RunExamples.getDataDir();

            // Load an existing 3D file
            Scene scene = new Scene( MyDir + "document.fbx");
            // Triangulate a scene
            PolygonModifier.buildTangentBinormal(scene);
            // Save 3D scene
            scene.save("BuildTangentAndBinormalData_out.fbx", FileFormat.FBX7400ASCII);
            // ExEnd:BuildTangentAndBinormalData
        }
}

```
