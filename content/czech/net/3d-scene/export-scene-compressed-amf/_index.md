---
title: Export 3D scény do komprimovaného formátu AMF
linktitle: Export 3D scény do komprimovaného formátu AMF
second_title: Aspose.3D .NET API
description: Naučte se exportovat 3D scény do komprimovaného formátu AMF pomocí Aspose.3D for .NET. Vylepšete své rozvojové dovednosti pomocí tohoto podrobného průvodce.
type: docs
weight: 11
url: /cs/net/3d-scene/export-scene-compressed-amf/
---
## Úvod

dynamickém světě 3D modelování a vykreslování jsou prvořadé efektivita a flexibilita. Aspose.3D for .NET umožňuje vývojářům bezproblémově exportovat 3D scény do komprimovaného formátu AMF (Additive Manufacturing File), což zajišťuje optimální velikost souboru bez kompromisů v kvalitě. Tento tutoriál vás provede procesem krok za krokem a usnadní začátečníkům i zkušeným vývojářům využít možnosti Aspose.3D pro .NET.

## Předpoklady

Než se pustíte do výukového programu, ujistěte se, že máte následující předpoklady:

- Základní porozumění konceptům 3D modelování
- Visual Studio nainstalované na vašem počítači
-  Aspose.3D pro knihovnu .NET. Můžete si jej stáhnout[tady](https://releases.aspose.com/3d/net/)
- Touha zlepšit své 3D vývojové dovednosti!

## Importovat jmenné prostory

Ujistěte se, že ve svém projektu importujete potřebné jmenné prostory, abyste mohli využít funkčnost Aspose.3D pro .NET:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Krok 1: Načtěte 3D scénu

Začněte načtením 3D scény pomocí Aspose.3D for .NET. Vytvořte objekt scény a přidejte do něj entity, jako jsou boxy:

```csharp
Scene scene = new Scene();
var box = new Box();
var tr = scene.RootNode.CreateChildNode(box).Transform;
tr.Scale = new Vector3(12, 12, 12);
tr.Translation = new Vector3(10, 0, 0);
```

## Krok 2: Změna měřítka

Dále použijte transformaci měřítka na jiný rámeček ve scéně:

```csharp
tr = scene.RootNode.CreateChildNode(box).Transform;
tr.Scale = new Vector3(5, 5, 5);
```

## Krok 3: Nastavte Eulerovy úhly

Nastavte Eulerovy úhly pro transformaci:

```csharp
tr.EulerAngles = new Vector3(50, 10, 0);
```

## Krok 4: Vytvořte podřízené uzly

Pokračujte ve vytváření scény vytvořením podřízených uzlů:

```csharp
scene.RootNode.CreateChildNode();
scene.RootNode.CreateChildNode().CreateChildNode(box);
scene.RootNode.CreateChildNode().CreateChildNode(box);
```

## Krok 5: Uložte komprimovaný soubor AMF

Nakonec uložte 3D scénu do komprimovaného souboru AMF v požadovaném výstupním adresáři:

```csharp
scene.Save("Your Output Directory" + "Aspose.amf", new AmfSaveOptions() { EnableCompression = false });
```

## Závěr

Gratulujeme! Úspěšně jste exportovali 3D scénu do komprimovaného formátu AMF pomocí Aspose.3D for .NET. Tato výkonná knihovna otevírá svět možností pro 3D vývojáře a umožňuje jim vytvářet efektivní a vizuálně úžasné modely.

## FAQ

### Q1: Je Aspose.3D kompatibilní s oblíbeným 3D modelovacím softwarem?

Odpověď 1: Aspose.3D podporuje různé formáty souborů, díky čemuž je kompatibilní s oblíbenými nástroji pro 3D modelování.

### Q2: Mohu povolit kompresi pro jiné formáty souborů kromě AMF?

Odpověď 2: Ano, Aspose.3D poskytuje možnosti pro povolení komprese pro různé formáty souborů.

### Q3: Je Aspose.3D vhodný pro začátečníky i pokročilé vývojáře?

A3: Rozhodně! Aspose.3D nabízí jednoduchost pro začátečníky a pokročilé funkce pro zkušené vývojáře.

### Q4: Existují nějaká omezení velikosti 3D scén, které lze exportovat?

A4: Aspose.3D je navržen pro zpracování scén různé složitosti a neexistují žádná přísná omezení velikosti.

### Q5: Kde najdu další podporu a komunitní diskuse?

A5: Navštivte[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) za podporu a diskuze.