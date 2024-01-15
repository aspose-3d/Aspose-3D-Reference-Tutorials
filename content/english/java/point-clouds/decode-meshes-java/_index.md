---
title: Decode Meshes Efficiently with Aspose.3D for Java
linktitle: Decode Meshes Efficiently with Aspose.3D for Java
second_title: Aspose.3D Java API
description: 
type: docs
weight: 10
url: /java/point-clouds/decode-meshes-java/
---

## Complete Source Code
```java
package examples.pointcloud;

import com.aspose.threed.FileFormat;
import com.aspose.threed.PointCloud;
import examples.RunExamples;

import java.io.IOException;

public class DecodeMesh {
    public static void run() throws IOException {
        // ExStart:1
        PointCloud pointCloud = (PointCloud) FileFormat.DRACO.decode(RunExamples.getDataDir() + "point_cloud_no_qp.drc");
        // ExEnd:1
    }
}

```
