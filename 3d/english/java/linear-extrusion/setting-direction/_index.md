---
date: 2026-08-02
description: Learn how to change extrusion direction in linear extrusion and export
  OBJ files using Aspose.3D for Java. Follow our step‑by‑step guide.
images:
- /java/linear-extrusion/setting-direction/og-image.png
keywords:
- change extrusion direction
- export obj file java
- Aspose.3D Java
lastmod: 2026-08-02
linktitle: Change Extrusion Direction – Aspose.3D Java
og_description: Change extrusion direction in linear extrusion with Aspose.3D for
  Java and export OBJ files. This guide shows step‑by‑step code and tips for developers.
og_image_alt: Guide showing how to change extrusion direction and export OBJ using
  Aspose.3D Java
og_title: Change Extrusion Direction – Aspose.3D Java Tutorial
schemas:
- author: Aspose
  dateModified: '2026-08-02'
  description: Learn how to change extrusion direction in linear extrusion and export
    OBJ files using Aspose.3D for Java. Follow our step‑by‑step guide.
  headline: Change Extrusion Direction in 3D Models – Aspose.3D Java
  type: TechArticle
- questions:
  - answer: '`LinearExtrusion`'
    question: What class performs linear extrusion?
  - answer: '`setDirection(Vector3 direction)`'
    question: Which method sets the extrusion vector?
  - answer: Yes—use `scene.save(..., FileFormat.WAVEFRONTOBJ)`
    question: Can the result be saved as OBJ?
  - answer: A free trial is available; a license is mandatory for commercial use.
    question: Is a license required for production?
  - answer: IntelliJ IDEA and Eclipse are fully supported.
    question: Which IDE works best with Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- change extrusion direction
- Aspose.3D
- Java 3D modeling
- export OBJ
title: Change Extrusion Direction in 3D Models – Aspose.3D Java
url: /java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Change Extrusion Direction in 3D Models – Aspose.3D Java

## Introduction

In this comprehensive tutorial you’ll discover **how to change extrusion direction** when performing a linear extrusion with Aspose.3D for Java. Whether you’re building a CAD‑like tool, preparing assets for a game engine, or generating parts for 3‑D printing, controlling the extrusion direction lets you create exactly the shape you need. We’ll walk through each step, from initializing a profile to saving the result as an OBJ file, so you can also **export 3D model OBJ** files directly from Java.

## Quick Answers
- **What class performs linear extrusion?** `LinearExtrusion`
- **Which method sets the extrusion vector?** `setDirection(Vector3 direction)`
- **Can the result be saved as OBJ?** Yes—use `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **Is a license required for production?** A free trial is available; a license is mandatory for commercial use.
- **Which IDE works best with Aspose.3D?** IntelliJ IDEA and Eclipse are fully supported.

## What is Linear Extrusion?

Linear extrusion is the process of extending a 2‑D sketch (such as a rectangle or circle) along a straight line to generate a 3‑D solid. By default the extrusion follows the positive Z‑axis, but Aspose.3D lets you change that path with the `setDirection` property, giving you full control over the final geometry.

## Why Change Extrusion Direction in Linear Extrusion?

Changing the extrusion direction lets you align new geometry with existing objects, create angled components without extra transforms, and generate models that match the coordinate system required by downstream pipelines (e.g., 3‑D printers or game engines). This eliminates the need for post‑processing steps and reduces file‑size overhead by up to 15 % when using directional vectors that avoid unnecessary rotations.

## Prerequisites

Before we dive in, make sure you have:

- Basic knowledge of Java.
- Aspose.3D library installed. You can download it from [here](https://releases.aspose.com/3d/java/). You can also browse all Aspose releases at the main page [here](https://releases.aspose.com/).
- An IDE such as Eclipse or IntelliJ IDEA.

## Import Packages

The `com.aspose.threed` namespace provides the core 3‑D classes and utility types.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Step 1: Initialize Base Profile

The `RectangleShape` class creates the 2‑D profile that will be extruded. A small rounding radius gives the edges a smooth look.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Step 2: Create a Scene

The `Scene` class is Aspose.3D's top‑level container that holds all 3‑D nodes, lights, cameras, and materials.

```java
Scene scene = new Scene();
```

## Step 3: Create Nodes

A `Node` represents an object in the scene graph, allowing you to attach geometry, transforms, and other properties.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Step 4: Perform Linear Extrusion on the Left Node

`LinearExtrusion` performs the extrusion operation, converting a 2‑D profile into a 3‑D mesh.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Step 5: Perform Linear Extrusion on the Right Node with Direction

Here we **change extrusion direction**. By passing a custom `Vector3` to `setDirection`, the extrusion follows the vector (0.3, 0.2, 1), producing a slanted shape that aligns with the scene’s coordinate system.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Step 6: Save 3D Scene

The `save` method writes the scene to a file in the specified format.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Common Issues and Solutions

| Issue | Why it Happens | Fix |
|-------|----------------|-----|
| OBJ file appears empty | The profile was not added to a node | Ensure `createChildNode` is called on a valid node |
| Direction seems unchanged | `setDirection` was called after the extrusion was already constructed | Set direction inside the `LinearExtrusion` initializer as shown |
| Low‑resolution mesh | `setSlices` value is too low | Increase the slice count (e.g., 100 or more) |

## Conclusion

You now know **how to change extrusion direction** in a linear extrusion, how to tweak twist and slice settings, and how to **export 3D model OBJ** files using Aspose.3D for Java. These techniques give you fine‑grained control over geometry creation and make it straightforward to integrate 3‑D assets into larger pipelines.

## Frequently Asked Questions

**Q:** Can I use Aspose.3D with other programming languages?  
**A:** Yes—Aspose.3D provides APIs for .NET and Java, allowing cross‑platform development.

**Q:** Is there a free trial available for Aspose.3D?  
**A:** Absolutely. You can explore the full feature set with a free trial [here](https://releases.aspose.com/).

**Q:** Where can I find detailed documentation for Aspose.3D for Java?  
**A:** The comprehensive reference is available [here](https://reference.aspose.com/3d/java/).

**Q:** How do I get support for Aspose.3D?  
**A:** Visit the official [Aspose.3D forum](https://forum.aspose.com/c/3d/18) for assistance from the community and product team.

**Q:** Are temporary licenses available for testing?  
**A:** Yes—temporary licenses can be obtained [here](https://purchase.aspose.com/temporary-license/).

---

**Last Updated:** 2026-08-02  
**Tested With:** Aspose.3D for Java (latest release)  
**Author:** Aspose

{{< blocks/products/products-backtop-button >}}

## Related Tutorials

- [How to Extrude Shape - Creating 3D Models with Linear Extrusion in Java](/3d/java/linear-extrusion/)
- [Create 3D Extrusion Java with Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Java 3D Graphics Tutorial – Center in Linear Extrusion](/3d/java/linear-extrusion/controlling-center/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}