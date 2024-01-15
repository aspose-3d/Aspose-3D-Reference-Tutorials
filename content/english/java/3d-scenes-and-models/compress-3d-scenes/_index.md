---
title: Compress 3D Scenes for Efficient Storage and Sharing with Aspose.3D for Java
linktitle: Compress 3D Scenes for Efficient Storage and Sharing with Aspose.3D for Java
second_title: Aspose.3D Java API
description: 
type: docs
weight: 11
url: /java/3d-scenes-and-models/compress-3d-scenes/
---

## Complete Source Code
```java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package examples.scene;

import com.aspose.threed.AmfSaveOptions;
import com.aspose.threed.Box;
import com.aspose.threed.Scene;
import com.aspose.threed.Transform;
import com.aspose.threed.Vector3;


public class ExportSceneToCompressedAMF {
            public static void run() throws Exception {
            // ExStart:CompressedAMF
            // The path to the documents directory.
            String MyDir = "Your Document Directory";
            Scene scene = new Scene();
            Box box = new Box();
            Transform tr = scene.getRootNode().createChildNode(box).getTransform();
            tr.setScale(new Vector3(12, 12, 12));
            tr.setTranslation(new Vector3(10, 0, 0));
            tr = scene.getRootNode().createChildNode(box).getTransform();
            tr.setScale(new Vector3(5, 5, 5));
            tr.setEulerAngles(new Vector3(50, 10, 0));
            scene.getRootNode().createChildNode();
            scene.getRootNode().createChildNode().createChildNode(box);
            scene.getRootNode().createChildNode().createChildNode(box);
            AmfSaveOptions opt = new AmfSaveOptions();
            opt.setEnableCompression(false);
            scene.save(MyDir + "test.amf", opt);
            // ExEnd:CompressedAMF
        }
    
}

```
