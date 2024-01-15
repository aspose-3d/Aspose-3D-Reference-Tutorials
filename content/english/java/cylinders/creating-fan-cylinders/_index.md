---
title: Creating Customized Fan Cylinders with Aspose.3D for Java
linktitle: Creating Customized Fan Cylinders with Aspose.3D for Java
second_title: Aspose.3D Java API
description: 
type: docs
weight: 10
url: /java/cylinders/creating-fan-cylinders/
---

## Complete Source Code
```java
package examples.WorkingWithCylinder;

import com.aspose.threed.*;


import java.io.IOException;

public class CreateFanCylinder {
    public static void run() throws IOException {
        // ExStart:1
        // Create a Scene
        Scene scene = new Scene();
        // Create a cylinder
        Cylinder fan = new Cylinder(2, 2, 10, 20, 1, false);
        // Set GenerateGanCylinder to true
        fan.setGenerateFanCylinder(true);
        // Set ThetaLength
        fan.setThetaLength(MathUtils.toRadian(270.0));
        // Create ChildNode
        scene.getRootNode().createChildNode(fan).getTransform().setTranslation(10, 0, 0);
        // Create a cylinder without a fan
        Cylinder nonfan = new Cylinder(2, 2, 10, 20, 1, false);
        // Create ChildNode
        scene.getRootNode().createChildNode(nonfan);
        // Save scene
        scene.save("Your Document Directory"+ "CreateFanCylinder.obj", FileFormat.WAVEFRONTOBJ);
        // ExEnd:1
    }
}

```
