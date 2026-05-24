---
title: Create 3D Extrusion with Slices – Aspose.3D for Java
linktitle: Create 3D Extrusion with Slices – Aspose.3D for Java
second_title: Aspose.3D Java API
description: Learn how to create 3d extrusion with slices using Aspose.3D for Java. This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting OBJ.
weight: 13
url: /java/linear-extrusion/specifying-slices/
date: 2026-05-24
keywords:
- create 3d extrusion java
- Aspose 3D slices
- linear extrusion Java
schemas:
- type: TechArticle
  headline: Create 3D Extrusion with Slices – Aspose.3D for Java
  description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  dateModified: '2026-05-24'
  author: Aspose
- type: HowTo
  name: Create 3D Extrusion with Slices – Aspose.3D for Java
  description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  steps:
  - name: Set up the scene and define the profile
    text: '`RectangleShape` is a class that defines a 2‑D rectangle profile. First
      we create a `RectangleShape` and give it a **rounding radius** so the corners
      are smooth. `Scene` is the root container for all nodes and geometry. Then we
      initialise a new `Scene` that will hold all geometry.'
  - name: Create child node objects for each extrusion
    text: '`Node` represents an element in the scene graph that can hold geometry
      and transformations. Every piece of geometry lives under a `Node`. Here we generate
      two sibling nodes – one for a low‑slice extrusion and another for a high‑slice
      extrusion – and move the left node a little to the side so the res'
  - name: Perform linear extrusion and set slices
    text: '`LinearExtrusion` is the class that creates a solid by sweeping a profile
      linearly. `LinearExtrusion` is Aspose.3D''s class that generates a solid by
      extruding a 2‑D profile along a straight line. Using an **anonymous inner class**
      we call `setSlices` to control the smoothness. The left node gets onl'
  - name: Export OBJ – save the scene
    text: Finally we write the scene to a Wavefront OBJ file, a format widely supported
      by 3‑D editors and game engines. This demonstrates the **export OBJ Java** capability
      of Aspose.3D.
- type: FAQPage
  questions:
  - question: How can I download Aspose.3D for Java?
    answer: You can download the library [here](https://releases.aspose.com/3d/java/).
  - question: Where can I find the documentation for Aspose.3D?
    answer: Refer to the documentation [here](https://reference.aspose.com/3d/java/).
  - question: Is there a free trial available?
    answer: Yes, you can explore a free trial [here](https://releases.aspose.com/).
  - question: How can I get support for Aspose.3D?
    answer: Visit the support forum [here](https://forum.aspose.com/c/3d/18).
  - question: Can I purchase a temporary license?
    answer: Yes, a temporary license can be obtained [here](https://purchase.aspose.com/temporary-license/).
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Create 3D Extrusion with Slices – Aspose.3D for Java

## Introduction

If you need to **create 3d extrusion** objects that look smooth and precise, controlling the number of slices is the key. In this tutorial we’ll walk through how to specify slices while performing a linear extrusion with Aspose.3D for Java. You’ll see why slice count matters, how to set a rounding radius, and how to export the result as an OBJ file that can be used in any 3‑D pipeline.

## Quick Answers
- **What does “slices” control?** The number of intermediate cross‑sections used to approximate the extrusion surface.  
- **Which method sets the slice count?** `LinearExtrusion.setSlices(int)`  
- **Can I change the rounding radius of the profile?** Yes, via `RectangleShape.setRoundingRadius(double)`  
- **What file format is used in this example?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **Do I need a license to run the code?** A free trial works for evaluation; a commercial license is required for production.

`LinearExtrusion.setSlices(int)` sets how many intermediate slices the extrusion will generate.  
`RectangleShape.setRoundingRadius(double)` defines the corner radius of a rectangular profile.

## How to create 3d extrusion java with slices?

Load your 2‑D profile, choose a slice count, set the rounding radius, and call `save` – the entire workflow fits in a handful of lines. Aspose.3D for Java handles the geometry creation, slice interpolation, and OBJ export automatically, so you can focus on visual quality rather than low‑level mesh calculations.

## What is a linear extrusion with slices?

A linear extrusion with slices turns a flat 2‑D shape into a 3‑D solid by sweeping it along a straight line while generating a configurable number of intermediate cross‑sections. The slice count directly influences how smoothly curved edges, such as rounded corners, are rendered.

## Why use Aspose.3D for Java to create 3d extrusion?

Aspose.3D provides **full programmatic control** over every extrusion parameter, supports **50+ input and output formats** (including OBJ, FBX, STL, and GLTF), and can process **multi‑hundred‑page models** without loading the entire file into memory. It runs on any Java‑enabled platform, requires no native DLLs, and guarantees deterministic results across Windows, Linux, and macOS.

## Prerequisites

1. **Java Development Kit** – JDK 8 or higher installed.  
2. **Aspose.3D for Java** – Download the library from the official site [here](https://releases.aspose.com/3d/java/).  
3. An IDE or text editor of your choice.

## Import Packages

Add the Aspose.3D namespace to your project so you can access the 3‑D modeling classes.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Step‑by‑Step Guide

### Step 1: Set up the scene and define the profile

`RectangleShape` is a class that defines a 2‑D rectangle profile.  
First we create a `RectangleShape` and give it a **rounding radius** so the corners are smooth.  
`Scene` is the root container for all nodes and geometry.  
Then we initialise a new `Scene` that will hold all geometry.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Step 2: Create child node objects for each extrusion

`Node` represents an element in the scene graph that can hold geometry and transformations.  
Every piece of geometry lives under a `Node`. Here we generate two sibling nodes – one for a low‑slice extrusion and another for a high‑slice extrusion – and move the left node a little to the side so the results are easy to compare.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Step 3: Perform linear extrusion and set slices

`LinearExtrusion` is the class that creates a solid by sweeping a profile linearly.  
`LinearExtrusion` is Aspose.3D's class that generates a solid by extruding a 2‑D profile along a straight line. Using an **anonymous inner class** we call `setSlices` to control the smoothness. The left node gets only 2 slices (coarse), while the right node gets 10 slices (smooth).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Step 4: Export OBJ – save the scene

Finally we write the scene to a Wavefront OBJ file, a format widely supported by 3‑D editors and game engines. This demonstrates the **export OBJ Java** capability of Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Common Issues and Solutions

| Issue | Why it Happens | Fix |
|-------|----------------|-----|
| **Extrusion appears flat** | Slice count set to 1 or 0 | Ensure `setSlices` is called with a value ≥ 2. |
| **Rounded corners look jagged** | Rounding radius too small relative to slice count | Increase either the radius or the slice count for smoother curves. |
| **File not found on save** | `MyDir` points to a non‑existent folder | Create the directory beforehand or use an absolute path. |

## Frequently Asked Questions

**Q: How can I download Aspose.3D for Java?**  
A: You can download the library [here](https://releases.aspose.com/3d/java/).

**Q: Where can I find the documentation for Aspose.3D?**  
A: Refer to the documentation [here](https://reference.aspose.com/3d/java/).

**Q: Is there a free trial available?**  
A: Yes, you can explore a free trial [here](https://releases.aspose.com/).

**Q: How can I get support for Aspose.3D?**  
A: Visit the support forum [here](https://forum.aspose.com/c/3d/18).

**Q: Can I purchase a temporary license?**  
A: Yes, a temporary license can be obtained [here](https://purchase.aspose.com/temporary-license/).

---

**Last Updated:** 2026-05-24  
**Tested With:** Aspose.3D for Java 24.11 (latest at time of writing)  
**Author:** Aspose

## Related Tutorials

- [Create 3D Extrusion Java with Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [How to Set Direction in Linear Extrusion with Aspose.3D for Java](/3d/java/linear-extrusion/setting-direction/)
- [Create 3D Scene with Twist in Linear Extrusion – Aspose.3D for Java](/3d/java/linear-extrusion/applying-twist/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}