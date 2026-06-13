---
title: "Create 3D Mesh Java – Center in Linear Extrusion"
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
description: "Learn a java 3d graphics tutorial on controlling the center in linear extrusion with Aspose.3D, including how to set rounding radius and save OBJ file java."
weight: 11
url: /java/linear-extrusion/controlling-center/
date: 2026-06-13
keywords:
- create 3d mesh java
- set rounding radius
- export 3d model obj
- save obj file java
- aspose 3d export obj
schemas:
- type: TechArticle
  headline: Create 3D Mesh Java – Center in Linear Extrusion
  description: Learn a java 3d graphics tutorial on controlling the center in linear
    extrusion with Aspose.3D, including how to set rounding radius and save OBJ file
    java.
  dateModified: '2026-06-13'
  author: Aspose
- type: HowTo
  name: Create 3D Mesh Java – Center in Linear Extrusion
  description: Learn a java 3d graphics tutorial on controlling the center in linear
    extrusion with Aspose.3D, including how to set rounding radius and save OBJ file
    java.
  steps:
  - name: Set Up the Base Profile
    text: First, create the 2‑D shape that will be extruded. Here we use a rectangle
      and **set rounding radius** to 0.3, which smooths the corners and demonstrates
      how to **round extrusion corners**.
  - name: Create a 3D Scene
    text: '**Scene** is the top‑level container that holds all 3‑D objects, lights,
      and cameras.'
  - name: Add Left and Right Nodes
    text: A **Node** represents a transformable object in the scene graph, allowing
      positioning and hierarchy.
  - name: Linear Extrusion – No Center (Left Node)
    text: '**LinearExtrusion** converts a 2‑D profile into a 3‑D mesh by sweeping
      it along a straight line. **setCenter(boolean)** toggles whether the extrusion
      is centered around the profile origin.'
  - name: Add a Ground Plane for Reference (Left Node)
    text: A thin box acts as a visual floor, helping you see the extrusion’s orientation.
  - name: Linear Extrusion – Centered (Right Node)
    text: Now repeat the extrusion, this time enabling `center`. The geometry will
      be symmetric around the profile’s origin, giving you a perfectly balanced **create
      3d mesh java** result.
  - name: Add a Ground Plane for Reference (Right Node)
    text: Same ground plane for the right side, making the comparison clear.
  - name: Save the 3D Scene
    text: Finally, export the entire scene to a Wavefront OBJ file – a format readily
      usable in most 3‑D editors. The `save` method automatically converts the mesh
      to the OBJ specification, allowing you to **save obj file java** without additional
      post‑processing.
- type: FAQPage
  questions:
  - question: What does the center property do?
    answer: It determines whether the extrusion is symmetric around the profile's
      origin.
  - question: Do I need a license to run the code?
    answer: A temporary license works for testing; a full license is required for
      production.
  - question: Which file format is used for the result?
    answer: The scene is saved as a Wavefront OBJ file.
  - question: Can I change the number of slices?
    answer: Yes, use `setSlices(int)` on the `LinearExtrusion` object.
  - question: Is Aspose.3D compatible with Java 8+?
    answer: Absolutely – it supports all modern Java versions.
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Create 3D Mesh Java – Center in Linear Extrusion

## Introduction

If you're building 3‑D visualizations in Java, mastering extrusion techniques is essential. This **java 3d graphics tutorial** shows you how to **create 3d mesh java** objects by controlling the center of a linear extrusion with Aspose.3D for Java. By the end of this guide you’ll understand why the `center` property matters, how to **set rounding radius**, and how to **save obj file java**‑compatible output. You’ll also see how to **export 3d model obj** for use in any major 3‑D editor.

## Quick Answers
- **What does the center property do?** It determines whether the extrusion is symmetric around the profile's origin.  
- **Do I need a license to run the code?** A temporary license works for testing; a full license is required for production.  
- **Which file format is used for the result?** The scene is saved as a Wavefront OBJ file.  
- **Can I change the number of slices?** Yes, use `setSlices(int)` on the `LinearExtrusion` object.  
- **Is Aspose.3D compatible with Java 8+?** Absolutely – it supports all modern Java versions.

## What is a java 3d graphics tutorial?

A **java 3d graphics tutorial** is a step‑by‑step guide that teaches you how to use Java libraries to create, manipulate, and render three‑dimensional objects. In this tutorial you will learn to **create 3d mesh java** by converting a 2‑D profile into a full 3‑D model, control its central alignment, round extrusion corners, and finally export the result as an OBJ file that any 3‑D program can read.

## Why use Aspose.3D for Java?

Aspose.3D for Java provides a high‑level API that eliminates the need for manual mesh calculations, letting you focus on design rather than low‑level geometry. It supports **50+ input and output formats**—including OBJ, FBX, STL, and GLTF—so you can **export 3d model obj** or any other format with a single method call. The library processes multi‑hundred‑page scenes without loading the entire file into memory, delivering **up to 3× faster performance** compared with raw OpenGL pipelines on typical server hardware.

## Prerequisites

Before we dive in, ensure you have:

1. **Java Development Environment** – JDK 8 or newer installed.  
2. **Aspose.3D for Java** – Download the library and documentation [here](https://reference.aspose.com/3d/java/).  
3. **Document Directory** – Create a folder on your machine to store generated files; we’ll refer to it as **“Your Document Directory.”**

## Import Packages

In your Java IDE, import the Aspose.3D classes you’ll need. This gives the compiler access to the extrusion and scene‑building features.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Step‑by‑Step Guide

### Step 1: Set Up the Base Profile

First, create the 2‑D shape that will be extruded. Here we use a rectangle and **set rounding radius** to 0.3, which smooths the corners and demonstrates how to **round extrusion corners**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### Step 2: Create a 3D Scene

**Scene** is the top‑level container that holds all 3‑D objects, lights, and cameras.

```java
Scene scene = new Scene();
```

### Step 3: Add Left and Right Nodes

A **Node** represents a transformable object in the scene graph, allowing positioning and hierarchy.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Step 4: Linear Extrusion – No Center (Left Node)

**LinearExtrusion** converts a 2‑D profile into a 3‑D mesh by sweeping it along a straight line.  
**setCenter(boolean)** toggles whether the extrusion is centered around the profile origin.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

### Step 5: Add a Ground Plane for Reference (Left Node)

A thin box acts as a visual floor, helping you see the extrusion’s orientation.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

### Step 6: Linear Extrusion – Centered (Right Node)

Now repeat the extrusion, this time enabling `center`. The geometry will be symmetric around the profile’s origin, giving you a perfectly balanced **create 3d mesh java** result.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

### Step 7: Add a Ground Plane for Reference (Right Node)

Same ground plane for the right side, making the comparison clear.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

### Step 8: Save the 3D Scene

Finally, export the entire scene to a Wavefront OBJ file – a format readily usable in most 3‑D editors. The `save` method automatically converts the mesh to the OBJ specification, allowing you to **save obj file java** without additional post‑processing.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Common Issues and Solutions

| Issue | Why it Happens | Fix |
|-------|----------------|-----|
| **Extrusion appears offset** | `setCenter(false)` leaves the profile anchored at its corner. | Use `setCenter(true)` for symmetric results. |
| **OBJ file is empty** | Output directory path is incorrect or missing write permissions. | Verify `MyDir` points to an existing folder and the application has write access. |
| **Rounded corners look sharp** | Rounding radius is too small relative to rectangle size. | Increase the radius value (e.g., `setRoundingRadius(0.5)`). |

## Frequently Asked Questions

### Q1: Can I use Aspose.3D for Java in commercial projects?

A1: Yes, Aspose.3D for Java is available for commercial use. For licensing details, visit [here](https://purchase.aspose.com/buy).

### Q2: Is there a free trial available?

A2: Yes, you can explore a free trial of Aspose.3D for Java [here](https://releases.aspose.com/).

### Q3: Where can I find support for Aspose.3D for Java?

A3: The Aspose.3D community forum is a great place to seek support and share your experiences. Visit the forum [here](https://forum.aspose.com/c/3d/18).

### Q4: Do I need a temporary license for testing?

A4: Yes, if you require a temporary license for testing purposes, you can obtain one [here](https://purchase.aspose.com/temporary-license/).

### Q5: Where can I find the documentation?

A5: The documentation for Aspose.3D for Java is available [here](https://reference.aspose.com/3d/java/).

## Conclusion

By completing this **java 3d graphics tutorial**, you now know how to **create 3d mesh java** objects, control the center of a linear extrusion, adjust the rounding radius, and **save obj file java** output using Aspose.3D. These techniques give you fine‑grained control over mesh symmetry, which is vital for game assets, CAD prototypes, and scientific visualizations. Feel free to experiment with different profiles, slice counts, and export formats to expand your 3‑D toolbox.

---

**Last Updated:** 2026-06-13  
**Tested With:** Aspose.3D for Java 24.11  
**Author:** Aspose

## Related Tutorials

- [Create 3D Extrusion Java with Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [How to Set Direction in Linear Extrusion with Aspose.3D for Java](/3d/java/linear-extrusion/setting-direction/)
- [Create 3D Scene with Twist in Linear Extrusion – Aspose.3D for Java](/3d/java/linear-extrusion/applying-twist/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}