---
title: Aspose.3D SaveOptions के साथ जावा में 3D फ़ाइल सेविंग को अनुकूलित करें
linktitle: Aspose.3D SaveOptions के साथ जावा में 3D फ़ाइल सेविंग को अनुकूलित करें
second_title: Aspose.3D जावा एपीआई
description: Aspose.3D SaveOptions के साथ जावा में 3D फ़ाइल सेविंग को अनुकूलित करना सीखें। प्रदर्शन बढ़ाएं और आउटपुट को सहजता से अनुकूलित करें।
weight: 16
url: /hi/java/load-and-save/optimize-3d-file-saving/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D SaveOptions के साथ जावा में 3D फ़ाइल सेविंग को अनुकूलित करें

## परिचय

Aspose.3D एक सुविधा संपन्न जावा लाइब्रेरी है जो डेवलपर्स को 3D मॉडल के साथ निर्बाध रूप से काम करने में सक्षम बनाती है। जब 3D फ़ाइलों को सहेजने की बात आती है, तो SaveOptions क्लास आपकी आवश्यकताओं के अनुसार आउटपुट को ठीक करने के लिए ढेर सारी सेटिंग्स प्रदान करता है। इस ट्यूटोरियल में, हम विभिन्न सेव विकल्पों का पता लगाएंगे और प्रक्रिया को अनुकूलित करने के लिए उनका लाभ कैसे उठाया जा सकता है।

## आवश्यक शर्तें

इससे पहले कि हम ट्यूटोरियल में उतरें, सुनिश्चित करें कि आपके पास निम्नलिखित आवश्यक शर्तें हैं:

-  जावा के लिए Aspose.3D: सुनिश्चित करें कि आपके जावा प्रोजेक्ट में Aspose.3D लाइब्रेरी एकीकृत है। आप इसे डाउनलोड कर सकते हैं[यहाँ](https://releases.aspose.com/3d/java/).

- जावा विकास पर्यावरण: अपनी मशीन पर एक कार्यात्मक जावा विकास वातावरण स्थापित करें।

- दस्तावेज़ निर्देशिका: एक निर्देशिका बनाएं जहां आप अपनी 3D फ़ाइलें सहेजना चाहते हैं और बाद में उपयोग के लिए उसका पथ नोट करें।

## पैकेज आयात करें

 अपने जावा प्रोजेक्ट में, Aspose.3D के साथ काम करने के लिए आवश्यक पैकेज आयात करें। इसमें शामिल है`Scene` कक्षा और विभिन्न SaveOptions कक्षाएं। नीचे एक बुनियादी उदाहरण है:

```java
import com.aspose.threed.*;


import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

अब, आइए अलग-अलग SaveOptions के उपयोग को प्रदर्शित करने के लिए प्रत्येक उदाहरण को कई चरणों में विभाजित करें।

## चरण 1: जीएलटीएफ सेवऑप्शन में प्रिटी प्रिंट

`prettyPrintInGltfSaveOption` विधि आपको मानव पठनीयता के लिए इंडेंटेड JSON सामग्री के साथ एक GLTF फ़ाइल उत्पन्न करने की अनुमति देती है।

```java
public static void prettyPrintInGltfSaveOption() throws IOException {
    // 3D दृश्य आरंभ करें
    Scene scene = new Scene(new Sphere());
    
    // GLTFSaveOptions आरंभ करें
    GltfSaveOptions opt = new GltfSaveOptions(FileFormat.GLTF2);
    
    // बेहतर पठनीयता के लिए सुंदर प्रिंट सक्षम करें
    opt.setPrettyPrint(true);
    
    // 3D दृश्य सहेजें
    scene.save("Your Document Directory" + "prettyPrintInGltfSaveOption.gltf", opt);
}
```

## चरण 2: HTML5 सेवऑप्शन

`html5SaveOption` विधि दर्शाती है कि अनुकूलन विकल्पों सहित एक 3D दृश्य को HTML5 फ़ाइल के रूप में कैसे सहेजा जाए।

```java
public static void html5SaveOption() throws IOException {
    // एक दृश्य आरंभ करें
    Scene scene = new Scene();
    
    // सिलेंडर के साथ एक चाइल्ड नोड बनाएं
    Node node = scene.getRootNode().createChildNode(new Cylinder());
    
    //चाइल्ड नोड के लिए गुण सेट करें
    LambertMaterial mat = new LambertMaterial();
    mat.setDiffuseColor(new Vector3(0.34, 0.59, 0.41));
    node.setMaterial(mat);
    
    // दृश्य में प्रकाश जोड़ें
    Light light = new Light();
    light.setLightType(LightType.POINT);
    scene.getRootNode().createChildNode(light).getTransform().setTranslation(10, 0, 10);
    
    // HTML5SaveOptions आरंभ करें
    Html5SaveOptions opt = new Html5SaveOptions();
    
    // विकल्पों को अनुकूलित करें (उदाहरण के लिए, ग्रिड और उपयोगकर्ता इंटरफ़ेस बंद करें)
    opt.setShowGrid(false);
    opt.setShowUI(false);
    
    // दृश्य को HTML5 फ़ाइल के रूप में सहेजें
    scene.save("Your Document Directory" + "html5SaveOption.html", FileFormat.HTML5);
}
```

 अन्य SaveOptions विधियों के लिए समान ब्रेकडाउन जारी रखें जैसे`colladaSaveOption`, `discreet3DSSaveOption`, `fbxSaveOption`, `objSaveOption`, `STLSaveOption`, `U3DSaveOption`, `glTFSaveOptions` , और`drcSaveOptions`.

## निष्कर्ष

इस व्यापक ट्यूटोरियल का अनुसरण करके, आपने सीखा है कि Aspose.3D SaveOptions का उपयोग करके जावा में 3D फ़ाइल सेविंग को कैसे अनुकूलित किया जाए। चाहे आप जीएलटीएफ फ़ाइलों को सुंदर ढंग से प्रिंट करने में रुचि रखते हों या HTML5 आउटपुट को कस्टमाइज़ करने में रुचि रखते हों, Aspose.3D आपको अपने 3D ग्राफ़िक्स वर्कफ़्लो को बढ़ाने के लिए टूल से लैस करता है।

## अक्सर पूछे जाने वाले प्रश्न

### Q1: मैं glTF फ़ाइल में संपत्तियों को कैसे एम्बेड कर सकता हूँ?

 A1: संपत्तियों को एम्बेड करने के लिए, का उपयोग करें`setEmbedAssets(true)` विधि में`GltfSaveOptions` कक्षा।

###  Q2: का उद्देश्य क्या है`setPositionBits` method in `DracoSaveOptions`?

 ए2: द`setPositionBits` विधि ड्रेको संपीड़न एल्गोरिदम में स्थिति के लिए परिमाणीकरण बिट्स सेट करती है।

### Q3: क्या मैं U3D फ़ाइल में सामान्य डेटा निर्यात कर सकता हूँ?

 A3: हाँ, आप सेटिंग करके सामान्य डेटा निर्यात कर सकते हैं`setExportNormals(true)` में`U3dSaveOptions` कक्षा।

### Q4: मैं OBJ निर्यात में सहेजी गई सामग्री फ़ाइलों को कैसे त्याग सकता हूँ?

A4: का उपयोग करें`setFileSystem(new DummyFileSystem())` विधि में`ObjSaveOptions` सामग्री फ़ाइलों को त्यागने के लिए कक्षा।

### Q5: क्या OBJ फ़ाइल में निर्भरता को स्थानीय निर्देशिका में सहेजने का कोई तरीका है?

 A5: हाँ, उपयोग करें`setFileSystem(new LocalFileSystem(MyDir))` विधि में`ObjSaveOptions` स्थानीय स्तर पर निर्भरता को बचाने के लिए वर्ग।
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
