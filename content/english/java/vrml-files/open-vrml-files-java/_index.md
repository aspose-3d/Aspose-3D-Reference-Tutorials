---
title: Open and Manipulate VRML Files in Java with Aspose.3D
linktitle: Open and Manipulate VRML Files in Java with Aspose.3D
second_title: Aspose.3D Java API
description: 
type: docs
weight: 10
url: /java/vrml-files/open-vrml-files-java/
---

## Complete Source Code
```java
package examples.workingwithVRML;

import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Sphere;


import java.io.IOException;

public class OpenVRML {
    public static void run() throws IOException {
        // ExStart:OpenVRML
        // The path to the documents directory.
        String MyDir = "Your Document Directory";
        // initialize a scene
        Scene scene = new Scene();
        // open Virtual Reality Modeling Language (VRML) file format
        scene.open( MyDir + "test.wrl");
        // work with VRML file format...
        // ExEnd:OpenVRML
    }
}

```
