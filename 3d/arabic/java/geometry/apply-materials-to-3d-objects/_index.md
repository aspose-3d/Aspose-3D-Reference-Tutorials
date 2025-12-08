---
date: 2025-12-08
description: تعلّم درسًا في رسومات Java ثلاثية الأبعاد حول كيفية إضافة القوام باستخدام
  Aspose.3D. طبّق مواد واقعية على الكائنات ثلاثية الأبعاد في Java بسرعة.
language: ar
linktitle: Apply Materials to 3D Objects in Java with Aspose.3D
second_title: Aspose.3D Java API
title: دروس رسومات جافا ثلاثية الأبعاد – تطبيق المواد على الكائنات ثلاثية الأبعاد
  في جافا باستخدام Aspose.3D
url: /java/geometry/apply-materials-to-3d-objects/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# تطبيق المواد على كائنات 3D في Java باستخدام Aspose.3D

## المقدمة

في هذا **دليل رسومات 3D بجافا**، سنوضح لك **كيفية إضافة نسيج جافا** إلى مكعب ثلاثي الأبعاد بسيط باستخدام Aspose.3D Java API. تطبيق المواد والأنسجة هو الخطوة الأساسية التي تحول شبكة مسطحة إلى كائن واقعي يمكنك استخدامه في الألعاب أو التصورات أو عروض المنتجات. في نهاية هذا الدليل ستحصل على ملف FBX مُنقّش بالكامل يمكنك فتحه في أي عارض ثلاثي الأبعاد.

## إجابات سريعة
- **ما الهدف الرئيسي؟** تطبيق مادة Phong مع نسيج انتشاري على مكعب.  
- **أي مكتبة؟** Aspose.3D for Java (يتوفر إصدار تجريبي مجاني).  
- **كم من الوقت يستغرق؟** حوالي 10‑15 دقيقة للحصول على مثال عملي.  
- **هل أحتاج إلى ترخيص؟** يلزم ترخيص مؤقت للبُنى غير التجريبية.  
- **ما صيغة الملف الناتج؟** FBX 7.4 ASCII (متوافق مع معظم أدوات 3D).

## ما هو دليل رسومات 3D بجافا؟

**دليل رسومات 3D بجافا** يرافقك خلال إنشاء، تعديل، وتصدير محتوى ثلاثي الأبعاد باستخدام مكتبات مبنية على Java. في هذه الحالة نركز على معالجة المواد—تعيين الألوان، الأنسجة، وخصائص الإضاءة للكيانات الهندسية.

## لماذا نستخدم Aspose.3D لإضافة نسيج جافا؟

Aspose.3D يقدم API نظيفًا موجهًا للكائنات يُبسط تفاصيل صيغ الملفات منخفضة المستوى. يدعم مجموعة واسعة من الصيغ (FBX, STL, OBJ, إلخ) ويسمح لك بدمج الأنسجة مباشرة داخل الملف، وهو مثالي عندما تريد أصلًا واحدًا محمولًا.

## المتطلبات المسبقة

قبل البدء، تأكد من وجود ما يلي:

- مجموعة تطوير جافا (JDK 8 أو أعلى) مثبتة.
- أحدث ملف JAR الخاص بـ Aspose.3D for Java مضاف إلى مسار الفئات في مشروعك.
- فهم أساسي لصياغة جافا والبرمجة الكائنية.

## استيراد الحزم

```java
import com.aspose.threed.*;


import java.nio.file.Files;
import java.nio.file.Paths;
```

## الخطوة 1: تهيئة كائن المشهد

```java
// Initialize scene object
Scene scene = new Scene();
```

## الخطوة 2: تهيئة كائن عقدة المكعب

```java
// Initialize cube node object
Node cubeNode = new Node("cube");
```

## الخطوة 3: إنشاء شبكة باستخدام مُنشئ المضلعات

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## الخطوة 4: ربط العقدة بالشبكة

```java
// Point node to the mesh
cubeNode.setEntity(mesh);
```

## الخطوة 5: إضافة المكعب إلى المشهد

```java
// Add cube to the scene
scene.getRootNode().addChildNode(cubeNode);
```

## الخطوة 6: تهيئة كائن PhongMaterial

```java
// Initialize PhongMaterial object
PhongMaterial mat = new PhongMaterial();
```

## الخطوة 7: تهيئة كائن النسيج

```java
// Initialize Texture object
Texture diffuse = new Texture();
```

## الخطوة 8: ضبط مسار الملف المحلي للنسيج

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
```

## الخطوة 9: ضبط مسار الملف المحلي للنسيج المدمج

```java
// Set local file path for embedded texture
diffuse.setFileName(MyDir + "surface.dds");
```

## الخطوة 10: تعيين نسيج المادة

```java
// Set Texture of the material
mat.setTexture(Material.MAP_DIFFUSE, diffuse);
```

## الخطوة 11: دمج بيانات المحتوى الخام إلى FBX (اختياري)

```java
// Set file name for embedded texture
diffuse.setFileName("embedded-texture.png");
// Set binary content
diffuse.setContent(Files.readAllBytes(Paths.get(MyDir, "aspose-logo.jpg")));
```

## الخطوة 12: ضبط لون الانعكاس

```java
// Set specular color
mat.setSpecularColor(new Vector3(1, 0, 0));
```

## الخطوة 13: ضبط السطوع

```java
// Set brightness
mat.setShininess(100);
```

## الخطوة 14: ضبط خاصية المادة لكائن المكعب

```java
// Set material property of the cube object
cubeNode.setMaterial(mat);
```

## الخطوة 15: حفظ المشهد ثلاثي الأبعاد

```java
// Set the file name
MyDir = MyDir + "MaterialToCube.fbx";
// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## المشكلات الشائعة والحلول

| المشكلة | السبب | الإصلاح |
|-------|--------|-----|
| **النسيج غير مرئي** | مسار ملف غير صحيح أو صيغة نسيج غير مدعومة. | تحقق من أن `MyDir` يشير إلى المجلد الصحيح واستخدم صيغة مدعومة مثل `.dds` أو `.png`. |
| **فشل تحميل ملف FBX** | نقص بيانات النسيج المدمج. | استخدم الكتلة الاختيارية (الخطوة 11) لدمج بايتات النسيج مباشرة داخل FBX. |
| **المادة تظهر باللون الأسود** | قيم الانعكاس أو الانتشار غير مضبوطة. | تأكد من استدعاء `setSpecularColor` و `setTexture` قبل الحفظ. |

## الأسئلة المتكررة

**س: هل يمكنني تطبيق مواد متعددة على كائن ثلاثي الأبعاد واحد؟**  
ج: نعم، Aspose.3D يتيح لك تعيين مواد مختلفة لأجزاء شبكة منفصلة أو لعقد فرعية.

**س: ما صيغ الملفات التي يدعمها Aspose.3D لحفظ المشاهد؟**  
ج: FBX, STL, OBJ, 3DS، والعديد غيرها. راجع [الوثائق الرسمية](https://reference.aspose.com/3d/java/) للقائمة الكاملة.

**س: هل يتوفر ترخيص مؤقت لـ Aspose.3D for Java؟**  
ج: نعم، يمكنك الحصول على [ترخيص مؤقت](https://purchase.aspose.com/temporary-license/) للتقييم.

**س: أين يمكنني العثور على دعم Aspose.3D؟**  
ج: منتدى [Aspose.3D](https://forum.aspose.com/c/3d/18) هو أفضل مكان للحصول على مساعدة المجتمع.

**س: هل يمكنني تنزيل مكتبة Aspose.3D من رابط محدد؟**  
ج: بالتأكيد—استخدم [رابط التحميل](https://releases.aspose.com/3d/java/) للحصول على أحدث ملفات JAR.

---

**آخر تحديث:** 2025-12-08  
**تم الاختبار مع:** Aspose.3D for Java 24.11  
**المؤلف:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}