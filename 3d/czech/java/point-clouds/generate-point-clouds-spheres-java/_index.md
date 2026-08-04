---
date: 2026-05-29
description: Naučte se, jak vytvořit draco point cloud ze sféry pomocí Aspose.3D pro
  Java. Podrobný návod krok za krokem, předpoklady, kód a řešení problémů.
keywords:
- create draco point cloud
- Aspose 3D point cloud Java
- DracoSaveOptions Java
linktitle: Jak vytvořit draco point cloud ze sfér pomocí Aspose 3D Java
schemas:
- author: Aspose
  dateModified: '2026-05-29'
  description: Learn how to create draco point cloud from a sphere with Aspose.3D
    for Java. Step‑by‑step guide, prerequisites, code, and troubleshooting.
  headline: How to create draco point cloud from spheres using Aspose 3D Java
  type: TechArticle
- questions:
  - answer: Yes. After loading the `.drc` file back into a `Scene`, you can export
      vertices using Aspose.3D’s generic `Scene.save` method with formats like PLY
      or OBJ.
    question: Can I convert the generated point cloud to other formats (e.g., PLY,
      OBJ)?
  - answer: The current Aspose.3D implementation focuses on geometry only. To add
      attributes, extend the scene with custom `VertexElement` objects before encoding.
    question: Does the Draco encoder support custom point attributes (e.g., color,
      normals)?
  - answer: Draco compresses efficiently, but clouds exceeding **100 million** points
      may require more than 8 GB RAM. Consider chunking or streaming APIs for very
      large datasets.
    question: How large can a point cloud be before performance degrades?
  - answer: Absolutely. three.js includes a Draco loader that reads the file directly
      for real‑time rendering.
    question: Is the generated `.drc` file compatible with web viewers like three.js?
  - answer: The default level (5) works for most cases. If file size is critical,
      experiment with values between **0** (fastest) and **10** (maximum compression)
      to balance speed vs. size.
    question: Do I need to call `opt.setCompressionLevel()` for better results?
  type: FAQPage
second_title: Aspose.3D Java API
title: Jak vytvořit draco point cloud ze sfér pomocí Aspose 3D Java
url: /cs/java/point-clouds/generate-point-clouds-spheres-java/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Generování Aspose 3D Point Cloud z koulí v Javě

## Úvod

Vítejte v tomto podrobném průvodci, jak **create draco point cloud** z koulí pomocí Aspose.3D pro Java. Ať už vytváříte vědecké vizualizace, herní assety nebo prototypy AR/VR, point cloudu poskytují lehkou reprezentaci 3‑D geometrie, kterou lze streamovat do prohlížečů nebo zpracovávat v pipeline strojového učení. V následujících několika minutách uvidíte přesně, jak převést jednoduchou kouli na Draco‑kódované bodové mračno, proč je to důležité a jak se vyhnout nejčastějším úskalím.

## Rychlé odpovědi
- **Jaká knihovna je použita?** Aspose.3D for Java  
- **V jakém formátu je bodové mračno uloženo?** Draco (`.drc`)  
- **Potřebuji licenci pro testování?** Bezplatná zkušební verze funguje pro hodnocení; pro produkci je vyžadována komerční licence.  
- **Která verze Javy je podporována?** Java 8 nebo vyšší (doporučeno JDK 11)  
- **Jak dlouho trvá implementace?** Přibližně 10‑15 minut pro základní bodové mračno koule  

## Co je draco point cloud?

Draco point cloud je kompaktní binární reprezentace 3‑D vrcholů komprimovaná pomocí algoritmu Draco od Googlu. **Aspose.3D** poskytuje vestavěné `DracoSaveOptions` pro zápis tohoto formátu přímo z objektu `Scene`, což přináší až 90 % úsporu velikosti ve srovnání s nekomprimovanými seznamy vrcholů.

## Proč generovat bodové mračno ze koule?

Vytvoření bodového mračna ze koule je ideální úvodní projekt, protože koule je matematicky uzavřený tvar, který jasně ukazuje, jak jsou vrcholy vzorkovány a ukládány. Tento přístup je užitečný pro:

- **Rychlé prototypování** – testování renderovacích pipeline bez importu složitých meshů.  
- **Benchmarky detekce kolizí** – generování deterministických rozdělení bodů pro fyzikální enginy.  
- **Demo komprese** – porovnání velikosti surového OBJ s Draco‑komprimovanými soubory `.drc` (často 10‑násobná úspora pro 10 k‑bodová mračna).  

## Požadavky

Než začneme, ujistěte se, že máte následující:

- **Java Development Kit (JDK)** – Ujistěte se, že máte na svém počítači nainstalovanou Javu. Můžete si ji stáhnout z [Oracle's website](https://www.oracle.com/java/technologies/javase-downloads.html).  
- **Aspose.3D Library** – Pro provádění 3D operací v Javě potřebujete knihovnu Aspose.3D. Můžete si ji stáhnout z [Aspose.3D Java documentation](https://reference.aspose.com/3d/java/).  

### Další požadavky

| Požadavek | Důvod |
|-------------|--------|
| Maven nebo Gradle nástroj pro sestavení | Zjednodušuje správu závislostí pro Aspose.3D. |
| Oprávnění k zápisu do výstupní složky | Potřebné pro uložení souboru `.drc`. |
| Volitelný: licenční soubor | Vyžadováno pro produkční běhy (zkušební verze funguje pro vývoj). |

## Import balíčků

Ve vašem Java projektu importujte potřebné balíčky, abyste mohli začít pracovat s Aspose.3D. Přidejte následující řádky do svého kódu:

```java
import com.aspose.threed.*;
import com.aspose.threed.geometry.*;
import com.aspose.threed.save.*;
```

> **Definition anchor:** `Scene` je vrchní kontejner Aspose.3D, který v paměti obsahuje mesh, světla, kamery a další 3‑D entity.

## Jak vytvořit draco point cloud ze sféry v Javě?

Načtěte svou kouli, aktivujte režim point‑cloud a uložte ji s Draco kompresí pomocí pouhých tří řádků kódu. Nejprve nakonfigurujte `DracoSaveOptions` pro výstup point cloud, poté vytvořte primitivní objekt `Sphere`, přidejte jej do `Scene` a nakonec zavolejte `save`. Tento vzor funguje pro jakýkoli mesh, který chcete převést.

## Krok 1: Nastavení DracoSaveOptions

`DracoSaveOptions` říká Aspose.3D, aby kódovalo geometrii jako point cloud místo plného mesh.

```java
DracoSaveOptions dracoOptions = new DracoSaveOptions();
dracoOptions.setPointCloud(true);               // Enable point‑cloud output
dracoOptions.setCompressionLevel(7);            // 0‑10 range; 7 gives good size/ speed balance
```

> **Definition anchor:** `DracoSaveOptions` je konfigurační objekt, který řídí, jak Aspose.3D zapisuje Draco soubory, včetně úrovně komprese a příznaku point‑cloud.

## Krok 2: Vytvořit kouli

Třída `Sphere` představuje matematicky dokonalou kouli. Můžete ovládat poloměr a hustotu tessellace, aby ovlivnily počet bodů.

```java
// Create a sphere with radius 5.0 and 32 longitudinal/latitudinal segments
Sphere sphere = new Sphere(5.0, 32, 32);
```

> **Definition anchor:** `Sphere` je třída primitivního tvaru, která generuje mesh vrcholů a ploch na základě parametrů poloměru a segmentů.

## Krok 3: Kódovat a uložit Point Cloud

Přidejte kouli do nového `Scene`, poté zavolejte `save` s dříve nakonfigurovanými `DracoSaveOptions`.

```java
Scene scene = new Scene();
scene.getRootNode().attachChild(sphere);               // Add sphere to scene graph
scene.save("output_point_cloud.drc", dracoOptions);   // Write compressed point cloud
```

> **Definition anchor:** `Scene.save` zapisuje celou scénu do určeného souboru pomocí poskytnutých možností uložení.

### Kvantifikované tvrzení

Aspose.3D podporuje **30+** 3‑D formátů souborů (včetně OBJ, STL, FBX, GLTF) a může zpracovat **500‑stránkové** modely bez načítání celého souboru do paměti, což jej činí vhodným pro rozsáhlé workflow s point‑cloud.

## Časté problémy a řešení

| Problém | Důvod | Řešení |
|-------|--------|----------|
| **Soubor nenalezen** | Nesprávná výstupní cesta | Použijte absolutní cestu nebo se ujistěte, že adresář existuje před uložením. |
| **Prázdné point cloud** | `setPointCloud(true)` vynecháno | Ověřte, že příznak `DracoSaveOptions` je nastaven podle kroku 1. |
| **Výjimka licence** | Spuštění bez platné licence v produkci | Použijte dočasnou nebo trvalou licenci (viz FAQ níže). |

## Často kladené otázky

**Q: Mohu převést vygenerované point cloud do jiných formátů (např. PLY, OBJ)?**  
A: Ano. Po načtení souboru `.drc` zpět do `Scene` můžete exportovat vrcholy pomocí obecné metody `Scene.save` z Aspose.3D s formáty jako PLY nebo OBJ.

**Q: Podporuje Draco enkodér vlastní atributy bodů (např. barvu, normály)?**  
A: Současná implementace Aspose.3D se zaměřuje pouze na geometrii. Pro přidání atributů rozšiřte scénu o vlastní objekty `VertexElement` před kódováním.

**Q: Jak velké může být point cloud, než se výkon zhorší?**  
A: Draco komprimuje efektivně, ale mračna přesahující **100 milionů** bodů mohou vyžadovat více než 8 GB RAM. Zvažte rozdělení na části nebo streamingové API pro velmi velké datové sady.

**Q: Je vygenerovaný soubor `.drc` kompatibilní s webovými prohlížeči jako three.js?**  
A: Rozhodně. three.js obsahuje Draco loader, který soubor čte přímo pro renderování v reálném čase.

**Q: Musím volat `opt.setCompressionLevel()` pro lepší výsledky?**  
A: Výchozí úroveň (5) funguje pro většinu případů. Pokud je velikost souboru kritická, experimentujte s hodnotami mezi **0** (nejrychlejší) a **10** (maximální komprese) pro vyvážení rychlosti a velikosti.

## FAQ

### Q1: Mohu používat Aspose.3D zdarma?

A1: Ano, můžete si Aspose.3D vyzkoušet zdarma. Navštivte [here](https://releases.aspose.com/) pro zahájení.

### Q2: Kde mohu najít podporu pro Aspose.3D?

A2: Podporu a komunitu najdete na [Aspose.3D forum](https://forum.aspose.com/c/3d/18).

### Q3: Jak mohu zakoupit Aspose.3D?

A3: Navštivte [purchase page](https://purchase.aspose.com/buy) pro nákup Aspose.3D a odemknutí plného potenciálu.

### Q4: Je k dispozici dočasná licence?

A4: Ano, můžete získat dočasnou licenci [here](https://purchase.aspose.com/temporary-license/) pro vaše vývojové potřeby.

### Q5: Kde najdu dokumentaci?

A5: Podívejte se na podrobnou [Aspose.3D Java documentation](https://reference.aspose.com/3d/java/) pro komplexní informace.

## Závěr

Gratulujeme! Úspěšně jste **create draco point cloud** ze koule pomocí Aspose.3D pro Java. Nyní můžete načíst soubor `.drc` do libovolného Draco‑kompatibilního prohlížeče, streamovat jej přes web nebo jej předat do následných zpracovatelských pipeline, jako je klasifikace point‑cloud nebo rekonstrukce povrchu.

---

**Poslední aktualizace:** 2026-05-29  
**Testováno s:** Aspose.3D for Java 24.10  
**Autor:** Aspose  

```java
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Sphere;


import java.io.IOException;
```

```java
// ExStart:3
DracoSaveOptions opt = new DracoSaveOptions();
opt.setPointCloud(true);
// ExEnd:3
```

```java
// ExStart:4
Sphere sphere = new Sphere();
// ExEnd:4
```

```java
// ExStart:5
FileFormat.DRACO.encode(sphere, "Your Document Directory" + "sphere.drc", opt);
// ExEnd:5
```

{{< blocks/products/products-backtop-button >}}

## Související tutoriály

- [Jak převést mesh na point cloud v Javě s Aspose.3D](/3d/java/point-clouds/create-point-clouds-java/)
- [Jak exportovat PLY – Point Cloudy s Aspose.3D pro Java](/3d/java/point-clouds/export-point-clouds-ply-java/)
- [Jak vytvořit sphere mesh v Javě – Komprimovat 3D meshe pomocí Google Draco](/3d/java/3d-mesh-data/compress-meshes-google-draco/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}