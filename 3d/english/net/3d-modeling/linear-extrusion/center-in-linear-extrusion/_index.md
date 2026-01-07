---
title: Add Ground Plane and Center in Linear Extrusion
linktitle: Add Ground Plane and Center in Linear Extrusion
second_title: Aspose.3D .NET API
description: Learn how to add ground plane while performing linear extrusion with Aspose.3D for .NET and export Wavefront OBJ files. Master centering and grounding techniques in 3‑D modeling.
weight: 10
url: /net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
date: 2026-01-07
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Add Ground Plane and Center in Linear Extrusion

## Introduction

Welcome to this comprehensive guide on mastering linear extrusion using Aspose.3D for .NET. If you're looking to **add ground plane** to your models and **export Wavefront OBJ** files while keeping the extrusion centered, you're in the right place. In this tutorial, we'll delve into the linear extrusion technique, specifically focusing on the centering aspect and how a ground plane helps you visualize the result more clearly.

## Quick Answers
- **What does “add ground plane” achieve?** It provides a visual reference that makes it easy to see where the extrusion sits on the X‑Z plane.  
- **Which format is used to export the model?** The scene is saved as a Wavefront OBJ file (`FileFormat.WavefrontOBJ`).  
- **Do I need a license to run the code?** A free trial works for development; a permanent license is required for production.  
- **Can I change the extrusion length?** Yes – modify the second parameter of `LinearExtrusion`.  
- **Is centering optional?** Setting `Center = true` centers the extrusion around the profile; `false` aligns it to one side.

## Prerequisites

Before we embark on this exciting journey, make sure you have the following prerequisites in place:

- Basic understanding of C# programming language.  
- Visual Studio installed on your machine.  
- Aspose.3D for .NET library, which you can download from the [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/).  
- Ensure you have access to the [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/) for reference throughout the tutorial.

## Import Namespaces

To kick things off, let's import the necessary namespaces. These will lay the foundation for our 3D modeling masterpiece.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Step 1: Initialize the Base Profile

We start by defining a rectangular profile that will be extruded. The `RoundingRadius` adds a subtle fillet to the corners.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Step 2: Create a 3D Scene

A `Scene` object acts as the container for all geometry, lights, and cameras.

```csharp
Scene scene = new Scene();
```

## Step 3: Create Left and Right Nodes

Two sibling nodes are created under the root. One will demonstrate extrusion **without** centering, the other **with** centering. We also translate the left node so the two examples don’t overlap.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## Step 4: Perform Linear Extrusion on Left Node (No Center)

Here we extrude the profile without centering. Notice the `Center = false` flag.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## Step 5: Add Ground Plane for Reference (Left Node)

Adding a thin box acts as a **ground plane** so you can clearly see how the extrusion sits on the base.

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## Step 6: Perform Linear Extrusion on Right Node (With Center)

Now we extrude the same profile but enable centering. The geometry will be symmetrically placed around the profile’s origin.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## Step 7: Add Ground Plane for Reference (Right Node)

A second ground plane is added to the right node to keep the visual comparison consistent.

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## Step 8: Export Wavefront OBJ File

Finally, we **export Wavefront OBJ** so the result can be opened in any standard 3‑D viewer.

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Why Add a Ground Plane?

Adding a ground plane gives you an immediate visual cue about the extrusion’s height and alignment. It’s especially helpful when you need to compare centered vs. non‑centered results, as demonstrated in this tutorial.

## Common Issues & Tips

- **Ground plane not visible:** Ensure the plane’s thickness (`0.01` in the `Box` constructor) is small enough not to obscure the extrusion but large enough to be rendered.  
- **Export fails:** Verify the output directory exists and you have write permissions.  
- **Centered extrusion appears offset:** Double‑check the `Center` property; `true` centers the profile, `false` aligns it to one side.

## Frequently Asked Questions

### Q1: Can I use Aspose.3D for .NET with other programming languages?

A1: Aspose.3D primarily supports .NET languages such as C# and VB.NET.

### Q2: Where can I find support for Aspose.3D-related queries?

A2: Visit the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) for dedicated support and discussions.

### Q3: Is there a free trial available for Aspose.3D for .NET?

A3: Yes, you can access the free trial [here](https://releases.aspose.com/).

### Q4: How can I obtain a temporary license for Aspose.3D for .NET?

A4: You can acquire a temporary license [here](https://purchase.aspose.com/temporary-license/).

### Q5: Where can I purchase the Aspose.3D for .NET license?

A5: Purchase your license [here](https://purchase.aspose.com/buy).

### Q6: Can I export the scene to other formats besides OBJ?

A6: Yes, Aspose.3D supports many formats such as STL, FBX, and GLTF. Simply change the `FileFormat` enum value in the `Save` method.

### Q7: How do I change the extrusion’s number of slices?

A7: Adjust the `Slices` property in the `LinearExtrusion` constructor to control mesh density.

---

**Last Updated:** 2026-01-07  
**Tested With:** Aspose.3D for .NET latest version  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}