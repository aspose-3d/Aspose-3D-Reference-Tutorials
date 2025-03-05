---
title: Vytváření krychlových scén
linktitle: Vytváření krychlových scén
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET bez námahy vytvářejte úžasné 3D scény z kostek. Stáhněte si knihovnu, postupujte podle našeho podrobného průvodce a uvolněte.
type: docs
weight: 12
url: /cs/net/geometry-and-hierarchy/create-cube-scenes/
---
## Úvod

Jste připraveni ponořit se do podmanivého světa 3D designu? V tomto tutoriálu vás provedeme procesem vytváření fascinujících scén s krychlí pomocí Aspose.3D pro .NET. Aspose.3D je výkonná a všestranná knihovna, která umožňuje vývojářům bezproblémově vytvářet pohlcující 3D zážitky.

## Předpoklady

Než se vydáme na tuto kreativní cestu, ujistěte se, že máte vše, co potřebujete:

1.  Aspose.3D for .NET Library: Stáhněte a nainstalujte knihovnu z[Založte dokumentaci](https://reference.aspose.com/3d/net/).

2. Vývojové prostředí: Nastavte si preferované vývojové prostředí .NET.

3. Základní znalost C#: Tento tutoriál předpokládá, že máte základní znalosti o programování v C#.

## Importovat jmenné prostory

Nyní začněme tím, že importujeme potřebné jmenné prostory do vašeho kódu C#:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
```

## Krok 1: Inicializujte scénu

Začněte vytvořením nové 3D scény:

```csharp
// ExStart:CreateCubeScene
// Inicializujte objekt scény
Scene scene = new Scene();
```

## Krok 2: Vytvořte uzel pro krychli

Nyní přidejte uzel, který bude reprezentovat naši krychli ve scéně:

```csharp
// Inicializujte objekt třídy Node
Node cubeNode = new Node("cube");
```

## Krok 3: Vytvořte síť

Použijte třídu Common k vytvoření sítě pro vaši krychli pomocí metody polygon builder:

```csharp
// Volejte Common class create mesh pomocí metody polygon builder pro nastavení instance mesh
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## Krok 4: Nasměrujte uzel na geometrii sítě

Přidružte geometrii sítě k uzlu krychle:

```csharp
// Bodový uzel ke geometrii sítě
cubeNode.Entity = mesh;
```

## Krok 5: Přidejte uzel do scény

Umístěte uzel krychle do kořenových uzlů scény:

```csharp
// Přidejte uzel do scény
scene.RootNode.ChildNodes.Add(cubeNode);
```

## Krok 6: Uložte 3D scénu

Zadejte výstupní adresář a uložte 3D scénu v podporovaném formátu souboru (v tomto případě FBX):

```csharp
// Cesta k adresáři dokumentů.
var output = "Your Output Directory" + "CubeScene.fbx";

// Uložte 3D scénu v podporovaných formátech souborů
scene.Save(output, FileFormat.FBX7400ASCII);
```

## Krok 7: Zobrazte zprávu o úspěchu

Informujte uživatele, že scéna krychle byla úspěšně vytvořena:

```csharp
Console.WriteLine("\nCube Scene created successfully.\nFile saved at " + output);
```

Gratulujeme! Právě jste vytvořili svou první 3D scénu krychle pomocí Aspose.3D pro .NET. Experimentujte s různými tvary, texturami a osvětlením, abyste odemkli říši možností.

## Závěr

tomto tutoriálu jsme prozkoumali proces vytváření úchvatných 3D scén v kostce pomocí Aspose.3D pro .NET. Nyní, vyzbrojeni těmito znalostmi, můžete popustit uzdu své kreativitě a přivést své 3D vize k životu.

## FAQ

### Q1: Je Aspose.3D kompatibilní s různými formáty 3D souborů?

Odpověď 1: Ano, Aspose.3D podporuje různé formáty souborů, včetně FBX, STL a dalších.

### Q2: Mohu přizpůsobit vzhled krychle?

A2: Rozhodně! Experimentujte s materiály, barvami a texturami, abyste dosáhli požadovaného vzhledu.

### Q3: Kde najdu další podporu a zdroje?

 A3: Navštivte[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) za komunitní pomoc a diskuse.

### Q4: Je k dispozici bezplatná zkušební verze?

 A4: Ano, můžete prozkoumat bezplatnou zkušební verzi[tady](https://releases.aspose.com/).

### Q5: Jak mohu získat dočasnou licenci pro Aspose.3D?

 A5: Získejte dočasnou licenci[tady](https://purchase.aspose.com/temporary-license/).