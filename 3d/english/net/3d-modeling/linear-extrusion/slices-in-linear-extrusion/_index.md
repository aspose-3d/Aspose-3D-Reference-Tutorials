---
title: How to Linear Extrusion with Slices Using Aspose.3D for .NET
linktitle: How to Linear Extrusion with Slices
second_title: Aspose.3D .NET API
description: Learn how to linear extrusion with slices using Aspose.3D for .NET. Create detailed 3D models with step‑by‑step code examples.
weight: 13
url: /net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
date: 2026-03-23
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# How to Linear Extrusion with Slices Using Aspose.3D for .NET

## Introduction

Welcome to the world of 3D design using Aspose.3D for .NET! In this tutorial you'll discover **how to linear extrusion** with slices, a technique that lets you control the level of detail in your models. Whether you're a seasoned developer or just getting started, we’ll walk you through every step, explain the why behind each action, and give you practical tips you can apply right away.

## Quick Answers
- **What is linear extrusion with slices?** It’s a method of extending a 2D profile into 3D while specifying how many intermediate cross‑sections (slices) are generated.  
- **Why use slices?** More slices give smoother curvature; fewer slices keep the mesh lightweight.  
- **Prerequisites?** Aspose.3D for .NET, a .NET‑compatible IDE, and basic C# knowledge.  
- **Typical runtime?** The sample runs in under a second on a modern PC.  
- **Output format?** The example saves to Wavefront OBJ, but Aspose.3D supports many formats.

## What is Linear Extrusion with Slices?

Linear extrusion takes a 2‑D shape (a profile) and stretches it along a straight line to create a 3‑D solid. The **Slices** property determines how many intermediate cross‑sections are inserted between the start and end of the extrusion, affecting smoothness and polygon count.

## Why Use Slices in Linear Extrusion?

- **Control Mesh Density:** Fine‑tune the balance between visual quality and file size.  
- **Optimize Performance:** Use fewer slices for real‑time applications, more for high‑resolution renders.  
- **Creative Flexibility:** Combine different slice counts on separate objects to highlight design intent.

## Prerequisites

Before diving in, make sure you have:

- Aspose.3D for .NET Library – download it from [here](https://releases.aspose.com/3d/net/).  
- An IDE that supports C# (Visual Studio, Rider, VS Code, etc.).  
- Basic familiarity with C# syntax and object‑oriented concepts.  
- A curiosity to experiment with 3‑D geometry!

## Import Namespaces

First, import the namespaces that give you access to the core Aspose.3D classes.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Step‑by‑Step Guide

### Step 1: Initialize the Base Profile

We start with a simple rectangular shape and give it a small rounding radius so the edges aren’t perfectly sharp.

```csharp
// ExStart:InitializeBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd:InitializeBaseProfile
```

### Step 2: Create a 3D Scene

A `Scene` acts as the container for all nodes, meshes, lights, and cameras.

```csharp
// ExStart:Create3DScene
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### Step 3: Add Left and Right Nodes

We’ll create two sibling nodes under the scene’s root. The left node will receive a low slice count, the right node a high slice count, so you can compare the visual difference.

```csharp
// ExStart:CreateLeftRightNodes
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### Step 4: Perform Linear Extrusion on the Left Node (Low Detail)

Here we extrude the rectangle with only **2 slices**. This produces a coarse mesh—great for quick previews.

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### Step 5: Perform Linear Extrusion on the Right Node (High Detail)

Now we use **10 slices** for a much smoother result. Notice how the geometry becomes finer.

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### Step 6: Save the 3D Scene

Finally, write the scene to an OBJ file. Replace `"Your Output Directory"` with a valid path on your machine.

```csharp
// ExStart:Save3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
// ExEnd:Save3DScene
```

## Common Issues and Solutions

| Issue | Why It Happens | Fix |
|-------|----------------|-----|
| **No file created** | Output path is invalid or missing write permission. | Use an absolute path and ensure the folder exists. |
| **Object looks flat** | `Slices` set to 1 or 0. | Set `Slices` to at least 2 for a visible extrusion. |
| **Unexpected geometry** | Rounding radius too large for the rectangle size. | Adjust `RoundingRadius` to a value smaller than half the rectangle’s smallest side. |

## Frequently Asked Questions

**Q: Can I change the extrusion direction?**  
A: Yes. Use the `Transform` property on the node to rotate or translate the extruded geometry before saving.

**Q: Does Aspose.3D support other extrusion types?**  
A: Absolutely. Besides `LinearExtrusion`, you can use `RevolveExtrusion`, `SweepExtrusion`, and more.

**Q: What file formats can I export to?**  
A: Aspose.3D supports OBJ, STL, FBX, 3MF, Collada, and many others. Just change the `FileFormat` enum.

**Q: Is there a way to programmatically set a material?**  
A: Yes. After creating the node, assign a `Material` to its `Entity` collection.

**Q: How does slice count affect memory usage?**  
A: More slices increase vertex and face counts, which raises memory consumption proportionally. Use profiling to find the sweet spot for your target platform.

## Original FAQ's

### Q1: Can I use Aspose.3D for .NET with other programming languages?

A1: Aspose.3D is primarily designed for .NET, but you can explore interoperability options with languages like Python using .NET bindings.

### Q2: Where can I find detailed documentation for Aspose.3D for .NET?

A2: Refer to the documentation [here](https://reference.aspose.com/3d/net/) for in‑depth information on Aspose.3D's capabilities and usage.

### Q3: Is there a free trial available for Aspose.3D for .NET?

A3: Yes, you can grab your free trial [here](https://releases.aspose.com/) to explore the library's features before making a purchase.

### Q4: How can I get technical support for Aspose.3D for .NET?

A4: Visit the Aspose.3D forum [here](https://forum.aspose.com/c/3d/18) to seek assistance and engage with the community.

### Q5: Can I use a temporary license for Aspose.3D for .NET?

A5: Yes, obtain a temporary license [here](https://purchase.aspose.com/temporary-license/) for evaluation purposes.

## Conclusion

You’ve now seen **how to linear extrusion** with slices using Aspose.3D for .NET, explored the impact of different slice counts, and learned how to export your work. Experiment with other profiles, play with the `Slices` value, and integrate materials or lights to create production‑ready 3‑D assets.

---

**Last Updated:** 2026-03-23  
**Tested With:** Aspose.3D 24.11 for .NET (latest at time of writing)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}