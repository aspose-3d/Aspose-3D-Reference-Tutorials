---
title: Applying Twist in Linear Extrusion with Aspose.3D for Java
linktitle: Applying Twist in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
description: Learn how to add a twist to your 3D models using Aspose.3D for Java. Follow our step-by-step guide for enhanced linear extrusion effects.
type: docs
weight: 14
url: /java/linear-extrusion/applying-twist/
---
## Introduction

Welcome to this step-by-step tutorial on applying a twist in linear extrusion using Aspose.3D for Java. Aspose.3D is a powerful Java library that enables developers to work with 3D file formats, offering robust functionality for creating, manipulating, and rendering 3D scenes. In this tutorial, we will explore how to apply a twist effect during the linear extrusion process to enhance your 3D models.

## Prerequisites

Before diving into the tutorial, ensure you have the following prerequisites in place:

- Java Development Environment: Make sure you have Java installed on your system.
- Aspose.3D Library: Download and install the Aspose.3D library for Java from the [download link](https://releases.aspose.com/3d/java/).
- Documentation: Refer to the [Aspose.3D documentation](https://reference.aspose.com/3d/java/) for comprehensive guidance.

## Import Packages

Before starting the coding process, import the necessary packages into your Java project. Here's an example of how to do this:

```java
package examples.LinearExtrusion;

import com.aspose.threed.*;


import java.io.IOException;
```

## Step 1: Set Document Directory

Begin by setting the document directory where your 3D scene will be saved.

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## Step 2: Initialize Base Profile

Initialize the base profile to be extruded. In this example, we use a rectangle shape with a rounding radius.

```java
// ExStart:InitializeBaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:InitializeBaseProfile
```

## Step 3: Create a Scene

Create a 3D scene to host the extruded nodes.

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
```

## Step 4: Create Nodes

Create left and right nodes within the scene. Adjust the translation of the left node.

```java
// ExStart:CreateNodes
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CreateNodes
```

## Step 5: Perform Linear Extrusion with Twist

Perform linear extrusion on both left and right nodes, applying twist and slices properties.

```java
// ExStart:LinearExtrusionWithTwist
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd:LinearExtrusionWithTwist
```

## Step 6: Save 3D Scene

Save the 3D scene in the Wavefront OBJ file format.

```java
// ExStart:Save3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:Save3DScene
```

## Conclusion

Congratulations! You have successfully applied a twist in linear extrusion using Aspose.3D for Java. This tutorial provided a detailed, step-by-step guide to help you enhance your 3D modeling capabilities.

## FAQ's

### Q1: Can I use Aspose.3D for Java to work with other 3D file formats?

A1: Yes, Aspose.3D supports various 3D file formats, allowing you to import, export, and manipulate diverse file types.

### Q2: Where can I find support for Aspose.3D for Java?

A2: Visit the [Aspose.3D forum](https://forum.aspose.com/c/3d/18) for community support and discussions.

### Q3: Is there a free trial available for Aspose.3D for Java?

A3: Yes, you can access the free trial version from [here](https://releases.aspose.com/).

### Q4: How can I obtain a temporary license for Aspose.3D for Java?

A4: Get a temporary license from the [temporary license page](https://purchase.aspose.com/temporary-license/).

### Q5: Where can I purchase Aspose.3D for Java?

A5: Purchase Aspose.3D for Java from the [buying page](https://purchase.aspose.com/buy).
