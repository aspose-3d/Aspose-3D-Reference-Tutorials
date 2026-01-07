---
title: Create 3D Scene Aspose: Linear Extrusion Direction
linktitle: Create 3D Scene Aspose: Linear Extrusion Direction
second_title: Aspose.3D .NET API
description: Learn how to create 3D scene Aspose using linear extrusion direction in Aspose.3D for .NET. Follow this step‑by‑step guide with code examples.
weight: 11
url: /net/3d-modeling/linear-extrusion/direction-in-linear-extrusion/
date: 2026-01-07
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Direction in Linear Extrusion

## Introduction

Creating a **3D scene** programmatically can feel daunting, but with **Aspose.3D for .NET** it becomes a smooth, enjoyable process. In this tutorial you’ll learn how to **create 3D scene Aspose**‑style and explore the *Direction* property of linear extrusion, which lets you tilt and steer the extrusion path for more dynamic models.

## Quick Answers
- **What does “Direction” do in linear extrusion?**  
  It defines a custom vector that tilts the extrusion, giving you control over the final shape’s orientation.
- **Do I need a license to run the sample?**  
  A temporary or trial license is sufficient for development and testing.
- **Which .NET versions are supported?**  
  Aspose.3D works with .NET Framework 4.5+, .NET Core 3.1+, and .NET 5/6.
- **Can I export to formats other than OBJ?**  
  Yes – the `Scene.Save` method supports many formats such as FBX, STL, and Collada.
- **Where can I find more examples?**  
  The official Aspose.3D documentation and forum contain dozens of ready‑to‑run samples.

## What is Linear Extrusion Direction?

Linear extrusion takes a 2‑D profile (like a rectangle) and sweeps it along a straight line to produce a 3‑D solid. By default the sweep follows the global Z‑axis. Adding a **Direction** vector tells Aspose to extrude along a custom axis, enabling slanted or skewed shapes without extra geometry work.

## Why Use the Direction Property?

- **Creative freedom:** Build ramps, angled beams, or architectural features with a single line of code.  
- **Reduced geometry:** No need to rotate or transform the whole mesh after extrusion.  
- **Performance:** The extrusion is calculated once with the correct orientation, saving processing time.

## Prerequisites

Before we dive in, ensure you have:

- **Aspose.3D for .NET** – download from the official site: [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/).  
- A working **.NET development environment** (Visual Studio, VS Code, or Rider).  

## Import Namespaces

Add the required `using` statements to the top of your C# file so the compiler knows where to find the Aspose classes.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Step‑by‑Step Guide

### Step 1: Initialize the Base Profile

We start with a simple rectangle that will be extruded. The `RoundingRadius` adds a subtle fillet to the corners.

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

Nodes act as placeholders in the scene graph. Here we create two child nodes – one for the default extrusion and another for the directional extrusion.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(8, 0, 0);
```

### Step 4: Linear Extrusion without Direction

The left node demonstrates a classic extrusion with a full 360° twist and 100 slices for smoothness.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

### Step 5: Linear Extrusion with Direction

Now we add the `Direction` vector to the right node. Changing the vector’s components tilts the extrusion, producing an angled solid.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, Direction = new Vector3(0.3, 0.2, 1) });
```

### Step 6: Save the 3D Scene

Finally, export the scene to an OBJ file (or any other supported format). Replace the placeholder path with your desired output folder.

```csharp
scene.Save("Your Output Directory" + "DirectionInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Common Issues & Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| **Scene saves empty file** | Output path is invalid or missing write permissions. | Verify the directory exists and the application has write access. |
| **Extrusion appears flat** | `Direction` vector not normalized. | Provide a non‑zero vector; Aspose normalizes it internally, but extreme values can cause visual artifacts. |
| **Twist looks uneven** | Insufficient `Slices` for the chosen twist angle. | Increase `Slices` (e.g., 200) for smoother rotation. |

## FAQ's

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

## Frequently Asked Questions

**Q: Can I use the Direction property with other extrusion types (e.g., revolve)?**  
A: The `Direction` property is specific to `LinearExtrusion`. For revolve or sweep operations, use the corresponding transformation matrices.

**Q: Does the extrusion respect the profile’s local coordinate system?**  
A: Yes – the profile is interpreted in the XY‑plane before being extruded along the defined direction.

**Q: How large can the extrusion length be?**  
A: The length is a `double`; practical limits are bound by floating‑point precision and the target file format.

**Q: Is it possible to animate the extrusion direction at runtime?**  
A: You can modify the node’s transform or recreate the extrusion with a new `Direction` vector on each frame.

**Q: Which file formats preserve the custom direction when exported?**  
A: OBJ, FBX, and Collada retain the geometry exactly as generated; some formats may flatten the direction into vertex positions.

## Conclusion

By following this guide you now know how to **create 3D scene Aspose**‑style and leverage the `Direction` property to produce angled extrusions effortlessly. Experiment with different vectors, twists, and profiles to unlock a world of creative 3‑D designs.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2026-01-07  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

---