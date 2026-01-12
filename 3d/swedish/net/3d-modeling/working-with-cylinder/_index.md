---
date: 2026-01-12
description: Lär dig hur du skapar en shear bottom cylinder och hur du exporterar
  3D-modellen i OBJ-format med Aspose.3D för .NET. Följ den här steg‑för‑steg‑guiden
  för att behärska 3D-modellering.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: Hur man skapar en shear bottom cylinder med Aspose.3D för .NET
url: /sv/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Customized Shear Bottom Cylinder

## Introduction
Välkommen till vår omfattande guide där **du kommer att lära dig hur du skapar shear bottom cylinder**‑modeller med Aspose.3D för .NET. Oavsett om du bygger en spelresurs, en mekanisk del eller en visuell demo, visar den här tutorialen exakt hur du formar en cylinders botten, applicerar en shear och slutligen **exporterar 3D‑modellen OBJ**‑filen för användning i någon efterföljande pipeline. Låt oss gå igenom varje steg tillsammans, så att du kan börja producera anpassad geometri på några minuter.

## Quick Answers
- **Vad är en shear bottom cylinder?** En cylinder vars bottenyta är lutad (sheared) snarare än plan.  
- **Vilket bibliotek används?** Aspose.3D för .NET.  
- **Hur exporterar jag modellen?** Använd `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Behöver jag en licens?** En provversion finns tillgänglig; en kommersiell licens krävs för produktion.  
- **Vilka förutsättningar krävs?** .NET‑utvecklingsmiljö och Aspose.3D NuGet‑paketet.

## What is a shear bottom cylinder?
A shear bottom cylinder is a standard cylindrical mesh whose bottom face has been transformed by a shear operation. This lets you create angled bases, ramps, or custom connectors without manually editing vertices.

## Why use Aspose.3D for this task?
- **Full control** over geometry parameters (radius, height, segments).  
- **Built‑in shear support** via the `ShearBottom` property, saving you from low‑level mesh manipulation.  
- **One‑click export** to popular formats like OBJ, FBX, and STL, making integration with other tools seamless.

## Prerequisites
Before we dive in, make sure you have:

- Basic knowledge of C# and .NET.
- Aspose.3D for .NET installed. You can download it **[here](https://releases.aspose.com/3d/net/)**.
- A .NET‑compatible IDE (Visual Studio, Rider, or VS Code).

## Import Namespaces
In your C# file, start by importing the necessary namespaces:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Step 1: Create a Scene
First, instantiate a new 3‑D scene that will hold all of our objects.

```csharp
Scene scene = new Scene();
```

## Step 2: Create Cylinder 1
Create the primary cylinder that we’ll customise with a sheared bottom.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Step 3: Customize Shear Bottom for Cylinder 1
Apply the shear, enable fan‑generation, and adjust other properties to achieve the desired shape.

```csharp
// Shear 47.5deg in the xy plane (z‑axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## Step 4: Add Cylinder 1 to the Scene
Place the customized cylinder in the scene and move it a little to the right so we can see both objects side‑by‑side.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## Step 5: Create Cylinder 2
Create a second, plain cylinder for comparison.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Step 6: Add Cylinder 2 to the Scene
Add the second cylinder without any custom shear—this helps illustrate the effect of the previous steps.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## Step 7: Save the Scene
Finally, export the whole scene as an OBJ file so you can open it in Blender, Maya, or any other 3‑D viewer.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## Common Issues & Tips
- **Shear values**: The `Vector2` takes X and Y shear factors. A value of `0.83` corresponds to roughly 47.5°, but you can adjust it for different angles.
- **Export path**: Ensure the folder you specify exists and you have write permissions; otherwise `scene.Save` will throw an exception.
- **Performance**: For very high‑segment cylinders, consider reducing the segment count (`20` in the example) to keep the OBJ file size manageable.

## Frequently Asked Questions

### Is Aspose.3D for .NET suitable for beginners?
Absolutely! Aspose.3D for .NET offers a user‑friendly API, making it accessible for both beginners and experienced developers.

### Can I apply different shearing angles to cylinders?
Yes, you can customize the `ShearBottom` for each cylinder individually, allowing you to achieve unique effects.

### Is there a trial version available?
Yes, you can explore the free trial version **[here](https://releases.aspose.com/)**.

### Where can I find additional support?
Visit the **[Aspose.3D forum](https://forum.aspose.com/c/3d/18)** for community support and discussions.

### How can I obtain a temporary license?
Get your temporary license **[here](https://purchase.aspose.com/temporary-license/)**.

**Additional Q&A**

**Q: How do I change the export format to FBX?**  
A: Replace `FileFormat.WavefrontOBJ` with `FileFormat.FBX` in the `scene.Save` call.

**Q: Can I animate the cylinder after exporting?**  
A: OBJ does not support animation; use FBX or GLTF if you need animated data.

**Q: What if I need a larger cylinder radius?**  
A: Adjust the first two parameters of the `Cylinder` constructor (e.g., `new Cylinder(4, 4, …)`).

## Conclusion
You’ve now mastered how to **create shear bottom cylinder** models and export them as OBJ files using Aspose.3D for .NET. Experiment with different shear values, segment counts, and export formats to fit your project’s needs. Happy modeling!

---

**Last Updated:** 2026-01-12  
**Tested With:** Aspose.3D for .NET 24.11 (latest at time of writing)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}