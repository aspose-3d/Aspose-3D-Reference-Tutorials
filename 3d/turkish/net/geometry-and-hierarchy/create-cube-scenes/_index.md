---
date: 2026-04-12
description: Aspose.3D for .NET kullanarak küp sahneleri oluşturmayı ve sahneyi FBX
  olarak kaydetmeyi öğrenin – adım adım kılavuz, ön koşullar ve kod örnekleri.
keywords:
- how to create cube
- how to export fbx
- add mesh to node
- export scene as fbx
- save scene as fbx
linktitle: Küp Sahneleri Oluşturma
second_title: Aspose.3D .NET API
title: Aspose.3D for .NET ile küp sahneleri nasıl oluşturulur
url: /tr/net/geometry-and-hierarchy/create-cube-scenes/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for .NET ile küp sahneleri nasıl oluşturulur

## Giriş

Basit bir 3‑D küpü hayata geçirmeye hazır mısınız? Bu öğreticide Aspose.3D for .NET ile **küp sahneleri nasıl oluşturulur** öğrenecek, modeli bir FBX dosyası olarak dışa aktaracak ve sonucu anında göreceksiniz. Bir oyun varlığı prototipleiyor ya da verileri görselleştiriyor olun, aşağıdaki adımlar size dokular, ışıklandırma veya animasyon ekleyebileceğiniz sağlam bir temel sağlayacak.

## Hızlı Yanıtlar
- **Bu öğretici neyi kapsıyor?** Bir küp ağı oluşturma, ağı düğüme ekleme ve sahneyi FBX dosyası olarak kaydetme.  
- **Hangi kütüphane gerekli?** Aspose.3D for .NET (ücretsiz deneme mevcut).  
- **Örneği çalıştırmak için lisansa ihtiyacım var mı?** Geliştirme ve test için geçici veya deneme lisansı yeterlidir.  
- **Hangi IDE'yi kullanabilirim?** .NET uyumlu herhangi bir IDE (Visual Studio, Rider, VS Code).  
- **Ne kadar sürer?** Kodu yazmak, derlemek ve çalıştırmak yaklaşık 10 dakika.

## Aspose.3D ile küp sahneleri nasıl oluşturulur

Bir küp sahnesi, 3‑D grafiklerin “Hello World” örneğidir. Size, ağ oluşturma aşamasından **sahneyi FBX olarak dışa aktarma** aşamasına kadar olan iş akışınızın doğru çalıştığını doğrulama imkanı verir. Aşağıda her adımı adım adım inceleyecek, “neden”ini açıklayacak ve kodu tam olarak nereye yerleştirmeniz gerektiğini göstereceğiz.

## 3D küp sahnesi nedir?

Bir 3D küp sahnesi, sahne grafiği içinde yer alan tek bir küp geometrisinden oluşan minimal üç boyutlu bir modeldir. 3D grafiklerin “Hello World” örneği olarak hizmet eder ve iş akışınızın – ağ oluşturma ve dosya dışa aktarımı – doğru çalıştığını doğrulamanızı sağlar.

## Neden Aspose.3D ile küp sahneleri oluşturmalısınız?

* **Çapraz format desteği:** Ek dönüştürücüler olmadan FBX, STL, OBJ ve birçok diğer formata dışa aktarım.  
* **Saf .NET API:** Yerel bağımlılık yok, C# geliştiricileri için mükemmel.  
* **Zengin özellik seti:** Yerleşik ağ oluşturucular, malzeme işleme ve sahne hiyerarşi yönetimi.  
* **Hızlı prototipleme:** Birkaç satır kod yazarak kullanıma hazır bir 3D dosya elde edin.  

## Önkoşullar

1. **Aspose.3D for .NET Kütüphanesi** – [Aspose belgelerinden](https://reference.aspose.com/3d/net/) indirin ve kurun.  
2. **Geliştirme Ortamı** – Visual Studio 2022, Rider veya .NET 6+ destekleyen herhangi bir editör.  
3. **Temel C# bilgisi** – sınıflar, nesneler ve konsol uygulamalarıyla rahat olmalısınız.

## Ad Alanlarını İçe Aktarın

İlk olarak, derleyicinin Aspose.3D tiplerinin nerede olduğunu bilmesi için gerekli `using` ifadelerini ekleyin.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
```

## Adım adım kılavuz

### Adım 1: Sahneyi Başlat

Tüm düğümleri, ağları, ışıkları ve kameraları tutacak boş bir `Scene` nesnesi oluşturun.

```csharp
// ExStart:CreateCubeScene
// Initialize scene object
Scene scene = new Scene();
```

### Adım 2: Küp için bir Düğüm Oluşturun

`Node`, geometri için bir kapsayıcı görevi görür. Hiyerarşide daha sonra bulabilmeniz için ona anlaşılır bir ad verin.

```csharp
// Initialize Node class object
Node cubeNode = new Node("cube");
```

### Adım 3: Ağı Oluşturun

Aspose.3D, çokgen oluşturucu kullanarak bir küp ağı üretebilen `Common` adlı bir yardımcı sağlar. Bu, köşe ve yüzleri manuel olarak tanımlamanızı engeller.

```csharp
// Call Common class create mesh using polygon builder method to set mesh instance 
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

### Adım 4: Ağı Düğüme Ekle

Az önce oluşturduğunuz ağı düğümün `Entity` özelliğine atayın. Bu, geometriyi sahne grafiğiyle bağlar.

```csharp
// Point node to the Mesh geometry
cubeNode.Entity = mesh;
```

### Adım 5: Düğümü Sahneye Ekle

Küp düğümünü sahnenin köküne ekleyin, böylece nihai çıktının bir parçası olur.

```csharp
// Add Node to a scene
scene.RootNode.ChildNodes.Add(cubeNode);
```

### Adım 6: FBX Nasıl Dışa Aktarılır (sahneyi FBX olarak kaydet)

Bir çıktı yolu seçin ve sahneyi dışa aktarın. Burada, 3D editörler tarafından yaygın olarak desteklenen FBX 7400 ASCII formatını kullanıyoruz.

```csharp
// The path to the documents directory.
var output = "Your Output Directory" + "CubeScene.fbx";

// Save 3D scene in the supported file formats
scene.Save(output, FileFormat.FBX7400ASCII);
```

### Adım 7: Başarı Mesajını Göster

Kullanıcıya dosyanın başarıyla yazıldığını açık bir şekilde bildirin.

```csharp
Console.WriteLine("\nCube Scene created successfully.\nFile saved at " + output);
```

## Yaygın sorunlar ve çözümler

| Sorun | Neden oluşur | Çözüm |
|-------|--------------|-------|
| **File not found** hatası `scene.Save` çalıştırılırken | Çıktı dizini mevcut değil veya yazma izniniz yok. | Önce dizini oluşturun (`Directory.CreateDirectory`) veya sahip olduğunuz mutlak bir yol kullanın. |
| **Boş dosya** dışa aktardıktan sonra | Ağ düğüme eklenmemiş veya düğüm sahneye eklenmemiş. | `cubeNode.Entity = mesh;` ve `scene.RootNode.ChildNodes.Add(cubeNode);` ifadelerinin çalıştırıldığından emin olun. |
| **Yanlış format** bir görüntüleyicide açarken | Yanlış `FileFormat` enum değeri kullanılıyor. | ASCII FBX için `FileFormat.FBX7400ASCII`, ikili için `FileFormat.FBX7400Binary` kullanın. |

## Sıkça Sorulan Sorular

**S: Aspose.3D farklı 3D dosya formatlarıyla uyumlu mu?**  
C: Evet, Aspose.3D FBX, STL, OBJ, GLTF ve daha birçok formatı destekler; tek bir kod satırıyla **sahneyi FBX olarak kaydedebilir** veya diğer formatlara dönüştürebilirsiniz.

**S: Küpün görünümünü özelleştirebilir miyim?**  
C: Kesinlikle. Ağa bir `Material` atayabilir, rengini değiştirebilir veya `Material` sınıfını kullanarak bir doku uygulayabilirsiniz.

**S: Ek destek ve kaynakları nerede bulabilirim?**  
C: Topluluk yardımı ve tartışmalar için [Aspose.3D forumunu](https://forum.aspose.com/c/3d/18) ziyaret edin.

**S: Ücretsiz deneme mevcut mu?**  
C: Evet, ücretsiz deneme sürümünü [buradan](https://releases.aspose.com/) inceleyebilirsiniz.

**S: Aspose.3D için geçici bir lisans nasıl alabilirim?**  
C: Geçici bir lisansı [buradan](https://purchase.aspose.com/temporary-license/) edinebilirsiniz.

## Sonuç

Bu rehberde **küp sahneleri nasıl oluşturulur** adım adım gösterdik; `Scene`'i başlatmaktan **sahneyi FBX olarak dışa aktarmaya** kadar. Artık daha karmaşık geometrilerle denemeler yapabilir, dokular, ışıklar ekleyebilir ve hatta modellerinizi canlandırabilirsiniz. Aspose.3D API'yi keşfetmeye devam edin – olasılıklar neredeyse sınırsız.

**Son Güncelleme:** 2026-04-12  
**Test Edilen:** Aspose.3D for .NET 24.11 (yazım zamanındaki en son sürüm)  
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}