---
date: 2026-09-08
description: Naučte se, jak definovat jednotky a exportovat scénu do FBX v Javě pomocí
  Aspose.3D. Tento krok‑za‑krokem průvodce ukazuje nastavení názvu aplikace, measurement
  units a získávání informací o 3D scene.
keywords:
- how to define units
- export scene to fbx
- how to set application name
- define measurement units
lastmod: 2026-09-08
linktitle: Jak uložit FBX a získat informace o 3D scéně v Javě
og_description: Naučte se, jak definovat jednotky a exportovat scénu do FBX v Javě
  s Aspose.3D. Průvodce zahrnuje nastavení názvu aplikace, measurement units a získávání
  informací o 3D scene v několika krocích.
og_image_alt: Guide showing how to define units and export a 3D scene to FBX using
  Aspose.3D Java
og_title: Jak definovat jednotky a exportovat scénu do FBX v Javě
schemas:
- author: Aspose
  dateModified: '2026-09-08'
  description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  headline: How to define units and export scene to FBX in Java
  type: TechArticle
- description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  name: How to define units and export scene to FBX in Java
  steps:
  - name: initialize a 3D scene
    text: The `Scene` class is Aspose.3D's top‑level container that represents an
      entire 3D scene, including geometry, lights, cameras, and metadata. First, create
      an empty `Scene` object. This will be the container for all geometry, lights,
      cameras, and asset metadata.
  - name: define measurement units
    text: The unit system determines the real‑world scale of the scene; Aspose.3D
      lets you specify a unit name and a scale factor relative to meters. In this
      example we use an ancient Egyptian unit called “pole” with a custom scale factor.
      > **Tip:** Adjust `unitScaleFactor` to match the real‑world size of yo
  - name: export scene to FBX
    text: Now that the asset information is attached, we save the scene as an FBX
      file. The `FileFormat.FBX7500ASCII` option produces a human‑readable ASCII FBX,
      which is handy for debugging. > **Remember:** Replace `"Your Document Directory"`
      with an absolute path or a path relative to your project's working
  type: HowTo
- questions:
  - answer: Replace `FileFormat.FBX7500ASCII` with `FileFormat.FBX7500` when calling
      `scene.save(...)`.
    question: How do I change the output format to binary FBX?
  - answer: Yes, use `scene.getUserData().add("Key", "Value")` to embed additional
      key‑value pairs.
    question: Can I add custom user‑defined metadata beyond the built‑in asset fields?
  - answer: It does. Simply change the `FileFormat` enum to `OBJ` or `GLTF2` as needed.
    question: Does Aspose.3D support other export formats like OBJ or GLTF?
  - answer: Aspose.3D for Java supports Java 8 and later.
    question: What version of Java is required?
  - answer: Absolutely. Load the file with `new Scene("input.fbx")`, modify `scene.getAssetInfo()`,
      then save.
    question: Is it possible to load an existing FBX, modify its asset info, and resave?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- export scene to fbx
- Aspose.3D
- Java 3D
- define units
- 3D asset metadata
title: Jak definovat jednotky a exportovat scénu do FBX v Javě
url: /cs/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak definovat jednotky a exportovat scénu do FBX v Javě

## Úvod

Pokud hledáte jasný, praktický návod, jak **definovat jednotky** a **exportovat scénu do FBX**, a zároveň získat užitečná metadata z vašich 3D scén, jste na správném místě. V tomto tutoriálu projdeme každý krok pomocí knihovny **Aspose.3D for Java**: od vytvoření scény, **nastavení názvu aplikace**, **definování měrných jednotek**, až po finální **export scény do FBX**. Na konci budete mít připravený soubor FBX, který obsahuje informace o assetu potřebné pro následné pipeline.

## Rychlé odpovědi
- **What is the primary goal?** Exportovat scénu do FBX, která obsahuje vlastní informace o assetu.  
- **Which library is used?** Aspose.3D for Java.  
- **Do I need a license?** Bezplatná zkušební verze funguje pro vývoj; pro produkci je vyžadována komerční licence.  
- **Can I change the measurement units?** Ano – použijte `setUnitName` a `setUnitScaleFactor`.  
- **Where is the output saved?** Do cesty, kterou zadáte v `scene.save(...)`.  

## Požadavky

Předtím, než začneme, ujistěte se, že máte:

- Solidní znalost základní syntaxe Javy.  
- **Aspose.3D for Java** stažený a přidaný do vašeho projektu (můžete jej získat z oficiální) [Aspose 3D download page](https://releases.aspose.com/3d/java/).  
- Váš oblíbený Java IDE (IntelliJ IDEA, Eclipse, NetBeans atd.) správně nakonfigurovaný.

## Import balíčků

Ve vašem Java zdrojovém souboru importujte třídy Aspose.3D, které poskytují podporu pro práci se scénou a souborovými formáty.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Pro tip:** Udržujte seznam importů co nejmenší, aby se předešlo zbytečným závislostem a zlepšily se časy kompilace.

## Jaký je proces ukládání souboru FBX?

Pro uložení scény jako souboru FBX vytvoříte `Scene`, nastavíte požadovaná metadata assetu, definujete měrnou jednotku a poté zavoláte `scene.save(path, FileFormat.FBX7500ASCII)`. Tento postup zapíše geometrii, materiály a metadata do ASCII FBX, který lze prohlížet nebo importovat nástroji v následném zpracování.

### Krok 1: inicializovat 3D scénu

Třída `Scene` je nejvyšší kontejner Aspose.3D, který představuje celou 3D scénu, včetně geometrie, světel, kamer a metadat. Nejprve vytvořte prázdný objekt `Scene`. Ten bude kontejnerem pro veškerou geometrii, světla, kamery a metadata assetu.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Jak nastavit název aplikace v Javě

Objekt `AssetInfo` ukládá metadata jako název aplikace, dodavatele a verzi pro scénu. Přidání vlastních metadat pomáhá nástrojům v následném zpracování identifikovat zdroj souboru. Použijte objekt `AssetInfo` k **nastavení názvu aplikace** (a dodavatele) před uložením souboru.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Proč je to důležité:** Mnoho pipeline filtruje nebo označuje assety na základě původní aplikace, což činí tento krok nezbytným pro velké projekty.

### Krok 3: definovat měrné jednotky

Systém jednotek určuje reálné měřítko scény; Aspose.3D vám umožňuje zadat název jednotky a měřítkový faktor relativní k metrům. V tomto příkladu používáme starověkou egyptskou jednotku nazvanou „pole“ s vlastním měřítkovým faktorem.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Tip:** Upravit `unitScaleFactor` tak, aby odpovídal reálné velikosti vašich modelů; 1.0 představuje poměr 1:1 s vybranou jednotkou.

### Krok 4: exportovat scénu do FBX

Nyní, když jsou informace o assetu připojeny, uložíme scénu jako soubor FBX. Volba `FileFormat.FBX7500ASCII` vytváří čitelný ASCII FBX, což je užitečné pro ladění.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
// ExEnd:AddAssetInformationToScene
```

> **Pamatujte:** Nahraďte `"Your Document Directory"` absolutní cestou nebo cestou relativní k pracovnímu adresáři vašeho projektu.

## Proč exportovat scénu do FBX pomocí Aspose.3D?

Aspose.3D podporuje **více než 50 vstupních a výstupních formátů** a dokáže zpracovat scény o stovkách stránek bez načítání celého souboru do paměti, což vám poskytuje plnou kontrolu nad exportovaným souborem — metadata, jednotky a geometrie — bez nutnosti těžké 3D autorizační aplikace. To umožňuje rychlé a spolehlivé automatizované generování assetů, dávkové zpracování a konverze na straně serveru.

## Běžné případy použití

- **Game asset pipelines** – vložte informace o tvůrci přímo do souborů FBX pro sledování verzí.  
- **Architectural visualization** – uložte projektem specifické jednotky, aby se předešlo chybám měřítka při importu do renderovacích enginů.  
- **Automated reporting** – generujte FBX soubory za běhu s metadaty, která mohou číst nástroje pro následnou analytiku.  
- **Cloud‑based 3D services** – programově vytvářejte a exportujte scény bez GUI, ideální pro SaaS platformy.

## Řešení problémů a tipy

| Problém | Řešení |
|-------|----------|
| **Soubor nenalezen po uložení** | Ověřte, že `MyDir` ukazuje na existující složku a že má vaše aplikace oprávnění k zápisu. |
| **Jednotky se zdají být nesprávné v externím prohlížeči** | Zkontrolujte `unitScaleFactor`; některé prohlížeče očekávají metry jako základní jednotku. |
| **Metadata assetu chybí** | Ujistěte se, že voláte `scene.getAssetInfo()` **před** uložením; změny provedené po `save()` nebudou zachovány. |
| **Úzké místo výkonu u velkých scén** | Použijte `scene.optimize()` před uložením ke snížení využití paměti. |
| **ASCII FBX je příliš velký** | Přepněte na binární FBX pomocí `FileFormat.FBX7500` (viz FAQ). |

## Často kladené otázky

**Q: Jak změním výstupní formát na binární FBX?**  
A: Nahraďte `FileFormat.FBX7500ASCII` za `FileFormat.FBX7500` při volání `scene.save(...)`.

**Q: Mohu přidat vlastní uživatelem definovaná metadata nad rámec vestavěných polí assetu?**  
A: Ano, použijte `scene.getUserData().add("Key", "Value")` k vložení dalších párů klíč‑hodnota.

**Q: Podporuje Aspose.3D další exportní formáty jako OBJ nebo GLTF?**  
A: Ano. Jednoduše změňte výčet `FileFormat` na `OBJ` nebo `GLTF2` podle potřeby.

**Q: Jaká verze Javy je vyžadována?**  
A: Aspose.3D for Java podporuje Java 8 a novější.

**Q: Je možné načíst existující FBX, upravit jeho informace o assetu a znovu uložit?**  
A: Rozhodně. Načtěte soubor pomocí `new Scene("input.fbx")`, upravte `scene.getAssetInfo()`, a poté uložte.

**Poslední aktualizace:** 2026-09-08  
**Testováno s:** Aspose.3D for Java 24.11  
**Autor:** Aspose

## Související tutoriály

- [Zmenšit velikost 3D souboru – Komprimovat scény pomocí Aspose.3D for Java](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [Jak nastavit barvu vector3 v Javě: změna difúzní barvy a správa 3D vlastností ve scénách Java pomocí Aspose.3D](/3d/java/3d-scenes-and-models/managing-3d-properties-scenes/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}