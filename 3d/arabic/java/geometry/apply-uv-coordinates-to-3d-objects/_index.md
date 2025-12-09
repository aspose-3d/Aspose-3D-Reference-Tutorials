---
date: 2025-12-09
description: تعلم كيفية رسم خريطة UV لنماذج ثلاثية الأبعاد عن طريق إضافة UVs إلى الشبكة
  وتطبيق الخامات باستخدام Java و Aspose.3D. اتبع هذا الدليل خطوة بخطوة لتطبيق الخامات
  على كائناتك ثلاثية الأبعاد.
language: ar
linktitle: 'UV Mapping 3D Models: UV Coordinates in Java with Aspose.3D'
second_title: Aspose.3D Java API
title: 'تعيين UV لنماذج ثلاثية الأبعاد: إحداثيات UV في جافا باستخدام Aspose.3D'
url: /java/geometry/apply-uv-coordinates-to-3d-objects/
weight: 18
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# تخطيط UV لنماذج ثلاثية الأبعاد: إحداثيات UV في Java باستخدام Aspose.3D

## Introduction

مرحبًا! في هذا الدرس الشامل ستتعلم **uv mapping 3d models** باستخدام Java ومكتبة Aspose.3D القوية. تخطيط UV هو التقنية التي تتيح لك **add uvs to mesh** بحيث تتطابق القوام بشكل مثالي مع كائناتك ثلاثية الأبعاد. بنهاية هذا الدليل ستتمكن من رسم القوام بأسلوب Java ورؤية نماذجك تنبض بالحياة.

## Quick Answers
- **ماذا يفعل تخطيط UV؟** يقوم بتعيين إحداثيات القوام ثنائية الأبعاد (U & V) لكل رأس في شبكة ثلاثية الأبعاد.  
- **ما المكتبة المستخدمة؟** Aspose.3D for Java.  
- **كم عدد أسطر الكود؟** حوالي 30 سطرًا، مقسمة على أربعة كتل شفرة.  
- **هل أحتاج إلى رخصة؟** نسخة تجريبية مجانية تكفي للتطوير؛ تحتاج إلى رخصة تجارية للإنتاج.  
- **هل يمكنني إعادة استخدام هذا لأشكال أخرى؟** بالتأكيد – نفس النهج يعمل مع أي شبكة.

## What is UV Mapping 3D Models?

تخطيط UV لنماذج ثلاثية الأبعاد هو عملية إسقاط صورة ثنائية الأبعاد (القوام) على سطح ثلاثي الأبعاد. يحصل كل رأس على زوج من الإحداثيات — U (أفقي) و V (عمودي) — التي تخبر المُعالج أين يلتقط القوام. هذه الخطوة أساسية للتصيير الواقعي، وأصول الألعاب، وتجارب AR/VR.

## Why Use Aspose.3D for UV Mapping?

- **واجهة برمجة تطبيقات Java متعددة المنصات** – تعمل على Windows وLinux وmacOS.  
- **محرك هندسي عالي الأداء** – يتعامل مع الشبكات الكبيرة بسهولة.  
- **معالجة قوام مدمجة** – يدعم القوام المنتشرة (diffuse)، اللامعة (specular)، خريطة العمق (normal) وغيرها.  
- **واجهة برمجة تطبيقات واضحة وسلسة** – تجعل من السهل **add uvs to mesh** الحاجة إلى تحليل ملفات منخفض المستوى.

## Prerequisites

- **Java Development Kit (JDK 8 أو أعلى)** مثبت ومُكوَّن.  
- **Aspose.3D for Java** – حمّل أحدث ملف JAR من الموقع الرسمي [هنا](https://releases.aspose.com/3d/java/).  
- **معرفة أساسية بالـ 3‑D** – فهم الرؤوس، المضلعات، ومفاهيم تخطيط القوام.

## Import Packages

أولاً، نحتاج إلى استيراد فئات Aspose.3D التي ستسمح لنا بإنشاء الهندسة وتعيين بيانات UV.

### Step 1: Import Aspose.3D Packages

```java
import com.aspose.threed.*;

import java.util.Arrays;
```

الآن بعد أن تم إعداد الاستيرادات، دعنا ننتقل إلى إنشاء بيانات UV لمكعب بسيط.

## Setup UV Coordinates on a 3D Object

فيما يلي سنستعرض الخطوات الدقيقة لتوليد إحداثيات UV وربطها بشبكة.

### Step 2: Create UVs and Indices

```java
// ExStart:SetupUVOnCube
// UVs
Vector4[] uvs = new Vector4[]
{
    new Vector4( 0.0, 1.0,0.0, 1.0),
    new Vector4( 1.0, 0.0,0.0, 1.0),
    new Vector4( 0.0, 0.0,0.0, 1.0),
    new Vector4( 1.0, 1.0,0.0, 1.0)
};

// Indices of the uvs per each polygon
int[] uvsId = new int[]
{
    0,1,3,2,2,3,5,4,4,5,7,6,6,7,9,8,1,10,11,3,12,0,2,13
};
// ExEnd:SetupUVOnCube
```

*شرح*:  
- **uvs** يحتوي على متجهات إحداثيات UV الفعلية (U, V, W, Q).  
- **uvsId** يربط كل رأس من المضلع بإدخال في مصفوفة `uvs`، مما يتيح خطوة **add uvs to mesh** لاحقًا.

### Step 3: Create Mesh and UVset

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Create UVset
VertexElementUV elementUV = mesh.createElementUV(TextureMapping.DIFFUSE, MappingMode.POLYGON_VERTEX, ReferenceMode.INDEX_TO_DIRECT);
// Copy the data to the UV vertex element
elementUV.setData(uvs);
elementUV.setIndices(uvsId);
```

*شرح*:  
- `Common.createMeshUsingPolygonBuilder()` يبني شبكة على شكل مكعب.  
- `createElementUV` ينشئ عنصر UV لقناة القوام **diffuse**.  
- `setData` و `setIndices` يضيفان فعليًا **add uvs to mesh**، ربطًا بين متجهات UV ومضلعات المكعب.

### Step 4: Print Confirmation

```java
System.out.println("\nUVs have been set up successfully on the cube.");
```

إذا قمت بتشغيل البرنامج، يجب أن ترى رسالة التأكيد في وحدة التحكم، مما يدل على أن خطوة تخطيط UV اكتملت دون أخطاء.

## Common Issues and Solutions

| المشكلة | سبب حدوثها | الحل |
|-------|----------------|-----|
| **تظهر UVs مشوهة** | ترتيب غير في `uvsId` أو ترتيب مضلع غير متطابق. | تحقق من أن مصفوفة الفهارس تتطابق مع ترتيب مضلع الشبكة. |
| **القوام غير مرئي** | مجموعة UV مرتبطة بقناة القوام الخاطئة. | استخدم `TextureMapping.DIFFUSE` للقوام الرئيسي؛ القنوات الأخرى (NORMAL، SPECULAR) تحتاج إلى مجموعات UV منفصلة. |
| **استثناء وقت التشغيل `NullPointerException`** | `Common.createMeshUsingPolygonBuilder()` أعاد قيمة `null`. | تأكد من استيراد فئة المساعد بشكل صحيح وتنفيذ الطريقة. |

## Frequently Asked Questions

**س: هل يمكنني تطبيق إحداثيات UV على نماذج ثلاثية الأبعاد معقدة؟**  
**ج:** نعم. نفس سير العمل يعمل مع أي شبكة — فقط قدم مصفوفة UV أكبر وقائمة فهارس مطابقة.

**س: أين يمكنني العثور على موارد إضافية ودعم لـ Aspose.3D؟**  
**ج:** زر [توثيق Aspose.3D](https://reference.aspose.com/3d/java/) للحصول على مراجع API مفصلة، و[منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) للحصول على مساعدة المجتمع.

**س: هل هناك نسخة تجريبية مجانية متاحة لـ Aspose.3D؟**  
**ج:** بالتأكيد. يمكنك تنزيل نسخة تجريبية كاملة الوظائف من [صفحة إصدارات Aspose.3D](https://releases.aspose.com/).

**س: كيف يمكنني الحصول على رخصة مؤقتة لـ Aspose.3D؟**  
**ج:** تُوفر الرخص المؤقتة [هنا](https://purchase.aspose.com/temporary-license/).

**س: أين يمكنني شراء Aspose.3D؟**  
**ج:** خيارات الشراء مدرجة في [صفحة شراء Aspose.3D الرسمية](https://purchase.aspose.com/buy).

---

**آخر تحديث:** 2025-12-09  
**تم الاختبار باستخدام:** Aspose.3D 24.12 for Java  
**المؤلف:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}