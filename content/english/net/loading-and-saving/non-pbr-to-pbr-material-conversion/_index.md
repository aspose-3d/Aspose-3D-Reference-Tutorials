---
title: Loading and Saving -  Non-PBR to PBR Material Conversion
linktitle: Loading and Saving -  Non-PBR to PBR Material Conversion
second_title: Aspose.3D .NET API
description: Explore Aspose.3D for .NET - Convert Non-PBR to PBR materials effortlessly. Comprehensive tutorial and powerful API.
type: docs
weight: 16
url: /net/loading-and-saving/non-pbr-to-pbr-material-conversion/
---
## Introduction

Welcome to this step-by-step guide on using Aspose.3D for .NET to convert Non-PBR (Physically Based Rendering) to PBR materials. Aspose.3D is a powerful API that allows developers to work seamlessly with 3D file formats in their .NET applications.

## Prerequisites

Before we dive into the tutorial, ensure you have the following prerequisites:

- Aspose.3D for .NET: Make sure you have the Aspose.3D for .NET library installed. You can find the download link [here](https://releases.aspose.com/3d/net/).

- Basic Understanding of C#: This tutorial assumes you have a fundamental understanding of C# programming.

- IDE (Integrated Development Environment): Choose your preferred IDE for .NET development, such as Visual Studio.

## Import Namespaces

In your C# code, start by importing the necessary namespaces:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Step 1: Initialize a New 3D Scene

Begin by creating a new 3D scene using the following code:

```csharp
// ExStart:Non_PBRtoPBRMaterial
// initialize a new 3D scene
var scene = new Scene();
```

## Step 2: Create a 3D Object

Next, create a 3D object, for example, a box:

```csharp
var box = new Box();
scene.RootNode.CreateChildNode("box1", box).Material = new PhongMaterial() { DiffuseColor = new Vector3(1, 0, 1) };
```

## Step 3: Configure Material Conversion

Set up material conversion options for Non-PBR to PBR conversion:

```csharp
GltfSaveOptions options = new GltfSaveOptions(FileFormat.GLTF2);
options.MaterialConverter = delegate (Material material)
{
    PhongMaterial phongMaterial = (PhongMaterial)material;
    return new PbrMaterial() { Albedo = new Vector3(phongMaterial.DiffuseColor.x, phongMaterial.DiffuseColor.y, phongMaterial.DiffuseColor.z) };
};
```

## Step 4: Save in GLTF 2.0 Format

Save the converted scene in GLTF 2.0 format:

```csharp
scene.Save("Your Output Directory" + "Non_PBRtoPBRMaterial_Out.gltf", options);
// ExEnd:Non_PBRtoPBRMaterial
```

Repeat these steps as needed for your specific use case, ensuring each detail is configured correctly.

## Conclusion

Congratulations! You've successfully learned how to convert Non-PBR to PBR materials using Aspose.3D for .NET. This powerful tool opens up endless possibilities for 3D graphics manipulation in your .NET applications.

## FAQ's

### Q1: Is Aspose.3D compatible with all 3D file formats?

A1: Yes, Aspose.3D supports a wide range of 3D file formats, providing flexibility in your projects.

### Q2: Can I use Aspose.3D for commercial applications?

A2: Absolutely! Aspose.3D is a commercial product, and you can purchase it [here](https://purchase.aspose.com/buy).

### Q3: Do I need a temporary license for testing?

A3: Yes, you can obtain a temporary license for testing purposes [here](https://purchase.aspose.com/temporary-license/).

### Q4: Where can I find support for Aspose.3D?

A4: Visit the [Aspose.3D forum](https://forum.aspose.com/c/3d/18) for community support and discussions.

### Q5: Is there a free trial available?

A5: Yes, you can explore a free trial version [here](https://releases.aspose.com/).
