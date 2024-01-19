---
title: Aplikace materiálu PBR na box ve 3D scénách
linktitle: Aplikace materiálu PBR na box ve 3D scénách
second_title: Aspose.3D .NET API
description: Prozkoumejte svět 3D grafiky s Aspose.3D pro .NET. Vytvářejte pohlcující scény bez námahy pomocí fyzicky založených renderovacích materiálů.
type: docs
weight: 10
url: /cs/net/geometry-and-hierarchy/apply-pbr-material-to-box/
---
## Úvod

Vítejte ve fascinujícím světě 3D grafiky! V tomto podrobném průvodci prozkoumáme výkonnou knihovnu Aspose.3D for .NET a naučíme se, jak vytvářet úžasné 3D scény pomocí materiálů PBR (Physically Based Rendering). Aspose.3D zjednodušuje komplexní proces 3D grafiky a otevírá říši možností pro vývojáře.

## Předpoklady

Než se ponoříme do vzrušujícího světa 3D grafiky, ujistěte se, že máte vše nastaveno:

### Stáhněte a nainstalujte Aspose.3D pro .NET

 Navštivte[Aspose.3D pro dokumentaci .NET](https://reference.aspose.com/3d/net/) pro podrobné pokyny ke stažení a instalaci knihovny.

### Získejte licenci

 Chcete-li odemknout plný potenciál Aspose.3D, získejte platnou licenci. Můžete získat dočasnou licenci[tady](https://purchase.aspose.com/temporary-license/) nebo zakoupit plnou licenci[tady](https://purchase.aspose.com/buy).

## Importovat jmenné prostory

Nejprve se ujistěte, že jste naimportovali potřebné jmenné prostory, abyste mohli využít schopností Aspose.3D pro .NET:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Krok 1: Inicializujte scénu

Začněte inicializací 3D scény pomocí následujícího fragmentu kódu:

```csharp
Scene scene = new Scene();
```

## Krok 2: Inicializujte materiál PBR

Vytvořte objekt materiálu PBR pro dosažení realistického vykreslení:

```csharp
PbrMaterial mat = new PbrMaterial();
```

## Krok 3: Nastavte vlastnosti materiálu

Jemně dolaďte vlastnosti materiálu, aby byl téměř kovový a velmi drsný:

```csharp
mat.MetallicFactor = 0.9;
mat.RoughnessFactor = 0.9;
```

## Krok 4: Vytvořte krabici

Vygenerujte krabici, na kterou bude aplikován materiál PBR:

```csharp
var boxNode = scene.RootNode.CreateChildNode("box", new Box());
```

## Krok 5: Naneste materiál na krabici

Přiřaďte materiál PBR k vytvořenému uzlu krabice:

```csharp
boxNode.Material = mat;
```

## Krok 6: Uložte 3D scénu

Uložte 3D scénu do formátu STL s požadovaným výstupním adresářem:

```csharp
scene.Save("Your Output Directory" + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
```

Gratulujeme! Úspěšně jste použili materiál PBR na krabici ve 3D scéně pomocí Aspose.3D for .NET.

## Závěr

Pusťte se do 3D grafiky s Aspose.3D for .NET otevírá dveře nekonečným kreativním možnostem. Díky intuitivnímu rozhraní API a robustním funkcím se vytváření vizuálně úžasných scén stává pro vývojáře příjemným zážitkem.

## FAQ

### Q1: Je Aspose.3D kompatibilní s jinými 3D formáty souborů?

Odpověď 1: Ano, Aspose.3D podporuje různé formáty 3D souborů, což zajišťuje flexibilitu ve vašich projektech.

### Q2: Mohu použít Aspose.3D pro komerční aplikace?

A2: Rozhodně! Aspose.3D poskytuje komerční licence pro bezproblémovou integraci do vašich aplikací.

### Q3: Je k dispozici zkušební verze?

A3: Ano, můžete prozkoumat možnosti Aspose.3D stažením bezplatné zkušební verze[tady](https://releases.aspose.com/).

### Q4: Kde najdu podporu komunity a diskuse?

 A4: Připojte se ke komunitě Aspose.3D na adrese[Aspose.3D fóra](https://forum.aspose.com/c/3d/18) za podporu a diskuze.

### Q5: Jak získám dočasnou licenci pro Aspose.3D?

 A5: Můžete získat dočasnou licenci[tady](https://purchase.aspose.com/temporary-license/) pro účely hodnocení.