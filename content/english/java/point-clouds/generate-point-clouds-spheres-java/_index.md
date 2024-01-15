---
title: Generating Point Clouds from Spheres in Java
linktitle: Generating Point Clouds from Spheres in Java
second_title: Aspose.3D Java API
description: 
type: docs
weight: 14
url: /java/point-clouds/generate-point-clouds-spheres-java/
---

## Complete Source Code
```java
package examples.pointcloud;

import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Sphere;
import examples.RunExamples;

import java.io.IOException;

public class EncodeSphereAsPointCloud {
    public static void run() throws IOException {
        // ExStart:1
        DracoSaveOptions opt = new DracoSaveOptions();
        opt.setPointCloud(true);
        FileFormat.DRACO.encode(new Sphere(), RunExamples.getDataDir()+"sphere.drc", opt);
        // ExEnd:1
    }
}

```
