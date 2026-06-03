---
title: Export scene as FBX and build cylinder with Aspose.3D Java
linktitle: Building Primitive 3D Models with Aspose.3D for Java
second_title: Aspose.3D Java API
description: Learn how to export scene as FBX and create 3D cylinder, box, and other primitive models using Aspose.3D for Java.
weight: 10
url: /java/primitive-3d-models/building-primitive-3d-models/
date: 2026-06-03
keywords:
- export scene as fbx
- convert 3d model fbx
- Aspose 3D primitives
- Java 3D modeling
schemas:
- type: TechArticle
  headline: Export scene as FBX and build cylinder with Aspose.3D Java
  description: Learn how to export scene as FBX and create 3D cylinder, box, and other
    primitive models using Aspose.3D for Java.
  dateModified: '2026-06-03'
  author: Aspose
- type: HowTo
  name: Export scene as FBX and build cylinder with Aspose.3D Java
  description: Learn how to export scene as FBX and create 3D cylinder, box, and other
    primitive models using Aspose.3D for Java.
  steps:
  - name: Initialize a Scene Object
    text: The `Scene` class is Aspose.3D's top‑level container that holds all nodes,
      lights, cameras, and materials in memory.
  - name: Build a 3D box model
    text: The `Box` class represents a rectangular prism and is useful for testing
      the coordinate system. Adding it as a child of the scene’s root node positions
      it at the origin.
  - name: Create a 3D cylinder model
    text: The `Cylinder` class is Aspose.3D's built‑in cylinder primitive. It comes
      with default dimensions (radius = 1, height = 2) but you can customise them
      via its constructor.
  - name: Save the drawing in the FBX format
    text: After assembling the scene, export it so other tools (e.g., Unity, Blender)
      can read it. We use the `FBX7500ASCII` format, which is widely supported and
      human‑readable.
- type: FAQPage
  questions:
  - question: Can I use Aspose.3D for Java with other programming languages?
    answer: Aspose.3D primarily supports Java, but there are versions available for
      .NET and C++ as well.
  - question: Is Aspose.3D suitable for complex 3D modeling tasks?
    answer: Absolutely. It provides a comprehensive set of features—including mesh
      manipulation, material assignment, and animation—making it suitable for both
      simple primitives and intricate models.
  - question: Where can I find additional help and support?
    answer: Visit the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) for community
      support and discussions.
  - question: Can I try Aspose.3D before purchasing?
    answer: Yes, you can explore a [free trial](https://releases.aspose.com/) before
      making a purchase decision.
  - question: How do I obtain a temporary license for Aspose.3D?
    answer: You can obtain a [temporary license](https://purchase.aspose.com/temporary-license/)
      for Aspose.3D through the website.
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Export scene as FBX and build cylinder with Aspose.3D Java

## Introduction

If you’ve ever needed to **create a 3D cylinder** (or any other basic shape) directly from Java code, Aspose.3D makes the task painless. In this tutorial we’ll walk through the entire workflow—from setting up the environment to **export scene as FBX**—so you can start generating 3D geometry programmatically right away. You’ll see how the library handles primitives, how to organise them in a scene graph, and how to save the result in a format that Unity, Blender, or any other 3D tool can read.

## Quick Answers
- **What library lets me create a 3D cylinder in Java?** Aspose.3D for Java.  
- **Which format can I export the scene to?** FBX (ASCII 7500) using `FileFormat.FBX7500ASCII`.  
- **Do I need a license for development?** A free trial works for testing; a permanent license is required for production.  
- **What are the main primitives supported?** Box, Cylinder, Sphere, Cone, and more than 10 additional shapes.  
- **Is the code compatible with Java 8 and later?** Yes, Aspose.3D targets JDK 8+.

## What is a 3D cylinder primitive?

A cylinder primitive is a basic geometric shape defined by a radius and height. In many 3D pipelines it serves as a building block for more complex models such as pipes, wheels, or architectural columns. Aspose.3D provides a ready‑made `Cylinder` class, so you don’t have to calculate vertices manually.

## Why use Aspose.3D for Java?

Aspose.3D for Java offers a comprehensive, pure‑Java 3D engine that eliminates the need for native libraries, making it ideal for cross‑platform development. It supports a wide range of import and export formats, provides a robust scene graph for hierarchical organization, and includes built‑in primitives that let you create geometry with minimal code. These features together accelerate development and reduce maintenance overhead.

- **Full‑featured 3D engine** – supports import/export of **over 30** popular formats (FBX, OBJ, STL, GLTF, 3DS, etc.).  
- **Pure Java API** – no native dependencies, perfect for cross‑platform projects.  
- **Robust scene graph** – lets you organise objects hierarchically, making large scenes easy to manage.  
- **Easy licensing** – start with a free trial, then upgrade to a permanent license when you go live.

## Prerequisites

Before diving into the code, make sure you have:

1. **Java Development Kit (JDK)** – JDK 8 or newer installed on your machine.  
2. **Aspose.3D for Java library** – download and install it from the [download page](https://releases.aspose.com/3d/java/).  

## Import Packages

Begin by importing the core Aspose.3D namespace. This gives you access to `Scene`, `Box`, `Cylinder`, and file‑format constants.

```java
import com.aspose.threed.*;
```

Now that the library is referenced, let’s create a scene and add some primitive geometry.

## How to export scene as FBX and create 3D primitives?

Load a new `Scene` object, add primitive nodes (Box, Cylinder, etc.), and then call `save` with the FBX7500ASCII format. In just a few lines you obtain a fully‑featured FBX file that can be opened in any major 3D editor, enabling seamless integration with game engines, rendering pipelines, or AR/VR applications.

### Step 1: Initialize a Scene Object

The `Scene` class is Aspose.3D's top‑level container that holds all nodes, lights, cameras, and materials in memory.

```java
// The path to the documents directory.
String myDir = "Your Document Directory";

// Initialize a Scene object
Scene scene = new Scene();
```

### Step 2: Build a 3D box model

The `Box` class represents a rectangular prism and is useful for testing the coordinate system. Adding it as a child of the scene’s root node positions it at the origin.

```java
// Create a Box model
scene.getRootNode().createChildNode("box", new Box());
```

### Step 3: Create a 3D cylinder model

The `Cylinder` class is Aspose.3D's built‑in cylinder primitive. It comes with default dimensions (radius = 1, height = 2) but you can customise them via its constructor.

```java
// Create a Cylinder model
scene.getRootNode().createChildNode("cylinder", new Cylinder());
```

### Step 4: Save the drawing in the FBX format

After assembling the scene, export it so other tools (e.g., Unity, Blender) can read it. We use the `FBX7500ASCII` format, which is widely supported and human‑readable.

```java
// Save drawing in the FBX format
myDir = myDir + "test.fbx";
scene.save(myDir, FileFormat.FBX7500ASCII);
```

## Common Issues and Solutions

| Issue | Why it Happens | Fix |
|-------|----------------|-----|
| **File not found** when saving | `myDir` points to a non‑existent folder | Ensure the directory exists or create it with `new File(myDir).mkdirs();` |
| **Empty scene** after export | No nodes were added before calling `save` | Verify that `createChildNode` calls are executed (debug with `scene.getRootNode().getChildCount()` ) |
| **License exception** | Running without a valid license in production | Apply a temporary or permanent license using `License license = new License(); license.setLicense("Aspose.3D.Java.lic");` |

## Frequently Asked Questions

**Q: Can I use Aspose.3D for Java with other programming languages?**  
A: Aspose.3D primarily supports Java, but there are versions available for .NET and C++ as well.

**Q: Is Aspose.3D suitable for complex 3D modeling tasks?**  
A: Absolutely. It provides a comprehensive set of features—including mesh manipulation, material assignment, and animation—making it suitable for both simple primitives and intricate models.

**Q: Where can I find additional help and support?**  
A: Visit the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) for community support and discussions.

**Q: Can I try Aspose.3D before purchasing?**  
A: Yes, you can explore a [free trial](https://releases.aspose.com/) before making a purchase decision.

**Q: How do I obtain a temporary license for Aspose.3D?**  
A: You can obtain a [temporary license](https://purchase.aspose.com/temporary-license/) for Aspose.3D through the website.

## Conclusion

You’ve now learned how to **export scene as FBX**, and how to **create 3D cylinder**, box, and other primitive models using Aspose.3D for Java. Feel free to experiment with additional primitives such as Sphere, Cone, or Torus, and explore material assignments to give your models a realistic look. Once you’re comfortable, you can integrate the generated FBX files into game engines, AR/VR pipelines, or any downstream 3D workflow.

---

**Last Updated:** 2026-06-03  
**Tested With:** Aspose.3D for Java 24.11 (latest at time of writing)  
**Author:** Aspose

## Related Tutorials

- [How to Export Scene to FBX and Retrieve 3D Scene Info in Java](/3d/java/3d-scenes-and-models/get-scene-information/)
- [How to Export FBX and Build Node Hierarchies in Java](/3d/java/geometry/build-node-hierarchies/)
- [How to Create Cylinder Models with Aspose.3D for Java](/3d/java/cylinders/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< blocks/products/products-backtop-button >}}
{{< /blocks/products/pf/main-wrap-class >}}