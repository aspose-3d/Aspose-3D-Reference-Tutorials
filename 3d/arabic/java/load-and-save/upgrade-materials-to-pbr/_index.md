---
title: قم بترقية المواد ثلاثية الأبعاد إلى PBR لتعزيز الواقعية في Java باستخدام Aspose.3D
linktitle: قم بترقية المواد ثلاثية الأبعاد إلى PBR لتعزيز الواقعية في Java باستخدام Aspose.3D
second_title: Aspose.3D جافا API
description: قم بترقية المواد ثلاثية الأبعاد إلى PBR بسهولة في Java باستخدام Aspose.3D. تحقيق الواقعية المحسنة لمرئيات آسرة.
type: docs
weight: 13
url: /ar/java/load-and-save/upgrade-materials-to-pbr/
---
## مقدمة

تعد ترقية المواد ثلاثية الأبعاد الخاصة بك إلى PBR خطوة تحويلية نحو تحقيق مرئيات نابضة بالحياة في تطبيقات Java الخاصة بك. يعمل Aspose.3D على تبسيط هذه العملية، مما يسمح لك بالانتقال بسلاسة من المواد التقليدية إلى مواد PBR. في هذا البرنامج التعليمي، سوف نستكشف المتطلبات الأساسية الضرورية، ونستورد الحزم، ونقسم كل مثال إلى خطوات تفصيلية.

## المتطلبات الأساسية

قبل الغوص في البرنامج التعليمي، تأكد من أن لديك المتطلبات الأساسية التالية:

1.  Aspose.3D لـ Java: قم بتنزيل وتثبيت مكتبة Aspose.3D من[صفحة الإصدار](https://releases.aspose.com/3d/java/).

2. بيئة تطوير Java: تأكد من إعداد بيئة تطوير Java على جهازك.

3. دليل المستندات: قم بإنشاء دليل مخصص لمستنداتك ثلاثية الأبعاد.

## حزم الاستيراد

لبدء عملية الترقية، قم باستيراد الحزم المطلوبة إلى مشروع Java الخاص بك. استخدم مقتطف الشفرة التالي كدليل:

```java
import com.aspose.threed.*;
```

تأكد من تضمين جميع حزم Aspose.3D الضرورية للاستفادة من وظائفها بسلاسة.

## الخطوة 1: تهيئة مشهد ثلاثي الأبعاد جديد

ابدأ بتهيئة مشهد ثلاثي الأبعاد جديد باستخدام الكود التالي:

```java
// ExStart: تهيئة المشهد
String MyDir = "Your Document Directory";
Scene s = new Scene();
// ExEnd: تهيئة المشهد
```

## الخطوة 2: إنشاء صندوق باستخدام PhongMaterial

قم بإنشاء مربع ثلاثي الأبعاد وقم بتعيين مادة PhongMaterial إليه:

```java
// ExStart:CreateBoxWithMaterial
Box box = new Box();
PhongMaterial mat = new PhongMaterial();
mat.setDiffuseColor(new Vector3(1, 0, 1));
s.getRootNode().createChildNode("box1", box).setMaterial(mat);
// ExEnd:CreateBoxWithMaterial
```

## الخطوة 3: احفظ بتنسيق GLTF 2.0

احفظ المشهد بتنسيق GLTF 2.0، وقم بتحويل PhongMaterial إلى PBRMaterial أثناء العملية:

```java
// ExStart:SaveInGLTF
GltfSaveOptions opt = new GltfSaveOptions(FileFormat.GLTF2);
opt.setMaterialConverter(new MaterialConverter() {
    @Override
    public Material call(Material material) {
        PhongMaterial m = (PhongMaterial) material;
        PbrMaterial ret = new PbrMaterial();
        ret.setAlbedo(m.getDiffuseColor());
        return ret;
    }
});
s.save(MyDir + "Non_PBRtoPBRMaterial_Out.gltf", opt);
// ExEnd:SaveInGLTF
```

اتبع هذه الخطوات بدقة لترقية المواد ثلاثية الأبعاد الخاصة بك بسلاسة إلى PBR، مما يعزز الواقعية في تطبيقات Java.

## خاتمة

في الختام، يمكّنك Aspose.3D for Java من رفع المظهر المرئي لرسوماتك ثلاثية الأبعاد عن طريق ترقية المواد إلى PBR. احتضن هذه التقنية لتحقيق الواقعية المحسنة وجذب انتباه جمهورك من خلال تطبيقات Java المذهلة بصريًا.

## الأسئلة الشائعة

### س1: هل Aspose.3D متوافق مع بيئات تطوير Java بخلاف Eclipse؟

ج1: نعم، Aspose.3D متوافق مع بيئات تطوير Java المتنوعة.

### س2: هل يمكنني استخدام Aspose.3D للمشاريع التجارية؟

 ج2: نعم، يمكنك استخدام Aspose.3D لكل من المشاريع الشخصية والتجارية. قم بزيارة[صفحة الشراء](https://purchase.aspose.com/buy) للحصول على تفاصيل الترخيص.

### س3: هل هناك نسخة تجريبية مجانية متاحة؟

ج3: نعم، يمكنك الوصول إلى النسخة التجريبية المجانية[هنا](https://releases.aspose.com/).

### س4: أين يمكنني العثور على الدعم لـ Aspose.3D؟

 ج4: اكتشف[منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) لدعم المجتمع.

### س5: كيف يمكنني الحصول على ترخيص مؤقت لـ Aspose.3D؟

 ج5: زيارة[هذا الرابط](https://purchase.aspose.com/temporary-license/) للحصول على معلومات الترخيص المؤقت.