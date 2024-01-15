---
title: Transform 3D Nodes with Euler Angles in Java using Aspose.3D
linktitle: Transform 3D Nodes with Euler Angles in Java using Aspose.3D
second_title: Aspose.3D Java API
description: 
type: docs
weight: 19
url: /java/geometry/transform-3d-nodes-with-euler-angles/
---

## Complete Source Code
```java
package examples.geometry;

import com.aspose.threed.*;


public class TransformationToNodeByEulerAngles {

        public static void run() throws Exception {
            // ExStart:AddTransformationToNodeByEulerAngles
            // Initialize scene object
            Scene scene = new Scene();

            // Initialize Node class object
            Node cubeNode = new Node("cube");

            // Call Common class create mesh using polygon builder method to set mesh instance
            Mesh mesh = Common.createMeshUsingPolygonBuilder();

            // Point node to the Mesh geometry
            cubeNode.setEntity(mesh);
            // Euler angles
            cubeNode.getTransform().setEulerAngles(new Vector3(0.3, 0.1, -0.5));
            // Set translation
            cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
            // Add cube to the scene
            scene.getRootNode().getChildNodes().add(cubeNode);

            // The path to the documents directory.
            String MyDir = "Your Document Directory";
            MyDir = MyDir + RunExamples.getOutputFilePath("TransformationToNode.fbx");

            // Save 3D scene in the supported file formats
            scene.save(MyDir, FileFormat.FBX7500ASCII);
            // ExEnd:AddTransformationToNodeByEulerAngles
            System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);

        }
}

```
