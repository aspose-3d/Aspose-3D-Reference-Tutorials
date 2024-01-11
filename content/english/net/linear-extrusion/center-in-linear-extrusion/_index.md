---
title: Center in Linear Extrusion
linktitle: Center in Linear Extrusion
second_title: Aspose.3D .NET API
description: Explore the world of 3D modeling with Aspose.3D for .NET. Center linear extrusion techniques, create stunning designs, and unleash your creativity.
type: docs
weight: 10
url: /net/linear-extrusion/center-in-linear-extrusion/
---
## Introduction

Welcome to this comprehensive guide on mastering linear extrusion using Aspose.3D for .NET. If you're looking to enhance your 3D modeling skills and create stunning extrusions, you're in the right place. In this tutorial, we'll delve into the linear extrusion technique, specifically focusing on the centering aspect to bring your designs to a whole new level.

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

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Step 2: Create a 3D Scene

```csharp
Scene scene = new Scene();
```

## Step 3: Create Left and Right Nodes

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## Step 4: Perform Linear Extrusion on Left Node

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## Step 5: Set Ground Plane for Reference

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## Step 6: Perform Linear Extrusion on Right Node

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## Step 7: Set Ground Plane for Reference (Right Node)

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## Step 8: Save 3D Scene

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Conclusion

Congratulations! You've successfully mastered the art of linear extrusion with centering using Aspose.3D for .NET. Feel free to experiment with different parameters and explore the vast possibilities this technique offers.

## FAQ's

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

