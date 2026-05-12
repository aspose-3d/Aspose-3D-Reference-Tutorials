---
date: 2026-03-23
description: Naučte se, jak vytvořit extruzi s otáčením pomocí Aspose.3D pro .NET.
  Tento krok‑za‑krokem průvodce pokrývá techniky lineární extruze s otáčením.
linktitle: Twist in Linear Extrusion
second_title: Aspose.3D .NET API
title: Jak vytvořit extruzi s kroucením v lineární extruzi
url: /cs/net/3d-modeling/linear-extrusion/twist-in-linear-extrusion/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak vytvořit extruzi s otáčením v lineární extruzi

## Úvod

Pokud vytváříte aplikace .NET, které potřebují poutavé 3D vizualizace, brzy zjistíte, že **jak vytvořit extruzi** je základní dovednost. Aspose.3D pro .NET vám poskytuje čisté, vysoce výkonné API pro převod jednoduchých 2‑D profilů na sofistikované 3‑D modely — zejména když k nim přidáte otáčení. V tomto tutoriálu projdeme každý krok, od nastavení scény až po uložení finálního OBJ souboru, abyste mohli vidět sílu lineární extruze s otáčením v praxi.

## Rychlé odpovědi
- **Jaká třída je primární pro extruzi?** `LinearExtrusion`
- **Která vlastnost přidává rotaci?** `Twist`
- **Kolik řezů (slices) poskytuje plynulé výsledky?** Přibližně 100 řezů (upravit podle potřeby)
- **Mohu použít jiné tvary?** Ano, libovolný `IProfile`, například kruhy, mnohoúhelníky nebo vlastní křivky
- **Jaký formát souboru je v příkladu použit?** Wavefront OBJ (`.obj`)

## Předpoklady

Než se pustíme do práce, ujistěte se, že máte následující:

- Aspose.3D pro .NET nainstalovaný. Pokud jste si jej ještě nestáhli, získáte jej **[zde](https://releases.aspose.com/3d/net/)**.
- Funkční vývojové prostředí .NET (Visual Studio, VS Code nebo jakékoli jiné IDE podle vašeho výběru).
- Základní znalost syntaxe C# a objektově orientovaných konceptů.

## Import jmenných prostorů

V jakémkoli .NET projektu je správné používání jmenných prostorů klíčové. Začněte importováním potřebných jmenných prostorů, abyste mohli efektivně využívat funkce Aspose.3D. Níže je ukázka, která vás provede tímto krokem:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Průvodce krok za krokem

### Krok 1: Inicializace základního profilu

Nejprve definujeme tvar, který bude extrudován. V tomto příkladu použijeme obdélník s malým poloměrem zaoblení, aby hrany měly jemnou křivku.

```csharp
// Initialize the base profile to be extruded
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

### Krok 2: Vytvoření 3D scény

Objekt `Scene` funguje jako plátno, kde žijí všechny 3‑D entity. Představte si jej jako jeviště pro vaši extruzi.

```csharp
// Create a scene 
Scene scene = new Scene();
```

### Krok 3: Přidání levých a pravých uzlů

Uzly vám umožňují organizovat objekty hierarchicky. Vytvoříme dva sourozenecké uzly — jeden pro rovnou extruzi a druhý pro verzi s otáčením.

```csharp
// Create left node
var left = scene.RootNode.CreateChildNode();
// Create right node
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
```

### Krok 4: Provedení lineární extruze s otáčením na levém uzlu

Vlastnost `Twist` určuje, o kolik se profil během extruze otočí. Nastavením na **0** získáte klasickou rovnou extruzi.

```csharp
// Twist property defines the degree of the rotation while extruding the profile
// Perform linear extrusion on the left node using twist and slices property
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 0, Slices = 100 });
```

### Krok 5: Provedení lineární extruze s otáčením na pravém uzlu

Nyní aplikujeme 90‑stupňové otáčení na stejný profil. Tím jasně demonstrujeme efekt **lineární extruze s otáčením**.

```csharp
// Perform linear extrusion on the right node using twist and slices property
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 90, Slices = 100 });
```

### Krok 6: Uložení 3D scény

Nakonec exportujeme scénu do formátu, který lze zobrazit v libovolném 3‑D prohlížeči. Příklad používá Wavefront OBJ, ale Aspose.3D podporuje i mnoho dalších formátů.

```csharp
// Save 3D scene
scene.Save("Your Output Directory" + "TwistInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Proč použít lineární extruzi s otáčením?

- **Rychlé prototypování:** Převádějte 2‑D skici na 3‑D díly bez ručního modelování.
- **Flexibilita designu:** Upravením hodnoty `Twist` vytvoříte spirály, šroubovité žebry nebo dekorativní prvky.
- **Výkonnostní přívětivost:** Parametr `Slices` vám umožní vyvážit vizuální věrnost a rychlost běhu.

## Časté problémy a tipy

- **Příliš mnoho řezů:** Zatímco 100 řezů vypadá plynule, extrémně vysoké hodnoty mohou zpomalit vykreslování. Otestujte nižší počty, pokud se objeví problémy s výkonem.
- **Negativní hodnoty otáčení:** Negativní `Twist` otáčí profil opačným směrem — užitečné pro zrcadlené návrhy.
- **Cesty k souborům:** Ujistěte se, že výstupní adresář existuje a máte oprávnění k zápisu; jinak `scene.Save` vyvolá výjimku.

## Závěr

V tomto tutoriálu jsme ukázali **jak vytvořit extruzi** s otáčením pomocí Aspose.3D pro .NET. Úpravou vlastností `Twist` a `Slices` můžete generovat širokou škálu tvarů, od jednoduchých zkroucených prutů po složité šroubovité struktury, a to vše pomocí několika řádků kódu.

## Často kladené otázky

**Q: Mohu aplikovat lineární extruzi s otáčením na jiné tvary?**  
A: Rozhodně! Jakákoli třída implementující `IProfile` — například `CircleShape`, `PolygonShape` nebo vlastní spline — může být extrudována s otáčením.

**Q: Co vlastně představuje vlastnost `Twist`?**  
A: Udává celkový úhel rotace (ve stupních), který se aplikuje na profil během délky extruze.

**Q: Ovlivní zvýšení počtu řezů využití paměti?**  
A: Ano, více řezů generuje více vrcholů a ploch, což spotřebuje více paměti a může ovlivnit výkon na zařízeních s omezenými zdroji.

**Q: Mohu kombinovat lineární extruzi s dalšími funkcemi Aspose.3D?**  
A: Určitě. Po extruzi můžete aplikovat materiály, textury nebo dokonce Boolean operace a vytvořit tak ještě bohatší modely.

**Q: Kde mohu získat pomoc nebo diskutovat nápady s ostatními vývojáři?**  
A: Připojte se ke komunitě Aspose.3D na **[Aspose fóru](https://forum.aspose.com/c/3d/18)** pro podporu, ukázky a diskuze.

---

**Poslední aktualizace:** 2026-03-23  
**Testováno s:** Aspose.3D 24.11 pro .NET  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}