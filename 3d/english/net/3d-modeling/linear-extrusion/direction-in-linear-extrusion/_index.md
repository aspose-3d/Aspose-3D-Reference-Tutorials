---
title: Create 3D Extrusion with Aspose: Direction in Linear Extrusion
linktitle: Direction in Linear Extrusion
second_title: Aspose.3D .NET API
description: Learn how to create 3D extrusion with Aspose.3D for .NET, using the Direction property in linear extrusion to craft complex models quickly.
weight: 11
url: /net/3d-modeling/linear-extrusion/direction-in-linear-extrusion/
date: 2026-03-23
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Direction in Linear Extrusion

## Introduction

Creating 3D extrusion with Aspose is a powerful way to add depth and realism to your .NET applications. In this tutorial you’ll learn **how to create 3D extrusion aspose** by using the *Direction* property of the `LinearExtrusion` class. We’ll walk through every step—from setting up the profile to saving the final OBJ file—so you can immediately apply the technique in real‑world projects.

## Quick Answers
- **What does the Direction property do?** It tilts the extrusion vector, letting you control the slope of the generated geometry.  
- **Do I need a license to run the sample?** Yes, a valid Aspose.3D license is required for production; a temporary license works for testing.  
- **Which .NET versions are supported?** .NET Framework 4.5+, .NET Core 3.1+, .NET 5/6+.  
- **Can I export to formats other than OBJ?** Absolutely – Aspose.3D supports FBX, STL, 3MF and more.  
- **How long does the code take to run?** Less than a second for the example shown.

## What is linear extrusion in Aspose.3D?

Linear extrusion takes a 2‑D profile (like a rectangle or circle) and sweeps it along a straight line to generate a 3‑D solid. By default the sweep follows the Z‑axis, but the **Direction** property lets you tilt that line, giving you creative control over the shape’s orientation.

## Why use the Direction property?

- **Custom slopes:** Build ramps, angled beams, or architectural elements without extra math.  
- **Single‑step modeling:** Avoid post‑processing transformations; the geometry is created exactly as needed.  
- **Performance:** The extrusion is performed natively by Aspose.3D, which is faster than manual mesh manipulation.

## Prerequisites

Before we dive in, ensure you have:

- Aspose.3D for .NET installed – download it from [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/).  
- A .NET development environment (Visual Studio 2022, VS Code, or Rider).  
- A valid Aspose license (temporary license works for learning).

## Import Namespaces

In your .NET project, import the necessary namespaces to access the functionality of Aspose.3D. Add the following lines to the beginning of your code:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Step‑by‑Step Guide

### Step 1: Initialize the Base Profile

We start by defining the 2‑D shape that will be extruded. Here we create a rectangle with a small rounding radius.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

### Step 2: Create a 3D Scene

A `Scene` object is the container for all nodes, meshes, lights, and cameras.

```csharp
Scene scene = new Scene();
```

### Step 3: Create Nodes

Nodes act as placeholders for geometry. We’ll create two child nodes—one for the default extrusion and one for the directional extrusion.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(8, 0, 0);
```

### Step 4: Linear Extrusion without Direction

First, we demonstrate the classic extrusion that follows the Z‑axis. The `Twist` and `Slices` properties add a full 360° twist and smooth the mesh.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

### Step 5: Linear Extrusion with Direction

Now we add the **Direction** property to the right node. By providing a custom `Vector3`, the extrusion tilts toward the specified direction, creating an angled solid.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, Direction = new Vector3(0.3, 0.2, 1) });
```

### Step 6: Save the 3D Scene

Finally, export the scene to an OBJ file (or any other supported format). Replace `"Your Output Directory"` with your desired path.

```csharp
scene.Save("Your Output Directory" + "DirectionInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| **Missing license exception** | Load a temporary or permanent license before creating the `Scene`. |
| **Extrusion looks flat** | Verify the `Direction` vector is not zero; a small Z component (e.g., 1) is required. |
| **File not found on save** | Ensure the output directory exists and you have write permissions. |
| **Unexpected rotation** | Remember that `Twist` is applied around the extrusion axis; adjust `Direction` accordingly. |

## Frequently Asked Questions

### Q1: How can I obtain a temporary license for Aspose.3D for .NET?

A1: Visit [Aspose Temporary License](https://purchase.aspose.com/temporary-license/) to get a temporary license.

### Q2: Where can I find support for Aspose.3D?

A2: Join the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) to seek assistance and connect with the community.

### Q3: Is there a free trial available?

A3: Yes, explore the features with a free trial at [Aspose.3D Releases](https://releases.aspose.com/).

### Q4: How do I purchase Aspose.3D for .NET?

A4: Navigate to the [Aspose Purchase Page](https://purchase.aspose.com/buy) for licensing options and purchasing details.

### Q5: Where can I find detailed documentation for Aspose.3D for .NET?

A5: Refer to the comprehensive [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/) for in‑depth information.

## Conclusion

In this tutorial we showed **how to create 3D extrusion aspose** by leveraging both the standard linear extrusion and the advanced `Direction` property. With these techniques you can model ramps, sloped beams, and any custom‑oriented geometry directly inside your .NET application, saving time and reducing post‑processing steps.

---

**Last Updated:** 2026-03-23  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}