---
date: 2026-05-24
description: 了解如何在 Java 中設定 aspose 3d license、套用 license file、以 stream 方式載入，或使用 metered
  licensing 搭配 public and private keys。
keywords:
- set aspose 3d license
- aspose 3d java licensing
- metered licensing java
linktitle: 如何在 Aspose.3D for Java 中設定 Aspose License
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
title: 如何在 Java 中設定 Aspose 3D 授權 (set aspose 3d license)
url: /zh-hant/java/licensing/applying-license-in-aspose-3d/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 如何在 Java 中設定 Aspose 3D 授權 (set aspose 3d license)

## 介紹

在本完整教學中，您將學習 **如何在 Java 環境中設定 aspose 3d 授權**。無論您偏好載入授權檔案、以串流方式讀取，或是使用公私鑰的計量授權，我們都會一步步說明，讓您快速且有信心地解鎖 Aspose.3D 的完整功能。正確設定授權可移除評估水印、啟用高級 3D 格式，並確保完全符合 Aspose 的授權模式。

## 快速解答
- **設定 Aspose.3D 授權的主要方式是什麼？** 使用 `License` 類別，呼叫 `setLicense` 並傳入檔案路徑或串流。  
- **可以從串流載入授權嗎？** 可以 – 將 `.lic` 檔案包裝在 `FileInputStream` 中，傳給 `setLicense`。  
- **如果需要計量授權該怎麼做？** 建立 `Metered` 物件，並使用您的公私鑰呼叫 `setMeteredKey`。  
- **開發版是否需要授權？** 任何非評估情境皆需使用試用或臨時授權。  
- **支援哪些 Java 版本？** Aspose.3D 支援 Java 6 至 Java 21，涵蓋超過 15 個主要版本。

## `License` 類別是什麼？
`License` 類別是 Aspose.3D 的核心授權物件，負責將 `.lic` 檔案載入記憶體、驗證授權資訊，並在實例化後全域套用於 JVM 程序，使所有後續的 Aspose.3D 操作皆在授權模式下執行，無評估限制。

## 為什麼要設定 Aspose 3D 授權？
套用有效授權可啟用 **超過 50 種高級 3D 檔案格式**（包括 FBX、OBJ、STL、GLTF），並移除渲染圖像上的「Evaluation」水印。亦可解除場景大小限制，讓您處理 **高達 100 萬個頂點** 的模型而不會出現效能下降。

## 前置條件

在開始之前，請確保您已具備以下條件：

- 基本的 Java 程式設計知識。  
- 已安裝 Aspose.3D 套件。您可從 [release page](https://releases.aspose.com/3d/java/) 下載。

## 匯入套件

首先，將必要的套件匯入您的 Java 專案。確保 Aspose.3D 已加入 classpath。範例如下：

```java
import com.aspose.threed.License;
import com.aspose.threed.Metered;

import java.io.FileInputStream;
import java.io.IOException;
```

`License` 類別負責載入 `.lic` 檔案並全域套用，而 `Metered` 類別則透過驗證公私鑰，提供雲端計量授權功能。

## 如何從檔案套用授權？

直接從磁碟上的 `.lic` 檔案載入授權。此方式最適合桌面或本機部署，確保授權於啟動時讀取一次，並在 JVM 整個生命週期內快取，避免後續執行時的額外開銷。

### 步驟 1：建立 `License` 物件
實例化 `License` 類別，為接受授權檔案做好準備。

### 步驟 2：套用授權檔案
提供 `.lic` 檔案的絕對或相對路徑，呼叫 `setLicense`。此方法不回傳值，首次成功呼叫後授權會被快取，之後的呼叫成本極低。

```java
import com.aspose.threed.License;
import com.aspose.threed.Metered;

import java.io.FileInputStream;
import java.io.IOException;
```

## 如何從串流套用授權？

當授權檔案以資源形式嵌入、存放於安全位置，或需即時從遠端服務取得時，可使用串流方式。透過 `InputStream`，您可以避免暴露實體檔案路徑，並可將授權資料加密或封裝於 JAR 中，提高安全性，同時仍讓程式庫讀取授權位元組。

### 步驟 1：建立 `License` 物件
同前，先建立 `License` 類別的實例。

### 步驟 2：透過 `FileInputStream` 載入授權
開啟指向 `.lic` 檔案（或任何 `InputStream`）的 `FileInputStream`，並傳給 `setLicense`。串流會在讀取一次後自動關閉。

```java
License license = new License();
```

## 如何使用公私鑰進行計量授權？

計量授權讓您在沒有實體 `.lic` 檔案的情況下啟用 Aspose.3D，使用 Aspose 雲端服務發放的金鑰。此方式特別適合 SaaS 或雲端部署，免除在每個執行個體上管理授權檔案的麻煩；程式庫會向 Aspose 的計量伺服器驗證金鑰一次，然後在會話期間快取結果。

### 步驟 1：初始化 `Metered` 授權物件
`Metered` 類別代表雲端授權，負責向 Aspose 計量伺服器驗證使用情況。

### 步驟 2：設定公私鑰
呼叫 `setMeteredKey(publicKey, privateKey)`，傳入您購買計量授權時取得的金鑰。程式庫會向伺服器驗證一次，然後快取結果。

```java
license.setLicense("Aspose._3D.lic");
```

## 常見問題與技巧

- **找不到檔案** – 確認 `.lic` 檔案路徑相對於工作目錄是否正確，或改用絕對路徑。  
- **串流過早關閉** – 使用串流時，請保持 `License` 物件在整個應用程式期間存活；授權在首次成功呼叫後會被快取。  
- **計量金鑰不匹配** – 再次確認公私鑰屬於同一筆計量授權，拼寫錯誤會導致執行時例外。  
- **專業提示：** 將授權檔案存放於來源樹之外的安全位置，並透過環境變數載入，以避免將授權檔提交至版本控制。

## 結論

恭喜！您已成功學會 **如何在 Java 中設定 aspose 3d 授權**，包括從檔案套用、以串流方式載入，以及使用公私鑰的計量授權三種可靠方法。擁有授權後，您可以無縫將 Aspose.3D 整合至 Java 應用程式，解鎖所有高級 3D 處理功能，並符合 Aspose 的授權要求。

## 常見問答

**Q: Aspose.3D 是否相容所有 Java 版本？**  
A: 是的，Aspose.3D 支援 Java 6 至 Java 21，涵蓋超過 15 個主要版本。

**Q: 我可以在哪裡找到更多文件？**  
A: 您可參考文件 [here](https://reference.aspose.com/3d/java/)。

**Q: 購買前可以試用 Aspose.3D 嗎？**  
A: 可以，您可在此取得免費試用版 [here](https://releases.aspose.com/)。

**Q: 如何取得 Aspose.3D 的支援？**  
A: 請前往 [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) 取得支援。

**Q: 測試時需要臨時授權嗎？**  
A: 需要，請在此取得臨時授權 [here](https://purchase.aspose.com/temporary-license/)。

**Q: 檔案授權與計量授權有何差異？**  
A: 檔案授權是綁定特定產品版本的靜態 `.lic` 檔案；計量授權則透過公私鑰向 Aspose 的雲端計量服務驗證使用情況。

**Q: 可以在靜態初始化子程式中嵌入授權載入程式碼嗎？**  
A: 完全可以 – 將 `License` 初始化放在 static block 中，可確保類別首次載入時即套用授權。

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

## 相關教學

- [Aspose.3D Java 逐步授權指南](/3d/java/licensing/)
- [使用 Aspose 3D Java 建立 3D 場景](/3d/java/3d-scenes-and-models/)
- [使用 Aspose.3D 在 Java 中建立 3D 立方體並套用 PBR 材質](/3d/java/geometry/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}