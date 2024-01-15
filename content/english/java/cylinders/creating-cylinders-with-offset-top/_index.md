---
title: Creating Cylinders with Offset Top in Aspose.3D for Java
linktitle: Creating Cylinders with Offset Top in Aspose.3D for Java
second_title: Aspose.3D Java API
description: 
type: docs
weight: 11
url: /java/cylinders/creating-cylinders-with-offset-top/
---

## Complete Source Code
```java
package examples.WorkingWithCylinder;

import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;
import examples.RunExamples;

import java.io.IOException;

public class CustomizedOffsetTopCylinder {
    public static void run() throws IOException {
        // ExStart:1
        // Create a scene
        Scene scene = new Scene();
        // Initialize cylinder
        Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
        // Set OffsetTop
        cylinder1.setOffsetTop(new Vector3(5, 3, 0));
        // Create ChildNode
        scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
        // Initialize second cylinder without customized OffsetTop
        Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
        // Create ChildNode
        scene.getRootNode().createChildNode(cylinder2);
        // Save
        scene.save(RunExamples.getDataDir()+ "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
        // ExEnd:1
    }
}

```
