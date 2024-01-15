---
title: Export 3D Scenes as Point Clouds with Aspose.3D for Java
linktitle: Export 3D Scenes as Point Clouds with Aspose.3D for Java
second_title: Aspose.3D Java API
description: 
type: docs
weight: 15
url: /java/point-clouds/export-3d-scenes-point-clouds-java/
---

## Complete Source Code
```java
package examples.pointcloud;

import com.aspose.threed.ObjSaveOptions;
import com.aspose.threed.Scene;
import com.aspose.threed.Sphere;
import examples.RunExamples;

import java.io.IOException;

public class Export3DSceneAsPointCloud {
    //This method is supported by version 19.8 or greater
    public static void run() throws IOException {
        // ExStart:1
        // Initialize Scene
        Scene scene = new Scene(new Sphere());
        // Initialize  ObjSaveOptions
        ObjSaveOptions opt = new ObjSaveOptions();
        // To export 3D scene as point cloud setPointCould
        opt.setPointCloud(true);
        // Save
        scene.save(RunExamples.getDataDir()+ "export3DSceneAsPointCloud.obj", opt);
        // ExEnd:1
    }
}

```
