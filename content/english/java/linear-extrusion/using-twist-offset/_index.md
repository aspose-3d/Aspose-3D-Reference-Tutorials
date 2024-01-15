---
title: Using Twist Offset in Linear Extrusion with Aspose.3D for Java
linktitle: Using Twist Offset in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
description: 
type: docs
weight: 15
url: /java/linear-extrusion/using-twist-offset/
---

## Complete Source Code
```java
package examples.LinearExtrusion;

import com.aspose.threed.*;


import java.io.IOException;

public class TwistOffsetInLinearExtrusion {
    public static void run() throws IOException {
        // ExStart:TwistOffsetInLinearExtrusion
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

        // TwistOffset property is the translate offset while rotating the extrusion.
        // Perform linear extrusion on left node using twist and slices property
        left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
        // Perform linear extrusion on right node using twist, twist offset and slices property
        right.createChildNode(new LinearExtrusion(profile, 10)  {{setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0));}});

        // Save 3D scene
        scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
        // ExEnd:TwistOffsetInLinearExtrusion
    }
}

```
