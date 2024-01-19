---
title: Transforming Node pomocí Transformation Matrix ve 3D scénách
linktitle: Transforming Node pomocí Transformation Matrix ve 3D scénách
second_title: Aspose.3D .NET API
description: Transformujte uzly bez námahy ve 3D scénách pomocí Aspose.3D for .NET. Naučte se krok za krokem transformace uzlů pomocí kurzu.
type: docs
weight: 21
url: /cs/net/geometry-and-hierarchy/transformation-node-matrix/
---
## Úvod

V dynamické oblasti 3D grafiky a vizualizací je schopnost manipulovat s objekty ve scéně zásadním aspektem. Aspose.3D for .NET umožňuje vývojářům bezproblémově transformovat uzly pomocí transformačních matic, čímž přidává vrstvu kreativity a kontroly do 3D scén. Tento tutoriál vás krok za krokem provede procesem transformace uzlu ve 3D scéně.

## Předpoklady

Než se pustíte do výukového programu, ujistěte se, že máte splněny následující předpoklady:

1.  Knihovna Aspose.3D for .NET: Ujistěte se, že máte ve svém projektu .NET nainstalovanou knihovnu Aspose.3D. Můžete si jej stáhnout[tady](https://releases.aspose.com/3d/net/).

2. Vývojové prostředí: Nastavte funkční vývojové prostředí .NET, a pokud jste tak ještě neučinili, vytvořte nový projekt, ve kterém budete implementovat transformace.

## Importovat jmenné prostory

Začněte importováním potřebných jmenných prostorů do vašeho projektu .NET. Tyto jmenné prostory poskytují základní třídy a metody pro manipulaci s 3D scénou.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

Nyní, když jsme probrali základy, pojďme si rozdělit proces transformace na průvodce krok za krokem.

## Krok 1: Inicializujte scénu a uzel

```csharp
// ExStart:AddTransformationToNodeByTransformationMatrix
// Inicializujte objekt scény
Scene scene = new Scene();

// Inicializujte objekt třídy Node
Node cubeNode = new Node("cube");
```

V tomto kroku vytvoříme novou 3D scénu a uzel pojmenovaný „kostka“ v rámci této scény.

## Krok 2: Vytvořte síť a nastavte geometrii

```csharp
// Volejte Common class create mesh pomocí metody polygon builder pro nastavení instance mesh
Mesh mesh = Common.CreateMeshUsingPolygonBuilder(); 

// Bodový uzel ke geometrii sítě
cubeNode.Entity = mesh;
```

Zde vygenerujeme síť pomocí metody polygon builder a přiřadíme ji k uzlu, čímž vytvoříme geometrii pro naši krychli.

## Krok 3: Nastavte vlastní matici překladu

```csharp
// Nastavit vlastní překladovou matici
cubeNode.Transform.TransformMatrix = new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
);        
```

Definujte vlastní matici překladu, abyste určili konkrétní transformaci použitou na uzel. Upravte hodnoty matice podle potřeby pro požadovanou transformaci.

## Krok 4: Přidejte uzel do scény

```csharp
// Přidejte kostku na scénu
scene.RootNode.ChildNodes.Add(cubeNode);            
```

Zahrňte uzel krychle do scény, čímž se stane součástí celkového 3D prostředí.

## Krok 5: Uložte scénu

```csharp
// Cesta k adresáři dokumentů.
var output = "Your Output Directory" + "TransformationToNode.fbx";

//Uložte 3D scénu v podporovaných formátech souborů
scene.Save(output, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByTransformationMatrix
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

Zadejte výstupní adresář a název souboru a poté uložte 3D scénu v požadovaném formátu souboru. V tomto příkladu jej ukládáme ve formátu FBX7500ASCII.

## Závěr

Gratulujeme! Úspěšně jste transformovali uzel pomocí transformační matice ve 3D scéně pomocí Aspose.3D for .NET. Tato schopnost otevírá dveře různým a vizuálně podmanivým 3D aplikacím.

## FAQ

### Q1: Co je to transformační matice ve 3D grafice?

A1: Transformační matice je matematická reprezentace používaná k aplikaci různých transformací (posun, rotace, změna měřítka) na objekty ve 3D prostoru.

### Q2: Mohu použít více transformací na jeden uzel?

Odpověď 2: Ano, můžete kombinovat více transformací vynásobením jejich příslušných matic a použitím výsledku na uzel.

### Otázka 3: Existují další podporované formáty souborů pro ukládání 3D scén?

 Odpověď 3: Aspose.3D for .NET podporuje různé formáty souborů, včetně STL, GLTF, OBJ a dalších. Odkazovat na[dokumentace](https://reference.aspose.com/3d/net/) pro úplný seznam.

### Q4: Jak mohu získat dočasnou licenci pro Aspose.3D for .NET?

 A4: Navštivte[dočasná licenční stránka](https://purchase.aspose.com/temporary-license/) na webu Aspose k získání dočasné licence pro účely hodnocení.

### Otázka 5: Kde mohu vyhledat pomoc nebo se spojit s komunitou Aspose.3D?

A5: Navštivte[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) klást otázky, sdílet zkušenosti a spojit se s ostatními vývojáři pomocí Aspose.3D.