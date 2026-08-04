---
date: 2026-04-12
description: Aspose.3D Java API'yi kullanarak sağlam 3D sahne grafikleri için alt
  düğümler oluşturmayı, düğüme mesh eklemeyi ve FBX dışa aktarmayı öğrenin.
keywords:
- create child nodes
- how to export fbx
- add mesh to node
- java 3d scene graph
- save scene fbx
linktitle: Java ve Aspose.3D ile 3D Sahnelere Düğüm Hiyerarşileri Oluşturun
second_title: Aspose.3D Java API
title: Java'da Aspose.3D ile Çocuk Düğümler Oluşturun ve FBX Dışa Aktarın
url: /tr/java/geometry/build-node-hierarchies/
weight: 16
---

{{< blocks/products/pf/main-wrap-class >}}  
{{< blocks/products/pf/main-container >}}  
{{< blocks/products/pf/tutorial-page-section >}}  

# FBX Nasıl Dışa Aktarılır ve Java'da Aspose.3D ile Düğüm Hiyerarşileri Nasıl Oluşturulur  

## Giriş  

Java uygulamasından **create child nodes**, **add mesh to node** ve **how to export FBX** konularında net, adım adım bir rehber arıyorsanız, doğru yerdesiniz. Bu öğreticide **java 3d scene graph** oluşturmayı, mesh'leri eklemeyi, dönüşümleri uygulamayı ve sonunda sahneyi Aspose.3D Java API'si kullanarak bir FBX dosyası olarak kaydetmeyi göstereceğiz. Basit bir demo prototipleği yapıyor olun ya da üretim‑hazır bir 3D motoru geliştiriyor olun, bu kavramları ustalaşmak sahne hiyerarşiniz ve dışa aktarma iş akışınız üzerinde tam kontrol sağlar.  

## Hızlı Yanıtlar  
- **Bu öğreticinin temel amacı nedir?** **create child nodes**, mesh'leri eklemeyi ve **export FBX** bir düğüm hiyerarşisi oluşturduktan sonra göstermektir.  
- **Hangi kütüphane kullanılıyor?** Aspose.3D for Java.  
- **Bir lisansa ihtiyacım var mı?** Geliştirme için ücretsiz deneme çalışır; üretim için ticari lisans gereklidir.  
- **Hangi dosya formatı üretilir?** FBX (ASCII 7500).  
- **Düğüm dönüşümlerini özelleştirebilir miyim?** Evet – çeviri, dönüş ve ölçekleme tümü desteklenir.  

## Aspose.3D bağlamında “create child nodes” nedir?  

Child node'lar oluşturmak, sahne grafiğinde bir üst düğüme alt `Node` nesneleri eklemek anlamına gelir. Bu hiyerarşik yapı, dönüşümü üst düzeyde bir kez uygulamanıza ve otomatik olarak tüm alt düğümlere etki etmesine olanak tanır; bu, dönen tekerlekli bir araba şasisi gibi gerçekçi nesne ilişkileri için gereklidir.  

## Dışa aktarmadan önce neden düğüm hiyerarşileri oluşturulmalı?  

İyi yapılandırılmış bir hiyerarşi kod tekrarını azaltır, animasyonu basitleştirir ve gerçek‑dünya ilişkilerini yansıtır. Daha sonra **convert scene fbx** (veya başka bir format) yaptığınızda, hiyerarşi korunur, böylece Blender, Maya veya Unity gibi sonraki araçlar ebeveyn‑çocuk ilişkilerini tam olarak tasarladığınız gibi anlar.  

## Düğüm Hiyerarşileri için Yaygın Kullanım Senaryoları  

| Kullanım Durumu | Hiyerarşinin Yardımcı Olma Nedeni | Tipik Sonuç |
|-----------------|-----------------------------------|-------------|
| **Mekanik montajlar** (ör. robot kol) | Temel düğümü döndürmek, tüm bağlı segmentleri hareket ettirir | Karmaşık mekanizmaların kolay animasyonu |
| **Karakter iskeletleri** | İskelet kemikleri, kökün alt düğümleridir | Tutarlı poz dönüşümleri |
| **Sahne organizasyonu** | Statik nesneleri “props” düğümü altında gruplamak | Daha temiz sahne yönetimi ve seçici dışa aktarma |
| **Detay seviyesi (LOD) geçişi** | Üst düğüm, alt mesh'lerin görünürlüğünü değiştirir | Farklı donanımlar için optimize edilmiş renderleme |

## Önkoşullar  

1. **Java Geliştirme Ortamı** – JDK 8+ ve tercih ettiğiniz bir IDE veya derleme aracı.  
2. **Aspose.3D for Java Kütüphanesi** – Kütüphaneyi [download page](https://releases.aspose.com/3d/java/) adresinden indirin ve kurun.  
3. **Belge Dizini** – Oluşturulan FBX dosyasının kaydedileceği makinenizdeki bir klasör.  

## Paketleri İçe Aktar  

İlk olarak gerekli Aspose.3D sınıflarını içe aktarın:  

```java
import com.aspose.threed.*;
```  

## Adım 1: Sahne Nesnesini Başlat  

```java
// Initialize scene object
Scene scene = new Scene();
```  

## Adım 2: Çocuk Düğümler Oluştur ve Mesh'i Düğüme Ekle  

Bu adımda **how to create child nodes** ve **add mesh to node** nesnelerinin nasıl yapılacağını gösteriyoruz.  

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

## Adım 3: Üst Düğüm'e Dönüş Uygula  

Ebeveyn düğümünü döndürmek, tüm alt düğümleri otomatik olarak döndürür; bu, hiyerarşik sahnelerin temel avantajıdır.  

```java
// Rotate the top node, affecting all child nodes
top.getTransform().setRotation(Quaternion.fromEulerAngle(Math.PI, 4, 0));
```  

## Adım 4: 3D Sahneyi Kaydet – FBX Nasıl Dışa Aktarılır  

Şimdi **save scene as FBX**, “how to export fbx” iş akışını tamamlıyoruz.  

```java
// Save 3D scene in the supported file format (FBX in this case)
String MyDir = "Your Document Directory";
MyDir = MyDir + "NodeHierarchy.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nNode hierarchy added successfully to document.\nFile saved at " + MyDir);
```  

### Beklenen Sonuç  

Kodu çalıştırmak, belirtilen dizinde **NodeHierarchy.fbx** adlı bir dosya oluşturur. Herhangi bir FBX‑uyumlu görüntüleyicide açarak merkezi bir pivottan sol ve sağda konumlandırılmış iki küpü, hepsinin birlikte döndüğünü görebilirsiniz.  

## Yaygın Sorunlar ve Çözümler  

| Sorun | Neden Oluşur | Çözüm |
|-------|--------------|-------|
| **File not found** hatası kaydederken | `MyDir` yolu yanlış veya son ayırıcı eksik | Dizinin var olduğundan ve bir dosya ayırıcı (`/` veya `\\`) ile bittiğinden emin olun. |
| **Mesh görünür değil** dışa aktardıktan sonra | Mesh varlığı atanmadı veya çeviri onu görünüm dışına taşıdı | `cube1.setEntity(mesh)` doğrulamasını yapın ve çeviri değerlerini kontrol edin. |
| **Dönüş hatalı görünüyor** | Radyan ile derece karıştırılması | `Quaternion.fromEulerAngle` radyan bekler; değerleri buna göre ayarlayın. |

## Sorun Giderme İpuçları  

- **Dizini doğrula**: Klasör mevcut olmayabilir, bu yüzden `scene.save` öncesinde `new File(MyDir).mkdirs();` kullanın.  
- **Sahne grafiğini incele**: `scene.getRootNode().getChildren().size()` çağırarak çocuk düğümlerin eklendiğini doğrulayın.  
- **FBX sürüm uyumluluğunu kontrol et**: Bazı eski araçlar sadece FBX 2013'ü destekler; gerekirse formatı `FileFormat.FBX2013` olarak değiştirebilirsiniz.  

## Sıkça Sorulan Sorular  

**Q:** Aspose.3D for Java yeni başlayanlar için uygun mu?  
**A:** Kesinlikle! API, temiz, nesne‑yönelimli bir yaklaşımla tasarlanmıştır ve 3D programlamaya yeni olsanız bile öğrenmesi kolaydır.  

**Q:** Aspose.3D for Java'yi ticari projelerde kullanabilir miyim?  
**A:** Evet, kullanabilirsiniz. Lisans detayları için [purchase page](https://purchase.aspose.com/buy) adresini ziyaret edin.  

**Q:** Aspose.3D for Java için destek nasıl alabilirim?  
**A:** Topluluk ve Aspose destek ekibinden yardım almak için [Aspose.3D forum](https://forum.aspose.com/c/3d/18) adresine katılın.  

**Q:** Ücretsiz deneme mevcut mu?  
**A:** Elbette! Bağlı kalmadan önce özellikleri [free trial](https://releases.aspose.com/) ile keşfedin.  

**Q:** Belgeleri nerede bulabilirim?  
**A:** Aspose.3D for Java hakkında detaylı bilgi için [documentation](https://reference.aspose.com/3d/java/) adresine bakın.  

## Sonuç  

**create child nodes**, **add mesh to node**, ve **how to export FBX** konularında ustalaşmak, Java'da gelişmiş 3D uygulamalar oluşturmanın temel adımlarıdır. Aspose.3D ile düşük seviyeli detayları soyutlayan, lisans‑dostu güçlü bir çözüm elde eder ve sahne grafiği üzerinde tam kontrol sağlarsınız. Farklı mesh'ler, dönüşümler ve dışa aktarma formatlarıyla deneyler yaparak daha fazla olasılığı ortaya çıkarın.  

---  

**Son Güncelleme:** 2026-04-12  
**Test Edilen Versiyon:** Aspose.3D for Java 24.11  
**Yazar:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}  

{{< /blocks/products/pf/main-container >}}  
{{< /blocks/products/pf/main-wrap-class >}}  

{{< blocks/products/products-backtop-button >}}