---
title: कैंसिलेशनटोकन का उपयोग करना
linktitle: कैंसिलेशनटोकन का उपयोग करना
second_title: Aspose.3D .NET API
description: .NET के लिए Aspose.3D के साथ 3D मॉडलिंग की निर्बाध दुनिया का अन्वेषण करें। कैंसिलेशनटोकन का उपयोग करके 3डी दस्तावेज़ों को कुशलतापूर्वक लोड करना और सहेजना सीखें।
weight: 10
url: /hi/net/loading-and-saving/cancellation-token/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# कैंसिलेशनटोकन का उपयोग करना

## परिचय

आपके 3D मॉडलिंग और रेंडरिंग प्रोजेक्ट को बेहतर बनाने के लिए .NET के लिए Aspose.3D का उपयोग करने पर हमारी व्यापक मार्गदर्शिका में आपका स्वागत है। Aspose.3D एक शक्तिशाली लाइब्रेरी है जो .NET डेवलपर्स को 3D फ़ाइलों के साथ निर्बाध रूप से काम करने में सक्षम बनाती है। इस ट्यूटोरियल में, हम लोडिंग और सेविंग पहलुओं पर ध्यान देंगे, विशेष रूप से एसिंक्रोनस कार्यों के कुशल प्रबंधन के लिए कैंसिलेशनटोकन के उपयोग पर ध्यान केंद्रित करेंगे।

## आवश्यक शर्तें

इससे पहले कि हम इस यात्रा पर निकलें, सुनिश्चित करें कि आपके पास निम्नलिखित शर्तें हैं:

-  .NET के लिए Aspose.3D: यहां से लाइब्रेरी डाउनलोड और इंस्टॉल करें[यहाँ](https://releases.aspose.com/3d/net/).
- .NET वातावरण: सुनिश्चित करें कि आपके पास एक संगत .NET विकास वातावरण स्थापित है।
- C# की बुनियादी समझ: C# प्रोग्रामिंग भाषा से परिचित होने की अनुशंसा की जाती है।

## नामस्थान आयात करें

आरंभ करने के लिए, सुनिश्चित करें कि आपने अपने प्रोजेक्ट में आवश्यक नामस्थान शामिल किए हैं। ये नामस्थान 3डी फ़ाइल हेरफेर के लिए आवश्यक कार्यात्मकताओं तक पहुंच प्रदान करेंगे।

```csharp
using Aspose.ThreeD;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
```

## लोड करना और सहेजना - कैंसिलेशनटोकन का उपयोग करना

### चरण 1: कैंसिलेशनटोकनसोर्स बनाएं

```csharp
// एक्सस्टार्ट: कैंसिलेशनटोकनसोर्स

CancellationTokenSource cts = new CancellationTokenSource();
```

यहां, हम कैंसिलेशनटोकनसोर्स को इंस्टेंट करते हैं, जो एसिंक्रोनस ऑपरेशंस में कैंसिलेशन को प्रबंधित करने के लिए एक महत्वपूर्ण घटक है।

### चरण 2: 3डी दृश्य प्रारंभ करें

```csharp
Scene scene = new Scene();
```

दृश्य वर्ग का एक उदाहरण बनाएँ। यह आपकी 3डी मॉडलिंग गतिविधियों के लिए कैनवास होगा।

### चरण 3: कैंसिलेशनटोकन टाइमआउट सेट करें

```csharp
cts.CancelAfter(1000);
```

 का उपयोग करके रद्दीकरण समय-सीमा निर्धारित करें`CancelAfter` तरीका। इस उदाहरण में, टाइमआउट 1000 मिलीसेकंड (1 सेकंड) पर सेट है।

### चरण 4: 3D दस्तावेज़ खोलें

```csharp
try
{
    scene.Open("Your Output Directory" + "document.fbx", cts.Token);
    Console.WriteLine("Import is done within 1000ms");
}
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
```

 3डी दस्तावेज़ को निर्दिष्ट समय सीमा के भीतर खोलने का प्रयास करें।`cts.Token` पैरामीटर यह सुनिश्चित करता है कि निर्धारित समयबाह्य से अधिक होने पर ऑपरेशन रद्द किया जा सकता है।

### चरण 5: आयात अपवाद को संभालें

किसी आयात अपवाद के मामले में, यह जाँच कर कि क्या यह किसी ऑपरेशनकैंसल्ड अपवाद के कारण हुआ है, इसे शालीनता से संभालें।

```csharp
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
// ExEnd:रद्दीकरणटोकनस्रोत
```

## निष्कर्ष

बधाई हो! आपने 3D दस्तावेज़ों की लोडिंग को प्रबंधित करने के लिए CancelationToken के साथ .NET के लिए Aspose.3D का उपयोग करने की प्रक्रिया को सफलतापूर्वक पार कर लिया है। यह तकनीक आपके 3डी अनुप्रयोगों के समग्र प्रदर्शन को बढ़ाते हुए कुशल और समय पर आयात संचालन सुनिश्चित करती है।

## अक्सर पूछे जाने वाले प्रश्न

### Q1: क्या Aspose.3D सभी 3D फ़ाइल स्वरूपों के साथ संगत है?

 A1: Aspose.3D FBX, STL, OBJ और अन्य सहित 3D फ़ाइल स्वरूपों की एक विस्तृत श्रृंखला का समर्थन करता है। को देखें[प्रलेखन](https://reference.aspose.com/3d/net/) पूरी सूची के लिए.

### Q2: मैं Aspose.3D के लिए अस्थायी लाइसेंस कैसे प्राप्त कर सकता हूं?

 A2: विजिट करके अस्थायी लाइसेंस प्राप्त करें[इस लिंक](https://purchase.aspose.com/temporary-license/).

### Q3: मुझे Aspose.3D के लिए समर्थन कहां मिल सकता है?

 A3: सामुदायिक चर्चा में शामिल हों[Aspose.3D फोरम](https://forum.aspose.com/c/3d/18).

### Q4: क्या मैं खरीदने से पहले Aspose.3D को निःशुल्क आज़मा सकता हूँ?

 उ4: हां, नि:शुल्क परीक्षण के साथ सुविधाओं का पता लगाएं[यहाँ](https://releases.aspose.com/).

### Q5: .NET के लिए Aspose.3D का नवीनतम संस्करण क्या है?

 A5: जाँच करके अद्यतित रहें[डाउनलोड पेज](https://releases.aspose.com/3d/net/) नवीनतम रिलीज़ के लिए.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
