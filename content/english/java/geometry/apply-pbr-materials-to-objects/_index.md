---
title: Apply PBR Materials to 3D Objects in Java with Aspose.3D
linktitle: Apply PBR Materials to 3D Objects in Java with Aspose.3D
second_title: Aspose.3D Java API
description: 
type: docs
weight: 10
url: /java/geometry/apply-pbr-materials-to-objects/
---

## Complete Source Code
```java
package examples.geometry;

import com.aspose.threed.*;


public class ApplyPBRMaterialToBox {

        public static void run() throws Exception {
            // ExStart:ApplyPBRMaterialToBox
            // The path to the documents directory.
            String MyDir = "Your Document Directory";

            // initialize a scene
            Scene scene = new Scene();
            // initialize PBR material object
            PbrMaterial mat = new PbrMaterial();
            // an almost metal material
            mat.setMetallicFactor(0.9);
            // material surface is very rough
            mat.setRoughnessFactor(0.9);
            // create a box to which the material will be applied
            Node boxNode = scene.getRootNode().createChildNode("box", new Box());
            boxNode.setMaterial(mat);
            // save 3d scene into STL format
            scene.save(MyDir + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
            // ExEnd:ApplyPBRMaterialToBox
        }
}

```
