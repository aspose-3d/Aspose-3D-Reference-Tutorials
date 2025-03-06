---
title: Direction in Linear Extrusion
linktitle: Direction in Linear Extrusion
second_title: Aspose.3D .NET API
description: Unlock the world of 3D modeling with Aspose.3D for .NET. Learn direction linear extrusion, boost creativity, and craft immersive applications effortlessly.
weight: 11
url: /net/3d-modeling/linear-extrusion/direction-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Direction in Linear Extrusion

## Introduction

In the dynamic world of software development, creating immersive 3D models is an indispensable skill. Aspose.3D for .NET provides developers with a robust set of tools to harness the potential of 3D modeling in their applications. In this tutorial, we will delve into the intriguing world of linear extrusion and explore the nuances of the "Direction in Linear Extrusion" feature.

## Prerequisites

Before we embark on this exciting journey, make sure you have the following prerequisites in place:

- Aspose.3D for .NET: Download and install the library from [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/).

- Development Environment: Ensure you have a working .NET development environment set up.

## Import Namespaces

In your .NET project, import the necessary namespaces to access the functionality of Aspose.3D. Add the following lines to the beginning of your code:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Step 1: Initialize the Base Profile

Begin by initializing the base profile to be extruded. In this example, we create a rectangle shape with a rounding radius of 0.3.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Step 2: Create a 3D Scene

Build the foundation for your 3D masterpiece by creating a scene.

```csharp
Scene scene = new Scene();
```

## Step 3: Create Nodes

Generate nodes within the scene to represent different components of your 3D environment.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(8, 0, 0);
```

## Step 4: Linear Extrusion without Direction

Perform linear extrusion on the left node using the `Twist` and `Slices` properties.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## Step 5: Linear Extrusion with Direction

Extend the extrusion capabilities by incorporating the `Direction` property in the right node.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, Direction = new Vector3(0.3, 0.2, 1) });
```

## Step 6: Save the 3D Scene

Preserve your creation by saving the 3D scene. Replace `"Your Output Directory"` with the desired directory.

```csharp
scene.Save("Your Output Directory" + "DirectionInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Congratulations! You have successfully implemented linear extrusion with Aspose.3D for .NET, exploring both the traditional and directional approaches.

## Conclusion

In this tutorial, we navigated through the fascinating realm of 3D modeling using Aspose.3D for .NET. Linear extrusion, with and without direction, opens up endless possibilities for developers seeking to create visually stunning applications. With Aspose.3D, the power of 3D modeling is at your fingertips.

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

A5: Refer to the comprehensive [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/) for in-depth information.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
