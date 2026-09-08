---
date: 2026-09-08
description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
  This step‑by‑step guide shows setting the application name, measurement units, and
  retrieving 3D scene information.
images:
- /java/3d-scenes-and-models/get-scene-information/og-image.png
keywords:
- how to define units
- export scene to fbx
- how to set application name
- define measurement units
lastmod: 2026-09-08
linktitle: How to Save FBX and Retrieve 3D Scene Info in Java
og_description: Learn how to define units and export a scene to FBX in Java with Aspose.3D.
  The guide covers setting application name, measurement units, and retrieving 3D
  scene info in a few steps.
og_image_alt: Guide showing how to define units and export a 3D scene to FBX using
  Aspose.3D Java
og_title: How to define units and export scene to FBX in Java
schemas:
- author: Aspose
  dateModified: '2026-09-08'
  description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  headline: How to define units and export scene to FBX in Java
  type: TechArticle
- description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  name: How to define units and export scene to FBX in Java
  steps:
  - name: initialize a 3D scene
    text: The `Scene` class is Aspose.3D's top‑level container that represents an
      entire 3D scene, including geometry, lights, cameras, and metadata. First, create
      an empty `Scene` object. This will be the container for all geometry, lights,
      cameras, and asset metadata.
  - name: define measurement units
    text: The unit system determines the real‑world scale of the scene; Aspose.3D
      lets you specify a unit name and a scale factor relative to meters. In this
      example we use an ancient Egyptian unit called “pole” with a custom scale factor.
      > **Tip:** Adjust `unitScaleFactor` to match the real‑world size of yo
  - name: export scene to FBX
    text: Now that the asset information is attached, we save the scene as an FBX
      file. The `FileFormat.FBX7500ASCII` option produces a human‑readable ASCII FBX,
      which is handy for debugging. > **Remember:** Replace `"Your Document Directory"`
      with an absolute path or a path relative to your project's working
  type: HowTo
- questions:
  - answer: Replace `FileFormat.FBX7500ASCII` with `FileFormat.FBX7500` when calling
      `scene.save(...)`.
    question: How do I change the output format to binary FBX?
  - answer: Yes, use `scene.getUserData().add("Key", "Value")` to embed additional
      key‑value pairs.
    question: Can I add custom user‑defined metadata beyond the built‑in asset fields?
  - answer: It does. Simply change the `FileFormat` enum to `OBJ` or `GLTF2` as needed.
    question: Does Aspose.3D support other export formats like OBJ or GLTF?
  - answer: Aspose.3D for Java supports Java 8 and later.
    question: What version of Java is required?
  - answer: Absolutely. Load the file with `new Scene("input.fbx")`, modify `scene.getAssetInfo()`,
      then save.
    question: Is it possible to load an existing FBX, modify its asset info, and resave?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- export scene to fbx
- Aspose.3D
- Java 3D
- define units
- 3D asset metadata
title: How to define units and export scene to FBX in Java
url: /java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# How to define units and export scene to FBX in Java

## Introduction

If you’re looking for a clear, hands‑on guide on **how to define units** and **export a scene to FBX** while extracting useful metadata from your 3D scenes, you’ve come to the right place. In this tutorial we’ll walk through every step using the **Aspose.3D for Java** library: from creating a scene, **setting the application name**, **defining measurement units**, to finally **exporting the scene to FBX**. By the end you’ll have a ready‑to‑use FBX file that carries the asset information you need for downstream pipelines.

## Quick answers
- **What is the primary goal?** Export a scene to FBX that contains custom asset information.  
- **Which library is used?** Aspose.3D for Java.  
- **Do I need a license?** A free trial works for development; a commercial license is required for production.  
- **Can I change the measurement units?** Yes – use `setUnitName` and `setUnitScaleFactor`.  
- **Where is the output saved?** To the path you specify in `scene.save(...)`.  

## Prerequisites

Before we start, make sure you have:

- A solid grasp of core Java syntax.  
- **Aspose.3D for Java** downloaded and added to your project (you can get it from the official) [Aspose 3D download page](https://releases.aspose.com/3d/java/).  
- Your favourite Java IDE (IntelliJ IDEA, Eclipse, NetBeans, etc.) properly configured.

## Import packages

In your Java source file, import the Aspose.3D classes that provide scene handling and file‑format support.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Pro tip:** Keep the import list minimal to avoid unnecessary dependencies and improve compile times.

## What is the process for saving an FBX file?

To save a scene as an FBX file you create a `Scene`, set any desired asset metadata, define the measurement unit, and then call `scene.save(path, FileFormat.FBX7500ASCII)`. This sequence writes geometry, materials, and metadata into an ASCII FBX that can be inspected or imported by downstream tools.

### Step 1: initialize a 3D scene

The `Scene` class is Aspose.3D's top‑level container that represents an entire 3D scene, including geometry, lights, cameras, and metadata. First, create an empty `Scene` object. This will be the container for all geometry, lights, cameras, and asset metadata.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### How to set application name in Java

The `AssetInfo` object stores metadata such as application name, vendor, and version for the scene. Adding custom metadata helps downstream tools identify the source of the file. Use the `AssetInfo` object to **set the application name** (and vendor) before you save the file.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Why this matters:** Many pipelines filter or tag assets based on the originating application, making this step essential for large projects.

### Step 3: define measurement units

The unit system determines the real‑world scale of the scene; Aspose.3D lets you specify a unit name and a scale factor relative to meters. In this example we use an ancient Egyptian unit called “pole” with a custom scale factor.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Tip:** Adjust `unitScaleFactor` to match the real‑world size of your models; 1.0 represents a 1‑to‑1 mapping with the chosen unit.

### Step 4: export scene to FBX

Now that the asset information is attached, we save the scene as an FBX file. The `FileFormat.FBX7500ASCII` option produces a human‑readable ASCII FBX, which is handy for debugging.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
// ExEnd:AddAssetInformationToScene
```

> **Remember:** Replace `"Your Document Directory"` with an absolute path or a path relative to your project's working directory.

## Why export scene to FBX with Aspose.3D?

Aspose.3D supports **50+ input and output formats** and can process multi‑hundred‑page scenes without loading the entire file into memory, giving you full control over the exported file—metadata, units, and geometry—without needing a heavyweight 3D authoring application. This makes automated asset generation, batch processing, and server‑side conversions fast and reliable.

## Common use cases

- **Game asset pipelines** – embed creator information directly in FBX files for version tracking.  
- **Architectural visualization** – store project‑specific units to avoid scaling errors when importing into rendering engines.  
- **Automated reporting** – generate FBX files on‑the‑fly with metadata that downstream analytics tools can read.  
- **Cloud‑based 3D services** – programmatically create and export scenes without a GUI, perfect for SaaS platforms.

## Troubleshooting & tips

| Issue | Solution |
|-------|----------|
| **File not found after save** | Verify that `MyDir` points to an existing folder and that your application has write permissions. |
| **Units appear incorrect in external viewer** | Double‑check `unitScaleFactor`; some viewers expect meters as the base unit. |
| **Asset metadata missing** | Ensure you call `scene.getAssetInfo()` **before** saving; changes made after `save()` won’t be persisted. |
| **Performance bottleneck on large scenes** | Use `scene.optimize()` before saving to reduce memory usage. |
| **ASCII FBX is too large** | Switch to binary FBX by using `FileFormat.FBX7500` (see FAQ). |

## Frequently asked questions

**Q: How do I change the output format to binary FBX?**  
A: Replace `FileFormat.FBX7500ASCII` with `FileFormat.FBX7500` when calling `scene.save(...)`.

**Q: Can I add custom user‑defined metadata beyond the built‑in asset fields?**  
A: Yes, use `scene.getUserData().add("Key", "Value")` to embed additional key‑value pairs.

**Q: Does Aspose.3D support other export formats like OBJ or GLTF?**  
A: It does. Simply change the `FileFormat` enum to `OBJ` or `GLTF2` as needed.

**Q: What version of Java is required?**  
A: Aspose.3D for Java supports Java 8 and later.

**Q: Is it possible to load an existing FBX, modify its asset info, and resave?**  
A: Absolutely. Load the file with `new Scene("input.fbx")`, modify `scene.getAssetInfo()`, then save.

---

**Last Updated:** 2026-09-08  
**Tested With:** Aspose.3D for Java 24.11  
**Author:** Aspose

## Related Tutorials

- [Reduce 3D File Size – Compress Scenes with Aspose.3D for Java](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [How to set vector3 color java: Change Diffuse Color and Manage 3D Properties in Java Scenes using Aspose.3D](/3d/java/3d-scenes-and-models/managing-3d-properties-scenes/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}