---
date: 2026-04-08
description: تعلم كيفية تضمين النسيج في ملف FBX باستخدام Java و Aspose.3D. يوضح لك
  هذا الدرس كيفية تعيين المادة إلى الشبكة، وتطبيق المواد على الكائنات ثلاثية الأبعاد،
  وحفظ ملف FBX مع النسيج بسرعة.
keywords:
- how to embed texture
- assign material to mesh
- apply materials to 3d
- save fbx with texture
- embed texture into fbx
linktitle: تطبيق المواد على الكائنات ثلاثية الأبعاد في جافا باستخدام Aspose.3D
second_title: Aspose.3D Java API
title: كيفية تضمين القوام في FBX باستخدام Java – تطبيق المواد على الأجسام ثلاثية الأبعاد
  باستخدام Aspose.3D
url: /ar/java/geometry/apply-materials-to-3d-objects/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# كيفية تضمين القوام في ملف FBX باستخدام Java – تطبيق المواد على الأجسام ثلاثية الأبعاد باستخدام Aspose.3D

## المقدمة

في هذا **دليل رسومات Java ثلاثية الأبعاد** سنرشدك إلى **كيفية تضمين القوام** في مكعب ثلاثي الأبعاد بسيط باستخدام Aspose.3D Java API. تطبيق المواد والقوام هو الخطوة الأساسية التي تحول شبكة مسطحة إلى كائن واقعي يمكنك استخدامه في الألعاب أو التصورات أو عروض المنتجات. في نهاية هذا الدليل ستحصل على ملف FBX مملوء بالقوام يمكنك فتحه في أي عارض ثلاثي الأبعاد، وستفهم كيفية **تعيين مادة إلى الشبكة**، **تطبيق المواد على الأجسام ثلاثية الأبعاد**، و **حفظ FBX مع القوام** لتوزيع موثوق.

## كيفية تضمين القوام في ملف FBX باستخدام Java

تضمين القوام مباشرةً في ملف FBX يعني أن بيانات القوام تسافر مع الهندسة، مما يلغي مشاكل القوام المفقود عندما يُفتح النموذج على جهاز آخر. هذه التقنية مفيدة بشكل خاص لتدفقات عمل **تصدير المشهد إلى FBX** حيث تريد أصلًا واحدًا محمولًا.

## إجابات سريعة
- **ما هو الهدف الرئيسي؟** تطبيق مادة Phong مع قوام انتشار على مكعب.  
- **ما المكتبة المستخدمة؟** Aspose.3D for Java (يتوفر نسخة تجريبية مجانية).  
- **كم من الوقت يستغرق؟** حوالي 10‑15 دقيقة للحصول على مثال عملي.  
- **هل أحتاج إلى ترخيص؟** يلزم ترخيص مؤقت للبنيات غير التجريبية.  
- **ما هو تنسيق الملف الناتج؟** FBX 7.4 ASCII (متوافق مع معظم أدوات 3‑D).  

## لماذا نستخدم Aspose.3D لتضمين القوام في FBX؟

توفر Aspose.3D واجهة برمجة تطبيقات نظيفة كائنية التوجه تُجردك من تفاصيل تنسيقات الملفات منخفضة المستوى. تدعم مجموعة واسعة من التنسيقات (FBX، STL، OBJ، إلخ) وتتيح لك **assign material mesh** وتضمين القوام في استدعاء واحد سلس. هذا يجعل من السهل جدًا **إصلاح مشكلة القوام المفقود** مقارنةً بتحرير FBX يدويًا.

## المتطلبات المسبقة

قبل أن تبدأ، تأكد من أن لديك:

- Java Development Kit (JDK 8 أو أعلى) مثبت.  
- أحدث ملف JAR لـ Aspose.3D for Java مضاف إلى مسار الفئة (classpath) في مشروعك.  
- فهم أساسي لبنية Java وبرمجة الكائنات.  
- ملف قوام (مثال: `surface.dds` أو `embedded-texture.png`) جاهز على القرص.

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

## الخطوة 3: إنشاء شبكة باستخدام Polygon Builder

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

## الخطوة 7: تهيئة كائن Texture

```java
// Initialize Texture object
Texture diffuse = new Texture();
```

## الخطوة 8: تعيين مسار الملف المحلي للقوام

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
```

## الخطوة 9: تعيين مسار الملف المحلي للقوام المضمن

```java
// Set local file path for embedded texture
diffuse.setFileName(MyDir + "surface.dds");
```

## الخطوة 10: تعيين القوام للمادة

```java
// Set Texture of the material
mat.setTexture(Material.MAP_DIFFUSE, diffuse);
```

## الخطوة 11: تضمين بيانات المحتوى الخام إلى FBX (اختياري)

```java
// Set file name for embedded texture
diffuse.setFileName("embedded-texture.png");
// Set binary content
diffuse.setContent(Files.readAllBytes(Paths.get(MyDir, "aspose-logo.jpg")));
```

## الخطوة 12: تعيين لون الانعكاس (Specular Color)

```java
// Set specular color
mat.setSpecularColor(new Vector3(1, 0, 0));
```

## الخطوة 13: تعيين السطوع

```java
// Set brightness
mat.setShininess(100);
```

## الخطوة 14: تعيين خاصية المادة لكائن المكعب

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

## لماذا هذا مهم

يُزيل تضمين القوام الحاجة إلى شحن ملفات صور منفصلة بجانب نموذج FBX، وهو مصدر شائع للأصول المكسورة في خطوط الأنابيب التي تنتقل بين المصممين والمحركات وشبكات توصيل المحتوى. كما يضمن أن المظهر البصري الذي تراه في المحرر هو بالضبط ما سيشاهده المستخدمون النهائيون.

## حالات الاستخدام الشائعة

- **خطوط أنابيب أصول الألعاب** – تقديم ملف FBX واحد إلى Unity أو Unreal دون القلق بشأن القوام المفقودة.  
- **تصور المنتجات** – إرسال نموذج مملوء بالقوام إلى العملاء الذين قد لا يمتلكون مجلد القوام الأصلي.  
- **النمذجة السريعة** – إنشاء نُسخ مؤقتة مملوءة بالقوام بسرعة للتحقق من المفهوم.  

## المشكلات الشائعة والحلول

| المشكلة | السبب | الحل |
|-------|--------|-----|
| **القوام غير مرئي** | مسار ملف خاطئ أو تنسيق قوام غير مدعوم. | تحقق من أن `MyDir` يشير إلى المجلد الصحيح واستخدم تنسيقًا مدعومًا مثل `.dds` أو `.png`. |
| **فشل تحميل ملف FBX** | بيانات القوام المضمنة مفقودة. | استخدم الكتلة الاختيارية (الخطوة 11) لتضمين بايتات القوام مباشرةً في FBX. |
| **المادة تظهر باللون الأسود** | قيم الانعكاس أو الانتشار غير مضبوطة. | تأكد من استدعاء `setSpecularColor` و `setTexture` قبل الحفظ. |

## الأسئلة المتكررة

**س: هل يمكنني تطبيق مواد متعددة على كائن ثلاثي الأبعاد واحد؟**  
ج: نعم، تتيح لك Aspose.3D تعيين مواد مختلفة لأجزاء شبكة منفصلة أو لعقد فرعية.

**س: ما تنسيقات الملفات التي تدعمها Aspose.3D لحفظ المشاهد؟**  
ج: FBX، STL، OBJ، 3DS، والعديد غيرها. راجع [التوثيق](https://reference.aspose.com/3d/java/) الرسمي للحصول على القائمة الكاملة.

**س: هل يتوفر ترخيص مؤقت لـ Aspose.3D for Java؟**  
ج: نعم، يمكنك الحصول على [ترخيص مؤقت](https://purchase.aspose.com/temporary-license/) للتقييم.

**س: أين يمكنني العثور على دعم Aspose.3D؟**  
ج: منتدى [Aspose.3D](https://forum.aspose.com/c/3d/18) هو أفضل مكان للحصول على مساعدة المجتمع.

**س: هل يمكنني تنزيل مكتبة Aspose.3D من رابط محدد؟**  
ج: بالتأكيد—استخدم [رابط التنزيل](https://releases.aspose.com/3d/java/) للحصول على أحدث ملفات JAR.

**س: كيف أصلح مشكلة القوام المفقود بعد تصدير المشهد إلى FBX؟**  
ج: تأكد من أن القوام إما مضمّن (الخطوة 11) أو أن المسار النسبي المستخدم في `setFileName` يشير إلى موقع سيسافر مع ملف FBX.

**س: هل تسمح لي Aspose.3D **assign material mesh** للوجوه الفردية؟**  
ج: نعم، يمكنك إنشاء عدة كائنات `Material` وتعيينها لأجزاء شبكة محددة عبر واجهة `MeshPart` API.

## الخلاصة

لقد تعلمت الآن **كيفية تضمين القوام** في تطبيق Java باستخدام Aspose.3D، وكيفية **assign material mesh**، وكيفية تجنب مشكلة “القوام المفقود” الشائعة. لا تتردد في تجربة تنسيقات قوام مختلفة، تعديل إعدادات الانعكاس، أو دمج مواد متعددة لنماذج أكثر تعقيدًا. عندما تكون مستعدًا، استكشف خيارات تصدير أخرى مثل OBJ أو STL لتوسيع سير عملك.

---

**Last Updated:** 2026-04-08  
**Tested With:** تم الاختبار مع Aspose.3D for Java أحدث إصدار  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}