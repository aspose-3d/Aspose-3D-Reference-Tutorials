---
title: लीनियर एक्सट्रूज़न में ट्विस्ट ऑफसेट
linktitle: लीनियर एक्सट्रूज़न में ट्विस्ट ऑफसेट
second_title: Aspose.3D .NET API
description: लीनियर एक्सट्रूज़न में ट्विस्ट ऑफसेट पर हमारे चरण-दर-चरण गाइड के साथ .NET के लिए Aspose.3D के जादू का अन्वेषण करें। अपने 3D प्रोजेक्ट को सहजता से उन्नत करें।
type: docs
weight: 15
url: /hi/net/3d-modeling/linear-extrusion/twist-offset-in-linear-extrusion/
---
## परिचय

.NET के लिए Aspose.3D की दुनिया में आपका स्वागत है, एक बहुमुखी लाइब्रेरी जो डेवलपर्स को आसानी से 3D हेरफेर को संभालने के लिए सशक्त बनाती है। इस ट्यूटोरियल में, हम दिलचस्प विशेषताओं में से एक - "रैखिक एक्सट्रूज़न में ट्विस्ट ऑफसेट" पर प्रकाश डालेंगे। यदि आप अपने 3डी प्रोग्रामिंग कौशल को उन्नत करने के लिए तैयार हैं, तो आइए सीधे इसमें उतरें!

## आवश्यक शर्तें

इससे पहले कि हम इस रोमांचक यात्रा पर निकलें, सुनिश्चित करें कि आपके पास निम्नलिखित शर्तें हैं:

-  .NET लाइब्रेरी के लिए Aspose.3D: लाइब्रेरी को डाउनलोड और इंस्टॉल करें[रिलीज पेज](https://releases.aspose.com/3d/net/).

- आपका विकास परिवेश: सुनिश्चित करें कि आपका विकास परिवेश तैयार है और शुरू करने के लिए तैयार है।

## नामस्थान आयात करें

.NET के लिए Aspose.3D द्वारा प्रदान की गई कार्यक्षमता तक पहुँचने के लिए आवश्यक नामस्थान आयात करके प्रारंभ करें। आपके कोड में, यह ऐसा दिख सकता है:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

अब, आइए लीनियर एक्सट्रूज़न में ट्विस्ट ऑफसेट में महारत हासिल करने के लिए उदाहरण को प्रबंधनीय चरणों में विभाजित करें:

## चरण 1: बेस प्रोफ़ाइल प्रारंभ करें

एक आधार प्रोफ़ाइल बनाकर शुरुआत करें, यहां एक निर्दिष्ट गोलाई त्रिज्या के साथ एक आयताकार आकार का उदाहरण दिया गया है।

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## चरण 2: एक दृश्य बनाएं

अपने नोड्स और आकृतियों को होस्ट करने के लिए एक 3D दृश्य बनाएं।

```csharp
Scene scene = new Scene();
```

## चरण 3: नोड्स बनाएं

दृश्य के भीतर बाएं और दाएं दोनों तरफ नोड्स बनाएं।

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

## चरण 4: बाएं नोड पर रैखिक एक्सट्रूज़न

ट्विस्ट और स्लाइस प्रॉपर्टी का उपयोग करके बाएं नोड पर रैखिक एक्सट्रूज़न करें।

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## चरण 5: ट्विस्ट ऑफसेट के साथ दाएं नोड पर रैखिक एक्सट्रूज़न

दाएं नोड पर, ट्विस्ट, ट्विस्ट ऑफसेट और स्लाइस प्रॉपर्टी का उपयोग करके रैखिक एक्सट्रूज़न करें।

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

## चरण 6: 3डी दृश्य सहेजें

फ़ाइल स्वरूप को वेवफ्रंटओबीजे के रूप में निर्दिष्ट करते हुए, 3डी दृश्य को अपनी वांछित आउटपुट निर्देशिका में सहेजें।

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

बधाई हो! आपने .NET के लिए Aspose.3D का उपयोग करके लीनियर एक्सट्रूज़न में ट्विस्ट ऑफ़सेट को सफलतापूर्वक कार्यान्वित किया है।

## निष्कर्ष

इस ट्यूटोरियल में, हमने .NET के लिए Aspose.3D की शक्तिशाली क्षमताओं का पता लगाया, विशेष रूप से लीनियर एक्सट्रूज़न में ट्विस्ट ऑफ़सेट पर ध्यान केंद्रित किया। इन नए पाए गए कौशलों के साथ, आप अपने 3डी प्रोजेक्ट्स में गतिशीलता लाने के लिए अच्छी तरह से सुसज्जित हैं।

## अक्सर पूछे जाने वाले प्रश्न

### Q1: क्या मैं अन्य प्रोग्रामिंग भाषाओं के साथ .NET के लिए Aspose.3D का उपयोग कर सकता हूँ?

A1: Aspose.3D मुख्य रूप से .NET भाषाओं का समर्थन करता है, लेकिन Aspose जावा और अन्य प्लेटफार्मों के लिए समान लाइब्रेरी प्रदान करता है।

### Q2: मैं .NET के लिए Aspose.3D के लिए अस्थायी लाइसेंस कैसे प्राप्त करूं?

 ए2: विजिट करें[इस लिंक](https://purchase.aspose.com/temporary-license/)परीक्षण उद्देश्यों के लिए अस्थायी लाइसेंस प्राप्त करना।

### Q3: क्या .NET के लिए Aspose.3D के लिए कोई सामुदायिक मंच है?

 उ3: बिल्कुल! समुदाय में शामिल हों[Aspose.3D फोरम](https://forum.aspose.com/c/3d/18) साथी डेवलपर्स के साथ जुड़ना और सहायता प्राप्त करना।

### Q4: क्या अतिरिक्त उदाहरण और दस्तावेज़ उपलब्ध हैं?

 ए4: अन्वेषण करें[प्रलेखन](https://reference.aspose.com/3d/net/) व्यापक मार्गदर्शिकाओं और उदाहरणों के लिए।

### Q5: मैं .NET के लिए Aspose.3D कहां से खरीद सकता हूं?

 A5: की ओर जाएं[इस लिंक](https://purchase.aspose.com/buy) खरीदारी करने और Aspose.3D की पूरी क्षमता को अनलॉक करने के लिए।