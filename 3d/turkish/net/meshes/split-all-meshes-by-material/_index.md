---
title: Sahnenin Tüm Ağlarını Malzemeye Göre Bölme
linktitle: Sahnenin Tüm Ağlarını Malzemeye Göre Bölme
second_title: Aspose.3D .NET API'si
description: Aspose.3D for .NET kullanarak 3D ağları malzemeye göre nasıl böleceğinizi öğrenin. 3D modellerin verimli organizasyonu ve yönetimi için adım adım kılavuzumuzu izleyin.
weight: 21
url: /tr/net/meshes/split-all-meshes-by-material/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Sahnenin Tüm Ağlarını Malzemeye Göre Bölme

## giriiş
Aspose.3D for .NET kullanarak bir 3D sahnenin tüm ağlarını malzemeye göre bölmeyi anlatan bu adım adım kılavuza hoş geldiniz. 3D modellerle çalışıyorsanız ve ağlarınızı malzemelere göre verimli bir şekilde düzenlemek istiyorsanız bu eğitim tam size göre. Aspose.3D, 3D dosyalarla çalışmak için çeşitli özellikler sunan güçlü bir .NET kitaplığıdır ve bu da onu geliştiriciler için mükemmel bir seçim haline getirir.
## Önkoşullar
Eğiticiye dalmadan önce aşağıdaki önkoşullara sahip olduğunuzdan emin olun:
- C# programlama dilinin temel anlayışı.
- Makinenizde Visual Studio yüklü.
-  Aspose.3D for .NET kitaplığı. Şuradan indirebilirsiniz[Burada](https://releases.aspose.com/3d/net/).
- Bölmek istediğiniz bir 3B giriş dosyası (örneğin, "test.fbx").
## Ad Alanlarını İçe Aktar
C# projenize gerekli ad alanlarını içe aktararak başlayın:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```
## Adım 1: 3D Dosyayı Yükleyin
```csharp
// Belgeler dizininin yolu.
string input = RunExamples.GetDataFilePath("test.fbx");
// 3D dosya yükleme
Scene scene = new Scene(input);
```
 Bu adımda Aspose.3D'yi kullanarak 3D dosyayı yüklüyoruz.`Scene` sınıf.
## Adım 2: Tüm Meshleri Böl
```csharp
// Tüm ağları böl
PolygonModifier.SplitMesh(scene, SplitMeshPolicy.CloneData);
```
 Burada şunu kullanıyoruz:`SplitMesh` gelen yöntem`PolygonModifier` malzemeye göre tüm ağları bölmek için sınıf.
## 3. Adım: Bölünmüş Sahneyi Kaydedin
```csharp
// Dosyayı kaydet
var output = "Your Output Directory" + "test-splitted.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```
Değişiklikleri korumak için değiştirilen sahneyi yeni bir dosyaya kaydedin.
## Adım 4: Başarı Mesajını Görüntüleyin
```csharp
// Başarı mesajını görüntüle
Console.WriteLine("\nSplitting all meshes of a scene per material successfully.\nFile saved at " + output);
```
İşlemin başarıyla tamamlandığını belirten bir başarı mesajı yazdırın.
## Çözüm
Tebrikler! Aspose.3D for .NET'i kullanarak bir 3D sahnenin tüm ağlarını malzemeye göre nasıl böleceğinizi başarıyla öğrendiniz. Bu, karmaşık 3D modelleri düzenlemek ve yönetmek için değerli bir teknik olabilir.
## SSS
### 1. Aspose.3D for .NET'i diğer programlama dilleriyle birlikte kullanabilir miyim?
Aspose.3D öncelikle .NET için tasarlanmıştır ancak .NET dil bağlantıları aracılığıyla diğer dillerle birlikte çalışabilirlik sağlar.
### 2. Deneme sürümü mevcut mu?
 Evet, ücretsiz deneme sürümüne erişebilirsiniz[Burada](https://releases.aspose.com/).
### 3. Daha fazla örneği ve belgeyi nerede bulabilirim?
 Kapsamlı belgeleri şu adreste keşfedin:[Aspose.3D Belgeleri](https://reference.aspose.com/3d/net/).
### 4. Aspose.3D için nasıl destek alabilirim?
 Ziyaret edin[Aspose.3D forumu](https://forum.aspose.com/c/3d/18) topluluk desteği ve tartışmalar için.
### 5. Geçici lisans alabilir miyim?
 Evet, geçici lisans alabilirsiniz[Burada](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
