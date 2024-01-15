---
title: Efficiently Detect 3D File Formats in Java with Aspose.3D
linktitle: Efficiently Detect 3D File Formats in Java with Aspose.3D
second_title: Aspose.3D Java API
description: 
type: docs
weight: 11
url: /java/load-and-save/detect-3d-file-formats/
---

## Complete Source Code
```java
package examples.loadsave;

import com.aspose.threed.FileFormat;


import java.io.IOException;

public class DetectFormat {
    public static void run() throws IOException {
            // ExStart:DetectFormat
            // The path to the documents directory.
            String MyDir = "Your Document Directory";
            // Detect the format of a 3D file
            FileFormat inputFormat = FileFormat.detect(MyDir + "document.fbx");
            // Display the file format
            System.out.println("File Format: " + inputFormat.toString());
            // ExEnd:DetectFormat
        }
}

```
