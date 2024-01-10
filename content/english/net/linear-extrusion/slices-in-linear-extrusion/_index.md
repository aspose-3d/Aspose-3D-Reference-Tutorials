---
title: Linear Extrusion -  Slices in Linear Extrusion
linktitle: Linear Extrusion -  Slices in Linear Extrusion
second_title: Aspose.3D .NET API
description: Explore the world of 3D design with Aspose.3D for .NET. Create stunning models using our linear extrusion tutorial.
type: docs
weight: 13
url: /net/linear-extrusion/slices-in-linear-extrusion/
---
## Introduction

Welcome to the world of 3D design using Aspose.3D for .NET! Whether you're a seasoned developer or just getting started, this tutorial will guide you through the process of creating stunning 3D visualizations using the powerful Aspose.3D library.

## Prerequisites

Before diving into the world of 3D design with Aspose.3D, make sure you have the following prerequisites:

- Aspose.3D for .NET Library: Ensure you have the Aspose.3D library installed. You can download it from [here](https://releases.aspose.com/3d/net/).

- Integrated Development Environment (IDE): Use any preferred IDE compatible with .NET development.

- Basic Understanding of C#: Familiarize yourself with C# programming language fundamentals.

- Desire to Explore 3D Design: A passion for creating visually stunning 3D models!

## Import Namespaces

To start your 3D design journey with Aspose.3D, you'll need to import the necessary namespaces. This ensures that your code can access the required classes and functionalities.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Linear Extrusion - Slices in Linear Extrusion

Now, let's dive into a practical example - Linear Extrusion with Slices. This technique allows you to create intricate 3D models with varying levels of detail.

### Step 1: Initialize the Base Profile

```csharp
// ExStart:InitializeBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd:InitializeBaseProfile
```

### Step 2: Create a 3D Scene

```csharp
// ExStart:Create3DScene
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### Step 3: Create Left and Right Nodes

```csharp
// ExStart:CreateLeftRightNodes
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### Step 4: Perform Linear Extrusion on Left Node

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### Step 5: Perform Linear Extrusion on Right Node

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### Step 6: Save 3D Scene

```csharp
// ExStart:Save3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
// ExEnd:Save3DScene
```

## Conclusion

Congratulations! You've successfully learned how to perform Linear Extrusion with Slices using Aspose.3D for .NET. This is just the beginning of your 3D design journey with Aspose.3D - unleash your creativity and explore the endless possibilities!

## FAQ's

### Q1: Can I use Aspose.3D for .NET with other programming languages?

A1: Aspose.3D is primarily designed for .NET, but you can explore interoperability options with languages like Python using .NET bindings.

### Q2: Where can I find detailed documentation for Aspose.3D for .NET?

A2: Refer to the documentation [here](https://reference.aspose.com/3d/net/) for in-depth information on Aspose.3D's capabilities and usage.

### Q3: Is there a free trial available for Aspose.3D for .NET?

A3: Yes, you can grab your free trial [here](https://releases.aspose.com/) to explore the library's features before making a purchase.

### Q4: How can I get technical support for Aspose.3D for .NET?

A4: Visit the Aspose.3D forum [here](https://forum.aspose.com/c/3d/18) to seek assistance and engage with the community.

### Q5: Can I use a temporary license for Aspose.3D for .NET?

A5: Yes, obtain a temporary license [here](https://purchase.aspose.com/temporary-license/) for evaluation purposes.
