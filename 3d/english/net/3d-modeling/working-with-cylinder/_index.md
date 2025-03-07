---
title: Customized Shear Bottom Cylinder
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
description: Learn to create customized shear bottom cylinders using Aspose.3D for .NET with our detailed step-by-step guide. Elevate your 3D modeling skills today!
weight: 12
url: /net/3d-modeling/working-with-cylinder/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Customized Shear Bottom Cylinder

## Introduction
Welcome to our comprehensive guide on creating a customized cylinder using Aspose.3D for .NET. If you're looking to enhance your 3D modeling skills and add unique features to your projects, you're in the right place. In this tutorial, we'll walk you through the process step by step, using clear explanations and code snippets.
## Prerequisites
Before we dive into the tutorial, ensure you have the following:
- Basic understanding of C# and .NET programming.
- Aspose.3D for .NET library installed. You can download it [here](https://releases.aspose.com/3d/net/).
- A development environment set up for .NET programming.
## Import Namespaces
In your C# code, start by importing the necessary namespaces:
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
Begin by creating a 3D scene using Aspose.3D:
```csharp
Scene scene = new Scene();
```
## Step 2: Create Cylinder 1
Generate the first cylinder and set its properties:
```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
## Step 3: Customize Shear Bottom for Cylinder 1
Apply a customized shear bottom to the first cylinder:
```csharp
// Shear 47.5deg in the xy plane (z-axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```
## Step 4: Add Cylinder 1 to the Scene
Add the first cylinder to the scene and set its translation:
```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
## Step 5: Create Cylinder 2
Generate a second cylinder with similar properties:
```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
## Step 6: Add Cylinder 2 to the Scene
Add the second cylinder to the scene without customized parameters:
```csharp
scene.RootNode.CreateChildNode(cylinder2);
```
## Step 7: Save the Scene
Save the scene as a Wavefront OBJ file in your document directory:
```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```
## Conclusion
Congratulations! You've successfully created a customized shear bottom cylinder using Aspose.3D for .NET. This tutorial aimed to provide a step-by-step guide for users with varying levels of expertise in 3D modeling and programming.
## Frequently Asked Questions
### Is Aspose.3D for .NET suitable for beginners?
Absolutely! Aspose.3D for .NET offers a user-friendly interface, making it accessible for both beginners and experienced developers.
### Can I apply different shearing angles to cylinders?
Yes, you can customize the shear bottom for each cylinder individually, allowing you to achieve unique effects.
### Is there a trial version available?
Yes, you can explore the free trial version [here](https://releases.aspose.com/).
### Where can I find additional support?
Visit the [Aspose.3D forum](https://forum.aspose.com/c/3d/18) for community support and discussions.
### How can I obtain a temporary license?
Get your temporary license [here](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
