---
date: 2026-01-17
description: Naučte se, jak aplikovat PBR materiál na krabici pomocí Aspose.3D pro
  .NET, vytvořit PBR materiál a exportovat soubory STL ASCII s fyzikálně založeným
  renderováním.
linktitle: Applying PBR Material to Box
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

Vítejte ve fascinujícím světě 3D grafiky! V tomto krok‑za‑krokem průvodci se naučíte **how to apply pbr** materiál na krabici pomocí Aspose.3D pro .NET. Provedeme vás vytvořením PBR materiálu, jeho přidáním k meshi a nakonec **exporting STL ASCII**, abyste mohli model použít v jakémkoli následném pracovním postupu. Ať už vytváříte prototyp hry nebo vizualizaci produktu, zvládnutí tohoto postupu otevírá dveře k realistickému fyzikálně založenému renderování (PBR) ve vašich .NET aplikacích.

## Rychlé odpovědi
- **Jaký je hlavní cíl?** Aplikovat PBR materiál na krabici a exportovat jej jako STL ASCII.  
- **Která knihovna je použita?** Aspose.3D for .NET (how to use aspose).  
- **Potřebuji licenci?** Ano, pro produkci je vyžadována dočasná nebo plná licence.  
- **Podporovaný výstupní formát?** STL ASCII (export stl ascii) a mnoho dalších 3D formátů.  
- **Jak dlouho to trvá?** Přibližně 10‑15 minut pro základní implementaci.

## Co je PBR materiál?
Physically Based Rendering (PBR) je model stínování, který simuluje, jak světlo interaguje se skutečnými povrchy. Úpravou vlastností, jako jsou faktory metalic a roughness, můžete dosáhnout vysoce realistických výsledků bez ručního ladění složitých shaderů.

## Proč používat Physically Based Rendering (PBR)?
- **Realismus:** Materiály reagují na osvětlení způsobem, který odpovídá skutečné fyzice.  
- **Konzistence:** Stejný materiál vypadá správně za jakéhokoli osvětlení.  
- **Efektivita:** Moderní GPU jsou optimalizovány pro výpočty PBR, což vám poskytuje výkon zdarma.

## Předpoklady

Než se ponoříme do kódu, ujistěte se, že máte následující:

### Stáhněte a nainstalujte Aspose.3D pro .NET
Navštivte [Aspose.3D for .NET documentation](https://reference.aspose.com/3d/net/) pro podrobné instrukce ke stažení a instalaci knihovny.

### Získání licence
Chcete‑li odemknout plný potenciál Aspose.3D, pořiďte si platnou licenci. Dočasnou licenci můžete získat [zde](https://purchase.aspose.com/temporary-license/) nebo zakoupit plnou licenci [zde](https://purchase.aspose.com/buy).

## Importujte jmenné prostory
Nejprve se ujistěte, že importujete potřebné jmenné prostory pro využití možností Aspose.3D pro .NET:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Krok 1: Inicializace scény
Začněte inicializací 3D scény pomocí následujícího úryvku kódu:

```csharp
Scene scene = new Scene();
```

## Krok 2: Vytvoření PBR materiálu
Nyní **create pbr material**, který našemu objektu dodá realistický vzhled:

```csharp
PbrMaterial mat = new PbrMaterial();
```

## Krok 3: Nastavení vlastností materiálu
Doladěte vlastnosti materiálu tak, aby byl téměř kovový a velmi drsný — ideální pro kartáčovaný kovový povrch:

```csharp
mat.MetallicFactor = 0.9;
mat.RoughnessFactor = 0.9;
```

## Krok 4: Vytvoření krabice
Vytvořte krabici, na kterou bude aplikován PBR materiál:

```csharp
var boxNode = scene.RootNode.CreateChildNode("box", new Box());
```

## Krok 5: Přidání PBR materiálu k krabici
Přiřaďte dříve nakonfigurovaný **add pbr material** k vytvořenému uzlu krabice:

```csharp
boxNode.Material = mat;
```

## Krok 6: Uložení 3D scény jako STL ASCII
Nakonec **export stl ascii**, aby mohl být model otevřen v jakémkoli standardním 3D prohlížeči nebo sliceru:

```csharp
scene.Save("Your Output Directory" + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
```

Gratulujeme! Úspěšně jste aplikovali PBR materiál na krabici ve 3D scéně pomocí Aspose.3D pro .NET.

## Časté úskalí a tipy
- **Licence nenalezena:** Ujistěte se, že soubor licence je načten před jakýmkoli voláním Aspose; jinak knihovna běží v evaluačním režimu.  
- **Nesprávná cesta k souboru:** Použijte `Path.Combine`, abyste se vyhnuli chybějícím oddělovačům cest na různých OS.  
- **Roughness vs. Metallic:** Nastavení obou faktorů příliš vysoko může způsobit, že povrch vypadá plochý; experimentujte s hodnotami mezi 0.5‑0.9 pro vyvážený vzhled.

## Závěr
Vstup do 3D grafiky s Aspose.3D pro .NET otevírá dveře k neomezeným kreativním možnostem. Díky intuitivnímu API a robustním funkcím se tvorba vizuálně ohromujících scén stává příjemným zážitkem pro vývojáře. Dále zkuste nahradit krabici složitějším meshem nebo experimentovat s různými PBR texturami a sledovat, jak světlo reaguje.

## Často kladené otázky

**Q1: Is Aspose.3D compatible with other 3D file formats?**  
A1: Yes, Aspose.3D supports various 3D file formats, ensuring flexibility in your projects.

**Q2: Can I use Aspose.3D for commercial applications?**  
A2: Absolutely! Aspose.3D provides commercial licenses for seamless integration into your applications.

**Q3: Is there a trial version available?**  
A3: Yes, you can explore Aspose.3D's capabilities by downloading the free trial [here](https://releases.aspose.com/).

**Q4: Where can I find community support and discussions?**  
A4: Join the Aspose.3D community at [Aspose.3D Forums](https://forum.aspose.com/c/3d/18) for support and discussions.

**Q5: How do I obtain a temporary license for Aspose.3D?**  
A5: You can get a temporary license [here](https://purchase.aspose.com/temporary-license/) for evaluation purposes.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Poslední aktualizace:** 2026-01-17  
**Testováno s:** Aspose.3D 24.11 pro .NET  
**Autor:** Aspose  

---