---
date: 2026-03-23
description: Aspose.3D for .NET kullanarak bükülmüş ekstrüzyon oluşturmayı öğrenin.
  Bu adım adım rehber, lineer ekstrüzyon bükülme tekniklerini kapsar.
linktitle: Twist in Linear Extrusion
second_title: Aspose.3D .NET API
title: Doğrusal Ekstrüzyonda Bükülmeli Ekstrüzyon Nasıl Oluşturulur
url: /tr/net/3d-modeling/linear-extrusion/twist-in-linear-extrusion/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Doğrusal Ekstrüzyonda Burulmalı Ekstrüzyon Nasıl Oluşturulur

## Introduction

Eğer göz alıcı 3D görsellere ihtiyaç duyan .NET uygulamaları geliştiriyorsanız, **ekstrüzyon nasıl oluşturulur** sorusunun temel bir beceri olduğunu yakında keşfedeceksiniz. Aspose.3D for .NET, basit 2‑D profilleri sofistike 3‑D modellere dönüştürmek için temiz ve yüksek performanslı bir API sunar—özellikle bir burulma eklediğinizde. Bu öğreticide sahneyi kurmaktan son OBJ dosyasını kaydetmeye kadar her adımı adım adım göstereceğiz, böylece doğrusal ekstrüzyon burulması gücünü aksiyon içinde görebileceksiniz.

## Quick Answers
- **What is the primary class for extrusion?** `LinearExtrusion`
- **Which property adds rotation?** `Twist`
- **How many slices give smooth results?** Around 100 slices (adjust as needed)
- **Can I use other shapes?** Yes, any `IProfile` such as circles, polygons, or custom curves
- **What file format is used in the example?** Wavefront OBJ (`.obj`)

## Prerequisites

Başlamadan önce aşağıdakilere sahip olduğunuzdan emin olun:

- Aspose.3D for .NET yüklü. Henüz indirmediyseniz **[buradan](https://releases.aspose.com/3d/net/)** edinebilirsiniz.
- Çalışan bir .NET geliştirme ortamı (Visual Studio, VS Code veya tercih ettiğiniz herhangi bir IDE).
- C# sözdizimi ve nesne‑yönelimli kavramlara temel aşinalık.

## Import Namespaces

Her .NET projesinde, ad alanlarının doğru kullanımı çok önemlidir. Aspose.3D işlevselliğinden etkili bir şekilde yararlanmak için gerekli ad alanlarını içe aktararak başlayın. İşte size rehber olacak bir kod parçacığı:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Step‑by‑Step Guide

### Step 1: Initialize the Base Profile

Ekstrüde edilecek şekli tanımlayarak başlıyoruz. Bu örnekte kenarları hafif bir eğri vermek için küçük bir yuvarlama yarıçapına sahip bir dikdörtgen kullanıyoruz.

```csharp
// Initialize the base profile to be extruded
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

### Step 2: Create a 3D Scene

`Scene` nesnesi, tüm 3‑D varlıkların yaşadığı bir tuval görevi görür. Bunu ekstrüzyonunuzun sahnesi olarak düşünebilirsiniz.

```csharp
// Create a scene 
Scene scene = new Scene();
```

### Step 3: Add Left and Right Nodes

Düğümler, nesneleri hiyerarşik olarak düzenlemenizi sağlar. Bir düz ekstrüzyon ve bir de burulmuş versiyon için iki kardeş düğüm oluşturacağız.

```csharp
// Create left node
var left = scene.RootNode.CreateChildNode();
// Create right node
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
```

### Step 4: Perform Linear Extrusion with Twist on the Left Node

`Twist` özelliği, profil ekstrüde edilirken ne kadar döneceğini kontrol eder. **0** olarak ayarlandığında klasik düz bir ekstrüzyon elde edilir.

```csharp
// Twist property defines the degree of the rotation while extruding the profile
// Perform linear extrusion on the left node using twist and slices property
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 0, Slices = 100 });
```

### Step 5: Perform Linear Extrusion with Twist on the Right Node

Şimdi aynı profile %90’lık bir burulma uyguluyoruz. Bu, **linear extrusion twist** etkisini net bir şekilde gösterir.

```csharp
// Perform linear extrusion on the right node using twist and slices property
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 90, Slices = 100 });
```

### Step 6: Save the 3D Scene

Son olarak sahneyi, herhangi bir 3‑D görüntüleyicide açabileceğiniz bir formata dışa aktarın. Örnekte Wavefront OBJ kullanılmıştır, ancak Aspose.3D birçok başka formatı da destekler.

```csharp
// Save 3D scene
scene.Save("Your Output Directory" + "TwistInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Why Use Linear Extrusion with a Twist?

- **Rapid prototyping:** Turn 2‑D sketches into 3‑D parts without manual modeling.
- **Design flexibility:** Adjust the `Twist` value to create spirals, helical ribs, or decorative features.
- **Performance‑friendly:** The `Slices` parameter lets you balance visual fidelity and runtime speed.

## Common Issues & Tips

- **Too many slices:** While 100 slices look smooth, extremely high values may slow down rendering. Test with lower counts if performance becomes a concern.
- **Negative twist values:** A negative `Twist` rotates in the opposite direction—useful for mirrored designs.
- **File paths:** Ensure the output directory exists and you have write permissions; otherwise `scene.Save` will throw an exception.

## Conclusion

Bu öğreticide **ekstrüzyon nasıl oluşturulur** sorusunu, Aspose.3D for .NET kullanarak bir burulma ile gösterdik. `Twist` ve `Slices` özelliklerini ayarlayarak basit burulmuş çubuklardan karmaşık helisel yapılara kadar çok çeşitli şekiller oluşturabilirsiniz; tümü sadece birkaç satır kodla mümkün.

## Frequently Asked Questions

**Q: Can I apply linear extrusion with a twist to other shapes?**  
A: Absolutely! Any class that implements `IProfile`—such as `CircleShape`, `PolygonShape`, or a custom spline—can be extruded with a twist.

**Q: What does the `Twist` property actually represent?**  
A: It specifies the total rotation angle (in degrees) applied to the profile over the extrusion length.

**Q: Will increasing the number of slices affect memory usage?**  
A: Yes, more slices generate more vertices and faces, which consumes additional memory and may impact performance on low‑end devices.

**Q: Can I combine linear extrusion with other Aspose.3D features?**  
A: Definitely. You can apply materials, textures, or even Boolean operations after extrusion to create even richer models.

**Q: Where can I get help or discuss ideas with other developers?**  
A: Join the Aspose.3D community at **[Aspose Forum](https://forum.aspose.com/c/3d/18)** for support, samples, and discussions.

---

**Last Updated:** 2026-03-23  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}