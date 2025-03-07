---
title: CancellationToken'ı kullanma
linktitle: CancellationToken'ı kullanma
second_title: Aspose.3D .NET API'si
description: Aspose.3D for .NET ile 3D modellemenin kusursuz dünyasını keşfedin. CancellationToken'ı kullanarak 3D belgeleri verimli bir şekilde yüklemeyi ve kaydetmeyi öğrenin.
weight: 10
url: /tr/net/loading-and-saving/cancellation-token/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# CancellationToken'ı kullanma

## giriiş

3D modelleme ve render projelerinizi geliştirmek için Aspose.3D for .NET'i kullanmaya ilişkin kapsamlı kılavuzumuza hoş geldiniz. Aspose.3D, .NET geliştiricilerinin 3D dosyalarla sorunsuz bir şekilde çalışmasına olanak tanıyan güçlü bir kütüphanedir. Bu eğitimde, özellikle asenkron görevlerin verimli yönetimi için CancellationToken kullanımına odaklanarak yükleme ve kaydetme konularını ele alacağız.

## Önkoşullar

Bu yolculuğa çıkmadan önce aşağıdaki önkoşulların yerine getirildiğinden emin olun:

-  Aspose.3D for .NET: Kitaplığı şuradan indirip yükleyin:[Burada](https://releases.aspose.com/3d/net/).
- .NET Ortamı: Uyumlu bir .NET geliştirme ortamı kurduğunuzdan emin olun.
- Temel C# Anlayışı: C# programlama diline aşinalık önerilir.

## Ad Alanlarını İçe Aktar

Başlamak için projenize gerekli ad alanlarını eklediğinizden emin olun. Bu ad alanları, 3B dosya işleme için gereken işlevlere erişim sağlayacaktır.

```csharp
using Aspose.ThreeD;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
```

## Yükleme ve Kaydetme - CancellationToken'ı Kullanma

### 1. Adım: CancellationTokenSource'u oluşturun

```csharp
// ExStart:CancellationTokenSource

CancellationTokenSource cts = new CancellationTokenSource();
```

Burada, eşzamansız işlemlerde iptali yönetmek için çok önemli bir bileşen olan CancellationTokenSource'u başlatıyoruz.

### 2. Adım: 3D Sahneyi Başlatın

```csharp
Scene scene = new Scene();
```

Scene sınıfının bir örneğini oluşturun. Bu, 3D modelleme faaliyetlerinizin tuvali olacaktır.

### 3. Adım: CancellationToken Zaman Aşımını Ayarlayın

```csharp
cts.CancelAfter(1000);
```

 İptal zaman aşımını şunu kullanarak ayarlayın:`CancelAfter` yöntem. Bu örnekte zaman aşımı 1000 milisaniyeye (1 saniye) ayarlanmıştır.

### Adım 4: 3D Belgeyi Açın

```csharp
try
{
    scene.Open("Your Output Directory" + "document.fbx", cts.Token);
    Console.WriteLine("Import is done within 1000ms");
}
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
```

 3D belgeyi belirtilen zaman dilimi içinde açmayı deneyin.`cts.Token` parametresi, ayarlanan zaman aşımını aşması durumunda işlemin iptal edilebilmesini sağlar.

### Adım 5: İçe Aktarma İstisnasını İşleyin

Bir ImportException durumunda, bunun bir OperationCanceledException'dan kaynaklanıp kaynaklanmadığını kontrol ederek durumu dikkatli bir şekilde ele alın.

```csharp
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
// ExEnd:CancellationTokenSource
```

## Çözüm

Tebrikler! 3D belgelerin yüklenmesini yönetmek için Aspose.3D for .NET'i CancellationToken ile kullanma sürecini başarıyla tamamladınız. Bu teknik, içe aktarma işlemlerinin verimli ve zamanında yapılmasını sağlayarak 3D uygulamalarınızın genel performansını artırır.

## SSS'ler

### S1: Aspose.3D tüm 3D dosya formatlarıyla uyumlu mudur?

 Cevap1: Aspose.3D, FBX, STL, OBJ ve daha fazlasını içeren çok çeşitli 3D dosya formatlarını destekler. Bakın[dokümantasyon](https://reference.aspose.com/3d/net/) tam liste için.

### S2: Aspose.3D için nasıl geçici lisans alabilirim?

 A2: Ziyaret ederek geçici bir lisans alın[bu bağlantı](https://purchase.aspose.com/temporary-license/).

### S3: Aspose.3D desteğini nerede bulabilirim?

 A3: Topluluk tartışmasına katılın[Aspose.3D forumu](https://forum.aspose.com/c/3d/18).

### S4: Satın almadan önce Aspose.3D'yi ücretsiz deneyebilir miyim?

 Cevap4: Evet, ücretsiz deneme sürümüyle özellikleri keşfedin[Burada](https://releases.aspose.com/).

### S5: Aspose.3D for .NET'in en son sürümü nedir?

 Cevap5: Kontrol ederek güncel kalın[indirme sayfası](https://releases.aspose.com/3d/net/) son sürüm için.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
