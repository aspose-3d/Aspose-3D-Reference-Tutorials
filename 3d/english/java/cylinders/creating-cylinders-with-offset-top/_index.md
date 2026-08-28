---
date: 2026-08-12
description: How to generate 3d using Aspose.3D – create a cylinder with offset top
  in Java, add child node, set offset top, generate 3D model, export OBJ, and evaluate
  with a temporary license.
images:
- /java/cylinders/creating-cylinders-with-offset-top/og-image.png
keywords:
- how to generate 3d
- aspose temporary license
- export obj file
- set offset top
- java 3d cylinder
lastmod: 2026-08-12
linktitle: How to generate 3d – create cylinder with offset top (Java)
og_description: How to generate 3d with Aspose.3D for Java. Learn to offset cylinder
  tops, add child nodes, and export OBJ using a temporary license.
og_image_alt: Guide showing Java code to create a cylinder with offset top and export
  OBJ using Aspose.3D
og_title: How to generate 3d – create cylinder with offset top (Java)
schemas:
- author: Aspose
  dateModified: '2026-08-12'
  description: How to generate 3d using Aspose.3D – create a cylinder with offset
    top in Java, add child node, set offset top, generate 3D model, export OBJ, and
    evaluate with a temporary license.
  headline: How to generate 3d – create cylinder with offset top (Java)
  type: TechArticle
- description: How to generate 3d using Aspose.3D – create a cylinder with offset
    top in Java, add child node, set offset top, generate 3D model, export OBJ, and
    evaluate with a temporary license.
  name: How to generate 3d – create cylinder with offset top (Java)
  steps:
  - name: Create a Java 3D scene
    text: '`Scene` is the top‑level container that holds all nodes, meshes, lights,
      and cameras in a 3‑D environment.'
  - name: Initialize cylinder with offset top
    text: '`Cylinder` represents a cylindrical mesh and provides properties such as
      radius, height, and offset.'
  - name: Add child node Java – attach the first cylinder
    text: '`Node` is an element in the scene graph that can hold geometry and transformations.'
  - name: Java export OBJ – save the scene as OBJ
    text: '`FileFormat` enumerates the supported export formats such as OBJ, STL,
      and FBX.'
  type: HowTo
- questions:
  - answer: Yes, it works seamlessly with Eclipse, IntelliJ IDEA, NetBeans, and other
      IDEs.
    question: Is Aspose.3D compatible with different Java IDEs?
  - answer: Absolutely! Use the `Material` class to assign textures and surface properties.
    question: Can I apply textures to the created 3D objects?
  - answer: Various licensing models are available; you can explore them **[Aspose
      purchase page](https://purchase.aspose.com/buy)**.
    question: Are there licensing options for Aspose.3D?
  - answer: Join the **[Aspose.3D community forum](https://forum.aspose.com/c/3d/18)**
      for support and discussion.
    question: How can I get help or share experiences?
  - answer: Yes, an **aspose temporary license** can be obtained for evaluation **[temporary
      license request page](https://purchase.aspose.com/temporary-license/)**.
    question: Is a temporary license available for testing?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- generate 3d
- aspose.3d
- java cylinder offset
title: How to generate 3d – create cylinder with offset top (Java)
url: /java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# How to generate 3d – create cylinder with offset top (Java)

## Introduction

If you’re looking to **create cylinder** objects with a custom offset top in a Java‑based 3D scene, Aspose.3D makes the process straightforward. In this tutorial we’ll walk through every step—from setting up the scene to exporting the final model as an OBJ file—so you can integrate offset‑top cylinders into your applications with confidence. By the end of the guide you’ll also understand how an **aspose temporary license** lets you evaluate these features without a full purchase.

## Quick answers
- **What library is used?** Aspose.3D for Java  
- **Can I offset the top of a cylinder?** Yes, via `setOffsetTop`  
- **How do I add a child node in Java?** Call `createChildNode` on the root node  
- **Which format can I export to?** Wavefront OBJ (`export obj file`)  
- **Do I need a license for testing?** An **aspose temporary license** is available for evaluation  

## What is Aspose temporary license?

An **aspose temporary license** is a short‑term, free evaluation key that unlocks the full feature set of Aspose.3D for Java during development and testing. It removes evaluation watermarks and allows you to generate 3D model files, such as OBJ, STL, or FBX, exactly as a paid license would.

## Why use Aspose.3D for Java?

Aspose.3D provides a high‑level, cross‑platform API that simplifies 3D creation and export. It includes built‑in exporters for more than 30 formats, supports scene‑graph hierarchies, and lets you focus on geometry rather than low‑level mesh handling.

- **High‑level API:** No need to manage low‑level mesh data.  
- **Cross‑platform:** Works on any JVM‑compatible environment.  
- **Built‑in exporters:** Directly save to OBJ, STL, FBX, and more—Aspose.3D supports **30+** export formats.  
- **Extensible:** Easily add child nodes, apply transformations, and integrate with other Java libraries.  

## Prerequisites

Before we dive in, make sure you have:

- **Java Development Kit (JDK)** – a compatible version installed.  
- **Aspose.3D for Java library** – download the latest JAR from the official site **[Aspose.3D for Java download page](https://releases.aspose.com/3d/java/)**.  
- An IDE of your choice (Eclipse, IntelliJ IDEA, NetBeans, etc.).  

## Import packages

The following imports bring in the essential Aspose.3D classes needed to create and export a cylinder.

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Step‑by‑step guide

### Step 1: Create a Java 3D scene

`Scene` is the top‑level container that holds all nodes, meshes, lights, and cameras in a 3‑D environment.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### Step 2: Initialize cylinder with offset top

`Cylinder` represents a cylindrical mesh and provides properties such as radius, height, and offset.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### Step 3: Add child node Java – attach the first cylinder

`Node` is an element in the scene graph that can hold geometry and transformations.

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### Step 4: Initialize a second cylinder (no offset)

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### Step 5: Add child node Java – attach the second cylinder

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Step 6: Java export OBJ – save the scene as OBJ

`FileFormat` enumerates the supported export formats such as OBJ, STL, and FBX.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

## How to generate 3d model and export OBJ in Java

To generate a 3D model, load the scene, apply any required transformations, and then call `scene.save("path/CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ)`. The **aspose temporary license** removes the evaluation watermark, allowing you to produce production‑ready OBJ files without purchasing a full license.

## Real‑world use cases

- **Architectural visualisation:** Offset‑top cylinders model columns that taper toward the ceiling.  
- **Mechanical parts:** Create pistons or gear housings where the top surface is intentionally shifted.  
- **Game assets:** Produce varied pillar shapes on the fly, reducing the need for hand‑crafted meshes.

## Common issues and solutions

| Issue | Reason | Fix |
|-------|--------|-----|
| **OBJ file is empty** | Scene not saved correctly or wrong path. | Verify the output directory exists and you have write permissions. |
| **Offset not applied** | Using an older Aspose.3D version. | Update to the latest library where `setOffsetTop` is supported. |
| **Child node not visible** | Transformation not applied. | Ensure you call `getTransform().setTranslation` after creating the child node. |

## Frequently asked questions

**Q: Is Aspose.3D compatible with different Java IDEs?**  
A: Yes, it works seamlessly with Eclipse, IntelliJ IDEA, NetBeans, and other IDEs.

**Q: Can I apply textures to the created 3D objects?**  
A: Absolutely! Use the `Material` class to assign textures and surface properties.

**Q: Are there licensing options for Aspose.3D?**  
A: Various licensing models are available; you can explore them **[Aspose purchase page](https://purchase.aspose.com/buy)**.

**Q: How can I get help or share experiences?**  
A: Join the **[Aspose.3D community forum](https://forum.aspose.com/c/3d/18)** for support and discussion.

**Q: Is a temporary license available for testing?**  
A: Yes, an **aspose temporary license** can be obtained for evaluation **[temporary license request page](https://purchase.aspose.com/temporary-license/)**.

---

**Last updated:** 2026-08-12  
**Tested with:** Aspose.3D for Java 24.12 (latest)  
**Author:** Aspose

---

{{< blocks/products/products-backtop-button >}}

## Related Tutorials

- [How to Create Cylinder Models with Aspose.3D for Java](/3d/java/cylinders/)
- [How to create cylinder fan shape using Aspose.3D for Java](/3d/java/cylinders/creating-fan-cylinders/)
- [Create Child Nodes and Export FBX in Java with Aspose.3D](/3d/java/geometry/build-node-hierarchies/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}