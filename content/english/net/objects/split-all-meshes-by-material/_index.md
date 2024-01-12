---
title: Splitting All Meshes of Scene by Material
linktitle: Splitting All Meshes of Scene by Material
second_title: Aspose.3D .NET API
description: Learn how to split 3D meshes by material using Aspose.3D for .NET. Follow our step-by-step guide for efficient organization and management of 3D models.
type: docs
weight: 21
url: /net/objects/split-all-meshes-by-material/
---
## Introduction
Welcome to this step-by-step guide on splitting all meshes of a 3D scene by material using Aspose.3D for .NET. If you're working with 3D models and want to efficiently organize your meshes based on materials, this tutorial is for you. Aspose.3D is a powerful .NET library that provides a range of features for working with 3D files, making it an excellent choice for developers.
## Prerequisites
Before diving into the tutorial, make sure you have the following prerequisites:
- Basic understanding of C# programming language.
- Visual Studio installed on your machine.
- Aspose.3D for .NET library. You can download it from [here](https://releases.aspose.com/3d/net/).
- An input 3D file (for example, "test.fbx") that you want to split.
## Import Namespaces
Start by importing the necessary namespaces in your C# project:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```
## Step 1: Load the 3D File
```csharp
// The path to the documents directory.
string input = RunExamples.GetDataFilePath("test.fbx");
// Load a 3D file
Scene scene = new Scene(input);
```
In this step, we load the 3D file using Aspose.3D's `Scene` class.
## Step 2: Split All Meshes
```csharp
// Split all meshes
PolygonModifier.SplitMesh(scene, SplitMeshPolicy.CloneData);
```
Here, we use the `SplitMesh` method from the `PolygonModifier` class to split all meshes based on the material.
## Step 3: Save the Split Scene
```csharp
// Save file
var output = "Your Output Directory" + "test-splitted.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```
Save the modified scene to a new file to retain the changes.
## Step 4: Display Success Message
```csharp
// Display success message
Console.WriteLine("\nSplitting all meshes of a scene per material successfully.\nFile saved at " + output);
```
Print a success message indicating that the operation was completed successfully.
## Conclusion
Congratulations! You have successfully learned how to split all meshes of a 3D scene by material using Aspose.3D for .NET. This can be a valuable technique for organizing and managing complex 3D models.
## FAQs
### 1. Can I use Aspose.3D for .NET with other programming languages?
Aspose.3D is primarily designed for .NET, but it provides interoperability with other languages through .NET language bindings.
### 2. Is there a trial version available?
Yes, you can access the free trial version [here](https://releases.aspose.com/).
### 3. Where can I find more examples and documentation?
Explore the comprehensive documentation at [Aspose.3D Documentation](https://reference.aspose.com/3d/net/).
### 4. How can I get support for Aspose.3D?
Visit the [Aspose.3D forum](https://forum.aspose.com/c/3d/18) for community support and discussions.
### 5. Can I obtain a temporary license?
Yes, you can get a temporary license [here](https://purchase.aspose.com/temporary-license/).
