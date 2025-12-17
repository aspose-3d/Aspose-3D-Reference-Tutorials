---
date: 2025-12-17
description: 了解如何在 Aspose.3D for Java 中設定授權，以及如何使用公私鑰進行計量授權。
linktitle: Applying a License in Aspose.3D for Java
second_title: Aspose.3D Java API
title: 在 Aspose.3D for Java 中設定授權 – 完整指南
url: /zh-hant/java/licensing/applying-license-in-aspose-3d/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 如何在 Aspose.3D for Java 中設定授權

## 介紹

歡迎！在本分步教學中，您將學會 **如何在 Java 應用程式中設定 Aspose.3D 的授權**，同時了解 **如何使用公私鑰** 進行計量授權。Aspose.3D 是一套功能強大的 Java 函式庫，可簡化 3D 檔案格式的操作，而有效的授權則能解鎖全部功能。完成本指南後，您即可將授權無縫整合至任何 Java 專案。

## 快速答覆
- **設定授權的主要方式是什麼？** 使用 `License` 類別，呼叫 `setLicense` 並傳入檔案路徑或串流。  
- **可以從串流載入授權嗎？** 可以——`FileInputStream` 完全相容。  
- **公私鑰的用途是什麼？** 透過 `Metered` 類別啟用計量授權。  
- **開發階段需要授權嗎？** 測試時使用暫時或試用授權即可；正式上線則需正式授權。  
- **支援哪些 Java 版本？** Aspose.3D 支援 Java 6 及以上版本。

## 前置條件

在開始之前，請確保您已具備：

- 基本的 Java 程式設計知識。  
- 已將 Aspose.3D 函式庫加入專案。可從[發行頁面](https://releases.aspose.com/3d/java/)下載。  
- 有效的 `.lic` 檔案或您的公私鑰。

## 匯入套件

在 Java 原始檔中加入必要的匯入語句，並確保 Aspose.3D JAR 已在 classpath 中。

```java
import com.aspose.threed.License;
import com.aspose.threed.Metered;

import java.io.FileInputStream;
import java.io.IOException;
```

## 使用檔案設定授權

### 步驟 1：建立 License 物件

實例化 `License` 類別——此物件將保存授權資訊。

```java
License license = new License();
```

### 步驟 2：從檔案設定授權

提供相對或絕對路徑指向您的 `.lic` 檔案，然後套用授權。

```java
license.setLicense("Aspose._3D.lic");
```

> **專業提示：** 請將授權檔案放在來源控制目錄之外，以免意外洩漏。

## 使用串流設定授權

### 步驟 1：建立 License 物件

同上，先建立一個全新的 `License` 實例。

```java
License license = new License();
```

### 步驟 2：從串流設定授權

將授權檔案讀入 `FileInputStream`，再將串流傳給 `setLicense`。`try‑with‑resources` 區塊會自動關閉串流。

```java
try (FileInputStream myStream = new FileInputStream("Aspose._3D.lic")) {
    license.setLicense(myStream);
}
```

## 使用公私鑰進行計量授權

### 步驟 1：初始化 Metered 授權物件

建立 `Metered` 類別的實例，該類別負責計量（即付費即用）授權。

```java
Metered metered = new Metered();
```

### 步驟 2：設定公私鑰

提供您從 Aspose 取得的金鑰。這些金鑰讓函式庫能向授權伺服器回報使用情況。

```java
metered.setMeteredKey("your-public-key", "your-private-key");
```

> **警告：** 千萬不要在公開發佈的 JAR 中硬編碼私鑰。建議從安全位置或環境變數載入。

## 常見使用情境

- **企業級 3D 渲染管線** – 設定授權後即可解鎖高效能 API。  
- **自動化測試環境** – 使用暫時授權（請參考 FAQ）驗證功能，無需購買正式授權。  
- **計量 SaaS 解決方案** – 整合公私鑰，依實際使用量向客戶收費。

## 結論

恭喜！您現在已掌握 **如何在 Java 中使用檔案、串流設定 Aspose.3D 授權**，以及 **如何使用公私鑰進行計量授權**。依照上述步驟，您可以自信地將 Aspose.3D 整合至任何 Java 應用程式，充分發揮其 3D 處理功能。

## 常見問題

**Q1：Aspose.3D 是否相容所有 Java 版本？**  
A1：是的，Aspose.3D 支援 Java 6 及以上版本。

**Q2：我可以在哪裡找到更多文件？**  
A2：請參閱文件[此處](https://reference.aspose.com/3d/java/)。

**Q3：我可以在購買前試用 Aspose.3D 嗎？**  
A3：可以，請在[此處](https://releases.aspose.com/)取得免費試用。

**Q4：如何取得 Aspose.3D 的支援？**  
A4：前往[Aspose.3D 論壇](https://forum.aspose.com/c/3d/18)取得社群與官方支援。

**Q5：測試時需要暫時授權嗎？**  
A5：需要，請在[此處](https://purchase.aspose.com/temporary-license/)取得暫時授權。

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}
{{< blocks/products/products-backtop-button >}}

---

**最後更新：** 2025-12-17  
**測試環境：** Aspose.3D 24.11 for Java  
**作者：** Aspose  

---