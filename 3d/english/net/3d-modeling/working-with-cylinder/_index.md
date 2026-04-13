---
title: How to Create Cylinder with Shear Bottom – Aspose.3D for .NET
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
description: Learn how to create cylinder and export OBJ file using Aspose.3D for .NET. This beginner-friendly guide covers 3D scene setup and OBJ export.
weight: 12
url: /net/3d-modeling/working-with-cylinder/
date: 2026-03-26
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# How to Create Cylinder with Shear Bottom – Aspose.3D for .NET

## Introduction
If you’re wondering **how to create cylinder** objects with a customized shear bottom in a .NET environment, you’ve landed in the right place. In this tutorial we’ll walk through every step—from setting up a 3‑D scene to exporting the final model as an OBJ file—so you can boost your *beginner 3D modeling* skills using **Aspose.3D for .NET**.

## Quick Answers
- **What is the primary class to start a 3D model?** `Scene` creates the root container for all geometry.  
- **Which method exports the model to OBJ?** `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Do I need a license for testing?** A free trial is available — see the trial link in the FAQ.  
- **Can I change the shear angle?** Yes, modify `ShearBottom` with a `Vector2` value.  
- **Is this suitable for beginners?** Absolutely; the API abstracts low‑level mesh handling.

## What is a 3D Scene?
A *3D scene* is a hierarchical container that holds all geometric entities, lights, cameras, and transformations. In Aspose.3D the `Scene` class provides a clean way to organize and later export your models.

## Why Export OBJ?
OBJ is a widely‑supported, text‑based format that many 3‑D applications (Blender, Maya, Unity) can import. Exporting to OBJ lets you share or further edit your cylinder models outside of .NET.

## Prerequisites
Before we dive in, make sure you have:

- Basic knowledge of C# and .NET development.  
- **Aspose.3D for .NET** installed – you can download it **[here](https://releases.aspose.com/3d/net/)**.  
- A .NET IDE (Visual Studio, Rider, or VS Code) ready for coding.

## Import Namespaces
First, bring the required namespaces into scope so the API types are recognized.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Step 1: Create a 3D Scene
The `Scene` object acts as the root of your model hierarchy.

```csharp
Scene scene = new Scene();
```

## Step 2: Create Cylinder 1
We generate the first cylinder with a radius of 2, height 10, and 20 radial segments.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Step 3: Customize Shear Bottom for Cylinder 1
Apply a shear transformation, enable fan‑cylinder generation, and adjust other properties to achieve the desired shape.

```csharp
// Shear 47.5deg in the xy plane (z-axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## Step 4: Add Cylinder 1 to the Scene
Place the first cylinder at a convenient location using a translation transform.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## Step 5: Create Cylinder 2
A second cylinder is created with the same base dimensions but without custom shear—perfect for side‑by‑side comparison.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Step 6: Add Cylinder 2 to the Scene
We simply attach the second cylinder to the scene graph.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## Step 7: Export the Scene as an OBJ File
Finally, we save the entire scene to an OBJ file so it can be opened in any standard 3‑D viewer.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## Common Issues and Solutions
| Issue | Why It Happens | Fix |
|-------|----------------|-----|
| **OBJ file is empty** | The scene has no geometry attached. | Ensure both cylinders are added to `scene.RootNode`. |
| **Shear looks wrong** | `ShearBottom` expects a tangent of the angle. | Use `Math.Tan(angleInRadians)` or the provided `0.83` for ~47.5°. |
| **File path errors** | Invalid or missing directory. | Use `Path.Combine(Environment.CurrentDirectory, "CustomizedShearBottomCylinder.obj")`. |

## Frequently Asked Questions
### Is Aspose.3D for .NET suitable for beginners?
Absolutely! Aspose.3D for .NET offers a high‑level API that abstracts the math‑heavy parts of 3‑D modeling, making it approachable for developers at any skill level.

### Can I apply different shearing angles to cylinders?
Yes, each `Cylinder` instance has its own `ShearBottom` property, so you can assign a unique angle to each object.

### Is there a trial version available?
Yes, you can explore the free trial version **[here](https://releases.aspose.com/)**.

### Where can I find additional support?
Visit the **[Aspose.3D forum](https://forum.aspose.com/c/3d/18)** for community help, code samples, and discussion.

### How can I obtain a temporary license?
Get your temporary license **[here](https://purchase.aspose.com/temporary-license/)**.

**Additional Q&A**

**Q: How do I export the model in a different format, like STL?**  
A: Replace `FileFormat.WavefrontOBJ` with `FileFormat.STL` in the `scene.Save` call.

**Q: Can I animate the cylinders after creation?**  
A: Yes, you can add key‑frame animations to node transforms using the `Animation` classes provided by Aspose.3D.

**Q: Does the API support .NET Core?**  
A: The library is fully compatible with .NET Core, .NET 5+, and .NET 6+.

---

**Last Updated:** 2026-03-26  
**Tested With:** Aspose.3D for .NET (latest release)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}