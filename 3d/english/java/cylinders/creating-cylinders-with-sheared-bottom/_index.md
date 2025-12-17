---
title: "How to Use Aspose: Create Cylinders with Sheared Bottom in Java"
linktitle: "How to Use Aspose: Create Cylinders with Sheared Bottom in Java"
second_title: "Aspose.3D Java API"
description: "Learn how to use Aspose to create customized cylinders with sheared bottoms in Java, perfect for java 3d modeling and saving scenes as OBJ."
weight: 12
url: /java/cylinders/creating-cylinders-with-sheared-bottom/
date: 2025-12-09
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# How to Use Aspose: Create Cylinders with Sheared Bottom in Java

## Introduction

In this hands‑on tutorial you'll discover **how to use Aspose** to build a cylinder whose bottom is sheared—a technique often needed in *java 3d modeling* projects. We'll walk through every step, from setting up the scene to saving the final model as an OBJ file. By the end, you’ll have a reusable code snippet that you can drop into any Java‑based 3D application.

## Quick Answers
- **What does “shear bottom” mean?** It tilts the cylinder’s base by a specified angle in the XY plane.  
- **Which library handles the 3D math?** Aspose.3D for Java provides the `Cylinder` and `Vector2` classes.  
- **Do I need a license to run the example?** A temporary license works for evaluation; a full license is required for production.  
- **Can I export the model to other formats?** Yes—use `scene.save(..., FileFormat.WAVEFRONTOBJ)` to get an OBJ file.  
- **What Java version is required?** JDK 8 or later is sufficient.

## What is “how to use aspose” in the context of 3D modeling?

Aspose.3D for Java is a high‑level API that abstracts the complexities of 3D geometry, file formats, and transformations. Instead of dealing with low‑level vertex buffers, you call intuitive methods like `new Cylinder(...)` and let Aspose handle the heavy lifting.

## Why use Aspose for Java 3D Modeling?

- **Rapid development:** Build complex shapes with a few lines of code.  
- **Broad format support:** Export to OBJ, STL, FBX, and more.  
- **Cross‑platform:** Works on any OS that supports Java.  
- **Consistent API:** The same code works for desktop, server, or Android environments.

## Prerequisites

Before you start, ensure you have:

- **Java Development Kit (JDK) 8+** installed and configured in your IDE.  
- **Aspose.3D for Java** library added to your project classpath. You can download it from the official site [here](https://releases.aspose.com/3d/java/).  
- **A temporary or full license** (optional for trial runs).

## Import Packages

To begin, import the essential Aspose.3D classes and Java utilities:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Step 1: Create a Scene

A *scene* is the container that holds all 3D objects, lights, and cameras. Think of it as the stage where you’ll place your cylinders.

```java
// ExStart:3
// Create a scene
Scene scene = new Scene();
// ExEnd:3
```

## Step 2: Create Cylinder 1 (Sheared Bottom)

Now we’ll create the first cylinder and apply a shear transformation to its bottom. The `setShearBottom` method takes a `Vector2` where the X component represents the shear factor along the X‑axis and the Y component along the Y‑axis.

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

> **Pro tip:** The shear factor `0.83` corresponds to roughly 47.5°; adjust this value to achieve the exact angle you need.

## Step 3: Create Cylinder 2 (Standard)

For comparison, we’ll add a second cylinder without any shear. This helps you see the visual difference directly in the exported OBJ file.

```java
// ExStart:5
// Create cylinder 2
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// Add cylinder 2 without a ShearBottom to the scene
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

## Step 4: Save the Scene (How to Save Scene as OBJ)

Finally, we persist the scene to disk. The `FileFormat.WAVEFRONTOBJ` constant tells Aspose to write an OBJ file, which is widely supported by 3D editors like Blender and Maya.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

> **Note:** Replace `"Your Document Directory"` with an absolute or relative path appropriate for your environment.

## Common Issues and Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| **Cylinder appears flat** | Incorrect shear factor (outside 0‑1 range) | Use a value between 0 and 1; adjust gradually while previewing. |
| **OBJ file not loading in viewer** | Missing material definitions | Add a simple material to each node or export as STL for geometry‑only testing. |
| **LicenseException at runtime** | No valid license file | Place `Aspose.3D.lic` in the project root or use `License` class to load it programmatically. |

## Frequently Asked Questions

### Q1: Can I use Aspose.3D for Java with other Java 3D libraries?
**A:** Aspose.3D for Java is designed to work independently. While you can integrate it with other libraries, it provides a complete set of features for most 3D modeling tasks on its own.

### Q2: Is Aspose.3D suitable for beginners in 3D modeling?
**A:** Yes, Aspose.3D offers a user‑friendly API that abstracts low‑level details, making it accessible for both beginners and experienced developers.

### Q3: Where can I find additional support for Aspose.3D for Java?
**A:** Visit the [Aspose.3D forum](https://forum.aspose.com/c/3d/18) for community support, tutorials, and discussions.

### Q4: How can I obtain a temporary license for Aspose.3D?
**A:** You can get a temporary license [here](https://purchase.aspose.com/temporary-license/).

### Q5: Can I buy Aspose.3D for Java?
**A:** Yes, you can purchase Aspose.3D for Java [here](https://purchase.aspose.com/buy).

## Conclusion

We’ve walked through **how to use Aspose** to create two cylinders—one with a sheared bottom and one standard—then saved the result as an OBJ file. This technique is a building block for more sophisticated 3D models, such as custom parts, architectural elements, or game assets. Feel free to experiment with different shear values, radii, and heights to suit your project needs.

---

**Last Updated:** 2025-12-09  
**Tested With:** Aspose.3D for Java 24.11 (latest at time of writing)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}