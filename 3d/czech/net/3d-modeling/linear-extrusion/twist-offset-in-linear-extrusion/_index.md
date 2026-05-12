---
date: 2026-03-23
description: Naučte se, jak přidat zkroutění do lineární extruze pomocí Aspose.3D
  pro .NET a zjistěte, jak použít extruzi pro projekty 3D modelování v ASP.NET.
linktitle: Twist Offset in Linear Extrusion
second_title: Aspose.3D .NET API
title: Jak přidat zkroucení do lineární extruze pomocí Aspose.3D pro .NET
url: /cs/net/3d-modeling/linear-extrusion/twist-offset-in-linear-extrusion/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak přidat zkroucení do lineární extruze pomocí Aspose.3D pro .NET

## Úvod

Pokud hledáte jasný, krok‑za‑krokem průvodce **jak přidat zkroucení** do lineární extruze, jste na správném místě. V tomto tutoriálu projdeme kompletní proces s Aspose.3D pro .NET a ukážeme vám **jak použít extruzi** k vytvoření dynamických 3D tvarů, které jsou ideální pro *asp.net 3d modelování* scénáře. Na konci budete mít připravený příklad, který demonstruje offset zkroucení, řezy a uložení výsledku jako soubor OBJ.

## Rychlé odpovědi
- **Co dělá „twist offset“?** Posouvá počáteční bod zkroucení podél osy extruze.  
- **Potřebuji licenci pro spuštění ukázky?** Dočasná licence funguje pro testování; plná licence je vyžadována pro produkci.  
- **Které verze .NET jsou podporovány?** .NET Framework 4.5+, .NET Core 3.1+, .NET 5/6+.  
- **Mohu změnit počet řezů?** Ano—upravením vlastnosti `Slices` můžete kontrolovat hladkost sítě.  
- **Je výstupní formát omezen na OBJ?** Ne, Aspose.3D podporuje mnoho formátů; OBJ je zde použito pro jednoduchost.

## Co je Twist Offset v lineární extruzi?

Twist offset určuje translační posun aplikovaný na operaci zkroucení. Místo otáčení kolem přesného začátku extruze geometrie začíná otáčet od zadaného vektoru offsetu, což vám poskytuje větší tvůrčí kontrolu nad konečným tvarem.

## Proč použít Aspose.3D pro .NET?

- **Kompletní API** – Zpracovává profily, transformace a širokou škálu formátů souborů.  
- **Cross‑platform** – Funguje na Windows, Linuxu a macOS s .NET Core.  
- **Optimalizováno pro výkon** – Generuje čisté sítě bez ručního výpočtu.  
- **Vynikající dokumentace** – Spousta příkladů pro urychlení vývoje.

## Předpoklady

Před zahájením se ujistěte, že máte:

- Aspose.3D pro .NET knihovnu: Stáhněte a nainstalujte knihovnu ze [stránky vydání](https://releases.aspose.com/3d/net/).  
- Váš vývojový prostředí: Visual Studio, Rider nebo jakékoli IDE podporující C#.

## Importujte jmenné prostory

Nejprve importujte jmenné prostory, které vám poskytují přístup k základním 3D třídám.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Tyto příkazy zpřístupňují `Scene`, `LinearExtrusion`, `Vector3` a další nezbytné typy ve vašem kódu.

## Postupný průvodce

### Krok 1: Inicializace základního profilu

Začínáme s jednoduchým obdélníkovým profilem a přidáváme mu malý poloměr zaoblení, aby hrany nebyly zcela ostré.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

### Krok 2: Vytvoření scény

`Scene` funguje jako kontejner pro všechny uzly, světla, kamery a geometrii.

```csharp
Scene scene = new Scene();
```

### Krok 3: Vytvoření uzlů

Do kořene scény jsou přidány dva podřízené uzly—jeden pro jednoduchou extruzi a druhý pro zkroucenou verzi. Levý uzel je posunut podél osy X pro vizuální oddělení.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

### Krok 4: Lineární extruze na levém uzlu (bez twist offsetu)

Zde ukazujeme základní extruzi s úplným 360° zkroucením a 100 řezy pro plynulost.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

### Krok 5: Lineární extruze na pravém uzlu s twist offsetem

Nyní aplikujeme twist offset `(3, 0, 0)`. Tento posunuje začátek zkroucení o tři jednotky podél osy X, čímž vytvoří viditelně posunutou šroubovici.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

### Krok 6: Uložení 3D scény

Nakonec zapíšeme scénu do souboru OBJ. Podle potřeby změňte výstupní cestu pro vaše prostředí.

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Časté problémy a řešení

| Problém | Proč se to děje | Řešení |
|---------|----------------|--------|
| **Zkroucení vypadá ploché** | `Slices` je nastaveno příliš nízko, což vede k hrubé síti. | Zvyšte `Slices` (např. na 200) pro plynulejší rotaci. |
| **Objekt je mimo střed** | `TwistOffset` používá světové souřadnice; uzel může být již posunut. | Aplikujte offset relativně k lokální transformaci uzlu nebo upravte posunutí uzlu podle toho. |
| **Soubor nebyl uložen** | Nesprávná výstupní cesta nebo chybějící oprávnění k zápisu. | Ověřte, že adresář existuje a aplikace má oprávnění k zápisu. |
| **Výjimka licence** | Spuštění bez platné licence v ne‑zkušební verzi. | Načtěte dočasnou nebo trvalou licenci před vytvořením scény. |

## Často kladené otázky

### Q1: Mohu použít Aspose.3D pro .NET s jinými programovacími jazyky?

**A1:** Aspose.3D primárně podporuje .NET jazyky, ale Aspose poskytuje podobné knihovny pro Java a další platformy.

### Q2: Jak získám dočasnou licenci pro Aspose.3D pro .NET?

**A2:** Navštivte [tento odkaz](https://purchase.aspose.com/temporary-license/) a získejte dočasnou licenci pro testovací účely.

### Q3: Existuje komunitní fórum pro Aspose.3D pro .NET?

**A3:** Rozhodně! Připojte se ke komunitě na [Aspose.3D Forum](https://forum.aspose.com/c/3d/18), kde můžete komunikovat s ostatními vývojáři a získat pomoc.

### Q4: Jsou k dispozici další příklady a dokumentace?

**A4:** Prozkoumejte [dokumentaci](https://reference.aspose.com/3d/net/) pro podrobné návody a příklady.

### Q5: Kde mohu zakoupit Aspose.3D pro .NET?

**A5:** Přejděte na [tento odkaz](https://purchase.aspose.com/buy) a proveďte nákup, čímž odemknete plný potenciál Aspose.3D.

### Q6: Mohu exportovat model do formátů jiných než OBJ?

**A6:** Ano—Aspose.3D podporuje FBX, STL, 3MF a mnoho dalších. Stačí změnit hodnotu enumu `FileFormat` v metodě `Save`.

### Q7: Jak se „jak přidat zkroucení“ liší od běžné rotace?

**A7:** Zkroucení postupně otáčí profil podél délky extruze, zatímco běžná rotace aplikuje jednorázový statický úhel. Offset přidává translační posun před zahájením rotace.

**Poslední aktualizace:** 2026-03-23  
**Testováno s:** Aspose.3D pro .NET (nejnovější vydání)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}