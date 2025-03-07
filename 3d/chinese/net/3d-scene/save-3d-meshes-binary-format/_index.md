---
title: 以自定义二进制格式保存 3D 网格
linktitle: 以自定义二进制格式保存 3D 网格
second_title: Aspose.3D .NET API
description: 使用 Aspose.3D for .NET 探索 3D 世界。了解以自定义二进制格式保存网格。
weight: 13
url: /zh/net/3d-scene/save-3d-meshes-binary-format/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 以自定义二进制格式保存 3D 网格

## 介绍

欢迎来到 Aspose.3D for .NET 的世界，这是一个功能强大的库，使开发人员能够轻松处理 3D 文件。在本教程中，我们将深入研究使用 Aspose.3D for .NET 以自定义二进制格式保存 3D 网格的过程。本指南假设您对 C# 有基本了解并熟悉 Aspose.3D 库。

## 先决条件

在我们开始学习本教程之前，请确保您已准备好以下内容：

-  Aspose.3D for .NET：确保您已安装 Aspose.3D 库。您可以从以下位置下载：[这里](https://releases.aspose.com/3d/net/).

- 开发环境：设置您首选的 C# 开发环境，例如 Visual Studio。

- 输入 3D 文件：有一个要转换为自定义二进制格式的 3D 文件（例如 test.fbx）。

## 导入命名空间

在您的 C# 代码中，包含访问 Aspose.3D 功能所需的命名空间：

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

## 第 1 步：加载 3D 文件

使用 Aspose.3D 加载 3D 文件。在此示例中，我们加载一个名为“test.fbx”的文件：

```csharp
Scene scene = Scene.FromFile("test.fbx");
```

## 第 2 步：定义自定义二进制格式

定义要保存 3D 网格的自定义二进制格式的结构。该示例使用以 MeshBlock、Vertex 和 Triangle 作为组件的结构。

```csharp
//顶点的内存布局是
//浮动[3]位置；
//浮动[3]正常；
//浮动[3]紫外线；
var vertexDeclaration = new VertexDeclaration();
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Position);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Normal);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.UV);

```

## 第三步：打开文件进行写入

打开一个用于写入的二进制文件，其中将保存转换后的 3D 网格：

```csharp
using (var writer = new BinaryWriter(new FileStream("Your Output Directory" + "Save3DMeshesInCustomBinaryFormat_out", FileMode.Create, FileAccess.Write)))
```

## 第 4 步：迭代节点和实体

访问 3D 场景中的每个节点并将网格实体转换为自定义二进制格式。忽略灯光、摄像机和其他非网格实体：

```csharp
scene.RootNode.Accept(delegate(Node node)
{
    foreach (Entity entity in node.Entities)
    {
        if (!(entity is IMeshConvertible))
            continue;
        // ...（继续处理）
    }
    return true;
});
```

## 第 5 步：转换并写入控制点和三角形

对于每个网格实体，将控制点转换为世界空间并将它们与三角形索引一起写入二进制文件：

```csharp
Mesh m = ((IMeshConvertible)entity).ToMesh();

var triMesh = TriMesh.FromMesh(vertexDeclaration, m);


//网格的内存布局是：
//浮动[16]变换矩阵；
// int vertices_count；
// int 索引计数；
//顶点[vertices_count]个顶点；
// ushort[indices_count] 索引；


//写变换
var transform = node.GlobalTransform.TransformMatrix.ToArray();
for(int i = 0; i < transform.Length; i++)
    writer.Write((float)transform[i]);
//写入顶点/索引的数量
writer.Write(triMesh.VerticesCount);
writer.Write(triMesh.IndicesCount);
//写入顶点和索引
writer.Flush();
triMesh.WriteVerticesTo(writer.BaseStream);
triMesh.Write16bIndicesTo(writer.BaseStream);

```

## 结论

在本教程中，我们介绍了使用 Aspose.3D for .NET 以自定义二进制格式保存 3D 网格的过程。这个强大的库为开发人员提供了无缝操作 3D 文件所需的工具。尝试不同的格式和设置，以释放 Aspose.3D 在您的项目中的全部潜力。

## 常见问题解答

### Q1：我可以将 Aspose.3D for .NET 与其他编程语言一起使用吗？

A1：Aspose.3D 主要支持 .NET 语言，但您可以探索其他语言的兼容性选项。

### Q2：在哪里可以找到更多示例和资源？

 A2: 的[Aspose.3D 论坛](https://forum.aspose.com/c/3d/18)是寻找支持、示例以及与社区互动的好地方。

### Q3：Aspose.3D 有试用版吗？

 A3：是的，您可以从以下位置获得免费试用[这里](https://releases.aspose.com/).

### Q4：如何获得Aspose.3D的临时许可证？

 A4：参观[这个链接](https://purchase.aspose.com/temporary-license/)获得用于测试目的的临时许可证。

### Q5：我可以购买 Aspose.3D for .NET 吗？

 A5：是的，您可以从[购买页面](https://purchase.aspose.com/buy).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
