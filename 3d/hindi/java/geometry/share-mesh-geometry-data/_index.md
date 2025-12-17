---
date: 2025-12-12
description: Aspose.3D का उपयोग करके Java 3D में मेष ज्यामिति डेटा साझा करते हुए सामग्री
  का रंग सेट करना और सीन को FBX के रूप में सहेजना सीखें।
linktitle: Set Material Color and Share Mesh Geometry Data in Java 3D with Aspose.3D
second_title: Aspose.3D Java API
title: Aspose.3D के साथ Java 3D में मैटेरियल रंग सेट करें और मेष ज्योमेट्री डेटा साझा
  करें
url: /hi/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java 3D में Aspose.3D के साथ Material Color सेट करें और Mesh Geometry डेटा शेयर करें

## परिचय

Aspose.3D के साथ Java 3D की दुनिया में कदम रखने से आप शानदार विज़ुअलाइज़ेशन और इमर्सिव एक्सपीरियंस बना सकते हैं। इस ट्यूटोरियल में हम आपको **कैसे Mesh Geometry डेटा को शेयर करें** Java 3D में Aspose.3D का उपयोग करके, **कैसे प्रत्येक Mesh इंस्टेंस के लिए Material Color सेट करें** दिखाएंगे। प्रत्येक चरण को ध्यान से फॉलो करें, और अंत में आप कई नोड्स के बीच Mesh डेटा को सहजता से एक्सचेंज कर पाएँगे, रंगों को नियंत्रित करेंगे और FBX में एक्सपोर्ट करेंगे।

## त्वरित उत्तर
- **मुख्य लक्ष्य क्या है?** प्रत्येक नोड के लिए Material Color सेट करना और Mesh Geometry डेटा शेयर करना।  
- **कौन सी लाइब्रेरी आवश्यक है?** Aspose.3D for Java।  
- **परिणाम कैसे एक्सपोर्ट करें?** सीन को FBX फ़ाइल (FBX7400ASCII) के रूप में सेव करें।  
- **क्या लाइसेंस चाहिए?** प्रोडक्शन उपयोग के लिए एक टेम्पररी या फुल लाइसेंस आवश्यक है।  
- **कौन सा Java संस्करण काम करता है?** कोई भी Java 8+ पर्यावरण।

## पूर्वापेक्षाएँ

ट्यूटोरियल शुरू करने से पहले सुनिश्चित करें कि आपके पास निम्नलिखित पूर्वापेक्षाएँ मौजूद हैं:

- Java Development Environment: सुनिश्चित करें कि आपके सिस्टम पर Java डेवलपमेंट एनवायरनमेंट सेटअप है।  
- Aspose.3D Library: Aspose.3D लाइब्रेरी डाउनलोड और इंस्टॉल करें। आप लाइब्रेरी **[यहाँ](https://releases.aspose.com/3d/java/)** पा सकते हैं।

## पैकेज इम्पोर्ट करें

अपने Java प्रोजेक्ट में आवश्यक पैकेज इम्पोर्ट करके शुरू करें। यह चरण Aspose.3D लाइब्रेरी द्वारा प्रदान की गई कार्यक्षमताओं तक पहुँचने के लिए महत्वपूर्ण है।

```java
import com.aspose.threed.*;
```

## चरण 1: Scene ऑब्जेक्ट इनिशियलाइज़ करें (initialize scene java)

प्रक्रिया को शुरू करने के लिए एक Scene ऑब्जेक्ट इनिशियलाइज़ करें। यह वह कैनवास होगा जहाँ हमारा 3D जादू उभरेगा।

```java
// Initialize scene object
Scene scene = new Scene();
```

## चरण 2: Color Vectors परिभाषित करें

इस चरण में हम एक एरे ऑफ़ Color Vectors परिभाषित करेंगे, जिन्हें हमारे 3D सीन के विभिन्न तत्वों पर लागू किया जाएगा।

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## चरण 3: Polygon Builder का उपयोग करके 3D Mesh बनाएं (create 3d mesh java)

Common क्लास का उपयोग करके Polygon Builder मेथड से एक Mesh बनाएं। यह Mesh हमारे 3D एलिमेंट्स की बुनियाद होगी।

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## प्रत्येक नोड के लिए Material Color कैसे सेट करें?

Color Vectors के माध्यम से इटरेट करें, क्यूब नोड्स बनाएं, और Material, **set material color**, तथा ट्रांसलेशन जैसे एट्रिब्यूट सेट करें। यह प्रत्येक Mesh इंस्टेंस की विज़ुअल अपीयरेंस को नियंत्रित करने का मुख्य भाग है।

```java
int idx = 0;
for(Vector3 color : colors) {
    // Initialize cube node object
    Node cube = new Node("cube");
    cube.setEntity(mesh);
    LambertMaterial mat = new LambertMaterial();
    // Set color
    mat.setDiffuseColor(color);
    // Set material
    cube.setMaterial(mat);
    // Set translation
    cube.getTransform().setTranslation(new Vector3(idx++ * 20, 0, 0));
    // Add cube node
    scene.getRootNode().addChildNode(cube);
}
```

## चरण 5: 3D सीन को सेव करें (save scene fbx, convert mesh to fbx)

समर्थित फ़ाइल फ़ॉर्मेट में 3D सीन को सेव करने के लिए डायरेक्टरी और फ़ाइलनाम निर्दिष्ट करें, इस केस में FBX7400ASCII। यह चरण **convert mesh to FBX** को भी दर्शाता है।

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## निष्कर्ष

बधाई हो! आपने सफलतापूर्वक **Material Color सेट किया**, कई नोड्स के बीच Mesh Geometry डेटा शेयर किया, और Aspose.3D for Java का उपयोग करके परिणाम को FBX फ़ाइल के रूप में एक्सपोर्ट किया। यह विज़ुअली आकर्षक और इंटरैक्टिव 3D एप्लिकेशन बनाने के असीम संभावनाओं को खोलता है।

## अक्सर पूछे जाने वाले प्रश्न

### Q1: क्या मैं Aspose.3D को अन्य Java फ्रेमवर्क के साथ उपयोग कर सकता हूँ?

A1: हाँ, Aspose.3D विभिन्न Java फ्रेमवर्क के साथ सहजता से काम करने के लिए डिज़ाइन किया गया है।

### Q2: Aspose.3D के लिए कौन से लाइसेंसिंग विकल्प उपलब्ध हैं?

A2: आप लाइसेंसिंग विकल्प **[यहाँ](https://purchase.aspose.com/buy)** देख सकते हैं।

### Q3: मैं Aspose.3D के लिए सपोर्ट कैसे प्राप्त करूँ?

A3: सपोर्ट और चर्चा के लिए Aspose.3D **[फ़ोरम](https://forum.aspose.com/c/3d/18)** देखें।

### Q4: क्या कोई फ्री ट्रायल उपलब्ध है?

A4: हाँ, आप फ्री ट्रायल **[यहाँ](https://releases.aspose.com/)** प्राप्त कर सकते हैं।

### Q5: Aspose.3D के लिए टेम्पररी लाइसेंस कैसे प्राप्त करें?

A5: आप टेम्पररी लाइसेंस **[यहाँ](https://purchase.aspose.com/temporary-license/)** ले सकते हैं।

## अतिरिक्त अक्सर पूछे जाने वाले प्रश्न

**प्रश्न: क्या मैं सीन को FBX के अलावा अन्य फ़ॉर्मेट में एक्सपोर्ट कर सकता हूँ?**  
उत्तर: हाँ, Aspose.3D OBJ, STL, 3MF आदि को सपोर्ट करता है। केवल `save` कॉल में `FileFormat` एनेम को बदलें।

**प्रश्न: यदि सीन बन जाने के बाद Material बदलना हो तो क्या करें?**  
उत्तर: नोड को रिट्रीव करें, उसके `LambertMaterial` (जैसे `setDiffuseColor`) को मॉडिफ़ाई करें, और सीन को फिर से सेव करें।

**प्रश्न: क्या लाइब्रेरी बड़े Mesh को प्रभावी ढंग से हैंडल करती है?**  
उत्तर: Aspose.3D ऑप्टिमाइज़्ड डेटा स्ट्रक्चर उपयोग करता है; अत्यधिक बड़े Mesh के लिए स्ट्रीमिंग या सीन को स्प्लिट करने पर विचार करें।

**प्रश्न: क्या रंग परिवर्तन को एनीमेट किया जा सकता है?**  
उत्तर: हाँ, आप `AnimationController` API का उपयोग करके Material प्रॉपर्टीज़ को एनीमेट कर सकते हैं।

---

**अंतिम अपडेट:** 2025-12-12  
**टेस्टेड विथ:** Aspose.3D 24.11 for Java  
**लेखक:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}