---
title: 在 Aspose.3D for Java 中執行線性擠出
linktitle: 在 Aspose.3D for Java 中執行線性擠出
second_title: Aspose.3D Java API
description: 使用 Aspose.3D for Java 探索 3D 建模世界。學習輕鬆執行線性擠出。
weight: 10
url: /zh-hant/java/linear-extrusion/performing-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 在 Aspose.3D for Java 中執行線性擠出

## 介紹

歡迎來到這個關於在 Aspose.3D for Java 中執行線性拉伸的綜合教程！如果您希望使用 Java 增強 3D 建模技能，那麼您來對地方了。在本教程中，我們將引導您完成使用 Aspose.3D（一個用於 3D 建模的強大 Java 程式庫）執行線性擠壓的過程。

## 先決條件

在深入學習本教程之前，請確保您具備以下先決條件：

1. Java 開發環境：確保您的電腦上設定有 Java 開發環境。

2.  Aspose.3D 函式庫：下載並安裝 Aspose.3D 函式庫。你可以找到圖書館[這裡](https://releases.aspose.com/3d/java/).

## 導入包

設定開發環境並安裝 Aspose.3D 庫後，就可以匯入必要的套件了。在您的 Java 程式碼中，包含以下內容：

```java
import com.aspose.threed.*;
```

讓我們分解每個步驟以確保清晰的理解。

## 步驟1：設定文檔目錄

定義文檔目錄的路徑：

```java
String MyDir = "Your Document Directory";
```

這可確保產生的 3D 模型將保存在指定目錄中。

## 第 2 步：初始化基礎形狀

建立一個矩形形狀作為擠出的基本輪廓：

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

根據需要調整圓角半徑以自訂形狀。

## 步驟 3：執行線性擠壓

在基礎輪廓上執行線性擠壓：

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

在這裡，我們將形狀拉伸 10 個單位，設定切片數量，啟用居中，並應用扭曲和扭曲偏移。

## 第 4 步：建立 3D 場景

建立 3D 場景並將拉伸新增為子節點：

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

## 第 5 步：儲存 3D 場景

將生成的 3D 場景儲存為 Wavefront OBJ 檔案：

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

現在，您已經使用 Aspose.3D for Java 成功執行了線性擠出！

## 結論

恭喜！您已經了解如何利用 Aspose.3D for Java 執行線性擠出。這個強大的函式庫為您的 3D 建模專案開啟了一個充滿可能性的世界。

## 常見問題解答

### Q1：Aspose.3D 是否相容於所有 Java 版本？

A1：Aspose.3D 設計用於與 Java 1.6 及更高版本一起使用。

### Q2：我可以將Aspose.3D用於商業項目嗎？

A2：是的，Aspose.3D 可用於個人和商業項目。檢查許可詳細信息[這裡](https://purchase.aspose.com/buy).

### Q3：如何獲得 Aspose.3D 的支援？

 A3：訪問[Aspose.3D 論壇](https://forum.aspose.com/c/3d/18)尋求社區支持或考慮購買[臨時執照](https://purchase.aspose.com/temporary-license/)以獲得優質支援。

### Q4：Aspose.3D 中還有其他 3D 建模功能嗎？

 A4：當然！探索廣泛的文檔[這裡](https://reference.aspose.com/3d/java/)取得功能和範例的完整清單。

### Q5：Aspose.3D 有免費試用版嗎？

 A5：是的，您可以免費試用[這裡](https://releases.aspose.com/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
