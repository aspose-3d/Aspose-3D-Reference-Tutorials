---
date: 2025-12-18
description: Aspose.3D का उपयोग करके जावा में आकार को एक्सट्रूड करना, 3D सीन बनाना,
  और वेवफ्रंट OBJ फ़ाइलों को आसानी से निर्यात करना सीखें।
linktitle: How to Extrude Shape in Java with Aspose.3D Linear Extrusion
second_title: Aspose.3D Java API
title: जावा में Aspose.3D के साथ लीनियर एक्सट्रूज़न द्वारा आकार को कैसे एक्सट्रूड
  करें
url: /hi/java/linear-extrusion/performing-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for Java में रैखिक एक्सट्रूज़न करना

## परिचय

Aspose.3D for Java में **how to extrude shape** पर इस व्यापक ट्यूटोरियल में आपका स्वागत है! यदि आप Java का उपयोग करके अपने 3D मॉडलिंग कौशल को बढ़ाना चाहते हैं, तो आप सही जगह पर हैं। हम आपको 3D सीन बनाने, रैखिक एक्सट्रूज़न करने, और परिणाम को Wavefront OBJ फ़ाइल के रूप में निर्यात करने की प्रक्रिया दिखाएंगे—सभी स्पष्ट, चरण‑दर‑चरण कोड उदाहरणों के साथ।

## त्वरित उत्तर
- **What is linear extrusion?** एक 2D प्रोफ़ाइल को सीधी रेखा के साथ विस्तारित करके 3D ठोस बनाना।  
- **Which library handles this in Java?** Aspose.3D for Java.  
- **Can I export to OBJ?** हाँ, Wavefront OBJ निर्यात सुविधा का उपयोग करके।  
- **Do I need a license for development?** परीक्षण के लिए एक मुफ्त ट्रायल काम करता है; उत्पादन के लिए लाइसेंस आवश्यक है।  
- **What Java version is required?** Java 1.6 या बाद का।

## “how to extrude shape” क्या है?

Linear extrusion **3d modeling java** में एक बुनियादी तकनीक है जो एक सपाट प्रोफ़ाइल—जैसे आयत—को एक निर्धारित दूरी तक खींचकर एक आयतनात्मक वस्तु में बदल देती है। यह विधि यांत्रिक भागों, वास्तु तत्वों, और सजावटी मॉडलों के निर्माण में व्यापक रूप से उपयोग की जाती है।

## रैखिक एक्सट्रूज़न के लिए Aspose.3D का उपयोग क्यों करें?

- **Full control** ज्यामिति (स्लाइस, ट्विस्ट, ऑफ़सेट) पर।  
- **Seamless integration** Java प्रोजेक्ट्स के साथ—कोई नेटिव निर्भरताएँ नहीं।  
- **Built‑in exporters** लोकप्रिय फॉर्मैट्स के लिए, जिसमें Wavefront OBJ शामिल है, जिससे **generate 3d model** फ़ाइलें डाउनस्ट्रीम पाइपलाइन के लिए बनाना आसान हो जाता है।

## पूर्वापेक्षाएँ

ट्यूटोरियल में डुबकी लगाने से पहले, सुनिश्चित करें कि आपके पास निम्नलिखित पूर्वापेक्षाएँ मौजूद हैं:

1. **Java Development Environment** – एक JDK (1.6 या नया) और आपका पसंदीदा IDE।  
2. **Aspose.3D Library** – आधिकारिक साइट से लाइब्रेरी डाउनलोड और इंस्टॉल करें **[here](https://releases.aspose.com/3d/java/)**।

## पैकेज आयात करें

एक बार जब आप अपना विकास वातावरण सेट कर लेते हैं और Aspose.3D लाइब्रेरी इंस्टॉल कर लेते हैं, तो आवश्यक पैकेज आयात करें:

```java
import com.aspose.threed.*;
```

### चरण 1: दस्तावेज़ डायरेक्टरी सेट करें

परिभाषित करें कि उत्पन्न फ़ाइलें किस फ़ोल्डर में सहेजी जाएँगी:

```java
String MyDir = "Your Document Directory";
```

> यह सुनिश्चित करता है कि **generate 3d model** ऑपरेशन OBJ फ़ाइल को एक ज्ञात स्थान पर लिखे।

### चरण 2: बेस आकार प्रारंभ करें

एक आयत बनाएँ जो एक्सट्रूज़न प्रोफ़ाइल के रूप में कार्य करेगा:

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

आप गोल कोनों के लिए राउंडिंग रेडियस समायोजित कर सकते हैं या परिपूर्ण आयत के लिए इसे `0` सेट कर सकते हैं।

### चरण 3: रैखिक एक्सट्रूज़न करें

अब हम आयत को Z‑axis के साथ एक्सट्रूड करते हैं, स्लाइस जोड़ते हैं, सेंटरिंग सक्षम करते हैं, और ऑफ़सेट के साथ एक ट्विस्ट लागू करते हैं:

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

- **Extrusion length** – `10` इकाइयाँ।  
- **Slices** – स्मूथ ज्यामिति के लिए `100`।  
- **Twist** – `360°` पूर्ण घूर्णन बनाता है।  
- **Twist offset** – ट्विस्ट मूल बिंदु को `(10, 0, 0)` पर ले जाता है।

### चरण 4: 3D सीन बनाएं

एक सीन कंटेनर बनाएँ और एक्सट्रूज़न को एक चाइल्ड नोड के रूप में जोड़ें। यह चरण **creates 3d scene** प्रदान करता है जो कई वस्तुओं को रख सकता है:

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

### चरण 5: 3D सीन सहेजें

सीन को Wavefront OBJ फ़ाइल में निर्यात करें। यह **wavefront obj export** और **save 3d obj** क्षमताओं को दर्शाता है:

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

कोड चलाने के बाद, आप निर्दिष्ट डायरेक्टरी में `LinearExtrusion.obj` पाएँगे, जो किसी भी 3D व्यूअर में खोलने या आगे प्रोसेस करने के लिए तैयार है।

## सामान्य समस्याएँ और समाधान

| समस्या | कारण | समाधान |
|-------|--------|-----|
| OBJ file is empty | Output directory path is incorrect or not writable | Verify `MyDir` points to an existing folder with write permissions. |
| Twist not applied | `setCenter(true)` omitted | Ensure centering is enabled or adjust `setTwistOffset` values. |
| Compilation error on `LinearExtrusion` | Using an older Aspose.3D version | Update to the latest Aspose.3D release. |

## अक्सर पूछे जाने वाले प्रश्न

**Q: क्या Aspose.3D सभी Java संस्करणों के साथ संगत है?**  
A: Aspose.3D Java 1.6 और बाद के संस्करणों के साथ काम करता है।

**Q: क्या मैं Aspose.3D को वाणिज्यिक प्रोजेक्ट्स के लिए उपयोग कर सकता हूँ?**  
A: हाँ, वैध लाइसेंस के साथ वाणिज्यिक उपयोग की अनुमति है। आप इसे **[here](https://purchase.aspose.com/buy)** से प्राप्त कर सकते हैं।

**Q: यदि मुझे समस्याएँ आती हैं तो मैं समर्थन कहाँ से प्राप्त कर सकता हूँ?**  
A: समुदाय सहायता के लिए **[Aspose.3D forum](https://forum.aspose.com/c/3d/18)** पर जाएँ या प्रीमियम समर्थन के लिए **[temporary license](https://purchase.aspose.com/temporary-license/)** खरीदें।

**Q: Aspose.3D कौन-कौन सी अन्य 3D मॉडलिंग सुविधाएँ प्रदान करता है?**  
A: लाइब्रेरी में मेष (mesh) हेरफेर, बूलियन ऑपरेशन्स, टेक्सचर मैपिंग, और अधिक शामिल हैं। पूरी सूची **[here](https://reference.aspose.com/3d/java/)** देखें।

**Q: क्या कोई मुफ्त ट्रायल उपलब्ध है?**  
A: हाँ, आप ट्रायल संस्करण **[here](https://releases.aspose.com/)** से डाउनलोड कर सकते हैं।

## निष्कर्ष

आपने अब Aspose.3D for Java का उपयोग करके **how to extrude shape** सीख लिया है, एक 3D सीन बनाया है, और परिणाम को Wavefront OBJ फ़ाइल के रूप में निर्यात किया है। यह तकनीक **3d modeling java** प्रोजेक्ट्स की एक विस्तृत श्रृंखला—सरल भागों से लेकर जटिल असेंबली तक—के लिए द्वार खोलती है। अपने मॉडलों को और समृद्ध करने के लिए बूलियन ऑपरेशन्स या टेक्सचर मैपिंग जैसी अतिरिक्त सुविधाओं का अन्वेषण करें।

---

**अंतिम अद्यतन:** 2025-12-18  
**परीक्षण किया गया:** Aspose.3D 24.11 for Java  
**लेखक:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}