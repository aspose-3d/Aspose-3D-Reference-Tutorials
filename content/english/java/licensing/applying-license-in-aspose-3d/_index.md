---
title: Applying a License in Aspose.3D for Java
linktitle: Applying a License in Aspose.3D for Java
second_title: Aspose.3D Java API
description: 
type: docs
weight: 10
url: /java/licensing/applying-license-in-aspose-3d/
---

## Complete Source Code
```java
package examples.license;

import com.aspose.threed.License;
import com.aspose.threed.Metered;

import java.io.FileInputStream;
import java.io.IOException;

public class ApplyLicense {

    public static void usingFile() {
        // ExStart:ApplyLicenseUsingFile
        License license = new License();
        license.setLicense("Aspose._3D.lic");
        // ExEnd:ApplyLicenseUsingFile
    }

    public static void usingStreamObject() throws IOException {
        // ExStart:ApplyLicenseUsingStreamObject
        License license = new License();
        try(FileInputStream myStream = new FileInputStream("Aspose._3D.lic")) {
            license.setLicense(myStream);
        }
        // ExEnd:ApplyLicenseUsingStreamObject
    }


    public static void publicAndPrivateKeys() throws Exception {
        // ExStart:PublicAndPrivateKeys
        // Initialize a Metered license class object
        Metered metered = new Metered();
        // Set public and private keys
        metered.setMeteredKey("your-public-key", "your-private-key");
        // ExEnd:PublicAndPrivateKeys
    }
}

```
