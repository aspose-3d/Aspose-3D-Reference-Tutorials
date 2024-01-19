---
title: लोड हो रहा है और सहेजा जा रहा है - कस्टम सहेजें विकल्प
linktitle: लोड हो रहा है और सहेजा जा रहा है - कस्टम सहेजें विकल्प
second_title: Aspose.3D .NET API
description: .NET के लिए Aspose.3D की शक्ति का अन्वेषण करें। कोलाडा, 3डीएस, एफबीएक्स, ओबीजे, एसटीएल, यू3डी, जीएलटीएफ, डीआरसी और आरवीएम प्रारूपों पर चरण-दर-चरण गाइड के साथ अपने 3डी दृश्य बचत को अनुकूलित करना सीखें।
type: docs
weight: 21
url: /hi/net/loading-and-saving/custom-save-options/
---
## परिचय

.NET के लिए Aspose.3D की दुनिया में आपका स्वागत है! यदि आप अपनी 3डी विकास क्षमताओं को बढ़ाना चाह रहे हैं, तो आप सही जगह पर हैं। इस ट्यूटोरियल में, हम लोडिंग और सेविंग फ़ंक्शंस में गहराई से उतरेंगे, विशेष रूप से कस्टम सेव विकल्पों पर ध्यान केंद्रित करेंगे। .NET के लिए Aspose.3D एक शक्तिशाली लाइब्रेरी है जो डेवलपर्स को 3D दृश्यों में कुशलतापूर्वक हेरफेर करने और सहेजने में सक्षम बनाती है।

## आवश्यक शर्तें

इससे पहले कि हम Aspose.3D की रोमांचक विशेषताओं की खोज शुरू करें, सुनिश्चित करें कि आपके पास निम्नलिखित शर्तें हैं:

- C# और .NET विकास की बुनियादी समझ।
-  .NET लाइब्रेरी के लिए Aspose.3D स्थापित किया गया। आप इसे यहां से डाउनलोड कर सकते हैं[रिलीज पेज](https://releases.aspose.com/3d/net/).
- विज़ुअल स्टूडियो या किसी अन्य पसंदीदा C# IDE के साथ स्थापित एक विकास वातावरण।

## नामस्थान आयात करें

आरंभ करने के लिए, आइए आवश्यक नामस्थान आयात करें:

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose.ThreeD.Shading;
using System.Drawing;
```

अब जब हमने मंच तैयार कर लिया है तो आइए ट्यूटोरियल को कई चरणों में विभाजित करें।

## चरण 1: कोलाडा सहेजें विकल्प

आइए कोलाडा से शुरुआत करें, जो एक लोकप्रिय 3डी फ़ाइल स्वरूप है। कोलाडा बचत विकल्पों को अनुकूलित करने के लिए इन चरणों का पालन करें:

### 1. निर्देशिका सेट करें:
   ```csharp
   string dataDir = "Your Document Directory";
   ```

### 2. कोलाडा सेव विकल्प प्रारंभ करें:
   ```csharp
   ColladaSaveOptions saveColladaOpts = new ColladaSaveOptions();
   ```

### 3. विकल्प कॉन्फ़िगर करें:
   ```csharp
   saveColladaOpts.Indented = true;
   saveColladaOpts.TransformStyle = ColladaTransformStyle.Matrix;
   saveColladaOpts.LookupPaths = new List<string>(new string[] { dataDir });
   ```

## चरण 2: विवेकपूर्ण 3डीएस सेव विकल्प

अब, आइए डिस्क्रीट 3DS और इसके अनुकूलन विकल्पों का पता लगाएं:

### 1. निर्देशिका सेट करें:
   ```csharp
   string dataDir = "Your Document Directory";
   ```

### 2. 3DS सेव विकल्प प्रारंभ करें:
   ```csharp
   Discreet3dsSaveOptions saveOpts = new Discreet3dsSaveOptions();
   ```

### 3. विकल्प कॉन्फ़िगर करें:
   ```csharp
   saveOpts.DuplicatedNameCounterBase = 2;
   // अतिरिक्त कॉन्फ़िगरेशन विकल्प...
   ```

FBX, OBJ, STL, U3D, glTF और DRC सेव विकल्पों के लिए इस चरण-दर-चरण दृष्टिकोण को जारी रखें, प्रत्येक को अपनी आवश्यकताओं के अनुसार अनुकूलित करें।

## चरण 3: glTF सहेजें विकल्प

अब, आइए glTF पर ध्यान केंद्रित करें, जो वेब और मोबाइल एप्लिकेशन में व्यापक रूप से उपयोग किया जाने वाला प्रारूप है। इन चरणों के साथ अपने glTF सेव विकल्पों को अनुकूलित करें:

### 1. आरंभिक दृश्य वस्तु:
   ```csharp
   Scene scene = new Scene();
   scene.RootNode.CreateChildNode("sphere", new Sphere());
   ```

### 2. glTF बचत विकल्प सेट करें:
   ```csharp
   GltfSaveOptions opt = new GltfSaveOptions(FileContentType.ASCII);
   opt.EmbedAssets = true;
   opt.UseCommonMaterials = true;
   opt.BufferFile = "mybuf.bin";
   ```

### 3. glTF फ़ाइल सहेजें:
   ```csharp
   scene.Save("Your Output Directory" + "glTFSaveOptions_out.gltf", opt);
   ```

डीआरसी और आरवीएम जैसे अन्य सेव विकल्पों के लिए समान संरचना का पालन करें।

## निष्कर्ष

बधाई हो! आपने .NET के लिए Aspose.3D में कस्टम सेव विकल्पों का सफलतापूर्वक पता लगा लिया है। यह शक्तिशाली लाइब्रेरी आपकी 3डी दृश्य बचत प्रक्रिया को अनुकूलित करने के लिए असंख्य विकल्प प्रदान करती है।

## अक्सर पूछे जाने वाले प्रश्न

### Q1: क्या मैं अन्य .NET फ्रेमवर्क के साथ .NET के लिए Aspose.3D का उपयोग कर सकता हूँ?

A1: हां, Aspose.3D विभिन्न .NET फ्रेमवर्क के साथ संगत है, जो आपके विकास परिवेश में लचीलापन सुनिश्चित करता है।

### Q2: क्या Aspose.3D के लिए कोई लाइसेंसिंग विकल्प उपलब्ध हैं?

 उ2: हां, आप लाइसेंसिंग विकल्प तलाश सकते हैं[यहाँ](https://purchase.aspose.com/buy).

### Q3: मुझे Aspose.3D-संबंधित प्रश्नों के लिए समर्थन कहां मिल सकता है?

 A3: आप पर समर्थन मांग सकते हैं[Aspose.3D फोरम](https://forum.aspose.com/c/3d/18).

### Q4: क्या कोई निःशुल्क परीक्षण उपलब्ध है?

 उ4: हाँ, आप निःशुल्क परीक्षण का उपयोग कर सकते हैं[यहाँ](https://releases.aspose.com/).

### Q5: मैं Aspose.3D के लिए अस्थायी लाइसेंस कैसे प्राप्त कर सकता हूं?

 A5: एक अस्थायी लाइसेंस प्राप्त करें[यहाँ](https://purchase.aspose.com/temporary-license/).