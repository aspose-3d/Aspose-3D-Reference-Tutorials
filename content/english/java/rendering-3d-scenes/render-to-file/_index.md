---
title: Save Rendered 3D Scenes to Image Files with Aspose.3D for Java
linktitle: Save Rendered 3D Scenes to Image Files with Aspose.3D for Java
second_title: Aspose.3D Java API
description: 
type: docs
weight: 13
url: /java/rendering-3d-scenes/render-to-file/
---

## Complete Source Code
```java
package examples.render;

import com.aspose.threed.*;


import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

public class RenderToFile extends RenderBase {
    public static void run() throws IOException {

        Scene scene = new Scene();
        Camera camera = setupScene(scene);
        String output = "render-to-file.png";
        //Scene.render uses ImageIO internally, what output format is supported depends on your JRE.
        scene.render(camera, output, new Dimension(1024, 1024), "png");
    }
}

```
