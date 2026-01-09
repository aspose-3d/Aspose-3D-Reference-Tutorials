---
date: 2026-01-09
description: Naučte se, jak vytvořit 3D scénu v .NET pomocí Aspose.3D a objevte, jak
  zkroucením extruze využít techniky lineárního zkroucení extruze.
linktitle: Twist in Linear Extrusion
second_title: Aspose.3D .NET API
title: Vytvořte 3D scénu .NET – Otočení v lineární extruzi
url: /cs/net/3d-modeling/linear-extrusion/twist-in-linear-extrusion/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Vytvořte 3D scénu .NET – Otočení v lineární extruzi

## Úvod

Ve stále se vyvíjejícím světě .NET vývoje je využití síly 3D grafiky vzrušujícím úkolem. **Aspose.3D for .NET** představuje cenný nástroj, který vývojářům umožňuje **vytvořit 3D scénu .NET** aplikace, jež jsou jak pohlcující, tak vizuálně úchvatné. V tomto komplexním průvodci prozkoumáme zajímavou funkci — Lineární extruze s otočením — a provedeme vás každým krokem, abyste mohli s jistotou přidávat dynamické otáčky do svých modelů.

## Rychlé odpovědi
- **Co znamená „vytvořit 3d scénu .net“?** Odkazuje na programové vytvoření 3‑D scény pomocí knihovny Aspose.3D v prostředí .NET.  
- **Jak přidám otočení k extruzi?** Nastavte vlastnost `Twist` u objektu `LinearExtrusion`; hodnota představuje úhel rotace ve stupních.  
- **Potřebuji licenci pro Aspose.3D?** Bezplatná zkušební verze stačí pro hodnocení; pro produkční použití je vyžadována komerční licence.  
- **Které verze .NET jsou podporovány?** .NET Framework 4.5+, .NET Core 3.1+, .NET 5/6 a novější.  
- **Jaký dopad má hodnota `Slices`?** Více řezu poskytuje hladší otočení, ale zvyšuje paměťovou a výpočetní náročnost.

## Co je lineární extruze s otočením?
Lineární extruze táhne 2‑D profil podél přímé dráhy, zatímco vlastnost **twist** postupně otáčí profil a vytváří šroubovitý efekt. Tato technika je ideální pro modelování pružin, zkroucených sloupů nebo dekorativních prvků.

## Proč použít Aspose.3D pro tento úkol?
- **Jednoduché API** – intuitivní třídy jako `LinearExtrusion` a `RectangleShape`.  
- **Plná integrace s .NET** – funguje hladce s C#, VB.NET i F#.  
- **Cross‑platform výstup** – export do OBJ, STL, FBX a mnoha dalších formátů.

## Předpoklady

Než se vydáme na tuto 3D cestu, ujistěte se, že máte připravené následující předpoklady:

- Aspose.3D for .NET: Ujistěte se, že jste nainstalovali knihovnu Aspose.3D. Pokud ne, můžete ji stáhnout [zde](https://releases.aspose.com/3d/net/).

- Základní znalosti vývoje v .NET: Tento tutoriál předpokládá základní porozumění vývoji v .NET.

## Importujte jmenné prostory

V jakémkoli .NET projektu je správné používání jmenných prostorů klíčové. Začněte importováním potřebných jmenných prostorů, abyste mohli efektivně využívat funkce Aspose.3D. Níže je úryvek, který vás provede:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Jak vytvořit 3d scénu .net s lineárním otočením extruze

Níže je krok‑za‑krokem průvodce, který ukazuje přesně, jak **vytvořit 3D scénu .NET** a aplikovat otočení na lineární extruzi.

### Krok 1: Inicializujte základní profil

```csharp
// Initialize the base profile to be extruded
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

Začínáme definicí obdélníkového profilu. Pokud chcete, můžete upravit `RoundingRadius` pro zaoblení rohů.

### Krok 2: Vytvořte 3D scénu

```csharp
// Create a scene 
Scene scene = new Scene();
```

Objekt `Scene` funguje jako plátno, kde budou umístěny všechny 3‑D objekty.

### Krok 3: Vytvořte levý a pravý uzel

```csharp
// Create left node
var left = scene.RootNode.CreateChildNode();
// Create right node
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
```

Uzly jsou kontejnery pro geometrii. Vytvoříme dva uzly, abychom mohli porovnat ne‑otočenou extruzi (vlevo) s otočenou (vpravo). Levý uzel je posunut o 15 jednotek podél osy X pro vizuální oddělení.

### Krok 4: Proveďte lineární extruzi s otočením na levém uzlu

```csharp
// Twist property defines the degree of the rotation while extruding the profile
// Perform linear extrusion on the left node using twist and slices property
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 0, Slices = 100 });
```

Zde je `Twist` nastaven na **0°**, což vytváří rovnou extruzi. Hodnota `Slices` **100** poskytuje hladký povrch.

### Krok 5: Proveďte lineární extruzi s otočením na pravém uzlu

```csharp
// Perform linear extrusion on the right node using twist and slices property
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 90, Slices = 100 });
```

Nastavením `Twist = 90` otáčíte profil o plných 90 stupňů během délky extruze, čímž vzniká výrazná šroubovice.

### Krok 6: Uložte 3D scénu

```csharp
// Save 3D scene
scene.Save("Your Output Directory" + "TwistInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Scéna je exportována jako soubor OBJ, který můžete otevřít ve většině 3‑D prohlížečů nebo importovat do dalších pipeline.

## Časté problémy a řešení

| Problém | Proč se vyskytuje | Jak opravit |
|---------|-------------------|-------------|
| **Otočení vypadá ploché** | `Slices` je příliš nízký, což způsobuje hrubou geometrii. | Zvyšte `Slices` (např. na 200) pro hladší otáčky. |
| **Výkon klesá při vysokém počtu `Slices`** | Více polygonů vyžaduje více paměti/CPU. | Použijte nejnižší `Slices`, které stále splňují vizuální kvalitu, nebo povolte zjednodušení geometrie po extruzi. |
| **Soubor nebyl při uložení nalezen** | Cesta výstupního adresáře je neplatná. | Zadejte úplnou absolutní cestu nebo se ujistěte, že adresář existuje před voláním `Save`. |

## Často kladené otázky

**Q: Mohu použít lineární extruzi s otočením i na jiné tvary?**  
A: Rozhodně! Můžete experimentovat s různými základními profily mimo obdélníky a odemknout tak nespočet designových možností.

**Q: Jakou roli hraje vlastnost 'Twist' v lineární extruzi?**  
A: Vlastnost 'Twist' určuje úhel rotace během procesu extruze, což ovlivňuje konečný 3D tvar.

**Q: Existují výkonnostní úvahy při použití vysokého počtu řezů?**  
A: Vyšší počet řezů přidává detail, ale může ovlivnit výkon. Najděte rovnováhu podle požadavků vaší aplikace.

**Q: Mohu kombinovat lineární extruzi s dalšími funkcemi Aspose.3D?**  
A: Ano! Aspose.3D nabízí bohatou sadu funkcí. Klidně kombinujte lineární extruzi s dalšími možnostmi pro složitější návrhy.

**Q: Existuje komunita pro podporu a diskuze o Aspose.3D?**  
A: Ano, připojte se ke komunitě Aspose.3D na [Aspose Forum](https://forum.aspose.com/c/3d/18) pro podporu a zajímavé diskuze.

---

**Poslední aktualizace:** 2026-01-09  
**Testováno s:** Aspose.3D 24.11 for .NET  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}