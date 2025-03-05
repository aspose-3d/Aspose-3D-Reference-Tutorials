---
title: Vytvoření prázdného 3D dokumentu
linktitle: Vytvoření prázdného 3D dokumentu
second_title: Aspose.3D .NET API
description: Prozkoumejte svět tvorby 3D dokumentů s Aspose.3D pro .NET. Vytvářejte, upravujte a ukládejte úžasné 3D scény bez námahy.
type: docs
weight: 11
url: /cs/net/loading-and-saving/create-empty-3d-document/
---
## Úvod

Vítejte ve světě tvorby 3D dokumentů pomocí Aspose.3D pro .NET! V tomto tutoriálu prozkoumáme základy načítání a ukládání 3D dokumentů. Aspose.3D for .NET poskytuje výkonnou sadu nástrojů pro práci s 3D scénami a my vás provedeme každým krokem, který vám pomůže hladce začít.

## Předpoklady

Než se pustíme do výukového programu, ujistěte se, že máte splněny následující předpoklady:

-  Aspose.3D for .NET: Ujistěte se, že máte nainstalovanou knihovnu. Můžete si jej stáhnout z[tady](https://releases.aspose.com/3d/net/).

## Importovat jmenné prostory

Chcete-li začít, importujte potřebné jmenné prostory do svého projektu .NET:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## Načítání a ukládání – vytvoření prázdného 3D dokumentu

### Krok 1: Nastavte svůj výstupní adresář

```csharp
// Cesta k adresáři dokumentů.
var output = "Your Output Directory" + "document.fbx";
```

### Krok 2: Vytvořte prázdný 3D dokument

```csharp
// ExStart:CreateEmpty3DDocument

// Vytvořte objekt třídy Scene
Scene scene = new Scene();

// Uložte dokument 3D scény ve formátu FBX
scene.Save(output);

// ExEnd:CreateEmpty3DDocument
```

### Krok 3: Zobrazte výsledek

```csharp
Console.WriteLine("\nAn empty 3D document created successfully.\nFile saved at " + output);
```

Gratulujeme! Právě jste vytvořili svůj první prázdný 3D dokument pomocí Aspose.3D for .NET. Neváhejte a prozkoumejte další funkce a funkce, abyste mohli naplno využít potenciál této knihovny.

## Závěr

 V tomto tutoriálu jsme probrali základy vytváření prázdného 3D dokumentu pomocí Aspose.3D for .NET. Jak budete pokračovat ve své cestě s 3D vývojem, podívejte se na[dokumentace](https://reference.aspose.com/3d/net/) pro podrobné informace a pokročilé funkce.

## FAQ

### Q1: Je Aspose.3D for .NET vhodný pro začátečníky?

Odpověď 1: Ano, Aspose.3D for .NET poskytuje uživatelsky přívětivé rozhraní, díky kterému je přístupné začátečníkům i zkušeným vývojářům.

### Q2: Mohu vyzkoušet Aspose.3D pro .NET před nákupem?

 A2: Rozhodně! Máte přístup k bezplatné zkušební verzi[tady](https://releases.aspose.com/).

### Q3: Jak mohu získat podporu pro Aspose.3D pro .NET?

 A3: Navštivte[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) vyhledat pomoc a spojit se s komunitou.

### Q4: Jsou k dispozici dočasné licence pro Aspose.3D pro .NET?

 A4: Ano, můžete získat dočasnou licenci[tady](https://purchase.aspose.com/temporary-license/).

### Q5: Kde mohu zakoupit Aspose.3D pro .NET?

 A5: Můžete si koupit knihovnu[tady](https://purchase.aspose.com/buy).