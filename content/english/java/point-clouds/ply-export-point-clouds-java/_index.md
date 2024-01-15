---
title: Streamline Point Cloud Handling with PLY Export in Java
linktitle: Streamline Point Cloud Handling with PLY Export in Java
second_title: Aspose.3D Java API
description: 
type: docs
weight: 16
url: /java/point-clouds/ply-export-point-clouds-java/
---

## Complete Source Code
```java
package examples.pointcloud;

import com.aspose.threed.FileFormat;
import com.aspose.threed.PlySaveOptions;
import com.aspose.threed.Sphere;


import java.io.IOException;

public class ExportToPlyAsPointCloud {
    public static void run() throws IOException {
        // ExStart:1
        PlySaveOptions opt = new PlySaveOptions();
        opt.setPointCloud(true);
        FileFormat.PLY.encode(new Sphere(),"Your Document Directory" + "sphere.ply", opt);
        // ExEnd:1
    }
}

```
