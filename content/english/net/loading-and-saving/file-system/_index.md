---
title: File System Implementation
linktitle: File System Implementation
second_title: Aspose.3D .NET API
description: Explore overriding file system access permissions by specifying different implementations. Follow our step-by-step guide. Efficient, powerful and developer-friendly!
type: docs
weight: 18
url: /net/loading-and-saving/file-system/
---
## Introduction

In the ever-evolving world of 3D graphics and modeling, Aspose.3D for .NET emerges as a powerful tool, providing developers with seamless integration and powerful capabilities. This tutorial walks you through overriding file system access permissions by specifying different implementations. Aspose.3D provides different file system implementations, or you can use your own implementation. Buckle up as we embark on a journey that harnesses the power of Aspose.3D!

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
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

These namespaces will provide the essential building blocks for our 3D manipulation.



## Step 1: Create a Box Object and add Materials
```csharp
Scene scene = new Scene();
var material = new PhongMaterial();
var boxNode = scene.RootNode.CreateChildNode(new Box());
boxNode.Material = material;
```

This code sets up the environment for the 3D scene, creating the Box object and adding materials to it.


## Step 2: File System Implementation

```csharp
var opt = new ObjSaveOptions();
var memFs = new Dictionary<string, MemoryStream>();
opt.FileSystem = FileSystem.CreateMemoryFileSystem(memFs);
using var output = new MemoryStream();
opt.FileName = "output.obj";
scene.Save(output, opt);
```

The default file system is LocalFileSystem, which is not secure in an environment like the server side, but you can override file system access permissions by specifying a different implementation. You can also use your own implementation.


## Step 3: Write Material

```csharp
//The material will be written to variable memFs named output.mtl
var materialInBytes = memFs["output.mtl"].ToArray();
```

We write the material into the output.mtl file.

## Conclusion

Congratulations! You have successfully learned how to override file system access permissions by specifying a different implementation. Armed with this knowledge you can start your own 3D journey, feel free to experiment and incorporate this knowledge into your projects.This tutorial only scratches the surface, so dig deeper into the [documentation](https://reference.aspose.com/3d/net/) for more advanced features.

## FAQ's

### Q1:  Is Aspose.3D compatible with all .NET frameworks?

A1: Yes, Aspose.3D is compatible with a wide range of .NET frameworks, ensuring flexibility for developers.

### Q2: Where can I find community support for Aspose.3D?

A2: Visit the [Aspose.3D forum](https://forum.aspose.com/c/3d/18) to engage with the community and seek assistance.

### Q3: Is there a trial version available?

A3: Yes, you can explore Aspose.3D with a [free trial](https://releases.aspose.com/).

### Q4: Where can I find detailed documentation for Aspose.3D for .NET?

A4: Refer to the [documentation](https://reference.aspose.com/3d/net/) for comprehensive information.

### Q5: Where can I purchase Aspose.3D for .NET?

A5: Visit the [purchase page](https://purchase.aspose.com/buy) to acquire the full version of Aspose.3D.
