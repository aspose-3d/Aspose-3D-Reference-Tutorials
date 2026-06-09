---
title: Aspose Temporary License – Create Cylinder with Offset Top (Java)
linktitle: Aspose Temporary License – Create Cylinder with Offset Top (Java)
second_title: Aspose.3D Java API
description: Learn how to create a cylinder with offset top in Aspose.3D for Java, add child node Java, set offset top, generate 3D model, and export OBJ using an Aspose temporary license.
weight: 11
url: /java/cylinders/creating-cylinders-with-offset-top/
date: 2026-04-08
keywords:
- aspose temporary license
- generate 3d model
- add child node java
- java export obj
- set offset top
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose Temporary License – Create Cylinder with Offset Top (Java)

## Introduction

If you’re looking to **create cylinder** objects with a custom offset top in a Java‑based 3D scene, Aspose.3D makes the process straightforward. In this tutorial we’ll walk through every step—from setting up the scene to exporting the final model as an OBJ file—so you can integrate offset‑top cylinders into your applications with confidence. By the end of the guide you’ll also understand how an **aspose temporary license** lets you evaluate these features without a full purchase.

## Quick Answers
- **What library is used?** Aspose.3D for Java  
- **Can I offset the top of a cylinder?** Yes, using `setOffsetTop`  
- **How do I add a child node in Java?** Call `createChildNode` on the root node  
- **Which format can I export to?** Wavefront OBJ (`java export obj`)  
- **Do I need a license for testing?** An **aspose temporary license** is available for evaluation  

## What is Aspose Temporary License?

An **aspose temporary license** is a short‑term, free evaluation key that unlocks the full feature set of Aspose.3D for Java during development and testing. It removes evaluation watermarks and allows you to generate 3D model files, such as OBJ, STL, or FBX, exactly as a paid license would.

## Why Use Aspose.3D for Java?

- **High‑level API:** No need to manage low‑level mesh data.  
- **Cross‑platform:** Works on any JVM‑compatible environment.  
- **Built‑in exporters:** Directly save to OBJ, STL, FBX, and more.  
- **Extensible:** Easily add child nodes, apply transformations, and integrate with other Java libraries.  

## Prerequisites

Before we dive in, make sure you have:

- **Java Development Kit (JDK)** – a compatible version installed.  
- **Aspose.3D for Java library** – download the latest JAR from the official site [here](https://releases.aspose.com/3d/java/).  
- An IDE of your choice (Eclipse, IntelliJ IDEA, NetBeans, etc.).  

## Import Packages

First, import the classes we’ll need. Place these statements at the top of your Java file:

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Step‑by‑Step Guide

### Step 1: Create a Java 3D Scene

A **java 3d scene** acts as the container for all 3D objects.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### Step 2: Initialize Cylinder with Offset Top

Here we answer **how to create cylinder** with a custom offset. The constructor defines radius, height, slices, stacks, and whether the cylinder is closed. After that, we shift the top using `setOffsetTop`.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### Step 3: Add Child Node Java – Attach the First Cylinder

We create a child node under the scene’s root node and move the cylinder to a desired location.

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### Step 4: Initialize a Second Cylinder (No Offset)

For comparison, we add a regular cylinder without an offset.

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### Step 5: Add Child Node Java – Attach the Second Cylinder

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Step 6: Java Export OBJ – Save the Scene as OBJ

Finally, we **java export obj** the whole scene (both cylinders) as a Wavefront OBJ file, which is widely supported by 3D tools.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

When you run the program, you’ll find `CustomizedOffsetTopCylinder.obj` in the specified directory, ready to be opened in Blender, Maya, or any other OBJ‑compatible viewer.

## How to Generate 3D Model and Export OBJ in Java

The combination of `Scene.save(..., FileFormat.WAVEFRONTOBJ)` and the **aspose temporary license** lets you **generate 3d model** files quickly, without needing external converters. This is especially handy during prototyping or when sharing assets with designers.

## Real‑World Use Cases

- **Architectural visualisation:** Offset‑top cylinders model columns that taper toward the ceiling.  
- **Mechanical parts:** Create pistons or gear housings where the top surface is intentionally shifted.  
- **Game assets:** Produce varied pillar shapes on the fly, reducing the need for hand‑crafted meshes.

## Common Issues and Solutions

| Issue | Reason | Fix |
|-------|--------|-----|
| **OBJ file is empty** | Scene not saved correctly or wrong path. | Verify the output directory exists and you have write permissions. |
| **Offset not applied** | Using an older Aspose.3D version. | Update to the latest library where `setOffsetTop` is supported. |
| **Child node not visible** | Transformation not applied. | Ensure you call `getTransform().setTranslation` after creating the child node. |

## Frequently Asked Questions

**Q: Is Aspose.3D compatible with different Java IDEs?**  
A: Yes, it works seamlessly with Eclipse, IntelliJ IDEA, NetBeans, and other IDEs.

**Q: Can I apply textures to the created 3D objects?**  
A: Absolutely! Use the `Material` class to assign textures and surface properties.

**Q: Are there licensing options for Aspose.3D?**  
A: Various licensing models are available; you can explore them [here](https://purchase.aspose.com/buy).

**Q: How can I get help or share experiences?**  
A: Join the Aspose.3D community forum [here](https://forum.aspose.com/c/3d/18) for support and discussion.

**Q: Is a temporary license available for testing?**  
A: Yes, an **aspose temporary license** can be obtained for evaluation [here](https://purchase.aspose.com/temporary-license/).

---

**Last Updated:** 2026-04-08  
**Tested With:** Aspose.3D for Java 24.12 (latest)  
**Author:** Aspose

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
