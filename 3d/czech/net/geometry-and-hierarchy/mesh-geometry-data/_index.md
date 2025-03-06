---
title: Práce s daty geometrie sítě
linktitle: Práce s daty geometrie sítě
second_title: Aspose.3D .NET API
description: Ovládněte umění programování 3D grafiky s Aspose.3D pro .NET. Vytvářejte, manipulujte a ukládejte úžasné 3D scény bez námahy.
weight: 15
url: /cs/net/geometry-and-hierarchy/mesh-geometry-data/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Práce s daty geometrie sítě

## Úvod

Vítejte ve vzrušujícím světě programování 3D grafiky s Aspose.3D pro .NET! V tomto tutoriálu se ponoříme do složitosti práce s Mesh Geometry Data ve 3D scénách pomocí Aspose.3D, výkonné a všestranné knihovny pro vývojáře .NET. Ať už jste zkušený programátor nebo s 3D grafikou teprve začínáte, tento podrobný průvodce vám pomůže zvládnout umění manipulace s daty geometrie sítě bez námahy.

## Předpoklady

Než se vydáme na tuto 3D cestu, ujistěte se, že máte splněny následující předpoklady:

- Pracovní znalost programování C# a .NET.
- Visual Studio nainstalované na vašem počítači.
- Aspose.3D for .NET knihovna, kterou si můžete stáhnout[tady](https://releases.aspose.com/3d/net/).

Nyní, když je vše připraveno, pojďme skočit do fascinujícího světa programování 3D grafiky!

## Importovat jmenné prostory

Ve svém projektu C# začněte importováním potřebných jmenných prostorů:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose.ThreeD.Shading;
```

Tyto jmenné prostory poskytují přístup k základním třídám a metodám potřebným pro práci s 3D scénami a daty geometrie sítě.

## Krok 1: Inicializujte scénu

```csharp
// Inicializujte objekt scény
Scene scene = new Scene();
```

Tím se vytvoří prázdná 3D scéna, kde můžete vytvářet a manipulovat s 3D modely.

## Krok 2: Definujte barevné vektory

```csharp
// Definujte barevné vektory
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

Určete pole barevných vektorů, které budou aplikovány na různé části vaší 3D scény.

## Krok 3: Vytvořte síť a nastavte barvy

```csharp
// Volejte Common class create mesh pomocí metody polygon builder pro nastavení instance mesh
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();

int idx = 0;
foreach (Vector3 color in colors)
{
    // Inicializujte objekt uzlu krychle
    Node cube = new Node("cube");
    cube.Entity = mesh;
    LambertMaterial mat = new LambertMaterial();
    
    // Nastavit barvu
    mat.DiffuseColor = color;
    
    // Nastavit materiál
    cube.Material = mat;
    
    // Nastavte překlad
    cube.Transform.Translation = new Vector3(idx++ * 20, 0, 0);
    
    // Přidat uzel krychle
    scene.RootNode.ChildNodes.Add(cube);
}
```

Vytvořte síť pomocí metody polygon builder a aplikujte barvy na různé části scény.

## Krok 4: Uložte 3D scénu

```csharp
// Cesta k adresáři dokumentů.
var output = "Your Output Directory" + "MeshGeometryData.fbx";

// Uložte 3D scénu v podporovaných formátech souborů
scene.Save(output, FileFormat.FBX7400ASCII);
```

Zadejte výstupní adresář a uložte svou 3D scénu ve formátu souboru FBX7400ASCII.

## Závěr

Gratulujeme! Úspěšně jste se naučili pracovat s daty geometrie sítě ve 3D scénách pomocí Aspose.3D for .NET. Tento tutoriál vás vybavil základními kroky k vytváření a manipulaci s 3D modely. Experimentujte, prozkoumávejte a posuňte své znalosti programování 3D grafiky do nových výšin!

## FAQ

### Q1: Mohu používat Aspose.3D pro .NET s jinými programovacími jazyky?

Odpověď 1: Aspose.3D je primárně navržen pro .NET, ale můžete prozkoumat další produkty Aspose, které podporují různé platformy a jazyky.

### Q2: Je k dispozici bezplatná zkušební verze pro Aspose.3D?

 A2: Ano, máte přístup k bezplatné zkušební verzi[tady](https://releases.aspose.com/).

### Q3: Kde najdu další podporu a zdroje?

 A3: Navštivte[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) za podporu komunity a diskuze.

### Q4: Jak získám dočasnou licenci pro Aspose.3D?

 A4: Můžete získat dočasnou licenci[tady](https://purchase.aspose.com/temporary-license/).

### Q5: Jaké formáty souborů jsou podporovány pro ukládání 3D scén?

 A5: Aspose.3D podporuje různé formáty souborů, včetně FBX, STL a dalších. Odkazovat na[dokumentace](https://reference.aspose.com/3d/net/) pro úplný seznam.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
