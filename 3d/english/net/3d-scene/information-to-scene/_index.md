---
title: How to Add Vendor Info and Save FBX Scene Using Aspose.3D
linktitle: Extracting Information to Scene Assets
second_title: Aspose.3D .NET API
description: Learn how to add vendor information to a 3D scene and how to save FBX files using Aspose.3D for .NET. Follow this step‑by‑step guide with ready‑to‑run code.
weight: 10
url: /net/3d-scene/information-to-scene/
date: 2026-03-26
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# How to Add Vendor Info and Save FBX Scene Using Aspose.3D

## Introduction

Welcome to this comprehensive tutorial that shows **how to add vendor** details to a 3D scene and then **how to save FBX** files with Aspose.3D for .NET. Whether you’re building architectural visualizations, game assets, or engineering models, embedding vendor and application metadata makes your scenes more informative and easier to manage downstream. Let’s walk through the process step by step.

## Quick Answers
- **What does “add vendor” mean?** It stores the application and vendor names inside the scene’s AssetInfo block.  
- **Which format supports vendor info?** FBX (ASCII or binary) retains the metadata when saved.  
- **How to save FBX?** Use `scene.Save(path, FileFormat.FBX7500ASCII)` or the binary equivalent.  
- **Do I need a license?** A free trial works for development; a commercial license is required for production.  
- **Can I change measurement units?** Yes, set `AssetInfo.UnitName` and `AssetInfo.UnitScaleFactor`.

## What is “how to add vendor” in a 3D scene?
Adding vendor information means populating the `AssetInfo` properties of a `Scene` object. These properties travel with the file, allowing any consumer of the FBX file to see which application created it and who the vendor is.

## Why add vendor information?
- **Traceability:** Quickly identify the source of a model in large pipelines.  
- **Compliance:** Some industries require explicit vendor tagging for asset management.  
- **Automation:** Scripts can filter or process files based on vendor metadata.

## Prerequisites

- Aspose.3D for .NET installed. You can download it from the [Aspose.3D for .NET page](https://releases.aspose.com/3d/net/).

## Import Namespaces

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## How to Add Vendor Information

### Step 1: Initialize a 3D Scene

```csharp
Scene scene = new Scene();
```

Creating a fresh `Scene` gives you a clean canvas to work with.

### Step 2: Set Application and Vendor Information

```csharp
scene.AssetInfo.ApplicationName = "Egypt";
scene.AssetInfo.ApplicationVendor = "Manualdesk";
```

Here we demonstrate **how to add vendor** data by assigning meaningful strings to `ApplicationName` and `ApplicationVendor`.

### Step 3: Define Measurement Units

```csharp
scene.AssetInfo.UnitName = "pole";
scene.AssetInfo.UnitScaleFactor = 0.6;
```

Specifying the unit system ensures that anyone opening the FBX file interprets dimensions correctly. In this example, one “pole” equals 60 cm.

## How to Save FBX Scene

### Step 4: Save the Scene (how to save fbx)

```csharp
var output = "Your Output Directory" + "InformationToScene.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

This line shows **how to save fbx** using the ASCII version of FBX 7.5.0. If you prefer binary, replace `FBX7500ASCII` with `FBX7500Binary`.

> **Pro tip:** Keep the file extension `.fbx` consistent with the format you choose; otherwise some viewers may misinterpret the content.

### Step 5: Display Success Message

```csharp
Console.WriteLine("\nAsset information added successfully to Scene.\nFile saved at " + output);
```

A friendly console message confirms that the scene, complete with vendor metadata, has been written to disk.

## Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| **Vendor info not appearing in viewer** | Ensure you saved the file as **FBX ASCII** or **Binary**; some older viewers only read one format. |
| **Path contains spaces** | Wrap the path in quotes or use `Path.Combine` to build a safe file path. |
| **Unit scale looks wrong** | Double‑check `UnitScaleFactor`; it’s a multiplier relative to meters. |
| **License exception** | Use the free trial for testing; obtain a full license for production builds. |

## Frequently Asked Questions

**Q: Can I use Aspose.3D for .NET with other programming languages?**  
A: Aspose.3D primarily supports .NET languages, but you can explore interoperability options for other languages.

**Q: Is there a free trial available for Aspose.3D for .NET?**  
A: Yes, you can access the free trial [here](https://releases.aspose.com/).

**Q: How do I get support for Aspose.3D‑related queries?**  
A: Visit the [Aspose.3D forum](https://forum.aspose.com/c/3d/18) for community and support.

**Q: Can I purchase a temporary license for Aspose.3D for .NET?**  
A: Yes, you can acquire a temporary license [here](https://purchase.aspose.com/temporary-license/).

**Q: Where can I find detailed documentation for Aspose.3D for .NET?**  
A: Refer to the [documentation](https://reference.aspose.com/3d/net/) for in‑depth information.

---

**Last Updated:** 2026-03-26  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}