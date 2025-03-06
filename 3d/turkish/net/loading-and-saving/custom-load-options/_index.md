---
title: Özel Yükleme Seçenekleri
linktitle: Özel Yükleme Seçenekleri
second_title: Aspose.3D .NET API'si
description: Kesintisiz 3D model yükleme ve kaydetme için Aspose.3D for .NET'i keşfedin.
weight: 15
url: /tr/net/loading-and-saving/custom-load-options/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Özel Yükleme Seçenekleri

## giriiş

Geliştiricilerin 3D dosyalarla sorunsuz bir şekilde çalışmasını sağlayan güçlü bir kütüphane olan Aspose.3D for .NET dünyasına hoş geldiniz. Bu eğitimde, özel yükleme seçeneklerine odaklanarak 3D modelleri yükleme ve kaydetmenin inceliklerini inceleyeceğiz. İster deneyimli bir geliştirici olun, ister yeni gelen biri olun, bu kılavuz süreç boyunca size adım adım yol gösterecek ve Aspose.3D for .NET'in tüm potansiyelinden yararlanmanızı sağlayacaktır.

## Önkoşullar

Bu yolculuğa çıkmadan önce aşağıdaki önkoşulların mevcut olduğundan emin olun:

-  Aspose.3D for .NET: Kitaplığın kurulu olduğundan emin olun. İndirebilirsin[Burada](https://releases.aspose.com/3d/net/).

- Belge Dizini: 3D model dosyalarınızı saklamak için bir dizin oluşturun.

Artık temel bilgilere sahip olduğunuza göre, 3D model manipülasyonunun heyecan verici dünyasına dalalım!

## Ad Alanlarını İçe Aktar

Öncelikle gerekli ad alanlarını içe aktaralım. Bu, Aspose.3D dünyasına yolculuğumuza zemin hazırlayacak.

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
```

## Yükleme ve Kaydetme - Özel Yükleme Seçenekleri

### Adım 1: Discreet3DS Dosyalarını Yükleme

```csharp
private static void Discreet3DSLoadOption()
{
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();

    //Özel seçenekleri ayarlama
    loadOpts.ApplyAnimationTransform = true;
    loadOpts.FlipCoordinateSystem = true;
    loadOpts.GammaCorrectedColor = true;
    loadOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Dosyayı yükleme seçenekleriyle yükleyin
    var scene = Scene.FromFile("test.3ds", loadOpts);
}
```

### Adım 2: OBJ Dosyalarını Yükleme

```csharp
private static void ObjLoadOption()
{
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();

    //Özel seçenekleri ayarlama
    loadObjOpts.EnableMaterials = true;
    loadObjOpts.FlipCoordinateSystem = true;
    loadObjOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Dosyayı yükleme seçenekleriyle yükleyin
    var scene = Scene.FromFile("test.obj", loadObjOpts);

}
```

### Adım 3: STL Dosyalarını Yükleme

```csharp
private static void STLLoadOption()
{
    // Belgeler dizininin yolu.
    StlLoadOptions loadSTLOpts = new StlLoadOptions();

    //Özel seçenekleri ayarlama
    loadSTLOpts.FlipCoordinateSystem = true;
    loadSTLOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Dosyayı yükleme seçenekleriyle yükleyin
    var scene = Scene.FromFile("test.stl", loadSTLOpts);
}
```

### Adım 4: U3D Dosyalarını Yükleme

```csharp
private static void U3DLoadOption()
{
    // Belgeler dizininin yolu.
    string dataDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();

    //Özel seçenekleri ayarlama
    loadU3DOpts.FlipCoordinateSystem = true;
    loadU3DOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Dosyayı yükleme seçenekleriyle yükleyin
    var scene = Scene.FromFile("test.u3d", loadU3DOpts);
}
```

### Adım 5: glTF Dosyalarını Yükleme

```csharp
private static void glTFLoadOptions()
{
    // Belgeler dizininin yolu.
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();

    //Özel seçenekleri ayarlama
    loadOpt.FlipTexCoordV = true;
    scene.Open("Duck.gltf", loadOpt);
}
```

### Adım 6: PLY Dosyalarını Yükleme

```csharp
private static void PlyLoadOptions()
{
    // Belgeler dizininin yolu.
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();

    //Özel seçenekleri ayarlama
    loadPLYOpts.FlipCoordinateSystem = true;
    scene.Open("vase-v2.ply", loadPLYOpts);
}
```

### Adım 7: FBX Dosyalarını Yükleme

```csharp
private static void FBXLoadOptions()
{
    // Belgeler dizininin yolu.
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions() { KeepBuiltinGlobalSettings = true };

    //Özel seçenekleri ayarlama
    scene.Open("test.FBX", opt);

    // FBX dosyasındaki GlobalSettings'te tanımlanan çıktı özellikleri
    foreach (Property property in scene.RootNode.AssetInfo.Properties)
    {
        Console.WriteLine(property);
    }
}
```

## Çözüm

Tebrikler! Aspose.3D for .NET'i kullanarak 3D modelleri yükleme ve kaydetmenin karmaşık dünyasında başarıyla gezindiniz. Bu eğitim, çeşitli dosya formatlarını ve bunların özel yükleme seçeneklerini kapsayarak 3B varlıkları kolaylıkla değiştirmenizi sağlar.

## SSS'ler

### S1: Aspose.3D for .NET yeni başlayanlar için uygun mu?

A1: Kesinlikle! Aspose.3D for .NET, kullanıcı dostu bir arayüz sunarak her seviyeden geliştiricinin erişebilmesini sağlar.

### S2: Aspose.3D'yi ticari projeler için kullanabilir miyim?

C2: Evet, Aspose.3D for .NET, projelerinizde kullanmanıza olanak tanıyan ticari bir lisansla birlikte gelir.

### S3: Desteklenen dosya formatlarında herhangi bir sınırlama var mı?

 Cevap3: Aspose.3D for .NET, OBJ, STL, FBX ve daha fazlasını içeren çok çeşitli popüler 3D dosya formatlarını destekler. Bakın[dokümantasyon](https://reference.aspose.com/3d/net/) kapsamlı bir liste için.

### S4: Deneme sürümü mevcut mu?

Cevap4: Evet, Aspose.3D for .NET'in yeteneklerini aşağıdaki dosyayı indirerek keşfedebilirsiniz.[ücretsiz deneme](https://releases.aspose.com/).

### S5: Aspose.3D for .NET desteğini nereden alabilirim?

 A5: ziyaret edin[Aspose.3D forumu](https://forum.aspose.com/c/3d/18) Toplumsal destek ve yardım için.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
