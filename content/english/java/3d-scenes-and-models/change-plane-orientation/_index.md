---
title: Modify Plane Orientation for Precise 3D Scene Positioning in Java
linktitle: Modify Plane Orientation for Precise 3D Scene Positioning in Java
second_title: Aspose.3D Java API
description: 
type: docs
weight: 10
url: /java/3d-scenes-and-models/change-plane-orientation/
---

## Complete Source Code
```java
package examples.scene;

import com.aspose.threed.FileFormat;
import com.aspose.threed.Plane;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;



public class ChangePlaneOrientation {
    public static void run() throws Exception {
        // ExStart:ChangePlaneOrientation
        // The path to the documents directory.
        String MyDir = "Your Document Directory";
        // Initialize Scene
        Scene scene = new Scene();
        // Initialize Plane
        Plane plane = new Plane();
        // Set Vector
        plane.setUp(new Vector3(1, 1, 3));
        scene.getRootNode().createChildNode(plane);
        //This will generate a plane that has customized orientation
        scene.save(MyDir+"ChangePlaneOrientation.obj", FileFormat.WAVEFRONTOBJ);
        // ExEnd:ChangePlaneOrientation
    }
}

```
