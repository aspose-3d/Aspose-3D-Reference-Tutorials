---
title: 3डी व्यूपोर्ट में दृश्य प्रभाव लागू करना
linktitle: 3डी व्यूपोर्ट में दृश्य प्रभाव लागू करना
second_title: Aspose.3D .NET API
description: .NET के लिए Aspose.3D के साथ 3D विज़ुअलाइज़ेशन की दुनिया का अन्वेषण करें। चरण-दर-चरण ट्यूटोरियल का उपयोग करके अपने दृश्यों पर मनोरम दृश्य प्रभाव लागू करना सीखें। पिक्सेलेशन, ग्रेस्केल, एज डिटेक्शन और ब्लर इफेक्ट्स के साथ अपने प्रोजेक्ट्स को उन्नत करें।
weight: 10
url: /hi/net/rendering/apply-visual-effects/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3डी व्यूपोर्ट में दृश्य प्रभाव लागू करना

## परिचय

3डी दृश्यों की दृश्य अपील को बढ़ाना गहन अनुभव बनाने का एक महत्वपूर्ण पहलू है। .NET के लिए Aspose.3D, 3D व्यूपोर्ट पर दृश्य प्रभाव लागू करने के लिए उपकरणों का एक शक्तिशाली सेट प्रदान करता है। इस ट्यूटोरियल में, हम 3डी दृश्य में पिक्सेलेशन, ग्रेस्केल, एज डिटेक्शन और ब्लर सहित विभिन्न प्रभावों को लागू करने की प्रक्रिया से गुजरेंगे।

## आवश्यक शर्तें

ट्यूटोरियल में जाने से पहले, सुनिश्चित करें कि आपके पास निम्नलिखित हैं:

- C# और .NET विकास का कार्यसाधक ज्ञान।
-  .NET लाइब्रेरी के लिए Aspose.3D स्थापित किया गया। आप इसे यहां से डाउनलोड कर सकते हैं[यहाँ](https://releases.aspose.com/3d/net/).
- प्रयोग के लिए एक 3D दृश्य फ़ाइल (उदाहरण के लिए, "scene.obj")।

## नामस्थान आयात करें

आरंभ करने के लिए, Aspose.3D और अन्य निर्भरताओं के लिए आवश्यक नामस्थान आयात करें। अपने कोड में निम्नलिखित पंक्तियाँ जोड़ें:

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

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

 का उपयोग करके अपना 3D दृश्य लोड करें`Scene` कक्षा।

## चरण 2: एक कैमरा बनाएं

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

एक कैमरा इंस्टेंस बनाएं और उसकी स्थिति और लक्ष्य निर्धारित करें।

## चरण 3: दृश्य में प्रकाश जोड़ें

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

दृश्य प्रभावों को बढ़ाने के लिए प्रकाश व्यवस्था का परिचय दें।

## चरण 4: एक रेंडरर और रेंडर लक्ष्य बनाएं

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    // रेंडरर सेटिंग्स कॉन्फ़िगर करें
    renderer.EnableShadows = false;

    // एक रेंडर लक्ष्य बनाएं
    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // व्यूपोर्ट कॉन्फ़िगर करें
        Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });

        // दृश्य को बनावट के अनुसार प्रस्तुत करें
        renderer.Render(rt);

        // प्रस्तुत बनावट को एक फ़ाइल में सहेजें
        ((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "Original_viewport_out.png", ImageFormat.Png);

        // प्रसंस्करण के बाद के प्रभावों को जारी रखें...
    }
}
```

दृश्य को कैप्चर करने के लिए एक रेंडरर और एक रेंडर लक्ष्य बनाएं।

## चरण 5: प्रसंस्करण के बाद प्रभाव लागू करें

### चरण 5.1 पिक्सेलेशन प्रभाव

```csharp
// पिक्सेलेशन प्रभाव बनाएं
PostProcessing pixelation = renderer.GetPostProcessing("pixelation");
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_pixelation_out.png", ImageFormat.Png);
```

पिक्सेलेशन प्रभाव लागू करें और परिणाम सहेजें।

### चरण 5.2 ग्रेस्केल प्रभाव

```csharp
// ग्रेस्केल प्रभाव बनाएँ
PostProcessing grayscale = renderer.GetPostProcessing("grayscale");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale_out.png", ImageFormat.Png);
```

ग्रेस्केल प्रभाव लागू करें और परिणाम सहेजें।

### चरण 5.3 प्रभावों को संयोजित करें

```csharp
// ग्रेस्केल और पिक्सेलेशन प्रभाव को मिलाएं
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale+pixelation_out.png", ImageFormat.Png);
```

अद्वितीय परिणामों के लिए अनेक प्रभावों को संयोजित करें।

### चरण 5.4 एज डिटेक्शन प्रभाव

```csharp
// एज डिटेक्शन प्रभाव बनाएं
PostProcessing edgedetection = renderer.GetPostProcessing("edge-detection");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(edgedetection);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_edgedetection_out.png", ImageFormat.Png);
```

एज डिटेक्शन इफ़ेक्ट लागू करें और परिणाम सहेजें।

### चरण 5.5 धुंधला प्रभाव

```csharp
// धुंधला प्रभाव बनाएँ
PostProcessing blur = renderer.GetPostProcessing("blur");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(blur);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_blur_out.png", ImageFormat.Png);
```

धुंधला प्रभाव लागू करें और परिणाम सहेजें।

## निष्कर्ष

3डी व्यूपोर्ट में दृश्य प्रभावों के साथ प्रयोग करने से आपके दृश्यों में गहराई और रचनात्मकता आती है। .NET के लिए Aspose.3D इस प्रक्रिया को सरल बनाता है, आपकी परियोजनाओं को उन्नत करने के लिए पोस्ट-प्रोसेसिंग प्रभावों की एक श्रृंखला की पेशकश करता है।

## अक्सर पूछे जाने वाले प्रश्न

### Q1: क्या मैं एक साथ कई प्रभाव लागू कर सकता हूँ?

A1: हां, आप अद्वितीय और जटिल परिणामों के लिए विभिन्न पोस्ट-प्रोसेसिंग प्रभावों को जोड़ सकते हैं।

### Q2: मैं दृश्य प्रभावों की तीव्रता को कैसे समायोजित कर सकता हूं?

A2: प्रत्येक प्रभाव में ऐसे पैरामीटर हो सकते हैं जिन्हें आप इसकी तीव्रता को नियंत्रित करने के लिए बदल सकते हैं। विशिष्ट विवरण के लिए दस्तावेज़ देखें।

### Q3: क्या Aspose.3D गेम डेवलपमेंट के लिए उपयुक्त है?

A3: जबकि Aspose.3D मुख्य रूप से 3D मॉडलिंग और रेंडरिंग के लिए डिज़ाइन किया गया है, इसका उपयोग गेम विकास के कुछ पहलुओं में किया जा सकता है।

### Q4: क्या अतिरिक्त पोस्ट-प्रोसेसिंग प्रभाव उपलब्ध हैं?

A4: Aspose.3D विभिन्न प्रकार के अंतर्निहित पोस्ट-प्रोसेसिंग प्रभाव प्रदान करता है, और आप लाइब्रेरी का उपयोग करके कस्टम प्रभाव बना सकते हैं।

### Q5: क्या मैं व्यावसायिक परियोजनाओं के लिए Aspose.3D का उपयोग कर सकता हूँ?

 A5: हां, आप व्यावसायिक उद्देश्यों के लिए Aspose.3D का उपयोग कर सकते हैं। को देखें[खरीद पृष्ठ](https://purchase.aspose.com/buy) लाइसेंसिंग विवरण के लिए.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
