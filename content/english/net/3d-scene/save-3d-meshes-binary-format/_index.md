---
title: Saving 3D Meshes in Custom Binary Format
linktitle: Saving 3D Meshes in Custom Binary Format
second_title: Aspose.3D .NET API
description: Explore the world of 3D with Aspose.3D for .NET. Learn to save meshes in custom binary format.
type: docs
weight: 13
url: /net/3d-scene/save-3d-meshes-binary-format/
---
## Introduction

Welcome to the world of Aspose.3D for .NET, a powerful library that empowers developers to work with 3D files effortlessly. In this tutorial, we'll delve into the process of saving 3D meshes in a custom binary format using Aspose.3D for .NET. This guide assumes you have a basic understanding of C# and are familiar with the Aspose.3D library.

## Prerequisites

Before we jump into the tutorial, make sure you have the following in place:

- Aspose.3D for .NET: Ensure you have the Aspose.3D library installed. You can download it from [here](https://releases.aspose.com/3d/net/).

- Development Environment: Set up your preferred C# development environment, such as Visual Studio.

- Input 3D File: Have a 3D file (e.g., test.fbx) that you want to convert into a custom binary format.

## Import Namespaces

In your C# code, include the necessary namespaces to access the Aspose.3D functionalities:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
```

## Step 1: Load a 3D File

Load your 3D file using Aspose.3D. In this example, we load a file named "test.fbx":

```csharp
Scene scene = Scene.FromFile("test.fbx");
```

## Step 2: Define Custom Binary Format

Define the structure of the custom binary format you want to save your 3D meshes in. The example uses a structure with MeshBlock, Vertex, and Triangle as components.

```csharp
//The memory layout of a vertex is 
// float[3] position;
// float[3] normal;
// float[3] uv;
var vertexDeclaration = new VertexDeclaration();
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Position);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Normal);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.UV);

```

## Step 3: Open File for Writing

Open a binary file for writing, where the converted 3D meshes will be saved:

```csharp
using (var writer = new BinaryWriter(new FileStream("Your Output Directory" + "Save3DMeshesInCustomBinaryFormat_out", FileMode.Create, FileAccess.Write)))
```

## Step 4: Iterate through Nodes and Entities

Visit each node in the 3D scene and convert mesh entities to the custom binary format. Ignore lights, cameras, and other non-mesh entities:

```csharp
scene.RootNode.Accept(delegate(Node node)
{
    foreach (Entity entity in node.Entities)
    {
        if (!(entity is IMeshConvertible))
            continue;
        // ... (continue processing)
    }
    return true;
});
```

## Step 5: Convert and Write Control Points and Triangles

For each mesh entity, convert control points to world space and write them to the binary file along with triangle indices:

```csharp
Mesh m = ((IMeshConvertible)entity).ToMesh();

var triMesh = TriMesh.FromMesh(vertexDeclaration, m);


//The mesh's memory layout is:
// float[16] transform_matrix;
// int vertices_count;
// int indices_count;
// vertex[vertices_count] vertices;
// ushort[indices_count] indices;


//write transform
var transform = node.GlobalTransform.TransformMatrix.ToArray();
for(int i = 0; i < transform.Length; i++)
    writer.Write((float)transform[i]);
//write number of vertices/indices
writer.Write(triMesh.VerticesCount);
writer.Write(triMesh.IndicesCount);
//write vertices and indices
writer.Flush();
triMesh.WriteVerticesTo(writer.BaseStream);
triMesh.Write16bIndicesTo(writer.BaseStream);

```

## Conclusion

In this tutorial, we covered the process of saving 3D meshes in a custom binary format using Aspose.3D for .NET. This powerful library provides developers with the tools needed to manipulate 3D files seamlessly. Experiment with different formats and settings to unlock the full potential of Aspose.3D in your projects.

## FAQs

### Q1: Can I use Aspose.3D for .NET with other programming languages?

A1: Aspose.3D primarily supports .NET languages, but you can explore compatibility options for other languages.

### Q2: Where can I find additional examples and resources?

A2: The [Aspose.3D forum](https://forum.aspose.com/c/3d/18) is a great place to find support, examples, and engage with the community.

### Q3: Is there a trial version available for Aspose.3D?

A3: Yes, you can get a free trial from [here](https://releases.aspose.com/).

### Q4: How do I obtain a temporary license for Aspose.3D?

A4: Visit [this link](https://purchase.aspose.com/temporary-license/) to get a temporary license for testing purposes.

### Q5: Can I purchase Aspose.3D for .NET?

A5: Yes, you can buy Aspose.3D from the [purchase page](https://purchase.aspose.com/buy).
