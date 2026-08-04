---
date: 2026-03-26
description: Naučte se, jak přidat informace o dodavateli do 3D scény a jak uložit
  soubory FBX pomocí Aspose.3D pro .NET. Postupujte podle tohoto krok‑za‑krokem průvodce
  s připraveným kódem, který lze spustit.
linktitle: Extracting Information to Scene Assets
second_title: Aspose.3D .NET API
title: Jak přidat informace o dodavateli a uložit scénu FBX pomocí Aspose.3D
url: /cs/net/3d-scene/information-to-scene/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak přidat informace o dodavateli a uložit scénu FBX pomocí Aspose.3D

## Úvod

Vítejte v tomto komplexním tutoriálu, který ukazuje **jak přidat informace o dodavateli** do 3D scény a následně **jak uložit soubory FBX** pomocí Aspose.3D pro .NET. Ať už vytváříte architektonické vizualizace, herní assety nebo inženýrské modely, vložení metadat o dodavateli a aplikaci činí vaše scény informativnějšími a usnadňuje jejich následnou správu. Projděme si proces krok za krokem.

## Rychlé odpovědi
- **Co znamená „add vendor“?** Ukládá názvy aplikace a dodavatele do bloku AssetInfo scény.  
- **Který formát podporuje informace o dodavateli?** FBX (ASCII nebo binární) zachovává metadata při uložení.  
- **Jak uložit FBX?** Použijte `scene.Save(path, FileFormat.FBX7500ASCII)` nebo binární ekvivalent.  
- **Potřebuji licenci?** Bezplatná zkušební verze funguje pro vývoj; pro produkci je vyžadována komerční licence.  
- **Mohu změnit jednotky měření?** Ano, nastavte `AssetInfo.UnitName` a `AssetInfo.UnitScaleFactor`.

## Co je „how to add vendor“ v 3D scéně?
Přidání informací o dodavateli znamená naplnění vlastností `AssetInfo` objektu `Scene`. Tyto vlastnosti cestují se souborem a umožňují každému, kdo FBX soubor použije, zjistit, která aplikace jej vytvořila a kdo je dodavatelem.

## Proč přidávat informace o dodavateli?
- **Sledovatelnost:** Rychle identifikovat zdroj modelu ve velkých pipelinech.  
- **Shoda:** Některá odvětví vyžadují explicitní označování dodavatele pro správu aktiv.  
- **Automatizace:** Skripty mohou filtrovat nebo zpracovávat soubory na základě metadat o dodavateli.

## Požadavky

- Aspose.3D pro .NET nainstalováno. Můžete jej stáhnout ze stránky [Aspose.3D for .NET page](https://releases.aspose.com/3d/net/).

## Importujte jmenné prostory

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## Jak přidat informace o dodavateli

### Krok 1: Inicializace 3D scény

```csharp
Scene scene = new Scene();
```

Vytvoření nové `Scene` vám poskytne čisté plátno pro práci.

### Krok 2: Nastavení informací o aplikaci a dodavateli

```csharp
scene.AssetInfo.ApplicationName = "Egypt";
scene.AssetInfo.ApplicationVendor = "Manualdesk";
```

Zde ukazujeme **jak přidat informace o dodavateli** přiřazením smysluplných řetězců k `ApplicationName` a `ApplicationVendor`.

### Krok 3: Definování měrných jednotek

```csharp
scene.AssetInfo.UnitName = "pole";
scene.AssetInfo.UnitScaleFactor = 0.6;
```

Určení systému jednotek zajišťuje, že každý, kdo otevře FBX soubor, správně interpretuje rozměry. V tomto příkladu jeden „pole“ odpovídá 60 cm.

## Jak uložit scénu FBX

### Krok 4: Uložení scény (jak uložit fbx)

```csharp
var output = "Your Output Directory" + "InformationToScene.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Tento řádek ukazuje **jak uložit fbx** pomocí ASCII verze FBX 7.5.0. Pokud dáváte přednost binárnímu formátu, nahraďte `FBX7500ASCII` za `FBX7500Binary`.

> **Tip:** Udržujte příponu souboru `.fbx` v souladu s formátem, který zvolíte; jinak některé prohlížeče mohou obsah špatně interpretovat.

### Krok 5: Zobrazení zprávy o úspěchu

```csharp
Console.WriteLine("\nAsset information added successfully to Scene.\nFile saved at " + output);
```

Přátelská zpráva v konzoli potvrzuje, že scéna, včetně metadat o dodavateli, byla zapsána na disk.

## Časté problémy a řešení

| Problém | Řešení |
|-------|----------|
| **Informace o dodavateli se nezobrazují ve vieweru** | Ujistěte se, že jste soubor uložili jako **FBX ASCII** nebo **Binary**; některé starší prohlížeče čtou jen jeden formát. |
| **Cesta obsahuje mezery** | Obalte cestu uvozovkami nebo použijte `Path.Combine` pro vytvoření bezpečné cesty. |
| **Měřítko jednotky vypadá špatně** | Zkontrolujte `UnitScaleFactor`; jedná se o násobek vzhledem k metrům. |
| **Výjimka licence** | Použijte bezplatnou zkušební verzi pro testování; pro produkční sestavení získejte plnou licenci. |

## Často kladené otázky

**Q: Mohu použít Aspose.3D pro .NET s jinými programovacími jazyky?**  
A: Aspose.3D primárně podporuje .NET jazyky, ale můžete prozkoumat možnosti interoperability s jinými jazyky.

**Q: Je k dispozici bezplatná zkušební verze pro Aspose.3D pro .NET?**  
A: Ano, bezplatnou zkušební verzi můžete získat [zde](https://releases.aspose.com/).

**Q: Jak získám podporu pro dotazy týkající se Aspose.3D?**  
A: Navštivte [forum Aspose.3D](https://forum.aspose.com/c/3d/18) pro komunitu a podporu.

**Q: Mohu zakoupit dočasnou licenci pro Aspose.3D pro .NET?**  
A: Ano, dočasnou licenci můžete získat [zde](https://purchase.aspose.com/temporary-license/).

**Q: Kde najdu podrobnou dokumentaci pro Aspose.3D pro .NET?**  
A: Odkazujte se na [dokumentaci](https://reference.aspose.com/3d/net/) pro podrobné informace.

---

**Poslední aktualizace:** 2026-03-26  
**Testováno s:** Aspose.3D 24.11 pro .NET  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}