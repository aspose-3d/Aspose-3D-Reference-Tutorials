---
date: 2026-05-24
description: Aspose.3D for Java का उपयोग करके स्लाइस के साथ 3D एक्सट्रूज़न कैसे बनाएं,
  सीखें। यह चरण‑दर‑चरण गाइड रैखिक एक्सट्रूज़न, गोलाई त्रिज्या सेट करना, और OBJ निर्यात
  को कवर करता है।
keywords:
- create 3d extrusion java
- Aspose 3D slices
- linear extrusion Java
linktitle: स्लाइस के साथ 3D एक्सट्रूज़न बनाएं – Aspose.3D for Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  headline: Create 3D Extrusion with Slices – Aspose.3D for Java
  type: TechArticle
- description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  name: Create 3D Extrusion with Slices – Aspose.3D for Java
  steps:
  - name: Set up the scene and define the profile
    text: '`RectangleShape` is a class that defines a 2‑D rectangle profile. First
      we create a `RectangleShape` and give it a **rounding radius** so the corners
      are smooth. `Scene` is the root container for all nodes and geometry. Then we
      initialise a new `Scene` that will hold all geometry.'
  - name: Create child node objects for each extrusion
    text: '`Node` represents an element in the scene graph that can hold geometry
      and transformations. Every piece of geometry lives under a `Node`. Here we generate
      two sibling nodes – one for a low‑slice extrusion and another for a high‑slice
      extrusion – and move the left node a little to the side so the res'
  - name: Perform linear extrusion and set slices
    text: '`LinearExtrusion` is the class that creates a solid by sweeping a profile
      linearly. `LinearExtrusion` is Aspose.3D''s class that generates a solid by
      extruding a 2‑D profile along a straight line. Using an **anonymous inner class**
      we call `setSlices` to control the smoothness. The left node gets onl'
  - name: Export OBJ – save the scene
    text: Finally we write the scene to a Wavefront OBJ file, a format widely supported
      by 3‑D editors and game engines. This demonstrates the **export OBJ Java** capability
      of Aspose.3D.
  type: HowTo
- questions:
  - answer: You can download the library [here](https://releases.aspose.com/3d/java/).
    question: How can I download Aspose.3D for Java?
  - answer: Refer to the documentation [here](https://reference.aspose.com/3d/java/).
    question: Where can I find the documentation for Aspose.3D?
  - answer: Yes, you can explore a free trial [here](https://releases.aspose.com/).
    question: Is there a free trial available?
  - answer: Visit the support forum [here](https://forum.aspose.com/c/3d/18).
    question: How can I get support for Aspose.3D?
  - answer: Yes, a temporary license can be obtained [here](https://purchase.aspose.com/temporary-license/).
    question: Can I purchase a temporary license?
  type: FAQPage
second_title: Aspose.3D Java API
title: स्लाइस के साथ 3D एक्सट्रूज़न बनाएं – Aspose.3D for Java
url: /hi/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D एक्सट्रूज़न को स्लाइस के साथ बनाएं – Aspose.3D for Java

## परिचय

यदि आपको **create 3d extrusion** ऑब्जेक्ट्स चाहिए जो स्मूद और सटीक दिखें, तो स्लाइस की संख्या को नियंत्रित करना मुख्य है। इस ट्यूटोरियल में हम Aspose.3D for Java के साथ लीनियर एक्सट्रूज़न करते समय स्लाइस कैसे निर्दिष्ट करें, यह देखेंगे। आप देखेंगे कि स्लाइस काउंट क्यों महत्वपूर्ण है, राउंडिंग रेडियस कैसे सेट करें, और परिणाम को OBJ फ़ाइल के रूप में कैसे एक्सपोर्ट करें जिसे किसी भी 3‑D पाइपलाइन में उपयोग किया जा सकता है।

## त्वरित उत्तर

- **“slices” क्या नियंत्रित करता है?** एक्सट्रूज़न सतह का अनुमान लगाने के लिए उपयोग किए जाने वाले मध्यवर्ती क्रॉस‑सेक्शन की संख्या।  
- **कौन सा मेथड स्लाइस काउंट सेट करता है?** `LinearExtrusion.setSlices(int)`  
- **क्या मैं प्रोफ़ाइल का राउंडिंग रेडियस बदल सकता हूँ?** हाँ, `RectangleShape.setRoundingRadius(double)` के माध्यम से  
- **इस उदाहरण में कौन सा फ़ाइल फ़ॉर्मेट उपयोग किया गया है?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **कोड चलाने के लिए क्या लाइसेंस चाहिए?** मूल्यांकन के लिए एक फ्री ट्रायल काम करता है; उत्पादन के लिए एक कमर्शियल लाइसेंस आवश्यक है।

`LinearExtrusion.setSlices(int)` निर्धारित करता है कि एक्सट्रूज़न कितने मध्यवर्ती स्लाइस उत्पन्न करेगा।  
`RectangleShape.setRoundingRadius(double)` एक आयताकार प्रोफ़ाइल के कोने के रेडियस को परिभाषित करता है।

## स्लाइस के साथ 3d extrusion java कैसे बनाएं?

अपने 2‑D प्रोफ़ाइल को लोड करें, स्लाइस काउंट चुनें, राउंडिंग रेडियस सेट करें, और `save` कॉल करें – पूरा वर्कफ़्लो कुछ ही लाइनों में फिट हो जाता है। Aspose.3D for Java जियोमेट्री निर्माण, स्लाइस इंटरपोलेशन, और OBJ एक्सपोर्ट को स्वचालित रूप से संभालता है, ताकि आप लो‑लेवल मेष गणनाओं के बजाय विज़ुअल क्वालिटी पर ध्यान केंद्रित कर सकें।

## स्लाइस के साथ लीनियर एक्सट्रूज़न क्या है?

स्लाइस के साथ लीनियर एक्सट्रूज़न एक सपाट 2‑D आकार को एक सीधी रेखा के साथ स्वेप करके 3‑D ठोस में बदल देता है, जबकि कॉन्फ़िगर करने योग्य संख्या में मध्यवर्ती क्रॉस‑सेक्शन उत्पन्न करता है। स्लाइस काउंट सीधे यह प्रभावित करता है कि गोल कोनों जैसी वक्र किनारें कितनी स्मूद रेंडर होती हैं।

## 3d एक्सट्रूज़न बनाने के लिए Aspose.3D for Java का उपयोग क्यों करें?

Aspose.3D हर एक्सट्रूज़न पैरामीटर पर **पूर्ण प्रोग्रामेटिक नियंत्रण** प्रदान करता है, **50+ इनपुट और आउटपुट फ़ॉर्मेट** (OBJ, FBX, STL, और GLTF सहित) को सपोर्ट करता है, और **सैकड़ों‑पेज मॉडल** को पूरी फ़ाइल को मेमोरी में लोड किए बिना प्रोसेस कर सकता है। यह किसी भी Java‑सक्षम प्लेटफ़ॉर्म पर चलता है, कोई नेटिव DLL आवश्यक नहीं है, और Windows, Linux, और macOS में निर्धारक परिणाम सुनिश्चित करता है।

## पूर्वापेक्षाएँ

1. **Java Development Kit** – JDK 8 या उससे ऊपर स्थापित हो।  
2. **Aspose.3D for Java** – आधिकारिक साइट से लाइब्रेरी डाउनलोड करें [here](https://releases.aspose.com/3d/java/).  
3. आपका पसंदीदा IDE या टेक्स्ट एडिटर।

## पैकेज इम्पोर्ट करें

Aspose.3D नेमस्पेस को अपने प्रोजेक्ट में जोड़ें ताकि आप 3‑D मॉडलिंग क्लासेज़ तक पहुंच सकें।

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## स्टेप‑बाय‑स्टेप गाइड

### स्टेप 1: सीन सेट अप करें और प्रोफ़ाइल परिभाषित करें

`RectangleShape` एक क्लास है जो 2‑D आयताकार प्रोफ़ाइल को परिभाषित करती है।  
पहले हम एक `RectangleShape` बनाते हैं और उसे **rounding radius** देते हैं ताकि कोने स्मूद हों।  
`Scene` सभी नोड्स और जियोमेट्री के लिए रूट कंटेनर है।  
फिर हम एक नया `Scene` इनिशियलाइज़ करते हैं जो सभी जियोमेट्री को रखेगा।

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### स्टेप 2: प्रत्येक एक्सट्रूज़न के लिए चाइल्ड नोड ऑब्जेक्ट बनाएं

`Node` सीन ग्राफ में एक तत्व को दर्शाता है जो जियोमेट्री और ट्रांसफ़ॉर्मेशन रख सकता है।  
जियोमेट्री का हर टुकड़ा एक `Node` के अंतर्गत रहता है। यहाँ हम दो सिब्लिंग नोड्स बनाते हैं – एक लो‑स्लाइस एक्सट्रूज़न के लिए और दूसरा हाई‑स्लाइस एक्सट्रूज़न के लिए – और बाएँ नोड को थोड़ा साइड में ले जाते हैं ताकि परिणामों की तुलना आसान हो।

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### स्टेप 3: लीनियर एक्सट्रूज़न करें और स्लाइस सेट करें

`LinearExtrusion` वह क्लास है जो प्रोफ़ाइल को रैखिक रूप से स्वेप करके एक ठोस बनाता है।  
`LinearExtrusion` Aspose.3D की क्लास है जो 2‑D प्रोफ़ाइल को सीधी रेखा के साथ एक्सट्रूड करके ठोस उत्पन्न करती है। एक **anonymous inner class** का उपयोग करके हम `setSlices` कॉल करते हैं ताकि स्मूदनेस नियंत्रित हो सके। बाएँ नोड को केवल 2 स्लाइस मिलते हैं (खुरदुरा), जबकि दाएँ नोड को 10 स्लाइस मिलते हैं (स्मूद)।

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### स्टेप 4: OBJ एक्सपोर्ट करें – सीन को सेव करें

अंत में हम सीन को एक Wavefront OBJ फ़ाइल में लिखते हैं, जो फ़ॉर्मेट 3‑D एडिटर्स और गेम इंजिन्स द्वारा व्यापक रूप से सपोर्टेड है। यह Aspose.3D की **export OBJ Java** क्षमता को दर्शाता है।

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## सामान्य समस्याएँ और समाधान

| Issue | Why it Happens | Fix |
|-------|----------------|-----|
| **Extrusion सपाट दिखता है** | स्लाइस काउंट 1 या 0 सेट किया गया है | सुनिश्चित करें कि `setSlices` को मान ≥ 2 के साथ कॉल किया गया है। |
| **Rounded corners खुरदुरे दिखते हैं** | राउंडिंग रेडियस स्लाइस काउंट की तुलना में बहुत छोटा है | स्मूद कर्व्स के लिए या तो रेडियस बढ़ाएँ या स्लाइस काउंट बढ़ाएँ। |
| **सेव पर फ़ाइल नहीं मिली** | `MyDir` एक गैर‑मौजूद फ़ोल्डर की ओर इशारा करता है | डायरेक्टरी को पहले बनाएं या एक एब्सोल्यूट पाथ उपयोग करें। |

## अक्सर पूछे जाने वाले प्रश्न

**Q: मैं Aspose.3D for Java कैसे डाउनलोड कर सकता हूँ?**  
A: आप लाइब्रेरी [here](https://releases.aspose.com/3d/java/) से डाउनलोड कर सकते हैं।

**Q: Aspose.3D की डॉक्यूमेंटेशन कहाँ मिल सकती है?**  
A: डॉक्यूमेंटेशन के लिए [here](https://reference.aspose.com/3d/java/) देखें।

**Q: क्या कोई फ्री ट्रायल उपलब्ध है?**  
A: हाँ, आप एक फ्री ट्रायल [here](https://releases.aspose.com/) का उपयोग कर सकते हैं।

**Q: मैं Aspose.3D के लिए सपोर्ट कैसे प्राप्त कर सकता हूँ?**  
A: सपोर्ट फ़ोरम [here](https://forum.aspose.com/c/3d/18) पर जाएँ।

**Q: क्या मैं एक टेम्पररी लाइसेंस खरीद सकता हूँ?**  
A: हाँ, एक टेम्पररी लाइसेंस [here](https://purchase.aspose.com/temporary-license/) से प्राप्त किया जा सकता है।

---

**अंतिम अपडेट:** 2026-05-24  
**परीक्षण किया गया:** Aspose.3D for Java 24.11 (latest at time of writing)  
**लेखक:** Aspose

## संबंधित ट्यूटोरियल

- [Aspose.3D के साथ 3D एक्सट्रूज़न जावा बनाएं](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Aspose.3D for Java के साथ लीनियर एक्सट्रूज़न में दिशा कैसे सेट करें](/3d/java/linear-extrusion/setting-direction/)
- [Aspose.3D for Java में लीनियर एक्सट्रूज़न के साथ ट्विस्ट के साथ 3D सीन बनाएं](/3d/java/linear-extrusion/applying-twist/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}