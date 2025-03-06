---
title: .NET के लिए Aspose.3D के साथ फिशआई लेंस प्रभाव लागू करना
linktitle: 3डी दृश्य में फिशआई लेंस प्रभाव लागू करना
second_title: Aspose.3D .NET API
description: .NET के लिए Aspose.3D के साथ अपने 3D दृश्यों को बेहतर बनाएं! चरण दर चरण मनमोहक फिशआई लेंस प्रभाव लागू करना सीखें। अब डाउनलोड करो!
weight: 12
url: /hi/net/rendering/fisheye-lens-effect-3d-scene/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# .NET के लिए Aspose.3D के साथ फिशआई लेंस प्रभाव लागू करना

## परिचय
क्या आप अपने 3डी दृश्यों की दृश्य अपील को बढ़ाना चाह रहे हैं? .NET के लिए Aspose.3D के साथ फिशआई लेंस प्रभावों की आकर्षक दुनिया में गोता लगाएँ। यह ट्यूटोरियल आपको अपने 3डी दृश्यों पर फ़िशआई लेंस प्रभाव लागू करने के बारे में चरण दर चरण मार्गदर्शन करेगा, जिससे उन्हें एक अद्वितीय और मनोरम परिप्रेक्ष्य मिलेगा।
## आवश्यक शर्तें
शुरू करने से पहले, सुनिश्चित करें कि आपके पास निम्नलिखित आवश्यक शर्तें हैं:
-  .NET के लिए Aspose.3D: सुनिश्चित करें कि आपके पास .NET के लिए Aspose.3D लाइब्रेरी स्थापित है। यदि नहीं, तो आप इसे डाउनलोड कर सकते हैं[यहाँ](https://releases.aspose.com/3d/net/).
-  नमूना 3डी दृश्य: हम एक नमूना 3डी दृश्य फ़ाइल (वर्चुअलसिटी.जीएलबी) के साथ काम करेंगे। आप अपने स्वयं के दृश्य का उपयोग कर सकते हैं या यहां से नमूना डाउनलोड कर सकते हैं[Aspose.3D दस्तावेज़ीकरण](https://reference.aspose.com/3d/net/).
## नामस्थान आयात करें
अपने .NET प्रोजेक्ट में, Aspose.3D कार्यात्मकताओं तक पहुँचने के लिए आवश्यक नामस्थान शामिल करें। अपने कोड की शुरुआत में निम्नलिखित नामस्थान जोड़ें:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Imaging;
using System.Linq;
using System.Text;
```
## चरण 1: 3डी दृश्य लोड करें
निम्नलिखित कोड का उपयोग करके 3D दृश्य फ़ाइल को अपने प्रोजेक्ट में लोड करें:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## चरण 2: कैमरा और लाइटें सेट करें
अपने दृश्य के दृश्य पहलुओं को बेहतर बनाने के लिए एक कैमरा और रोशनी बनाएं। आवश्यकतानुसार नियरप्लेन, फारप्लेन और रोटेशनमोड जैसे मापदंडों को समायोजित करें:
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light() { Color = new Vector3(Color.CadetBlue) }).Transform.Translation = new Vector3(49, 0, 49);
```
## चरण 3: रेंडरर और रेंडर लक्ष्य बनाएं
रेंडरर सेट करें और क्यूब मैप और 2डी बनावट के लिए रेंडर लक्ष्य बनाएं:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    IRenderTexture final = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(false, 32, 0, 0), 1024, 1024);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
```
## चरण 4: फिशआई लेंस प्रभाव लागू करें
प्रस्तुत क्यूब मानचित्र पर प्रसंस्करण के बाद फिशआई लेंस प्रभाव निष्पादित करें:
```csharp
PostProcessing fisheye = renderer.GetPostProcessing("fisheye");
fisheye.FindProperty("fov").Value = 360.0;
fisheye.Input = rt.Targets[0];
renderer.Execute(fisheye, final);
((ITexture2D)final.Targets[0]).Save("Your Output Directory" + "fisheye.png", ImageFormat.Png);
```
## निष्कर्ष
बधाई हो! आपने .NET के लिए Aspose.3D का उपयोग करके अपने 3D दृश्य में फ़िशआई लेंस प्रभाव सफलतापूर्वक लागू कर दिया है। अपनी रचनात्मकता को उजागर करने के लिए विभिन्न दृश्यों और मापदंडों के साथ प्रयोग करें।
## अक्सर पूछे जाने वाले प्रश्नों
### क्या मैं किसी 3D दृश्य पर फ़िशआई प्रभाव लागू कर सकता हूँ?
हां, आप किसी भी 3डी दृश्य पर फिशआई प्रभाव लागू कर सकते हैं। सुनिश्चित करें कि इष्टतम परिणामों के लिए दृश्य ठीक से लोड और प्रकाशित हो।
### दृश्य क्षेत्र (एफओवी) को 360 डिग्री पर समायोजित करने का क्या महत्व है?
360 डिग्री का दृश्य क्षेत्र एक पूर्ण गोलाकार प्रक्षेपण सुनिश्चित करता है, जिससे एक आश्चर्यजनक फिशआई प्रभाव पैदा होता है।
### मैं अपने 3D दृश्य में प्रकाश व्यवस्था को कैसे अनुकूलित कर सकता हूँ?
आप वांछित प्रकाश प्रभाव प्राप्त करने के लिए रोशनी के गुणों, जैसे स्थिति, प्रकार और रंग को समायोजित कर सकते हैं।
### क्या संसाधित किए जा सकने वाले 3D दृश्य के आकार की कोई सीमा है?
3डी दृश्य का आकार मुख्य रूप से सिस्टम संसाधनों द्वारा सीमित है। सुनिश्चित करें कि आपका हार्डवेयर आपके दृश्य के आकार को संभाल सकता है।
### क्या मैं फिशआई प्रभाव परिणाम के लिए पीएनजी के बजाय एक अलग आउटपुट प्रारूप का उपयोग कर सकता हूं?
हां, आप अपनी आवश्यकताओं के आधार पर आउटपुट को विभिन्न छवि प्रारूपों में सहेजने के लिए कोड को संशोधित कर सकते हैं।
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
