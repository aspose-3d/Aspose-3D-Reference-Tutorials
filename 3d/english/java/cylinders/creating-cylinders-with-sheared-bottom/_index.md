---
title: Java 3D Scene – Sheared Bottom Cylinders with Aspose.3D
linktitle: Java 3D Scene – Sheared Bottom Cylinders with Aspose.3D
second_title: Aspose.3D Java API
description: Learn how to build a java 3d scene by creating cylinders with a sheared bottom using Aspose.3D for Java. This tutorial covers installing Aspose 3D, applying shear transformation, and exporting OBJ files.
weight: 12
url: /java/cylinders/creating-cylinders-with-sheared-bottom/
date: 2026-05-14
keywords:
- java 3d scene
- install aspose 3d
- export obj java
- apply shear transformation
- aspose 3d tutorial
schemas:
- type: TechArticle
  headline: Java 3D Scene – Sheared Bottom Cylinders with Aspose.3D
  description: Learn how to build a java 3d scene by creating cylinders with a sheared
    bottom using Aspose.3D for Java. This tutorial covers installing Aspose 3D, applying
    shear transformation, and exporting OBJ files.
  dateModified: '2026-05-14'
  author: Aspose
- type: HowTo
  name: Java 3D Scene – Sheared Bottom Cylinders with Aspose.3D
  description: Learn how to build a java 3d scene by creating cylinders with a sheared
    bottom using Aspose.3D for Java. This tutorial covers installing Aspose 3D, applying
    shear transformation, and exporting OBJ files.
  steps:
  - name: Create a Scene
    text: A scene is the container for all 3‑D objects. We’ll start by creating an
      empty scene.
  - name: Create Cylinder 1 – How to Shear Cylinder
    text: Now we’ll build the first cylinder and **apply shear transformation** to
      its bottom. This demonstrates **how to shear cylinder** geometry directly via
      the API.
  - name: Create Cylinder 2 – Standard Cylinder (No Shear)
    text: For comparison, we’ll add a second cylinder that does **not** have a sheared
      bottom.
  - name: Save the Scene – Export OBJ File Java
    text: Finally, we export the scene to a Wavefront OBJ file, illustrating **export
      obj file java** usage.
- type: FAQPage
  questions:
  - question: Can I use Aspose.3D for Java with other Java 3D libraries?
    answer: Aspose.3D is designed to work independently. While you can integrate it
      with other libraries, it already provides a full‑featured API for most 3‑D tasks.
  - question: Is Aspose.3D suitable for beginners in 3D modeling?
    answer: Absolutely. The API is straightforward, and this **beginner 3d tutorial**
      demonstrates core concepts with minimal code.
  - question: Where can I find additional support for Aspose.3D for Java?
    answer: Visit the [Aspose.3D forum](https://forum.aspose.com/c/3d/18) for community
      help and official answers.
  - question: How can I obtain a temporary license for Aspose.3D?
    answer: You can get a temporary license [here](https://purchase.aspose.com/temporary-license/).
  - question: Where do I purchase a full Aspose.3D for Java license?
    answer: Purchase options are available [here](https://purchase.aspose.com/buy).
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java 3D Scene – Sheared Bottom Cylinders with Aspose.3D

## Introduction

In this hands‑on **java 3d scene** tutorial you’ll learn how to model a cylinder whose bottom is sheared, then export the result as a Wavefront OBJ file. Whether you’re a beginner exploring 3‑D concepts or a seasoned developer needing a quick programmatic transformation, this guide shows the complete workflow with Aspose.3D for Java— from project setup to final file output.

## Quick Answers
- **What library is used?** Aspose.3D for Java  
- **Can I install Aspose 3D via Maven?** Yes – add the Aspose.3D dependency to your `pom.xml`  
- **Is a license required for development?** A temporary license is sufficient for testing; a full license is needed for production  
- **Which file format is demonstrated?** Wavefront OBJ (`.obj`)  
- **How long does the example take to run?** Under a second on a typical workstation  

## What is a java 3d scene?

A **java 3d scene** is a container object that holds all meshes, lights, cameras, and transformations required to render or export a 3‑D model. The `Scene` class in Aspose.3D represents this container in memory, allowing you to add geometry, apply transformations, and finally serialize the whole scene to a file format of your choice.

## Why use Aspose.3D for this task?

Aspose.3D supports **50+ input and output formats**—including OBJ, FBX, STL, and GLTF— and can process multi‑hundred‑page models without loading the entire file into memory. Its API offers built‑in transformation utilities, so you can apply shear, scale, or rotate primitives with just a few lines of code, eliminating the need for external modeling tools.

## Prerequisites

Before we begin, ensure you have the following:

- Java Development Kit (JDK) installed on your system.  
- **Install Aspose 3D** – download the library from the official site [here](https://releases.aspose.com/3d/java/).  
- An IDE or build tool (Maven/Gradle) to manage the Aspose.3D dependency.  

## Import Packages

The following imports give you access to the core scene graph, geometry creation, and file‑handling classes.

The `Scene` class is Aspose.3D's top‑level object that represents a single 3‑D environment in memory.  
The `Cylinder` class creates a cylindrical mesh with configurable radius, height, and tessellation.  
The `Vector2` class defines a two‑dimensional vector used for shear factors.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## How to build a java 3d scene with a sheared cylinder?

Load the Aspose.3D library, create a new `Scene`, add a cylinder, apply a shear transformation to its bottom vertices, and finally save the scene as an OBJ file. This entire process can be achieved in under ten lines of Java code, making it ideal for rapid prototyping or automated asset generation.

### Step 1: Create a Scene

A scene is the container for all 3‑D objects. We’ll start by creating an empty scene.

```java
// ExStart:3
// Create a scene
Scene scene = new Scene();
// ExEnd:3
```

### Step 2: Create Cylinder 1 – How to Shear Cylinder

Now we’ll build the first cylinder and **apply shear transformation** to its bottom. This demonstrates **how to shear cylinder** geometry directly via the API.

```java
// ExStart:4
// Create cylinder 1
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Customized shear bottom for cylinder 1
cylinder1.setShearBottom(new Vector2(0, 0.83)); // Shear 47.5deg in the xy plane (z-axis)
// Add cylinder 1 to the scene
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

### Step 3: Create Cylinder 2 – Standard Cylinder (No Shear)

For comparison, we’ll add a second cylinder that does **not** have a sheared bottom.

```java
// ExStart:5
// Create cylinder 2
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// Add cylinder 2 without a ShearBottom to the scene
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Step 4: Save the Scene – Export OBJ File Java

Finally, we export the scene to a Wavefront OBJ file, illustrating **export obj file java** usage.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

## Why This Matters for Java 3D Modeling

Applying a shear to a primitive enables the creation of more organic and customized shapes directly in code, eliminating the need for external modeling software. This approach is especially useful for architectural visualizations with sloped bases, lightweight game assets requiring custom footprints, and rapid prototyping where dimensions must be adjusted programmatically.

- Architectural visualizations where sloped bases are required.  
- Game assets that need custom footprints while keeping geometry lightweight.  
- Rapid prototyping where you want to tweak dimensions programmatically.

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| **Shear appears too extreme** | Adjust the `Vector2` values; they represent the shear factor (0‑1 range). |
| **OBJ file not opening in viewer** | Verify that the target directory exists and that you have write permissions. |
| **License exception at runtime** | Apply a temporary or permanent license before creating the scene (`License license = new License(); license.setLicense("Aspose.3D.lic");`). |

## Frequently Asked Questions

**Q: Can I use Aspose.3D for Java with other Java 3D libraries?**  
A: Aspose.3D is designed to work independently. While you can integrate it with other libraries, it already provides a full‑featured API for most 3‑D tasks.

**Q: Is Aspose.3D suitable for beginners in 3D modeling?**  
A: Absolutely. The API is straightforward, and this **beginner 3d tutorial** demonstrates core concepts with minimal code.

**Q: Where can I find additional support for Aspose.3D for Java?**  
A: Visit the [Aspose.3D forum](https://forum.aspose.com/c/3d/18) for community help and official answers.

**Q: How can I obtain a temporary license for Aspose.3D?**  
A: You can get a temporary license [here](https://purchase.aspose.com/temporary-license/).

**Q: Where do I purchase a full Aspose.3D for Java license?**  
A: Purchase options are available [here](https://purchase.aspose.com/buy).


**Last Updated:** 2026-05-14  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose

## Related Tutorials

- [Create 3D Scene Java with Aspose 3D Java](/3d/java/3d-scenes-and-models/)
- [java 3d graphics tutorial – Concatenate Matrices Aspose.3D](/3d/java/geometry/transform-3d-nodes-with-matrices/)
- [Java 3D Graphics Tutorial - Create a 3D Cube Scene with Aspose.3D](/3d/java/geometry/create-3d-cube-scene/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}