---
title: "Create 3D Scene – Set Extrusion Direction Aspose.3D Java"
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
description: "Learn how to create 3d scene and save obj file using Aspose.3D for Java. Follow our step‑by‑step guide for linear extrusion direction."
weight: 12
url: /java/linear-extrusion/setting-direction/
date: 2025-12-18
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Create 3D Scene – Set Extrusion Direction Aspose.3D Java

## Introduction

In this tutorial you’ll learn **how to create 3d scene** objects and control the extrusion direction with Aspose.3D for Java. Whether you’re building architectural visualizations, product prototypes, or game assets, mastering linear extrusion gives you the flexibility to model complex shapes quickly. We’ll walk through every step, from adding nodes in Java to **export 3d model obj** files, so you can see the result instantly.

## Quick Answers
- **What does “create 3d scene” mean?** It means initializing an Aspose.3D `Scene` object that will hold all geometry, lights, and cameras.  
- **How do I set extrusion direction?** Use the `setDirection(Vector3)` method on a `LinearExtrusion` instance.  
- **Which format should I use to export?** The OBJ format (`FileFormat.WAVEFRONTOBJ`) is widely supported for 3‑D workflows.  
- **Do I need a license for Aspose.3D?** A free trial works for development; a commercial license is required for production.  
- **Can I add more nodes in Java?** Yes—use `scene.getRootNode().createChildNode()` to add as many objects as needed.

## What is a “create 3d scene” workflow?

A **create 3d scene** workflow starts with an empty `Scene` object, adds geometry (like extruded profiles), positions it with transforms, and finally saves the scene to a file format such as OBJ. This pattern is the backbone of most 3‑D applications built with Aspose.3D.

## Why set extrusion direction?

Setting the extrusion direction lets you tilt, rotate, or skew the shape while it’s being extruded, giving you control over the final geometry without extra post‑processing. It’s especially useful for:

- Creating tapered columns or custom‑shaped pipes.  
- Aligning extrusions with non‑standard axes in mechanical parts.  
- Generating artistic shapes for visual effects.

## Prerequisites

Before we dive in, make sure you have:

- Basic Java knowledge.  
- Aspose.3D library installed – download it from [here](https://releases.aspose.com/3d/java/).  
- An IDE such as Eclipse or IntelliJ IDEA.

## Import Packages

First, import the required Aspose.3D classes:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Step 1: Initialize Base Profile

Create the 2‑D profile that will be extruded. In this example we use a rounded rectangle:

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

> **Pro tip:** Adjust the rounding radius to control how sharp or smooth the rectangle corners appear before extrusion.

## Step 2: Create a Scene

Now we **create 3d scene** that will host our objects:

```java
Scene scene = new Scene();
```

## Step 3: Add Nodes Java – Positioning the Objects

We’ll add two child nodes (left and right) to the scene’s root node and move the left one a little to the side:

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Step 4: How to extrude – Left Node (default direction)

Extrude the profile on the left node using the default Z‑axis direction. We also set a full 360° twist and increase slice count for smoothness:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Step 5: How to set direction – Right Node

Here we **how to set direction** by providing a custom `Vector3`. This tilts the extrusion toward the vector (0.3, 0.2, 1):

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Step 6: Save OBJ file – Export 3D model

Finally, we **save obj file** to see the result in any 3‑D viewer:

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

When you open the generated OBJ file, you’ll see two extruded rectangles: one with the default direction and one tilted according to the vector we set.

## Common Issues and Solutions

| Issue | Reason | Fix |
|-------|--------|-----|
| OBJ file appears empty | Scene not saved or path incorrect | Verify `MyDir` points to a writable folder and the file name ends with `.obj`. |
| Extrusion looks flat | `setSlices` too low | Increase `setSlices` (e.g., 200) for smoother geometry. |
| Direction seems unchanged | Vector not normalized | Use a normalized `Vector3` or adjust values to reflect the desired tilt. |

## Frequently Asked Questions

### Q1: Can I use Aspose.3D with other programming languages?
A1: Aspose.3D supports various languages, including .NET and Java.

### Q2: Is there a free trial available for Aspose.3D?
A2: Yes, you can explore the features of Aspose.3D with a free trial [here](https://releases.aspose.com/).

### Q3: Where can I find detailed documentation for Aspose.3D for Java?
A3: The comprehensive documentation is available [here](https://reference.aspose.com/3d/java/).

### Q4: How can I get support for Aspose.3D?
A4: Visit the [Aspose.3D forum](https://forum.aspose.com/c/3d/18) for any assistance or queries.

### Q5: Are temporary licenses available for Aspose.3D?
A5: Yes, you can obtain a temporary license [here](https://purchase.aspose.com/temporary-license/).

---

**Last Updated:** 2025-12-18  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}