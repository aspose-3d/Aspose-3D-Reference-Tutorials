---
title: Controlling Center in Linear Extrusion with Aspose.3D for Java
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
description: Explore the world of 3D graphics in Java with Aspose.3D. Control the center in linear extrusion effortlessly.
weight: 11
url: /java/linear-extrusion/controlling-center/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Controlling Center in Linear Extrusion with Aspose.3D for Java

## Introduction

In the world of 3D graphics and Java programming, controlling the center in linear extrusion plays a crucial role in achieving the desired effects in your projects. Aspose.3D for Java provides a powerful toolkit to handle such tasks seamlessly. In this tutorial, we'll dive into the process of controlling the center in linear extrusion using Aspose.3D for Java, breaking down each step to ensure a smooth and comprehensive understanding.

## Prerequisites

Before we embark on this tutorial journey, make sure you have the following prerequisites in place:

1. Java Development Environment: Ensure that you have a Java development environment set up on your machine.

2. Aspose.3D for Java: Download and install the Aspose.3D library. You can find the library and its documentation [here](https://reference.aspose.com/3d/java/).

3. Document Directory: Create a directory to store your Java documents. Let's call it "Your Document Directory."

## Import Packages

In your Java development environment, import the necessary packages for Aspose.3D. This ensures that your code has access to the functionalities provided by the library.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Step 1: Set Up the Base Profile

Initialize the base profile to be extruded. In this example, we'll use a rectangle shape with a rounding radius of 0.3.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Step 2: Create a 3D Scene

Build the foundation of your 3D world by creating a scene.

```java
Scene scene = new Scene();
```

## Step 3: Create Left and Right Nodes

Establish left and right nodes within your scene. These nodes serve as the canvas for your 3D objects.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Step 4: Linear Extrusion with Center Property

Perform linear extrusion on the left node without centering, and set the number of slices to 3.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## Step 5: Set Ground Plane for Reference

Enhance the visual representation by adding a ground plane to the left node.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## Step 6: Linear Extrusion with Center Property (Right Node)

Perform linear extrusion on the right node, this time centering the extrusion, and again set the number of slices to 3.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## Step 7: Set Ground Plane for Reference (Right Node)

Similar to the left node, add a ground plane to the right node for reference.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## Step 8: Save the 3D Scene

Save your 3D scene in Wavefront OBJ format.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Conclusion

Controlling the center in linear extrusion with Aspose.3D for Java opens up exciting possibilities in 3D graphics development. By following this step-by-step guide, you've learned how to manipulate the center property, allowing you to achieve the desired visual effects in your Java projects.

## FAQ's

### Q1: Can I use Aspose.3D for Java in commercial projects?

A1: Yes, Aspose.3D for Java is available for commercial use. For licensing details, visit [here](https://purchase.aspose.com/buy).

### Q2: Is there a free trial available?

A2: Yes, you can explore a free trial of Aspose.3D for Java [here](https://releases.aspose.com/).

### Q3: Where can I find support for Aspose.3D for Java?

A3: The Aspose.3D community forum is a great place to seek support and share your experiences. Visit the forum [here](https://forum.aspose.com/c/3d/18).

### Q4: Do I need a temporary license for testing?

A4: Yes, if you require a temporary license for testing purposes, you can obtain one [here](https://purchase.aspose.com/temporary-license/).

### Q5: Where can I find the documentation?

A5: The documentation for Aspose.3D for Java is available [here](https://reference.aspose.com/3d/java/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
