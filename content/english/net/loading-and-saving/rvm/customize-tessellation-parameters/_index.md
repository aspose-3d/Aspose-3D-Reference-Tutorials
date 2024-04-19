---
title: Customize tessellation parameters
linktitle: Customize tessellation parameters
second_title: Aspose.3D .NET API
description: Explore Use RvmLoadOptions to customize the tessellation parameters of primitive geometry imported from an RVM file.Please follow our step-by-step guide. Efficient, powerful and developer-friendly!
type: docs
weight: 18
url: /net/loading-and-saving/rvm/customize-tessellation-parameters/
---
## Introduction

In the ever-evolving world of 3D graphics and modeling, Aspose.3D for .NET emerges as a powerful tool, providing developers with seamless integration and powerful functionality. This tutorial walks you through using RvmLoadOptions to customize the tessellation parameters of primitive geometry imported from an RVM file. Buckle up as we embark on a journey utilizing the power of Aspose.3D!

## Prerequisites

Before we dive into the coding adventure, make sure you have the following prerequisites in place:

- Basic understanding of C# programming language.
- Visual Studio installed on your machine.
- Aspose.3D for .NET library downloaded and added to your project.

Now, let's get our hands dirty with some code!

## Import Namespaces

In your C# project, ensure you have the necessary namespaces included:

```csharp
using System;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD;
```

These namespaces will provide the essential building blocks for our 3D manipulation.



## Step 1: Create RvmLoadOptions object
```csharp
RvmLoadOptions opt = new RvmLoadOptions();
```

First we need to create a RvmLoadOptions object.


## Step 2: Set custom tessellation parameters

```csharp
opt.RectangularTorusSegments = 30;
opt.CylinderRadialSegments = 20;
opt.DishLatitudeSegments = 20;
opt.DishLongitudeSegments = 20;
opt.CenterScene = true;
```

We need to manually customize these parameters, including 'RectangularTorusSegments', 'CylinderRadialSegments', 'DishLatitudeSegments', 'DishLongitudeSegments', 'CenterScene'.


## Step 3: Save file

```csharp
var scene = Scene.FromFile("input.rvm", opt);
scene.Save("output.obj");
```

We apply the parameters to the rvm file and save the file in obj format.

## Conclusion

Congratulations! You have successfully completed using RVM LoadOptions to customize the tessellation parameters of primitive geometry imported from an RVM file. This tutorial only scratches the surface, so dig deeper into the [documentation](https://reference.aspose.com/3d/net/) for more advanced features.

## FAQ's

### Q1:  Where can I find comprehensive documentation for Aspose.3D for .NET?

A1: The documentation is available [here](https://reference.aspose.com/3d/net/).

### Q2: Where can I find community support for Aspose.3D?

A2: Visit the [Aspose.3D forum](https://forum.aspose.com/c/3d/18) to engage with the community and seek assistance.

### Q3: Is there a trial version available?

A3: Yes, you can explore Aspose.3D with a [free trial](https://releases.aspose.com/).

### Q4: How can I obtain a temporary license for Aspose.3D?

A4: You can acquire a temporary license [here](https://purchase.aspose.com/temporary-license/).

### Q5: Where can I purchase Aspose.3D for .NET?

A5: Visit the [purchase page](https://purchase.aspose.com/buy) to acquire the full version of Aspose.3D.
