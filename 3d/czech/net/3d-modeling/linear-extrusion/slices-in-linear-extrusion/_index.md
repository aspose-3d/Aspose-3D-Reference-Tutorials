---
date: 2026-01-09
description: Naučte se, jak vytvořit 3D scénu a uložit 3D model pomocí Aspose.3D pro
  .NET, včetně exportu Wavefront OBJ a lineárních extruzních řezů.
linktitle: Create 3D Scene with Linear Extrusion Slices
second_title: Aspose.3D .NET API
title: Vytvořte 3D scénu s lineárními extruzními řezy
url: /cs/net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Vytvořte 3D scénu s lineárními extruzními řezy

## Úvod

Vítejte ve světě 3D designu s Aspose.3D pro .NET! V tomto tutoriálu **vytvoříte 3d scénu** objektů, použijete lineární extruzi s vlastním počtem řezů a nakonec **uložíte 3d model** jako soubor Wavefront OBJ. Ať už vytváříte rychlý prototyp nebo vizualizaci připravenou pro produkci, níže uvedené kroky vám ukážou **jak používat Aspose** k vygenerování vysoce kvalitní geometrie přímo z C#.

## Rychlé odpovědi
- **Co znamená „vytvořit 3d scénu“?** To znamená vytvořit objekt Scene, který obsahuje všechny 3D entity (meshe, světla, kamery).  
- **Jaký formát se používá pro export?** Příklad exportuje do **Wavefront OBJ** (`export wavefront obj`).  
- **Kolik řezů mohu nastavit?** Můžete nastavit libovolné celé číslo; ukázka používá 2 a 10 řezů.  
- **Potřebuji licenci?** Pro produkční použití je vyžadována dočasná nebo plná licence.  
- **Mohu to spustit na .NET Core?** Ano, Aspose.3D podporuje .NET Framework i .NET Core.

## Předpoklady

Před tím než se ponoříte do světa 3D designu s Aspose.3D, ujistěte se, že máte následující předpoklady:

- **Knihovna Aspose.3D pro .NET:** Ujistěte se, že máte nainstalovanou knihovnu Aspose.3D. Můžete si ji stáhnout [zde](https://releases.aspose.com/3d/net/).

- **Integrované vývojové prostředí (IDE):** Použijte libovolné IDE kompatibilní s vývojem v .NET.

- **Základní znalost C#:** Seznamte se se základy programovacího jazyka C#.

- **Touha prozkoumat 3D design:** Váš zájem o tvorbu vizuálně úchvatných 3D modelů!

## Import jmenných prostorů

Abyste mohli zahájit svou 3D designovou cestu s Aspose.3D, musíte importovat potřebné jmenné prostory. To zajistí, že váš kód bude mít přístup k požadovaným třídám a funkcím.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Jak vytvořit 3d scénu s lineární extruzí

Níže projdeme každý krok potřebný k vytvoření scény, aplikaci extruze a **uložení 3d modelu** jako souboru OBJ. Vysvětlení jsou psána konverzačním stylem, aby bylo snadné je sledovat.

### Krok 1: Inicializace základního profilu

Nejprve definujeme 2‑D tvar, který bude extrudován. V tomto případě obdélník se zaoblenými rohy.

```csharp
// ExStart:InitializeBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd:InitializeBaseProfile
```

### Krok 2: Vytvoření 3D scény

Objekt `Scene` je kontejner pro veškerou geometrii, světla a kamery – jádro **vytváření 3d scény**.

```csharp
// ExStart:Create3DScene
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### Krok 3: Vytvoření levých a pravých uzlů

Přidáme dva podřízené uzly ke kořeni scény. Jeden použije nízký počet řezů, druhý vyšší, abyste viděli vizuální rozdíl.

```csharp
// ExStart:CreateLeftRightNodes
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### Krok 4: Provedení lineární extruze na levém uzlu

Zde extrudujeme obdélník s **2 řezy**. Méně řezů dává hrubší vzhled.

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### Krok 5: Provedení lineární extruze na pravém uzlu

Nyní extrudujeme stejný profil, ale s **10 řezy**, což vytváří hladší povrch.

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### Krok 6: Uložení 3D scény

Nakonec exportujeme scénu do souboru Wavefront OBJ. Toto demonstruje **jak uložit obj** a **exportovat wavefront obj** pomocí Aspose.3D.

```csharp
// ExStart:Save3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
// ExEnd:Save3DScene
```

## Časté problémy a řešení

| Problém | Proč k tomu dochází | Řešení |
|---------|----------------------|--------|
| Soubor OBJ je prázdný | Cesta k výstupu je nesprávná nebo chybí oprávnění k zápisu. | Ověřte, že adresář existuje a aplikace má právo zapisovat. |
| Řezy neovlivňují hladkost | `Slices` hodnota je příliš nízká pro velikost geometrie. | Zvyšte počet řezů nebo upravte rozměry profilu. |
| Výjimka licence | Spuštění bez platné licence v ne‑zkušební verzi. | Použijte dočasnou nebo trvalou licenci pomocí `License license = new License(); license.SetLicense("Aspose.3D.lic");` |

## Často kladené otázky

**Q: Mohu použít Aspose.3D pro .NET s jinými programovacími jazyky?**  
A: Aspose.3D je primárně navrženo pro .NET, ale můžete prozkoumat možnosti interoperability s jazyky jako Python pomocí .NET vazeb.

**Q: Kde najdu podrobnou dokumentaci pro Aspose.3D pro .NET?**  
A: Odkaz na dokumentaci [zde](https://reference.aspose.com/3d/net/) poskytuje podrobné informace o možnostech a použití Aspose.3D.

**Q: Je k dispozici bezplatná zkušební verze pro Aspose.3D pro .NET?**  
A: Ano, můžete získat bezplatnou zkušební verzi [zde](https://releases.aspose.com/) a prozkoumat funkce knihovny před zakoupením.

**Q: Jak mohu získat technickou podporu pro Aspose.3D pro .NET?**  
A: Navštivte fórum Aspose.3D [zde](https://forum.aspose.com/c/3d/18), kde můžete požádat o pomoc a komunikovat s komunitou.

**Q: Mohu použít dočasnou licenci pro Aspose.3D pro .NET?**  
A: Ano, získat dočasnou licenci [zde](https://purchase.aspose.com/temporary-license/) pro evaluační účely.

## Závěr

Gratulujeme! Úspěšně jste se naučili **vytvořit 3d scénu**, aplikovat lineární extruzi s vlastním počtem řezů a **uložit 3d model** jako soubor Wavefront OBJ pomocí Aspose.3D pro .NET. Toto je jen začátek vaší 3D designové cesty – neváhejte experimentovat s různými profily, hodnotami řezů a exportními formáty, abyste odhalili plný potenciál **3d modelování c#**.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Poslední aktualizace:** 2026-01-09  
**Testováno s:** Aspose.3D 24.11 pro .NET  
**Autor:** Aspose