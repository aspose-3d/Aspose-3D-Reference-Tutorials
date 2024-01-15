---
title: Compress 3D Meshes with Google Draco in Java
linktitle: Compress 3D Meshes with Google Draco in Java
second_title: Aspose.3D Java API
description: 
type: docs
weight: 10
url: /java/3d-mesh-data/compress-meshes-google-draco/
---

## Complete Source Code
```java
package examples.objects;

import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Sphere;


import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Encode3DMeshinGoogleDraco {

        public static void run() throws IOException {
            // ExStart:Encode3DMeshinGoogleDraco
            // The path to the documents directory.
            String MyDir = "Your Document Directory";

            // Create a sphere
            Sphere sphere = new Sphere();
            // Encode the sphere to Google Draco raw data using optimal compression level.
            DracoSaveOptions opt = new DracoSaveOptions();
            opt.setCompressionLevel(DracoCompressionLevel.OPTIMAL);
            byte[] b = FileFormat.DRACO.encode(sphere.toMesh(), opt);
            // Save the raw bytes to file
            Files.write(Paths.get(MyDir, "SphereMeshtoDRC_Out.drc"), b);
            // ExEnd:Encode3DMeshinGoogleDraco
        }
}

```
