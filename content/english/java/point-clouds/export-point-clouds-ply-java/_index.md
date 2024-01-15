---
title: Export Point Clouds to PLY Format with Aspose.3D for Java
linktitle: Export Point Clouds to PLY Format with Aspose.3D for Java
second_title: Aspose.3D Java API
description: 
type: docs
weight: 13
url: /java/point-clouds/export-point-clouds-ply-java/
---

## Complete Source Code
```java
package examples.pointcloud;

import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Sphere;


import java.io.IOException;

public class EncodeMeshToPly {
    public static void run() throws IOException {
        // ExStart:1
        FileFormat.PLY.encode(new Sphere(), "Your Document Directory" + "sphere.ply");
        // ExEnd:1
    }
}


```
