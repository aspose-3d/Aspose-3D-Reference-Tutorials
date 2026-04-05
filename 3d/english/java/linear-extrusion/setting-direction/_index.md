---
title: How to Set Direction in Linear Extrusion with Aspose.3D for Java
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
description: Learn how to set direction in linear extrusion and export 3d model obj using Aspose.3D for Java. Follow our step‑by‑step guide.
weight: 12
url: /java/linear-extrusion/setting-direction/
date: 2026-02-22
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# How to Set Direction in Linear Extrusion with Aspose.3D for Java

## Introduction

In this comprehensive tutorial you’ll discover **how to set direction** when performing a linear extrusion with Aspose.3D for Java. Whether you’re building a CAD‑like tool or generating geometry for a game engine, controlling the extrusion direction lets you create exactly the shape you need. We’ll walk through each step, from initializing a profile to saving the result as an OBJ file, so you can also **export 3d model obj** files directly from Java.

## Quick Answers
- **What is the primary class for linear extrusion?** `LinearExtrusion`
- **Which method defines extrusion direction?** `setDirection(Vector3 direction)`
- **Can I export the result as OBJ?** Yes, using `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **Do I need a license for development?** A free trial is available; a license is required for production.
- **What Java IDE works best?** IntelliJ IDEA or Eclipse are both fully supported.

## What is Linear Extrusion?

Linear extrusion takes a 2‑D profile (such as a rectangle or circle) and extends it along a straight line to create a 3‑D solid. By default the extrusion follows the positive Z‑axis, but Aspose.3D lets you change that path with the `setDirection` property.

## Why Set Direction in Linear Extrusion?

Setting a custom direction is useful when:
- Aligning geometry with existing objects in a scene.
- Creating slanted or angled parts without extra transformation steps.
- Exporting models that must match a specific coordinate system (e.g., for 3‑D printing or game engines).

## Prerequisites

Before we dive in, make sure you have:

- Basic knowledge of Java.
- Aspose.3D library installed. You can download it from [here](https://releases.aspose.com/3d/java/).
- An IDE such as Eclipse or IntelliJ IDEA.

## Import Packages

First, import the namespaces that provide the core 3‑D classes and utility types.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Step 1: Initialize Base Profile

Create the shape that will be extruded. In this example we use a `RectangleShape` with a small rounding radius to give the edges a smooth look.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Step 2: Create a Scene

A `Scene` object acts as a container for all 3‑D nodes, lights, cameras, and materials.

```java
Scene scene = new Scene();
```

## Step 3: Create Nodes

Add two child nodes to the scene root—one for the left‑hand extrusion and one for the right‑hand extrusion. The right node is translated so the two objects don’t overlap.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Step 4: Perform Linear Extrusion on the Left Node

Extrude the profile on the left node using the default Z‑axis direction. We also add a full 360° twist and increase the slice count for a smoother mesh.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Step 5: Perform Linear Extrusion on the Right Node with Direction

Here’s where we **set direction**. By passing a custom `Vector3` to `setDirection`, the extrusion follows the vector (0.3, 0.2, 1), producing a slanted shape.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Step 6: Save 3D Scene

Finally, export the scene to the Wavefront OBJ format. This step demonstrates how to **save obj file java** projects and makes it easy to view the result in any 3‑D viewer.

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

You now know **how to set direction** in a linear extrusion, how to tweak twist and slice settings, and how to **export 3d model obj** files using Aspose.3D for Java. These techniques give you fine‑grained control over geometry creation and make it straightforward to integrate 3‑D assets into larger pipelines.

## FAQ's

### Q1: Can I use Aspose.3D with other programming languages?

A1: Aspose.3D supports various programming languages, including .NET and Java.

### Q2. Is there a free trial available for Aspose.3D?

A2: Yes, you can explore the features of Aspose.3D with a free trial [here](https://releases.aspose.com/).

### Q3: Where can I find detailed documentation for Aspose.3D for Java?

A3: The comprehensive documentation is available [here](https://reference.aspose.com/3d/java/).

### Q4: How can I get support for Aspose.3D?

A4: Visit the [Aspose.3D forum](https://forum.aspose.com/c/3d/18) for any assistance or queries.

### Q5: Are temporary licenses available for Aspose.3D?

A5: Yes, you can obtain a temporary license [here](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2026-02-22  
**Tested With:** Aspose.3D for Java (latest release)  
**Author:** Aspose