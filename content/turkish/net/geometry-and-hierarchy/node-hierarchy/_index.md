---
title: Düğüm Hiyerarşisini Anlamak
linktitle: Düğüm Hiyerarşisini Anlamak
second_title: Aspose.3D .NET API'si
description: Aspose.3D for .NET'in gücünün kilidini açın! Bu adım adım kılavuzla düğüm hiyerarşisi manipülasyonuna dalın. Çarpıcı 3D sahneleri zahmetsizce oluşturun.
type: docs
weight: 16
url: /tr/net/geometry-and-hierarchy/node-hierarchy/
---
## giriiş

Geliştiricilerin .NET uygulamalarındaki 3D sahneler ve modellerle sorunsuz bir şekilde çalışmasını sağlayan güçlü bir kütüphane olan Aspose.3D for .NET dünyasına hoş geldiniz. Bu eğitimde Aspose.3D'yi kullanarak 3D sahnelerdeki düğüm hiyerarşisini anlamanın inceliklerini inceleyeceğiz. Bu kılavuzun sonunda, 3 boyutlu sahnelerin yapısını düğümler aracılığıyla nasıl değiştireceğiniz konusunda sağlam bir kavrayışa sahip olacak ve çarpıcı görsel deneyimler yaratabileceksiniz.

## Önkoşullar

Bu 3D yolculuğa çıkmadan önce aşağıdaki önkoşulların mevcut olduğundan emin olun:

-  Aspose.3D for .NET Kütüphanesi: Aspose.3D kütüphanesinin .NET projenize entegre olduğundan emin olun. Bunu henüz yapmadıysanız, şu adrese gidin:[dokümantasyon](https://reference.aspose.com/3d/net/) rehberlik için.

-  Kütüphaneyi İndirin: Aspose.3D kütüphanesini indirmediyseniz, en son sürümü şuradan edinin:[İndirme: {link](https://releases.aspose.com/3d/net/) ve belgelerde verilen kurulum talimatlarını izleyin.

-  Lisans Alın: Aspose.3D'nin tüm potansiyelini açığa çıkarmak için geçerli bir lisansa ihtiyacınız var. Elinizde yoksa edinebilirsiniz[Burada](https://purchase.aspose.com/buy) veya birini tercih edin[ücretsiz deneme](https://releases.aspose.com/) yeteneklerini keşfetmek için.

-  Destek ve Topluluk: Aspose.3D topluluğuna katılın[destek Forumu](https://forum.aspose.com/c/3d/18)diğer geliştiricilerle bağlantı kurmak, yardım istemek ve en son gelişmelerden haberdar olmak için.

-  Geçici Lisans (İsteğe Bağlı): Bir satın alma işlemi yapmadan önce Aspose.3D'yi araştırıyorsanız, bir geçici Lisans almayı düşünün.[geçici lisans](https://purchase.aspose.com/temporary-license/) genişletilmiş erişim için.

Artık araçlarımız hazır olduğuna göre Aspose.3D'yi kullanarak 3D düğüm hiyerarşisi manipülasyonunun heyecan verici dünyasına dalalım.

## Ad Alanlarını İçe Aktar

.NET projenizde Aspose.3D'nin sağladığı işlevsellikten yararlanmak için gerekli ad alanlarını içe aktardığınızdan emin olun. Kodunuza aşağıdaki satırları ekleyin:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

Bu ad alanları, 3B sahnelerle çalışmaya yönelik temel sınıflara ve yöntemlere erişmenizi sağlayacaktır.

## Adım 1: Sahne Nesnesini Başlatın

```csharp
Scene scene = new Scene();
```

 kullanarak yeni bir 3B sahne oluşturarak başlayın.`Scene` sınıf.

## 2. Adım: Alt Düğümler Oluşturun

```csharp
Node top = scene.RootNode.CreateChildNode();
Node cube1 = top.CreateChildNode("cube1");
Node cube2 = top.CreateChildNode("cube2");
```

 Düğümler arasında ebeveyn-çocuk ilişkileri oluşturarak hiyerarşik bir yapı oluşturun. Bu örnekte,`cube1` Ve`cube2` alt düğümleridir`top` düğüm.

## Adım 3: Mesh Oluşturun ve Atayın

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
cube1.Entity = mesh;
cube2.Entity = mesh;
```

 Uygun bir yöntem kullanarak bir ağ oluşturun (burada,`CreateMeshUsingPolygonBuilder`) ve onu alt düğümlere atayın.

## Adım 4: Çevirileri Ayarlayın

```csharp
cube1.Transform.Translation = new Vector3(-10, 0, 0);
cube2.Transform.Translation = new Vector3(10, 0, 0);
```

Her küp düğümü için çevirileri tanımlayın ve bunları 3B alanda konumlandırın.

## Adım 5: Rotasyonu Ana Düğüme Uygulayın

```csharp
top.Transform.Rotation = Quaternion.FromEulerAngle(Math.PI, 4, 0);
```

Ana düğümü döndürün (`top`) ve bu dönüşümün tüm alt düğümlerini nasıl etkilediğini gözlemleyin.

## Adım 6: 3D Sahneyi Kaydedin

```csharp
string output = "Your Output Directory" + "NodeHierarchy.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Çıkış dizinini belirtin ve 3D sahneyi istediğiniz dosya formatında (burada FBX7500ASCII) kaydedin.

## Adım 7: Başarı Mesajını Görüntüleyin

```csharp
Console.WriteLine("\nNode hierarchy added successfully to document.\nFile saved at " + output);
```

Kullanıcıyı düğüm hiyerarşisinin başarıyla eklendiği ve kaydedilen dosya konumu hakkında bilgilendirin.

## Çözüm

Tebrikler! Aspose.3D for .NET'te 3D düğüm hiyerarşisinin karmaşık dünyasında başarıyla gezindiniz. Bu eğitim sizi 3B sahneleri kolaylıkla oluşturma, değiştirme ve kaydetme bilgisiyle donattı. Yolculuğunuza devam ederken daha fazla özelliği keşfedin ve .NET projelerinizde Aspose.3D'nin tüm potansiyelini ortaya çıkarın.

## SSS'ler

### S1: Aspose.3D for .NET'i lisans olmadan kullanabilir miyim?

Cevap1: Lisans tüm özelliklerin kilidini açarken, ücretsiz denemeyi kullanarak Aspose.3D'yi sınırlı yeteneklerle keşfedebilirsiniz.

### S2: 3D sahneleri kaydetmek için desteklenen başka dosya formatları var mı?

Cevap2: Evet, Aspose.3D çeşitli formatları destekler; kapsamlı bir liste için belgelere bakın.

### S3: Aspose.3D topluluğuna nasıl katkıda bulunabilirim?

Cevap 3: Destek forumuna katılın, deneyimlerinizi paylaşın ve diğerlerinin sorularına yardımcı olarak katkıda bulunun.

### S4: Aspose.3D oyun geliştirmeye uygun mu?

Cevap4: Kesinlikle! Aspose.3D çok yönlüdür ve oyun geliştirme projelerine entegre edilebilir.

### S5: Geçici lisans ile tam lisans arasındaki fark nedir?

Cevap5: Geçici lisans, değerlendirme amacıyla kısa süreli erişim sağlarken, tam lisans sınırsız kullanım sunar.