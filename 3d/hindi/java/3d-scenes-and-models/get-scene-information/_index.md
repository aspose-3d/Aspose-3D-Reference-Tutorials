---
date: 2026-09-08
description: Aspose.3D का उपयोग करके Java में यूनिट्स को परिभाषित करने और सीन को FBX
  में निर्यात करने का तरीका सीखें। यह चरण‑दर‑चरण गाइड application name सेट करने, measurement
  units, और 3D सीन जानकारी प्राप्त करने को दर्शाता है।
keywords:
- how to define units
- export scene to fbx
- how to set application name
- define measurement units
lastmod: 2026-09-08
linktitle: Java में FBX को सहेजने और 3D सीन जानकारी प्राप्त करने का तरीका
og_description: Aspose.3D के साथ Java में यूनिट्स को परिभाषित करने और सीन को FBX में
  निर्यात करने का तरीका सीखें। गाइड में application name सेट करना, measurement units,
  और कुछ चरणों में 3D सीन जानकारी प्राप्त करना शामिल है।
og_image_alt: Guide showing how to define units and export a 3D scene to FBX using
  Aspose.3D Java
og_title: Java में यूनिट्स को परिभाषित करने और सीन को FBX में निर्यात करने का तरीका
schemas:
- author: Aspose
  dateModified: '2026-09-08'
  description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  headline: How to define units and export scene to FBX in Java
  type: TechArticle
- description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  name: How to define units and export scene to FBX in Java
  steps:
  - name: initialize a 3D scene
    text: The `Scene` class is Aspose.3D's top‑level container that represents an
      entire 3D scene, including geometry, lights, cameras, and metadata. First, create
      an empty `Scene` object. This will be the container for all geometry, lights,
      cameras, and asset metadata.
  - name: define measurement units
    text: The unit system determines the real‑world scale of the scene; Aspose.3D
      lets you specify a unit name and a scale factor relative to meters. In this
      example we use an ancient Egyptian unit called “pole” with a custom scale factor.
      > **Tip:** Adjust `unitScaleFactor` to match the real‑world size of yo
  - name: export scene to FBX
    text: Now that the asset information is attached, we save the scene as an FBX
      file. The `FileFormat.FBX7500ASCII` option produces a human‑readable ASCII FBX,
      which is handy for debugging. > **Remember:** Replace `"Your Document Directory"`
      with an absolute path or a path relative to your project's working
  type: HowTo
- questions:
  - answer: Replace `FileFormat.FBX7500ASCII` with `FileFormat.FBX7500` when calling
      `scene.save(...)`.
    question: How do I change the output format to binary FBX?
  - answer: Yes, use `scene.getUserData().add("Key", "Value")` to embed additional
      key‑value pairs.
    question: Can I add custom user‑defined metadata beyond the built‑in asset fields?
  - answer: It does. Simply change the `FileFormat` enum to `OBJ` or `GLTF2` as needed.
    question: Does Aspose.3D support other export formats like OBJ or GLTF?
  - answer: Aspose.3D for Java supports Java 8 and later.
    question: What version of Java is required?
  - answer: Absolutely. Load the file with `new Scene("input.fbx")`, modify `scene.getAssetInfo()`,
      then save.
    question: Is it possible to load an existing FBX, modify its asset info, and resave?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- export scene to fbx
- Aspose.3D
- Java 3D
- define units
- 3D asset metadata
title: Java में यूनिट्स को परिभाषित करने और सीन को FBX में निर्यात करने का तरीका
url: /hi/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# जावा में यूनिट्स को परिभाषित करने और सीन को FBX में निर्यात करने का तरीका

## परिचय

यदि आप अपने 3D सीन से उपयोगी मेटाडेटा निकालते हुए **यूनिट्स को परिभाषित करने** और **सीन को FBX में निर्यात करने** के लिए एक स्पष्ट, व्यावहारिक मार्गदर्शिका की तलाश में हैं, तो आप सही जगह पर आए हैं। इस ट्यूटोरियल में हम **Aspose.3D for Java** लाइब्रेरी का उपयोग करके हर चरण को विस्तार से देखेंगे: सीन बनाना, **एप्लिकेशन नाम सेट करना**, **मापन इकाइयों को परिभाषित करना**, और अंत में **सीन को FBX में निर्यात करना**। अंत तक आपके पास एक तैयार‑उपयोगी FBX फ़ाइल होगी जिसमें वह एसेट जानकारी होगी जिसकी आपको डाउनस्ट्रीम पाइपलाइन के लिए आवश्यकता होगी।

## त्वरित उत्तर

- **मुख्य लक्ष्य क्या है?** एक कस्टम एसेट जानकारी वाले सीन को FBX में निर्यात करना।  
- **कौन सी लाइब्रेरी उपयोग की गई है?** Aspose.3D for Java।  
- **क्या मुझे लाइसेंस की आवश्यकता है?** विकास के लिए एक मुफ्त ट्रायल काम करता है; उत्पादन के लिए एक व्यावसायिक लाइसेंस आवश्यक है।  
- **क्या मैं मापन इकाइयों को बदल सकता हूँ?** हाँ – `setUnitName` और `setUnitScaleFactor` का उपयोग करें।  
- **आउटपुट कहाँ सहेजा जाता है?** `scene.save(...)` में आप जो पाथ निर्दिष्ट करते हैं, वहाँ।

## पूर्वापेक्षाएँ

शुरू करने से पहले, सुनिश्चित करें कि आपके पास है:

- कोर जावा सिंटैक्स की ठोस समझ।  
- **Aspose.3D for Java** डाउनलोड किया हुआ और आपके प्रोजेक्ट में जोड़ा हुआ (आप इसे आधिकारिक से प्राप्त कर सकते हैं) [Aspose 3D download page](https://releases.aspose.com/3d/java/)।  
- आपका पसंदीदा जावा IDE (IntelliJ IDEA, Eclipse, NetBeans, आदि) सही ढंग से कॉन्फ़िगर किया हुआ।

## पैकेज इम्पोर्ट करें

अपने जावा स्रोत फ़ाइल में, Aspose.3D क्लासेज़ को इम्पोर्ट करें जो सीन हैंडलिंग और फ़ाइल‑फ़ॉर्मेट समर्थन प्रदान करती हैं।

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Pro tip:** इम्पोर्ट सूची को न्यूनतम रखें ताकि अनावश्यक निर्भरताओं से बचा जा सके और कंपाइल टाइम सुधार सके।

## FBX फ़ाइल को सहेजने की प्रक्रिया क्या है?

एक सीन को FBX फ़ाइल के रूप में सहेजने के लिए आप एक `Scene` बनाते हैं, इच्छित एसेट मेटाडेटा सेट करते हैं, मापन इकाई को परिभाषित करते हैं, और फिर `scene.save(path, FileFormat.FBX7500ASCII)` को कॉल करते हैं। यह क्रम ज्योमेट्री, मैटेरियल्स, और मेटाडेटा को एक ASCII FBX में लिखता है जिसे डाउनस्ट्रीम टूल्स द्वारा निरीक्षण या इम्पोर्ट किया जा सकता है।

### चरण 1: 3D सीन को इनिशियलाइज़ करें

`Scene` क्लास Aspose.3D का टॉप‑लेवल कंटेनर है जो पूरे 3D सीन का प्रतिनिधित्व करता है, जिसमें ज्योमेट्री, लाइट्स, कैमरा, और मेटाडेटा शामिल हैं। पहले, एक खाली `Scene` ऑब्जेक्ट बनाएं। यह सभी ज्योमेट्री, लाइट्स, कैमरा, और एसेट मेटाडेटा का कंटेनर होगा।

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### जावा में एप्लिकेशन नाम कैसे सेट करें

`AssetInfo` ऑब्जेक्ट सीन के लिए एप्लिकेशन नाम, विक्रेता, और संस्करण जैसी मेटाडेटा संग्रहीत करता है। कस्टम मेटाडेटा जोड़ने से डाउनस्ट्रीम टूल्स को फ़ाइल के स्रोत की पहचान करने में मदद मिलती है। फ़ाइल को सहेजने से पहले `AssetInfo` ऑब्जेक्ट का उपयोग करके **एप्लिकेशन नाम सेट करें** (और विक्रेता)।

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Why this matters:** कई पाइपलाइन मूल एप्लिकेशन के आधार पर एसेट्स को फ़िल्टर या टैग करती हैं, जिससे यह चरण बड़े प्रोजेक्ट्स के लिए आवश्यक बन जाता है।

### चरण 3: मापन इकाइयों को परिभाषित करें

यूनिट सिस्टम सीन के वास्तविक दुनिया के स्केल को निर्धारित करता है; Aspose.3D आपको मीटर के सापेक्ष एक यूनिट नाम और स्केल फ़ैक्टर निर्दिष्ट करने देता है। इस उदाहरण में हम एक प्राचीन मिस्री इकाई “pole” का उपयोग करते हैं जिसमें एक कस्टम स्केल फ़ैक्टर है।

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Tip:** `unitScaleFactor` को अपने मॉडल के वास्तविक आकार से मेल खाने के लिए समायोजित करें; 1.0 चुनी गई इकाई के साथ 1‑to‑1 मैपिंग दर्शाता है।

### चरण 4: सीन को FBX में निर्यात करें

अब जब एसेट जानकारी जुड़ गई है, हम सीन को FBX फ़ाइल के रूप में सहेजते हैं। `FileFormat.FBX7500ASCII` विकल्प एक मानव‑पठनीय ASCII FBX उत्पन्न करता है, जो डिबगिंग के लिए उपयोगी है।

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
// ExEnd:AddAssetInformationToScene
```

> **Remember:** `"Your Document Directory"` को एक पूर्ण पाथ या आपके प्रोजेक्ट की कार्यशील डायरेक्टरी के सापेक्ष पाथ से बदलें।

## Aspose.3D के साथ सीन को FBX में निर्यात क्यों करें?

Aspose.3D **50+ इनपुट और आउटपुट फ़ॉर्मेट** को समर्थन देता है और पूरी फ़ाइल को मेमोरी में लोड किए बिना कई सौ पृष्ठों वाले सीन को प्रोसेस कर सकता है, जिससे आपको निर्यातित फ़ाइल—मेटाडेटा, यूनिट्स, और ज्योमेट्री—पर पूर्ण नियंत्रण मिलता है, बिना किसी भारी 3D ऑथरिंग एप्लिकेशन की आवश्यकता के। यह स्वचालित एसेट जेनरेशन, बैच प्रोसेसिंग, और सर्वर‑साइड कन्वर्ज़न को तेज़ और विश्वसनीय बनाता है।

## सामान्य उपयोग केस

- **Game asset pipelines** – संस्करण ट्रैकिंग के लिए निर्माता जानकारी को सीधे FBX फ़ाइलों में एम्बेड करें।  
- **Architectural visualization** – रेंडरिंग इंजन में इम्पोर्ट करते समय स्केलिंग त्रुटियों से बचने के लिए प्रोजेक्ट‑विशिष्ट यूनिट्स को संग्रहीत करें।  
- **Automated reporting** – मेटाडेटा के साथ ऑन‑द‑फ्लाई FBX फ़ाइलें जनरेट करें जिन्हें डाउनस्ट्रीम एनालिटिक्स टूल पढ़ सकते हैं।  
- **Cloud‑based 3D services** – प्रोग्रामेटिकली सीन बनाएं और निर्यात करें बिना GUI के, SaaS प्लेटफ़ॉर्म के लिए उपयुक्त।

## समस्या निवारण और टिप्स

| Issue | Solution |
|-------|----------|
| **सेव के बाद फ़ाइल नहीं मिली** | जाँचें कि `MyDir` एक मौजूदा फ़ोल्डर की ओर इशारा कर रहा है और आपके एप्लिकेशन के पास लिखने की अनुमति है। |
| **बाहरी व्यूअर में यूनिट्स गलत दिख रहे हैं** | `unitScaleFactor` को दोबारा जांचें; कुछ व्यूअर बेस यूनिट के रूप में मीटर की अपेक्षा करते हैं। |
| **एसेट मेटाडेटा गायब है** | सुनिश्चित करें कि आप `scene.getAssetInfo()` **सेव से पहले** कॉल करें; `save()` के बाद किए गए परिवर्तन सहेजे नहीं जाएंगे। |
| **बड़े सीन पर प्रदर्शन बाधा** | मेमोरी उपयोग कम करने के लिए सेव से पहले `scene.optimize()` का उपयोग करें। |
| **ASCII FBX बहुत बड़ा है** | `FileFormat.FBX7500` का उपयोग करके बाइनरी FBX में स्विच करें (FAQ देखें)। |

## अक्सर पूछे जाने वाले प्रश्न

**Q: आउटपुट फ़ॉर्मेट को बाइनरी FBX में कैसे बदलें?**  
A: `scene.save(...)` कॉल करते समय `FileFormat.FBX7500ASCII` को `FileFormat.FBX7500` से बदलें।

**Q: बिल्ट‑इन एसेट फ़ील्ड्स के अलावा कस्टम यूज़र‑डिफाइंड मेटाडेटा जोड़ सकता हूँ?**  
A: हाँ, अतिरिक्त की‑वैल्यू जोड़े को एम्बेड करने के लिए `scene.getUserData().add("Key", "Value")` का उपयोग करें।

**Q: क्या Aspose.3D OBJ या GLTF जैसे अन्य एक्सपोर्ट फ़ॉर्मेट्स को सपोर्ट करता है?**  
A: हां। बस आवश्यकतानुसार `FileFormat` एनोम को `OBJ` या `GLTF2` में बदलें।

**Q: जावा का कौन सा संस्करण आवश्यक है?**  
A: Aspose.3D for Java, Java 8 और उसके बाद के संस्करणों को सपोर्ट करता है।

**Q: क्या मौजूदा FBX को लोड करके, उसकी एसेट जानकारी को संशोधित करके, फिर पुनः सहेजना संभव है?**  
A: बिल्कुल। फ़ाइल को `new Scene("input.fbx")` से लोड करें, `scene.getAssetInfo()` को संशोधित करें, फिर सहेजें।

---

**अंतिम अपडेट:** 2026-09-08  
**परीक्षित संस्करण:** Aspose.3D for Java 24.11  
**लेखक:** Aspose

## संबंधित ट्यूटोरियल

- [3D फ़ाइल आकार घटाएँ – Aspose.3D for Java के साथ सीन को संपीड़ित करें](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [जावा में vector3 रंग कैसे सेट करें: Diffuse Color बदलें और Aspose.3D का उपयोग करके जावा सीन में 3D प्रॉपर्टीज़ प्रबंधित करें](/3d/java/3d-scenes-and-models/managing-3d-properties-scenes/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}