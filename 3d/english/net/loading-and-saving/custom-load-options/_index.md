---
title: Custom Load Options
linktitle: Custom Load Options
second_title: Aspose.3D .NET API
description: Explore Aspose.3D for .NET the ultimate solution for seamless 3D model loading and saving.
weight: 15
url: /net/loading-and-saving/custom-load-options/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Custom Load Options

## Introduction

Welcome to the world of Aspose.3D for .NET – a powerful library that empowers developers to work seamlessly with 3D files. In this tutorial, we'll delve into the intricacies of loading and saving 3D models, focusing on custom load options. Whether you are a seasoned developer or a newcomer, this guide will walk you through the process step by step, ensuring you harness the full potential of Aspose.3D for .NET.

## Prerequisites

Before we embark on this journey, make sure you have the following prerequisites in place:

- Aspose.3D for .NET: Ensure you have the library installed. You can download it [here](https://releases.aspose.com/3d/net/).

- Document Directory: Create a directory to store your 3D model files.

Now that you have the essentials, let's dive into the exciting world of 3D model manipulation!

## Import Namespaces

First things first, let's import the necessary namespaces. This will set the stage for our journey into the Aspose.3D realm.

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
```

## Loading and Saving - Custom Load Options

### Step 1: Loading Discreet3DS Files

```csharp
private static void Discreet3DSLoadOption()
{
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();

    // Set custom options
    loadOpts.ApplyAnimationTransform = true;
    loadOpts.FlipCoordinateSystem = true;
    loadOpts.GammaCorrectedColor = true;
    loadOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Load file with the load options
    var scene = Scene.FromFile("test.3ds", loadOpts);
}
```

### Step 2: Loading OBJ Files

```csharp
private static void ObjLoadOption()
{
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();

    // Set custom options
    loadObjOpts.EnableMaterials = true;
    loadObjOpts.FlipCoordinateSystem = true;
    loadObjOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Load file with the load options
    var scene = Scene.FromFile("test.obj", loadObjOpts);

}
```

### Step 3: Loading STL Files

```csharp
private static void STLLoadOption()
{
    // The path to the documents directory.
    StlLoadOptions loadSTLOpts = new StlLoadOptions();

    // Set custom options
    loadSTLOpts.FlipCoordinateSystem = true;
    loadSTLOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Load file with the load options
    var scene = Scene.FromFile("test.stl", loadSTLOpts);
}
```

### Step 4: Loading U3D Files

```csharp
private static void U3DLoadOption()
{
    // The path to the documents directory.
    string dataDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();

    // Set custom options
    loadU3DOpts.FlipCoordinateSystem = true;
    loadU3DOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Load file with the load options
    var scene = Scene.FromFile("test.u3d", loadU3DOpts);
}
```

### Step 5: Loading glTF Files

```csharp
private static void glTFLoadOptions()
{
    // The path to the documents directory.
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();

    // Set custom options
    loadOpt.FlipTexCoordV = true;
    scene.Open("Duck.gltf", loadOpt);
}
```

### Step 6: Loading PLY Files

```csharp
private static void PlyLoadOptions()
{
    // The path to the documents directory.
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();

    // Set custom options
    loadPLYOpts.FlipCoordinateSystem = true;
    scene.Open("vase-v2.ply", loadPLYOpts);
}
```

### Step 7: Loading FBX Files

```csharp
private static void FBXLoadOptions()
{
    // The path to the documents directory.
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions() { KeepBuiltinGlobalSettings = true };

    // Set custom options
    scene.Open("test.FBX", opt);

    // Output properties defined in GlobalSettings in FBX file
    foreach (Property property in scene.RootNode.AssetInfo.Properties)
    {
        Console.WriteLine(property);
    }
}
```

## Conclusion

Congratulations! You've successfully navigated through the intricate world of loading and saving 3D models using Aspose.3D for .NET. This tutorial covered various file formats and their custom load options, empowering you to manipulate 3D assets with ease.

## FAQ's

### Q1: Is Aspose.3D for .NET suitable for beginners?

A1: Absolutely! Aspose.3D for .NET provides a user-friendly interface, making it accessible for developers of all levels.

### Q2: Can I use Aspose.3D for commercial projects?

A2: Yes, Aspose.3D for .NET comes with a commercial license, allowing you to use it in your projects.

### Q3: Are there any limitations on the file formats supported?

A3: Aspose.3D for .NET supports a wide range of popular 3D file formats, including OBJ, STL, FBX, and more. Refer to the [documentation](https://reference.aspose.com/3d/net/) for a comprehensive list.

### Q4: Is there a trial version available?

A4: Yes, you can explore the capabilities of Aspose.3D for .NET by downloading the [free trial](https://releases.aspose.com/).

### Q5: Where can I seek support for Aspose.3D for .NET?

A5: Visit the [Aspose.3D forum](https://forum.aspose.com/c/3d/18) for community support and assistance.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
