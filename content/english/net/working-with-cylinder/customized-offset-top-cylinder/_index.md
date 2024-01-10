---
title: Customized Offset Top Cylinder
linktitle: Customized Offset Top Cylinder
second_title: Aspose.3D .NET API
description: Explore the wonders of 3D graphics with Aspose.3D for .NET. Learn to create customized offset top cylinders effortlessly. Elevate your coding experience now!
type: docs
weight: 11
url: /net/working-with-cylinder/customized-offset-top-cylinder/
---
## Introduction
Welcome to the world of 3D graphics manipulation with Aspose.3D for .NET! In this tutorial, we'll guide you through the process of creating a customized offset top cylinder using Aspose.3D, a powerful library for working with 3D scenes, objects, and formats in .NET applications.
## Prerequisites
Before we dive into the tutorial, make sure you have the following prerequisites:
- Basic knowledge of C# programming language.
- Visual Studio installed on your machine.
- Aspose.3D for .NET library downloaded and referenced in your project.
Now, let's get started with the step-by-step guide!
## Import Namespaces
Firstly, make sure to import the necessary namespaces in your C# code:
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
## Step 1: Create a Scene
```csharp
// Create a scene
Scene scene = new Scene();
```
This initializes a new 3D scene using Aspose.3D.
## Step 2: Initialize the Cylinder
```csharp
// Initialize cylinder
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
Here, we create a cylinder with specific parameters such as radius, height, and slices.
## Step 3: Set OffsetTop for the First Cylinder
```csharp
// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```
This sets a customized offset top for the first cylinder.
## Step 4: Create ChildNode for the First Cylinder
```csharp
// Create ChildNode
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
We add the first cylinder as a child node to the scene, adjusting its position.
## Step 5: Initialize the Second Cylinder
```csharp
// Initialize second cylinder without customized OffsetTop
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
A second cylinder is initialized without a customized offset top.
## Step 6: Create ChildNode for the Second Cylinder
```csharp
// Create ChildNode
scene.RootNode.CreateChildNode(cylinder2);
```
We add the second cylinder as a child node to the scene.
## Step 7: Save the Scene
```csharp
// Save
scene.Save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WavefrontOBJ);
```
This saves the 3D scene, including the customized offset top cylinder, in the Wavefront OBJ format.
Now you've successfully created a customized offset top cylinder using Aspose.3D for .NET!
## Conclusion
In this tutorial, we've explored the basics of working with Aspose.3D for .NET to create a customized offset top cylinder. This library opens up endless possibilities for 3D graphics manipulation within your .NET applications.
## FAQs
### Q: Where can I find the documentation for Aspose.3D for .NET?
A: The documentation is available [here](https://reference.aspose.com/3d/net/).
### Q: How can I download Aspose.3D for .NET?
A: You can download it [here](https://releases.aspose.com/3d/net/).
### Q: Is there a free trial available for Aspose.3D for .NET?
A: Yes, you can get a free trial [here](https://releases.aspose.com/).
### Q: Where can I get support for Aspose.3D for .NET?
A: Visit the [Aspose.3D forum](https://forum.aspose.com/c/3d/18) for support.
### Q: Can I obtain a temporary license for Aspose.3D for .NET?
A: Yes, you can get a temporary license [here](https://purchase.aspose.com/temporary-license/).
