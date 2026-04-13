---
title: Create 3D Extrusion with Slices – Aspose.3D for Java
linktitle: Create 3D Extrusion with Slices – Aspose.3D for Java
second_title: Aspose.3D Java API
description: Learn how to create 3d extrusion with slices using Aspose.3D for Java. This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting OBJ.
weight: 13
url: /java/linear-extrusion/specifying-slices/
date: 2026-02-22
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Create 3D Extrusion with Slices – Aspose.3D for Java

## Introduction

If you need to **create 3d extrusion** objects that look smooth and precise, controlling the number of slices is the key. In this tutorial we’ll walk through how to specify slices while performing a linear extrusion with Aspose.3D for Java. You’ll see why slice count matters, how to set a rounding radius, and how to export the result as an OBJ file that can be used in any 3D pipeline.

## Quick Answers
- **What does “slices” control?** The number of intermediate cross‑sections used to approximate the extrusion surface.  
- **Which method sets the slice count?** `LinearExtrusion.setSlices(int)`  
- **Can I change the rounding radius of the profile?** Yes, via `RectangleShape.setRoundingRadius(double)`  
- **What file format is used in this example?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **Do I need a license to run the code?** A free trial works for evaluation; a commercial license is required for production.

## What is a linear extrusion with slices?

Linear extrusion takes a 2‑D profile (like a rectangle) and stretches it along a straight line to form a 3‑D solid. By specifying **slices**, you tell Aspose.3D how many intermediate steps to generate, which directly influences the smoothness of curved edges such as a rounded rectangle.

## Why use Aspose.3D for Java to create 3d extrusion?

* **Full control** – You can adjust slice count, rounding radius, and export format programmatically.  
* **Cross‑platform** – Works on any Java‑enabled environment without native dependencies.  
* **Export flexibility** – Directly save to OBJ, FBX, STL, and many other formats.

## Prerequisites

1. **Java Development Kit** – JDK 8 or higher installed.  
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

First we create a `RectangleShape` and give it a **rounding radius** so the corners are smooth. Then we initialise a new `Scene` that will hold all geometry.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Step 2: **Create child node** objects for each extrusion

Every piece of geometry lives under a `Node`. Here we generate two sibling nodes – one for a low‑slice extrusion and another for a high‑slice extrusion – and move the left node a little to the side so the results are easy to compare.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Step 3: Perform linear extrusion and **set slices**

Now we actually **create 3d extrusion** objects. The `LinearExtrusion` constructor takes the profile and the extrusion depth. Using an **anonymous inner class** we call `setSlices` to control the smoothness. The left node gets only 2 slices (coarse), while the right node gets 10 slices (smooth).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Step 4: **Export OBJ** – save the scene

Finally we write the scene to a Wavefront OBJ file, a format widely supported by 3‑D editors and game engines. This demonstrates the **export obj java** capability of Aspose.3D.

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

**Last Updated:** 2026-02-22  
**Tested With:** Aspose.3D for Java 24.11 (latest at time of writing)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}