---
title: Building Primitive 3D Models with Aspose.3D for Java
linktitle: Building Primitive 3D Models with Aspose.3D for Java
second_title: Aspose.3D Java API
description: 
type: docs
weight: 10
url: /java/primitive-3d-models/building-primitive-3d-models/
---

## Complete Source Code
```java
package examples.modeling;
import com.aspose.threed.*;


public class Primitive3DModels {

    public static void run() throws Exception {
            // ExStart:Primitive3DModels
            // The path to the documents directory.
            String MyDir = "Your Document Directory";

            // Initialize a Scene object
            Scene scene = new Scene();
            // Create a Box model
            scene.getRootNode().createChildNode("box", new Box());
            // Create a Cylinder model
            scene.getRootNode().createChildNode("cylinder", new Cylinder());
            // Save drawing in the FBX format
            MyDir = MyDir + RunExamples.getOutputFilePath("test.fbx");
            scene.save(MyDir, FileFormat.FBX7500ASCII);

            // ExEnd:Primitive3DModels
            System.out.println("\nBuilding a scene from primitive 3D models successfully.\nFile saved at " + MyDir);

    }
}

```
