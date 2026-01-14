---
date: 2026-01-14
description: Naučte se animovat krychli ve 3D scénách pomocí Aspose.3D pro .NET. Tento
  průvodce ukazuje, jak vytvořit animační křivku, svázat klíčové snímky a animovat
  3D vlastnosti.
linktitle: Animating Properties to Document in 3D Scenes
second_title: Aspose.3D .NET API
title: Jak animovat krychli ve 3D scénách pomocí Aspose.3D pro .NET
url: /cs/net/animation/property-to-document/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak animovat krychli ve 3D scénách pomocí Aspose.3D pro .NET

## Úvod

Pokud se pouštíte do tvorby a animace 3D scén v .NET, Aspose.3D je vaším nástrojem volby. V tomto krok‑za‑krokem průvodci prozkoumáme **jak animovat krychli** pomocí animace jejích vlastností, vytváření animačních křivek a vázání keyframe. Na konci budete mít plně animovanou krychli, kterou můžete exportovat do populárních 3D formátů.

## Rychlé odpovědi
- **Jaká knihovna se používá?** Aspose.3D pro .NET  
- **Jaký hlavní úkol tento tutoriál pokrývá?** Jak animovat krychli ve 3D scéně  
- **Klíčové kroky?** Importovat jmenné prostory, vytvořit scénu, vázat keyframe, uložit soubor  
- **Potřebuji licenci?** Bezplatná zkušební verze stačí pro učení; komerční licence je vyžadována pro produkci  
- **Podporovaný výstupní formát?** FBX (ASCII 7500) a další formáty podporované Aspose.3D  

## Co je „jak animovat krychli“ v Aspose.3D?
Animace krychle znamená měnit její transformační vlastnosti (např. Translation, Rotation nebo Scale) v čase pomocí dat keyframe. Aspose.3D poskytuje čisté API pro vytvoření **animačních křivek**, **vázání keyframe** a **animaci 3D vlastností** přímo na uzlech scény.

## Proč animovat krychli pomocí Aspose.3D?
- **Plná integrace s .NET** – funguje s .NET Framework, .NET Core i .NET 5/6.  
- **Žádné externí závislosti** – není potřeba Unity ani jiné enginy pro jednoduché animace.  
- **Flexibilita exportu** – animované scény lze uložit jako FBX, OBJ, GLTF atd., pro další zpracování.

## Požadavky

Před tím, než se pustíme do této vzrušující cesty, ujistěte se, že máte následující předpoklady:

- Aspose.3D pro .NET: Ujistěte se, že máte knihovnu nainstalovanou. Můžete si ji stáhnout z [Aspose.3D webu](https://releases.aspose.com/3d/net/).

- Znalost C#: Znalost programovacího jazyka C# je nezbytná pro pochopení a implementaci příkladů.

- Integrované vývojové prostředí (IDE): Použijte své oblíbené IDE, například Visual Studio, pro psaní kódu podle příkladů.

- Základní pojmy 3D scény: Pochopení základních konceptů 3D scény vám usnadní učení.

## Importování jmenných prostorů

Ve svém C# kódu zajistěte import potřebných jmenných prostorů pro Aspose.3D. Zde je požadovaná sada:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose._3D.Examples.CSharp.Geometry_Hierarchy;
```

## Krok 1: Inicializace objektu Scene

Vytvořte prázdnou scénu, která bude obsahovat všechny naše uzly a animace.

```csharp
Scene scene = new Scene();
```

## Krok 2: Vytvoření mesh pomocí Polygon Builderu

Generujeme jednoduchou mesh krychle pomocí pomocné metody `Common.CreateMeshUsingPolygonBuilder()`.

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## Krok 3: Vytvoření uzlů krychle

Přidejte mesh krychle do scény jako podřízený uzel kořene. Název uzlu **cube1** bude použit později při vázání keyframe.

```csharp
Node cube1 = scene.RootNode.CreateChildNode("cube1", mesh);
```

## Krok 4: Najděte vlastnost Translation

Pro animaci pozice krychle musíme najít její **Translation** vlastnost na transformaci uzlu.

```csharp
Property translation = cube1.Transform.FindProperty("Translation");
```

## Krok 5: Vytvoření Bind Pointu

`BindPoint` spojuje vlastnost scény s animační křivkou. Zde vázáme vlastnost translation.

```csharp
BindPoint bindPoint = new BindPoint(scene, translation);
```

## Krok 6: Vázání animační křivky na komponentu X

Nyní vytvoříme animační křivku pro osu **X**. Toto demonstruje krok **create animation curve** a ukazuje, jak **bind keyframes**.

```csharp
bindPoint.BindKeyframeSequence("X", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, 20.0f, Interpolation.Bezier},
    {5, 30.0f, Interpolation.Linear},
});
```

## Krok 7: Vázání animační křivky na komponentu Z

Podobně animujeme osu **Z**, aby krychle měla dynamičtější trajektorii pohybu.

```csharp
bindPoint.BindKeyframeSequence("Z", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, -10.0f, Interpolation.Bezier},
    {5, 0.0f, Interpolation.Linear},
});
```

## Krok 8: Uložení 3D scény

Exportujte animovanou scénu do souboru FBX. Formát `FBX7500ASCII` je široce podporován 3D nástroji.

```csharp
string output = "Your Output Directory" + "PropertyToDocument.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

## Krok 9: Zobrazení zprávy o úspěchu

Dejte uživateli zpětnou vazbu, že animace byla úspěšně přidána.

```csharp
Console.WriteLine("\nAnimation property added successfully to document.\nFile saved at " + output);
```

## Časté problémy a řešení

| Problém | Důvod | Řešení |
|---------|-------|--------|
| Žádný pohyb pozorován | Časy keyframe neodpovídají přehrávacímu rozsahu | Ujistěte se, že časová osa animace scény zahrnuje časy keyframe (0‑5 sekund v tomto příkladu). |
| Nesprávná cesta k souboru | `output` ukazuje na neexistující adresář | Nejprve vytvořte adresář nebo použijte absolutní cestu. |
| Výjimka licence | Spuštění bez platné licence v produkci | Aplikujte svou Aspose.3D licenci před vytvořením `Scene`. |

## Často kladené otázky

### Q1: Kde mohu najít dokumentaci k Aspose.3D?

A1: Dokumentace je k dispozici [zde](https://reference.aspose.com/3d/net/).

### Q2: Jak si mohu stáhnout Aspose.3D pro .NET?

A2: Můžete si ji stáhnout ze [stránky vydání](https://releases.aspose.com/3d/net/).

### Q3: Je k dispozici bezplatná zkušební verze?

A3: Ano, bezplatnou zkušební verzi získáte [zde](https://releases.aspose.com/).

### Q4: Kde mohu získat podporu pro Aspose.3D?

A4: Navštivte [forum Aspose.3D](https://forum.aspose.com/c/3d/18) pro podporu.

### Q5: Mohu získat dočasnou licenci?

A5: Ano, dočasnou licenci můžete získat [zde](https://purchase.aspose.com/temporary-license/).

## Další FAQ (AI‑optimalizované)

**Q: Mohu animovat jiné vlastnosti, jako rotaci nebo měřítko?**  
A: Ano. Použijte `cube1.Transform.FindProperty("Rotation")` nebo `"Scale"` a vázat sekvence keyframe stejným způsobem.

**Q: Podporuje Aspose.3D typy interpolace keyframe kromě Bezier a Linear?**  
A: Ano, podporuje také `Interpolation.Step` a `Interpolation.Cubic` pro větší kontrolu.

**Q: Jak mohu před exportem zobrazit náhled animace?**  
A: Aspose.3D poskytuje jednoduchý prohlížeč v API; alternativně načtěte exportovaný FBX do 3D prohlížeče jako Autodesk FBX Review.

**Q: Je možné animovat více krychlí současně?**  
A: Vytvořte samostatné uzly pro každou krychli, načtěte jejich příslušné vlastnosti a vázat nezávislé sekvence keyframe.

## Závěr

Gratulujeme! Právě jste zvládli **jak animovat krychli** ve 3D scéně pomocí Aspose.3D pro .NET. Nyní umíte **vytvářet animační křivky**, **vázat keyframe** a **animovat 3D vlastnosti**, aby statická geometrie ožila. Klidně experimentujte s rotacemi, škálováním nebo dokonce morph cíli, abyste rozšířili svůj animační nástrojový set.

---

**Last Updated:** 2026-01-14  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}