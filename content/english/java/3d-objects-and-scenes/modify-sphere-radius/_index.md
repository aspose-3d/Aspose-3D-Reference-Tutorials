---
title: Modify 3D Sphere Radius in Java with Aspose.3D
linktitle: Modify 3D Sphere Radius in Java with Aspose.3D
second_title: Aspose.3D Java API
description: 
type: docs
weight: 10
url: /java/3d-objects-and-scenes/modify-sphere-radius/
---

## Complete Source Code
```java
package examples.objects;

import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Sphere;

import java.io.IOException;

public class WorkingWithSphereRadius {
    public static void run() throws IOException {
        // ExStart:WorkingWithSphereRadius

        // initialize a scene
        Scene scene = new Scene();
        // initialize a Sphere
        Sphere sphere = new Sphere();
        // set radius
        sphere.setRadius(10);
        // add sphere to the scene
        scene.getRootNode().createChildNode(sphere);
        // save scene
        scene.save("sphere.obj", FileFormat.WAVEFRONTOBJ);
        // ExEnd:WorkingWithSphereRadius

    }
}

```
