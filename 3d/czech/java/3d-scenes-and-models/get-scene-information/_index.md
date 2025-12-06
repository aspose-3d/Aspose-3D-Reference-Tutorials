---
date: 2025-12-06
description: Naučte se, jak ukládat soubory FBX a získávat informace o scéně pomocí
  Aspose.3D pro Javu. Tento krok‑za‑krokem průvodce zahrnuje nastavení názvu aplikace,
  definování měrných jednotek a export scény do formátu FBX.
language: cs
linktitle: How to Save FBX and Retrieve 3D Scene Info in Java
second_title: Aspose.3D Java API
title: Jak uložit FBX a získat informace o 3D scéně v Javě
url: /java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak uložit FBX a získat informace o 3D scéně v Javě

## Introduction

Pokud hledáte jasný, praktický návod, jak **uložit fbx** soubory a zároveň získat užitečná metadata z vašich 3D scén, jste na správném místě. V tomto tutoriálu projdeme každý krok pomocí knihovny **Aspose.3D Java**: od vytvoření scény, **nastavení názvu aplikace**, **definování měrných jednotek**, až po **export scény do FBX**. Na konci budete mít připravený FBX soubor, který nese informace o assetech potřebné pro následné pipeline.

## Quick Answers
- **Jaký je hlavní cíl?** Uložit FBX soubor, který obsahuje vlastní informace o assetech.  
- **Která knihovna se používá?** Aspose.3D for Java.  
- **Potřebuji licenci?** Bezplatná zkušební verze funguje pro vývoj; pro produkci je vyžadována komerční licence.  
- **Mohu změnit měrné jednotky?** Ano – použijte `setUnitName` a `setUnitScaleFactor`.  
- **Kam se ukládá výstup?** Na cestu, kterou zadáte v `scene.save(...)`.

## Prerequisites

Před zahájením se ujistěte, že máte:

- Pevné pochopení základní syntaxe Javy.  
- **Aspose.3D for Java** stažený a přidaný do vašeho projektu (můžete jej získat na oficiální [Aspose 3D download page](https://releases.aspose.com/3d/java/)).  
- Váš oblíbený Java IDE (IntelliJ IDEA, Eclipse, NetBeans atd.) správně nakonfigurovaný.

## Import Packages

V souboru Java importujte třídy Aspose.3D, které poskytují správu scény a podporu formátů souborů.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Tip:** Udržujte seznam importů co nejmenší, abyste se vyhnuli zbytečným závislostem a zlepšili dobu kompilace.

## What is the process for saving an FBX file?

Níže je stručný, krok za krokem průvodce, který ukazuje **jak přidat informace o assetech** do scény a poté **exportovat scénu do FBX**.

### Step 1: Initialize a 3D Scene

Nejprve vytvořte prázdný objekt `Scene`. Ten bude kontejnerem pro veškerou geometrii, světla, kamery a metadata assetů.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Step 2: Set Application and Vendor Information

Přidání vlastních metadat pomáhá následným nástrojům identifikovat zdroj souboru. Zde **nastavujeme název aplikace** a dodavatele pomocí objektu `AssetInfo`.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Proč je to důležité:** Mnoho pipeline filtruje nebo označuje assety na základě původní aplikace, což činí tento krok nezbytným pro velké projekty.

### Step 3: Define Measurement Units

Aspose.3D vám umožňuje specifikovat jednotkový systém, který vaše scéna používá. V tomto příkladu používáme starověkou egyptskou jednotku nazvanou „pole“ s vlastním měřítkovým faktorem.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Tip:** Upravit `unitScaleFactor` tak, aby odpovídal reálné velikosti vašich modelů; 1.0 představuje 1‑k‑1 mapování s vybranou jednotkou.

### Step 4: Export Scene to FBX

Nyní, když jsou informace o assetech připojeny, uložíme scénu jako FBX soubor. Volba `FileFormat.FBX7500ASCII` vytváří lidsky čitelný ASCII FBX, což je užitečné pro ladění.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddAssetInformationToScene
```

> **Pamatujte:** Nahraďte `"Your Document Directory"` absolutní cestou nebo cestou relativní k pracovnímu adresáři vašeho projektu.

### Step 5: Print Success Message

Jednoduchý výstup do konzole potvrzuje, že operace byla úspěšná, a říká vám, kam byl soubor zapsán.

```java
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
```

## Common Use Cases

- **Pipeline herních assetů** – vložit informace o tvůrci přímo do FBX souborů pro sledování verzí.  
- **Architektonická vizualizace** – uložit jednotky specifické pro projekt, aby se předešlo chybám měřítka při importu do renderovacích enginů.  
- **Automatizované reportování** – generovat FBX soubory za běhu s metadaty, která mohou číst následné analytické nástroje.

## Troubleshooting & Tips

| Problém | Řešení |
|-------|----------|
| **Soubor nebyl po uložení nalezen** | Ověřte, že `MyDir` ukazuje na existující složku a že má vaše aplikace oprávnění k zápisu. |
| **Jednotky se zobrazují nesprávně v externím prohlížeči** | Zkontrolujte `unitScaleFactor`; některé prohlížeče očekávají metry jako základní jednotku. |
| **Metadata assetu chybí** | Ujistěte se, že voláte `scene.getAssetInfo()` **před** uložením; změny provedené po `save()` nebudou zachovány. |

## FAQ's

### Q1: Je Aspose.3D kompatibilní se všemi Java IDE?

A1: Ano, Aspose.3D je navrženo tak, aby fungovalo bez problémů se všemi hlavními Java IDE.

### Q2: Mohu používat Aspose.3D pro komerční projekty?

A2: Rozhodně. Aspose.3D nabízí komerční licence pro vývojáře, což zajišťuje soulad s licenčními požadavky.

### Q3: Kde mohu najít další podporu pro Aspose.3D?

A3: Pro jakékoli dotazy nebo pomoc navštivte [Aspose.3D forum](https://forum.aspose.com/c/3d/18).

### Q4: Je k dispozici bezplatná zkušební verze Aspose.3D?

A4: Ano, můžete si funkce vyzkoušet pomocí bezplatné zkušební verze dostupné [zde](https://releases.aspose.com/).

### Q5: Jak mohu získat dočasnou licenci pro Aspose.3D?

A5: Získejte dočasnou licenci pro testovací účely [zde](https://purchase.aspose.com/temporary-license/).

## Frequently Asked Questions

**Q: Jak změním výstupní formát na binární FBX?**  
A: Nahraďte `FileFormat.FBX7500ASCII` za `FileFormat.FBX7500` při volání `scene.save(...)`.

**Q: Mohu přidat vlastní uživatelem definovaná metadata nad rámec vestavěných polí assetu?**  
A: Ano, použijte `scene.getUserData().add("Key", "Value")` pro vložení dalších párů klíč‑hodnota.

**Q: Podporuje Aspose.3D jiné exportní formáty jako OBJ nebo GLTF?**  
A: Ano. Stačí změnit výčet `FileFormat` na `OBJ` nebo `GLTF2` podle potřeby.

**Q: Jaká verze Javy je požadována?**  
A: Aspose.3D for Java podporuje Java 8 a novější.

**Q: Je možné načíst existující FBX, upravit jeho informace o assetech a znovu uložit?**  
A: Rozhodně. Načtěte soubor pomocí `new Scene("input.fbx")`, upravte `scene.getAssetInfo()`, a poté uložte.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Poslední aktualizace:** 2025-12-06  
**Testováno s:** Aspose.3D for Java 24.11  
**Autor:** Aspose