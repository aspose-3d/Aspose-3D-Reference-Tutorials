---
date: 2026-01-27
description: जावा में Aspose.3D के साथ सामग्री के आधार पर मेष को कुशलतापूर्वक विभाजित
  करना सीखें। यह गाइड आपको दिखाता है कि कैसे ड्रॉ कॉल्स को कम किया जाए और सामग्री
  के आधार पर मेष को विभाजित करते समय रेंडरिंग प्रदर्शन को बेहतर बनाया जाए।
linktitle: How to Split Mesh by Material in Java Using Aspose.3D
second_title: Aspose.3D Java API
title: जावा में Aspose.3D का उपयोग करके सामग्री के आधार पर मेष को कैसे विभाजित करें
url: /hi/java/3d-mesh-data/split-meshes-by-material/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# How to Split Mesh by Material in Java Using Aspose.3D

## Introduction

यदि आप Java में 3D ग्राफ़िक्स के साथ काम कर रहे हैं, तो आप जल्दी ही देखेंगे कि बड़े meshes को प्रोसेस करना प्रदर्शन का बोतलनेक बन सकता है—विशेष रूप से जब एक ही mesh में कई material होते हैं। **material के आधार पर mesh को split करने** से आप प्रत्येक material‑विशिष्ट polygon समूह को अलग कर सकते हैं, जिससे तेज़ rendering, आसान culling, और texture handling पर अधिक सूक्ष्म नियंत्रण मिलता है। इस ट्यूटोरियल में हम **material के आधार पर mesh को split करने** के सटीक चरणों को Aspose.3D लाइब्रेरी का उपयोग करके दिखाएंगे, साथ ही व्यावहारिक व्याख्याएँ, draw calls को कम करने के टिप्स, और rendering प्रदर्शन को बेहतर बनाने के सुझाव प्रदान करेंगे।

## Quick Answers
# Aspose.3D का इस्तेमाल करके Java में मटीरियल के हिसाब से मेश कैसे स्प्लिट करें

## इंट्रोडक्शन

यदि आप Java में 3D ग्राफ़िक्स के साथ काम कर रहे हैं, तो आप जल्दी ही देखेंगे कि बड़े meshes को प्रोसेस करना प्रदर्शन का बोतलनेक बन सकता है—विशेष रूप से जब एक ही mesh में कई material होते हैं। **material के आधार पर mesh को split करने** से आप प्रत्येक material‑विशिष्ट polygon समूह को अलग कर सकते हैं, जिससे तेज़ rendering, आसान culling, और texture handling पर अधिक सूक्ष्म नियंत्रण मिलता है। इस ट्यूटोरियल में हम **material के आधार पर mesh को split करने** के सटीक चरणों को Aspose.3D लाइब्रेरी का उपयोग करके दिखाएंगे, साथ ही व्यावहारिक व्याख्याएँ, draw calls को कम करने के टिप्स, और rendering प्रदर्शन को बेहतर बनाने के सुझाव प्रदान करेंगे।

## क्विक आंसर्स
- **“material के आधार पर mesh को split करना” क्या मतलब है?** यह एक ही mesh को कई sub‑meshes में विभाजित करता है, जहाँ प्रत्येक sub‑mesh में वही polygons होते हैं जो एक ही material को साझा करते हैं।
- **Aspose.3D क्यों उपयोग करें?** यह एक हाई‑लेवल, क्रॉस‑प्लेटफ़ॉर्म API प्रदान करता है जो लो‑लेवल फ़ाइल फ़ॉर्मेट को एब्स्ट्रैक्ट करता है जबकि प्रदर्शन बनाए रखता है।
- **इम्प्लीमेंटेशन में कितना समय लगेगा?** लगभग 10–15 मिनट कोडिंग और टेस्टिंग के लिए।
- **क्या लाइसेंस की आवश्यकता है?** एक फ्री ट्रायल उपलब्ध है; प्रोडक्शन उपयोग के लिए कमर्शियल लाइसेंस आवश्यक है।
- **कौन सा Java संस्करण समर्थित है?** Java 8 या उससे ऊपर।

## What is Mesh Splitting?

Mesh splitting वह प्रक्रिया है जिसमें एक जटिल 3D mesh को छोटे, अधिक प्रबंधनीय टुकड़ों में विभाजित किया जाता है। जब split material के आधार पर किया जाता है, तो प्रत्येक परिणामी sub‑mesh में केवल वही polygons होते हैं जो एक ही material को संदर्भित करते हैं। यह दृष्टिकोण draw calls को कम करता है, rendering प्रदर्शन को सुधारता है, और per‑material shaders जैसे कार्यों को सरल बनाता है।

## Why Split Mesh by Material?
## मेश स्प्लिटिंग क्या है?

Mesh splitting वह प्रक्रिया है जिसमें एक जटिल 3D mesh को छोटे, अधिक प्रबंधनीय टुकड़ों में विभाजित किया जाता है। जब split material के आधार पर किया जाता है, तो प्रत्येक परिणामी sub‑mesh में केवल वही polygons होते हैं जो एक ही material को संदर्भित करते हैं। यह दृष्टिकोण draw calls को कम करता है, rendering प्रदर्शन को सुधारता है, और per‑material shaders जैसे कार्यों को सरल बनाता है।

## मटीरियल के हिसाब से मेश क्यों स्प्लिट करें?

- **Performance:** Rendering engines material के अनुसार draw calls को batch कर सकते हैं, जिससे GPU state changes कम होते हैं।
- **Flexibility:** आप प्रत्येक material पर अलग‑अलग post‑processing इफ़ेक्ट्स या collision logic लागू कर सकते हैं।
- **Memory Management:** छोटे meshes को मेमोरी में इन‑और‑आउट स्ट्रीम करना आसान होता है, जो मोबाइल या VR एप्लिकेशन्स के लिए महत्वपूर्ण है।
- **Reduced Draw Calls:** कम state changes का मतलब है GPU अधिक कुशलता से फ्रेम प्रोसेस कर सकता है।
- **Improved Rendering Performance:** Materials को अलग करने से अक्सर बेहतर culling और shading परिणाम मिलते हैं।

## Prerequisites
## ज़रूरी शर्तें

कोड में डुबकी लगाने से पहले सुनिश्चित करें कि आपके पास निम्नलिखित हों:

- Java प्रोग्रामिंग का बेसिक ज्ञान।
- Aspose.3D for Java लाइब्रेरी इंस्टॉल हो (डाउनलोड करें [Aspose वेबसाइट](https://releases.aspose.com/3d/java/) से)।
- IntelliJ IDEA, Eclipse, या VS Code जैसे IDE, जो Java विकास के लिए कॉन्फ़िगर किया गया हो।

## Import Packages
## पैकेज इंपोर्ट करें

पहले, आवश्यक Aspose.3D क्लासेज़ और कोई भी स्टैंडर्ड Java यूटिलिटीज़ इम्पोर्ट करें:

```java
import com.aspose.threed.*;

import java.util.Arrays;
```

 Step‑by‑Step Guide

नीचे प्रत्येक चरण का संक्षिप्त walkthrough दिया गया है, जहाँ कोड ब्लॉक्स से पहले व्याख्याएँ हैं ताकि आप ठीक‑ठीक समझ सकें कि क्या हो रहा है।

### Step 1: Create a Mesh of a Box
स्टेप-बाय-स्टेप गाइड

नीचे प्रत्येक चरण का संक्षिप्त walkthrough दिया गया है, जहाँ कोड ब्लॉक्स से पहले व्याख्याएँ हैं ताकि आप ठीक‑ठीक समझ सकें कि क्या हो रहा है।

### स्टेप 1: बॉक्स का मेश बनाएं

हम एक सरल ज्यामितीय primitive—एक बॉक्स—से शुरू करते हैं, ताकि बाद में प्रत्येक फेस (plane) को अपना material मिल सके।

```java
// ExStart:SplitMeshbyMaterial

// Create a mesh of a box (composed of 6 planes)
Mesh box = (new Box()).toMesh();
```

### Step 2: Create a Material Element
### स्टेप 2: एक मटेरियल एलिमेंट बनाएं

`VertexElementMaterial` प्रत्येक polygon के लिए material indices संग्रहीत करता है। इसे mesh से जोड़कर हम नियंत्रित कर सकते हैं कि प्रत्येक फेस कौन सा material उपयोग करे।

```java
// Create a material element on the box mesh
VertexElementMaterial mat = (VertexElementMaterial) box.createElement(VertexElementType.MATERIAL, MappingMode.POLYGON, ReferenceMode.INDEX);
```

### Step 3: Specify Different Material Indices
### स्टेप 3: अलग-अलग मटेरियल इंडेक्स बताएं

यहाँ हम बॉक्स के छह planes में से प्रत्येक को एक अनूठा material index असाइन करते हैं। ऐरे का क्रम `Box` primitive द्वारा उत्पन्न polygons के क्रम से मेल खाता है।

```java
// Specify different material indices for each plane
mat.setIndices(new int[]{0, 1, 2, 3, 4, 5});
```

### Step 4: Split the Mesh into Sub‑Meshes
### स्टेप 4: मेश को सब-मेश में बांटें

`PolygonModifier.splitMesh` को `SplitMeshPolicy.CLONE_DATA` के साथ कॉल करने से प्रत्येक अलग‑अलग material index के लिए एक नया sub‑mesh बनता है, जबकि मूल vertex डेटा संरक्षित रहता है।

```java
// Split the mesh into 6 sub-meshes, each plane becoming a sub-mesh
Mesh[] planes = PolygonModifier.splitMesh(box, SplitMeshPolicy.CLONE_DATA);
```

### Step 5: Update Material Indices and Split Again
### स्टेप 5: मटेरियल इंडेक्स अपडेट करें और फिर से बांटें

एक अलग splitting रणनीति दिखाने के लिए, अब हम पहले तीन planes को material 0 और शेष तीन को material 1 के तहत समूहित करते हैं, फिर `COMPACT_DATA` का उपयोग करके अनउपयोगी vertices को हटाते हुए split करते हैं।

```java
// Update material indices and split into 2 sub-meshes
mat.getIndices().clear();
mat.setIndices(new int[]{0, 0, 0, 1, 1, 1});
planes = PolygonModifier.splitMesh(box, SplitMeshPolicy.COMPACT_DATA);
```

### Step 6: Confirm Success
### स्टेप 6: सफलता कन्फर्म करें

एक साधा console संदेश आपको बताता है कि ऑपरेशन बिना त्रुटियों के पूरा हो गया।

```java
// Display success message
System.out.println("\nSplitting a mesh by specifying the material successfully.");
// ExEnd:SplitMeshbyMaterial
```

## Reduce Draw Calls and Improve Rendering Performance

प्रत्येक material को अपना अलग mesh बनाकर, आप ग्राफ़िक्स पाइपलाइन को प्रत्येक material के लिए एक ही draw call जारी करने की अनुमति देते हैं, बजाय प्रत्येक polygon के लिए कई draw calls के। यह draw calls में कमी सीधे स्मूथ फ्रेम रेट में परिवर्तित होती है, विशेषकर लो‑एंड हार्डवेयर पर। अतिरिक्त रूप से, `COMPACT_DATA` नीति अनउपयोगी vertices को हटाती है, जिससे मेमोरी बैंडविड्थ कम होती है और GPU अधिक कुशलता से रेंडर करता है।

## Common Issues and Solutions

| Issue | Why It Happens | Fix |
|-------|----------------|-----|
| **Sub‑meshes contain duplicate vertices** | Using `CLONE_DATA` copies all vertex data for each sub‑mesh. | Switch to `COMPACT_DATA` when you want shared vertices to be deduplicated. |
| **Incorrect material assignment** | Indices array length does not match polygon count. | Verify the number of polygons (e.g., a box has 6) and supply a matching indices array. |

## Frequently Asked Questions

**Q: Is Aspose.3D compatible with other Java 3D libraries?**  
A: Yes, Aspose.3D can coexist with libraries like Java 3D or jMonkeyEngine, allowing you to import/export meshes between them.

**Q: Can this technique be applied to complex models with hundreds of materials?**  
A: Absolutely. The same API calls work regardless of mesh complexity; just ensure your indices array correctly reflects the material layout.

**Q: Where can I find the full Aspose.3D Java documentation?**  
A: Visit the official [Aspose.3D Java documentation](https://reference.aspose.com/3d/java/) for detailed API references and additional examples.

**Q: Is a free trial available for Aspose.3D for Java?**  
A: Yes, you can download a trial version from the [Aspose Releases page](https://releases.aspose.com/).

**Q: How can I get support if I run into issues?**  
A: The Aspose community forum ([Aspose.3D forum](https://forum.aspose.com/c/3d/18)) is an excellent place to ask questions and receive help from both the Aspose team and other developers.

---

**Last Updated:** 2026-01-27  
**Tested With:** Aspose.3D for Java 24.11  
**Author:** Aspose  
## ड्रॉ कॉल कम करें और रेंडरिंग परफॉर्मेंस बेहतर करें

प्रत्येक material को अपना अलग mesh बनाकर, आप ग्राफ़िक्स पाइपलाइन को प्रत्येक material के लिए एक ही draw call जारी करने की अनुमति देते हैं, बजाय प्रत्येक polygon के लिए कई draw calls के। यह draw calls में कमी सीधे स्मूथ फ्रेम रेट में परिवर्तित होती है, विशेषकर लो‑एंड हार्डवेयर पर। अतिरिक्त रूप से, `COMPACT_DATA` नीति अनउपयोगी vertices को हटाती है, जिससे मेमोरी बैंडविड्थ कम होती है और GPU अधिक कुशलता से रेंडर करता है।

## आम दिक्कतें और समाधान

| दिक्कत | ऐसा क्यों होता है | ठीक करें |
|-------|----------------|-----|
| **सब-मेश में डुप्लीकेट वर्टेक्स होते हैं** | `CLONE_DATA` का इस्तेमाल करने से हर सब-मेश के लिए सभी वर्टेक्स डेटा कॉपी हो जाते हैं। | जब आप शेयर किए गए वर्टेक्स को डीडुप्लीकेट करना चाहते हैं तो `COMPACT_DATA` पर स्विच करें। |
| **गलत मटेरियल असाइनमेंट** | इंडेक्स ऐरे की लंबाई पॉलीगॉन काउंट से मैच नहीं करती है। | पॉलीगॉन की संख्या वेरिफ़ाई करें (जैसे, एक बॉक्स में 6 हैं) और मैचिंग इंडेक्स ऐरे दें। |

## अक्सर पूछे जाने वाले सवाल

**सवाल: क्या Aspose.3D दूसरी Java 3D लाइब्रेरी के साथ कम्पैटिबल है?**
जवाब: हाँ, Aspose.3D Java3D या jMonkeyEngine जैसी लाइब्रेरी के साथ काम कर सकता है, जिससे आप उनके बीच मेश इंपोर्ट/एक्सपोर्ट कर सकते हैं।

**सवाल: क्या यह टेक्निक सैकड़ों मटीरियल वाले कॉम्प्लेक्स मॉडल पर अप्लाई की जा सकती है?**
जवाब: बिल्कुल। मेश कॉम्प्लेक्सिटी के बावजूद वही API कॉल काम करते हैं; बस यह पक्का करें कि आपका इंडेक्स ऐरे मटीरियल लेआउट को सही ढंग से दिखाए।

**सवाल: मुझे पूरा Aspose.3D Java डॉक्यूमेंटेशन कहाँ मिल सकता है?**
जवाब: डिटेल्ड API रेफरेंस और एक्स्ट्रा उदाहरणों के लिए ऑफिशियल [Aspose.3D Java डॉक्यूमेंटेशन](https://reference.aspose.com/3d/java/) पर जाएँ।

**सवाल: क्या Java के लिए Aspose.3D का फ़्री ट्रायल उपलब्ध है?**
जवाब: हाँ, आप [Aspose Releases पेज](https://releases.aspose.com/) से ट्रायल वर्शन डाउनलोड कर सकते हैं।

**सवाल: अगर मुझे कोई दिक्कत आती है तो मुझे सपोर्ट कैसे मिल सकता है?**
जवाब: Aspose कम्युनिटी फ़ोरम ([Aspose.3D फ़ोरम](https://forum.aspose.com/c/3d/18)) सवाल पूछने और Aspose टीम और दूसरे डेवलपर्स से मदद पाने के लिए एक बहुत अच्छी जगह है।

---

**पिछला अपडेट:** 2026-01-27
**इसके साथ टेस्ट किया गया:** Java 24.11 के लिए Aspose.3D
**लेखक:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}