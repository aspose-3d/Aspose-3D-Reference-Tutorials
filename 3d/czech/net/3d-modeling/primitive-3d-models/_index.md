---
date: 2026-03-26
description: Naučte se, jak vytvořit 3D modely krabice a válce a uložit scénu jako
  FBX pomocí Aspose.3D pro .NET.
linktitle: Create 3D Box and Cylinder Models with Aspose.3D for .NET
second_title: Aspose.3D .NET API
title: Vytvořte 3D modely krabice a válce pomocí Aspose.3D pro .NET
url: /cs/net/3d-modeling/primitive-3d-models/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Vytvořte 3D modely krabice a válce pomocí Aspose.3D

## Úvod

Vítejte ve vzrušujícím světě 3D modelování s Aspose.3D pro .NET! V tomto tutoriálu se naučíte **jak vytvořit 3d krabici** primitivy, přidat válec a exportovat celou scénu do FBX. Ať už stavíte rychlý prototyp nebo produkčně připravený pipeline aktiv, tyto kroky vám poskytnou pevný základ pro práci s 3D geometrií v .NET.

## Rychlé odpovědi
- **Co tento tutoriál pokrývá?** Vytvoření 3D krabice, 3D válce a uložení scény jako FBX souboru.  
- **Která knihovna je vyžadována?** Aspose.3D pro .NET (stáhněte z oficiálního webu).  
- **Jak dlouho trvá implementace?** Přibližně 10‑15 minut pro základní scénu.  
- **Mohu přizpůsobit rozměry?** Ano – konstruktory Box a Cylinder přijímají parametry velikosti.  
- **Je pro produkci potřeba licence?** Platná licence Aspose.3D je vyžadována pro ne‑zkušební verze.

## Co je „vytvořit 3d krabici“?

Vytvoření 3D krabice znamená vygenerování jednoduchého krychle nebo pravoúhlého hranolu, který může sloužit jako stavební blok pro složitější modely. V Aspose.3D třída `Box` představuje tento primitiv a můžete jej přidat do scény jediným řádkem kódu.

## Proč použít Aspose.3D pro tento úkol?

- **Čisté .NET API:** Žádné nativní závislosti, ideální pro projekty v C# a VB.NET.  
- **Široká podpora formátů:** Export do FBX, OBJ, STL a mnoha dalších.  
- **Vysoce‑úrovňové primitivy:** Box, Cylinder, Sphere atd., umožňují soustředit se na logiku místo na nízkoúrovňovou konstrukci mesh.  
- **Optimalizováno pro výkon:** Efektivně zpracovává velké scény.

## Požadavky

Než se pustíme dál, ujistěte se, že máte:

- Aspose.3D pro .NET: Stáhněte a nainstalujte knihovnu z [download link](https://releases.aspose.com/3d/net/).  
- Vývojové prostředí .NET (Visual Studio, Rider nebo VS Code) kompatibilní s verzí Aspose.3D, kterou jste nainstalovali.

Nyní, když máte vše potřebné, začněme krok za krokem budovat scénu.

## Importujte jmenné prostory

Začněte importováním potřebných jmenných prostorů pro přístup k funkcionalitě poskytované Aspose.3D:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```

S těmito jmennými prostory jste připraveni uvolnit sílu Aspose.3D ve vaší .NET aplikaci.

## Krok 1: Inicializujte objekt Scene

```csharp
// Initialize a Scene object
Scene scene = new Scene();
```

Objekt `Scene` funguje jako plátno, kde budou žít všechny 3D entity.

## Krok 2: Vytvořte model krabice

```csharp
// Create a Box model
scene.RootNode.CreateChildNode("box", new Box());
```

Tento řádek přidá **3D krabici** primitivum do kořene vaší scény. Později můžete upravit její šířku, výšku a hloubku předáním parametrů do konstruktoru `Box`.

## Krok 3: Vytvořte model válce

```csharp
// Create a Cylinder model
scene.RootNode.CreateChildNode("cylinder", new Cylinder());
```

Válec doplňuje krabici a ukazuje, jak snadné je kombinovat různé primitivy.

## Krok 4: Uložte výkres ve formátu FBX

```csharp
// Save drawing in the FBX format
var output = "Your Output Directory" + "test.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Zde **převádíme model do FBX** uložením celé scény jako FBX souboru. Klidně změňte cestu a název souboru podle struktury vašeho projektu.

## Krok 5: Zobrazte zprávu o úspěchu

```csharp
// Display success message
Console.WriteLine("\nBuilding a scene from primitive 3D models successfully.\nFile saved at " + output);
```

Přátelská zpráva v konzoli potvrzuje, že operace **build 3d scene** byla dokončena bez chyb.

## Časté problémy a tipy

- **Výstupní adresář neexistuje:** Ujistěte se, že složka v `output` existuje, nebo před uložením použijte `Directory.CreateDirectory()`.  
- **Licence není nastavena:** V ne‑zkušební verzi zavolejte `License license = new License(); license.SetLicense("Aspose.3D.lic");` před vytvořením `Scene`.  
- **Vlastní rozměry:** Použijte `new Box(width, height, depth)` nebo `new Cylinder(radius, height)` pro nastavení velikosti.

## Závěr

Gratulujeme! Úspěšně jste **vytvořili 3d krabici** a válec jako primitiva, postavili jednoduchou scénu a uložili ji jako FBX soubor pomocí Aspose.3D pro .NET. Základy jsou nyní ve vašem nářadí a můžete prozkoumat [documentation](https://reference.aspose.com/3d/net/) pro pokročilejší funkce jako materiály, osvětlení a animace.

## Často kladené otázky

### Q1: Mohu použít Aspose.3D pro .NET s jinými programovacími jazyky?
A1: Aspose.3D primárně podporuje .NET, ale jsou k dispozici i jiné verze pro Javu a další platformy.

### Q2: Je k dispozici bezplatná zkušební verze?
A2: Ano, můžete prozkoumat možnosti Aspose.3D pomocí [free trial](https://releases.aspose.com/).

### Q3: Kde mohu najít podporu pro Aspose.3D pro .NET?
A3: Navštivte [Aspose.3D forum](https://forum.aspose.com/c/3d/18) pro komunitní podporu a diskuze.

### Q4: Jak mohu získat dočasnou licenci?
A4: Dočasnou licenci můžete získat [here](https://purchase.aspose.com/temporary-license/).

### Q5: Existují nějaké ukázkové tutoriály?
A5: Ano, prozkoumejte další tutoriály a příklady v [documentation](https://reference.aspose.com/3d/net/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Poslední aktualizace:** 2026-03-26  
**Testováno s:** Aspose.3D 24.11 for .NET  
**Autor:** Aspose