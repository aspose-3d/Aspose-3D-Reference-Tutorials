---
title: Nastavení normálů na krychli
linktitle: Nastavení normálů na krychli
second_title: Aspose.3D .NET API
description: Naučte se nastavit normály na 3D krychli pomocí Aspose.3D pro .NET. Vylepšete své dovednosti v oblasti 3D modelování pomocí tohoto podrobného průvodce.
weight: 17
url: /cs/net/geometry-and-hierarchy/setup-normals-cube/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Nastavení normálů na krychli

## Úvod

Vítejte v našem podrobném průvodci nastavením normál na krychli ve 3D scénách pomocí Aspose.3D pro .NET. Aspose.3D je výkonná knihovna, která umožňuje vývojářům .NET pracovat s 3D soubory a poskytuje širokou škálu funkcí pro 3D modelování a manipulaci.

V tomto tutoriálu vás provedeme procesem nastavení normál na krychli ve 3D scéně pomocí Aspose.3D. Normály jsou zásadní pro správné osvětlení a stínování ve 3D grafice a pochopení toho, jak je nastavit, je zásadní pro vytváření realistických a vizuálně přitažlivých 3D modelů.

## Předpoklady

Než se pustíme do výukového programu, ujistěte se, že máte následující předpoklady:

-  Aspose.3D for .NET: Ujistěte se, že máte nainstalovanou knihovnu Aspose.3D. Můžete si jej stáhnout z[Aspose.3D pro dokumentaci .NET](https://reference.aspose.com/3d/net/).

## Importovat jmenné prostory

Pro začátek importujme potřebné jmenné prostory do vašeho projektu:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

## Krok 1: Nezpracovaná normální data

První krok zahrnuje definování nezpracovaných normálních dat pro naši krychli. Normály jsou reprezentovány jako objekty Vector4 a zde je příklad:

```csharp
// ExStart:RawNormalData
Vector4[] normals = new Vector4[]
{
    new Vector4(-0.577350258,-0.577350258, 0.577350258, 1.0),
    //... (opakujte pro dalších 7 vrcholů)
};
// ExEnd:RawNormalData
```

## Krok 2: Vytvořte síť pomocí Polygon Builder

Dále vytvoříme síť pomocí metody polygon builder. To se provádí voláním společné třídy pro vytvoření instance sítě:

```csharp
// ExStart:CreateMesh
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
// ExEnd:CreateMesh
```

## Krok 3: Nastavte Normals na Cube

Nyní nastavíme normály na krychli vytvořením VertexElementNormal a zkopírováním normálních dat do prvku vertex:

```csharp
// ExStart:SetupNormalsOnCube
VertexElementNormal elementNormal = mesh.CreateElement(VertexElementType.Normal, MappingMode.ControlPoint, ReferenceMode.Direct) as VertexElementNormal;
elementNormal.Data.AddRange(normals);
// ExEnd:SetupNormalsOnCube
```

## Krok 4: Tisk zprávy o úspěchu

Nakonec vytiskneme zprávu o úspěchu, abychom potvrdili, že normály byly úspěšně nastaveny:

```csharp
Console.WriteLine("\nNormals have been set up successfully on the cube.");
```

## Závěr

Gratulujeme! Úspěšně jste se naučili, jak nastavit normály na krychli ve 3D scénách pomocí Aspose.3D pro .NET. Tyto znalosti jsou nezbytné pro dosažení realistických efektů osvětlení a stínování ve vašich 3D modelech.

## FAQ

### Q1: Je Aspose.3D kompatibilní s jinými 3D formáty souborů?

Odpověď 1: Ano, Aspose.3D podporuje různé formáty 3D souborů, což umožňuje bezproblémovou integraci s vašimi stávajícími projekty.

### Q2: Mohu vyzkoušet Aspose.3D před nákupem?

A2: Rozhodně! Bezplatnou zkušební verzi si můžete stáhnout z[tady](https://releases.aspose.com/).

### Q3: Kde najdu dočasné licence pro Aspose.3D?

 A3: Dočasné licence jsou k dispozici ke koupi[tady](https://purchase.aspose.com/temporary-license/).

### Q4: Jaká je zpětná vazba komunity na Aspose.3D?

 A4: Připojte se ke komunitě Aspose.3D na[Fórum](https://forum.aspose.com/c/3d/18) spojit se s ostatními vývojáři a sdílet zkušenosti.

### Q5: Existují nějaké další zdroje pro výuku Aspose.3D?

 A5: Prozkoumejte rozsáhlé[dokumentace](https://reference.aspose.com/3d/net/) k objevování dalších funkcí a tipů.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
