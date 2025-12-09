---
date: 2025-12-01
description: تعلم كيفية تغيير لون الملمس، والوصول إلى خصائص المادة، وتعيين قيم Vector3،
  واسترجاع الخصائص بالاسم في مشاهد Java باستخدام Aspose.3D – دليل شامل لتعليم Aspose
  3D.
linktitle: Change texture color and manage 3D properties in Java scenes using Aspose.3D
second_title: Aspose.3D Java API
title: تغيير لون النسيج وإدارة خصائص 3D في مشاهد Java باستخدام Aspose.3D
url: /ar/java/3d-scenes-and-models/managing-3d-properties-scenes/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# تغيير لون القوام وإدارة خصائص 3D في مشاهد Java باستخدام Aspose.3D

## المقدمة

في هذا **دليل Aspose 3D** ستكتشف كيفية **تغيير لون القوام** والعمل مع خصائص 3D والبيانات المخصصة داخل مشاهد Java. سواءً كنت تبني لعبة، أو عارض منتجات، أو عارض علمي، فإن القدرة على تعديل سمات المادة في وقت التشغيل تمنحك تحكمًا فنيًا كاملًا. دعنا نتبع العملية خطوة بخطوة، من تحميل المشهد إلى تعديل لون *Diffuse* باستخدام قيمة `Vector3`.

## إجابات سريعة
- **ماذا يمكنني تعديل؟** يمكنك تغيير لون القوام، الشفافية، اللمعان، وأي خاصية مخصصة مرتبطة بالمادة.  
- **أي فئة تحتفظ بالبيانات؟** `Material` و `PropertyCollection` الخاصة بها.  
- **كيف أضع لونًا جديدًا؟** استخدم `props.set("Diffuse", new Vector3(r, g, b))`.  
- **هل أحتاج إلى ترخيص؟** الترخيص المؤقت يكفي للتقييم؛ الترخيص الكامل مطلوب للإنتاج.  
- **الصيغ المدعومة؟** FBX، OBJ، STL، GLTF، والعديد غيرها.

## المتطلبات المسبقة

- مجموعة تطوير جافا (JDK) 8 أو أحدث مثبتة.  
- مكتبة Aspose.3D for Java (حمّلها من [موقع Aspose](https://releases.aspose.com/3d/java/)).  
- إلمام أساسي بصياغة Java ومفاهيم البرمجة الكائنية.

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

- `Scene` تقوم بتحميل وتمثيل ملف 3D.  
- `Material` تزودك بتعريف السطح (القوام، الألوان، إلخ).  
- `PropertyCollection` هي حاوية شبيهة بالقاموس تسمح لك **بالوصول إلى خصائص المادة** بالاسم.  
- `Vector3` هو نوع البيانات المستخدم للألوان والمتجهات ذات الثلاث مكونات.

## الخطوة 1: تهيئة المشهد

```java
String dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
```

ننشئ كائن `Scene` بتحميل ملف FBX يحتوي بالفعل على قوام. هذا هو القماش الذي سنقوم على **تغيير لون القوام** فيه.

## الخطوة 2: الوصول إلى خصائص المادة

```java
Material material = scene.getRootNode().getChildNodes().get(0).getMaterial();
PropertyCollection props = material.getProperties();
```

هنا **نصل إلى خصائص المادة** للـ mesh الأول في المشهد. كائن `Material` يحمل `PropertyCollection` يخزن كل سمة قابلة للتكوين، مثل *Diffuse*، *Specular*، والبيانات المخصصة للمستخدم.

## الخطوة 3: سرد جميع الخصائص

```java
for (Property prop : props) {
    System.out.println("Name" + prop.getName() + " Value = " + prop.getValue());
}
```

التكرار على `props` يطبع كل اسم خاصية وقيمتها الحالية. هذا الجرد السريع يساعدك على اكتشاف المفاتيح التي يمكنك تعديلها لاحقًا، مثل `"Diffuse"` للون الأساسي.

## الخطوة 4: ضبط قيمة Vector3 لتغيير لون القوام

```java
props.set("Diffuse", new Vector3(1, 0, 1));
```

**نصيحة احترافية:** مُنشئ `Vector3` يأخذ ثلاثة أعداد عائمة تمثل مكونات **الأحمر، الأخضر، والأزرق** (النطاق 0‑1). ضبط `(1, 0, 1)` يغيّر لون القوام الأساسي إلى اللون الأرجواني، وبالتالي **يغير لون القوام** للنموذج.

## الخطوة 5: استرجاع الخاصية بالاسم

```java
Object diffuse = (Vector3) props.get("Diffuse");
System.out.println(diffuse);
```

هذا يوضح **استرجاع الخاصية بالاسم**. نقوم بتحويل الـ `Object` المُرجع إلى `Vector3` للعمل مع اللون برمجيًا.

## الخطوة 6: الوصول إلى كائن الخاصية

```java
Property pdiffuse = props.findProperty("Diffuse");
System.out.println(pdiffuse);
```

`findProperty` تُعيد كائن `Property` الكامل، مما يمنحك الوصول إلى بيانات التعريف مثل نوع الخاصية، التسمية، وأي بيانات مخصصة مرفقة.

## الخطوة 7: استعراض الخصائص الفرعية للخاصية

```java
for (Property pp : pdiffuse.getProperties()) {
    System.out.println("Diffuse. " + pp.getName() + " = " + pp.getValue());
}
```

بعض الخصائص هرمية. استعراض `pdiffuse.getProperties()` يُظهر لك أي سمات متداخلة (مثل إحداثيات القوام، مفاتيح التحريك) التي تنتمي إلى إدخال *Diffuse*.

## المشكلات الشائعة والحلول

| المشكلة | لماذا يحدث | الحل |
|-------|----------------|-----|
| **`NullPointerException` على `material`** | قد لا يكون للعقدة مادة مُعينة. | استدعِ `node.setMaterial(new Material())` قبل الوصول إلى الخصائص. |
| **اللون لا يتغير** | النموذج يستخدم قوامًا يتجاوز لون *Diffuse*. | عطل القوام أو عدّل صورة القوام مباشرة. |
| **`ClassCastException` عند الاسترجاع** | محاولة تحويل خاصية ليست من نوع Vector3. | تحقق من نوع الخاصية باستخدام `pdiffuse.getValue().getClass()` قبل التحويل. |

## الأسئلة المتكررة

**س: كيف يمكنني تثبيت مكتبة Aspose.3D في مشروع Java الخاص بي؟**  
ج: حمّل ملف JAR من [موقع Aspose](https://releases.aspose.com/3d/java/) وأضفه إلى مسار الفئات في مشروعك أو إلى تبعيات Maven/Gradle.

**س: هل توجد خيارات تجربة مجانية لمكتبة Aspose.3D؟**  
ج: نعم، يمكن الحصول على نسخة تجريبية كاملة الوظائف لمدة 30 يومًا من [صفحة التجربة المجانية لـ Aspose](https://releases.aspose.com/).

**س: أين يمكنني العثور على وثائق مفصلة لـ Aspose.3D في Java؟**  
ج: المرجع الرسمي للـ API موجود على [وثائق Aspose.3D](https://reference.aspose.com/3d/java/).

**س: هل هناك منتدى دعم لـ Aspose.3D يمكنني طرح الأسئلة فيه؟**  
ج: بالتأكيد—زر [منتدى دعم Aspose.3D](https://forum.aspose.com/c/3d/18) للتواصل مع المجتمع والخبراء.

**س: كيف يمكنني الحصول على ترخيص مؤقت لـ Aspose.3D؟**  
ج: اطلبه عبر [صفحة الترخيص المؤقت](https://purchase.aspose.com/temporary-license/) على موقع Aspose.

**س: هل يمكنني تعديل سمات مادة أخرى غير اللون؟**  
ج: نعم، يمكن تعديل خصائص مثل `Specular`، `Opacity`، والبيانات المخصصة للمستخدم باستخدام نمط `props.set` نفسه.

## الخاتمة

لقد تعلمت الآن كيفية **تغيير لون القوام**، **الوصول إلى خصائص المادة**، **ضبط قيمة Vector3**، و**استرجاع الخاصية بالاسم** في مشهد Java باستخدام Aspose.3D. تمنحك هذه التقنيات تحكمًا دقيقًا في أي أصل ثلاثي الأبعاد، مما يتيح تأثيرات بصرية ديناميكية وتخصيصًا في وقت التشغيل لتطبيقاتك.

---

**آخر تحديث:** 2025-12-01  
**تم الاختبار مع:** Aspose.3D for Java 24.11  
**المؤلف:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}