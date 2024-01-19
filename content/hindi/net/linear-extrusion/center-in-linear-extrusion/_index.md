---
title: रैखिक एक्सट्रूज़न में केंद्र
linktitle: रैखिक एक्सट्रूज़न में केंद्र
second_title: Aspose.3D .NET API
description: .NET के लिए Aspose.3D के साथ 3D मॉडलिंग की दुनिया का अन्वेषण करें। रैखिक एक्सट्रूज़न तकनीकों को केंद्र में रखें, आश्चर्यजनक डिज़ाइन बनाएं और अपनी रचनात्मकता को उजागर करें।
type: docs
weight: 10
url: /hi/net/linear-extrusion/center-in-linear-extrusion/
---
## परिचय

.NET के लिए Aspose.3D का उपयोग करके रैखिक एक्सट्रूज़न में महारत हासिल करने पर इस व्यापक मार्गदर्शिका में आपका स्वागत है। यदि आप अपने 3डी मॉडलिंग कौशल को बढ़ाना और आश्चर्यजनक एक्सट्रूज़न बनाना चाहते हैं, तो आप सही जगह पर हैं। इस ट्यूटोरियल में, हम लीनियर एक्सट्रूज़न तकनीक में गहराई से उतरेंगे, विशेष रूप से आपके डिज़ाइन को एक नए स्तर पर लाने के लिए केंद्रित पहलू पर ध्यान केंद्रित करेंगे।

## आवश्यक शर्तें

इससे पहले कि हम इस रोमांचक यात्रा पर निकलें, सुनिश्चित करें कि आपके पास निम्नलिखित शर्तें हैं:

- C# प्रोग्रामिंग भाषा की बुनियादी समझ।
- आपकी मशीन पर विज़ुअल स्टूडियो स्थापित है।
-  .NET लाइब्रेरी के लिए Aspose.3D, जिसे आप यहां से डाउनलोड कर सकते हैं[Aspose.3D .NET दस्तावेज़ीकरण](https://reference.aspose.com/3d/net/).
-  सुनिश्चित करें कि आपके पास पहुंच है[Aspose.3D .NET दस्तावेज़ीकरण](https://reference.aspose.com/3d/net/) पूरे ट्यूटोरियल में संदर्भ के लिए।

## नामस्थान आयात करें

चीजों को शुरू करने के लिए, आइए आवश्यक नामस्थान आयात करें। ये हमारी 3डी मॉडलिंग उत्कृष्ट कृति की नींव रखेंगे।

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## चरण 1: बेस प्रोफ़ाइल प्रारंभ करें

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## चरण 2: एक 3डी दृश्य बनाएं

```csharp
Scene scene = new Scene();
```

## चरण 3: बाएँ और दाएँ नोड बनाएँ

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## चरण 4: बाएं नोड पर रैखिक एक्सट्रूज़न करें

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## चरण 5: संदर्भ के लिए ग्राउंड प्लेन सेट करें

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## चरण 6: दाएं नोड पर रैखिक एक्सट्रूज़न करें

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## चरण 7: संदर्भ के लिए ग्राउंड प्लेन सेट करें (दायां नोड)

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## चरण 8: 3डी दृश्य सहेजें

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## निष्कर्ष

बधाई हो! आपने .NET के लिए Aspose.3D का उपयोग करके सेंटरिंग के साथ रैखिक एक्सट्रूज़न की कला में सफलतापूर्वक महारत हासिल कर ली है। विभिन्न मापदंडों के साथ प्रयोग करने और इस तकनीक द्वारा प्रदान की जाने वाली विशाल संभावनाओं का पता लगाने के लिए स्वतंत्र महसूस करें।

## अक्सर पूछे जाने वाले प्रश्न

### Q1: क्या मैं अन्य प्रोग्रामिंग भाषाओं के साथ .NET के लिए Aspose.3D का उपयोग कर सकता हूँ?

A1: Aspose.3D मुख्य रूप से C# और VB.NET जैसी .NET भाषाओं का समर्थन करता है।

### Q2: मुझे Aspose.3D-संबंधित प्रश्नों के लिए समर्थन कहां मिल सकता है?

 A2: पर जाएँ[Aspose.3D फोरम](https://forum.aspose.com/c/3d/18) समर्पित समर्थन और चर्चा के लिए।

### Q3: क्या .NET के लिए Aspose.3D का निःशुल्क परीक्षण उपलब्ध है?

 उ3: हाँ, आप नि:शुल्क परीक्षण का उपयोग कर सकते हैं[यहाँ](https://releases.aspose.com/).

### Q4: मैं .NET के लिए Aspose.3D के लिए अस्थायी लाइसेंस कैसे प्राप्त कर सकता हूं?

 उ4: आप एक अस्थायी लाइसेंस प्राप्त कर सकते हैं[यहाँ](https://purchase.aspose.com/temporary-license/).

### Q5: मैं .NET लाइसेंस के लिए Aspose.3D कहां से खरीद सकता हूं?

 A5: अपना लाइसेंस खरीदें[यहाँ](https://purchase.aspose.com/buy).
