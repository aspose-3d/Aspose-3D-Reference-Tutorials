---
title: रैखिक बाहर निकालना में दिशा
linktitle: रैखिक बाहर निकालना में दिशा
second_title: Aspose.3D .NET API
description: .NET के लिए Aspose.3D के साथ 3D मॉडलिंग की दुनिया को अनलॉक करें। दिशा रैखिक एक्सट्रूज़न सीखें, रचनात्मकता को बढ़ावा दें, और सहजता से इमर्सिव एप्लिकेशन तैयार करें।
weight: 11
url: /hi/net/3d-modeling/linear-extrusion/direction-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# रैखिक बाहर निकालना में दिशा

## परिचय

सॉफ्टवेयर विकास की गतिशील दुनिया में, इमर्सिव 3डी मॉडल बनाना एक अनिवार्य कौशल है। .NET के लिए Aspose.3D डेवलपर्स को उनके अनुप्रयोगों में 3D मॉडलिंग की क्षमता का उपयोग करने के लिए उपकरणों का एक मजबूत सेट प्रदान करता है। इस ट्यूटोरियल में, हम लीनियर एक्सट्रूज़न की दिलचस्प दुनिया में उतरेंगे और "डायरेक्शन इन लीनियर एक्सट्रूज़न" सुविधा की बारीकियों का पता लगाएंगे।

## आवश्यक शर्तें

इससे पहले कि हम इस रोमांचक यात्रा पर निकलें, सुनिश्चित करें कि आपके पास निम्नलिखित शर्तें हैं:

-  .NET के लिए Aspose.3D: यहां से लाइब्रेरी डाउनलोड और इंस्टॉल करें[Aspose.3D .NET दस्तावेज़ीकरण](https://reference.aspose.com/3d/net/).

- विकास परिवेश: सुनिश्चित करें कि आपके पास एक कार्यशील .NET विकास परिवेश स्थापित है।

## नामस्थान आयात करें

अपने .NET प्रोजेक्ट में, Aspose.3D की कार्यक्षमता तक पहुँचने के लिए आवश्यक नेमस्पेस आयात करें। अपने कोड की शुरुआत में निम्नलिखित पंक्तियाँ जोड़ें:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## चरण 1: बेस प्रोफ़ाइल प्रारंभ करें

एक्सट्रूड किए जाने वाले बेस प्रोफाइल को इनिशियलाइज़ करके शुरुआत करें। इस उदाहरण में, हम 0.3 की गोलाई त्रिज्या के साथ एक आयताकार आकार बनाते हैं।

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## चरण 2: एक 3डी दृश्य बनाएं

एक दृश्य बनाकर अपनी 3डी उत्कृष्ट कृति के लिए आधार तैयार करें।

```csharp
Scene scene = new Scene();
```

## चरण 3: नोड्स बनाएं

अपने 3D वातावरण के विभिन्न घटकों का प्रतिनिधित्व करने के लिए दृश्य के भीतर नोड्स उत्पन्न करें।

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(8, 0, 0);
```

## चरण 4: बिना दिशा के रैखिक बाहर निकालना

 का उपयोग करके बाएं नोड पर रैखिक एक्सट्रूज़न करें`Twist` और`Slices` गुण।

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## चरण 5: दिशा के साथ रैखिक बाहर निकालना

 को शामिल करके एक्सट्रूज़न क्षमताओं का विस्तार करें`Direction` सही नोड में संपत्ति.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, Direction = new Vector3(0.3, 0.2, 1) });
```

## चरण 6: 3डी दृश्य सहेजें

 3डी दृश्य को सहेजकर अपनी रचना को सुरक्षित रखें। प्रतिस्थापित करें`"Your Output Directory"` वांछित निर्देशिका के साथ.

```csharp
scene.Save("Your Output Directory" + "DirectionInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

बधाई हो! आपने पारंपरिक और दिशात्मक दोनों दृष्टिकोणों की खोज करते हुए, .NET के लिए Aspose.3D के साथ रैखिक एक्सट्रूज़न को सफलतापूर्वक लागू किया है।

## निष्कर्ष

इस ट्यूटोरियल में, हमने .NET के लिए Aspose.3D का उपयोग करके 3D मॉडलिंग के आकर्षक क्षेत्र में भ्रमण किया। दिशा के साथ और बिना दिशा के रैखिक एक्सट्रूज़न, दृश्यमान आश्चर्यजनक एप्लिकेशन बनाने के इच्छुक डेवलपर्स के लिए अनंत संभावनाएं खोलता है। Aspose.3D के साथ, 3D मॉडलिंग की शक्ति आपकी उंगलियों पर है।

## अक्सर पूछे जाने वाले प्रश्न

### Q1: मैं .NET के लिए Aspose.3D के लिए अस्थायी लाइसेंस कैसे प्राप्त कर सकता हूं?

 A1: यात्रा[अस्थायी लाइसेंस प्रदान करें](https://purchase.aspose.com/temporary-license/) अस्थायी लाइसेंस प्राप्त करने के लिए.

### Q2: मुझे Aspose.3D के लिए समर्थन कहां मिल सकता है?

 A2: शामिल हों[Aspose.3D फोरम](https://forum.aspose.com/c/3d/18) सहायता प्राप्त करना और समुदाय से जुड़ना।

### Q3: क्या कोई निःशुल्क परीक्षण उपलब्ध है?

 उ3: हाँ, नि:शुल्क परीक्षण के साथ सुविधाओं का अन्वेषण करें[Aspose.3D रिलीज़](https://releases.aspose.com/).

### Q4: मैं .NET के लिए Aspose.3D कैसे खरीदूं?

 A4: पर नेविगेट करें[Aspose खरीद पृष्ठ](https://purchase.aspose.com/buy) लाइसेंसिंग विकल्पों और खरीदारी विवरण के लिए।

### Q5: मुझे .NET के लिए Aspose.3D के लिए विस्तृत दस्तावेज़ कहां मिल सकते हैं?

 A5: व्यापक का संदर्भ लें[Aspose.3D .NET दस्तावेज़ीकरण](https://reference.aspose.com/3d/net/) गहन जानकारी के लिए.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
