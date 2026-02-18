---
date: 2026-02-09
description: Aspose.3D kullanarak Java'da FBX'i dışa aktarmayı ve çocuk düğümler oluştururken
  düğüme mesh eklemeyi öğrenin.
linktitle: Build Node Hierarchies in 3D Scenes with Java and Aspose.3D
second_title: Aspose.3D Java API
title: FBX'i Nasıl Dışa Aktarır ve Java'da Düğüm Hiyerarşileri Nasıl Oluşturulur
url: /tr/java/geometry/build-node-hierarchies/
weight: 16
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# FBX Nasıl Dışa Aktarılır ve Java’da Aspose.3D ile Düğüm Hiyerarşileri Nasıl Oluşturulur

## Giriiş

Eğer bir Java aktarılırsa **FBX nasıl aktarılır** konusunda net, adım‑adım bir gezinme doğru yerdesiniz. Bu öğreticide, düğüm yöntemleri oluşturmayı, **düğüme mesh eklemeyi** ve son olarak sahneyi Aspose.3D Java API’si kullanarak bir FBX dosyasını olarak kaydetmeyi gösteririz. İster basit bir prototip, ister üretim‑hazır bir 3D motoru oluşturulsun, bu teknikler sahne grafiğiniz üzerinde tam kontrol sağlar.

## Hızlı Yanıtlar
- **Bu öğretmenin temel amacı nedir?** Düğüm gösterileri oluşturulduktan sonra FBX'in genişletilmesini göstermek.
- **Hangi kütüphanesi kullanılıyor?** Aspose.3D for Java.
- **Bir lisansa ihtiyacı var mı?** Geliştirme için ücretsiz deneme çalışır; üretim için ticari lisans gereklidir.
- **Hangi dosya formatı üretildi mi?** FBX (ASCII 7500).
- **Düğüm dönüşümlerini özelleştirebilir miyim?** Evet – çeviri, döndürme ve ölçekleme toplamı desteklenir.

## Aspose.3D bağlamında "FBX nasıl dışa aktarılır" nedir?

FBX aktarma aktarımı, Aspose.3D ile oluşturulabilen bellek içi sahne grafiği, Blender, Maya veya Unity gibi popüler 3D araçlarında açılabilir bir FBX dosyasına dönüştürülebilir gelir. API ağır işleri halleder, böylece sahne oluşturma üzerine odaklanabilirsiniz.

## Dışa aktarmadan önce neden düğüm hiyerarşileri oluşturmalısınız?

İyi düğümleme bir düğüm değiştirmesi, dönüşümleri bir üst düğümde bir kez uygulamanıza olanak tanır ve tüm alt düğümleri otomatik olarak etkiler. Bu, kodun tekrarını parçalara ayırır ve gerçek anlamda nesnel olarak (ör. bir araba şasisi ve tekerlekleri alt düğüm olarak) yansıtır.

## Önkoşullar

Başlamadan önce yaşamış olduğunuzdan emin olun:

1. **Java Geliştirme Ortamı** – JDK8+ ve bir IDE veya derleme aracı tercih ettiniz.
2. **Aspose.3D for Java Kütüphanesi** – Kütüphaneyi [indirme sayfası](https://releases.aspose.com/3d/java/) adresinden indirip kurun.
3. **Belge Dizini** – Oluşturulan FBX dosyalarının bilgisayarda kaydedileceği bir dizüstü bilgisayar.

## Paketleri İçe Aktar

Gerekli Aspose.3D sınıflarını içe aktararak başlayın:

```java
import com.aspose.threed.*;

```

## Adım 1: Sahne Nesnesini Başlatma

```java
// Initialize scene object
Scene scene = new Scene();
```

## Adım 2: Alt Düğümler Oluşturma ve Düğüme Mesh Ekleme

Bu adımda, **alt düğümlerin nasıl oluşturulacağını** ve **düğüme mesh eklemenin** nasıl yapılacağını gösteriyoruz.

```java
// Get a child node object
Node top = scene.getRootNode().createChildNode();

// Create the first cube node
Node cube1 = top.createChildNode("cube1");
Mesh mesh = Common.createMeshUsingPolygonBuilder(); // Use your mesh creation method
cube1.setEntity(mesh);
cube1.getTransform().setTranslation(new Vector3(-10, 0, 0));

// Create the second cube node
Node cube2 = top.createChildNode("cube2");
cube2.setEntity(mesh);
cube2.getTransform().setTranslation(new Vector3(10, 0, 0));
```

## Adım 3: Üst Düğüme Döndürme Uygulama

Üst düğümü döndürmek, hiyerarşik sahnelerin temel avantajlarından biri olan tüm alt düğümlerini otomatik olarak döndürür.

```java
// Rotate the top node, affecting all child nodes
top.getTransform().setRotation(Quaternion.fromEulerAngle(Math.PI, 4, 0));
```

## Adım 4: 3B Sahneyi Kaydetme – FBX Olarak Dışa Aktarma

Şimdi **sahneyi FBX olarak kaydediyoruz**, böylece “FBX olarak dışa aktarma” iş akışını tamamlıyoruz.

```java
// Save 3D scene in the supported file format (FBX in this case)
String MyDir = "Your Document Directory";
MyDir = MyDir + "NodeHierarchy.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nNode hierarchy added successfully to document.\nFile saved at " + MyDir);
```

### Beklenen Sonuç
Kodun çalıştırılması, belirtilen dizinde **NodeHierarchy.fbx** adlı bir dosya oluşturur. Bu dosyayı herhangi bir FBX uyumlu görüntüleyicide açarak, merkezi bir pivotun solunda ve sağında konumlandırılmış, birlikte dönen iki küpü görebilirsiniz.

## Sık Karşılaşılan Sorunlar ve Çözümler

| Sorun | Neden Oluşur | Çözüm |

|-------|----------------|-----|

| Kaydederken **Dosya bulunamadı** hatası | `MyDir` yolu yanlış veya sondaki ayırıcı eksik | Dizinin mevcut olduğundan ve dosya ayırıcıyla (`/` veya `\\`) bittiğinden emin olun. |

| Dışa aktardıktan sonra **Ağ görünmüyor** | Ağ varlığı atanmamış veya çeviri onu görünümden çıkarıyor | `cube1.setEntity(mesh)`'i doğrulayın ve çeviri değerlerini kontrol edin. |

| **Döndürme yanlış görünüyor** | Radyan ve derece yanlış kullanılıyor | `Quaternion.fromEulerAngle` radyan bekliyor; değerleri buna göre ayarlayın. |

## Sıkça Sorulan Sorular

**S: Aspose.3D for Java'yı yeni tutmak için uygun mu?**
C: elbette! API, temiz ve nesnel bir yönetim planıyla tasarlanmıştır; 3D programlamaya yeni olsanız bile öğrenmesi kolaydır.

**S: Aspose.3D for Java’yı ticari projelerde kullanabilir miyim?**
C: Evet, kullanabilirsiniz. Lisans ayrıntıları için [satın alma sayfası](https://purchase.aspose.com/buy) adresini ziyaret edin.

**S: Aspose.3D for Java için nasıl destek alınır?**
A: Topluluk ve Aspose destek ekibinden yardım almak için [Aspose.3D forumu](https://forum.aspose.com/c/3d/18) katılın.

**S: Ücretsiz bir deneme sürümü mevcut mu?**
C: Elbette! İçeriden bağlanmadan önce özelliklerin ayrılması için [ücretsiz deneme](https://releases.aspose.com/) adresini kullanın.

**S: Belgelendirmeye Nereden ulaşabilirim?**
C: Aspose.3D for Java hakkında ayrıntılı bilgi için [dokümantasyon](https://reference.aspose.com/3d/java/) talimatlara bakın.

## Çözüm

**FBX nasıl aktarılır**, düğüm bakımları oluşturma ve **düğüme mesh ekleme** bileşenlerin uzmanlaşması, Java’da gelişmiş 3D uygulamalar için temel adımlardır. Aspose.3D, düşük seviyeli ayrıntıları soyutlayan ve sahne grafiği üzerinde tam kontrol sağlayan güçlü, lisans‑dostu bir çözümdür. Farklı mesh'ler, dönüşümler ve ayrıştırılan formatlarla deneyleri yaparak daha fazla çözüm çözümü.

---

**Son Güncelleme:** 2026-02-09
**Şunlarla Test Edildi:** Java 24.11 için Aspose.3D
**Yazar:** Aspose 

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}