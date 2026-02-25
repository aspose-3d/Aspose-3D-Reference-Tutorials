---
date: 2026-02-25
description: जावा में Aspose.3D LoadOptions का उपयोग करके कोऑर्डिनेट सिस्टम को उलटने
  और 3D इम्पोर्ट को कस्टमाइज़ करना सीखें। 3DS, OBJ, STL, U3D, glTF, PLY, X और वैकल्पिक
  FBX के लिए चरण‑दर‑चरण गाइड।
linktitle: Customize 3D File Loading in Java with Aspose.3D LoadOptions
second_title: Aspose.3D Java API
title: कोऑर्डिनेट सिस्टम को उलटें – जावा में Aspose.3D के साथ 3D फ़ाइल लोडिंग को कस्टमाइज़
  करें
url: /hi/java/load-and-save/customize-3d-file-loading/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Flip Coordinate System – जावा में Aspose.3D के साथ 3D फ़ाइल लोडिंग को कस्टमाइज़ करें

3D डिज़ाइन और विकास के निरंतर विकसित होते परिदृश्य में, मॉडल आयात करते समय **flipping the coordinate system** एक सामान्य आवश्यकता है। चाहे आप एसेट्स को राइट‑हैंडेड से लेफ़्ट‑हैंडेड सिस्टम में बदल रहे हों या अपने इंजन की एक्सिस परम्पराओं के साथ मॉडल को संरेखित करने की आवश्यकता हो, Aspose.3D for Java आपको सूक्ष्म नियंत्रण प्रदान करता है। यह ट्यूटोरियल आपको Aspose.3D के `LoadOptions` का उपयोग करके **customize 3D import** करने की प्रक्रिया दिखाता है, जिसमें 3DS, OBJ, STL, U3D, glTF, PLY, X और वैकल्पिक FBX जैसे सबसे लोकप्रिय फॉर्मेट शामिल हैं।

## त्वरित उत्तर
- **“flip coordinate system” क्या करता है?** यह X/Y/Z अक्षों को लक्ष्य कोऑर्डिनेट परम्परा के अनुसार बदल देता है।  
- **कौन से फॉर्मेट फ्लिपिंग का समर्थन करते हैं?** सभी प्रमुख फॉर्मेट (3DS, OBJ, STL, U3D, glTF, PLY, X, FBX) `setFlipCoordinateSystem` विकल्प प्रदान करते हैं।  
- **क्या मुझे अतिरिक्त लाइब्रेरीज़ की जरूरत है?** केवल Aspose.3D for Java JAR; कोई बाहरी कन्वर्टर आवश्यक नहीं है।  
- **क्या मैं साथ ही मैटीरियल लोड कर सकता हूँ?** हाँ—OBJ फ़ाइलों के लिए `setEnableMaterials(true)` उपयोग करें।  
- **प्रोडक्शन के लिए लाइसेंस आवश्यक है?** गैर‑ट्रायल डिप्लॉयमेंट के लिए वैध Aspose.3D लाइसेंस आवश्यक है।

## “flip coordinate system” क्या है?
Flipping the coordinate system आयात किए गए मॉडल द्वारा उपयोग किए जाने वाले अक्षों की अभिविन्यास को बदलता है। यह तब आवश्यक होता है जब स्रोत फ़ाइल आपके रेंडरिंग इंजन से अलग हैंडेडनेस (right‑handed vs. left‑handed) का उपयोग करती है, जिससे मॉडल प्रतिबिंबित या उलटा दिखने से बचा जा सके।

## 3D आयात को कस्टमाइज़ क्यों करें?
- एनीमेशन ट्रांसफ़ॉर्म को संरक्षित रखें (`setApplyAnimationTransform`)।  
- रंग हैंडलिंग को सही करें (`setGammaCorrectedColor`)।  
- `getLookupPaths()` के माध्यम से बाहरी संसाधन पथों को हल करें।  
- केवल आवश्यक चीज़ें लोड करके मेमोरी उपयोग को अनुकूलित करें।

## पूर्वापेक्षाएँ
- जावा प्रोग्रामिंग की बुनियादी समझ।  
- स्थापित Java Development Kit (JDK)।  
- Aspose.3D for Java लाइब्रेरी डाउनलोड की गई। आप इसे [यहाँ](https://releases.aspose.com/3d/java/) प्राप्त कर सकते हैं।  
- 3DS, OBJ, STL, U3D, glTF, PLY, X, और FBX जैसे 3D फ़ाइल फॉर्मेट की परिचितता।

## पैकेज आयात करें

अपने जावा प्रोजेक्ट में, आवश्यक Aspose.3D पैकेज आयात करना सुनिश्चित करें:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## LoadOptions के साथ 3D आयात को कैसे कस्टमाइज़ करें

नीचे चरण‑दर‑चरण कोड स्निपेट्स दिए गए हैं जो प्रत्येक समर्थित फॉर्मेट के लिए **flip coordinate system** विकल्प को सक्षम करने का प्रदर्शन करते हैं। ये स्निपेट्स आपके प्रोजेक्ट में कॉपी करने के लिए तैयार हैं; केवल `"Your Document Directory"` को अपने एसेट्स के वास्तविक पथ से बदलें।

### चरण 1: 3DS फ़ाइल लोडिंग को कस्टमाइज़ करें

```java
public static void discreet3DSLoadOption() {
    String MyDir = "Your Document Directory";
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();
    loadOpts.setApplyAnimationTransform(true);
    loadOpts.setFlipCoordinateSystem(true);
    loadOpts.setGammaCorrectedColor(true);
    loadOpts.getLookupPaths().add(MyDir);
}
```

### चरण 2: OBJ फ़ाइल लोडिंग को कस्टमाइज़ करें

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### चरण 3: STL फ़ाइल लोडिंग को कस्टमाइज़ करें

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### चरण 4: U3D फ़ाइल लोडिंग को कस्टमाइज़ करें

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### चरण 5: glTF फ़ाइल लोडिंग को कस्टमाइज़ करें

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### चरण 6: PLY फ़ाइल लोडिंग को कस्टमाइज़ करें

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### चरण 7: X फ़ाइल लोडिंग को कस्टमाइज़ करें

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### चरण 8: FBX फ़ाइल लोडिंग को कस्टमाइज़ करें (वैकल्पिक)

```java
private static void FBXLoadOptions() throws IOException {
    String dataDir = "Your Document Directory";
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions();
    opt.setKeepBuiltinGlobalSettings(true);
    scene.open(dataDir + "test.FBX", opt);
    for(Property property:scene.getRootNode().getAssetInfo().getProperties()) {
        System.out.println(property);
    }
}
```

## सामान्य समस्याएँ और समाधान
- **लोड करने के बाद मॉडल प्रतिबिंबित दिखता है** – सुनिश्चित करें कि सही फॉर्मेट के लिए `setFlipCoordinateSystem(true)` सेट किया गया है।  
- **मैटीरियल गायब हैं** – OBJ फ़ाइलों के लिए, `setEnableMaterials(true)` सुनिश्चित करें और यह कि मैटीरियल फ़ाइलें (.mtl) लुकअप पाथ में से किसी एक में स्थित हों।  
- **टेक्सचर कोऑर्डिनेट उल्टे हैं** – glTF के लिए, अक्षों को उलटने के अलावा `setFlipTexCoordV(true)` की आवश्यकता हो सकती है।  
- **फ़ाइल नहीं मिली त्रुटियाँ** – बाहरी संसाधनों (टेक्सचर, सहायक फ़ाइलें) वाले डायरेक्टरी को `loadOpts.getLookupPaths()` में जोड़ें।

## निष्कर्ष

Aspose.3D के `LoadOptions` का उपयोग करके आप लगभग सभी प्रमुख फॉर्मेट के लिए **flip coordinate system** और **customize 3D import** कर सकते हैं। यह नियंत्रण स्तर पोस्ट‑प्रोसेसिंग स्क्रिप्ट्स की आवश्यकता को समाप्त करता है और सुनिश्चित करता है कि आपके एसेट्स पहली बार में ही सही ढंग से रेंडर हों।

## अक्सर पूछे जाने वाले प्रश्न

### Q1: Aspose.3D for Java दस्तावेज़ीकरण कहाँ मिल सकता है?
A1: दस्तावेज़ीकरण [यहाँ](https://reference.aspose.com/3d/java/) उपलब्ध है।

### Q2: मैं Aspose.3D for Java को कैसे डाउनलोड कर सकता हूँ?
A2: आप इसे [यहाँ](https://releases.aspose.com/3d/java/) डाउनलोड कर सकते हैं।

### Q3: क्या कोई मुफ्त ट्रायल उपलब्ध है?
A3: हाँ, आप मुफ्त ट्रायल [यहाँ](https://releases.aspose.com/) तक पहुँच सकते हैं।

### Q4: Aspose.3D for Java के लिए समर्थन कहाँ प्राप्त कर सकता हूँ?
A4: समर्थन फ़ोरम [यहाँ](https://forum.aspose.com/c/3d/18) देखें।

### Q5: परीक्षण के लिए क्या मुझे अस्थायी लाइसेंस चाहिए?
A5: हाँ, अस्थायी लाइसेंस [यहाँ](https://purchase.aspose.com/temporary-license/) प्राप्त करें।

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**अंतिम अपडेट:** 2026-02-25  
**परीक्षण किया गया:** Aspose.3D for Java 24.11 (latest)  
**लेखक:** Aspose