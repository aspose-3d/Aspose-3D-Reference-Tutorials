---
title: Java 3D Modeling – Sheared Bottom Cylinders with Aspose.3D
linktitle: Java 3D Modeling – Sheared Bottom Cylinders with Aspose.3D
second_title: Aspose.3D Java API
description: Learn java 3d modeling by creating cylinders with a sheared bottom using Aspose.3D for Java. This beginner 3d tutorial shows how to install Aspose 3D, apply shear transformation, and export OBJ file java.
weight: 12
url: /java/cylinders/creating-cylinders-with-sheared-bottom/
date: 2026-01-27
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java 3D Modeling – Sheared Bottom Cylinders with Aspose.3D

## Introduction

Welcome to this **java 3d modeling** tutorial! In this step‑by‑step guide we’ll walk through creating a cylinder whose bottom is sheared, using the Aspose.3D library for Java. Whether you’re following a **beginner 3d tutorial** or looking to add a custom shear transformation to an existing model, you’ll see exactly how to set up the scene, apply the shear, and finally **export OBJ file java** for use in other tools.

## Quick Answers
- **What library is used?** Aspose.3D for Java  
- **Can I install Aspose 3D via Maven?** Yes – add the Aspose.3D dependency to your `pom.xml`  
- **Is a license required for development?** A temporary license is sufficient for testing; a full license is needed for production  
- **Which file format is demonstrated?** Wavefront OBJ (`.obj`)  
- **How long does the example take to run?** Under a second on a typical workstation  

## Prerequisites

Before we begin, ensure you have the following:

- Java Development Kit (JDK) installed on your system.  
- **Install Aspose 3D** – download the library from the official site [here](https://releases.aspose.com/3d/java/).  
- An IDE or build tool (Maven/Gradle) to manage the Aspose.3D dependency.  

## Import Packages

First, import the classes we’ll need for the scene, geometry, and file handling.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Step 1: Create a Scene

A scene is the container for all 3‑D objects. We’ll start by creating an empty scene.

```java
// ExStart:3
// Create a scene
Scene scene = new Scene();
// ExEnd:3
```

## Step 2: Create Cylinder 1 – How to Shear Cylinder

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

## Step 3: Create Cylinder 2 – Standard Cylinder (No Shear)

For comparison, we’ll add a second cylinder that does **not** have a sheared bottom.

```java
// ExStart:5
// Create cylinder 2
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// Add cylinder 2 without a ShearBottom to the scene
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

## Step 4: Save the Scene – Export OBJ File Java

Finally, we export the scene to a Wavefront OBJ file, illustrating **export obj file java** usage.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

## Why This Matters for Java 3D Modeling

Adding a shear to a primitive lets you create more organic shapes without resorting to external modeling tools. This technique is handy for:

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

---

**Last Updated:** 2026-01-27  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
