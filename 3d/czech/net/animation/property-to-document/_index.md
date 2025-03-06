---
title: Animace vlastností pro dokument ve 3D scénách
linktitle: Animace vlastností pro dokument ve 3D scénách
second_title: Aspose.3D .NET API
description: Naučte se animovat 3D vlastnosti pomocí Aspose.3D pro .NET. Podrobný průvodce vytvářením dynamických scén.
weight: 10
url: /cs/net/animation/property-to-document/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Animace vlastností pro dokument ve 3D scénách

## Úvod

Pokud se ponoříte do říše tvorby 3D scén a animací v .NET, Aspose.3D je vaše základní sada nástrojů. V tomto podrobném průvodci prozkoumáme proces animace vlastností ve 3D scénách pomocí Aspose.3D for .NET. Na konci budete vybaveni znalostmi, abyste vdechli život svým 3D projektům.

## Předpoklady

Než se vydáme na tuto vzrušující cestu, ujistěte se, že máte splněny následující předpoklady:

-  Aspose.3D for .NET: Ujistěte se, že máte nainstalovanou knihovnu. Můžete si jej stáhnout z[Web Aspose.3D](https://releases.aspose.com/3d/net/).

- Znalost C#: Pro pochopení a implementaci příkladů je nezbytná znalost programovacího jazyka C#.

- Integrované vývojové prostředí (IDE): Pro kódování spolu s příklady použijte preferované IDE, jako je Visual Studio.

- Základní koncepty 3D scén: Díky pochopení základních konceptů 3D scén bude vaše cesta za učením plynulejší.

## Importovat jmenné prostory

Ujistěte se, že ve svém kódu C# importujete potřebné jmenné prostory pro Aspose.3D. Zde je příklad:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose._3D.Examples.CSharp.Geometry_Hierarchy;
```

## Krok 1: Inicializujte objekt scény

```csharp
Scene scene = new Scene();
```

## Krok 2: Vytvořte síť pomocí Polygon Builder

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## Krok 3: Vytvořte uzly krychle

```csharp
Node cube1 = scene.RootNode.CreateChildNode("cube1", mesh);
```

## Krok 4: Najděte překladovou vlastnost

```csharp
Property translation = cube1.Transform.FindProperty("Translation");
```

## Krok 5: Vytvořte bod vazby

```csharp
BindPoint bindPoint = new BindPoint(scene, translation);
```

## Krok 6: Spojte křivku animace na X komponentu

```csharp
bindPoint.BindKeyframeSequence("X", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, 20.0f, Interpolation.Bezier},
    {5, 30.0f, Interpolation.Linear},
});
```

## Krok 7: Spojte křivku animace na Z komponentu

```csharp
bindPoint.BindKeyframeSequence("Z", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, -10.0f, Interpolation.Bezier},
    {5, 0.0f, Interpolation.Linear},
});
```

## Krok 8: Uložte 3D scénu

```csharp
string output = "Your Output Directory" + "PropertyToDocument.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

## Krok 9: Zobrazte zprávu o úspěchu

```csharp
Console.WriteLine("\nAnimation property added successfully to document.\nFile saved at " + output);
```

## Závěr

Gratulujeme! Právě jste zvládli umění animace vlastností ve 3D scénách pomocí Aspose.3D for .NET. Nyní nechte svou kreativitu proudit a vlijte život do svých 3D výtvorů.

## Často kladené otázky

### Q1: Kde najdu dokumentaci Aspose.3D?

 A1: Dokumentace je k dispozici[tady](https://reference.aspose.com/3d/net/).

### Q2: Jak stáhnu Aspose.3D pro .NET?

 A2: Můžete si jej stáhnout z[stránka vydání](https://releases.aspose.com/3d/net/).

### Q3: Je k dispozici bezplatná zkušební verze?

 A3: Ano, můžete získat bezplatnou zkušební verzi[tady](https://releases.aspose.com/).

### Q4: Kde mohu získat podporu pro Aspose.3D?

 A4: Navštivte[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) pro podporu.

### Q5: Mohu získat dočasnou licenci?

 A5: Ano, můžete získat dočasnou licenci[tady](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
