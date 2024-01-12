---
title: Creating Fan Cylinder
linktitle: Creating Fan Cylinder
second_title: Aspose.3D .NET API
description: Unlock the world of 3D design with Aspose.3D for .NET! Create stunning fan and non-fan cylinders effortlessly. Download your trial now.
type: docs
weight: 10
url: /net/working-with-cylinder/create-fan-cylinder/
---
## Introduction
Welcome to the world of 3D modeling and visualization with Aspose.3D for .NET! In this step-by-step guide, we'll explore how to create a captivating fan cylinder using Aspose.3D for .NET. Aspose.3D is a powerful library that provides extensive capabilities for working with 3D content in .NET applications.
## Prerequisites
Before we dive into the exciting world of 3D modeling, ensure that you have the following prerequisites:
- A basic understanding of .NET programming.
- Visual Studio installed on your machine.
- Aspose.3D for .NET library, which you can download [here](https://releases.aspose.com/3d/net/).
- A genuine interest in unleashing your creativity through 3D design.
## Import Namespaces
Let's kick things off by importing the necessary namespaces to make Aspose.3D functionality available in your .NET project.
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
// Import Aspose.3D namespaces
```
Now that we're all set up, let's break down the process of creating a fan cylinder into manageable steps.
## Step 1: Create a Scene
```csharp
// Create a Scene
Scene scene = new Scene();
```
Begin by initializing a new 3D scene. This serves as the canvas where our fan cylinder will come to life.
## Step 2: Create a Fan Cylinder
```csharp
// Create a cylinder
var fan = new Cylinder(2, 2, 10, 20, 1, false);
```
Define the characteristics of your fan cylinder, specifying parameters such as radius, height, and resolution.
## Step 3: Customize Fan Cylinder Properties
```csharp
// Set GenerateFanCylinder to true
fan.GenerateFanCylinder = true;
// Set ThetaLength
fan.ThetaLength = MathUtils.ToRadian(270);
```
Tailor your fan cylinder by enabling the generation of the fan part and adjusting the angular sweep using ThetaLength.
## Step 4: Position the Fan Cylinder in the Scene
```csharp
// Create ChildNode
scene.RootNode.CreateChildNode(fan).Transform.Translation = new Vector3(10, 0, 0);
```
Add the fan cylinder as a child node to the scene's root node and position it within the 3D space.
## Step 5: Create a Non-Fan Cylinder
```csharp
// Create a cylinder without a fan
var nonfan = new Cylinder(2, 2, 10, 20, 1, false);
```
Explore the flexibility of Aspose.3D by creating a cylinder without the fan part.
## Step 6: Customize Non-Fan Cylinder Properties
```csharp
// Set GenerateFanCylinder to false
nonfan.GenerateFanCylinder = false;
// Set ThetaLength 
nonfan.ThetaLength = MathUtils.ToRadian(270);
```
Distinguish the non-fan cylinder by disabling the generation of the fan part.
## Step 7: Position the Non-Fan Cylinder in the Scene
```csharp
// Create ChildNode
scene.RootNode.CreateChildNode(nonfan);
```
Similarly, add the non-fan cylinder as a child node to the scene's root node.
## Step 8: Save the Scene
```csharp
// Save scene
scene.Save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WavefrontOBJ);
```
Save your masterpiece in the desired format and location. Now, you've successfully created a fan and non-fan cylinder using Aspose.3D for .NET!
## Conclusion
Congratulations on completing this hands-on guide to 3D modeling with Aspose.3D for .NET! You've unleashed your creativity in the digital realm, crafting fan and non-fan cylinders with ease.
## Frequently Asked Questions
### Can I use Aspose.3D for .NET with other .NET frameworks?
Yes, Aspose.3D is compatible with various .NET frameworks, providing versatility in your development projects.
### Is there a free trial available for Aspose.3D for .NET?
Yes, you can explore a free trial [here](https://releases.aspose.com/).
### Where can I find detailed documentation for Aspose.3D for .NET?
The documentation is available [here](https://reference.aspose.com/3d/net/).
### How can I get support for Aspose.3D for .NET?
Visit the support forum [here](https://forum.aspose.com/c/3d/18) for assistance from the community and Aspose experts.
### Are temporary licenses available for Aspose.3D for .NET?
Yes, temporary licenses can be obtained [here](https://purchase.aspose.com/temporary-license/).
