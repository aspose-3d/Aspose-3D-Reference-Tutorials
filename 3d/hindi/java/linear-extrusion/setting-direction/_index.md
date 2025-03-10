---
title: जावा के लिए Aspose.3D के साथ लीनियर एक्सट्रूज़न में दिशा निर्धारित करना
linktitle: जावा के लिए Aspose.3D के साथ लीनियर एक्सट्रूज़न में दिशा निर्धारित करना
second_title: Aspose.3D जावा एपीआई
description: जावा के लिए Aspose.3D के साथ लीनियर एक्सट्रूज़न में महारत हासिल करें! निर्बाध 3डी प्रोग्रामिंग के लिए हमारे गाइड का पालन करें। मनोरम अनुभव के लिए अभी डाउनलोड करें।
weight: 12
url: /hi/java/linear-extrusion/setting-direction/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# जावा के लिए Aspose.3D के साथ लीनियर एक्सट्रूज़न में दिशा निर्धारित करना

## परिचय

जावा के लिए Aspose.3D का उपयोग करके रैखिक एक्सट्रूज़न में दिशा निर्धारित करने पर हमारी चरण-दर-चरण मार्गदर्शिका में आपका स्वागत है। Aspose.3D एक शक्तिशाली जावा लाइब्रेरी है जो डेवलपर्स को 3D फ़ाइलों और दृश्यों के साथ निर्बाध रूप से काम करने की अनुमति देती है। इस ट्यूटोरियल में, हम लीनियर एक्सट्रूज़न में दिशा निर्धारित करने, 3डी प्रोग्रामिंग में आपकी दक्षता बढ़ाने के विशिष्ट कार्य पर ध्यान केंद्रित करेंगे।

## आवश्यक शर्तें

इससे पहले कि हम ट्यूटोरियल में उतरें, सुनिश्चित करें कि आपके पास निम्नलिखित आवश्यक शर्तें हैं:

- जावा प्रोग्रामिंग भाषा का बुनियादी ज्ञान।
-  Aspose.3D लाइब्रेरी स्थापित की गई। आप इसे यहां से डाउनलोड कर सकते हैं[यहाँ](https://releases.aspose.com/3d/java/).
- जावा के लिए एक एकीकृत विकास वातावरण (आईडीई), जैसे कि एक्लिप्स या इंटेलीजे।

## पैकेज आयात करें

सुनिश्चित करें कि आप अपने प्रोजेक्ट को किकस्टार्ट करने के लिए आवश्यक पैकेज आयात करें:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## चरण 1: बेस प्रोफ़ाइल प्रारंभ करें

 एक्सट्रूड किए जाने वाले बेस प्रोफाइल को इनिशियलाइज़ करके शुरुआत करें। इस उदाहरण में, हम a का उपयोग करते हैं`RectangleShape` 0.3 की गोलाई त्रिज्या के साथ:

```java
// दस्तावेज़ निर्देशिका का पथ.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## चरण 2: एक दृश्य बनाएं

इसके बाद, बाहर निकाली गई वस्तुओं को शामिल करने के लिए एक 3डी दृश्य बनाएं:

```java
Scene scene = new Scene();
```

## चरण 3: नोड्स बनाएं

दृश्य के भीतर बाएँ और दाएँ नोड बनाएँ:

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## चरण 4: बाएं नोड पर रैखिक एक्सट्रूज़न करें

 का उपयोग करके बाएं नोड पर रैखिक एक्सट्रूज़न करें`LinearExtrusion`मोड़ और स्लाइस जैसे निर्दिष्ट मापदंडों के साथ वर्ग:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## चरण 5: दिशा के साथ दाएं नोड पर रैखिक एक्सट्रूज़न करें

 का परिचय देते हुए, दाएँ नोड पर रैखिक एक्सट्रूज़न करें`setDirection` एक्सट्रूज़न दिशा को परिभाषित करने के लिए संपत्ति:

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## चरण 6: 3डी दृश्य सहेजें

3डी दृश्य को वांछित फ़ाइल स्वरूप में सहेजें। इस उदाहरण में, हम इसे वेवफ्रंट OBJ फ़ाइल के रूप में सहेजते हैं:

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## निष्कर्ष

बधाई हो! आपने जावा के लिए Aspose.3D का उपयोग करके रैखिक एक्सट्रूज़न में दिशा निर्धारित करना सफलतापूर्वक सीख लिया है। यह ट्यूटोरियल 3डी प्रोग्रामिंग में आपके कौशल को बढ़ाता है और रचनात्मक परियोजनाओं के लिए नई संभावनाएं खोलता है।

## अक्सर पूछे जाने वाले प्रश्न

### Q1: क्या मैं अन्य प्रोग्रामिंग भाषाओं के साथ Aspose.3D का उपयोग कर सकता हूँ?

A1: Aspose.3D .NET और Java सहित विभिन्न प्रोग्रामिंग भाषाओं का समर्थन करता है।

### Q2. क्या Aspose.3D के लिए कोई निःशुल्क परीक्षण उपलब्ध है?

 उ2: हाँ, आप नि:शुल्क परीक्षण के साथ Aspose.3D की विशेषताओं का पता लगा सकते हैं[यहाँ](https://releases.aspose.com/).

### Q3: मैं जावा के लिए Aspose.3D के लिए विस्तृत दस्तावेज़ कहां पा सकता हूं?

 A3: व्यापक दस्तावेज़ उपलब्ध है[यहाँ](https://reference.aspose.com/3d/java/).

### Q4: मैं Aspose.3D के लिए समर्थन कैसे प्राप्त कर सकता हूं?

 A4: पर जाएँ[Aspose.3D फोरम](https://forum.aspose.com/c/3d/18) किसी भी सहायता या प्रश्न के लिए।

### Q5: क्या Aspose.3D के लिए अस्थायी लाइसेंस उपलब्ध हैं?

 A5: हाँ, आप अस्थायी लाइसेंस प्राप्त कर सकते हैं[यहाँ](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
