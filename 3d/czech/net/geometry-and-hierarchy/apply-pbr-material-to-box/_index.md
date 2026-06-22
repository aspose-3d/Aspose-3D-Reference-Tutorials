---
date: 2026-04-12
description: Naučte se, jak aplikovat PBR materiál na krabici pomocí Aspose.3D pro
  .NET, vytvořit PBR materiál a exportovat STL ASCII soubory s fyzikálně založeným
  renderováním.
keywords:
- how to apply pbr
- create pbr material
- export stl ascii
- physically based rendering
- create box mesh
linktitle: Aplikace PBR materiálu na krabici
second_title: Aspose.3D .NET API
title: Jak aplikovat PBR materiál na krabici
url: /cs/net/geometry-and-hierarchy/apply-pbr-material-to-box/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak aplikovat PBR materiál na krabici

## Úvod

Vítejte ve fascinujícím světě 3D grafiky! V tomto krok‑za‑krokem tutoriálu **se naučíte, jak aplikovat pbr** materiál na krabici pomocí Aspose.3D pro .NET. Provedeme vás vytvořením PBR materiálu, jeho přidáním do sítě a nakonec **exportem STL ASCII**, abyste mohli model použít v jakémkoli následném pracovním postupu. Ať už vytváříte prototyp hry, vizualizaci produktu nebo rychlý prototyp pro 3D tisk, zvládnutí tohoto postupu otevírá dveře k realistickému fyzicky založenému renderování (PBR) ve vašich .NET aplikacích.

## Rychlé odpovědi
- **Jaký je hlavní cíl?** Aplikovat PBR materiál na krabici a exportovat jej jako STL ASCII.  
- **Která knihovna se používá?** Aspose.3D pro .NET (jak používat aspose).  
- **Potřebuji licenci?** Ano, pro produkci je vyžadována dočasná nebo plná licence.  
- **Podporovaný výstupní formát?** STL ASCII (export stl ascii) a mnoho dalších 3D formátů.  
- **Jak dlouho to trvá?** Přibližně 10‑15 minut pro základní implementaci.

## Co je PBR materiál?
Physically Based Rendering (PBR) je stínovací model, který simuluje, jak světlo interaguje s reálnými povrchy. Úpravou vlastností, jako jsou faktory metalic a drsnosti, můžete dosáhnout vysoce realistických výsledků bez ručního ladění složitých shaderů.

## Proč používat Physically Based Rendering (PBR)?
- **Realismus:** Materiály reagují na osvětlení způsobem, který odpovídá reálné fyzice.  
- **Konzistence:** Stejný materiál vypadá správně za jakéhokoli osvětlení.  
- **Efektivita:** Moderní GPU jsou optimalizovány pro výpočty PBR, což vám poskytuje výkon zdarma.

## Požadavky

Než se ponoříme do kódu, ujistěte se, že máte následující:

### Stáhněte a nainstalujte Aspose.3D pro .NET
Navštivte [Aspose.3D for .NET documentation](https://reference.aspose.com/3d/net/) pro podrobné instrukce ke stažení a instalaci knihovny.

### Získejte licenci
Pro odemčení plného potenciálu Aspose.3D získáte platnou licenci. Dočasnou licenci můžete získat [zde](https://purchase.aspose.com/temporary-license/) nebo zakoupit plnou licenci [zde](https://purchase.aspose.com/buy).

## Importujte jmenné prostory
Nejprve se ujistěte, že importujete potřebné jmenné prostory, abyste využili možnosti Aspose.3D pro .NET:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Průvodce krok za krokem

### Krok 1: Inicializace scény
Začněte vytvořením prázdné 3D scény. Tento kontejner bude obsahovat veškerou geometrii, materiály a světla, které později přidáte.

```csharp
Scene scene = new Scene();
```

### Krok 2: Vytvoření PBR materiálu
Nyní **vytvoříme pbr materiál**, který našemu boxu dodá realistický vzhled. Třída `PbrMaterial` poskytuje všechny parametry potřebné pro fyzicky založené renderování.

```csharp
PbrMaterial mat = new PbrMaterial();
```

### Krok 3: Nastavení vlastností materiálu
Jemně doladíte vlastnosti materiálu. V tomto příkladu uděláme povrch téměř kovový a velmi drsný — ideální pro kartáčovaný kovový box.

```csharp
mat.MetallicFactor = 0.9;
mat.RoughnessFactor = 0.9;
```

### Krok 4: Vytvoření boxové sítě
Vygenerujte jednoduchou geometrii boxu. Toto je krok **create box mesh**, na který odkazuje primární klíčové slovo.

```csharp
var boxNode = scene.RootNode.CreateChildNode("box", new Box());
```

### Krok 5: Aplikace PBR materiálu na box
Přiřaďte dříve nakonfigurovaný **add pbr material** k uzlu boxu, který jsme právě vytvořili.

```csharp
boxNode.Material = mat;
```

### Krok 6: Export STL ASCII (Jak exportovat STL)
Konečně **export stl ascii**, aby mohl být model otevřen v jakémkoli standardním 3D prohlížeči nebo sliceru. Použití `FileFormat.STLASCII` zaručuje soubor čitelný pro člověka.

```csharp
scene.Save("Your Output Directory" + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
```

## Časté úskalí a tipy
- **Licence nenalezena:** Ujistěte se, že soubor licence je načten *před* jakýmkoli voláním Aspose; jinak knihovna běží v evaluačním režimu.  
- **Nesprávná cesta k souboru:** Použijte `Path.Combine`, abyste se vyhnuli chybějícím oddělovačům cesty na různých operačních systémech.  
- **Rovnováha drsnosti vs. metalic:** Nastavení obou faktorů příliš vysoko může způsobit, že povrch vypadá plochý; experimentujte s hodnotami mezi `0.5‑0.9` pro vyvážený vzhled.  
- **Tip pro výkon:** Znovu použijte jedinou instanci `PbrMaterial`, pokud potřebujete aplikovat stejný materiál na více sítí; tím se sníží paměťová zátěž.

## Často kladené otázky

**Q1: Je Aspose.3D kompatibilní s jinými 3D formáty souborů?**  
A1: Ano, Aspose.3D podporuje širokou škálu 3D formátů souborů, což zajišťuje flexibilitu ve vašich projektech.

**Q2: Mohu používat Aspose.3D pro komerční aplikace?**  
A2: Rozhodně! Aspose.3D poskytuje komerční licence pro bezproblémovou integraci do produkčního softwaru.

**Q3: Je k dispozici zkušební verze?**  
A3: Ano, můžete prozkoumat možnosti Aspose.3D stažením bezplatné zkušební verze [zde](https://releases.aspose.com/).

**Q4: Kde mohu najít komunitní podporu a diskuze?**  
A4: Připojte se ke komunitě Aspose.3D na [Aspose.3D Forums](https://forum.aspose.com/c/3d/18) pro podporu a diskuze.

**Q5: Jak získám dočasnou licenci pro Aspose.3D?**  
A5: Dočasnou licenci můžete získat [zde](https://purchase.aspose.com/temporary-license/) pro evaluační účely.

## Závěr
Ponoření se do 3D grafiky s Aspose.3D pro .NET otevírá dveře k nekonečným tvůrčím možnostem. Díky intuitivnímu API a robustním funkcím se vytváření vizuálně úchvatných scén stává příjemným zážitkem pro vývojáře. Nyní, když víte, **jak aplikovat pbr** materiál na krabici a **exportovat STL ASCII**, zkuste nahradit krabici složitější sítí nebo experimentovat s texturovými mapami, abyste viděli, jak osvětlení reaguje v reálném čase.

---

**Poslední aktualizace:** 2026-04-12  
**Testováno s:** Aspose.3D 24.11 for .NET  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}
{{< blocks/products/products-backtop-button >}}