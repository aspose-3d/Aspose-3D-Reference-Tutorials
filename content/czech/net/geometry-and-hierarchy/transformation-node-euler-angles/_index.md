---
title: Transforming Node od Euler Angles ve 3D scénách
linktitle: Transforming Node od Euler Angles ve 3D scénách
second_title: Aspose.3D .NET API
description: Naučte se bez námahy transformovat 3D uzly s Aspose.3D pro .NET. Postupujte podle našeho podrobného průvodce pro ohromující výsledky ve vašich projektech.
type: docs
weight: 19
url: /cs/net/geometry-and-hierarchy/transformation-node-euler-angles/
---
## Úvod

Vítejte v tomto komplexním tutoriálu o transformaci uzlů pomocí Eulerových úhlů ve 3D scénách pomocí Aspose.3D pro .NET. V této příručce se ponoříme do vzrušujícího světa 3D grafiky a prozkoumáme proces přidávání transformací do uzlu pomocí Eulerových úhlů. Aspose.3D for .NET poskytuje výkonné nástroje pro práci s 3D scénami a sítěmi, takže je vynikající volbou pro vývojáře, kteří hledají všestrannost a efektivitu ve svých projektech.

## Předpoklady

Než se pustíme do výukového programu, ujistěte se, že máte splněny následující předpoklady:

-  Aspose.3D for .NET Library: Ujistěte se, že máte nainstalovanou knihovnu Aspose.3D. Můžete si jej stáhnout[tady](https://releases.aspose.com/3d/net/).

- Vývojové prostředí: Nastavte si preferované vývojové prostředí .NET, jako je Visual Studio.

## Importovat jmenné prostory

Začněte importováním potřebných jmenných prostorů pro přístup k funkcím poskytovaným Aspose.3D pro .NET:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

Nyní si příklad rozdělíme do několika kroků pro jasné pochopení.

## Krok 1: Inicializujte objekt scény

```csharp
// ExStart:AddTransformationToNodeByEulerAngles
// Inicializujte objekt scény
Scene scene = new Scene();
```

 Začněte vytvořením nové 3D scény pomocí`Scene` třída.

## Krok 2: Inicializujte objekt třídy uzlu

```csharp
// Inicializujte objekt třídy Node
Node cubeNode = new Node("cube");
```

 Vytvořte uzel ve scéně pomocí`Node`třída. Tento uzel bude sloužit jako kontejner pro náš 3D objekt.

## Krok 3: Vytvořte síť pomocí Polygon Builder

```csharp
// Volejte Common class create mesh pomocí metody polygon builder pro nastavení instance mesh
Mesh mesh = Common.CreateMeshUsingPolygonBuilder(); 
```

 Vyvolejte metodu (v tomto případě`CreateMeshUsingPolygonBuilder` ze zvyku`Common` class) pro vygenerování sítě pro 3D objekt.

## Krok 4: Nasměrujte uzel na geometrii sítě

```csharp
// Bodový uzel ke geometrii sítě
cubeNode.Entity = mesh;
```

Přidružte vytvořenou síť k uzlu.

## Krok 5: Nastavte Eulerovy úhly a překlad

```csharp
// Eulerovy úhly
cubeNode.Transform.EulerAngles = new Vector3(0.3, 0.1, -0.5);            
// Nastavte překlad
cubeNode.Transform.Translation = new Vector3(0, 0, 20);
```

Definujte Eulerovy úhly a posun pro uzel, abyste jej umístili do 3D prostoru.

## Krok 6: Přidejte kostku do scény

```csharp
// Přidejte kostku na scénu
scene.RootNode.ChildNodes.Add(cubeNode);
```

Začlenit uzel do hierarchie scény.

## Krok 7: Uložte 3D scénu

```csharp
// Cesta k adresáři dokumentů.
var output = "Your Output Directory" + "TransformationToNode.fbx";

//Uložte 3D scénu v podporovaných formátech souborů
scene.Save(output, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByEulerAngles
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

Určete výstupní adresář a uložte 3D scénu, včetně transformovaného uzlu, v požadovaném formátu souboru (v tomto případě FBX7500ASCII).

## Závěr

Gratulujeme! Úspěšně jste se naučili, jak transformovat uzel pomocí Eulerových úhlů ve 3D scénách pomocí Aspose.3D pro .NET. Tato výkonná knihovna otevírá dveře nekonečným možnostem vývoje 3D grafiky.

## FAQ

### Q1: Je Aspose.3D kompatibilní s jinými nástroji pro 3D modelování?

Odpověď 1: Aspose.3D podporuje různé formáty 3D souborů, což zvyšuje kompatibilitu s oblíbenými modelovacími nástroji.

### Q2: Mohu použít více transformací na jeden uzel?

A2: Ano, můžete kombinovat a použít více transformací k dosažení komplexních efektů.

### Q3: Kde najdu další dokumentaci Aspose.3D?

 A3: Viz[dokumentace](https://reference.aspose.com/3d/net/) pro podrobné informace a příklady.

### Q4: Potřebuji licenci pro používání Aspose.3D pro .NET?

 A4: Ano, můžete získat licenci[tady](https://purchase.aspose.com/buy) nebo prozkoumat a[zkušební verze zdarma](https://releases.aspose.com/).

### Q5: Potřebujete pomoc nebo máte konkrétní otázky?

A5: Navštivte[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) za podporu komunity.