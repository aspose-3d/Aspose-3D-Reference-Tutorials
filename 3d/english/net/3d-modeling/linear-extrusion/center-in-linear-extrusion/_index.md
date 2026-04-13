---
title: How to Use Aspose: Center in Linear Extrusion
linktitle: Center in Linear Extrusion
second_title: Aspose.3D .NET API
description: Learn how to use Aspose for centered linear extrusion, create 3d scene, and save obj file with Aspose.3D for .NET.
weight: 10
url: /net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Center in Linear Extrusion

## Introduction

Welcome to this comprehensive guide on **how to use Aspose** for centered linear extrusion in 3‑D modeling. If you want to **create 3d scene** objects, **export 3d model** files, and master the centering option, you’re in the right place. In the next few minutes we’ll walk through each step, explain why the centering flag matters, and show you how to **save obj file** output that’s ready for any viewer.

## Quick Answers
- **What does the Center property do?** It shifts the extrusion so it’s symmetric around the base profile.  
- **Which file format is used in this example?** Wavefront OBJ (`.obj`).  
- **Do I need a license for Aspose.3D?** A trial works for development; a commercial license is required for production.  
- **Can I change the number of slices?** Yes, adjust the `Slices` property to control mesh resolution.  
- **Is this compatible with .NET Core?** Absolutely – Aspose.3D supports .NET Framework, .NET Core, and .NET 5+.

## What is Centered Linear Extrusion?

Centered linear extrusion creates geometry that expands equally in both directions from the original profile, giving you a balanced model without manually translating the shape. This is especially handy when you need symmetrical parts or want to align objects precisely on a ground plane.

## Why use Aspose for this task?

Aspose.3D provides a clean, object‑oriented API that lets you **create 3d scene** objects, manipulate nodes, and export to popular formats with just a few lines of C#. No external 3‑D engines or heavy dependencies are required.

## Prerequisites

Before we dive in, ensure you have:

- Basic understanding of C# programming language.  
- Visual Studio installed on your machine.  
- Aspose.3D for .NET library, which you can download from the [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/).  
- Access to the [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/) for reference throughout the tutorial.

## Import Namespaces

First, import the namespaces that give us access to the core 3‑D classes.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Step 1: Initialize the Base Profile

We’ll start with a rectangle shape that will be extruded. The `RoundingRadius` adds a subtle fillet.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Step 2: Create a 3D Scene

A **Scene** is the container for all 3‑D objects. This is where we’ll **create 3d scene** and later **export 3d model**.

```csharp
Scene scene = new Scene();
```

## Step 3: Create Left and Right Nodes

We need two separate nodes to compare the effect of the `Center` flag. Notice the use of **left right nodes** terminology.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## Step 4: Perform Linear Extrusion on the Left Node (Center = false)

The left node demonstrates extrusion without centering, so the geometry starts at the profile’s origin.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## Step 5: Set Ground Plane for Reference (Left Node)

Adding a thin box gives us a visual ground plane to see how the extrusion sits relative to the origin.

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## Step 6: Perform Linear Extrusion on the Right Node (Center = true)

Now we enable the `Center` property. The extrusion expands equally in both directions, keeping the model centered on the ground plane.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## Step 7: Set Ground Plane for Reference (Right Node)

Again, we add a thin box so the two extrusions can be compared side‑by‑side.

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## Step 8: Save the 3D Scene

Finally, we **save obj file** using the Wavefront OBJ format. Adjust the output path as needed.

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Common Issues & Tips

- **Ground plane not visible?** Make sure the camera is positioned to view the thin box, or increase its thickness.  
- **Extrusion looks offset?** Verify the `Center` flag; `false` will anchor the extrusion at the profile base.  
- **Performance slow with many slices?** Reduce the `Slices` value; higher numbers increase mesh density.

## Frequently Asked Questions

**Q: Can I use Aspose.3D for .NET with other programming languages?**  
A: Aspose.3D primarily supports .NET languages such as C# and VB.NET.

**Q: Where can I find support for Aspose.3D-related queries?**  
A: Visit the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) for dedicated support and discussions.

**Q: Is there a free trial available for Aspose.3D for .NET?**  
A: Yes, you can access the free trial [here](https://releases.aspose.com/).

**Q: How can I obtain a temporary license for Aspose.3D for .NET?**  
A: You can acquire a temporary license [here](https://purchase.aspose.com/temporary-license/).

**Q: Where can I purchase the Aspose.3D for .NET license?**  
A: Purchase your license [here](https://purchase.aspose.com/buy).

## Conclusion

Congratulations! You’ve now learned **how to use Aspose** to perform centered linear extrusion, **create 3d scene**, **set ground plane**, and **save obj file**. Feel free to experiment with different profiles, slice counts, or export formats to broaden your 3‑D modeling toolkit.

---

**Last Updated:** 2026-03-21  
**Tested With:** Aspose.3D for .NET (latest release)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}