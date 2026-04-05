---
date: 2026-04-05
description: تعلم كيفية تعيين لون vector3 في جافا، وتغيير اللون المنتشر، واسترجاع
  خاصية المادة، وإدارة خصائص الـ3D في مشاهد جافا باستخدام Aspose.3D – دليل كامل خطوة
  بخطوة.
keywords:
- set vector3 color java
- Aspose 3D Java
- change diffuse color
linktitle: 'كيفية تعيين لون vector3 في جافا: تغيير اللون المنتشر وإدارة خصائص 3D في
  مشاهد جافا باستخدام Aspose.3D'
second_title: Aspose.3D Java API
title: 'كيفية تعيين لون vector3 في Java: تغيير اللون المنتشر وإدارة خصائص 3D في مشاهد
  Java باستخدام Aspose.3D'
url: /ar/java/3d-scenes-and-models/managing-3d-properties-scenes/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# كيفية تعيين لون vector3 في جافا: تغيير اللون المنتشر وإدارة خصائص 3D في مشاهد جافا باستخدام Aspose.3D

## مقدمة

في هذا **دليل Aspose 3D** ستكتشف **كيفية تعيين لون vector3 في جافا** والعمل مع خصائص 3D والبيانات المخصصة داخل مشاهد جافا. سواء كنت تبني لعبة، أو عارض منتجات، أو عارض علمي، فإن القدرة على تعديل خصائص المادة في وقت التشغيل تمنحك تحكمًا فنيًا كاملاً. دعنا نتبع العملية خطوة بخطوة، من تحميل المشهد إلى تعديل لون *Diffuse* باستخدام قيمة `Vector3`.

## إجابات سريعة
- **ما الذي يمكنني تعديله؟** يمكنك تغيير لون القوام، الشفافية، اللمعان، وأي خاصية مخصصة مرفقة بالمادة.  
- **أي فئة تحتفظ بالبيانات؟** `Material` و `PropertyCollection` الخاصة بها.  
- **كيف يمكنني تعيين لون جديد؟** استخدم `props.set("Diffuse", new Vector3(r, g, b))`.  
- **كيف يمكنني تعيين لون vector3 في جافا؟** استدعِ `props.set("Diffuse", new Vector3(r, g, b))` على مجموعة خصائص المادة.  
- **هل أحتاج إلى ترخيص؟** الترخيص المؤقت يعمل للتقييم؛ الترخيص الكامل مطلوب للإنتاج.  
- **الصيغ المدعومة؟** FBX، OBJ، STL، GLTF، والعديد غيرها.

## المتطلبات المسبقة

- Java Development Kit (JDK) 8 أو أحدث مثبت.  
- مكتبة Aspose.3D for Java (حمّلها من [موقع Aspose](https://releases.aspose.com/3d/java/)).  
- إلمام أساسي بصياغة جافا ومفاهيم البرمجة الكائنية.

## استيراد الحزم

قبل كتابة أي منطق، استورد الفئات التي تمنحك الوصول إلى خصائص المادة ومعالجة المتجهات.

```java
import java.io.IOException;

import com.aspose.threed.Material;
import com.aspose.threed.Property;
import com.aspose.threed.PropertyCollection;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;
```

### لماذا نستورد هذه الفئات؟

- `Scene` يقوم بتحميل وتمثيل ملف 3D.  
- `Material` يزودك بتعريف السطح (القوام، الألوان، إلخ).  
- `PropertyCollection` هو حاوية شبيهة بالقاموس تسمح لك **بالوصول إلى خصائص المادة** بالاسم.  
- `Vector3` هو نوع البيانات المستخدم للألوان والمتجهات ذات الثلاث مكونات.

## كيفية تعيين لون vector3 في جافا – دليل خطوة بخطوة لتغيير Diffuse

### الخطوة 1: تهيئة المشهد

```java
String dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
```

نقوم بإنشاء كائن `Scene` بتحميل ملف FBX يحتوي بالفعل على قوام. هذه هي اللوحة التي سنقوم فيها **بتغيير لون Diffuse**.

### الخطوة 2: الوصول إلى خصائص المادة

```java
Material material = scene.getRootNode().getChildNodes().get(0).getMaterial();
PropertyCollection props = material.getProperties();
```

هنا ن **نصل إلى خصائص المادة** للـ mesh الأول في المشهد. كائن `Material` يحتوي على `PropertyCollection` يخزن كل سمة قابلة للتكوين، مثل *Diffuse*، *Specular*، والبيانات المخصصة للمستخدم.

### الخطوة 3: سرد جميع الخصائص (فحص قبل التغيير)

```java
for (Property prop : props) {
    System.out.println("Name" + prop.getName() + " Value = " + prop.getValue());
}
```

التكرار على `props` يطبع كل اسم خاصية وقيمتها الحالية. هذا الجرد السريع يساعدك على اكتشاف المفاتيح التي يمكنك تعديلها لاحقًا، مثل `"Diffuse"` للون الأساسي.

### الخطوة 4: تعيين قيمة Vector3 لتغيير لون Diffuse

```java
props.set("Diffuse", new Vector3(1, 0, 1));
```

**نصيحة احترافية:** مُنشئ `Vector3` يأخذ ثلاثة أعداد عائمة تمثل مكونات **الأحمر، الأخضر، والأزرق** (النطاق 0‑1). تعيين `(1, 0, 1)` يغيّر اللون الأساسي للقوام إلى اللون الأرجواني، وبالتالي **يغير لون Diffuse** للنموذج. هذا هو جوهر **تعيين لون vector3 في جافا**.

### الخطوة 5: استرجاع خاصية المادة بالاسم

```java
Object diffuse = (Vector3) props.get("Diffuse");
System.out.println(diffuse);
```

هذا يوضح **استرجاع خاصية المادة** بالاسم. نقوم بتحويل الـ `Object` المرجع إلى `Vector3` للعمل مع اللون برمجيًا.

### الخطوة 6: الوصول إلى نسخة الخاصية مباشرةً

```java
Property pdiffuse = props.findProperty("Diffuse");
System.out.println(pdiffuse);
```

`findProperty` يُعيد كائن `Property` الكامل، مما يمنحك الوصول إلى البيانات الوصفية مثل نوع الخاصية، التسمية، وأي بيانات مخصصة مرفقة.

### الخطوة 7: استعراض الخصائص الفرعية للخاصية

```java
for (Property pp : pdiffuse.getProperties()) {
    System.out.println("Diffuse. " + pp.getName() + " = " + pp.getValue());
}
```

بعض الخصائص هرمية. استعراض `pdiffuse.getProperties()` يُظهر لك أي سمات متداخلة (مثل إحداثيات القوام، مفاتيح التحريك) التي تنتمي إلى مدخل *Diffuse*.

## لماذا هذا مهم

تغيير لون Diffuse في وقت التشغيل يتيح لك إنشاء تأثيرات بصرية ديناميكية—تخيل مكوّنات تكوين المنتجات حيث يختار المستخدمون الألوان، أو الألعاب التي تتفاعل مع أحداث اللعب. نظرًا لأن التغيير يتم عبر `PropertyCollection`، يمكنك أيضًا كتابة سكريبت لتحديثات جماعية عبر العديد من المواد بأقل قدر من الشيفرة.

## المشكلات الشائعة والحلول

| المشكلة | السبب | الحل |
|-------|----------------|-----|
| **`NullPointerException` على `material`** | قد لا يكون للعقدة مادة مُعينة. | استدعِ `node.setMaterial(new Material())` قبل الوصول إلى الخصائص. |
| **اللون لا يتغير** | النموذج يستخدم قوامًا يتجاوز لون *Diffuse*. | عطل القوام أو عدّل صورة القوام مباشرةً. |
| **`ClassCastException` عند الاسترجاع** | محاولة تحويل خاصية ليست من نوع Vector3. | تحقق من نوع الخاصية باستخدام `pdiffuse.getValue().getClass()` قبل التحويل. |

## الأسئلة المتكررة

**س: كيف يمكنني تثبيت مكتبة Aspose.3D في مشروعي جافا؟**  
ج: حمّل ملف JAR من [موقع Aspose](https://releases.aspose.com/3d/java/) وأضفه إلى مسار الفئات (classpath) في مشروعك أو إلى تبعيات Maven/Gradle.

**س: هل هناك خيارات تجربة مجانية لـ Aspose.3D؟**  
ج: نعم، تجربة كاملة الوظائف لمدة 30 يومًا متاحة من [صفحة التجربة المجانية لـ Aspose](https://releases.aspose.com/).

**س: أين يمكنني العثور على وثائق مفصلة لـ Aspose.3D في جافا؟**  
ج: المرجع الرسمي للـ API موجود في [توثيق Aspose.3D](https://reference.aspose.com/3d/java/).

**س: هل هناك منتدى دعم لـ Aspose.3D يمكنني طرح الأسئلة فيه؟**  
ج: بالتأكيد—زر [منتدى دعم Aspose.3D](https://forum.aspose.com/c/3d/18) للتواصل مع المجتمع والخبراء.

**س: كيف يمكنني الحصول على ترخيص مؤقت لـ Aspose.3D؟**  
ج: اطلب واحدًا عبر [صفحة الترخيص المؤقت](https://purchase.aspose.com/temporary-license/) على موقع Aspose.

**س: هل يمكنني تغيير خصائص مادة أخرى غير Diffuse؟**  
ج: نعم، يمكن تعديل خصائص مثل `Specular`، `Opacity`، والبيانات المخصصة للمستخدم باستخدام نمط `props.set` نفسه.

## الخلاصة

لقد تعلمت الآن **كيفية تعيين لون vector3 في جافا**، **استرجاع خاصية المادة**، تعيين قيمة `Vector3`، والتنقل في بيانات الخصائص الهرمية في مشهد جافا باستخدام Aspose.3D. هذه التقنيات تمنحك تحكمًا دقيقًا في أي عنصر 3D، مما يتيح تأثيرات بصرية ديناميكية وتخصيصًا في وقت التشغيل في تطبيقاتك.

---

**آخر تحديث:** 2026-04-05  
**تم الاختبار مع:** Aspose.3D for Java 24.11  
**المؤلف:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}