---
title: Rozdělení pletiva podle materiálu
linktitle: Rozdělení pletiva podle materiálu
second_title: Aspose.3D .NET API
description: Naučte se rozdělit 3D sítě podle materiálu pomocí Aspose.3D pro .NET. Zlepšete organizaci a efektivitu scény. Podrobný průvodce pro vývojáře.
type: docs
weight: 22
url: /cs/net/objects/split-mesh-by-material/
---
## Úvod
Vítejte v tomto komplexním tutoriálu o rozdělení sítě podle materiálu pomocí Aspose.3D pro .NET! Pokud jste vývojář pracující s 3D grafikou a chcete efektivně spravovat sítě a manipulovat s nimi, jste na správném místě. V této příručce prozkoumáme proces dělení sítě na základě materiálu, což je zásadní úkol při vytváření různorodých a vizuálně přitažlivých 3D scén.
## Předpoklady
Než se pustíte do výukového programu, ujistěte se, že máte splněny následující předpoklady:
-  Aspose.3D for .NET: Ujistěte se, že máte v projektu .NET nainstalovanou knihovnu Aspose.3D. Pokud ne, můžete si jej stáhnout z[vydání](https://releases.aspose.com/3d/net/) strana.
- Základní znalosti 3D grafiky: Seznamte se se základními pojmy 3D grafiky, abyste pochopili nuance manipulace se sítí.
- Vývojové prostředí: Nastavte vhodné vývojové prostředí .NET, jako je Visual Studio.
## Importovat jmenné prostory
Začněte importováním potřebných jmenných prostorů pro přístup k funkci Aspose.3D. Na začátek kódu uveďte následující:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```
Nyní si příklad rozdělíme do několika kroků:
## Krok 1: Vytvoření Box Mesh
```csharp
// Vytvořte síť krabice (složenou ze 6 rovin)
Mesh box = (new Box()).ToMesh();
```
Zde inicializujeme síť představující rámeček se šesti rovinami pomocí Aspose.3D.
## Krok 2: Přidání materiálu do sítě
```csharp
// Vytvořte materiálový prvek na této síti
VertexElementMaterial mat = (VertexElementMaterial)box.CreateElement(VertexElementType.Material, MappingMode.Polygon, ReferenceMode.Index);
// Pro každou rovinu zadejte jiný index materiálu
mat.Indices.AddRange(new int[] { 0, 1, 2, 3, 4, 5 });
```
Tento krok zahrnuje přidání prvku materiálu do sítě a přiřazení odlišných indexů materiálu každé rovině.
## Krok 3: Rozdělení sítě podle materiálu (Zásady CloneData)
```csharp
// Rozdělte jej na 6 dílčích sítí, každá rovina se stane dílčí sítí
Mesh[] planes = PolygonModifier.SplitMesh(box, SplitMeshPolicy.CloneData);
```
Zde jsme síť rozdělili do šesti dílčích sítí na základě specifikovaných materiálů s využitím zásady CloneData.
## Krok 4: Aktualizace materiálových indexů pro kompaktní data
```csharp
mat.Indices.Clear();
mat.Indices.AddRange(new int[] { 0, 0, 0, 1, 1, 1 });
```
Aktualizujte materiálové indexy, abyste se připravili na další operaci rozdělení pomocí zásady CompactData.
## Krok 5: Rozdělení sítě podle materiálu (CompactData Policy)
```csharp
//Rozdělte jej na 2 dílčí sítě, z nichž každá obsahuje specifické roviny
planes = PolygonModifier.SplitMesh(box, SplitMeshPolicy.CompactData);
```
Nyní rozdělíme síť na dvě dílčí sítě, seskupíme roviny na základě materiálů a použijeme zásady CompactData.
## Závěr
Gratulujeme! Úspěšně jste se naučili, jak rozdělit síť podle materiálu pomocí Aspose.3D pro .NET. Tato technika je nezbytná pro efektivní správu složitých 3D scén.
## Často kladené otázky
### Otázka: Mohu použít tuto techniku na vlastní sítě?
Absolutně! Pokud má vaše síť definované materiály, můžete použít tento přístup.
### Otázka: Jak se zásada CloneData liší od zásady CompactData?
Zásada CloneData zajišťuje, že každá dílčí síť sdílí stejné informace o řídicím bodu, zatímco zásada CompactData poskytuje každé dílčí síti její vlastní informace o řídicím bodu.
### Otázka: Jsou při používání této metody ohledy na výkon?
Obecně může mít zásada CloneData o něco lepší výkon díky sdíleným informacím o řídicím bodu.
### Otázka: Mohu si představit výsledky dělení sítě?
Ano, můžete vykreslit a vizualizovat výsledné dílčí sítě pomocí funkcí vykreslování Aspose.3D.
### Otázka: Je Aspose.3D vhodný pro vývoj her?
Zatímco se Aspose.3D primárně používá pro modelování a vykreslování, lze jej integrovat do kanálů vývoje her pro konkrétní úkoly.