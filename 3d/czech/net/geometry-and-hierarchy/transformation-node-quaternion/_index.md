---
title: Transforming Node by Quaternion
linktitle: Transforming Node by Quaternion
second_title: Aspose.3D .NET API
description: Naučte se transformovat 3D uzly pomocí čtveřice pomocí Aspose.3D for .NET. Průvodce krok za krokem pro začátečníky.
weight: 20
url: /cs/net/geometry-and-hierarchy/transformation-node-quaternion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Transforming Node by Quaternion

## Úvod

Vítejte v podrobném průvodci o transformaci uzlu pomocí čtveřice ve 3D scénách pomocí Aspose.3D pro .NET. V tomto tutoriálu prozkoumáme výkonné možnosti Aspose.3D pro .NET a projdeme si procesem přidávání transformací do 3D uzlu pomocí čtveřic.

## Předpoklady

Než se pustíme do výukového programu, ujistěte se, že máte splněny následující předpoklady:

-  Aspose.3D for .NET: Ujistěte se, že máte nainstalovanou knihovnu Aspose.3D. Můžete si jej stáhnout z[stránka vydání](https://releases.aspose.com/3d/net/).

- Vývojové prostředí: Nastavte své vývojové prostředí .NET pomocí nezbytných nástrojů a konfigurací.

- Základní pochopení 3D pojmů: Užitečná bude znalost 3D grafiky a pojmů.

## Importovat jmenné prostory

Ve svém projektu .NET zahrňte požadované jmenné prostory pro Aspose.3D:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

## Krok 1: Inicializujte objekt scény

```csharp
// ExStart:AddTransformationToNodeByQuaternion
// Inicializujte objekt scény
Scene scene = new Scene();
```

## Krok 2: Inicializujte objekt třídy uzlu

```csharp
// Inicializujte objekt třídy Node
Node cubeNode = new Node("cube");
```

## Krok 3: Vytvořte síť pomocí Polygon Builder

```csharp
// Volejte Common class create mesh pomocí metody polygon builder pro nastavení instance mesh
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## Krok 4: Nasměrujte uzel na geometrii sítě

```csharp
// Bodový uzel ke geometrii sítě
cubeNode.Entity = mesh;
```

## Krok 5: Nastavte Rotation pomocí Quaternion

```csharp
// Nastavte rotaci
cubeNode.Transform.Rotation = Quaternion.FromRotation(new Vector3(0, 1, 0), new Vector3(0.3, 0.5, 0.1));            
```

## Krok 6: Nastavte překlad

```csharp
// Nastavte překlad
cubeNode.Transform.Translation = new Vector3(0, 0, 20);            
```

## Krok 7: Přidejte kostku do scény

```csharp
// Přidejte kostku na scénu
scene.RootNode.ChildNodes.Add(cubeNode);
```

## Krok 8: Uložte 3D scénu

```csharp
// Cesta k adresáři dokumentů.
var output = "Your Output Directory" + "TransformationToNode.fbx";

// Uložte 3D scénu v podporovaných formátech souborů
scene.Save(output, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByQuaternion
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

## Závěr

 Gratulujeme! Úspěšně jste se naučili, jak transformovat uzel čtveřicí ve 3D scénách pomocí Aspose.3D pro .NET. Prozkoumejte další funkce a možnosti odkazem na[dokumentace](https://reference.aspose.com/3d/net/).

## FAQ

### Q1: Co je to čtveřice ve 3D grafice?

A1: Čtveřice jsou matematické entity používané k reprezentaci rotací ve 3D prostoru.

### Q2: Jak si mohu stáhnout Aspose.3D pro .NET?

 A2: Knihovnu si můžete stáhnout z[stránka vydání](https://releases.aspose.com/3d/net/).

### Q3: Je k dispozici bezplatná zkušební verze pro Aspose.3D pro .NET?

 A3: Ano, můžete získat bezplatnou zkušební verzi[tady](https://releases.aspose.com/).

### Q4: Kde najdu podporu pro Aspose.3D pro .NET?

 A4: Navštivte[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) za podporu a diskuze.

### Q5: Jak získám dočasnou licenci pro Aspose.3D?

 A5: Získejte dočasnou licenci[tady](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
