---
title: Share Mesh Geometry Data in Java 3D with Aspose.3D
linktitle: Share Mesh Geometry Data in Java 3D with Aspose.3D
second_title: Aspose.3D Java API
description: 
type: docs
weight: 15
url: /java/geometry/share-mesh-geometry-data/
---

## Complete Source Code
```java
package examples.geometry;

import com.aspose.threed.*;



public class MeshGeometryData {

        public static void run() throws Exception {
            // ExStart:ShareMeshGeometryData
            // Initialize scene object
            Scene scene = new Scene();

            // Define color vectors
            Vector3[] colors = new Vector3[] {
                new Vector3(1, 0, 0),
                new Vector3(0, 1, 0),
                new Vector3(0, 0, 1)
            };

            // Call Common class create mesh using polygon builder method to set mesh instance
            Mesh mesh = Common.createMeshUsingPolygonBuilder();

            int idx = 0;
            for(Vector3 color : colors)
            {
                // Initialize cube node object
                Node cube = new Node("cube");
                cube.setEntity(mesh);
                LambertMaterial mat = new LambertMaterial();
                // Set color
                mat.setDiffuseColor(color);
                // Set material
                cube.setMaterial(mat);
                // Set translation
                cube.getTransform().setTranslation(new Vector3(idx++ * 20, 0, 0));
                // Add cube node
                scene.getRootNode().addChildNode(cube);
            }

            // The path to the documents directory.
            String MyDir = "Your Document Directory";
            MyDir = MyDir + "MeshGeometryData.fbx";

            // Save 3D scene in the supported file formats
            scene.save(MyDir, FileFormat.FBX7400ASCII);
            // ExEnd:ShareMeshGeometryData
            System.out.println("\nMesh’s geometry data shared successfully between multiple nodes.\nFile saved at " + MyDir);

        }
}

```
