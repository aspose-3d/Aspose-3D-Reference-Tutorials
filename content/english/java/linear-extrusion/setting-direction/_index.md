---
title: Setting Direction in Linear Extrusion with Aspose.3D for Java
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
description: 
type: docs
weight: 12
url: /java/linear-extrusion/setting-direction/
---

## Complete Source Code
```java
package examples.LinearExtrusion;

import com.aspose.threed.*;


import java.io.IOException;

public class DirectionInLinearExtrusion {
    public static void run() throws IOException {
        // ExStart:DirectionInLinearExtrusion
        // The path to the documents directory.
        String MyDir = "Your Document Directory";
        // Initialize the base profile to be extruded
        RectangleShape profile = new RectangleShape();
        profile.setRoundingRadius(0.3);
        // Create a scene
        Scene scene = new Scene();
        // Create left node
        Node left = scene.getRootNode().createChildNode();
        // Create right node
        Node right = scene.getRootNode().createChildNode();
        left.getTransform().setTranslation(new Vector3(5, 0, 0));

        // Direction property defines the direction of the extrusion.
        // Perform linear extrusion on left node using twist and slices property
        left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
        // Perform linear extrusion on right node using twist, slices, and direction property
        right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});

        // Save 3D scene
        scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
        // ExEnd:DirectionInLinearExtrusion
    }
}

```
