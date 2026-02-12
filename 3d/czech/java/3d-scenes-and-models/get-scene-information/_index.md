---
date: 2026-02-12
description: Naučte se, jak exportovat scénu do formátu FBX a získat informace o 3D
  scéně pomocí Aspose.3D pro Javu. Tento krok‑za‑krokem průvodce zahrnuje nastavení
  názvu aplikace, definování měrných jednotek a export scény do FBX.
linktitle: How to Save FBX and Retrieve 3D Scene Info in Java
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

Pokud hledáte jasný, praktický návod na **jak exportovat scénu do FBX** a zároveň získat užitečná metadata z vašich 3D scén, jste na správném místě. V tomto tutoriálu projdeme každý krok pomocí knihovny **Aspose.3D Java**: od vytvoření scény, **nastavení názvu aplikace**, **definování měrných jednotek**, až po **export scény do FBX**. Na konci budete mít připravený FBX soubor, který nese informace o assetu potřebné pro downstream pipeline.

## Rychlé odpovědi
- **Jaký je hlavní cíl?** Exportovat scénu do FBX, která obsahuje vlastní informace o assetu.  
- **Která knihovna je použita?** Aspose.3D for Java.  
- **Potřebuji licenci?** Bezplatná zkušební verze funguje pro vývoj; pro produkci je vyžadována komerční licence.  
- **Mohu změnit měrné jednotky?** Ano – použijte `setUnitName` a `setUnitScaleFactor`.  
- **Kam se ukládá výstup?** Na cestu, kterou zadáte v `scene.save(...)`.

## Požadavky

Než začneme, ujistěte se, že máte:

- Solidní znalost základní syntaxe Javy.  
- **Aspose.3D for Java** stažený a přidaný do vašeho projektu (můžete jej získat z oficiální) [Aspose 3D download page](https://releases.aspose.com/3d/java/).  
- Váš oblíbený Java IDE (IntelliJ IDEA, Eclipse, NetBeans, atd.) správně nakonfigurovaný.

## Import balíčků

Ve vašem Java zdrojovém souboru importujte třídy Aspose.3D, které poskytují podporu pro práci se scénou a formáty souborů.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Tip:** Udržujte seznam importů na minimu, abyste se vyhnuli zbytečným závislostem a zlepšili dobu kompilace.

## Jaký je proces ukládání souboru FBX?

Níže je stručný, krok za krokem průvodce, který ukazuje **jak přidat informace o assetu** do scény a poté **exportovat scénu do FBX**.

### Krok 1: Inicializace 3D scény

Nejprve vytvořte prázdný objekt `Scene`. Ten bude kontejnrem pro veškerou geometrii, světla, kamery a metadata assetu.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Krok 2: Nastavení informací o aplikaci a dodavateli

Přidání vlastních metadat pomáhá downstream nástrojům identifikovat zdroj souboru. Zde **nastavíme název aplikace** a dodavatele pomocí objektu `AssetInfo`.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Proč je to důležité:** Mnoho pipeline filtruje nebo označuje assety na základě původní aplikace, což činí tento krok nezbytným pro velké projekty.

### Krok 3: Definování měrných jednotek

Aspose.3D vám umožňuje specifikovat jednotkový systém, který vaše scéna používá. V tomto příkladu používáme starověkou egyptskou jednotku nazvanou „pole“ s vlastním měřítkovým faktorem.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Tip:** Nastavte `unitScaleFactor` tak, aby odpovídal skutečné velikosti vašich modelů; 1.0 představuje 1‑k‑1 mapování s vybranou jednotkou.

### Krok 4: Export scény do FBX

Nyní, když jsou informace o assetu připojeny, uložíme scénu jako soubor FBX. Volba `FileFormat.FBX7500ASCII` vytváří lidsky čitelný ASCII FBX, což je užitečné pro ladění.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddAssetInformationToScene
```

> **Pamatujte:** Nahraďte `"Your Document Directory"` absolutní cestou nebo cestou relativní k pracovnímu adresáři vašeho projektu.

### Krok 5: Vytisknutí úspěšné zprávy

Jednoduchý výstup do konzole potvrzuje, že operace byla úspěšná, a říká vám, kam byl soubor zapsán.

```java
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
```

## Proč exportovat scénu do FBX pomocí Aspose.3D?

Export do FBX je běžná požadavek, protože FBX je široce podporován herními enginy, DCC nástroji a AR/VR pipeline. Aspose.3D vám poskytuje plnou kontrolu nad exportovaným souborem — metadata, jednotky a geometrie — bez potřeby těžké 3D autorizační aplikace. To umožňuje rychlé a spolehlivé automatické generování assetů, dávkové zpracování a konverze na serveru.

## Běžné případy použití

- **Game asset pipelines** – vložte informace o tvůrci přímo do FBX souborů pro sledování verzí.  
- **Architectural visualization** – uložte jednotky specifické pro projekt, aby se předešlo chybám měřítka při importu do renderovacích enginů.  
- **Automated reporting** – generujte FBX soubory za běhu s metadaty, která downstream analytické nástroje mohou číst.  
- **Cloud‑based 3D services** – programově vytvořte a exportujte scény bez GUI, ideální pro SaaS platformy.

## Řešení problémů a tipy

| Problém | Řešení |
|-------|----------|
| **File not found after save** | Ověřte, že `MyDir` ukazuje na existující složku a že má vaše aplikace oprávnění k zápisu. |
| **Units appear incorrect in external viewer** | Zkontrolujte `unitScaleFactor`; některé prohlížeče očekávají metry jako základní jednotku. |
| **Asset metadata missing** | Ujistěte se, že voláte `scene.getAssetInfo()` **před** uložením; změny provedené po `save()` nebudou zachovány. |
| **Performance bottleneck on large scenes** | Použijte `scene.optimize()` před uložením ke snížení využití paměti. |
| **ASCII FBX is too large** | Přepněte na binární FBX použitím `FileFormat.FBX7500` (viz FAQ). |

## Často kladené otázky

### Q1: Je Aspose.3D kompatibilní se všemi Java IDE?
A1: Ano, Aspose.3D je navrženo tak, aby fungovalo bez problémů se všemi hlavními Java IDE.

### Q2: Mohu používat Aspose.3D pro komerční projekty?
A2: Rozhodně. Aspose.3D nabízí komerční licence pro vývojáře, což zajišťuje, že splňujete licenční požadavky.

### Q3: Kde mohu najít další podporu pro Aspose.3D?
A3: Pro jakékoli dotazy nebo pomoc navštivte [Aspose.3D forum](https://forum.aspose.com/c/3d/18).

### Q4: Je k dispozici bezplatná zkušební verze pro Aspose.3D?
A4: Ano, můžete si vyzkoušet funkce pomocí bezplatné zkušební verze dostupné [zde](https://releases.aspose.com/).

### Q5: Jak mohu získat dočasnou licenci pro Aspose.3D?
A5: Získejte dočasnou licenci pro testovací účely [zde](https://purchase.aspose.com/temporary-license/).

## Často kladené otázky

**Q: Jak změním výstupní formát na binární FBX?**  
A: Nahraďte `FileFormat.FBX7500ASCII` za `FileFormat.FBX7500` při volání `scene.save(...)`.

**Q: Mohu přidat vlastní uživatelem definovaná metadata nad rámec vestavěných polí assetu?**  
A: Ano, použijte `scene.getUserData().add("Key", "Value")` pro vložení dalších párů klíč‑hodnota.

**Q: Podporuje Aspose.3D další exportní formáty jako OBJ nebo GLTF?**  
A: Ano. Jednoduše změňte enum `FileFormat` na `OBJ` nebo `GLTF2` podle potřeby.

**Q: Jaká verze Javy je vyžadována?**  
A: Aspose.3D for Java podporuje Java 8 a novější.

**Q: Je možné načíst existující FBX, upravit jeho informace o assetu a znovu uložit?**  
A: Rozhodně. Načtěte soubor pomocí `new Scene("input.fbx")`, upravte `scene.getAssetInfo()`, a poté uložte.

## Závěr

Nyní máte kompletní, připravený workflow pro **export scény do FBX**, který vkládá cenné informace o assetu, jako je název aplikace, dodavatel a vlastní měrné jednotky. Tento přístup zjednodušuje správu assetů, snižuje ruční evidenci a zajišťuje, že downstream nástroje získají veškerý potřebný kontext. Neváhejte prozkoumat další exportní formáty, přidat vlastní uživatelská data nebo integrovat tento kód do větších automatizačních pipeline.

---

**Poslední aktualizace:** 2026-02-12  
**Testováno s:** Aspose.3D for Java 24.11  
**Autor:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}