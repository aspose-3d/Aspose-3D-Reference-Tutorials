---
title: Convert Primitives to Meshes in Java (Box, Cylinder, Plane, Sphere, Torus)
linktitle: Convert Primitives to Meshes in Java (Box, Cylinder, Plane, Sphere, Torus)
second_title: Aspose.3D Java API
description: 
type: docs
weight: 12
url: /java/transforming-3d-meshes/convert-primitives-to-meshes/
---

## Complete Source Code
```java
package examples.objects;

import com.aspose.threed.*;
import examples.RunExamples;

public class ConvertBoxPrimitivetoMesh {

        public static void run() throws Exception {
            // Initialize scene object
            Scene scene = new Scene();

            // Initialize Node class object
            Node cubeNode = new Node("box");

            // ExStart:ConvertBoxPrimitivetoMesh
            // Initialize object by Box class
            IMeshConvertible convertible = new Box();
            // Convert a Box to Mesh
            Mesh mesh = convertible.toMesh();
            // ExEnd:ConvertBoxPrimitivetoMesh

            // Point node to the Mesh geometry
            cubeNode.setEntity(mesh);

            // Add Node to a scene
            scene.getRootNode().addChildNode(cubeNode);

            // The path to the documents directory.
            String MyDir = RunExamples.getDataDir() + RunExamples.getOutputFilePath("BoxToMeshScene.fbx");

            // Save 3D scene in the supported file formats
            scene.save(MyDir, FileFormat.FBX7400ASCII);

            System.out.println("\n Converted the primitive Box to a mesh successfully.\nFile saved at " + MyDir);
        }
}

```
