---
title: Vytváření primitivních 3D modelů
linktitle: Vytváření primitivních 3D modelů
second_title: Aspose.3D .NET API
description: Prozkoumejte svět 3D modelování s Aspose.3D pro .NET. Vytvářejte úžasné primitivní modely bez námahy.
type: docs
weight: 10
url: /cs/net/3d-modeling/primitive-3d-models/
---
## Úvod

Vítejte ve vzrušujícím světě 3D modelování s Aspose.3D pro .NET! V tomto komplexním tutoriálu prozkoumáme proces vytváření primitivních 3D modelů pomocí Aspose.3D krok za krokem. Ať už jste zkušený vývojář nebo zvědavý začátečník, tato příručka vám pomůže využít sílu Aspose.3D k vytvoření vizuálně úžasných 3D prvků pro vaše projekty.

## Předpoklady

Než se ponoříme do fascinující sféry 3D modelování, ujistěte se, že máte splněny následující předpoklady:

-  Aspose.3D for .NET: Stáhněte si a nainstalujte knihovnu Aspose.3D for .NET z[odkaz ke stažení](https://releases.aspose.com/3d/net/).

- Vývojové prostředí: Nastavte vývojové prostředí .NET zajišťující kompatibilitu s Aspose.3D.

Nyní, když máte to podstatné, pojďme se vydat na cestu vytváření primitivních 3D modelů krok za krokem.

## Importovat jmenné prostory

Začněte importem potřebných jmenných prostorů pro přístup k funkcím poskytovaným Aspose.3D:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```

těmito jmennými prostory na místě jste připraveni uvolnit sílu Aspose.3D ve vaší aplikaci .NET.

## Krok 1: Inicializujte objekt scény

```csharp
//Inicializujte objekt Scene
Scene scene = new Scene();
```

Vytvořte nový objekt scény, který slouží jako plátno pro vaše 3D mistrovské dílo.

## Krok 2: Vytvořte krabicový model

```csharp
// Vytvořte model krabice
scene.RootNode.CreateChildNode("box", new Box());
```

Přidejte krabicový model do kořene vaší scény. Přizpůsobte si rozměry a vlastnosti krabice podle své kreativní vize.

## Krok 3: Vytvořte model válce

```csharp
// Vytvořte model válce
scene.RootNode.CreateChildNode("cylinder", new Cylinder());
```

Vylepšete svou scénu představením modelu válce. Upravte jeho parametry, abyste dosáhli požadovaného tvaru a velikosti.

## Krok 4: Uložte výkres ve formátu FBX

```csharp
// Uložte výkres ve formátu FBX
var output = "Your Output Directory" + "test.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Uložte své 3D mistrovské dílo ve formátu FBX. Vyberte vhodný výstupní adresář a název souboru pro vaši tvorbu.

## Krok 5: Zobrazte zprávu o úspěchu

```csharp
// Zobrazit zprávu o úspěchu
Console.WriteLine("\nBuilding a scene from primitive 3D models successfully.\nFile saved at " + output);
```

Oslavte svůj úspěch! Scéna je úspěšně sestavena z primitivních 3D modelů a soubor je uložen.

## Závěr

 Gratulujeme! Úspěšně jste vytvořili úžasné 3D modely pomocí Aspose.3D pro .NET. Tato příručka pokrývá základy, ale možnosti jsou neomezené. Prozkoumat[dokumentace](https://reference.aspose.com/3d/net/) pro pokročilejší funkce a techniky.

## FAQ

### Q1: Mohu používat Aspose.3D pro .NET s jinými programovacími jazyky?

A1: Aspose.3D primárně podporuje .NET, ale jsou k dispozici i další verze pro Javu a další platformy.

### Q2: Je k dispozici bezplatná zkušební verze?

 A2: Ano, můžete prozkoumat možnosti Aspose.3D pomocí a[zkušební verze zdarma](https://releases.aspose.com/).

### Q3: Kde najdu podporu pro Aspose.3D pro .NET?

 A3: Navštivte[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) za podporu komunity a diskuze.

### Q4: Jak mohu získat dočasnou licenci?

 A4: Můžete získat dočasnou licenci[tady](https://purchase.aspose.com/temporary-license/).

### Q5: Jsou k dispozici nějaké ukázkové tutoriály?

 A5: Ano, prozkoumejte další návody a příklady v[dokumentace](https://reference.aspose.com/3d/net/).