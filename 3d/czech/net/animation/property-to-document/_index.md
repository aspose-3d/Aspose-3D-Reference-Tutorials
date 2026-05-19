---
date: 2026-03-28
description: Naučte se animovat krychli ve 3D scénách pomocí Aspose.3D pro .NET a
  exportovat animovanou scénu do formátu FBX. Tento průvodce ukazuje, jak vytvořit
  animační křivku, svázat klíčové snímky a animovat 3D vlastnosti.
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

Pokud se ponořujete do oblasti tvorby a animace 3D scén v .NET, Aspose.3D je vaším nástrojem první volby. V tomto krok‑za‑krokem průvodci prozkoumáme **jak animovat krychli** objektů animací jejich vlastností, vytvářením animačních křivek a svázáním klíčových snímků. Na konci budete mít plně animovanou krychli, kterou můžete exportovat do populárních 3D formátů.

## Rychlé odpovědi
- **Jaká knihovna se používá?** Aspose.3D pro .NET  
- **Jaký hlavní úkol tento tutoriál pokrývá?** Jak animovat krychli ve 3D scéně  
- **Klíčové kroky?** Importovat jmenné prostory, vytvořit scénu, svázat klíčové snímky, uložit soubor  
- **Potřebuji licenci?** Bezplatná zkušební verze stačí pro učení; komerční licence je vyžadována pro produkci  
- **Podporovaný výstupní formát?** FBX (ASCII 7500) a další podporované Aspose.3D  

## Co znamená „jak animovat krychli“ v Aspose.3D?

Animace krychle znamená měnit její transformační vlastnosti (jako Translaci, Rotaci nebo Škálování) v průběhu času pomocí dat klíčových snímků. Aspose.3D poskytuje čisté API pro vytváření **animačních křivek**, **svázání klíčových snímků** a **animaci 3D vlastností** přímo na uzlech scény.

## Proč animovat krychli pomocí Aspose.3D?

- **Plná integrace s .NET** – funguje s .NET Framework, .NET Core a .NET 5/6.  
- **Žádné externí závislosti** – není potřeba Unity ani jiné enginy pro jednoduché animace.  
- **Flexibilita exportu** – animované scény lze uložit jako FBX, OBJ, GLTF atd., pro následné pipeline.  

## Prerequisites

Než se vydáme na tuto vzrušující cestu, ujistěte se, že máte následující předpoklady připravené:

- Aspose.3D pro .NET: Ujistěte se, že máte knihovnu nainstalovanou. Můžete ji stáhnout z [webu Aspose.3D](https://releases.aspose.com/3d/net/).
- Znalost C#: Znalost programovacího jazyka C# je nezbytná pro pochopení a implementaci příkladů.
- Integrované vývojové prostředí (IDE): Použijte své oblíbené IDE, například Visual Studio, pro psaní kódu spolu s příklady.
- Základní koncepty 3D scény: Pochopení základních konceptů 3D scény usnadní vaši učební cestu.

## Import jmenných prostorů

Ve vašem C# kódu se ujistěte, že importujete potřebné jmenné prostory pro Aspose.3D. Zde je požadovaná sada:

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

## Krok 2: Vytvoření meshe pomocí Polygon Builderu

Vygenerujeme jednoduchý mesh krychle pomocí pomocné metody `Common.CreateMeshUsingPolygonBuilder()`.

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## Krok 3: Vytvoření uzlů krychle

Přidejte mesh krychle do scény jako podřízený uzel kořene. Název uzlu **cube1** bude později použit při svázání klíčových snímků.

```csharp
Node cube1 = scene.RootNode.CreateChildNode("cube1", mesh);
```

## Krok 4: Najděte vlastnost Translace

Pro animaci pozice krychle musíme najít její **Translation** vlastnost v transformaci uzlu.

```csharp
Property translation = cube1.Transform.FindProperty("Translation");
```

## Krok 5: Vytvoření Bind Pointu

`BindPoint` spojuje vlastnost scény s animační křivkou. Zde svazujeme vlastnost translace.

```csharp
BindPoint bindPoint = new BindPoint(scene, translation);
```

## Krok 6: Svázání animační křivky na komponentě X

Nyní vytvoříme animační křivku pro osu **X**. Toto demonstruje krok **vytvořit animační křivku** a ukazuje, jak **svázat klíčové snímky**.

```csharp
bindPoint.BindKeyframeSequence("X", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, 20.0f, Interpolation.Bezier},
    {5, 30.0f, Interpolation.Linear},
});
```

## Krok 7: Svázání animační křivky na komponentě Z

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

## Krok 9: Zobrazení úspěšné zprávy

Dejte uživateli zpětnou vazbu, že animace byla úspěšně přidána.

```csharp
Console.WriteLine("\nAnimation property added successfully to document.\nFile saved at " + output);
```

## Export animované scény do FBX

Jedním z nejčastějších úkolů po animaci krychle je **exportovat animovanou scénu do FBX**, aby ji mohly využívat další 3D aplikace. Výše uvedený kód již ukládá scénu ve formátu FBX7500ASCII, který zachovává data klíčových snímků a funguje bez problémů s nástroji jako Autodesk Maya, Blender a Unity. Když otevřete výsledný soubor `.fbx`, měli byste vidět krychli pohybující se podél os X a Z přesně podle definovaných sekvencí klíčových snímků.

## Časté problémy a řešení

| Problém | Důvod | Řešení |
|-------|--------|-----|
| Žádný pohyb pozorován | Časy klíčových snímků neodpovídají rozsahu přehrávání | Ujistěte se, že časová osa animace scény zahrnuje časy klíčových snímků (0‑5 sekund v tomto příkladu). |
| Nesprávná cesta k souboru | `output` ukazuje na neexistující adresář | Nejprve vytvořte adresář nebo použijte absolutní cestu. |
| Výjimka licence | Spuštění bez platné licence v produkci | Aplikujte svou licenci Aspose.3D před vytvořením objektu `Scene`. |

## Často kladené otázky

### Q1: Kde mohu najít dokumentaci k Aspose.3D?

A1: Dokumentace je k dispozici [zde](https://reference.aspose.com/3d/net/).

### Q2: Jak si mohu stáhnout Aspose.3D pro .NET?

A2: Můžete si ji stáhnout ze [stránky vydání](https://releases.aspose.com/3d/net/).

### Q3: Je k dispozici bezplatná zkušební verze?

A3: Ano, můžete získat bezplatnou zkušební verzi [zde](https://releases.aspose.com/).

### Q4: Kde mohu získat podporu pro Aspose.3D?

A4: Navštivte [forum Aspose.3D](https://forum.aspose.com/c/3d/18) pro podporu.

### Q5: Mohu získat dočasnou licenci?

A5: Ano, můžete získat dočasnou licenci [zde](https://purchase.aspose.com/temporary-license/).

## Další FAQ (AI‑optimalizováno)

**Q: Mohu animovat jiné vlastnosti, jako rotaci nebo škálování?**  
A: Ano. Použijte `cube1.Transform.FindProperty("Rotation")` nebo `"Scale"` a svazujte sekvence klíčových snímků stejným způsobem.

**Q: Podporuje Aspose.3D typy interpolace klíčových snímků jiných než Bezier a Linear?**  
A: Ano, podporuje také `Interpolation.Step` a `Interpolation.Cubic` pro větší kontrolu.

**Q: Jak mohu před exportem zobrazit náhled animace?**  
A: Aspose.3D poskytuje jednoduchý prohlížeč v API; alternativně načtěte exportovaný FBX do 3D prohlížeče jako Autodesk FBX Review.

**Q: Je možné animovat více krychlí současně?**  
A: Vytvořte samostatné uzly pro každou krychli, načtěte jejich příslušné vlastnosti a svazujte nezávislé sekvence klíčových snímků.

## Závěr

Gratulujeme! Právě jste zvládli **jak animovat krychli** ve 3D scéně pomocí Aspose.3D pro .NET. Nyní víte, jak **vytvořit animační křivky**, **svázat klíčové snímky** a **exportovat animovanou scénu do FBX**, aby se statická geometrie oživila. Neváhejte experimentovat s rotacemi, škálováním nebo dokonce s morph cíli, abyste rozšířili svou sadu nástrojů pro animaci.

---

**Last Updated:** 2026-03-28  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}