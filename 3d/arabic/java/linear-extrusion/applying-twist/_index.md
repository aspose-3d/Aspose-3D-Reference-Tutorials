---
date: 2025-12-17
description: تعلم كيفية إنشاء نموذج ثلاثي الأبعاد ملتوي باستخدام Aspose.3D للـ Java
  مع لفّ استخراج خطي وتصدير ملف OBJ بلغة Java. اتبع دليلنا خطوة بخطوة.
linktitle: Applying Twist in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: إنشاء نموذج ثلاثي الأبعاد ملتوي – تطبيق الالتواء في البثق الخطي باستخدام Aspose.3D
  لجافا
url: /ar/java/linear-extrusion/applying-twist/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# تطبيق الالتواء في البثق الخطي باستخدام Aspose.3D للـ Java

## المقدمة

مرحبًا بك في هذا الدليل خطوة بخطوة حول **كيفية إنشاء نموذج ثلاثي الأبعاد ملتوي** عن طريق تطبيق الالتواء أثناء البثق الخطي باستخدام Aspose.3D للـ Java. سواءً كنت تبني تصورات معمارية، أو أصول ألعاب، أو نماذج أولية هندسية، فإن إضافة الالتواء يمكن أن تعطي هندستك مظهرًا ديناميكيًا حلزونياً ببضع أسطر من الشيفرة فقط.

## إجابات سريعة
- **ما معنى “الالتواء” في البثق؟** إنه يدور الملف حول محور البثق أثناء تمديد الشكل.  
- **أي فئة API تتعامل مع الالتواء؟** `LinearExtrusion` توفر طريقة `setTwist`.  
- **هل أحتاج إلى ترخيص لتشغيل المثال؟** النسخة التجريبية المجانية تكفي للتقييم؛ يلزم ترخيص تجاري للإنتاج.  
- **هل يمكنني تصدير النتيجة كملف OBJ؟** نعم، استخدم `scene.save(..., FileFormat.WAVEFRONTOBJ)`.  
- **ما نسخة Java المطلوبة؟** Java 8 أو أحدث مدعومة بالكامل.

## المتطلبات المسبقة

قبل الغوص في الدليل، تأكد من توفر المتطلبات التالية:

- بيئة تطوير Java: تأكد من تثبيت Java على نظامك.  
- مكتبة Aspose.3D: قم بتنزيل وتثبيت مكتبة Aspose.3D للـ Java من [رابط التحميل](https://releases.aspose.com/3d/java/).  
- الوثائق: راجع [وثائق Aspose.3D](https://reference.aspose.com/3d/java/) للحصول على إرشادات شاملة.

## استيراد الحزم

قبل بدء عملية الترميز، استورد الحزم اللازمة إلى مشروع Java الخاص بك. إليك مثالًا على كيفية القيام بذلك:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## تعيين دليل المستند

أولاً، حدد المكان الذي سيتم حفظ ملف الـ 3D المُولد فيه.

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## تهيئة الملف الأساسي

بعد ذلك، أنشئ الشكل الذي سيتم بُثه. في هذا المثال نستخدم مستطيلًا مع نصف قطر تقويس صغير.

```java
// ExStart:InitializeBaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:InitializeBaseProfile
```

## إنشاء مشهد

كائن `Scene` يعمل كحاوية لجميع العقد ثلاثية الأبعاد.

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
```

## إنشاء العقد

أضف عقدتين فرعيتين إلى المشهد – واحدة ستبقى مستقيمة، والأخرى ستتلقى الالتواء.

```java
// ExStart:CreateNodes
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CreateNodes
```

## الالتواء في البثق الخطي

الآن نقوم بتنفيذ **الالتواء في البثق الخطي** على كلتا العقدتين. العقدة اليسرى تحصل على التواء 0° (مستقيمة)، بينما العقدة اليمنى تحصل على التواء 90°، مما يخلق شكلًا حلزونياً. كما نحدد عدد الشرائح لضمان هندسة ناعمة.

```java
// ExStart:LinearExtrusionWithTwist
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd:LinearExtrusionWithTwist
```

## تصدير ملف OBJ في Java

أخيرًا، احفظ المشهد بصيغة OBJ المدعومة على نطاق واسع. هذا يوضح قدرة **تصدير ملف OBJ في Java** في Aspose.3D.

```java
// ExStart:Save3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:Save3DScene
```

## لماذا هذا مهم

إنشاء نموذج ثلاثي الأبعاد ملتوي يمنحك تأثيرًا بصريًا قويًا دون الحاجة إلى أدوات نمذجة خارجية. وهو مفيد بشكل خاص لـ:

- **الأجزاء الميكانيكية** التي تحتاج إلى ميزات حلزونية (مثل النوابض، البراغي).  
- **التصاميم الفنية** حيث يضيف اللولب الخفيف اهتمامًا بصريًا.  
- **أصول الألعاب** التي تستفيد من الهندسة منخفضة البوليغون، المولدة إجرائيًا.

## المشكلات الشائعة والنصائح

| المشكلة | الحل |
|---------|------|
| الالتواء يبدو مسطحًا أو مفقودًا | تأكد من أن `setSlices` عالية بما فيه الكفاية (مثلاً 100) للحصول على دوران سلس. |
| ملف OBJ لا يفتح في العارض | تحقق من أن مسار الإخراج (`MyDir`) صحيح وأن الملف لديه أذونات كتابة. |
| تحجيم غير متوقع | تحقق من نظام الوحدات للملف المصدر؛ Aspose.3D يعمل بالمتر افتراضيًا. |

## الأسئلة المتكررة

**س: هل يمكنني استخدام Aspose.3D للـ Java للعمل مع صيغ ملفات 3D أخرى؟**  
ج: نعم، يدعم Aspose.3D مجموعة واسعة من الصيغ مثل FBX و STL و 3MF وغيرها.

**س: أين يمكنني العثور على دعم Aspose.3D للـ Java؟**  
ج: زر [منتدى Aspose.3D](https://forum.aspose.com/c/3d/18) للحصول على مساعدة المجتمع والمساعدة الرسمية.

**س: هل هناك نسخة تجريبية مجانية متاحة؟**  
ج: نعم، يمكنك تنزيل نسخة تجريبية من [هنا](https://releases.aspose.com/).

**س: كيف أحصل على ترخيص مؤقت للاختبار؟**  
ج: احصل على ترخيص مؤقت من [صفحة الترخيص المؤقت](https://purchase.aspose.com/temporary-license/).

**س: أين يمكنني شراء ترخيص كامل؟**  
ج: اشترِ Aspose.3D للـ Java من [صفحة الشراء](https://purchase.aspose.com/buy).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**آخر تحديث:** 2025-12-17  
**تم الاختبار مع:** Aspose.3D 24.11 للـ Java  
**المؤلف:** Aspose  

---