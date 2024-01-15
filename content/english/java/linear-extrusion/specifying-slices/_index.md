---
title: Specifying Slices in Linear Extrusion with Aspose.3D for Java
linktitle: Specifying Slices in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
description: 
type: docs
weight: 13
url: /java/linear-extrusion/specifying-slices/
---

## Complete Source Code
```java
package examples.LinearExtrusion;

import com.aspose.threed.*;

import java.io.IOException;

public class SlicesInLinearExtrusion {
    public static void run() throws IOException {
        // ExStart:SlicesInLinearExtrusion
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

        // Slices parameter defines the number of intermediate points along the path of the extrusion
        // Perform linear extrusion on left node using slices property
        left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
        // Perform linear extrusion on right node using slices property
        right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});

        // Save 3D scene
        scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
        // ExEnd:SlicesInLinearExtrusion

    }
}

```