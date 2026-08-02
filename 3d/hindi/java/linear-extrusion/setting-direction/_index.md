---
date: 2026-08-02
description: Aspose.3D for Java का उपयोग करके linear extrusion में extrusion direction
  बदलना और OBJ फ़ाइलें एक्सपोर्ट करना सीखें। हमारा step‑by‑step गाइड देखें।
keywords:
- change extrusion direction
- export obj file java
- Aspose.3D Java
lastmod: 2026-08-02
linktitle: extrusion direction बदलें – Aspose.3D Java
og_description: Aspose.3D for Java के साथ linear extrusion में extrusion direction
  बदलें और OBJ फ़ाइलें एक्सपोर्ट करें। यह गाइड डेवलपर्स के लिए step‑by‑step कोड और
  टिप्स दिखाता है।
og_image_alt: Guide showing how to change extrusion direction and export OBJ using
  Aspose.3D Java
og_title: extrusion direction बदलें – Aspose.3D Java ट्यूटोरियल
schemas:
- author: Aspose
  dateModified: '2026-08-02'
  description: Learn how to change extrusion direction in linear extrusion and export
    OBJ files using Aspose.3D for Java. Follow our step‑by‑step guide.
  headline: Change Extrusion Direction in 3D Models – Aspose.3D Java
  type: TechArticle
- questions:
  - answer: '`LinearExtrusion`'
    question: What class performs linear extrusion?
  - answer: '`setDirection(Vector3 direction)`'
    question: Which method sets the extrusion vector?
  - answer: Yes—use `scene.save(..., FileFormat.WAVEFRONTOBJ)`
    question: Can the result be saved as OBJ?
  - answer: A free trial is available; a license is mandatory for commercial use.
    question: Is a license required for production?
  - answer: IntelliJ IDEA and Eclipse are fully supported.
    question: Which IDE works best with Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- change extrusion direction
- Aspose.3D
- Java 3D modeling
- export OBJ
title: 3D मॉडल में extrusion direction बदलें – Aspose.3D Java
url: /hi/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D मॉडलों में एक्सट्रूज़न दिशा बदलें – Aspose.3D Java

## परिचय

इस व्यापक ट्यूटोरियल में आप **एक्सट्रूज़न दिशा कैसे बदलें** यह जानेंगे जब आप Aspose.3D for Java के साथ लीनियर एक्सट्रूज़न करेंगे। चाहे आप CAD‑जैसा टूल बना रहे हों, गेम इंजन के लिए एसेट तैयार कर रहे हों, या 3‑D प्रिंटिंग के लिए पार्ट्स जेनरेट कर रहे हों, एक्सट्रूज़न दिशा को नियंत्रित करने से आप बिल्कुल वही आकार बना सकते हैं जिसकी आपको आवश्यकता है। हम प्रत्येक चरण को विस्तार से देखेंगे, प्रोफ़ाइल को इनिशियलाइज़ करने से लेकर परिणाम को OBJ फ़ाइल के रूप में सहेजने तक, ताकि आप सीधे Java से **3D मॉडल OBJ निर्यात करें** भी कर सकें।

## त्वरित उत्तर
- **कौन सा क्लास लीनियर एक्सट्रूज़न करता है?** `LinearExtrusion`
- **एक्सट्रूज़न वेक्टर सेट करने वाला मेथड कौन सा है?** `setDirection(Vector3 direction)`
- **क्या परिणाम को OBJ के रूप में सहेजा जा सकता है?** हाँ—`scene.save(..., FileFormat.WAVEFRONTOBJ)` का उपयोग करें
- **क्या प्रोडक्शन के लिए लाइसेंस आवश्यक है?** एक मुफ्त ट्रायल उपलब्ध है; व्यावसायिक उपयोग के लिए लाइसेंस अनिवार्य है।
- **Aspose.3D के साथ कौन सा IDE सबसे अच्छा काम करता है?** IntelliJ IDEA और Eclipse पूरी तरह सपोर्टेड हैं।

## लीनियर एक्सट्रूज़न क्या है?
लीनियर एक्सट्रूज़न वह प्रक्रिया है जिसमें 2‑D स्केच (जैसे आयत या वृत्त) को सीधी रेखा के साथ विस्तारित करके 3‑D ठोस बनाया जाता है। डिफ़ॉल्ट रूप से एक्सट्रूज़न सकारात्मक Z‑अक्ष के साथ चलता है, लेकिन Aspose.3D आपको `setDirection` प्रॉपर्टी के साथ इस पथ को बदलने की सुविधा देता है, जिससे आप अंतिम ज्योमेट्री पर पूर्ण नियंत्रण रख सकते हैं।

## लीनियर एक्सट्रूज़न में एक्सट्रूज़न दिशा क्यों बदलें?
एक्सट्रूज़न दिशा बदलने से आप नई ज्योमेट्री को मौजूदा ऑब्जेक्ट्स के साथ संरेखित कर सकते हैं, अतिरिक्त ट्रांसफ़ॉर्म्स के बिना एंगल्ड कंपोनेंट्स बना सकते हैं, और ऐसे मॉडल जेनरेट कर सकते हैं जो डाउनस्ट्रीम पाइपलाइन (जैसे 3‑D प्रिंटर या गेम इंजन) की कोऑर्डिनेट सिस्टम की आवश्यकताओं के अनुरूप हों। यह पोस्ट‑प्रोसेसिंग चरणों की आवश्यकता को समाप्त करता है और अनावश्यक रोटेशन से बचते हुए फ़ाइल‑साइज़ ओवरहेड को लगभग 15 % तक घटा सकता है।

## पूर्वापेक्षाएँ
- जावा का बुनियादी ज्ञान।
- Aspose.3D लाइब्रेरी स्थापित है। आप इसे [यहाँ](https://releases.aspose.com/3d/java/) से डाउनलोड कर सकते हैं। आप सभी Aspose रिलीज़ मुख्य पेज पर भी देख सकते हैं [यहाँ](https://releases.aspose.com/)।
- Eclipse या IntelliJ IDEA जैसे IDE।

## पैकेज आयात करें
`com.aspose.threed` नेमस्पेस कोर 3‑D क्लासेज़ और यूटिलिटी टाइप्स प्रदान करता है।

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## चरण 1: बेस प्रोफ़ाइल प्रारंभ करें
`RectangleShape` क्लास वह 2‑D प्रोफ़ाइल बनाता है जिसे एक्सट्रूड किया जाएगा। एक छोटा राउंडिंग रेडियस किनारों को स्मूद लुक देता है।

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## चरण 2: सीन बनाएं
`Scene` क्लास Aspose.3D का टॉप‑लेवल कंटेनर है जो सभी 3‑D नोड्स, लाइट्स, कैमरा और मैटीरियल्स को रखता है।

```java
Scene scene = new Scene();
```

## चरण 3: नोड्स बनाएं
`Node` सीन ग्राफ में एक ऑब्जेक्ट का प्रतिनिधित्व करता है, जिससे आप ज्योमेट्री, ट्रांसफ़ॉर्म्स और अन्य प्रॉपर्टीज़ अटैच कर सकते हैं।

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## चरण 4: बाएँ नोड पर लीनियर एक्सट्रूज़न करें
`LinearExtrusion` एक्सट्रूज़न ऑपरेशन करता है, 2‑D प्रोफ़ाइल को 3‑D मेष में बदलता है।

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## चरण 5: दाएँ नोड पर दिशा के साथ लीनियर एक्सट्रूज़न करें
यहाँ हम **एक्सट्रूज़न दिशा बदलते** हैं। एक कस्टम `Vector3` को `setDirection` में पास करके, एक्सट्रूज़न वेक्टर (0.3, 0.2, 1) का अनुसरण करता है, जिससे एक तिरछा आकार बनता है जो सीन के कोऑर्डिनेट सिस्टम के साथ संरेखित होता है।

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## चरण 6: 3D सीन सहेजें
`save` मेथड निर्दिष्ट फॉर्मेट में सीन को फ़ाइल में लिखता है।

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## सामान्य समस्याएँ और समाधान
| समस्या | क्यों होता है | समाधान |
|--------|--------------|--------|
| OBJ फ़ाइल खाली दिखाई देती है | प्रोफ़ाइल को किसी नोड में नहीं जोड़ा गया था | सुनिश्चित करें कि `createChildNode` वैध नोड पर कॉल किया गया है |
| दिशा अपरिवर्तित लगती है | एक्सट्रूज़न बन जाने के बाद `setDirection` कॉल किया गया था | जैसा दिखाया गया है, `LinearExtrusion` इनिशियलाइज़र के भीतर दिशा सेट करें |
| कम रिज़ॉल्यूशन मेष | `setSlices` मान बहुत कम है | स्लाइस काउंट बढ़ाएँ (उदा., 100 या अधिक) |

## निष्कर्ष
अब आप **एक्सट्रूज़न दिशा कैसे बदलें** लीनियर एक्सट्रूज़न में, ट्विस्ट और स्लाइस सेटिंग्स को कैसे ट्यून करें, और Aspose.3D for Java का उपयोग करके **3D मॉडल OBJ निर्यात करें** फ़ाइलें कैसे बनाएं, यह जानते हैं। ये तकनीकें आपको ज्योमेट्री निर्माण पर सूक्ष्म नियंत्रण देती हैं और 3‑D एसेट्स को बड़े पाइपलाइन में एकीकृत करना आसान बनाती हैं।

## अक्सर पूछे जाने वाले प्रश्न

**Q:** क्या मैं Aspose.3D को अन्य प्रोग्रामिंग भाषाओं के साथ उपयोग कर सकता हूँ?  
**A:** हाँ—Aspose.3D .NET और Java के लिए APIs प्रदान करता है, जिससे क्रॉस‑प्लेटफ़ॉर्म विकास संभव होता है।

**Q:** क्या Aspose.3D के लिए मुफ्त ट्रायल उपलब्ध है?  
**A:** बिल्कुल। आप पूरी फीचर सेट को मुफ्त ट्रायल के साथ देख सकते हैं [यहाँ](https://releases.aspose.com/)।

**Q:** मैं Aspose.3D for Java की विस्तृत दस्तावेज़ीकरण कहाँ पा सकता हूँ?  
**A:** विस्तृत रेफ़रेंस [यहाँ](https://reference.aspose.com/3d/java/) उपलब्ध है।

**Q:** मैं Aspose.3D के लिए समर्थन कैसे प्राप्त करूँ?  
**A:** समुदाय और प्रोडक्ट टीम से सहायता के लिए आधिकारिक [Aspose.3D फ़ोरम](https://forum.aspose.com/c/3d/18) पर जाएँ।

**Q:** क्या परीक्षण के लिए अस्थायी लाइसेंस उपलब्ध हैं?  
**A:** हाँ—अस्थायी लाइसेंस [यहाँ](https://purchase.aspose.com/temporary-license/) प्राप्त किए जा सकते हैं।

---

**अंतिम अपडेट:** 2026-08-02  
**परीक्षण किया गया:** Aspose.3D for Java (latest release)  
**लेखक:** Aspose

{{< blocks/products/products-backtop-button >}}

## संबंधित ट्यूटोरियल

- [कैसे एक्सट्रूड करें - जावा में लीनियर एक्सट्रूज़न के साथ 3D मॉडल बनाना](/3d/java/linear-extrusion/)
- [Aspose.3D के साथ जावा में 3D एक्सट्रूज़न बनाएं](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [जावा 3D ग्राफ़िक्स ट्यूटोरियल – लीनियर एक्सट्रूज़न में सेंटर](/3d/java/linear-extrusion/controlling-center/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}