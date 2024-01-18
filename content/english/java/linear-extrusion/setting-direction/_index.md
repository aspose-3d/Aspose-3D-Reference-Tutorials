---
title: Setting Direction in Linear Extrusion with Aspose.3D for Java
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
description: Master linear extrusion with Aspose.3D for Java! Follow our guide for seamless 3D programming. Download now for a captivating experience.
type: docs
weight: 12
url: /java/linear-extrusion/setting-direction/
---
## Introduction

Welcome to our step-by-step guide on setting direction in linear extrusion using Aspose.3D for Java. Aspose.3D is a powerful Java library that allows developers to work seamlessly with 3D files and scenes. In this tutorial, we will focus on the specific task of setting direction in linear extrusion, enhancing your proficiency in 3D programming.

## Prerequisites

Before we dive into the tutorial, make sure you have the following prerequisites in place:

- Basic knowledge of Java programming language.
- Aspose.3D library installed. You can download it from [here](https://releases.aspose.com/3d/java/).
- An integrated development environment (IDE) for Java, such as Eclipse or IntelliJ.

## Import Packages

Ensure that you import the necessary packages to kickstart your project:

```java


import com.aspose.threed.*;


import java.io.IOException;
```

## Step 1: Initialize Base Profile

Begin by initializing the base profile to be extruded. In this example, we use a `RectangleShape` with a rounding radius of 0.3:

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Step 2: Create a Scene

Next, create a 3D scene to contain the extruded objects:

```java
Scene scene = new Scene();
```

## Step 3: Create Nodes

Create left and right nodes within the scene:

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Step 4: Perform Linear Extrusion on Left Node

Perform linear extrusion on the left node using the `LinearExtrusion` class with specified parameters such as twist and slices:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Step 5: Perform Linear Extrusion on Right Node with Direction

Perform linear extrusion on the right node, introducing the `setDirection` property to define the extrusion direction:

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Step 6: Save 3D Scene

Save the 3D scene to the desired file format. In this example, we save it as a Wavefront OBJ file:

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Conclusion

Congratulations! You've successfully learned how to set direction in linear extrusion using Aspose.3D for Java. This tutorial enhances your skills in 3D programming and opens up new possibilities for creative projects.

## FAQ's

### Q1: Can I use Aspose.3D with other programming languages?

A1: Aspose.3D supports various programming languages, including .NET and Java.

### Q2. Is there a free trial available for Aspose.3D?

A2: Yes, you can explore the features of Aspose.3D with a free trial [here](https://releases.aspose.com/).

### Q3: Where can I find detailed documentation for Aspose.3D for Java?

A3: The comprehensive documentation is available [here](https://reference.aspose.com/3d/java/).

### Q4: How can I get support for Aspose.3D?

A4: Visit the [Aspose.3D forum](https://forum.aspose.com/c/3d/18) for any assistance or queries.

### Q5: Are temporary licenses available for Aspose.3D?

A5: Yes, you can obtain a temporary license [here](https://purchase.aspose.com/temporary-license/).
