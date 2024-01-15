---
title: Expose Geometric Transformations in Java 3D with Aspose.3D
linktitle: Expose Geometric Transformations in Java 3D with Aspose.3D
second_title: Aspose.3D Java API
description: 
type: docs
weight: 13
url: /java/geometry/expose-geometric-transformations/
---

## Complete Source Code
```java
package examples.geometry;

import com.aspose.threed.Node;
import com.aspose.threed.Vector3;

public class ExposeGeometricTransformation {
    public static void run() throws Exception {
        //ExStart: 1
        // Initialize node
        Node n = new Node();
        // Get Geometric Translation
        n.getTransform().setGeometricTranslation(new Vector3(10, 0, 0));
        // The first Console.WriteLine will output the transform matrix that includes the geometric transformation
        // while the second one will not.
        System.out.println(n.evaluateGlobalTransform(true));
        System.out.println(n.evaluateGlobalTransform(false));
        //ExEnd: 1
    }
}

```
