---
title: Retrieve Information from 3D Scenes in Java Applications
linktitle: Retrieve Information from 3D Scenes in Java Applications
second_title: Aspose.3D Java API
description: 
type: docs
weight: 12
url: /java/3d-scenes-and-models/get-scene-information/
---

## Complete Source Code
```java
package examples.scene;

import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;


public class InformationToScene {

        public static void run() throws Exception {
            // ExStart:AddAssetInformationToScene
            // Initialize a 3D scene
            Scene scene = new Scene();

            // Set application/tool name
            scene.getAssetInfo().setApplicationName("Egypt");

            // Set application/tool vendor name
            scene.getAssetInfo().setApplicationVendor("Manualdesk");

            // We use ancient egyption measurement unit Pole
            scene.getAssetInfo().setUnitName("pole");

            // One Pole equals to 60cm
            scene.getAssetInfo().setUnitScaleFactor(0.6);

            // The path to the documents directory.
            String MyDir = "Your Document Directory";
            MyDir = MyDir + RunExamples.getOutputFilePath("InformationToScene.fbx");

            // Save scene to 3D supported file formats
            scene.save(MyDir, FileFormat.FBX7500ASCII);
            // ExEnd:AddAssetInformationToScene

            System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
        }
}

```
