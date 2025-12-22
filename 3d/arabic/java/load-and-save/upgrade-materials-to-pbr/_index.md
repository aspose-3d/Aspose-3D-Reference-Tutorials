---
date: 2025-12-22
description: تعلم كيفية تصدير المشهد إلى glTF في Java باستخدام Aspose.3D مع ترقية
  المواد ثلاثية الأبعاد إلى PBR لتحقيق واقعية محسنة.
linktitle: Export Scene to glTF in Java with Aspose.3D
second_title: Upgrade 3D Materials to PBR
title: تصدير المشهد إلى glTF في جافا باستخدام Aspose.3D
url: /ar/java/load-and-save/upgrade-materials-to-pbr/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# تصدير المشهد إلى glTF في Java باستخدام Aspose.3D – ترقية المواد إلى PBR

## Introduction

في هذا الدرس ستتعلم كيفية **تصدير المشهد إلى glTF** في Java باستخدام Aspose.3D مع ترقية موادك ثلاثية الأبعاد إلى تقنية الإضاءة الفيزيائية (PBR). ترقية المواد إلى PBR تمنح نماذجك مظهرًا أكثر واقعية، وتصديرها إلى تنسيق glTF 2.0 المدعوم على نطاق واسع يتيح لك مشاركة هذه الأصول عالية الجودة عبر المحركات، المتصفحات، ومنصات AR/VR. سنستعرض المتطلبات المسبقة، نستورد الحزم الضرورية، ونفصل كل مثال خطوة بخطوة لتتمكن من تطبيق التقنية في مشاريعك الخاصة.

## Quick Answers
- **ما معنى “export scene to glTF”؟** يقوم بتحويل مشهد Aspose.3D إلى تنسيق ملف glTF 2.0 مع الحفاظ على الهندسة، المواد، والهيكل الهرمي.  
- **لماذا يتم ترقية المواد إلى PBR أولاً؟** مواد PBR تتطابق مباشرة مع سير عمل metallic‑roughness في glTF، مما يوفر إضاءة واقعية دون خطوات تحويل إضافية.  
- **هل أحتاج إلى ترخيص لتشغيل الكود؟** النسخة التجريبية المجانية تكفي للتطوير؛ يلزم الحصول على ترخيص تجاري للإنتاج.  
- **ما هي بيئات تطوير Java المدعومة؟** أي بيئة تطوير يمكنها تجميع Java (Eclipse، IntelliJ IDEA، VS Code، إلخ).  
- **هل يمكنني تصدير مشاهد كبيرة؟** نعم، Aspose.3D يبث البيانات بكفاءة؛ فقط تأكد من توفر ذاكرة heap كافية للنماذج الكبيرة جدًا.

## What is “export scene to glTF”?
يعني تصدير المشهد إلى glTF تسلسل كامل المشهد ثلاثي الأبعاد—بما في ذلك الشبكات، العقد، الكاميرات، الأضواء، والمواد—إلى تنسيق GL Transmission Format (glTF). يُعد glTF معيارًا مفتوحًا مُحسّنًا للتصوير في الوقت الحقيقي، مما يجعله مثاليًا للاستخدام على الويب، الهواتف المحمولة، ومحركات الألعاب.

## Why upgrade materials to PBR before exporting?
توصف مواد PBR (Physically‑Based Rendering) كيفية تفاعل الضوء مع الأسطح باستخدام معلمات مثل albedo، metallic، وroughness. يدعم glTF 2.0 مواد PBR بشكل أصلي، لذا فإن تحويل مواد Phong أو المواد المخصصة إلى PBR يضمن أن الألوان، الانعكاسات، والإضاءة ستظهر بشكل صحيح عند تحميل النموذج في أي عارض يدعم glTF.

## Prerequisites

قبل أن تبدأ، تأكد من وجود ما يلي:

1. **Aspose.3D for Java** – قم بتنزيله من [صفحة الإصدار](https://releases.aspose.com/3d/java/).  
2. **بيئة تطوير Java** – JDK 8 أو أعلى وأي IDE تفضله.  
3. **مجلد المستندات** – مجلد على جهازك لقراءة/كتابة ملفات 3D.

## Import Packages

أضف مساحة الاسم الأساسية لـ Aspose.3D إلى مشروعك:

```java
import com.aspose.threed.*;
```

هذا الاستيراد الوحيد يمنحك الوصول إلى `Scene`، `Box`، `PhongMaterial`، `PbrMaterial`، `GltfSaveOptions`، وواجهة برمجة تطبيقات تحويل المواد.

## Step 1: Initialize a New 3D Scene

أنشئ مشهدًا جديدًا سيحمل الهندسة والمواد الخاصة بك:

```java
// ExStart:InitializeScene
String MyDir = "Your Document Directory";
Scene s = new Scene();
// ExEnd:InitializeScene
```

> **Pro tip:** احتفظ بـ `MyDir` كمسار مطلق أثناء التطوير لتجنب أخطاء عدم العثور على الملف.

## Step 2: Create a Box with a PhongMaterial

سنبدأ بصندوق بسيط يستخدم مادة Phong الكلاسيكية. سيتم تحويلها لاحقًا إلى مادة PBR أثناء التصدير:

```java
// ExStart:CreateBoxWithMaterial
Box box = new Box();
PhongMaterial mat = new PhongMaterial();
mat.setDiffuseColor(new Vector3(1, 0, 1));
s.getRootNode().createChildNode("box1", box).setMaterial(mat);
// ExEnd:CreateBoxWithMaterial
```

> **Why Phong?** مادة Phong سهلة الإعداد وتوضح كيفية عمل منطق التحويل.

## Step 3: Save in GLTF 2.0 Format (Export Scene to glTF)

قم بتكوين خيارات حفظ GLTF لتحويل أي `PhongMaterial` إلى `PbrMaterial` تلقائيًا. هذا هو جوهر **export scene to glTF**:

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

عند تشغيل هذا الكود، يُكتب المشهد إلى `Non_PBRtoPBRMaterial_Out.gltf`. يضمن `MaterialConverter` المخصص تحويل مادة Phong إلى مادة PBR، بحيث يُظهر ملف glTF الناتج إضاءة واقعية في أي عارض glTF.

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| **FileNotFoundException** عند الحفظ | تحقق من أن `MyDir` يشير إلى مجلد موجود وأن التطبيق يمتلك أذونات الكتابة. |
| **ClassCastException** في المحول | تأكد من أن المادة الممررة إلى المحول هي فعليًا `PhongMaterial`. أضف فحص `instanceof` إذا كنت تستخدم أنواع مواد مختلطة. |
| **Missing textures** بعد التصدير | يتوقع glTF توفير القوام بشكل منفصل؛ أضف معالجة القوام إلى المحول إذا لزم الأمر. |

## Frequently Asked Questions

**س: هل Aspose.3D متوافق مع بيئات تطوير Java غير Eclipse؟**  
ج: نعم، يعمل Aspose.3D مع أي IDE للـ Java، بما في ذلك IntelliJ IDEA، NetBeans، وVS Code.

**س: هل يمكنني استخدام Aspose.3D في المشاريع التجارية؟**  
ج: نعم، يمكنك استخدام Aspose.3D في المشاريع الشخصية والتجارية على حد سواء. زر [صفحة الشراء](https://purchase.aspose.com/buy) للحصول على تفاصيل الترخيص.

**س: هل هناك نسخة تجريبية مجانية متاحة؟**  
ج: نعم، يمكنك الحصول على نسخة تجريبية مجانية [من هنا](https://releases.aspose.com/).

**س: أين يمكنني العثور على الدعم لـ Aspose.3D؟**  
ج: استكشف [منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) للحصول على دعم المجتمع.

**س: كيف أحصل على ترخيص مؤقت لـ Aspose.3D؟**  
ج: زر [هذا الرابط](https://purchase.aspose.com/temporary-license/) للحصول على معلومات الترخيص المؤقت.

## Conclusion

باتباع الخطوات السابقة، أصبحت الآن تعرف كيفية **export scene to glTF** في Java باستخدام Aspose.3D مع ترقية مواد Phong تلقائيًا إلى PBR. يتيح لك هذا سير العمل إنشاء أصول عالية الجودة، معتمدة على الفيزياء، جاهزة لأنابيب التصوير الحديثة، عارضات الويب، وتجارب AR/VR. جرّب هندسات أكثر تعقيدًا، قوامًا، وإضاءة لاستغلال كامل قوة PBR وglTF.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2025-12-22  
**Tested With:** Aspose.3D 24.12 for Java  
**Author:** Aspose  

---