---
title: Sphere Primitive'i Mesh'e Dönüştürme
linktitle: Sphere Primitive'i Mesh'e Dönüştürme
second_title: Aspose.3D .NET API'si
description: Aspose.3D for .NET'i keşfedin ve özel bellek düzeniyle Sphere Mesh'i zahmetsizce Triangle Mesh'e dönüştürün. Sorunsuz entegrasyon için adım adım kılavuzumuzu izleyin.
type: docs
weight: 16
url: /tr/net/objects/convert-sphere-primitive-to-mesh/
---
## giriiş
Aspose.3D for .NET'in gücünden yararlanarak Sphere Mesh'i özel bellek düzeniyle Üçgen Mesh'e dönüştürmek mi istiyorsunuz? Bu adım adım kılavuz, süreç boyunca size yol gösterecek ve yeni başlayanların bile takip etmesini kolaylaştıracaktır. Bu eğitimin sonunda Aspose.3D for .NET kullanarak bunu nasıl başaracağınıza dair sağlam bir anlayışa sahip olacaksınız.
## Önkoşullar
Eğiticiye dalmadan önce aşağıdaki önkoşulların mevcut olduğundan emin olun:
- .NET programlamaya ilişkin temel bilgiler.
-  Aspose.3D for .NET kütüphanesi kuruldu. adresinden indirebilirsiniz.[Aspose.3D for .NET indirme sayfası](https://releases.aspose.com/3d/net/).
- C# programlama diline aşinalık.
## Ad Alanlarını İçe Aktar
Aspose.3D işlevselliğinden yararlanmak için C# projenizde gerekli ad alanlarını içe aktardığınızdan emin olun:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```
## Adım 1: Sahne Nesnesini Başlatın
```csharp
// Sahne nesnesini başlat
Scene scene = new Scene();
```
## Adım 2: Düğüm Sınıfı Nesnesini Başlatın
```csharp
// Düğüm sınıfı nesnesini başlat
Node cubeNode = new Node("sphere");
```
## Adım 3: Sphere Mesh'i Yazılı TriMesh'e Dönüştürün
```csharp
Mesh sphere = (new Sphere()).ToMesh();
var myMesh = TriMesh<MyVertex>.FromMesh(sphere);
```
## Adım 4: Özelleştirilmiş Yapıda Vertex Verilerini Alın
```csharp
MyVertex[] vertex = myMesh.VerticesToTypedArray();
```
## 5. Adım: 32 bit ve 16 bit Endeksleri Alın
```csharp
int[] indices32bit;
ushort[] indices16bit;
myMesh.IndicesToArray(out indices32bit);
myMesh.IndicesToArray(out indices16bit);
```
## Adım 6: Köşe ve Dizin Verilerini Bellek Akışına Yazma
```csharp
using (MemoryStream ms = new MemoryStream())
{
    myMesh.WriteVerticesTo(ms);
    myMesh.Write16bIndicesTo(ms);
    myMesh.Write32bIndicesTo(ms);
}
```
## Adım 7: Düğümü Mesh Geometrisine Noktalayın
```csharp
cubeNode.Entity = sphere;
```
## Adım 8: Sahneye Düğüm Ekleme
```csharp
scene.RootNode.ChildNodes.Add(cubeNode);
```
## Adım 9: 3D Sahneyi Kaydet
```csharp
string output = "Your Output Directory" + "SphereToTriangleMeshCustomMemoryLayoutScene.fbx";
scene.Save(output, FileFormat.FBX7400ASCII);
```
## Adım 10: Sonuçları Görüntüleyin
```csharp
Console.WriteLine("Indices = {0}, Actual vertices = {1}, vertices before merging = {2}", myMesh.IndicesCount, myMesh.VerticesCount, myMesh.UnmergedVerticesCount);
Console.WriteLine("Total bytes of vertices in memory {0}bytes", myMesh.VerticesSizeInBytes);
Console.WriteLine("\nConverted a Sphere mesh to a triangle mesh with a custom memory layout of the vertex successfully.\nFile saved at " + output);
```

## MyVertex Örnek Kaynak Kodu
```csharp
[StructLayout(LayoutKind.Sequential)]
struct MyVertex
{
	[Semantic(VertexFieldSemantic.Position)]
	FVector3 position;
	[Semantic(VertexFieldSemantic.Normal)]
	FVector3 normal;
}
```
## Çözüm
Tebrikler! Aspose.3D for .NET'i kullanarak Sphere Mesh'i özel bellek düzeniyle başarıyla Üçgen Mesh'e dönüştürdünüz. Bu güçlü kitaplık, .NET uygulamalarınızdaki 3B nesneleri işlemek için kusursuz bir yol sağlar.
## SSS
### S: Aspose.3D for .NET'i diğer .NET çerçeveleriyle kullanabilir miyim?
C: Evet, Aspose.3D for .NET çeşitli .NET çerçeveleriyle uyumludur.
### S: Aspose.3D for .NET'in ayrıntılı belgelerini nerede bulabilirim?
 C: Bkz.[Aspose.3D for .NET belgeleri](https://reference.aspose.com/3d/net/) derinlemesine bilgi için.
### S: Aspose.3D for .NET için nasıl geçici lisans alabilirim?
 Ziyaret[bu bağlantı](https://purchase.aspose.com/temporary-license/) geçici lisans almak için.
### S: Aspose.3D for .NET için örnek projeler mevcut mu?
 C: Aspose.3D for .NET belgelerini inceleyin ve[GitHub deposu](https://github.com/aspose-3d/Aspose.3D-for-.NET) Örnek projeler için.
### S: Aspose.3D for .NET desteği için aktif bir topluluk var mı?
 C: Evet, katılın[Aspose.3D for .NET forumu](https://forum.aspose.com/c/3d/18) toplumdan yardım almak için.