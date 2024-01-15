---
title: Generate Data for 3D Meshes in Java (Normals, Tangents, Binormals)
linktitle: Generate Data for 3D Meshes in Java (Normals, Tangents, Binormals)
second_title: Aspose.3D Java API
description: 
type: docs
weight: 11
url: /java/3d-mesh-data/generate-mesh-data/
---

## Complete Source Code
```java
package examples.objects;

import com.aspose.threed.*;


import java.io.IOException;

public class GenerateDataForMeshes {

        public static void run() throws IOException {
            // ExStart:GenerateDataForMeshes
            // The path to the documents directory.
            String MyDir = "Your Document Directory";

            // Load a 3ds file, 3ds file doesn't have normal data, but it has smoothing group
            Scene s = new Scene(MyDir + "camera.3ds");
            // Visit all nodes and create normal data for all meshes
            s.getRootNode().accept(new NodeVisitor() {
                @Override
                public boolean call(Node node) {
                    Mesh mesh = (Mesh)node.getEntity();
                    if (mesh != null)
                    {
                        VertexElementNormal normals = PolygonModifier.generateNormal(mesh);
                        mesh.addElement(normals);
                    }
                    return true;
                }
            });
            // ExEnd:GenerateDataForMeshes
            System.out.println("\nNormal data generated successfully for all meshes.");
        }
}

```
