---
title: Load PLY Point Clouds Seamlessly in Java
linktitle: Load PLY Point Clouds Seamlessly in Java
second_title: Aspose.3D Java API
description: 
type: docs
weight: 11
url: /java/point-clouds/load-ply-point-clouds-java/
---

## Complete Source Code
```java
package examples.pointcloud;

import com.aspose.threed.FileFormat;
import com.aspose.threed.Geometry;
import com.aspose.threed.Sphere;


import java.io.IOException;

public class DecodeMeshFromPly {
    public static void run() throws IOException {
        // ExStart:1
        Geometry geom = FileFormat.PLY.decode("Your Document Directory" + "sphere.ply");
        // ExEnd:1
    }
}

```
