---
date: 2026-05-24
description: 了解如何在 Java 中设置 aspose 3d license，应用 license 文件，进行 stream，或使用带有 public
  和 private keys 的 metered licensing。
keywords:
- set aspose 3d license
- aspose 3d java licensing
- metered licensing java
linktitle: 如何在 Aspose.3D for Java 中设置 Aspose License
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to set aspose 3d license in Java, apply a license file, stream
    it, or use metered licensing with public and private keys.
  headline: How to Set Aspose 3D License in Java (set aspose 3d license)
  type: TechArticle
- description: Learn how to set aspose 3d license in Java, apply a license file, stream
    it, or use metered licensing with public and private keys.
  name: How to Set Aspose 3D License in Java (set aspose 3d license)
  steps:
  - name: Create a `License` object
    text: Instantiate the `License` class; this prepares the runtime to accept a license
      file.
  - name: Apply the license file
    text: Provide the absolute or relative path to your `.lic` file and call `setLicense`.
      The method returns `void`, and the license is cached after the first successful
      call, so subsequent calls are inexpensive.
  - name: Create a `License` object
    text: As before, start by creating an instance of the `License` class.
  - name: Load the license via `FileInputStream`
    text: Open a `FileInputStream` pointing to your `.lic` file (or any `InputStream`)
      and pass it to `setLicense`. The stream is read once and then closed automatically.
  - name: Initialize a `Metered` license object
    text: The `Metered` class represents a cloud‑based license that validates usage
      against Aspose’s metering server.
  - name: Set public and private keys
    text: Call `setMeteredKey(publicKey, privateKey)` with the keys you received when
      you purchased a metered license. The library contacts the server once to verify
      the keys and then caches the result.
  type: HowTo
- questions:
  - answer: Yes, Aspose.3D supports Java 6 through Java 21, covering more than 15
      major releases.
    question: Is Aspose.3D compatible with all Java versions?
  - answer: You can refer to the documentation [here](https://reference.aspose.com/3d/java/).
    question: Where can I find additional documentation?
  - answer: Yes, you can explore a free trial [here](https://releases.aspose.com/).
    question: Can I try Aspose.3D before purchasing?
  - answer: Visit the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) for support.
    question: How can I get support for Aspose.3D?
  - answer: Yes, obtain a temporary license [here](https://purchase.aspose.com/temporary-license/).
    question: Do I need a temporary license for testing?
  type: FAQPage
second_title: Aspose.3D Java API
title: 如何在 Java 中设置 Aspose 3D license（set aspose 3d license）
url: /zh/java/licensing/applying-license-in-aspose-3d/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 如何在 Java 中设置 Aspose 3D 许可证（设置 aspose 3d 许可证）

## 介绍

在本综合教程中，您将了解 **如何设置 aspose 3d 许可证**，适用于 Java 环境下的 Aspose.3D。无论您是喜欢加载许可证文件、通过流读取，还是使用带有公钥和私钥的计量授权，我们都会一步步演示每种方法，让您快速且自信地解锁 Aspose.3D 的全部功能。正确设置许可证可去除评估水印，启用高级 3D 格式，并确保完全符合 Aspose 的授权模型。

## 快速答案
- **设置 Aspose.3D 许可证的主要方式是什么？** 使用 `License` 类并调用 `setLicense`，传入文件路径或流。  
- **可以从流中加载许可证吗？** 可以——将 `.lic` 文件包装在 `FileInputStream` 中并传递给 `setLicense`。  
- **如果需要计量许可证怎么办？** 初始化 `Metered` 对象并使用 `setMeteredKey` 传入您的公钥和私钥。  
- **开发构建是否需要许可证？** 任何非评估场景都需要试用或临时许可证。  
- **支持哪些 Java 版本？** Aspose.3D 支持 Java 6 到 Java 21，覆盖超过 15 个主要版本。

## 什么是 `License` 类？
`License` 类是 Aspose.3D 的核心授权对象，负责将 `.lic` 文件加载到内存中，验证许可证信息，并在实例化后全局应用于 JVM 进程，确保所有后续的 Aspose.3D 操作都在已授权模式下运行，且不受评估限制。

## 为什么要设置 Aspose 3D 许可证？
应用有效许可证可启用 **50 多种高级 3D 文件格式**（包括 FBX、OBJ、STL 和 GLTF），并去除渲染图像中的 “Evaluation” 水印。它还解除场景大小限制，允许处理 **多达 100 万顶点** 的模型而不会出现性能下降。

## 前提条件

在开始之前，请确保您已具备以下前提条件：

- 对 Java 编程有基本了解。  
- 已安装 Aspose.3D 库。您可以从[发布页面](https://releases.aspose.com/3d/java/)下载。

## 导入包

要开始使用，请在 Java 项目中导入必要的包。确保已将 Aspose.3D 添加到类路径中。示例代码如下：

```java
import com.aspose.threed.License;
import com.aspose.threed.Metered;

import java.io.FileInputStream;
import java.io.IOException;
```

`License` 类负责加载 `.lic` 文件并全局应用，而 `Metered` 类通过验证公钥和私钥，实现基于云的计量授权。

## 如何从文件应用许可证？

直接从磁盘上的 `.lic` 文件加载许可证。这是桌面或本地部署应用最直接的方式，确保在启动时读取一次许可证并在 JVM 生命周期内缓存，避免后续运行时的额外开销。

### 步骤 1：创建 `License` 对象
实例化 `License` 类，为运行时接受许可证文件做准备。

### 步骤 2：应用许可证文件
提供 `.lic` 文件的绝对或相对路径并调用 `setLicense`。该方法返回 `void`，首次成功调用后许可证会被缓存，后续调用开销极小。

```java
import com.aspose.threed.License;
import com.aspose.threed.Metered;

import java.io.FileInputStream;
import java.io.IOException;
```

## 如何从流应用许可证？

当许可证文件作为资源嵌入、存放在安全位置或在运行时从远程服务获取时，使用流加载许可证非常有用。通过 `InputStream`，您可以避免暴露物理文件路径，并可将许可证数据加密或打包在 JAR 中，从而提升安全性，同时仍让库读取许可证字节。

### 步骤 1：创建 `License` 对象
同前，首先创建 `License` 类的实例。

### 步骤 2：通过 `FileInputStream` 加载许可证
打开指向 `.lic` 文件（或任意 `InputStream`）的 `FileInputStream`，并将其传递给 `setLicense`。流会被读取一次并自动关闭。

```java
License license = new License();
```

## 如何使用公钥和私钥进行计量授权？

计量授权允许您在没有实体 `.lic` 文件的情况下激活 Aspose.3D，使用 Aspose 云服务颁发的密钥。此方式非常适合 SaaS 或基于云的部署，因为在每个实例上管理许可证文件不切实际；库会一次性联系 Aspose 的计量服务器验证密钥，然后在会话期间缓存结果。

### 步骤 1：初始化 `Metered` 许可证对象
`Metered` 类代表基于云的许可证，负责向 Aspose 的计量服务器验证使用情况。

### 步骤 2：设置公钥和私钥
使用 `setMeteredKey(publicKey, privateKey)` 将您购买计量许可证时获得的密钥传入。库会一次性联系服务器验证密钥并缓存结果。

```java
license.setLicense("Aspose._3D.lic");
```

## 常见问题与技巧

- **文件未找到** – 确认 `.lic` 文件路径相对于工作目录是否正确，或使用绝对路径。  
- **流过早关闭** – 使用流时，请保持 `License` 对象在应用整个期间存活；首次成功调用后许可证会被缓存。  
- **计量密钥不匹配** – 再次检查公钥和私钥是否对应同一计量许可证，拼写错误会导致运行时异常。  
- **专业提示**：将许可证文件存放在源码树之外的安全位置，并通过环境变量加载，以避免将其提交到版本控制。

## 结论

恭喜！您已成功学习 **如何在 Java 中设置 aspose 3d 许可证**，掌握了三种可靠方法：从文件应用许可证、通过流加载以及使用公钥和私钥配置计量授权。拥有许可证后，您可以将 Aspose.3D 无缝集成到 Java 应用中，解锁所有高级 3D 处理功能，并遵循 Aspose 的授权要求。

## 常见问题

**问：Aspose.3D 是否兼容所有 Java 版本？**  
答：是的，Aspose.3D 支持 Java 6 到 Java 21，覆盖超过 15 个主要版本。

**问：在哪里可以找到更多文档？**  
答：您可以访问[此处](https://reference.aspose.com/3d/java/)查看文档。

**问：可以在购买前试用 Aspose.3D 吗？**  
答：可以，您可以在[此处](https://releases.aspose.com/)获取免费试用。

**问：如何获取 Aspose.3D 的支持？**  
答：请访问[Aspose.3D 论坛](https://forum.aspose.com/c/3d/18)获取支持。

**问：测试时是否需要临时许可证？**  
答：是的，请在[此处](https://purchase.aspose.com/temporary-license/)获取临时许可证。

**问：文件许可证和计量许可证有什么区别？**  
答：文件许可证是绑定到特定产品版本的静态 `.lic` 文件，而计量许可证通过公钥/私钥在 Aspose 的云计量服务上验证使用情况。

**问：可以在静态初始化块中嵌入许可证加载代码吗？**  
答：完全可以——将 `License` 初始化放在静态块中，可确保类首次加载时一次性应用许可证。

```java
License license = new License();
```
```java
try (FileInputStream myStream = new FileInputStream("Aspose._3D.lic")) {
    license.setLicense(myStream);
}
```
```java
Metered metered = new Metered();
```
```java
metered.setMeteredKey("your-public-key", "your-private-key");
```

{{< blocks/products/products-backtop-button >}}

## 相关教程

- [Step by Step License Guide for Aspose.3D Java](/3d/java/licensing/)
- [Create 3D Scene Java with Aspose 3D Java](/3d/java/3d-scenes-and-models/)
- [Create 3D Cube, Apply PBR Materials in Java with Aspose.3D](/3d/java/geometry/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}