---
title: Build Node Hierarchies in 3D Scenes with Java and Aspose.3D
linktitle: Build Node Hierarchies in 3D Scenes with Java and Aspose.3D
second_title: Aspose.3D Java API
description: 
type: docs
weight: 16
url: /java/geometry/build-node-hierarchies/
---

## Complete Source Code
```java
package examples.geometry;

import com.aspose.threed.*;



public class NodeHierarchy {

        public static void run() throws Exception {
            // ExStart:AddNodeHierarchy
            // Initialize scene object
            Scene scene = new Scene();

            // Get a child node object
            Node top = scene.getRootNode().createChildNode();
            // Each cube node has their own translation
            Node cube1 = top.createChildNode("cube1");
            // Call Common class create mesh using polygon builder method to set mesh instance
            Mesh mesh = Common.createMeshUsingPolygonBuilder();
            // Point node to the mesh
            cube1.setEntity(mesh);
            // Set first cube translation
            cube1.getTransform().setTranslation(new Vector3(-10, 0, 0));
            Node cube2 = top.createChildNode("cube2");
            // Point node to the mesh
            cube2.setEntity(mesh);
            // Set second cube translation
            cube2.getTransform().setTranslation(new Vector3(10, 0, 0));

            // The rotated top node will affect all child nodes
            top.getTransform().setRotation(Quaternion.fromEulerAngle(Math.PI, 4, 0));

            // The path to the documents directory.
            String MyDir = "Your Document Directory";
            MyDir = MyDir + RunExamples.getOutputFilePath("NodeHierarchy.fbx");

            // Save 3D scene in the supported file formats
            scene.save(MyDir, FileFormat.FBX7500ASCII);
            // ExEnd:AddNodeHierarchy

            System.out.println("\nNode hierarchy added successfully to document.\nFile saved at " + MyDir);

        }
}

```
