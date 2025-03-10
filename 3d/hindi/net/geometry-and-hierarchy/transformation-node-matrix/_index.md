---
title: ट्रांसफ़ॉर्मेशन मैट्रिक्स द्वारा ट्रांसफ़ॉर्मिंग नोड
linktitle: ट्रांसफ़ॉर्मेशन मैट्रिक्स द्वारा ट्रांसफ़ॉर्मिंग नोड
second_title: Aspose.3D .NET API
description: .NET के लिए Aspose.3D का उपयोग करके नोड्स को 3D दृश्यों में आसानी से रूपांतरित करें। ट्यूटोरियल के साथ चरण-दर-चरण नोड परिवर्तन सीखें।
weight: 21
url: /hi/net/geometry-and-hierarchy/transformation-node-matrix/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# ट्रांसफ़ॉर्मेशन मैट्रिक्स द्वारा ट्रांसफ़ॉर्मिंग नोड

## परिचय

3डी ग्राफ़िक्स और विज़ुअलाइज़ेशन के गतिशील क्षेत्र में, किसी दृश्य के भीतर वस्तुओं में हेरफेर करने की क्षमता एक महत्वपूर्ण पहलू है। .NET के लिए Aspose.3D डेवलपर्स को 3D दृश्यों में रचनात्मकता और नियंत्रण की एक परत जोड़कर, ट्रांसफॉर्मेशन मैट्रिक्स का उपयोग करके नोड्स को निर्बाध रूप से बदलने का अधिकार देता है। यह ट्यूटोरियल चरण दर चरण एक नोड को 3डी दृश्य में बदलने की प्रक्रिया में आपका मार्गदर्शन करेगा।

## आवश्यक शर्तें

ट्यूटोरियल में जाने से पहले, सुनिश्चित करें कि आपके पास निम्नलिखित आवश्यक शर्तें हैं:

1.  .NET लाइब्रेरी के लिए Aspose.3D: सुनिश्चित करें कि आपके .NET प्रोजेक्ट में Aspose.3D लाइब्रेरी स्थापित है। आप इसे डाउनलोड कर सकते हैं[यहाँ](https://releases.aspose.com/3d/net/).

2. विकास परिवेश: एक कार्यशील .NET विकास परिवेश स्थापित करें, और यदि आपने पहले से नहीं किया है, तो एक नया प्रोजेक्ट बनाएं जहां आप परिवर्तनों को कार्यान्वित करेंगे।

## नामस्थान आयात करें

अपने .NET प्रोजेक्ट में आवश्यक नामस्थान आयात करके प्रारंभ करें। ये नामस्थान 3डी दृश्य हेरफेर के लिए आवश्यक कक्षाएं और विधियां प्रदान करते हैं।

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

अब जब हमने मूल बातें कवर कर ली हैं, तो आइए परिवर्तन प्रक्रिया को चरण-दर-चरण मार्गदर्शिका में विभाजित करें।

## चरण 1: दृश्य आरंभ करें

```csharp
// ExStart:AddTransformationToNodeByTransformationMatrix
// दृश्य वस्तु आरंभ करें
Scene scene = new Scene();

```

इस चरण में, हम एक नया खाली 3D दृश्य बनाते हैं।

## चरण 2: जाल बनाएं और दृश्य से जोड़ें

```csharp
// मेश इंस्टेंस सेट करने के लिए पॉलीगॉन बिल्डर विधि का उपयोग करके कॉमन क्लास क्रिएट मेश को कॉल करें
Mesh mesh = (new Box()).ToMesh();

// जाल के लिए एक कंटेनर नोड बनाएं।
Node cubeNode = scene.RootNode.CreateChildNode(mesh);
```

यहां, हम बहुभुज बिल्डर विधि का उपयोग करके एक जाल बनाते हैं और इसे नोड को सौंपते हैं, हमारे घन के लिए ज्यामिति स्थापित करते हैं।

## चरण 3: कस्टम अनुवाद मैट्रिक्स सेट करें

```csharp
// कस्टम अनुवाद मैट्रिक्स सेट करें
cubeNode.Transform.TransformMatrix = new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
);        
```

नोड पर लागू विशिष्ट परिवर्तन को निर्धारित करने के लिए एक कस्टम अनुवाद मैट्रिक्स को परिभाषित करें। अपने वांछित परिवर्तन के लिए मैट्रिक्स मानों को आवश्यकतानुसार समायोजित करें।

दृश्य में क्यूब नोड को शामिल करें, जिससे यह समग्र 3D वातावरण का हिस्सा बन जाए।

## चरण 4: दृश्य सहेजें

```csharp
// दस्तावेज़ निर्देशिका का पथ.
var output = "TransformationToNode.fbx";

// समर्थित फ़ाइल स्वरूपों में 3D दृश्य सहेजें
scene.Save(output);
// ExEnd:AddTransformationToNodeByTransformationMatrix
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

आउटपुट निर्देशिका और फ़ाइल नाम निर्दिष्ट करें, फिर 3D दृश्य को वांछित फ़ाइल स्वरूप में सहेजें। इस उदाहरण में, हम इसे FBX7500ASCII प्रारूप में सहेज रहे हैं।

## निष्कर्ष

बधाई हो! आपने .NET के लिए Aspose.3D के साथ एक 3D दृश्य में ट्रांसफ़ॉर्मेशन मैट्रिक्स का उपयोग करके एक नोड को सफलतापूर्वक रूपांतरित कर दिया है। यह क्षमता विविध और दृष्टि से मनमोहक 3डी अनुप्रयोगों के द्वार खोलती है।

## अक्सर पूछे जाने वाले प्रश्न

### Q1: 3डी ग्राफ़िक्स में ट्रांसफ़ॉर्मेशन मैट्रिक्स क्या है?

ए1: ट्रांसफ़ॉर्मेशन मैट्रिक्स एक गणितीय प्रतिनिधित्व है जिसका उपयोग 3डी स्पेस में वस्तुओं में विभिन्न परिवर्तनों (अनुवाद, रोटेशन, स्केलिंग) को लागू करने के लिए किया जाता है।

### Q2: क्या मैं एक ही नोड में एकाधिक परिवर्तन लागू कर सकता हूँ?

उ2: हां, आप कई परिवर्तनों को उनके संबंधित आव्यूहों को गुणा करके और परिणाम को नोड पर लागू करके जोड़ सकते हैं।

### Q3: क्या 3डी दृश्यों को सहेजने के लिए अन्य समर्थित फ़ाइल प्रारूप हैं?

 A3: .NET के लिए Aspose.3D STL, GLTF, OBJ और अन्य सहित विभिन्न फ़ाइल स्वरूपों का समर्थन करता है। को देखें[प्रलेखन](https://reference.aspose.com/3d/net/) एक व्यापक सूची के लिए.

### Q4: मैं .NET के लिए Aspose.3D के लिए अस्थायी लाइसेंस कैसे प्राप्त कर सकता हूं?

 A4: पर जाएँ[अस्थायी लाइसेंस पृष्ठ](https://purchase.aspose.com/temporary-license/)मूल्यांकन उद्देश्यों के लिए अस्थायी लाइसेंस प्राप्त करने के लिए Aspose वेबसाइट पर जाएं।

### Q5: मैं कहां से सहायता मांग सकता हूं या Aspose.3D समुदाय से जुड़ सकता हूं?

 A5: पर जाएँ[Aspose.3D फोरम](https://forum.aspose.com/c/3d/18) Aspose.3D का उपयोग करके प्रश्न पूछने, अनुभव साझा करने और अन्य डेवलपर्स से जुड़ने के लिए।
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
