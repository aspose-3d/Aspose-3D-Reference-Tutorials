---
title: Default File System
linktitle: Default File System
second_title: Aspose.3D .NET API
description: The default FileSystem in SaveOptions/LoadOptions is directory-based file system,You can override the default implementation by specify it through IOConfig.FileSystemFactory.
type: docs
weight: 21
url: /net/loading-and-saving/default-file-system/
---
## Introduction

Welcome to the world of Aspose.3D for .NET! If you're looking to enhance your 3D development capabilities, you've come to the right place. In this tutorial, we will override the default file system implementation by specifying IOConfig.FileSystemFactory. Aspose.3D for .NET is a powerful library that enables developers to efficiently manipulate and save 3D scenes.

## Prerequisites

Before we start exploring the exciting features of Aspose.3D, make sure you have the following prerequisites:

- Basic understanding of C# and .NET development.
- Aspose.3D for .NET library installed. You can download it from the [release page](https://releases.aspose.com/3d/net/).
- A development environment set up with Visual Studio or any other preferred C# IDE.

## Import Namespaces

To get started, let's import the necessary namespaces:

```csharp
using System;
using System.IO;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Utilities;
using Aspose.ThreeD;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Entities;
```

Now that we've set the stage let's break down the tutorial into multiple steps.

## Step 1: Override Method
```csharp
IOConfig.FileSystemFactory = () => {
      return FileSystem.CreateDummyFileSystem();
};
```

First we need to override the methods in the file system.


## Step 2: Create a Box Object and add Materials

```csharp
Scene scene = new Scene();
var material = new PhongMaterial();
var boxNode = scene.RootNode.CreateChildNode(new Box());
boxNode.Material = material;
```

This code sets up the environment for the 3D scene, creating the Box object and adding materials to it.


## Step 3: Dummy File System

```csharp
//opt.FileSystem would be dummy file system now
var opt = new ObjSaveOptions();
using var output = new MemoryStream();
opt.FileName = "output.obj";
scene.Save(output, opt);
```

The material file output.mtl will not be written to any places because we've configured a dummy file system as default implementation.

## Conclusion

Congratulations! You have successfully learned how to override the default implementation by specifying IOConfig.FileSystemFactory. Once you have this knowledge, you can start your own 3D journey, feel free to experiment and incorporate this knowledge into your projects. This tutorial is just the beginning of what you can achieve with this powerful library.Explore the [documentation](https://reference.aspose.com/3d/net/) for more advanced features and techniques.

## FAQ's

### Q1: Is Aspose.3D for .NET compatible with all 3D file formats?

A1: Yes, Aspose.3D for .NET supports a wide range of 3D file formats, ensuring compatibility with various industry standards.

### Q2: Are there any licensing options available for Aspose.3D?

A2: Yes, you can explore licensing options [here](https://purchase.aspose.com/buy).

### Q3: Where can I find support for Aspose.3D-related queries?

A3: You can seek support on the [Aspose.3D forum](https://forum.aspose.com/c/3d/18).

### Q4: Is there a free trial available?

A4: Yes, you can access a free trial [here](https://releases.aspose.com/).

### Q5: How can I get a temporary license for Aspose.3D?

A5: Obtain a temporary license [here](https://purchase.aspose.com/temporary-license/).
