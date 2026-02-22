---
date: 2026-02-22
description: Aspose.3D for Java का उपयोग करके रैखिक एक्सट्रूज़न में दिशा सेट करना
  और 3D मॉडल OBJ निर्यात करना सीखें। हमारे चरण‑दर‑चरण मार्गदर्शक का पालन करें।
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Aspose.3D for Java के साथ रैखिक एक्सट्रूज़न में दिशा कैसे सेट करें
url: /hi/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# How to Set Direction in Linear Extrusion with Aspose.3D for Java

## Introduction

इस व्यापक ट्यूटोरियल में आप **लाइनर एक्सट्रूज़न** के दौरान दिशा कैसे सेट करें, यह जानेंगे, Aspose.3D for Java का उपयोग करके। चाहे आप CAD‑जैसा टूल बना रहे हों या गेम इंजन के लिए ज्योमेट्री जेनरेट कर रहे हों, एक्सट्रूज़न दिशा को नियंत्रित करने से आप बिल्कुल वही आकार बना सकते हैं जिसकी आपको आवश्यकता है। हम प्रत्येक चरण को विस्तार से बताएँगे, प्रोफ़ाइल को इनिशियलाइज़ करने से लेकर परिणाम को OBJ फ़ाइल के रूप में सेव करने तक, ताकि आप सीधे Java से **3d मॉडल obj** फ़ाइलें एक्सपोर्ट कर सकें।

## Quick Answers
- **What is the primary class for linear extrusion?** `LinearExtrusion`
- **Which method defines extrusion direction?** `setDirection(Vector3 direction)`
- **Can I export the result as OBJ?** Yes, using `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **Do I need a license for development?** A free trial is available; a license is required for production.
- **What Java IDE works best?** IntelliJ IDEA or Eclipse are both fully supported.

## What is Linear Extrusion?

लाइनर एक्सट्रूज़न 2‑D प्रोफ़ाइल (जैसे कि रेक्टैंगल या सर्कल) को एक सीधी रेखा के साथ विस्तारित करके 3‑D ठोस बनाता है। डिफ़ॉल्ट रूप से एक्सट्रूज़न पॉज़िटिव Z‑axis का अनुसरण करता है, लेकिन Aspose.3D आपको `setDirection` प्रॉपर्टी के साथ इस पाथ को बदलने की सुविधा देता है।

## Why Set Direction in Linear Extrusion?

कस्टम दिशा सेट करना उपयोगी होता है जब:
- सीन में मौजूदा ऑब्जेक्ट्स के साथ ज्योमेट्री को संरेखित करना हो।
- अतिरिक्त ट्रांसफ़ॉर्मेशन स्टेप्स के बिना तिरछे या कोणीय भाग बनाना हो।
- ऐसे मॉडल एक्सपोर्ट करना हों जो किसी विशिष्ट कोऑर्डिनेट सिस्टम से मेल खाते हों (जैसे 3‑D प्रिंटिंग या गेम इंजन के लिए)।

## Prerequisites

शुरू करने से पहले सुनिश्चित करें कि आपके पास है:

- Java का बेसिक ज्ञान।
- Aspose.3D लाइब्रेरी इंस्टॉल हो। आप इसे [here](https://releases.aspose.com/3d/java/) से डाउनलोड कर सकते हैं।
- Eclipse या IntelliJ IDEA जैसे IDE।

## Import Packages

पहले उन नेमस्पेसेस को इम्पोर्ट करें जो कोर 3‑D क्लासेज़ और यूटिलिटी टाइप्स प्रदान करते हैं।

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Step 1: Initialize Base Profile

उस आकार को बनाएं जिसे एक्सट्रूड किया जाएगा। इस उदाहरण में हम `RectangleShape` का उपयोग करते हैं जिसमें किनारों को स्मूद दिखाने के लिए थोड़ा राउंडिंग रेडियस दिया गया है।

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Step 2: Create a Scene

एक `Scene` ऑब्जेक्ट सभी 3‑D नोड्स, लाइट्स, कैमरा और मैटेरियल्स के लिए कंटेनर के रूप में कार्य करता है।

```java
Scene scene = new Scene();
```

## Step 3: Create Nodes

सीन रूट में दो चाइल्ड नोड्स जोड़ें—एक बाएँ‑हाथ एक्सट्रूज़न के लिए और एक दाएँ‑हाथ एक्सट्रूज़न के लिए। दाएँ नोड को ट्रांसलेट किया गया है ताकि दोनों ऑब्जेक्ट्स ओवरलैप न हों।

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Step 4: Perform Linear Extrusion on the Left Node

बाएँ नोड पर डिफ़ॉल्ट Z‑axis दिशा का उपयोग करके प्रोफ़ाइल को एक्सट्रूड करें। हम एक पूर्ण 360° ट्विस्ट भी जोड़ते हैं और स्मूथ मेष के लिए स्लाइस काउंट बढ़ाते हैं।

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Step 5: Perform Linear Extrusion on the Right Node with Direction

यहीं पर हम **दिशा सेट** करते हैं। `setDirection` में एक कस्टम `Vector3` पास करके, एक्सट्रूज़न वेक्टर (0.3, 0.2, 1) का अनुसरण करता है, जिससे एक तिरछा आकार बनता है।

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Step 6: Save 3D Scene

अंत में, सीन को Wavefront OBJ फॉर्मेट में एक्सपोर्ट करें। यह चरण दिखाता है कि **obj फ़ाइल java** प्रोजेक्ट्स को कैसे सेव किया जाता है और इसे किसी भी 3‑D व्यूअर में आसानी से देखा जा सकता है।

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Common Issues and Solutions

| Issue | Why it Happens | Fix |
|-------|----------------|-----|
| OBJ फ़ाइल खाली दिखती है | प्रोफ़ाइल को किसी नोड में नहीं जोड़ा गया था | सुनिश्चित करें कि `createChildNode` वैध नोड पर कॉल किया गया है |
| दिशा बदलती नहीं दिख रही | `setDirection` को एक्सट्रूज़न बन जाने के बाद कॉल किया गया | जैसा दिखाया गया है, `LinearExtrusion` इनिशियलाइज़र के अंदर दिशा सेट करें |
| मेष की रेज़ोल्यूशन कम है | `setSlices` का मान बहुत कम है | स्लाइस काउंट बढ़ाएँ (उदाहरण के लिए 100 या अधिक) |

## Conclusion

अब आप जानते हैं **लाइनर एक्सट्रूज़न में दिशा कैसे सेट करें**, ट्विस्ट और स्लाइस सेटिंग्स को कैसे ट्यून करें, और Aspose.3D for Java का उपयोग करके **3d मॉडल obj** फ़ाइलें कैसे एक्सपोर्ट करें। ये तकनीकें आपको ज्योमेट्री निर्माण पर सूक्ष्म नियंत्रण देती हैं और बड़े पाइपलाइन में 3‑D एसेट्स को इंटीग्रेट करना आसान बनाती हैं।

## FAQ's

### Q1: Can I use Aspose.3D with other programming languages?

A1: Aspose.3D supports various programming languages, including .NET and Java.

### Q2. Is there a free trial available for Aspose.3D?

A2: Yes, you can explore the features of Aspose.3D with a free trial [here](https://releases.aspose.com/).

### Q3: Where can I find detailed documentation for Aspose.3D for Java?

A3: The comprehensive documentation is available [here](https://reference.aspose.com/3d/java/).

### Q4: How can I get support for Aspose.3D?

A4: Visit the [Aspose.3D forum](https://forum.aspose.com/c/3d/18) for any assistance or queries.

### Q5: Are temporary licenses available for Aspose.3D?

A5: Yes, you can obtain a temporary license [here](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2026-02-22  
**Tested With:** Aspose.3D for Java (latest release)  
**Author:** Aspose