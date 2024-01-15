---
title: Read Existing 3D Scenes Effortlessly in Java with Aspose.3D
linktitle: Read Existing 3D Scenes Effortlessly in Java with Aspose.3D
second_title: Aspose.3D Java API
description: 
type: docs
weight: 14
url: /java/load-and-save/read-existing-3d-scenes/
---

## Complete Source Code
```java
package examples.loadsave;

import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;


import java.io.IOException;

public class ReadExistingScene {

        public static void run() throws IOException {
            // ExStart:ReadExistingScene
            // The path to the documents directory.
            String MyDir = "Your Document Directory";

            // Initialize a Scene class object
            Scene scene = new Scene();
            // Load an existing 3D document
            scene.open(MyDir + "document.fbx");

            // ExEnd:ReadExistingScene
            System.out.println("\n3D Scene is ready for the modification, addition or processing purposes.");
            
        }
        
        public static void ReadRVMWithAttributes() throws IOException
        {
            //ExStart:ReadRVMWithAttributes
            String dataDir = "Your Document Directory";

            Scene scene = new Scene(dataDir + "att-test.rvm");
            
            FileFormat.RVM_BINARY.loadAttributes(scene, dataDir + "att-test.att");
            //ExEnd: ReadRVMWithAttributes
        }
}

```
