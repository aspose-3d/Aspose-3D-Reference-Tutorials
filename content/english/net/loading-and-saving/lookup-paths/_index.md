---
title: Manually Specify Lookup Texture
linktitle: Manually Specify Lookup Texture
second_title: Aspose.3D .NET API
description: Explore the world of 3D modeling in .NET with Aspose.3D. Learn how to manually specify lookup textures so that the importer can find them. Unleash your creativity now!
type: docs
weight: 18
url: /net/loading-and-saving/lookup-paths/
---
## Introduction

In the ever-evolving world of 3D graphics and modeling, Aspose.3D for .NET emerges as a powerful tool, providing developers with seamless integration and powerful capabilities. This tutorial will show you how to manually specify a lookup texture so that the importer can find it. Aspose.3D for .NET is a powerful library that enables developers to efficiently manipulate and save 3D scenes. Buckle up as we embark on a journey that harnesses the power of Aspose.3D!

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



## Step 1: Initialize the ObjLoadOptions object
```csharp
var opt = new ObjLoadOptions();
```

First we need to create an ObjLoadOptions object.


## Step 2: Lookup Paths

```csharp
//Specify the lookup paths, so the textures can be located.
opt.LookupPaths.Add("textures");
```

We need to manually specify the lookup texture so the importer can find it.


## Step 3: Save file

```csharp
var scene = Scene.FromFile("input.obj", opt);
scene.Save("output.glb");
```

We apply the texture parameters to the obj file and save the file in glb format.

## Conclusion

Congratulations! You have successfully learned how to manually specify a lookup texture so that the importer can find it. Armed with this knowledge, you can begin your own 3D journey, experimenting with different scenarios to unleash your creativity.This tutorial only scratches the surface, so dig deeper into the [documentation](https://reference.aspose.com/3d/net/) for more advanced features.

## FAQ's

### Q1:  Do I need a temporary license for testing?

A1: Yes, if you're testing the library, you can obtain a temporary license [here](https://purchase.aspose.com/temporary-license/).

### Q2: Where can I find community support for Aspose.3D?

A2: Visit the [Aspose.3D forum](https://forum.aspose.com/c/3d/18) to engage with the community and seek assistance.

### Q3: Is there a trial version available?

A3: Yes, you can explore Aspose.3D with a [free trial](https://releases.aspose.com/).

### Q4: Where can I find detailed documentation for Aspose.3D for .NET?

A4: Refer to the [documentation](https://reference.aspose.com/3d/net/) for comprehensive information.

### Q5: Where can I purchase Aspose.3D for .NET?

A5: Visit the [purchase page](https://purchase.aspose.com/buy) to acquire the full version of Aspose.3D.
