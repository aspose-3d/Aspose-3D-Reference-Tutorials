---
title: Konverze materiálu bez PBR na PBR
linktitle: Konverze materiálu bez PBR na PBR
second_title: Aspose.3D .NET API
description: Prozkoumejte Aspose.3D for .NET – bez námahy převeďte materiály bez PBR na PBR. Komplexní návod a výkonné API.
type: docs
weight: 16
url: /cs/net/loading-and-saving/gltf/non-pbr-to-pbr-material-conversion/
---
## Úvod

Vítejte v tomto podrobném průvodci o použití Aspose.3D pro .NET k převodu Non-PBR (Physically Based Rendering) na PBR materiály. Aspose.3D je výkonné API, které umožňuje vývojářům bezproblémově pracovat s 3D formáty souborů v jejich aplikacích .NET.

## Předpoklady

Než se pustíme do výukového programu, ujistěte se, že máte následující předpoklady:

-  Aspose.3D for .NET: Ujistěte se, že máte nainstalovanou knihovnu Aspose.3D for .NET. Odkaz ke stažení najdete[tady](https://releases.aspose.com/3d/net/).

- Základní porozumění C#: Tento tutoriál předpokládá, že máte základní znalosti o programování C#.

- IDE (Integrated Development Environment): Vyberte si preferované IDE pro vývoj .NET, jako je Visual Studio.

## Importovat jmenné prostory

V kódu C# začněte importováním potřebných jmenných prostorů:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Krok 1: Inicializujte novou 3D scénu

Začněte vytvořením nové 3D scény pomocí následujícího kódu:

```csharp
// ExStart:Non_PBRtoPBRMaterial
// inicializovat novou 3D scénu
var scene = new Scene();
```

## Krok 2: Vytvořte 3D objekt

Dále vytvořte 3D objekt, například krabici:

```csharp
var box = new Box();
scene.RootNode.CreateChildNode("box1", box).Material = new PhongMaterial() { DiffuseColor = new Vector3(1, 0, 1) };
```

## Krok 3: Nakonfigurujte konverzi materiálu

Nastavte možnosti převodu materiálu pro převod bez PBR na PBR:

```csharp
GltfSaveOptions options = new GltfSaveOptions(FileFormat.GLTF2);
options.MaterialConverter = delegate (Material material)
{
    PhongMaterial phongMaterial = (PhongMaterial)material;
    return new PbrMaterial() { Albedo = new Vector3(phongMaterial.DiffuseColor.x, phongMaterial.DiffuseColor.y, phongMaterial.DiffuseColor.z) };
};
```

## Krok 4: Uložte ve formátu GLTF 2.0

Uložte převedenou scénu ve formátu GLTF 2.0:

```csharp
scene.Save("Your Output Directory" + "Non_PBRtoPBRMaterial_Out.gltf", options);
// ExEnd:Non_PBRtoPBRMateriál
```

Opakujte tyto kroky podle potřeby pro váš konkrétní případ použití a ujistěte se, že každý detail je nakonfigurován správně.

## Závěr

Gratulujeme! Úspěšně jste se naučili, jak převádět materiály bez PBR na PBR pomocí Aspose.3D for .NET. Tento výkonný nástroj otevírá nekonečné možnosti pro manipulaci s 3D grafikou ve vašich aplikacích .NET.

## FAQ

### Q1: Je Aspose.3D kompatibilní se všemi 3D formáty souborů?

Odpověď 1: Ano, Aspose.3D podporuje širokou škálu formátů 3D souborů a poskytuje flexibilitu ve vašich projektech.

### Q2: Mohu použít Aspose.3D pro komerční aplikace?

 A2: Rozhodně! Aspose.3D je komerční produkt a můžete si jej zakoupit[tady](https://purchase.aspose.com/buy).

### Q3: Potřebuji pro testování dočasnou licenci?

 A3: Ano, můžete získat dočasnou licenci pro testovací účely[tady](https://purchase.aspose.com/temporary-license/).

### Q4: Kde najdu podporu pro Aspose.3D?

 A4: Navštivte[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) za podporu komunity a diskuze.

### Q5: Je k dispozici bezplatná zkušební verze?

 A5: Ano, můžete prozkoumat bezplatnou zkušební verzi[tady](https://releases.aspose.com/).