---
title: Torus Primitive'i Mesh'e Dönüştürme
linktitle: Torus Primitive'i Mesh'e Dönüştürme
second_title: Aspose.3D .NET API'si
description: Aspose.3D for .NET'in gücünü, Torus temel öğelerini ağlara dönüştürmeye ilişkin adım adım kılavuzumuzla keşfedin. 3D geliştirmenizi zahmetsizce yükseltin!
type: docs
weight: 17
url: /tr/net/objects/convert-torus-primitive-to-mesh/
---
## giriiş
Aspose.3D for .NET'in gücünden yararlanarak Torus primitifini sorunsuz bir şekilde ağa dönüştürmek için istekli misiniz? Başka yerde arama! Bu eğitimde, sorunsuz bir yolculuk sağlamak için her adımı parçalara ayırarak süreç boyunca size yol göstereceğiz. Aspose.3D for .NET, 3D sahneleri işlemek için sağlam bir platform sağlayarak, onu verimlilik ve esneklik arayan geliştiricilerin başvuracağı bir araç haline getiriyor.
## Önkoşullar
Eğiticiye dalmadan önce aşağıdaki önkoşulların yerine getirildiğinden emin olun:
-  Aspose.3D for .NET: Kitaplığı indirin ve yükleyin. İndirme linkini bulabilirsiniz[Burada](https://releases.aspose.com/3d/net/).
-  3D Dosya: Desteklenen formatta örnek bir 3D dosya hazırlayın. Eğer bir tane yoksa, kullanabilirsiniz.[test.fbx](https://reference.aspose.com/3d/net/) Aspose.3D belgelerinden dosya.
## Ad Alanlarını İçe Aktar
Aspose.3D ile sorunsuz entegrasyon sağlamak için .NET projenize gerekli ad alanlarını içe aktarın. Kodunuzun başına şunu ekleyin:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```
## 1. Adım: 3D Dosya Yükleyin
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("test.fbx"));
```
3D dosyanızı sahneye yükleyin. Yer değiştirmek`"test.fbx"` dosyanızın yolu ile birlikte.
## Adım 2: Düğüm Sınıfı Nesnesini Başlatın
```csharp
Node torusNode = new Node("torus");
```
Torus temel öğesi için yeni bir düğüm nesnesi oluşturun.
## Adım 3: Torus'u Mesh'e Dönüştürün
```csharp
IMeshConvertible convertible = new Torus();
Mesh mesh = convertible.ToMesh();
```
Torus primitifini ağa dönüştürmek için Aspose.3D'nin özelliklerinden yararlanın.
## Adım 4: Düğümü Mesh Geometrisine Noktalayın
```csharp
torusNode.Entity = mesh;
```
Mesh geometrisini düğümle ilişkilendirin.
## Adım 5: Sahneye Düğüm Ekleme
```csharp
scene.RootNode.ChildNodes.Add(torusNode);
```
Torus düğümünü sahneye entegre edin.
## Adım 6: 3D Sahneyi Kaydet
```csharp
var output = "Your Output Directory" + "TorusToMeshScene.fbx";
scene.Save(output, FileFormat.FBX7400ASCII);
Console.WriteLine("\nConverted the primitive Torus to a mesh successfully.\nFile saved at " + output);
```
Değiştirilen 3B sahneyi istediğiniz dosya formatında ve konumda kaydedin.
## Çözüm
Tebrikler! Aspose.3D for .NET'i kullanarak bir Torus temel öğesini başarıyla bir ağa dönüştürdünüz. Bu güçlü kitaplık, .NET projelerinizde 3B manipülasyon için bir olasılıklar dünyasının kapılarını açar.
## SSS
### Aspose.3D tüm 3D dosya formatlarıyla uyumlu mu?
Aspose.3D çok çeşitli 3D dosya formatlarını destekler. Tam liste için belgelere bakın.
### Aspose.3D'yi ticari projeler için kullanabilir miyim?
 Evet, Aspose.3D ticari lisanslar sunmaktadır. Ziyaret etmek[satın alma.aspose.com/buy](https://purchase.aspose.com/buy) detaylar için.
### Test amaçlı geçici lisanslar var mı?
 Evet, geçici lisans alabilirsiniz[Burada](https://purchase.aspose.com/temporary-license/) test için.
### Aspose.3D desteğini nerede bulabilirim?
 Ziyaret edin[Aspose.3D forumu](https://forum.aspose.com/c/3d/18) Toplumsal destek ve yardım için.
### Daha fazla öğretici ve örnek inceleyebilir miyim?
 Evet, şuraya bakın:[dokümantasyon](https://reference.aspose.com/3d/net/) Kapsamlı eğitimler ve örnekler için.