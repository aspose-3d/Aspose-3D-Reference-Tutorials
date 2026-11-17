---
date: 2026-11-17
description: Java में स्फीयर मेष बनाकर और Google Draco के माध्यम से Aspose.3D द्वारा
  इसे संपीड़ित करके 3D मॉडल का आकार कैसे घटाएँ। मिनटों में पूरा कार्यप्रवाह सीखें।
images:
- /java/3d-mesh-data/compress-meshes-google-draco/og-image.png
keywords:
- create sphere mesh
- how to compress 3d
- reduce 3d model size
- aspose 3d java
- compress 3d mesh
lastmod: 2026-11-17
linktitle: 3D मॉडल का आकार घटाने का तरीका – Java में Google Draco का उपयोग करके स्फीयर
  मेष बनाएं
og_description: Java का उपयोग करके Aspose.3D और Google Draco के साथ स्फीयर मेष बनाएं
  और 3D मॉडल को संपीड़ित करें। यह ट्यूटोरियल दिखाता है कि स्फीयर कैसे जनरेट करें,
  .drc में एक्सपोर्ट करें और मिनटों में 95% तक आकार में कमी प्राप्त करें।
og_image_alt: 'Developer guide: Reduce 3d model size with Java sphere mesh and Draco
  compression'
og_title: Java और Draco के साथ स्फीयर मेष बनाएं और 3D मॉडल को संपीड़ित करें
schemas:
- author: Aspose
  dateModified: '2026-11-17'
  description: How to reduce 3d model size by generating a sphere mesh in Java and
    compressing it with Google Draco via Aspose.3D. Learn the full workflow in minutes.
  headline: How to reduce 3d model size with a Java sphere mesh and Draco
  type: TechArticle
- description: How to reduce 3d model size by generating a sphere mesh in Java and
    compressing it with Google Draco via Aspose.3D. Learn the full workflow in minutes.
  name: How to reduce 3d model size with a Java sphere mesh and Draco
  steps:
  - name: set up the project
    text: Create a new Java project (any IDE works) and add all Aspose.3D JARs to
      the classpath. Keep your source files in a package such as `com.example.draco`
      for clarity.
  - name: how to create sphere mesh in Java
    text: 'The `Sphere` class is Aspose.3D''s built‑in geometry generator that produces
      a triangulated mesh with a configurable radius and tessellation. > **Pro tip:**
      The `Sphere` class generates a triangulated mesh with a default radius of 1.0.
      You can pass custom radius, tessellation, or material parameters '
  - name: export the mesh to Draco format
    text: After the sphere is added to a `Scene` object, call `scene.save("sphere.drc",
      SaveFormat.Draco)`. Aspose.3D automatically selects optimal compression settings,
      but you can fine‑tune them by adjusting `DracoCompressionOptions` if you need
      the smallest possible file. `DracoCompressionOptions` lets you
  - name: verify the output
    text: Open the generated `.drc` file with a Draco viewer (e.g., three.js `DRACOLoader`)
      to ensure the geometry renders correctly. You’ll notice a dramatic reduction
      in file size—often a factor of ten or more.
  type: HowTo
- questions:
  - answer: Yes, Aspose.3D supports OBJ, FBX, STL, GLTF, and many others, making it
      a versatile choice for **Aspose 3d export** pipelines.
    question: Is Aspose.3D compatible with different 3d file formats?
  - answer: Absolutely. Draco offers native libraries for C++, Python, and JavaScript.
      This tutorial focuses on Java, but the concepts apply across languages.
    question: Can I use Google Draco for compression in other programming languages?
  - answer: Visit the **[Aspose.3D Java documentation](https://reference.aspose.com/3d/java/)**
      for full API references and more examples.
    question: Where can I find additional Aspose.3D documentation?
  - answer: Explore temporary licensing options on the **[Aspose temporary license
      page](https://purchase.aspose.com/temporary-license/)**.
    question: How do I obtain a temporary license for Aspose.3D?
  - answer: Yes, join the discussion at the **[Aspose.3D Forum](https://forum.aspose.com/c/3d/18)**.
    question: Is there a community forum for Aspose.3D support?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- reduce 3d model size
- Aspose.3D
- Java 3D compression
- Google Draco
- sphere mesh
title: Java स्फीयर मेष और Draco के साथ 3D मॉडल का आकार कैसे घटाएँ
url: /hi/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# जावा स्फीयर मेष और ड्रैको के साथ 3डी मॉडल आकार कैसे कम करें

## परिचय

Aspose.3D for Java एक लाइब्रेरी है जो जावा कोड से सीधे 3‑D मॉडल बनाना, संशोधित करना और रूपांतरित करना संभव बनाती है। यदि आप उच्च‑गुणवत्ता वाली ज्योमेट्री प्रदान करते हुए **3d मॉडल आकार कम करने** का तेज़ तरीका खोज रहे हैं, तो आप सही जगह पर आए हैं। इस ट्यूटोरियल में हम **Aspose.3D for Java** के साथ एक स्फीयर मेष जेनरेट करेंगे और फिर **Google Draco** का उपयोग करके उस मेष को संकुचित करेंगे। अंत तक आपके पास एक तैयार‑उपयोग `.drc` फ़ाइल होगी जो मूल फ़ाइल से बहुत छोटी होगी, जिससे यह वेब‑आधारित व्यूअर्स, मोबाइल गेम्स, या किसी भी बैंडविड्थ‑सीमित जावा एप्लिकेशन के लिए उपयुक्त बनती है।

## त्वरित उत्तर

- **इस ट्यूटोरियल में क्या कवर किया गया है?** जावा में स्फीयर मेष बनाना और Aspose.3D के माध्यम से Google Draco के साथ उसे संकुचित करना।  
- **मुख्य लाइब्रेरी?** Aspose.3D for Java (मेश निर्माण और Draco निर्यात दोनों के लिए उपयोग किया जाता है)।  
- **सामान्य कार्यान्वयन समय?** एक बेसिक स्फीयर के लिए लगभग 10‑15 मिनट।  
- **मुख्य पूर्वापेक्षा?** क्लासपाथ में Aspose.3D JARs के साथ जावा विकास वातावरण।  
- **परिणाम?** एक `.drc` फ़ाइल जो अनकम्प्रेस्ड मेष की तुलना में **3d मॉडल आकार** को 95 % तक कम करती है।

## 3d मॉडल आकार कैसे कम करें?

अपने स्फीयर को लोड करें और दो सरल चरणों में उसे संकुचित करें। पहले, आप `new Sphere(1.0, 32, 32)` के साथ **स्फीयर मेष बनाते** हैं। फिर आप `scene.save("sphere.drc", SaveFormat.Draco)` का उपयोग करके सीन को सीधे Draco में निर्यात करते हैं। Aspose.3D स्वचालित रूप से ज्योमेट्री क्वांटाइज़ेशन और वर्टेक्स डेडुप्लिकेशन संभालता है, जिससे फ़ाइलें आमतौर पर 80‑95 % छोटी होती हैं जबकि दृश्य गुणवत्ता बनी रहती है।

`Sphere` क्लास Aspose.3D का अंतर्निहित ज्योमेट्री जेनरेटर है जो एक त्रिकोणीय स्फीयर मेष बनाता है। यह त्रिज्या और टेस्सेलेशन पैरामीटर स्वीकार करता है, जिससे आप संकुचन से पहले विवरण स्तर को नियंत्रित कर सकते हैं।

## 3d विकास के संदर्भ में “3d मॉडल आकार कम करना” क्या है?

**3d मॉडल आकार कम करना** का अर्थ है ज्योमेट्री डेटा की मात्रा को घटाना जिसे स्थानांतरित या संग्रहीत करने की आवश्यकता होती है, बिना दृश्य गुणवत्ता में स्पष्ट गिरावट के। Draco यह कार्य वर्टेक्स पोज़िशन, नॉर्मल्स और अन्य एट्रिब्यूट्स को अत्यधिक कॉम्पैक्ट बाइनरी फ़ॉर्मेट में एन्कोड करके करता है। जब इसे Aspose.3D के साथ जोड़ा जाता है, तो पूरा कार्यप्रवाह जावा के भीतर रहता है, इसलिए आपको नेटिव बाइनरीज़ से निपटना नहीं पड़ता।

## Aspose.3D के साथ Google Draco मेष संपीड़न क्यों उपयोग करें?

Google Draco को Aspose.3D के साथ मिलाकर एक कुशल पाइपलाइन मिलती है जो मेष फ़ाइलों को नाटकीय रूप से छोटा करती है जबकि उन्हें जावा प्रोजेक्ट्स में एकीकृत करना आसान बनाती है। लाइब्रेरी सभी लो‑लेवल एन्कोडिंग संभालती है, इसलिए डेवलपर्स को नेटिव Draco बाइनरीज़ से निपटने की जरूरत नहीं, जिससे विकास तेज़ होता है और वेब व मोबाइल के लिए छोटे एसेट्स मिलते हैं।

- **भारी आकार कमी:** Draco सामान्य मॉडलों के लिए मेष डेटा को 95 % तक कम कर सकता है, जिससे 5 MB OBJ को 0.3 MB `.drc` में बदल दिया जाता है।  
- **तेज़ रनटाइम डिकोडिंग:** Unity, Unreal, और three.js जैसे इंजन Draco को नेटिव रूप से डिकोड करते हैं, जिससे लोड समय तेज़ हो जाता है।  
- **सहज जावा एकीकरण:** Aspose.3D नेटिव Draco लाइब्रेरी को एब्स्ट्रैक्ट करता है, जिससे आप जावा इकोसिस्टम में रह सकते हैं।  
- **वन‑स्टॉप Aspose 3D निर्यात:** वही API जिसका उपयोग आप ज्योमेट्री बनाने के लिए करते हैं, निर्यात को भी संभालता है, जिससे पाइपलाइन सरल हो जाती है।  

Aspose.3D **50+ इनपुट और आउटपुट फ़ॉर्मेट** को सपोर्ट करता है — जिसमें OBJ, FBX, STL, GLTF, और कई अन्य शामिल हैं — और पूरी फ़ाइल को मेमोरी में लोड किए बिना सैकड़ों पेज वाले मॉडल को प्रोसेस कर सकता है।

## पूर्वापेक्षाएँ

- **Java Development Kit (JDK)** – संस्करण 8 या नया।  
- **Aspose.3D for Java** – नवीनतम JARs को **[Aspose 3D Java releases page](https://releases.aspose.com/3d/java/)** से डाउनलोड करें।  
- **Google Draco की बुनियादी परिचितता** – आप Aspose.3D का रैपर उपयोग करेंगे, इसलिए कोई नेटिव Draco सेटअप आवश्यक नहीं है।

## पैकेज आयात करें

```java
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Sphere;


import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

## स्टेप‑बाय‑स्टेप गाइड

### स्टेप 1: प्रोजेक्ट सेट अप करें

एक नया जावा प्रोजेक्ट बनाएं (कोई भी IDE काम करेगा) और सभी Aspose.3D JARs को क्लासपाथ में जोड़ें। स्पष्टता के लिए अपने स्रोत फ़ाइलों को `com.example.draco` जैसे पैकेज में रखें।

### स्टेप 2: जावा में स्फीयर मेष कैसे बनाएं

`Sphere` क्लास Aspose.3D का अंतर्निहित ज्योमेट्री जेनरेटर है जो एक त्रिकोणीय स्फीयर मेष बनाता है।  

```java
import java.nio.file.Files;
import java.nio.file.Paths;
import com.aspose.threed.Sphere;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.FileFormat;

// ExStart:Encode3DMeshinGoogleDraco
// The path to the documents directory.
String MyDir = "Your Document Directory";

// Create a sphere
Sphere sphere = new Sphere();

// Encode the sphere to Google Draco raw data using optimal compression level.
DracoSaveOptions opt = new DracoSaveOptions();
opt.setCompressionLevel(DracoCompressionLevel.OPTIMAL);
byte[] b = FileFormat.DRACO.encode(sphere.toMesh(), opt);

// Save the raw bytes to file
Files.write(Paths.get(MyDir, "SphereMeshtoDRC_Out.drc"), b);
// ExEnd:Encode3DMeshinGoogleDraco
```

> **प्रो टिप:** `Sphere` क्लास डिफ़ॉल्ट त्रिज्या 1.0 के साथ एक त्रिकोणीय मेष जेनरेट करता है। यदि आपको संकुचन से पहले अलग स्तर का विवरण चाहिए तो आप कस्टम त्रिज्या, टेस्सेलेशन, या मैटेरियल पैरामीटर पास कर सकते हैं।

### स्टेप 3: मेष को Draco फ़ॉर्मेट में निर्यात करें

`Scene` क्लास एक पूर्ण 3‑D सीन का प्रतिनिधित्व करता है जिसमें मेष, लाइट्स और कैमरे हो सकते हैं। `DracoCompressionOptions` क्लास आपको क्वांटाइज़ेशन और संकुचन स्तर जैसी Draco संकुचन सेटिंग्स को कस्टमाइज़ करने की अनुमति देता है। स्फीयर को `Scene` ऑब्जेक्ट में जोड़ने के बाद, `scene.save("sphere.drc", SaveFormat.Draco)` को कॉल करें। Aspose.3D स्वचालित रूप से इष्टतम संकुचन सेटिंग्स चुनता है, लेकिन यदि आपको सबसे छोटा फ़ाइल चाहिए तो आप `DracoCompressionOptions` को समायोजित करके उन्हें फाइन‑ट्यून कर सकते हैं। `DracoCompressionOptions` आपको

### स्टेप 4: आउटपुट को सत्यापित करें

`DRACOLoader` three.js का एक यूटिलिटी है जो Draco‑कम्प्रेस्ड `.drc` फ़ाइलों को लोड करता है और उन्हें WebGL‑संगत ज्योमेट्री में बदलता है। उत्पन्न `.drc` फ़ाइल को Draco व्यूअर (जैसे, three.js `DRACOLoader`) के साथ खोलें ताकि यह सुनिश्चित हो सके कि ज्योमेट्री सही ढंग से रेंडर हो रही है। आप फ़ाइल आकार में नाटकीय कमी देखेंगे—अक्सर दस गुना या उससे अधिक।

## सामान्य उपयोग मामलों

| परिदृश्य | मॉडल आकार क्यों कम करें? | यह ट्यूटोरियल कैसे मदद करता है |
|----------|-----------------------|--------------------------|
| वेब‑आधारित प्रोडक्ट कॉन्फ़िगरेटर | धीमी कनेक्शन पर तेज़ पेज लोड | Draco‑कम्प्रेस्ड `.drc` फ़ाइलें सेकंड में लोड होती हैं |
| मोबाइल AR/VR ऐप्स | डिवाइस पर कम मेमोरी फुटप्रिंट | छोटे मेष ऐप को प्रतिक्रियाशील रखते हैं |
| क्लाउड‑रेंडरड सीन | बैंडविड्थ लागत कम करें | Aspose.3D से Draco तक एक‑क्लिक निर्यात |

## सामान्य समस्याएँ और समाधान

| समस्या | कारण | समाधान |
|-------|--------|-----|
| **`NoClassDefFoundError` for Draco classes** | Aspose.3D JARs क्लासपाथ में नहीं हैं | सुनिश्चित करें कि *सभी* Aspose.3D JAR फ़ाइलें शामिल हैं और संस्करण दस्तावेज़ीकरण से मेल खाता है। |
| **Output file is empty** | `MyDir` एक गैर‑मौजूद फ़ोल्डर की ओर इशारा करता है | फ़ाइल लिखने से पहले प्रोग्रामेटिक रूप से डायरेक्टरी बनाएं (`Files.createDirectories(Paths.get(MyDir))`)। |
| **Compressed mesh looks distorted** | निम्न संकुचन स्तर या अपर्याप्त टेस्सेलेशन का उपयोग करना | `DracoCompressionLevel.OPTIMAL` पर स्विच करें और स्फीयर की टेस्सेलेशन बढ़ाएँ (जैसे, `new Sphere(1.0, 64, 64)`)। `DracoCompressionLevel.OPTIMAL` Draco आउटपुट के लिए सबसे उच्च संकुचन गुणवत्ता चुनता है। |

## अक्सर पूछे जाने वाले प्रश्न

**Q: क्या Aspose.3D विभिन्न 3d फ़ाइल फ़ॉर्मेट्स के साथ संगत है?**  
A: हाँ, Aspose.3D OBJ, FBX, STL, GLTF, और कई अन्य को सपोर्ट करता है, जिससे यह **Aspose 3d export** पाइपलाइन के लिए एक बहुमुखी विकल्प बनता है।

**Q: क्या मैं अन्य प्रोग्रामिंग भाषाओं में संकुचन के लिए Google Draco का उपयोग कर सकता हूँ?**  
A: बिल्कुल। Draco C++, Python, और JavaScript के लिए नेटिव लाइब्रेरीज़ प्रदान करता है। यह ट्यूटोरियल जावा पर केंद्रित है, लेकिन अवधारणाएँ सभी भाषाओं में लागू होती हैं।

**Q: अतिरिक्त Aspose.3D दस्तावेज़ीकरण कहाँ मिल सकता है?**  
A: पूर्ण API रेफ़रेंस और अधिक उदाहरणों के लिए **[Aspose.3D Java documentation](https://reference.aspose.com/3d/java/)** देखें।

**Q: Aspose.3D के लिए अस्थायी लाइसेंस कैसे प्राप्त करें?**  
A: **[Aspose temporary license page](https://purchase.aspose.com/temporary-license/)** पर अस्थायी लाइसेंस विकल्प देखें।

**Q: Aspose.3D समर्थन के लिए कोई समुदाय फ़ोरम है?**  
A: हाँ, **[Aspose.3D Forum](https://forum.aspose.com/c/3d/18)** पर चर्चा में शामिल हों।

## निष्कर्ष

इस गाइड में हमने दिखाया कि जावा में स्फीयर मेष बनाकर और फिर Aspose.3D के माध्यम से Google Draco से संकुचित करके **3d मॉडल आकार** को कैसे कम किया जाए। इन संक्षिप्त चरणों का पालन करके आप मेष फ़ाइलों को नाटकीय रूप से छोटा कर सकते हैं, लोड समय सुधार सकते हैं, और अपने जावा‑आधारित 3d एप्लिकेशन को प्रतिक्रियाशील और बैंडविड्थ‑मित्र बना सकते हैं।

---

**अंतिम अद्यतन:** 2026-11-17  
**परीक्षण किया गया:** Aspose.3D for Java 24.12 (latest)  
**लेखक:** Aspose

## संबंधित ट्यूटोरियल

- [3D फ़ाइल आकार कम करें – Aspose.3D for Java के साथ सीन संकुचित करें](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [Aspose.3D for Java का उपयोग करके स्फीयर से Draco पॉइंट क्लाउड जेनरेट करें](/3d/java/point-clouds/generate-point-clouds-spheres-java/)
- [Aspose.3D का उपयोग करके जावा में अनुकूलित रेंडरिंग के लिए मेष को त्रिकोणीय बनाने के तरीके सीखें](/3d/java/geometry/triangulate-meshes-for-optimized-rendering/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}