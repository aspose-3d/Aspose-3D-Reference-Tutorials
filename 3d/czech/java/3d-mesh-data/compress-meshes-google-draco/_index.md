---
date: 2026-09-08
description: Jak snížit velikost 3D modelu vytvořením sférové sítě v Java a kompresí
  pomocí Google Draco přes Aspose.3D. Naučte se celý pracovní postup během několika
  minut.
keywords:
- how to reduce 3d model size
- aspose 3d java
- draco mesh compression
- java sphere mesh
- 3d model optimization
lastmod: 2026-09-08
linktitle: Jak snížit velikost 3D modelu – Vytvořte sférovou síť v Java pomocí Google
  Draco
og_description: Jak snížit velikost 3D modelu vytvořením sférové sítě v Java a kompresí
  pomocí Google Draco s využitím Aspose.3D. Získáte soubor .drc až o 95 % menší během
  několika minut.
og_image_alt: 'Developer guide: Reduce 3d model size with Java sphere mesh and Draco
  compression'
og_title: Jak snížit velikost 3D modelu pomocí sférové sítě v Java a Draca
schemas:
- author: Aspose
  dateModified: '2026-09-08'
  description: How to reduce 3d model size by generating a sphere mesh in Java and
    compressing it with Google Draco via Aspose.3D. Learn the full workflow in minutes.
  headline: How to reduce 3d model size with a Java sphere mesh and Draco
  type: TechArticle
- description: How to reduce 3d model size by generating a sphere mesh in Java and
    compressing it with Google Draco via Aspose.3D. Learn the full workflow in minutes.
  name: How to reduce 3d model size with a Java sphere mesh and Draco
  steps:
  - name: set up the project
    text: Create a new Java project (any IDE works) and add all Aspose.3D JARs to
      the classpath. Keep your source files in a package such as `com.example.draco`
      for clarity.
  - name: how to create sphere mesh in Java
    text: 'The `Sphere` class is Aspose.3D''s built‑in geometry generator that produces
      a triangulated mesh with a configurable radius and tessellation. > **Pro tip:**
      The `Sphere` class generates a triangulated mesh with a default radius of 1.0.
      You can pass custom radius, tessellation, or material parameters '
  - name: export the mesh to Draco format
    text: After the sphere is added to a `Scene` object, call `scene.save("sphere.drc",
      SaveFormat.Draco)`. Aspose.3D automatically selects optimal compression settings,
      but you can fine‑tune them by adjusting `DracoCompressionOptions` if you need
      the smallest possible file. `DracoCompressionOptions` lets you
  - name: verify the output
    text: Open the generated `.drc` file with a Draco viewer (e.g., three.js `DRACOLoader`)
      to ensure the geometry renders correctly. You’ll notice a dramatic reduction
      in file size—often a factor of ten or more.
  type: HowTo
- questions:
  - answer: Yes, Aspose.3D supports OBJ, FBX, STL, GLTF, and many others, making it
      a versatile choice for **Aspose 3d export** pipelines.
    question: Is Aspose.3D compatible with different 3d file formats?
  - answer: Absolutely. Draco offers native libraries for C++, Python, and JavaScript.
      This tutorial focuses on Java, but the concepts apply across languages.
    question: Can I use Google Draco for compression in other programming languages?
  - answer: Visit the **[Aspose.3D Java documentation](https://reference.aspose.com/3d/java/)**
      for full API references and more examples.
    question: Where can I find additional Aspose.3D documentation?
  - answer: Explore temporary licensing options on the **[Aspose temporary license
      page](https://purchase.aspose.com/temporary-license/)**.
    question: How do I obtain a temporary license for Aspose.3D?
  - answer: Yes, join the discussion at the **[Aspose.3D Forum](https://forum.aspose.com/c/3d/18)**.
    question: Is there a community forum for Aspose.3D support?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- reduce 3d model size
- Aspose.3D
- Java 3D compression
- Google Draco
- sphere mesh
title: Jak snížit velikost 3D modelu pomocí sférové sítě v Java a Draca
url: /cs/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak snížit velikost 3d modelu pomocí sférické sítě v Javě a Draco

## Úvod

Pokud hledáte rychlý způsob, jak **snížit velikost 3d modelu** a přitom zachovat vysoce kvalitní geometrii, jste na správném místě. V tomto tutoriálu vás provedeme generováním sférické sítě pomocí **Aspose.3D for Java** a následným kompresováním této sítě pomocí **Google Draco**. Na konci budete mít připravený soubor `.drc`, který je dramaticky menší než originál, což je ideální pro webové prohlížeče, mobilní hry nebo jakoukoli Java aplikaci s omezenou šířkou pásma.

## Rychlé odpovědi
- **Co tento tutoriál pokrývá?** Vytvoření sférické sítě v Javě a komprese pomocí Google Draco přes Aspose.3D.  
- **Primární knihovna?** Aspose.3D for Java (použita pro tvorbu sítě i export do Draco).  
- **Typický čas implementace?** Přibližně 10‑15 minut pro základní kouli.  
- **Klíčová podmínka?** Vývojové prostředí Javy s JAR soubory Aspose.3D na classpathu.  
- **Výsledek?** Soubor `.drc`, který **snižuje velikost 3d modelu** až o 95 % ve srovnání s nekomprimovanou sítí.

## Jak snížit velikost 3d modelu?

Třída `Sphere` generuje triangulovanou sférickou geometrii na základě zadaného poloměru a parametrů tessellace. Načtěte svou kouli pomocí `new Sphere(1.0, 32, 32)` a exportujte ji přímo do Draco pomocí `scene.save("sphere.drc", SaveFormat.Draco)`. Metoda `scene.save` zapíše aktuální scénu do souboru ve specifikovaném formátu. Aspose.3D provádí konverzi interně, takže se vyhnete ručním krokům kódování. Exportér Draco automaticky aplikuje kvantizaci geometrie a deduplikaci vrcholů, což vede k souborům, které jsou často o 80‑95 % menší při zachování vizuální věrnosti.

## Co znamená „snížit velikost 3d modelu“ v kontextu 3d vývoje?

**Snížení velikosti 3d modelu** znamená zmenšení množství geometrických dat, která je třeba přenést nebo uložit, aniž by došlo k výraznému zhoršení vizuální kvality. Draco toho dosahuje kódováním pozic vrcholů, normál a dalších atributů do vysoce kompaktního binárního formátu. V kombinaci s Aspose.3D zůstává celý pracovní postup uvnitř Javy, takže nemusíte manipulovat s nativními binárními soubory Draco.

## Proč použít kompresi sítí Google Draco s Aspose.3D?

Google Draco v kombinaci s Aspose.3D poskytuje efektivní pipeline, která dramaticky zmenšuje soubory sítí a zároveň je snadno integruje do Java projektů. Knihovna se stará o veškeré nízkoúrovňové kódování, takže se vývojáři mohou soustředit na tvorbu geometrie, aniž by museli pracovat s nativními binárními soubory Draco, což vede k rychlejšímu vývoji a menším assetům pro web a mobil.

- **Obrovské zmenšení velikosti:** Draco může snížit data sítě až o 95 % u typických modelů, přemění 5 MB OBJ na 0,3 MB `.drc`.  
- **Rychlé dekódování za běhu:** Enginy jako Unity, Unreal a three.js dekódují Draco nativně, což vede k rychlejším načítacím časům.  
- **Bezproblémová integrace s Javou:** Aspose.3D abstrahuje nativní knihovnu Draco, což vám umožní zůstat v ekosystému Javy.  
- **Komplexní export z Aspose 3D:** Stejné API, které používáte k vytvoření geometrie, také provádí export, což zjednodušuje pipeline.

## Požadavky

- **Java Development Kit (JDK)** – verze 8 nebo novější.  
- **Aspose.3D for Java** – stáhněte nejnovější JAR soubory ze **[Aspose 3D Java releases page](https://releases.aspose.com/3d/java/)**.  
- **Základní znalost Google Draco** – použijete wrapper Aspose.3D, takže není vyžadována žádná nativní instalace Draco.

## Import balíčků

```java
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Sphere;


import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

## Průvodce krok za krokem

### Krok 1: nastavení projektu

Vytvořte nový Java projekt (funguje jakékoli IDE) a přidejte všechny JAR soubory Aspose.3D do classpathu. Pro přehlednost umístěte své zdrojové soubory do balíčku například `com.example.draco`.

### Krok 2: jak vytvořit sférickou síť v Javě

Třída `Sphere` je vestavěný generátor geometrie v Aspose.3D, který vytváří triangulovanou síť s konfigurovatelným poloměrem a tessellací.  

```java
import java.nio.file.Files;
import java.nio.file.Paths;
import com.aspose.threed.Sphere;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.FileFormat;

// ExStart:Encode3DMeshinGoogleDraco
// The path to the documents directory.
String MyDir = "Your Document Directory";

// Create a sphere
Sphere sphere = new Sphere();

// Encode the sphere to Google Draco raw data using optimal compression level.
DracoSaveOptions opt = new DracoSaveOptions();
opt.setCompressionLevel(DracoCompressionLevel.OPTIMAL);
byte[] b = FileFormat.DRACO.encode(sphere.toMesh(), opt);

// Save the raw bytes to file
Files.write(Paths.get(MyDir, "SphereMeshtoDRC_Out.drc"), b);
// ExEnd:Encode3DMeshinGoogleDraco
```

> **Tip:** Třída `Sphere` generuje triangulovanou síť s výchozím poloměrem 1.0. Můžete zadat vlastní poloměr, tessellaci nebo parametry materiálu, pokud potřebujete před kompresí jinou úroveň detailu.

### Krok 3: export sítě do formátu Draco

Po přidání koule do objektu `Scene` zavolejte `scene.save("sphere.drc", SaveFormat.Draco)`. Aspose.3D automaticky vybere optimální nastavení komprese, ale můžete je doladit úpravou `DracoCompressionOptions`, pokud potřebujete co nejmenší soubor. `DracoCompressionOptions` vám umožňuje přizpůsobit nastavení komprese Draco, jako je kvantizace a úroveň komprese.

### Krok 4: ověření výstupu

Otevřete vygenerovaný soubor `.drc` v Draco prohlížeči (např. three.js `DRACOLoader`), abyste se ujistili, že geometrie se vykresluje správně. Všimnete si dramatického snížení velikosti souboru – často o faktor deset nebo více.

## Běžné případy použití

| Scénář | Proč snížit velikost modelu? | Jak tento tutoriál pomáhá |
|----------|-----------------------------|---------------------------|
| Webové konfigurátory produktů | Rychlejší načítání stránek při pomalých připojeních | Draco‑komprimované soubory `.drc` se načtou během několika sekund |
| Mobilní AR/VR aplikace | Nižší paměťová náročnost na zařízeních | Menší sítě udržují aplikaci responsivní |
| Scény renderované v cloudu | Snížení nákladů na šířku pásma | Export jedním kliknutím z Aspose.3D do Draco |

## Běžné problémy a řešení

| Problém | Důvod | Řešení |
|-------|--------|-----|
| **`NoClassDefFoundError` pro třídy Draco** | JAR soubory Aspose.3D nejsou na classpathu | Ověřte, že jsou zahrnuty *všechny* JAR soubory Aspose.3D a že verze odpovídá dokumentaci. |
| **Výstupní soubor je prázdný** | `MyDir` ukazuje na neexistující složku | Vytvořte adresář programově (`Files.createDirectories(Paths.get(MyDir))`) před zápisem souboru. |
| **Komprimovaná síť vypadá deformovaně** | Použití nízké úrovně komprese nebo nedostatečná tessellace | Přepněte na `DracoCompressionLevel.OPTIMAL` a zvýšte tessellaci koule (např. `new Sphere(1.0, 64, 64)`). `DracoCompressionLevel.OPTIMAL` vybírá nejvyšší kvalitu komprese pro výstup Draco. |

## Často kladené otázky

**Q: Je Aspose.3D kompatibilní s různými 3d formáty souborů?**  
A: Ano, Aspose.3D podporuje OBJ, FBX, STL, GLTF a mnoho dalších, což z něj činí všestrannou volbu pro **Aspose 3d export** pipeline.

**Q: Mohu použít Google Draco pro kompresi v jiných programovacích jazycích?**  
A: Rozhodně. Draco nabízí nativní knihovny pro C++, Python a JavaScript. Tento tutoriál se zaměřuje na Javu, ale koncepty platí i pro ostatní jazyky.

**Q: Kde najdu další dokumentaci k Aspose.3D?**  
A: Navštivte **[Aspose.3D Java documentation](https://reference.aspose.com/3d/java/)** pro kompletní referenci API a další příklady.

**Q: Jak získám dočasnou licenci pro Aspose.3D?**  
A: Prozkoumejte možnosti dočasného licencování na **[Aspose temporary license page](https://purchase.aspose.com/temporary-license/)**.

**Q: Existuje komunitní fórum pro podporu Aspose.3D?**  
A: Ano, připojte se k diskuzi na **[Aspose.3D Forum](https://forum.aspose.com/c/3d/18)**.

## Závěr

V tomto průvodci jsme ukázali, jak **snížit velikost 3d modelu** vytvořením sférické sítě v Javě a následnou kompresí pomocí Google Draco prostřednictvím Aspose.3D. Dodržením těchto stručných kroků můžete dramaticky zmenšit soubory sítí, zlepšit načítací časy a udržet své Java‑založené 3d aplikace responsivní a šetrné k šířce pásma.

---

**Poslední aktualizace:** 2026-09-08  
**Testováno s:** Aspose.3D for Java 24.12 (latest)  
**Autor:** Aspose

## Související tutoriály

- [Snížení velikosti 3D souboru – komprese scén s Aspose.3D pro Java](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [Generování Draco bodového mraku ze sfér pomocí Aspose.3D pro Java](/3d/java/point-clouds/generate-point-clouds-spheres-java/)
- [Naučte se triangulovat sítě pro optimalizované renderování v Javě pomocí Aspose.3D](/3d/java/geometry/triangulate-meshes-for-optimized-rendering/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}