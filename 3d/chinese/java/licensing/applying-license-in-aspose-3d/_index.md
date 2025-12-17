---
date: 2025-12-17
description: 了解如何在 Aspose.3D for Java 中设置许可证以及如何使用公私钥进行计量授权。
linktitle: Applying a License in Aspose.3D for Java
second_title: Aspose.3D Java API
title: 如何在 Aspose.3D for Java 中设置许可证 – 完整指南
url: /zh/java/licensing/applying-license-in-aspose-3d/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 如何在 Aspose.3D for Java 中设置许可证

## 介绍

欢迎！在本一步一步的教程中，您将了解 **如何在 Aspose.3D 中设置许可证**，以及 **如何使用公私钥** 实现计量授权。Aspose.3D 是一个强大的 Java 库，简化了 3D 文件格式的处理，有效的许可证可解锁其全部功能。阅读完本指南后，您将能够在任何 Java 项目中无缝集成授权。

## 快速答案
- **设置许可证的主要方式是什么？** 使用 `License` 类并调用 `setLicense`，传入文件路径或流。  
- **可以从流加载许可证吗？** 可以——`FileInputStream` 完全适用。  
- **公私钥的作用是什么？** 它们通过 `Metered` 类实现计量授权。  
- **开发阶段需要许可证吗？** 临时或试用许可证足以进行测试；正式生产环境需要完整许可证。  
- **支持哪些 Java 版本？** Aspose.3D 支持 Java 6 及更高版本。

## 前置条件

在开始之前，请确保您已具备：

- 基本的 Java 编程知识。  
- 将 Aspose.3D 库添加到项目中。请从[发布页面](https://releases.aspose.com/3d/java/)下载。  
- 有效的 `.lic` 文件或您的公私计量密钥。

## 导入包

在 Java 源文件中添加所需的导入。确保 Aspose.3D JAR 已加入类路径。

```java
import com.aspose.threed.License;
import com.aspose.threed.Metered;

import java.io.FileInputStream;
import java.io.IOException;
```

## 使用文件设置许可证

### 步骤 1：创建 License 对象

实例化 `License` 类——该对象将保存许可证信息。

```java
License license = new License();
```

### 步骤 2：从文件设置许可证

提供相对或绝对路径指向您的 `.lic` 文件并应用。

```java
license.setLicense("Aspose._3D.lic");
```

> **专业提示：** 将许可证文件放在源码控制目录之外，以避免意外泄露。

## 使用流设置许可证

### 步骤 1：创建 License 对象

同前，先创建一个全新的 `License` 实例。

```java
License license = new License();
```

### 步骤 2：从流设置许可证

将许可证文件读取到 `FileInputStream`，并将该流传递给 `setLicense`。`try‑with‑resources` 代码块可确保流自动关闭。

```java
try (FileInputStream myStream = new FileInputStream("Aspose._3D.lic")) {
    license.setLicense(myStream);
}
```

## 使用公私钥进行计量授权

### 步骤 1：初始化 Metered 授权对象

创建 `Metered` 类的实例，该类负责计量（按使用付费）授权。

```java
Metered metered = new Metered();
```

### 步骤 2：设置公私钥

提供您从 Aspose 获得的密钥。这些密钥使库能够向授权服务器报告使用情况。

```java
metered.setMeteredKey("your-public-key", "your-private-key");
```

> **警告：** 切勿在公开分发的 JAR 中硬编码私钥。请考虑从安全位置或环境变量加载。

## 常见用例

- **企业级 3D 渲染流水线** – 设置许可证后解锁高性能 API。  
- **自动化测试环境** – 使用临时许可证（见 FAQ）验证功能，无需购买完整许可证。  
- **计量 SaaS 解决方案** – 集成公私钥，根据实际使用量计费客户。

## 结论

恭喜！您现在已经掌握了 **如何在 Java 中通过文件、流设置 Aspose.3D 许可证**，以及 **如何使用公私钥进行计量授权**。通过这些步骤，您可以自信地将 Aspose.3D 集成到任何 Java 应用中，充分利用其 3D 处理能力。

## 常见问题

**Q1: Aspose.3D 是否兼容所有 Java 版本？**  
A1: 是的，Aspose.3D 支持 Java 6 及更高版本。

**Q2: 我可以在哪里找到更多文档？**  
A2: 您可以参考[此处](https://reference.aspose.com/3d/java/)的文档。

**Q3: 我可以在购买前试用 Aspose.3D 吗？**  
A3: 可以，您可以在[此处](https://releases.aspose.com/)获取免费试用。

**Q4: 如何获取 Aspose.3D 的支持？**  
A4: 请访问[Aspose.3D 论坛](https://forum.aspose.com/c/3d/18)获取社区和官方支持。

**Q5: 测试时需要临时许可证吗？**  
A5: 需要，您可以在[此处](https://purchase.aspose.com/temporary-license/)获取临时许可证。

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}
{{< blocks/products/products-backtop-button >}}

---

**最后更新：** 2025-12-17  
**测试环境：** Aspose.3D 24.11 for Java  
**作者：** Aspose  

---