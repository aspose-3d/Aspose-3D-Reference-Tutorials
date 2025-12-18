---
title: "How to Add Ground Plane and Control Center in Linear Extrusion with Aspose.3D for Java"
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
description: "Learn how to add ground plane and set center property in linear extrusion using Aspose.3D for Java, with step‑by‑step code examples."
weight: 11
url: /java/linear-extrusion/controlling-center/
date: 2025-12-18
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Controlling Center in Linear Extrusion with Aspose.3D for Java

## Introduction

When you’re building 3D scenes in Java, the ability to **add ground plane** while precisely **set center property** on a linear extrusion can make the difference between a flat prototype and a polished visual. In this tutorial we’ll walk through the complete process of controlling the extrusion center and adding a ground plane using Aspose.3D for Java. You’ll see why this matters, how to set it up, and get a ready‑to‑run code sample that you can adapt to your own projects.

## Quick Answers
- **What does “add ground plane” do?** It creates a thin reference geometry that helps you see the extrusion’s position relative to the world axes.  
- **How do I set the center of a linear extrusion?** Use the `setCenter(boolean)` method on the `LinearExtrusion` object.  
- **Do I need a license to run the sample?** A temporary license works for testing; a full license is required for production.  
- **Which file format is used for saving?** The example saves to Wavefront OBJ (`.obj`).  
- **What Java version is required?** Java 8 or later is sufficient.

## What is “add ground plane” in a 3D scene?

Adding a ground plane means inserting a thin rectangular geometry (often a box with minimal thickness) that lies on the X‑Z plane. It acts as a visual floor, making it easier to judge the height and alignment of other objects, especially when you’re experimenting with extrusion centers.

## Why set the center property on a linear extrusion?

By default, a linear extrusion starts from the profile’s origin. Setting the center property (`setCenter(true)`) shifts the profile so that the extrusion is centered around the origin, which is useful for symmetrical designs or when you need consistent alignment across multiple objects.

## Prerequisites

Before we embark on this tutorial journey, make sure you have the following prerequisites in place:

1. **Java Development Environment** – Ensure that you have a Java development environment set up on your machine.  
2. **Aspose.3D for Java** – Download and install the Aspose.3D library. You can find the library and its documentation [here](https://reference.aspose.com/3d/java/).  
3. **Document Directory** – Create a directory to store your Java documents. Let’s call it “Your Document Directory.”

## Import Packages

In your Java development environment, import the necessary packages for Aspose.3D. This ensures that your code has access to the functionalities provided by the library.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Step 1: Set Up the Base Profile

Initialize the base profile to be extruded. In this example, we’ll use a rectangle shape with a rounding radius of 0.3.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Step 2: Create a 3D Scene

Build the foundation of your 3D world by creating a scene.

```java
Scene scene = new Scene();
```

## Step 3: Create Left and Right Nodes

Establish left and right nodes within your scene. These nodes serve as the canvas for your 3D objects.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Step 4: Linear Extrusion with Center Property (Left Node)

Perform linear extrusion on the left node **without centering** and set the number of slices to 3. Notice the `setCenter(false)` call – this is where we **set center property** to *false*.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## Step 5: Add Ground Plane for Reference (Left Node)

Enhance the visual representation by **adding a ground plane** to the left node. The thin box acts as a floor so you can clearly see the extrusion’s height.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## Step 6: Linear Extrusion with Center Property (Right Node)

Now perform linear extrusion on the right node, this time **centering the extrusion**. The `setCenter(true)` call demonstrates how to **set center property** to *true*.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## Step 7: Add Ground Plane for Reference (Right Node)

Just like the left side, add a ground plane to the right node for a consistent visual baseline.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## Step 8: Save the 3D Scene

Save your 3D scene in Wavefront OBJ format so you can view it in any standard 3D viewer.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Common Issues and Solutions

| Issue | Why It Happens | Fix |
|-------|----------------|-----|
| Ground plane not visible | Box thickness is too small for the viewer’s scale. | Increase the thickness (first parameter of `Box`) or zoom out in the viewer. |
| Extrusion appears offset | `setCenter` value not set as intended. | Double‑check the boolean passed to `setCenter`. |
| File not saved | Incorrect directory path or missing write permissions. | Verify `MyDir` points to an existing folder with write access. |

## Frequently Asked Questions

**Q1: Can I use Aspose.3D for Java in commercial projects?**  
A1: Yes, Aspose.3D for Java is available for commercial use. For licensing details, visit [here](https://purchase.aspose.com/buy).

**Q2: Is there a free trial available?**  
A2: Yes, you can explore a free trial of Aspose.3D for Java [here](https://releases.aspose.com/).

**Q3: Where can I find support for Aspose.3D for Java?**  
A3: The Aspose.3D community forum is a great place to seek support and share your experiences. Visit the forum [here](https://forum.aspose.com/c/3d/18).

**Q4: Do I need a temporary license for testing?**  
A4: Yes, if you require a temporary license for testing purposes, you can obtain one [here](https://purchase.aspose.com/temporary-license/).

**Q5: Where can I find the documentation?**  
A5: The documentation for Aspose.3D for Java is available [here](https://reference.aspose.com/3d/java/).

## Conclusion

Controlling the center in linear extrusion **and** learning how to **add ground plane** with Aspose.3D for Java opens up exciting possibilities in 3D graphics development. By following the steps above you now have a reusable pattern for creating centered extrusions, visual reference planes, and exporting the result to OBJ. Feel free to experiment with different profiles, slice counts, and transformations to fit your own project needs.

---

**Last Updated:** 2025-12-18  
**Tested With:** Aspose.3D 24.11 for Java (latest at time of writing)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}