---
date: 2026-02-14
description: 了解如何在 Aspose.3D for Java 中設定 Aspose 授權，包括如何從檔案套用授權以及設定公私鑰。
linktitle: How to Set Aspose License in Aspose.3D for Java
second_title: Aspose.3D Java API
title: 如何在 Aspose.3D for Java 中設定 Aspose 授權
url: /zh-hant/java/licensing/applying-license-in-aspose-3d/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 如何在 Aspose.3D for Java 中設定 Aspose 授權

## 簡介

在本完整教學中，您將了解 **如何設定 Aspose 授權** 於 Aspose.3D 的 Java 環境。無論您偏好載入授權檔案、以串流方式讀取，或是使用公私鑰的計量授權，我們都會一步步說明，讓您快速且有信心地解鎖 Aspose.3D 的完整功能。

## 快速解答
- **設定 Aspose.3D 授權的主要方式是什麼？** 使用 `License` 類別，呼叫 `setLicense` 並傳入檔案路徑或串流。  
- **可以從串流載入授權嗎？** 可以 – 將 `.lic` 檔案包裝成 `FileInputStream` 後傳入 `setLicense`。  
- **如果需要計量授權該怎麼做？** 建立 `Metered` 物件，並使用您的公私鑰呼叫 `setMeteredKey`。  
- **開發版是否需要授權？** 任何非評估情境皆需使用試用或臨時授權。  
- **支援哪些 Java 版本？** Aspose.3D 支援 Java 6 及以上版本。

## 先決條件

在開始之前，請確保您已具備以下條件：

- 具備基本的 Java 程式設計知識。  
- 已安裝 Aspose.3D 套件。您可從 [release page](https://releases.aspose.com/3d/java/) 下載。

## 匯入套件

要開始使用，請在您的 Java 專案中匯入必要的套件，並確保 Aspose.3D 已加入 classpath。以下為範例：

```java
import com.aspose.threed.License;
import com.aspose.threed.Metered;

import java.io.FileInputStream;
import java.io.IOException;
```

## 使用檔案套用授權

### 步驟 1：建立 License 物件

首先，在 Java 程式碼中建立一個 `License` 物件。

```java
License license = new License();
```

### 步驟 2：從檔案套用授權

指定授權檔案的路徑，並使用以下程式碼設定授權。此範例示範 **從檔案套用授權** 的做法。

```java
license.setLicense("Aspose._3D.lic");
```

## 使用串流物件套用授權

### 步驟 1：建立 License 物件

同樣在 Java 程式碼中建立一個 `License` 物件。

```java
License license = new License();
```

### 步驟 2：從串流物件設定授權

利用 `FileInputStream` 建立串流，並設定授權：

```java
try (FileInputStream myStream = new FileInputStream("Aspose._3D.lic")) {
    license.setLicense(myStream);
}
```

## 使用公私鑰進行計量授權

### 步驟 1：初始化 Metered 授權物件

初始化一個 `Metered` 授權物件：

```java
Metered metered = new Metered();
```

### 步驟 2：設定公私鑰

設定您的公私鑰以啟用計量授權。此步驟涵蓋 **設定公私鑰** 的情境。

```java
metered.setMeteredKey("your-public-key", "your-private-key");
```

## 為何設定授權很重要

正確的授權可移除評估水印、解鎖高階檔案格式，並確保符合 Aspose 的授權模型。選擇適當的方式（檔案、串流或計量）可讓您在 CI/CD 流程、雲端部署或桌面應用程式中無縫整合授權。

## 常見問題與提示

- **找不到檔案** – 請確認 `.lic` 檔案路徑相對於工作目錄是否正確，或改用絕對路徑。  
- **串流過早關閉** – 使用串流時，請保持 `License` 物件在應用程式執行期間存活；首次成功呼叫後授權會被快取。  
- **計量金鑰不匹配** – 請再次確認公私鑰屬於同一筆計量授權，錯字會導致執行時例外。  
- **小技巧：** 將授權檔案存放於來源樹之外的安全位置，並透過環境變數載入，以避免將授權檔提交至版本控制。

## 結論

恭喜！您已成功學會 **如何在 Aspose.3D for Java 中設定 Aspose 授權**，包括從檔案套用、以串流方式載入，以及使用公私鑰設定計量授權。現在您可以將 Aspose.3D 無縫整合至 Java 應用程式，充分發揮其 3D 處理功能。

## 常見問題

**Q: Aspose.3D 是否相容所有 Java 版本？**  
A: 是的，Aspose.3D 相容於 Java 6 及以上版本。

**Q: 我可以在哪裡找到更多文件？**  
A: 您可參考文件 [here](https://reference.aspose.com/3d/java/)。

**Q: 購買前可以先試用 Aspose.3D 嗎？**  
A: 可以，您可在此取得免費試用版 [here](https://releases.aspose.com/)。

**Q: 如何取得 Aspose.3D 的支援？**  
A: 請前往 [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) 取得支援。

**Q: 測試時需要臨時授權嗎？**  
A: 需要，請於此取得臨時授權 [here](https://purchase.aspose.com/temporary-license/)。

**Q: 檔案授權與計量授權有何差異？**  
A: 檔案授權是綁定特定產品版本的靜態 `.lic` 檔案；計量授權則透過公私鑰向 Aspose 雲端計量服務驗證使用情況。

**Q: 可以在靜態初始化子程式中嵌入授權載入程式碼嗎？**  
A: 完全可以 – 將 `License` 初始化放入 static block，可確保類別首次載入時即套用授權。

---

**最後更新：** 2026-02-14  
**測試環境：** Aspose.3D 24.11 for Java  
**作者：** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}