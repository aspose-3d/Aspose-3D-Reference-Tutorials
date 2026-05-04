---
date: 2026-05-04
description: Naučte se, jak exportovat scénu do FBX a nastavit název aplikace java
  pomocí Aspose.3D pro Java. Tento krok‑za‑krokem průvodce také ukazuje, jak definovat
  měrné jednotky a získat informace o 3D scéně.
keywords:
- export scene to fbx
- set application name java
- aspose 3d java
linktitle: Jak uložit FBX a získat informace o 3D scéně v Javě
second_title: Aspose.3D Java API
title: Jak exportovat scénu do FBX a získat informace o 3D scéně v Javě
url: /cs/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak exportovat scénu do FBX a získat informace o 3D scéně v Javě

## Úvod

Pokud hledáte jasný, praktický návod, jak **exportovat scénu do FBX** a zároveň získat užitečná metadata z vašich 3D scén, jste na správném místě. V tomto tutoriálu projdeme každý krok pomocí knihovny **Aspose.3D Java**: od vytvoření scény, **nastavení názvu aplikace**, **definování měrných jednotek**, až po finální **export scény do FBX**. Na konci budete mít připravený soubor FBX, který obsahuje informace o assetech potřebné pro následné pipeline.

## Rychlé odpovědi
- **Jaký je hlavní cíl?** Exportovat scénu do FBX, která obsahuje vlastní informace o assetech.  
- **Která knihovna se používá?** Aspose.3D for Java.  
- **Potřebuji licenci?** Bezplatná zkušební verze funguje pro vývoj; pro produkci je vyžadována komerční licence.  
- **Mohu změnit měrné jednotky?** Ano – použijte `setUnitName` a `setUnitScaleFactor`.  
- **Kam se ukládá výstup?** Na cestu, kterou zadáte v `scene.save(...)`.  

## Předpoklady

Než začneme, ujistěte se, že máte:

- Pevné pochopení základní syntaxe Javy.  
- **Aspose.3D for Java** stažený a přidaný do vašeho projektu (můžete jej získat z oficiální) [Aspose 3D download page](https://releases.aspose.com/3d/java/).  
- Váš oblíbený Java IDE (IntelliJ IDEA, Eclipse, NetBeans atd.) správně nakonfigurovaný.

## Import balíčků

Ve vašem Java zdrojovém souboru importujte třídy Aspose.3D, které poskytují podporu pro práci se scénou a formáty souborů.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Tip:** Udržujte seznam importů na minimu, aby se předešlo zbytečným závislostem a zlepšily se časy kompilace.

## Jaký je proces ukládání souboru FBX?

Níže je stručný, krok za krokem průvodce, který ukazuje **jak přidat informace o assetech** do scény a následně **exportovat scénu do FBX**.

### Krok 1: Inicializace 3D scény

Nejprve vytvořte prázdný objekt `Scene`. Ten bude kontejnrem pro veškerou geometrii, světla, kamery a metadata assetů.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Jak nastavit název aplikace v Javě

Přidání vlastních metadat pomáhá následným nástrojům identifikovat zdroj souboru. Použijte objekt `AssetInfo` k **nastavení názvu aplikace** (a dodavatele) před uložením souboru.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Proč je to důležité:** Mnoho pipeline filtruje nebo označuje assety na základě původní aplikace, což činí tento krok nezbytným pro velké projekty.

### Krok 3: Definice měrných jednotek

Aspose.3D vám umožňuje specifikovat systém jednotek, který vaše scéna používá. V tomto příkladu používáme starověkou egyptskou jednotku zvanou „pole“ s vlastním měřítkovým faktorem.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Tip:** Nastavte `unitScaleFactor` tak, aby odpovídal reálné velikosti vašich modelů; 1.0 představuje 1‑k‑1 mapování s vybranou jednotkou.

### Krok 4: Export scény do FBX

Nyní, když jsou informace o assetech připojeny, uložíme scénu jako soubor FBX. Volba `FileFormat.FBX7500ASCII` vytváří lidsky čitelný ASCII FBX, což je užitečné pro ladění.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddAssetInformationToScene
```

> **Pamatujte:** Nahraďte `"Your Document Directory"` absolutní cestou nebo cestou relativní k pracovnímu adresáři vašeho projektu.

### Krok 5: Vytisknout zprávu o úspěchu

Jednoduchý výstup do konzole potvrdí, že operace byla úspěšná, a řekne vám, kde byl soubor zapsán.

```java
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
```

## Proč exportovat scénu do FBX pomocí Aspose.3D?

Export do FBX je běžnou požadavkem, protože FBX je široce podporován herními enginy, DCC nástroji a AR/VR pipeline. Aspose.3D vám poskytuje plnou kontrolu nad exportovaným souborem — metadata, jednotky a geometrie — bez nutnosti těžké 3D autorizační aplikace. To umožňuje rychlé a spolehlivé automatické generování assetů, dávkové zpracování a konverze na serveru.

## Běžné případy použití

- **Pipeline pro herní assety** – vložte informace o tvůrci přímo do souborů FBX pro sledování verzí.  
- **Architektonická vizualizace** – uložte projektově specifické jednotky, aby se předešlo chybám měřítka při importu do renderovacích enginů.  
- **Automatizované reportování** – generujte FBX soubory za běhu s metadaty, která mohou číst následné analytické nástroje.  
- **Cloudové 3D služby** – programově vytvářejte a exportujte scény bez GUI, ideální pro SaaS platformy.

## Řešení problémů a tipy

| Issue | Solution |
|-------|----------|
| **Soubor nenalezen po uložení** | Ověřte, že `MyDir` ukazuje na existující složku a že má vaše aplikace oprávnění k zápisu. |
| **Jednotky se zobrazují nesprávně v externím prohlížeči** | Zkontrolujte `unitScaleFactor`; některé prohlížeče očekávají metry jako základní jednotku. |
| **Metadata assetu chybí** | Ujistěte se, že voláte `scene.getAssetInfo()` **před** uložením; změny provedené po `save()` nebudou zachovány. |
| **Úzké hrdlo výkonu u velkých scén** | Použijte `scene.optimize()` před uložením pro snížení využití paměti. |
| **ASCII FBX je příliš velký** | Přepněte na binární FBX pomocí `FileFormat.FBX7500` (viz FAQ). |

## Často kladené otázky

**Q: Jak změním výstupní formát na binární FBX?**  
A: Nahraďte `FileFormat.FBX7500ASCII` za `FileFormat.FBX7500` při volání `scene.save(...)`.

**Q: Mohu přidat vlastní uživatelem definovaná metadata nad rámec vestavěných polí assetu?**  
A: Ano, použijte `scene.getUserData().add("Key", "Value")` k vložení dalších párů klíč‑hodnota.

**Q: Podporuje Aspose.3D další exportní formáty jako OBJ nebo GLTF?**  
A: Ano. Stačí změnit výčtový typ `FileFormat` na `OBJ` nebo `GLTF2` podle potřeby.

**Q: Jaká verze Javy je požadována?**  
A: Aspose.3D for Java podporuje Java 8 a novější.

**Q: Je možné načíst existující FBX, upravit jeho informace o assetu a znovu uložit?**  
A: Rozhodně. Načtěte soubor pomocí `new Scene("input.fbx")`, upravte `scene.getAssetInfo()`, a poté uložte.

## Závěr

Nyní máte kompletní, připravený workflow pro **export scény do FBX** při vkládání cenných informací o assetech, jako je název aplikace, dodavatel a vlastní měrné jednotky. Tento přístup zjednodušuje správu assetů, snižuje ruční evidenci a zajišťuje, že následné nástroje získají veškerý potřebný kontext. Klidně prozkoumejte další exportní formáty, přidejte vlastní uživatelská data nebo integrujte tento kód do větších automatizačních pipeline.

---

**Poslední aktualizace:** 2026-05-04  
**Testováno s:** Aspose.3D for Java 24.11  
**Autor:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}