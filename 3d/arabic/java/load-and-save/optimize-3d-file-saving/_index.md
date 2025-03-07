---
title: تحسين حفظ الملفات ثلاثية الأبعاد في Java باستخدام Aspose.3D SaveOptions
linktitle: تحسين حفظ الملفات ثلاثية الأبعاد في Java باستخدام Aspose.3D SaveOptions
second_title: Aspose.3D جافا API
description: تعرف على كيفية تحسين حفظ الملفات ثلاثية الأبعاد في Java باستخدام Aspose.3D SaveOptions. تعزيز الأداء وتخصيص المخرجات دون عناء.
weight: 16
url: /ar/java/load-and-save/optimize-3d-file-saving/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# تحسين حفظ الملفات ثلاثية الأبعاد في Java باستخدام Aspose.3D SaveOptions

## مقدمة

Aspose.3D هي مكتبة Java غنية بالميزات تمكن المطورين من العمل مع النماذج ثلاثية الأبعاد بسلاسة. عندما يتعلق الأمر بحفظ الملفات ثلاثية الأبعاد، توفر فئة SaveOptions عددًا كبيرًا من الإعدادات لضبط الإخراج وفقًا لمتطلباتك. في هذا البرنامج التعليمي، سنستكشف خيارات الحفظ المختلفة وكيف يمكن الاستفادة منها لتحسين العملية.

## المتطلبات الأساسية

قبل أن نتعمق في البرنامج التعليمي، تأكد من توفر المتطلبات الأساسية التالية:

-  Aspose.3D لـ Java: تأكد من دمج مكتبة Aspose.3D في مشروع Java الخاص بك. يمكنك تنزيله[هنا](https://releases.aspose.com/3d/java/).

- بيئة تطوير Java: قم بإعداد بيئة تطوير Java وظيفية على جهازك.

- دليل المستندات: قم بإنشاء دليل تريد حفظ ملفاتك ثلاثية الأبعاد فيه ولاحظ مساره لاستخدامه لاحقًا.

## حزم الاستيراد

 في مشروع Java الخاص بك، قم باستيراد الحزم اللازمة للعمل مع Aspose.3D. وهذا يشمل`Scene` فئة وفئات SaveOptions المختلفة. فيما يلي مثال أساسي:

```java
import com.aspose.threed.*;


import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

الآن، دعونا نقسم كل مثال إلى خطوات متعددة لتوضيح استخدام خيارات SaveOptions المختلفة.

## الخطوة 1: طباعة جميلة في GLTF SaveOption

 ال`prettyPrintInGltfSaveOption` تسمح لك الطريقة بإنشاء ملف GLTF بمحتوى JSON ذو مسافة بادئة لسهولة القراءة البشرية.

```java
public static void prettyPrintInGltfSaveOption() throws IOException {
    // تهيئة المشهد ثلاثي الأبعاد
    Scene scene = new Scene(new Sphere());
    
    // تهيئة جلتفسافيوبتيونس
    GltfSaveOptions opt = new GltfSaveOptions(FileFormat.GLTF2);
    
    // قم بتمكين الطباعة الجميلة لتحسين إمكانية القراءة
    opt.setPrettyPrint(true);
    
    // حفظ المشهد ثلاثي الأبعاد
    scene.save("Your Document Directory" + "prettyPrintInGltfSaveOption.gltf", opt);
}
```

## الخطوة 2: HTML5 SaveOption

 ال`html5SaveOption` توضح الطريقة كيفية حفظ مشهد ثلاثي الأبعاد كملف HTML5، بما في ذلك خيارات التخصيص.

```java
public static void html5SaveOption() throws IOException {
    // تهيئة المشهد
    Scene scene = new Scene();
    
    // قم بإنشاء عقدة فرعية باستخدام أسطوانة
    Node node = scene.getRootNode().createChildNode(new Cylinder());
    
    //قم بتعيين خصائص العقدة الفرعية
    LambertMaterial mat = new LambertMaterial();
    mat.setDiffuseColor(new Vector3(0.34, 0.59, 0.41));
    node.setMaterial(mat);
    
    // أضف ضوءًا إلى المشهد
    Light light = new Light();
    light.setLightType(LightType.POINT);
    scene.getRootNode().createChildNode(light).getTransform().setTranslation(10, 0, 10);
    
    // تهيئة HTML5SaveOptions
    Html5SaveOptions opt = new Html5SaveOptions();
    
    // تخصيص الخيارات (على سبيل المثال، إيقاف تشغيل الشبكة وواجهة المستخدم)
    opt.setShowGrid(false);
    opt.setShowUI(false);
    
    // احفظ المشهد كملف HTML5
    scene.save("Your Document Directory" + "html5SaveOption.html", FileFormat.HTML5);
}
```

 تابع التفاصيل المشابهة لطرق SaveOptions الأخرى مثل`colladaSaveOption`, `discreet3DSSaveOption`, `fbxSaveOption`, `objSaveOption`, `STLSaveOption`, `U3DSaveOption`, `glTFSaveOptions` ، و`drcSaveOptions`.

## خاتمة

باتباع هذا البرنامج التعليمي الشامل، تعلمت كيفية تحسين حفظ الملفات ثلاثية الأبعاد في Java باستخدام Aspose.3D SaveOptions. سواء كنت مهتمًا بطباعة ملفات GLTF بشكل جميل أو تخصيص مخرجات HTML5، فإن Aspose.3D يزودك بالأدوات اللازمة لتحسين سير عمل الرسومات ثلاثية الأبعاد.

## الأسئلة الشائعة

### س1: كيف يمكنني تضمين الأصول في ملف glTF؟

 A1: لتضمين الأصول، استخدم`setEmbedAssets(true)` الطريقة في`GltfSaveOptions` فصل.

###  س2: ما الهدف من ذلك؟`setPositionBits` method in `DracoSaveOptions`?

 ج2: ال`setPositionBits` تقوم الطريقة بتعيين بتات التكمية للموضع في خوارزمية ضغط Draco.

### س3: هل يمكنني تصدير البيانات العادية في ملف U3D؟

 A3: نعم، يمكنك تصدير البيانات العادية عن طريق الإعداد`setExportNormals(true)` في ال`U3dSaveOptions` فصل.

### س4: كيف يمكنني تجاهل حفظ ملفات المواد في عملية تصدير OBJ؟

ج4: استخدم`setFileSystem(new DummyFileSystem())` الطريقة في`ObjSaveOptions` فئة لتجاهل الملفات المادية.

### س 5: هل هناك طريقة لحفظ التبعيات إلى دليل محلي في ملف OBJ؟

 ج5: نعم، استخدم`setFileSystem(new LocalFileSystem(MyDir))` الطريقة في`ObjSaveOptions` فئة لحفظ التبعيات محليا.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
