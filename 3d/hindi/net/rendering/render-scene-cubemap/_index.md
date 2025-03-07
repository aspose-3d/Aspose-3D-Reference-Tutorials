---
title: छह चेहरों के साथ क्यूबमैप में दृश्य प्रस्तुत करना
linktitle: छह चेहरों के साथ क्यूबमैप में दृश्य प्रस्तुत करना
second_title: Aspose.3D .NET API
description: .NET के लिए Aspose.3D के साथ शानदार क्यूबमैप बनाएं। 3डी दृश्यों को आकर्षक छह-मुखी क्यूबमैप में प्रस्तुत करने के लिए हमारी चरण-दर-चरण मार्गदर्शिका का पालन करें।
weight: 14
url: /hi/net/rendering/render-scene-cubemap/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# छह चेहरों के साथ क्यूबमैप में दृश्य प्रस्तुत करना

## परिचय
.NET के लिए Aspose.3D का उपयोग करके किसी दृश्य को छह चेहरों वाले क्यूबमैप में प्रस्तुत करने की इस चरण-दर-चरण मार्गदर्शिका में आपका स्वागत है। इस ट्यूटोरियल में, हम आपको 3डी दृश्य प्रस्तुत करके एक शानदार क्यूबमैप बनाने की प्रक्रिया के बारे में बताएंगे। Aspose.3D एक शक्तिशाली .NET API है जो 3D ग्राफिक्स हेरफेर को सरल बनाता है, और इस गाइड के साथ, आप मनोरम क्यूबमैप बनाने के लिए इसकी क्षमताओं का उपयोग करेंगे।
## आवश्यक शर्तें
इससे पहले कि हम ट्यूटोरियल में उतरें, सुनिश्चित करें कि आपके पास निम्नलिखित आवश्यक शर्तें हैं:
- C# और .NET विकास का कार्यसाधक ज्ञान।
-  .NET के लिए Aspose.3D स्थापित। आप इसे डाउनलोड कर सकते हैं[यहाँ](https://releases.aspose.com/3d/net/).
- रेंडरिंग के लिए GLB प्रारूप में एक 3D दृश्य फ़ाइल (उदाहरण के लिए, "VirtualCity.glb")।
## नामस्थान आयात करें
अपने C# कोड में Aspose.3D के लिए आवश्यक नामस्थान आयात करके प्रारंभ करें:
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
## चरण 1: दृश्य लोड करें
निम्नलिखित कोड का उपयोग करके 3D दृश्य फ़ाइल लोड करें:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## चरण 2: कैमरा और लाइटें बनाएं
दृश्य को रोशन करने के लिए एक कैमरा और दो लाइटें बनाएं:
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light()
{
    Color = new Vector3(Color.CadetBlue)
}).Transform.Translation = new Vector3(49, 0, 49);
```
## चरण 3: रेंडरर और रेंडर लक्ष्य बनाएं
गहराई बनावट के साथ एक रेंडरर और एक क्यूब मैप रेंडर लक्ष्य बनाएं:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
    ITextureCubemap cubemap = rt.Targets[0] as ITextureCubemap;
```
## चरण 4: क्यूबमैप फ़ेस सहेजें
निर्दिष्ट फ़ाइल नामों के साथ क्यूबमैप के प्रत्येक चेहरे को डिस्क पर सहेजें:
```csharp
CubeFaceData<string> fileNames = new CubeFaceData<string>()
{
    Right = "Your Output Directory" + "right.png",
    Left = "Your Output Directory" + "left.png",
    Back = "Your Output Directory" + "back.png",
    Front = "Your Output Directory" + "front.png",
    Bottom = "Your Output Directory" + "bottom.png",
    Top = "Your Output Directory" + "top.png"
};
cubemap.Save(fileNames, ImageFormat.Png);
```
## निष्कर्ष
बधाई हो! आपने .NET के लिए Aspose.3D का उपयोग करके एक 3D दृश्य को सफलतापूर्वक क्यूबमैप में प्रस्तुत किया है। आगे के अनुकूलन विकल्पों का अन्वेषण करें और इस शक्तिशाली एपीआई के साथ अपने 3डी ग्राफ़िक्स प्रोजेक्ट को बेहतर बनाएं।
## अक्सर पूछे जाने वाले प्रश्नों
### प्रश्न: क्या मैं अन्य 3D फ़ाइल स्वरूपों के साथ .NET के लिए Aspose.3D का उपयोग कर सकता हूँ?
हां, Aspose.3D आपके प्रोजेक्ट में लचीलापन प्रदान करते हुए विभिन्न 3D फ़ाइल स्वरूपों का समर्थन करता है।
### प्रश्न: मैं Aspose.3D के लिए समर्थन कैसे प्राप्त कर सकता हूं?
 दौरा करना[Aspose.3D फोरम](https://forum.aspose.com/c/3d/18) सामुदायिक समर्थन और चर्चा के लिए।
### प्रश्न: क्या कोई निःशुल्क परीक्षण उपलब्ध है?
 हाँ, आप नि:शुल्क परीक्षण का उपयोग कर सकते हैं[यहाँ](https://releases.aspose.com/).
### प्रश्न: क्या मैं Aspose.3D का उपयोग करके एनिमेशन के साथ दृश्य प्रस्तुत कर सकता हूँ?
बिल्कुल! Aspose.3D एनिमेटेड 3D दृश्यों को प्रस्तुत करने का समर्थन करता है।
### प्रश्न: मुझे विस्तृत दस्तावेज कहां मिल सकते हैं?
 को देखें[Aspose.3D दस्तावेज़ीकरण](https://reference.aspose.com/3d/net/) गहन जानकारी के लिए.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
