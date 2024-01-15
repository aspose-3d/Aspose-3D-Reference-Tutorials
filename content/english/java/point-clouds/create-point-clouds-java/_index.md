---
title: Create Point Clouds from Meshes in Java
linktitle: Create Point Clouds from Meshes in Java
second_title: Aspose.3D Java API
description: 
type: docs
weight: 12
url: /java/point-clouds/create-point-clouds-java/
---

## Complete Source Code
```java
package examples.pointcloud;

import com.aspose.threed.FileFormat;
import com.aspose.threed.Sphere;
import examples.RunExamples;

import java.io.IOException;

public class EncodeMesh {
    public static void run() throws IOException {
        // ExStart:1
        FileFormat.DRACO.encode(new Sphere(), RunExamples.getDataDir() + "sphere.drc");
        // ExEnd:1
    }
}

```
