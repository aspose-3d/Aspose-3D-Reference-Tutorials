---
title: व्यूपोर्ट को 3डी दृश्यों में कैप्चर करना
linktitle: व्यूपोर्ट को 3डी दृश्यों में कैप्चर करना
second_title: Aspose.3D .NET API
description: .NET के लिए Aspose.3D का उपयोग करके आश्चर्यजनक 3D व्यूपोर्ट कैप्चर करना सीखें। लचीलेपन के साथ दृश्यों को प्रस्तुत करने के लिए चरण-दर-चरण मार्गदर्शिका।
weight: 11
url: /hi/net/rendering/capture-viewport/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# व्यूपोर्ट को 3डी दृश्यों में कैप्चर करना

## परिचय

3डी ग्राफ़िक्स और विज़ुअलाइज़ेशन के क्षेत्र में, व्यूपोर्ट कैप्चर करना एक आवश्यक कौशल है जो आपके दृश्यों की गहराई और विवरण को बढ़ाता है। .NET के लिए Aspose.3D 3D दृश्यों को प्रस्तुत करने और उनमें हेरफेर करने के लिए एक मजबूत समाधान प्रदान करता है। यह ट्यूटोरियल आपको Aspose.3D का उपयोग करके 3D दृश्यों में व्यूपोर्ट कैप्चर करने की प्रक्रिया में मार्गदर्शन करेगा, जिससे आप आसानी से आश्चर्यजनक विज़ुअलाइज़ेशन बना सकेंगे।

## आवश्यक शर्तें

ट्यूटोरियल में जाने से पहले, सुनिश्चित करें कि आपके पास निम्नलिखित आवश्यक शर्तें हैं:

-  .NET लाइब्रेरी के लिए Aspose.3D: सुनिश्चित करें कि आपके पास Aspose.3D लाइब्रेरी स्थापित है। आप इसे यहां से डाउनलोड कर सकते हैं[यहाँ](https://releases.aspose.com/3d/net/).

## नामस्थान आयात करें

आरंभ करने के लिए, अपने .NET प्रोजेक्ट में आवश्यक नामस्थान आयात करें:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using System.Drawing;
using System.Drawing.Imaging;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
```

## चरण 1: मौजूदा 3डी दृश्य लोड करें

अपने प्रोजेक्ट में मौजूदा 3D दृश्य लोड करके शुरुआत करें। निम्नलिखित कोड स्निपेट इसे प्रदर्शित करता है:

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

## चरण 2: एक कैमरा बनाएं

इसके बाद, कैमरे का एक उदाहरण बनाएं और उसकी स्थिति और लक्ष्य निर्धारित करें:

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

## चरण 3: दृश्य में प्रकाश व्यवस्था जोड़ें

प्रकाश स्रोत जोड़कर अपने दृश्य को बेहतर बनाएं। नीचे दिया गया कोड स्निपेट दिखाता है कि पॉइंट लाइट कैसे बनाई जाती है:

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

## चरण 4: रेंडरर और रेंडर लक्ष्य को कॉन्फ़िगर करें

रेंडरर सेट करें और दृश्य कैप्चर करने के लिए रेंडर लक्ष्य बनाएं:

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    renderer.EnableShadows = false;

    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // ... (अगले चरणों में जारी)
    }
}
```

## चरण 5: व्यूपोर्ट और रेंडर को परिभाषित करें

व्यूपोर्ट को परिभाषित करें और आउटपुट छवियां उत्पन्न करने के लिए दृश्य प्रस्तुत करें:

```csharp
Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-1viewports_out.png", ImageFormat.Png);
```

## चरण 6: व्यूपोर्ट संशोधित करें और दोबारा प्रस्तुत करें

Aspose.3D के लचीलेपन को प्रदर्शित करते हुए व्यूपोर्ट को संशोधित करें और दृश्य को एक बार फिर प्रस्तुत करें:

```csharp
vp.Area = new RelativeRectangle() { ScaleWidth = 0.5f, ScaleHeight = 1 };
rt.CreateViewport(camera, new RelativeRectangle() { ScaleX = 0.5f, ScaleWidth = 0.5f, ScaleHeight = 1 });
camera.FieldOfView = 90;
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-2viewports_out.png", ImageFormat.Png);
```

वांछित दृश्य प्रभाव प्राप्त करने के लिए विभिन्न कॉन्फ़िगरेशन के साथ प्रयोग करना जारी रखें।

## निष्कर्ष

इस ट्यूटोरियल में, हमने .NET के लिए Aspose.3D का उपयोग करके 3D दृश्यों में व्यूपोर्ट कैप्चर करने की प्रक्रिया का पता लगाया। इसकी शक्तिशाली विशेषताओं का लाभ उठाकर, आप मनोरम दृश्य अनुभव प्रदान करते हुए अपने 3डी ग्राफ़िक्स प्रोजेक्ट को नई ऊंचाइयों तक पहुंचा सकते हैं।

## अक्सर पूछे जाने वाले प्रश्न

### Q1: क्या Aspose.3D अन्य 3D फ़ाइल स्वरूपों के साथ संगत है?

A1: हाँ, Aspose.3D विभिन्न 3D फ़ाइल स्वरूपों का समर्थन करता है, जो डिज़ाइन टूल की एक विस्तृत श्रृंखला के साथ संगतता सुनिश्चित करता है।

### Q2: क्या मैं गेम डेवलपमेंट के लिए Aspose.3D का उपयोग कर सकता हूँ?

A2: जबकि Aspose.3D मुख्य रूप से ग्राफिक्स और विज़ुअलाइज़ेशन के लिए डिज़ाइन किया गया है, इसकी कार्यक्षमताएँ गेम विकास के कुछ पहलुओं को पूरक कर सकती हैं।

### Q3: मुझे अतिरिक्त उदाहरण और दस्तावेज़ कहां मिल सकते हैं?

 A3: व्यापक का अन्वेषण करें[Aspose.3D दस्तावेज़ीकरण](https://reference.aspose.com/3d/net/) अधिक उदाहरणों और विस्तृत जानकारी के लिए।

### Q4: क्या कोई निःशुल्क परीक्षण उपलब्ध है?

 उ4: हाँ, आप निःशुल्क परीक्षण का उपयोग कर सकते हैं[यहाँ](https://releases.aspose.com/).

### Q5: मैं कैसे मदद मांग सकता हूं या समुदाय में भाग कैसे ले सकता हूं?

 A5: Aspose.3D समुदाय में शामिल हों[सहयता मंच](https://forum.aspose.com/c/3d/18) सहायता एवं सहयोग के लिए.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
