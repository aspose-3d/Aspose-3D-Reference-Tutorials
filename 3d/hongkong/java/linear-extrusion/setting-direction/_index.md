---
title: 使用 Aspose.3D for Java 設定線性拉伸方向
linktitle: 使用 Aspose.3D for Java 設定線性拉伸方向
second_title: Aspose.3D Java API
description: 使用 Aspose.3D for Java 掌握線性擠出！請遵循我們的無縫 3D 程式指南。立即下載以獲得迷人的體驗。
weight: 12
url: /zh-hant/java/linear-extrusion/setting-direction/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 使用 Aspose.3D for Java 設定線性拉伸方向

## 介紹

歡迎閱讀我們關於使用 Aspose.3D for Java 設定線性擠出方向的逐步指南。 Aspose.3D 是一個功能強大的 Java 程式庫，可讓開發人員無縫地處理 3D 檔案和場景。在本教程中，我們將重點關注在線性擠出中設置方向的具體任務，以提高您在 3D 程式設計方面的熟練程度。

## 先決條件

在我們深入學習本教程之前，請確保您具備以下先決條件：

- Java 程式語言的基礎知識。
-  Aspose.3D 庫已安裝。您可以從以下位置下載：[這裡](https://releases.aspose.com/3d/java/).
- Java 整合開發環境 (IDE)，例如 Eclipse 或 IntelliJ。

## 導入包

確保導入必要的套件來啟動您的專案：

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 第 1 步：初始化基本設定檔

首先初始化要拉伸的基礎輪廓。在這個例子中，我們使用一個`RectangleShape`圓角半徑為 0.3：

```java
//文檔目錄的路徑。
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## 第 2 步：建立場景

接下來，建立一個 3D 場景來包含擠出的物件：

```java
Scene scene = new Scene();
```

## 第三步：建立節點

在場景中建立左右節點：

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## 第四步：對左節點進行線性擠壓

使用以下命令對左側節點執行線性擠壓`LinearExtrusion`具有指定參數（例如扭曲和切片）的類別：

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## 步驟5：在右側節點上進行有方向的線性擠壓

對右側節點進行線性擠壓，引入`setDirection`屬性來定義擠出方向：

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## 第 6 步：儲存 3D 場景

將 3D 場景儲存為所需的檔案格式。在此範例中，我們將其另存為 Wavefront OBJ 檔案：

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 結論

恭喜！您已經成功學習如何使用 Aspose.3D for Java 設定線性拉伸方向。本教學可增強您的 3D 程式設計技能，並為創意專案開啟新的可能性。

## 常見問題解答

### Q1：我可以將Aspose.3D與其他程式語言一起使用嗎？

A1：Aspose.3D支援多種程式語言，包括.NET和Java。

### Q2。 Aspose.3D 是否有免費試用版？

 A2：是的，您可以透過免費試用探索 Aspose.3D 的功能[這裡](https://releases.aspose.com/).

### Q3：在哪裡可以找到 Aspose.3D for Java 的詳細文件？

 A3：提供全面的文檔[這裡](https://reference.aspose.com/3d/java/).

### Q4：如何獲得 Aspose.3D 的支援？

 A4：訪問[Aspose.3D 論壇](https://forum.aspose.com/c/3d/18)如有任何幫助或疑問。

### Q5：Aspose.3D 是否有臨時許可證？

 A5：是的，您可以獲得臨時許可證[這裡](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
