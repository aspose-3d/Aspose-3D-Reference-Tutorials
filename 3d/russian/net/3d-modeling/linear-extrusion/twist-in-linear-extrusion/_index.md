---
date: 2026-03-23
description: Узнайте, как создать выдавливание с закрутом, используя Aspose.3D для
  .NET. Это пошаговое руководство охватывает техники линейного выдавливания с закрутом.
linktitle: Twist in Linear Extrusion
second_title: Aspose.3D .NET API
title: Как создать экструзию с круткой в линейной экструзии
url: /ru/net/3d-modeling/linear-extrusion/twist-in-linear-extrusion/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Как создать экструзию со скручиванием в линейной экструзии

## Introduction

Если вы разрабатываете .NET‑приложения, которым нужны впечатляющие 3D‑визуализации, вы быстро поймёте, что **как создать экструзию** — это базовый навык. Aspose.3D for .NET предоставляет чистый, высокопроизводительный API для преобразования простых 2‑D профилей в сложные 3‑D модели — особенно когда к ним добавляется скручивание. В этом руководстве мы пройдём каждый шаг, от настройки сцены до сохранения окончательного OBJ‑файла, чтобы вы могли увидеть силу линейной экструзии со скручиванием в действии.

## Quick Answers
- **What is the primary class for extrusion?** `LinearExtrusion`
- **Which property adds rotation?** `Twist`
- **How many slices give smooth results?** Around 100 slices (adjust as needed)
- **Can I use other shapes?** Yes, any `IProfile` such as circles, polygons, or custom curves
- **What file format is used in the example?** Wavefront OBJ (`.obj`)

## Prerequisites

Before we dive in, make sure you have the following:

- Aspose.3D for .NET installed. If you haven’t downloaded it yet, get it **[here](https://releases.aspose.com/3d/net/)**.
- A working .NET development environment (Visual Studio, VS Code, or any IDE you prefer).
- Basic familiarity with C# syntax and object‑oriented concepts.

## Import Namespaces

In any .NET project, the proper use of namespaces is crucial. Begin by importing the necessary namespaces to leverage the functionalities of Aspose.3D effectively. Here's a snippet to guide you:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Step‑by‑Step Guide

### Step 1: Initialize the Base Profile

We start by defining the shape that will be extruded. In this example we use a rectangle with a small rounding radius to give the edges a subtle curve.

```csharp
// Initialize the base profile to be extruded
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

### Step 2: Create a 3D Scene

A `Scene` object acts as the canvas where all 3‑D entities live. Think of it as the stage for your extrusion.

```csharp
// Create a scene 
Scene scene = new Scene();
```

### Step 3: Add Left and Right Nodes

Nodes let you organize objects hierarchically. We’ll create two sibling nodes—one for a straight extrusion and another for a twisted version.

```csharp
// Create left node
var left = scene.RootNode.CreateChildNode();
// Create right node
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
```

### Step 4: Perform Linear Extrusion with Twist on the Left Node

The `Twist` property controls how much the profile rotates while it’s being extruded. Setting it to **0** gives a classic straight extrusion.

```csharp
// Twist property defines the degree of the rotation while extruding the profile
// Perform linear extrusion on the left node using twist and slices property
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 0, Slices = 100 });
```

### Step 5: Perform Linear Extrusion with Twist on the Right Node

Now we apply a 90‑degree twist to the same profile. This demonstrates the **linear extrusion twist** effect clearly.

```csharp
// Perform linear extrusion on the right node using twist and slices property
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 90, Slices = 100 });
```

### Step 6: Save the 3D Scene

Finally, export the scene to a format you can view in any 3‑D viewer. The example uses Wavefront OBJ, but Aspose.3D supports many other formats as well.

```csharp
// Save 3D scene
scene.Save("Your Output Directory" + "TwistInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Why Use Linear Extrusion with a Twist?

- **Rapid prototyping:** Turn 2‑D sketches into 3‑D parts without manual modeling.
- **Design flexibility:** Adjust the `Twist` value to create spirals, helical ribs, or decorative features.
- **Performance‑friendly:** The `Slices` parameter lets you balance visual fidelity and runtime speed.

## Common Issues & Tips

- **Too many slices:** While 100 slices look smooth, extremely high values may slow down rendering. Test with lower counts if performance becomes a concern.
- **Negative twist values:** A negative `Twist` rotates in the opposite direction—useful for mirrored designs.
- **File paths:** Ensure the output directory exists and you have write permissions; otherwise `scene.Save` will throw an exception.

## Conclusion

In this tutorial we’ve shown **how to create extrusion** with a twist using Aspose.3D for .NET. By adjusting the `Twist` and `Slices` properties you can generate a wide variety of shapes, from simple twisted bars to complex helical structures, all with just a few lines of code.

## Frequently Asked Questions

**Q: Can I apply linear extrusion with a twist to other shapes?**  
A: Absolutely! Any class that implements `IProfile`—such as `CircleShape`, `PolygonShape`, or a custom spline—can be extruded with a twist.

**Q: What does the `Twist` property actually represent?**  
A: It specifies the total rotation angle (in degrees) applied to the profile over the extrusion length.

**Q: Will increasing the number of slices affect memory usage?**  
A: Yes, more slices generate more vertices and faces, which consumes additional memory and may impact performance on low‑end devices.

**Q: Can I combine linear extrusion with other Aspose.3D features?**  
A: Definitely. You can apply materials, textures, or even Boolean operations after extrusion to create even richer models.

**Q: Where can I get help or discuss ideas with other developers?**  
A: Join the Aspose.3D community at **[Aspose Forum](https://forum.aspose.com/c/3d/18)** for support, samples, and discussions.

---

**Last Updated:** 2026-03-23  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}