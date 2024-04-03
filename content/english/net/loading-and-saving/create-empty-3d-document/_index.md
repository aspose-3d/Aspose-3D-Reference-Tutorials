---
title: Creating an Empty 3D Document
linktitle: Creating an Empty 3D Document
second_title: Aspose.3D .NET API
description: Explore the world of 3D document creation with Aspose.3D for .NET. Create, edit, and save stunning 3D scenes effortlessly.
type: docs
weight: 11
url: /net/loading-and-saving/create-empty-3d-document/
---
## Introduction

Welcome to the world of 3D document creation using Aspose.3D for .NET! In this tutorial, we will explore the basics of loading and saving 3D documents. Aspose.3D for .NET provides a powerful set of tools for working with 3D scenes, and we'll guide you through each step to help you get started smoothly.

## Prerequisites

Before we dive into the tutorial, make sure you have the following prerequisites in place:

- Aspose.3D for .NET: Ensure you have the library installed. You can download it from [here](https://releases.aspose.com/3d/net/).

## Import Namespaces

To begin, import the necessary namespaces in your .NET project:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## Loading and Saving - Creating an Empty 3D Document

### Step 1: Set Up Your Output Directory

```csharp
// The path to the documents directory.
var output = "Your Output Directory" + "document.fbx";
```

### Step 2: Create an Empty 3D Document

```csharp
// ExStart:CreateEmpty3DDocument

// Create an object of the Scene class
Scene scene = new Scene();

// Save the 3D scene document in FBX format
scene.Save(output);

// ExEnd:CreateEmpty3DDocument
```

### Step 3: Display the Result

```csharp
Console.WriteLine("\nAn empty 3D document created successfully.\nFile saved at " + output);
```

Congratulations! You've just created your first empty 3D document using Aspose.3D for .NET. Feel free to explore more features and functionalities to unleash the full potential of this library.

## Conclusion

In this tutorial, we covered the basics of creating an empty 3D document using Aspose.3D for .NET. As you continue your journey with 3D development, refer to the [documentation](https://reference.aspose.com/3d/net/) for in-depth insights and advanced features.

## FAQ's

### Q1: Is Aspose.3D for .NET suitable for beginners?

A1: Yes, Aspose.3D for .NET provides a user-friendly interface, making it accessible for both beginners and experienced developers.

### Q2: Can I try Aspose.3D for .NET before purchasing?

A2: Absolutely! You can access a free trial [here](https://releases.aspose.com/).

### Q3: How can I get support for Aspose.3D for .NET?

A3: Visit the [Aspose.3D forum](https://forum.aspose.com/c/3d/18) to seek assistance and connect with the community.

### Q4: Are temporary licenses available for Aspose.3D for .NET?

A4: Yes, you can obtain a temporary license [here](https://purchase.aspose.com/temporary-license/).

### Q5: Where can I purchase Aspose.3D for .NET?

A5: You can purchase the library [here](https://purchase.aspose.com/buy).
