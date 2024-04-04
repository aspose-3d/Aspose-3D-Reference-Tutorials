---
title: Nastavení UV na Cube
linktitle: Nastavení UV na Cube
second_title: Aspose.3D .NET API
description: Naučte se nastavit UV mapování na 3D krychli pomocí Aspose.3D pro .NET. Vytvářejte vizuálně úžasné scény s přesným mapováním textur.
type: docs
weight: 18
url: /cs/net/geometry-and-hierarchy/setup-uv-cube/
---
## Úvod

Vytváření podmanivých a vizuálně přitažlivých 3D scén často zahrnuje pečlivý proces nastavení UV mapování na geometrické tvary. V tomto tutoriálu prozkoumáme, jak nastavit UV na krychli pomocí Aspose.3D pro .NET. Aspose.3D je výkonná knihovna .NET, která poskytuje komplexní sadu funkcí pro 3D modelování a manipulaci.

## Předpoklady

Než se pustíte do výukového programu, ujistěte se, že máte následující předpoklady:

1. Aspose.3D for .NET Library: Ujistěte se, že máte nainstalovanou knihovnu Aspose.3D. Můžete si jej stáhnout[tady](https://releases.aspose.com/3d/net/).

2. Vývojové prostředí: Nastavte vývojové prostředí .NET s potřebnými nástroji.

Nyní přejdeme k tutoriálu.

## Importovat jmenné prostory

Nejprve naimportujte potřebné jmenné prostory pro přístup k funkcím Aspose.3D ve vaší aplikaci .NET.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

## Krok 1: Definujte UV pro krychli

Definujte UV souřadnice pro každý vrchol krychle. To zahrnuje specifikaci hodnot U a V pro každý roh krychle.

```csharp
// ExStart:DefineUVs
Vector4[] uvs = new Vector4[]
{
    new Vector4(0.0, 1.0, 0.0, 1.0),
    new Vector4(1.0, 0.0, 0.0, 1.0),
    new Vector4(0.0, 0.0, 0.0, 1.0),
    new Vector4(1.0, 1.0, 0.0, 1.0)
};
// ExEnd:DefineUVs
```

## Krok 2: Definujte UV indexy

Určete indexy UV souřadnic pro každý polygon krychle. To definuje, jak jsou UV záření mapována na povrchy krychle.

```csharp
// ExStart:DefineUVIindices
int[] uvsId = new int[]
{
    0, 1, 3, 2, 2, 3, 5, 4, 4, 5, 7, 6, 6, 7, 9, 8, 1, 10, 11, 3, 12, 0, 2, 13
};
// ExEnd:DefineUVIindices
```

## Krok 3: Vytvořte síť

Použijte knihovnu Aspose.3D k vytvoření sítě pomocí metody polygon builderu. To bude sloužit jako základ pro naši 3D kostku.

```csharp
// ExStart:CreateMesh
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
// ExEnd:CreateMesh
```

## Krok 4: Vytvořte UV prvek

Vytvořte UV prvek v síti pro uložení dat UV mapování.

```csharp
// ExStart:CreateUVElement
VertexElementUV elementUV = mesh.CreateElementUV(TextureMapping.Diffuse, MappingMode.PolygonVertex, ReferenceMode.IndexToDirect);
// ExEnd:CreateUVElement
```

## Krok 5: Zkopírujte data UV do sítě

Zkopírujte dříve definované UV souřadnice a indexy do prvku UV vertex sítě.

```csharp
// ExStart:CopyUVData
elementUV.Data.AddRange(uvs);
elementUV.Indices.AddRange(uvsId);
// ExEnd:CopyUVData
```

## Závěr

Gratulujeme! Úspěšně jste nastavili UV mapování na krychli pomocí Aspose.3D pro .NET. To otevírá možnosti pro vytváření složitých a vizuálně ohromujících 3D scén s přesným mapováním textur.

## FAQ

### Q1: Co je Aspose.3D pro .NET?

A1: Aspose.3D for .NET je výkonná knihovna pro 3D modelování a manipulaci v aplikacích .NET.

### Q2: Kde najdu dokumentaci Aspose.3D?

 A2: Dokumentace je k dispozici[tady](https://reference.aspose.com/3d/net/).

### Q3: Je k dispozici bezplatná zkušební verze?

 A3: Ano, máte přístup k bezplatné zkušební verzi[tady](https://releases.aspose.com/).

### Q4: Jak mohu získat podporu pro Aspose.3D?

 A4: Navštivte fórum podpory[tady](https://forum.aspose.com/c/3d/18).

### Q5: Jsou k dispozici dočasné licence?

 A5: Ano, můžete získat dočasnou licenci[tady](https://purchase.aspose.com/temporary-license/).