---
title: प्वाइंट क्लाउड के रूप में PLY प्रारूप में निर्यात करना
linktitle: प्वाइंट क्लाउड के रूप में PLY प्रारूप में निर्यात करना
second_title: Aspose.3D .NET API
description: .NET के लिए Aspose.3D के साथ 3D मॉडलिंग की दुनिया का अन्वेषण करें। मॉडलों को आसानी से PLY प्रारूप में निर्यात करना सीखें। आश्चर्यजनक दृश्यों के साथ अपनी परियोजनाओं को उन्नत करें।
weight: 16
url: /hi/net/loading-and-saving/ply/export-to-ply-point-cloud/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# प्वाइंट क्लाउड के रूप में PLY प्रारूप में निर्यात करना

## परिचय
3डी मॉडलिंग और विकास की गतिशील दुनिया में, .NET के लिए Aspose.3D एक शक्तिशाली टूलकिट के रूप में सामने आता है। यह ट्यूटोरियल आपको .NET के लिए Aspose.3D का उपयोग करके पॉइंट क्लाउड के रूप में PLY प्रारूप में 3D मॉडल निर्यात करने की प्रक्रिया में मार्गदर्शन करेगा। यदि आप आश्चर्यजनक दृश्यों के साथ अपनी परियोजनाओं को बढ़ाने के लिए तैयार हैं, तो आगे बढ़ें और इस बहुमुखी लाइब्रेरी की पूरी क्षमता को अनलॉक करें।
## आवश्यक शर्तें
ट्यूटोरियल में जाने से पहले, सुनिश्चित करें कि आपके पास निम्नलिखित आवश्यक शर्तें हैं:
-  .NET के लिए Aspose.3D: लाइब्रेरी को डाउनलोड और इंस्टॉल करें[डाउनलोड पेज](https://releases.aspose.com/3d/net/).
- विकास परिवेश: अपना पसंदीदा .NET विकास परिवेश सेट करें, जैसे विज़ुअल स्टूडियो।
## नामस्थान आयात करें
.NET के लिए Aspose.3D के साथ आरंभ करने के लिए, अपने प्रोजेक्ट में आवश्यक नेमस्पेस आयात करें:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```
## चरण 1: एक 3D मॉडल बनाएं
एक 3D मॉडल बनाकर शुरुआत करें जिसे आप पॉइंट क्लाउड के रूप में निर्यात करना चाहते हैं। उदाहरण के लिए, आइए एक गोला बनाएं:
```csharp
Sphere sphere = new Sphere();
```
## चरण 2: निर्यात सेटिंग्स परिभाषित करें
फ़ाइल स्वरूप (पीएलवाई) सहित निर्यात सेटिंग्स निर्दिष्ट करें और पॉइंट क्लाउड निर्यात सक्षम करें:
```csharp
PlySaveOptions saveOptions = new PlySaveOptions() { PointCloud = true };
```
## चरण 3: निर्यात पथ सेट करें
वह निर्देशिका निर्धारित करें जहाँ आप निर्यात की गई PLY फ़ाइल को सहेजना चाहते हैं:
```csharp
string exportPath = "Your Document Directory" + "sphere.ply";
```
## चरण 4: एन्कोड और निर्यात करें
 का उपयोग करें`Encode` 3D मॉडल को PLY प्रारूप में निर्यात करने की विधि:
```csharp
FileFormat.PLY.Encode(sphere, exportPath, saveOptions);
```
## निष्कर्ष
बधाई हो! आपने .NET के लिए Aspose.3D का उपयोग करके एक 3D मॉडल को पॉइंट क्लाउड के रूप में PLY प्रारूप में सफलतापूर्वक निर्यात किया है। यह आपके अनुप्रयोगों में गहन दृश्यों को एकीकृत करने की अनंत संभावनाओं को खोलता है।

## पूछे जाने वाले प्रश्न
### 1. क्या Aspose.3D सभी .NET फ्रेमवर्क के साथ संगत है?
Aspose.3D विभिन्न .NET फ्रेमवर्क का समर्थन करता है, जो विकास परिवेशों की एक विस्तृत श्रृंखला में अनुकूलता सुनिश्चित करता है।
### 2. क्या मैं व्यावसायिक परियोजनाओं के लिए Aspose.3D का उपयोग कर सकता हूँ?
 बिल्कुल! Aspose.3D व्यावसायिक उपयोग सहित लचीले लाइसेंसिंग विकल्प प्रदान करता है। इसकी जाँच पड़ताल करो[खरीद पृष्ठ](https://purchase.aspose.com/buy) जानकारी के लिए।
### 3. मैं Aspose.3D के लिए समर्थन कैसे प्राप्त कर सकता हूँ?
 दौरा करना[Aspose.3D फोरम](https://forum.aspose.com/c/3d/18) समुदाय से जुड़ने और विशेषज्ञों से सहायता प्राप्त करने के लिए।
### 4. क्या कोई निःशुल्क परीक्षण उपलब्ध है?
 हां, ए के साथ सुविधाओं का पता लगाएं[मुफ्त परीक्षण](https://releases.aspose.com/) प्रतिबद्धता बनाने से पहले.
### 5. मैं अस्थायी लाइसेंस कैसे प्राप्त करूं?
 अस्थायी लाइसेंसिंग विकल्पों के लिए, पर जाएँ[इस लिंक](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
