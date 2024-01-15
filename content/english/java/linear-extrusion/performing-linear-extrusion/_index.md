---
title: Performing Linear Extrusion in Aspose.3D for Java
linktitle: Performing Linear Extrusion in Aspose.3D for Java
second_title: Aspose.3D Java API
description: 
type: docs
weight: 10
url: /java/linear-extrusion/performing-linear-extrusion/
---

## Complete Source Code
```java
package examples.LinearExtrusion;

import com.aspose.threed.*;


public class PerformingLinearExtrusion {
    public static void run() throws Exception {
        // ExStart:PerformingLinearExtrusion
        // The path to the documents directory.
        String MyDir = "Your Document Directory";
        // Initialize the base shape to be extruded
        // Initialize the base profile to be extruded
        RectangleShape profile = new RectangleShape();
        profile.setRoundingRadius(0.3);
        // Perform Linear extrusion by passing a 2D shape as input and extend the shape in the 3rd dimension
        LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
        extrusion.setSlices(100);
        extrusion.setCenter(true);
        extrusion.setTwist(360);
        extrusion.setTwistOffset(new Vector3(10, 0, 0));
        // Create a scene
        Scene scene = new Scene();
        // Create a child node by passing extrusion
        scene.getRootNode().createChildNode(extrusion);
        // Save 3D scene
        scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
        // ExEnd:PerformingLinearExtrusion
    }
}

```
