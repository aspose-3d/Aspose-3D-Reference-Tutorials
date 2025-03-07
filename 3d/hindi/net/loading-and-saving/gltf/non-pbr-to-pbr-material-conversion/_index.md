---
title: गैर-पीबीआर से पीबीआर सामग्री रूपांतरण
linktitle: गैर-पीबीआर से पीबीआर सामग्री रूपांतरण
second_title: Aspose.3D .NET API
description: .NET के लिए Aspose.3D का अन्वेषण करें - गैर-पीबीआर सामग्री को आसानी से पीबीआर में परिवर्तित करें। व्यापक ट्यूटोरियल और शक्तिशाली एपीआई।
weight: 16
url: /hi/net/loading-and-saving/gltf/non-pbr-to-pbr-material-conversion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# गैर-पीबीआर से पीबीआर सामग्री रूपांतरण

## परिचय

गैर-पीबीआर (भौतिक रूप से आधारित रेंडरिंग) को पीबीआर सामग्री में परिवर्तित करने के लिए .NET के लिए Aspose.3D का उपयोग करने पर इस चरण-दर-चरण मार्गदर्शिका में आपका स्वागत है। Aspose.3D एक शक्तिशाली API है जो डेवलपर्स को उनके .NET अनुप्रयोगों में 3D फ़ाइल स्वरूपों के साथ निर्बाध रूप से काम करने की अनुमति देता है।

## आवश्यक शर्तें

इससे पहले कि हम ट्यूटोरियल में उतरें, सुनिश्चित करें कि आपके पास निम्नलिखित शर्तें हैं:

-  .NET के लिए Aspose.3D: सुनिश्चित करें कि आपके पास .NET लाइब्रेरी के लिए Aspose.3D स्थापित है। आप डाउनलोड लिंक पा सकते हैं[यहाँ](https://releases.aspose.com/3d/net/).

- C# की बुनियादी समझ: यह ट्यूटोरियल मानता है कि आपको C# प्रोग्रामिंग की बुनियादी समझ है।

- आईडीई (एकीकृत विकास पर्यावरण): .NET विकास के लिए अपना पसंदीदा आईडीई चुनें, जैसे कि विजुअल स्टूडियो।

## नामस्थान आयात करें

अपने C# कोड में, आवश्यक नामस्थान आयात करके प्रारंभ करें:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## चरण 1: एक नया 3डी दृश्य प्रारंभ करें

निम्नलिखित कोड का उपयोग करके एक नया 3D दृश्य बनाकर प्रारंभ करें:

```csharp
// एक्सस्टार्ट:नॉन_पीबीआरटूपीबीआरमटेरियल
// एक नया 3D दृश्य प्रारंभ करें
var scene = new Scene();
```

## चरण 2: एक 3डी ऑब्जेक्ट बनाएं

इसके बाद, एक 3D ऑब्जेक्ट बनाएं, उदाहरण के लिए, एक बॉक्स:

```csharp
var box = new Box();
scene.RootNode.CreateChildNode("box1", box).Material = new PhongMaterial() { DiffuseColor = new Vector3(1, 0, 1) };
```

## चरण 3: सामग्री रूपांतरण कॉन्फ़िगर करें

गैर-पीबीआर से पीबीआर रूपांतरण के लिए सामग्री रूपांतरण विकल्प सेट करें:

```csharp
GltfSaveOptions options = new GltfSaveOptions(FileFormat.GLTF2);
options.MaterialConverter = delegate (Material material)
{
    PhongMaterial phongMaterial = (PhongMaterial)material;
    return new PbrMaterial() { Albedo = new Vector3(phongMaterial.DiffuseColor.x, phongMaterial.DiffuseColor.y, phongMaterial.DiffuseColor.z) };
};
```

## चरण 4: जीएलटीएफ 2.0 प्रारूप में सहेजें

परिवर्तित दृश्य को GLTF 2.0 प्रारूप में सहेजें:

```csharp
scene.Save("Your Output Directory" + "Non_PBRtoPBRMaterial_Out.gltf", options);
// ExEnd:Non_PBRtoPBRMaterial
```

अपने विशिष्ट उपयोग के मामले के लिए आवश्यकतानुसार इन चरणों को दोहराएं, यह सुनिश्चित करते हुए कि प्रत्येक विवरण सही ढंग से कॉन्फ़िगर किया गया है।

## निष्कर्ष

बधाई हो! आपने .NET के लिए Aspose.3D का उपयोग करके गैर-पीबीआर सामग्री को पीबीआर में परिवर्तित करने का तरीका सफलतापूर्वक सीख लिया है। यह शक्तिशाली टूल आपके .NET अनुप्रयोगों में 3D ग्राफ़िक्स हेरफेर की अनंत संभावनाओं को खोलता है।

## अक्सर पूछे जाने वाले प्रश्न

### Q1: क्या Aspose.3D सभी 3D फ़ाइल स्वरूपों के साथ संगत है?

A1: हाँ, Aspose.3D आपकी परियोजनाओं में लचीलापन प्रदान करते हुए, 3D फ़ाइल स्वरूपों की एक विस्तृत श्रृंखला का समर्थन करता है।

### Q2: क्या मैं व्यावसायिक अनुप्रयोगों के लिए Aspose.3D का उपयोग कर सकता हूँ?

 ए2: बिल्कुल! Aspose.3D एक व्यावसायिक उत्पाद है, और आप इसे खरीद सकते हैं[यहाँ](https://purchase.aspose.com/buy).

### Q3: क्या मुझे परीक्षण के लिए अस्थायी लाइसेंस की आवश्यकता है?

 उ3: हाँ, आप परीक्षण उद्देश्यों के लिए एक अस्थायी लाइसेंस प्राप्त कर सकते हैं[यहाँ](https://purchase.aspose.com/temporary-license/).

### Q4: मुझे Aspose.3D के लिए समर्थन कहां मिल सकता है?

 A4: पर जाएँ[Aspose.3D फोरम](https://forum.aspose.com/c/3d/18) सामुदायिक समर्थन और चर्चा के लिए।

### Q5: क्या कोई निःशुल्क परीक्षण उपलब्ध है?

 A5: हां, आप निःशुल्क परीक्षण संस्करण तलाश सकते हैं[यहाँ](https://releases.aspose.com/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
