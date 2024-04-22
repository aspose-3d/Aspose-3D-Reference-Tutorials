---
title: Export attributes in RVM
linktitle: Export attributes in RVM
second_title: Aspose.3D .NET API
description: Explore the world of 3D modeling in .NET with Aspose.3D. Learn how to export properties in RVM. 
type: docs
weight: 18
url: /net/loading-and-saving/rvm/export-meta-data/
---
## Introduction

Welcome to our step-by-step guide on how to export properties in RVM using Aspose.3D for .NET. Aspose.3D is a powerful library that enables .NET developers to work with 3D files, providing extensive functionality for 3D modeling and manipulation. This guide will walk you through the process step-by-step, ensuring you leverage the full potential of Aspose.3D for .NET. Unleash your creativity now!

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
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```

These namespaces will provide the essential building blocks for our 3D manipulation.



## Step 1: Initialize the Scene Object and Box Object
```csharp
Scene scene = new Scene();
var box = new Box().ToMesh();
```

This code sets up the environment for your 3D scene and creates the Box object.


## Step 2: Set node properties

```csharp
//node's name is required to export attributes
var boxNode = scene.RootNode.CreateChildNode("box", box);
boxNode.SetProperty("rvm:Price", 12.0);
boxNode.SetProperty("rvm:Weight", 30.0);
var opt = new RvmSaveOptions();
```

When exporting properties we need to set the name of the node.


## Step 3: Export attributes

```csharp
//Properties with rvm: prefix will be exported.
opt.ExportAttributes = true;
opt.AttributePrefix = "rvm:";
opt.Author = "Aspose.3D";
opt.FileNote = "Test attribute export";
scene.Save("output.rvm", opt);
```

We will export the attributes with rvm prefix and save the file in rvm format.

## Conclusion

Congratulations! You have successfully learned how to export properties in RVM. Armed with this knowledge, you can start your own 3D journey and unleash the creative possibilities in Aspose.3D.This tutorial only scratches the surface, so dig deeper into the [documentation](https://reference.aspose.com/3d/net/) for more advanced features.

## FAQ's

### Q1:  Is Aspose.3D compatible with different 3D file formats?

A1: Yes, Aspose.3D supports various file formats, including FBX, STL, and more.

### Q2: Where can I find community support for Aspose.3D?

A2: Visit the [Aspose.3D forum](https://forum.aspose.com/c/3d/18) to engage with the community and seek assistance.

### Q3: Is there a trial version available?

A3: Yes, you can explore Aspose.3D with a [free trial](https://releases.aspose.com/).

### Q4: How can I obtain a temporary license for Aspose.3D?

A4: You can acquire a temporary license [here](https://purchase.aspose.com/temporary-license/).

### Q5: Where can I purchase Aspose.3D for .NET?

A5: Visit the [purchase page](https://purchase.aspose.com/buy) to acquire the full version of Aspose.3D.
