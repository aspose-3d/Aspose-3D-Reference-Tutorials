---
title: कस्टम लोड विकल्प
linktitle: कस्टम लोड विकल्प
second_title: Aspose.3D .NET API
description: निर्बाध 3D मॉडल लोडिंग और सेविंग के लिए .NET के लिए Aspose.3D का सर्वोत्तम समाधान खोजें।
weight: 15
url: /hi/net/loading-and-saving/custom-load-options/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# कस्टम लोड विकल्प

## परिचय

.NET के लिए Aspose.3D की दुनिया में आपका स्वागत है - एक शक्तिशाली लाइब्रेरी जो डेवलपर्स को 3D फ़ाइलों के साथ निर्बाध रूप से काम करने में सक्षम बनाती है। इस ट्यूटोरियल में, हम कस्टम लोड विकल्पों पर ध्यान केंद्रित करते हुए 3डी मॉडल को लोड करने और सहेजने की जटिलताओं पर ध्यान देंगे। चाहे आप अनुभवी डेवलपर हों या नवागंतुक, यह मार्गदर्शिका आपको चरण दर चरण प्रक्रिया के बारे में बताएगी, यह सुनिश्चित करते हुए कि आप .NET के लिए Aspose.3D की पूरी क्षमता का उपयोग करें।

## आवश्यक शर्तें

इससे पहले कि हम इस यात्रा पर निकलें, सुनिश्चित करें कि आपके पास निम्नलिखित शर्तें हैं:

-  .NET के लिए Aspose.3D: सुनिश्चित करें कि आपके पास लाइब्रेरी स्थापित है। आप इसे डाउनलोड कर सकते हैं[यहाँ](https://releases.aspose.com/3d/net/).

- दस्तावेज़ निर्देशिका: अपनी 3D मॉडल फ़ाइलों को संग्रहीत करने के लिए एक निर्देशिका बनाएं।

अब जब आपके पास आवश्यक चीजें हैं, तो आइए 3डी मॉडल हेरफेर की रोमांचक दुनिया में उतरें!

## नामस्थान आयात करें

सबसे पहली बात, आइए आवश्यक नामस्थान आयात करें। यह Aspose.3D क्षेत्र में हमारी यात्रा के लिए मंच तैयार करेगा।

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
```

## लोड करना और सहेजना - कस्टम लोड विकल्प

### चरण 1: डिस्क्रीट3डीएस फ़ाइलें लोड हो रही हैं

```csharp
private static void Discreet3DSLoadOption()
{
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();

    //कस्टम विकल्प सेट करें
    loadOpts.ApplyAnimationTransform = true;
    loadOpts.FlipCoordinateSystem = true;
    loadOpts.GammaCorrectedColor = true;
    loadOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //लोड विकल्पों के साथ फ़ाइल लोड करें
    var scene = Scene.FromFile("test.3ds", loadOpts);
}
```

### चरण 2: ओबीजे फ़ाइलें लोड हो रही हैं

```csharp
private static void ObjLoadOption()
{
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();

    //कस्टम विकल्प सेट करें
    loadObjOpts.EnableMaterials = true;
    loadObjOpts.FlipCoordinateSystem = true;
    loadObjOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //लोड विकल्पों के साथ फ़ाइल लोड करें
    var scene = Scene.FromFile("test.obj", loadObjOpts);

}
```

### चरण 3: एसटीएल फ़ाइलें लोड हो रही हैं

```csharp
private static void STLLoadOption()
{
    // दस्तावेज़ निर्देशिका का पथ.
    StlLoadOptions loadSTLOpts = new StlLoadOptions();

    //कस्टम विकल्प सेट करें
    loadSTLOpts.FlipCoordinateSystem = true;
    loadSTLOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //लोड विकल्पों के साथ फ़ाइल लोड करें
    var scene = Scene.FromFile("test.stl", loadSTLOpts);
}
```

### चरण 4: U3D फ़ाइलें लोड हो रही हैं

```csharp
private static void U3DLoadOption()
{
    // दस्तावेज़ निर्देशिका का पथ.
    string dataDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();

    //कस्टम विकल्प सेट करें
    loadU3DOpts.FlipCoordinateSystem = true;
    loadU3DOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //लोड विकल्पों के साथ फ़ाइल लोड करें
    var scene = Scene.FromFile("test.u3d", loadU3DOpts);
}
```

### चरण 5: glTF फ़ाइलें लोड हो रही हैं

```csharp
private static void glTFLoadOptions()
{
    // दस्तावेज़ निर्देशिका का पथ.
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();

    //कस्टम विकल्प सेट करें
    loadOpt.FlipTexCoordV = true;
    scene.Open("Duck.gltf", loadOpt);
}
```

### चरण 6: PLY फ़ाइलें लोड हो रही हैं

```csharp
private static void PlyLoadOptions()
{
    // दस्तावेज़ निर्देशिका का पथ.
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();

    //कस्टम विकल्प सेट करें
    loadPLYOpts.FlipCoordinateSystem = true;
    scene.Open("vase-v2.ply", loadPLYOpts);
}
```

### चरण 7: FBX फ़ाइलें लोड हो रही हैं

```csharp
private static void FBXLoadOptions()
{
    // दस्तावेज़ निर्देशिका का पथ.
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions() { KeepBuiltinGlobalSettings = true };

    //कस्टम विकल्प सेट करें
    scene.Open("test.FBX", opt);

    // एफबीएक्स फ़ाइल में ग्लोबलसेटिंग्स में परिभाषित आउटपुट गुण
    foreach (Property property in scene.RootNode.AssetInfo.Properties)
    {
        Console.WriteLine(property);
    }
}
```

## निष्कर्ष

बधाई हो! आपने .NET के लिए Aspose.3D का उपयोग करके 3D मॉडल को लोड करने और सहेजने की जटिल दुनिया में सफलतापूर्वक नेविगेट किया है। इस ट्यूटोरियल में विभिन्न फ़ाइल स्वरूपों और उनके कस्टम लोड विकल्पों को शामिल किया गया है, जो आपको 3डी संपत्तियों में आसानी से हेरफेर करने में सक्षम बनाता है।

## अक्सर पूछे जाने वाले प्रश्न

### Q1: क्या .NET के लिए Aspose.3D शुरुआती लोगों के लिए उपयुक्त है?

A1: बिल्कुल! .NET के लिए Aspose.3D एक उपयोगकर्ता-अनुकूल इंटरफ़ेस प्रदान करता है, जो इसे सभी स्तरों के डेवलपर्स के लिए सुलभ बनाता है।

### Q2: क्या मैं व्यावसायिक परियोजनाओं के लिए Aspose.3D का उपयोग कर सकता हूँ?

A2: हाँ, .NET के लिए Aspose.3D एक वाणिज्यिक लाइसेंस के साथ आता है, जो आपको इसे अपनी परियोजनाओं में उपयोग करने की अनुमति देता है।

### Q3: क्या समर्थित फ़ाइल स्वरूपों पर कोई सीमाएँ हैं?

 A3: .NET के लिए Aspose.3D OBJ, STL, FBX और अन्य सहित लोकप्रिय 3D फ़ाइल स्वरूपों की एक विस्तृत श्रृंखला का समर्थन करता है। को देखें[प्रलेखन](https://reference.aspose.com/3d/net/) एक व्यापक सूची के लिए.

### Q4: क्या कोई परीक्षण संस्करण उपलब्ध है?

A4: हाँ, आप डाउनलोड करके .NET के लिए Aspose.3D की क्षमताओं का पता लगा सकते हैं[मुफ्त परीक्षण](https://releases.aspose.com/).

### Q5: मैं .NET के लिए Aspose.3D के लिए समर्थन कहाँ से प्राप्त कर सकता हूँ?

 A5: पर जाएँ[Aspose.3D फोरम](https://forum.aspose.com/c/3d/18) सामुदायिक समर्थन और सहायता के लिए।
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
