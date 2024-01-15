---
title: Convert Polygons to Triangles for Efficient Rendering in Java 3D
linktitle: Convert Polygons to Triangles for Efficient Rendering in Java 3D
second_title: Aspose.3D Java API
description: 
type: docs
weight: 10
url: /java/polygon/convert-polygons-triangles/
---

## Complete Source Code
```java
package examples.polygons;

import com.aspose.threed.FileFormat;
import com.aspose.threed.PolygonModifier;
import com.aspose.threed.Scene;


import java.io.IOException;

public class ConvertPolygonsToTriangles {

        public static void run() throws Exception {
            // ExStart:ConvertPolygonsToTriangles
            // The path to the documents directory.
            String MyDir = "Your Document Directory";
            // Load an existing 3D file
            Scene scene = new Scene(MyDir + "document.fbx");
            // Triangulate a scene
            PolygonModifier.triangulate(scene);
            // Save 3D scene
            scene.save(MyDir + "triangulated_out.fbx", FileFormat.FBX7400ASCII);
            // ExEnd:ConvertPolygonsToTriangles
        }
}

```
