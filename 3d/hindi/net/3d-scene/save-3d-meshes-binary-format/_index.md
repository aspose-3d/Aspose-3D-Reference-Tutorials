---
title: कस्टम बाइनरी फॉर्मेट में 3डी मेश को सेव करना
linktitle: कस्टम बाइनरी फॉर्मेट में 3डी मेश को सेव करना
second_title: Aspose.3D .NET API
description: .NET के लिए Aspose.3D के साथ 3D की दुनिया का अन्वेषण करें। मेश को कस्टम बाइनरी फॉर्मेट में सहेजना सीखें।
type: docs
weight: 13
url: /hi/net/3d-scene/save-3d-meshes-binary-format/
---
## परिचय

.NET के लिए Aspose.3D की दुनिया में आपका स्वागत है, एक शक्तिशाली लाइब्रेरी जो डेवलपर्स को 3D फ़ाइलों के साथ सहजता से काम करने में सक्षम बनाती है। इस ट्यूटोरियल में, हम .NET के लिए Aspose.3D का उपयोग करके कस्टम बाइनरी प्रारूप में 3D मेश को सहेजने की प्रक्रिया के बारे में विस्तार से जानेंगे। यह मार्गदर्शिका मानती है कि आपको C# की बुनियादी समझ है और आप Aspose.3D लाइब्रेरी से परिचित हैं।

## आवश्यक शर्तें

इससे पहले कि हम ट्यूटोरियल में आगे बढ़ें, सुनिश्चित करें कि आपके पास निम्नलिखित जगहें हैं:

-  .NET के लिए Aspose.3D: सुनिश्चित करें कि आपके पास Aspose.3D लाइब्रेरी स्थापित है। आप इसे यहां से डाउनलोड कर सकते हैं[यहाँ](https://releases.aspose.com/3d/net/).

- विकास परिवेश: अपना पसंदीदा C# विकास परिवेश सेट करें, जैसे विज़ुअल स्टूडियो।

- इनपुट 3डी फ़ाइल: एक 3डी फ़ाइल (उदाहरण के लिए, test.fbx) रखें जिसे आप एक कस्टम बाइनरी प्रारूप में परिवर्तित करना चाहते हैं।

## नामस्थान आयात करें

अपने C# कोड में, Aspose.3D कार्यात्मकताओं तक पहुँचने के लिए आवश्यक नामस्थान शामिल करें:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
```

## चरण 1: एक 3डी फ़ाइल लोड करें

Aspose.3D का उपयोग करके अपनी 3D फ़ाइल लोड करें। इस उदाहरण में, हम "test.fbx" नामक एक फ़ाइल लोड करते हैं:

```csharp
Scene scene = Scene.FromFile("test.fbx");
```

## चरण 2: कस्टम बाइनरी प्रारूप को परिभाषित करें

उस कस्टम बाइनरी प्रारूप की संरचना को परिभाषित करें जिसमें आप अपने 3डी मेश को सहेजना चाहते हैं। उदाहरण घटकों के रूप में मेशब्लॉक, वर्टेक्स और ट्राएंगल के साथ एक संरचना का उपयोग करता है।

```csharp
// एक वर्टेक्स का मेमोरी लेआउट है
// फ्लोट[3] स्थिति;
// फ्लोट[3] सामान्य;
// फ्लोट[3] यूवी;
var vertexDeclaration = new VertexDeclaration();
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Position);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Normal);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.UV);

```

## चरण 3: लिखने के लिए फ़ाइल खोलें

लिखने के लिए एक बाइनरी फ़ाइल खोलें, जहाँ परिवर्तित 3D मेश सहेजे जाएंगे:

```csharp
using (var writer = new BinaryWriter(new FileStream("Your Output Directory" + "Save3DMeshesInCustomBinaryFormat_out", FileMode.Create, FileAccess.Write)))
```

## चरण 4: नोड्स और इकाइयों के माध्यम से पुनरावृति करें

3डी दृश्य में प्रत्येक नोड पर जाएं और मेश इकाइयों को कस्टम बाइनरी प्रारूप में परिवर्तित करें। रोशनी, कैमरे और अन्य गैर-जाल इकाइयों पर ध्यान न दें:

```csharp
scene.RootNode.Accept(delegate(Node node)
{
    foreach (Entity entity in node.Entities)
    {
        if (!(entity is IMeshConvertible))
            continue;
        // ... (प्रसंस्करण जारी रखें)
    }
    return true;
});
```

## चरण 5: नियंत्रण बिंदुओं और त्रिभुजों को रूपांतरित करें और लिखें

प्रत्येक जाल इकाई के लिए, नियंत्रण बिंदुओं को विश्व स्थान में परिवर्तित करें और उन्हें त्रिकोण सूचकांकों के साथ बाइनरी फ़ाइल में लिखें:

```csharp
Mesh m = ((IMeshConvertible)entity).ToMesh();

var triMesh = TriMesh.FromMesh(vertexDeclaration, m);


//जाल का मेमोरी लेआउट है:
// फ्लोट[16] ट्रांसफॉर्म_मैट्रिक्स;
// int vertices_count;
// intindices_count;
// शीर्ष[vertices_count] शीर्ष;
// यूशॉर्ट[indices_count] सूचकांक;


//परिवर्तन लिखें
var transform = node.GlobalTransform.TransformMatrix.ToArray();
for(int i = 0; i < transform.Length; i++)
    writer.Write((float)transform[i]);
//शीर्षों/सूचकांकों की संख्या लिखें
writer.Write(triMesh.VerticesCount);
writer.Write(triMesh.IndicesCount);
//शीर्ष और सूचकांक लिखें
writer.Flush();
triMesh.WriteVerticesTo(writer.BaseStream);
triMesh.Write16bIndicesTo(writer.BaseStream);

```

## निष्कर्ष

इस ट्यूटोरियल में, हमने .NET के लिए Aspose.3D का उपयोग करके कस्टम बाइनरी प्रारूप में 3D मेश को सहेजने की प्रक्रिया को कवर किया। यह शक्तिशाली लाइब्रेरी डेवलपर्स को 3D फ़ाइलों में निर्बाध रूप से हेरफेर करने के लिए आवश्यक उपकरण प्रदान करती है। अपनी परियोजनाओं में Aspose.3D की पूरी क्षमता को अनलॉक करने के लिए विभिन्न प्रारूपों और सेटिंग्स के साथ प्रयोग करें।

## पूछे जाने वाले प्रश्न

### Q1: क्या मैं अन्य प्रोग्रामिंग भाषाओं के साथ .NET के लिए Aspose.3D का उपयोग कर सकता हूँ?

A1: Aspose.3D मुख्य रूप से .NET भाषाओं का समर्थन करता है, लेकिन आप अन्य भाषाओं के लिए संगतता विकल्प तलाश सकते हैं।

### Q2: मुझे अतिरिक्त उदाहरण और संसाधन कहां मिल सकते हैं?

 ए2: द[Aspose.3D फोरम](https://forum.aspose.com/c/3d/18)समर्थन, उदाहरण ढूंढने और समुदाय के साथ जुड़ने के लिए एक बेहतरीन जगह है।

### Q3: क्या Aspose.3D के लिए कोई परीक्षण संस्करण उपलब्ध है?

 उ3: हाँ, आप नि:शुल्क परीक्षण प्राप्त कर सकते हैं[यहाँ](https://releases.aspose.com/).

### Q4: मैं Aspose.3D के लिए अस्थायी लाइसेंस कैसे प्राप्त करूं?

 ए4: विजिट करें[इस लिंक](https://purchase.aspose.com/temporary-license/) परीक्षण उद्देश्यों के लिए अस्थायी लाइसेंस प्राप्त करना।

### Q5: क्या मैं .NET के लिए Aspose.3D खरीद सकता हूँ?

 A5: हां, आप Aspose.3D यहां से खरीद सकते हैं[खरीद पृष्ठ](https://purchase.aspose.com/buy).