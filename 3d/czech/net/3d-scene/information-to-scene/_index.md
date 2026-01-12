---
date: 2026-01-12
description: Naučte se, jak přidávat metadata do 3D scén pomocí Aspose.3D pro .NET,
  včetně toho, jak přidat informace o dodavateli a exportovat soubory 3D modelů.
linktitle: 'How to Add Metadata: Extracting Information to Scene Assets'
second_title: Aspose.3D .NET API
title: 'Jak přidat metadata: extrahování informací do scénových aktiv'
url: /cs/net/3d-scene/information-to-scene/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak přidat metadata: Extrahování informací do scénových aktiv

## Úvod

V tomto komplexním tutoriálu se dozvíte **jak přidat metadata** do vašich 3D scén pomocí Aspose.3D pro .NET. Přidání metadat, jako jsou údaje o dodavateli, vlastní jednotky měření a další informace o aktivu, činí vaše modely informativnějšími, vyhledávatelnými a připravenými pro následné pipeline, jako jsou herní enginy nebo platformy AR/VR.

## Rychlé odpovědi
- **Jaký je hlavní účel?** Vložit metadata (informace o dodavateli, jednotky, vlastní značky) přímo do 3D scény.  
- **Která knihovna se používá?** Aspose.3D pro .NET.  
- **Mohu exportovat model po přidání metadat?** Ano – můžete **exportovat 3D model** soubory, např. uložit jako FBX.  
- **Potřebuji licenci?** K dispozici je bezplatná zkušební verze; pro produkční nasazení je vyžadována komerční licence.  
- **Jaké verze .NET jsou podporovány?** .NET Framework 4.5+, .NET Core 3.1+, .NET 5/6.

## Co znamená „jak přidat metadata“ v 3D scéně?

Přidání metadat znamená připojit popisné informace – například název aplikace, dodavatele, jednotky měření nebo vlastní značky – k samotnému souboru scény. Tato data cestují s modelem, když **uložíte scénu jako FBX** nebo jiný podporovaný formát, což umožňuje následným nástrojům pochopit kontext bez externích souborů.

## Proč vkládat vlastní metadata a informace o dodavateli?

- **Vyhledatelnost:** Systémy správy aktiv mohou filtrovat modely podle dodavatele nebo typu jednotky.  
- **Interoperabilita:** Enginy, které čtou FBX, mohou automaticky použít správnou měřítko, pokud **definujete jednotky měření**.  
- **Branding:** Zahrnutí názvu aplikace a dodavatele posiluje vlastnictví a soulad s licencí.  

## Předpoklady

Než se pustíme dál, ujistěte se, že máte:

- Aspose.3D pro .NET nainstalovaný. Můžete jej stáhnout ze [stránky Aspose.3D pro .NET](https://releases.aspose.com/3d/net/).

## Importujte jmenné prostory

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## Krok 1: Inicializujte 3D scénu

```csharp
Scene scene = new Scene();
```

Vytvořte nový objekt `Scene`, který bude obsahovat veškerou geometrii a informace o aktivech.

## Krok 2: Nastavte aplikaci a **přidejte informace o dodavateli**

```csharp
scene.AssetInfo.ApplicationName = "Egypt";
scene.AssetInfo.ApplicationVendor = "Manualdesk";
```

Zde vložíme **název aplikace** a **informace o dodavateli**. Toto je základní část **jak přidat metadata**, která identifikuje zdroj modelu.

## Krok 3: **Definujte jednotky měření** pro přesné škálování

```csharp
scene.AssetInfo.UnitName = "pole";
scene.AssetInfo.UnitScaleFactor = 0.6;
```

Zadáním `UnitName` a `UnitScaleFactor` říkáte následným nástrojům, že jeden „pole“ odpovídá 0,6 metru (60 cm). Tento krok je nezbytný, když později **exportujete 3D model** soubory, aby měly správné reálné rozměry.

## Krok 4: **Uložte scénu jako FBX** – **exportujte 3D model** s metadaty

```csharp
var output = "Your Output Directory" + "InformationToScene.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Volání `Save` zapíše scénu do souboru FBX a vloží všechna metadata, která jsme přidali. Tím se demonstruje **jak přidat metadata** a následně **uložit scénu jako FBX**, čímž **exportujete 3D model** s kompletními informacemi o aktivu.

## Krok 5: Zobrazte zprávu o úspěchu

```csharp
Console.WriteLine("\nAsset information added successfully to Scene.\nFile saved at " + output);
```

Přátelská zpráva v konzoli potvrzuje, že metadata byla zapsána a uvádí umístění souboru.

## Časté problémy a tipy

- **Nesprávná měřítko jednotky:** Zkontrolujte, že `UnitScaleFactor` odpovídá skutečnému převodu; jinak se exportované modely mohou jevit jako příliš velké nebo malé.  
- **Chybějící informace o dodavateli:** Pokud je `ApplicationVendor` prázdné, některé prohlížeče zobrazí „Unknown“. Vždy jej nastavujte, pokud je to možné.  
- **Chyby v cestě souboru:** Ujistěte se, že výstupní adresář existuje; jinak `scene.Save` vyvolá výjimku.

## Často kladené otázky

### Q1: Mohu použít Aspose.3D pro .NET s jinými programovacími jazyky?

A1: Aspose.3D primárně podporuje .NET jazyky, ale můžete prozkoumat možnosti interoperability pro jiné jazyky.

### Q2: Je k dispozici bezplatná zkušební verze Aspose.3D pro .NET?

A2: Ano, bezplatnou zkušební verzi získáte [zde](https://releases.aspose.com/).

### Q3: Jak získám podporu pro dotazy související s Aspose.3D?

A3: Navštivte [forum Aspose.3D](https://forum.aspose.com/c/3d/18) pro komunitu a podporu.

### Q4: Mohu zakoupit dočasnou licenci pro Aspose.3D pro .NET?

A4: Ano, dočasnou licenci můžete získat [zde](https://purchase.aspose.com/temporary-license/).

### Q5: Kde najdu podrobnou dokumentaci pro Aspose.3D pro .NET?

A5: Odkaz na [dokumentaci](https://reference.aspose.com/3d/net/) poskytuje podrobné informace.

## Závěr

Nyní ovládáte **jak přidat metadata** do 3D scény pomocí Aspose.3D pro .NET – nastavením aplikace a informací o dodavateli, **definováním jednotek měření** a nakonec **uložením scény jako FBX** pro **export 3D modelu** souborů, které nesou všechny tyto cenné informace. Použijte tyto techniky k obohacení vašich aktiv, zvýšení vyhledatelnosti a připravenosti na jakýkoli následný workflow.

---

**Poslední aktualizace:** 2026-01-12  
**Testováno s:** Aspose.3D 24.11 pro .NET  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}