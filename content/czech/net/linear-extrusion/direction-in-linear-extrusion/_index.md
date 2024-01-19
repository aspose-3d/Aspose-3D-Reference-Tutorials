---
title: Směr v lineárním vytlačování
linktitle: Směr v lineárním vytlačování
second_title: Aspose.3D .NET API
description: Odemkněte svět 3D modelování s Aspose.3D pro .NET. Naučte se směr lineárního vytlačování, podpořte kreativitu a bez námahy vytvářejte pohlcující aplikace.
type: docs
weight: 11
url: /cs/net/linear-extrusion/direction-in-linear-extrusion/
---
## Úvod

V dynamickém světě vývoje softwaru je tvorba pohlcujících 3D modelů nepostradatelnou dovedností. Aspose.3D for .NET poskytuje vývojářům robustní sadu nástrojů pro využití potenciálu 3D modelování v jejich aplikacích. V tomto tutoriálu se ponoříme do zajímavého světa lineárního vytlačování a prozkoumáme nuance funkce "Směr lineárního vytlačování".

## Předpoklady

Než se vydáme na tuto vzrušující cestu, ujistěte se, že máte splněny následující předpoklady:

-  Aspose.3D for .NET: Stáhněte a nainstalujte knihovnu z[Aspose.3D .NET dokumentace](https://reference.aspose.com/3d/net/).

- Vývojové prostředí: Ujistěte se, že máte nastavené funkční vývojové prostředí .NET.

## Importovat jmenné prostory

Ve svém projektu .NET importujte potřebné jmenné prostory pro přístup k funkcím Aspose.3D. Na začátek kódu přidejte následující řádky:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Krok 1: Inicializujte základní profil

Začněte inicializací základního profilu, který má být vytlačen. V tomto příkladu vytvoříme tvar obdélníku s poloměrem zaoblení 0,3.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Krok 2: Vytvořte 3D scénu

Vytvořte základ pro své 3D mistrovské dílo vytvořením scény.

```csharp
Scene scene = new Scene();
```

## Krok 3: Vytvořte uzly

Generujte uzly ve scéně, které reprezentují různé součásti vašeho 3D prostředí.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(8, 0, 0);
```

## Krok 4: Lineární vytlačování bez směru

 Proveďte lineární vysunutí na levém uzlu pomocí`Twist` a`Slices` vlastnosti.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## Krok 5: Lineární vytlačování se směrem

 Rozšiřte možnosti vytlačování začleněním`Direction` vlastnost v pravém uzlu.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, Direction = new Vector3(0.3, 0.2, 1) });
```

## Krok 6: Uložte 3D scénu

 Zachovejte svůj výtvor uložením 3D scény. Nahradit`"Your Output Directory"` s požadovaným adresářem.

```csharp
scene.Save("Your Output Directory" + "DirectionInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Gratulujeme! Úspěšně jste implementovali lineární vytlačování pomocí Aspose.3D pro .NET a prozkoumali jste jak tradiční, tak směrový přístup.

## Závěr

tomto tutoriálu jsme prošli fascinující oblastí 3D modelování pomocí Aspose.3D pro .NET. Lineární vytlačování, s i bez směru, otevírá nekonečné možnosti pro vývojáře, kteří chtějí vytvářet vizuálně ohromující aplikace. S Aspose.3D máte sílu 3D modelování na dosah ruky.

## FAQ

### Q1: Jak mohu získat dočasnou licenci pro Aspose.3D for .NET?

 A1: Návštěva[Přijměte dočasnou licenci](https://purchase.aspose.com/temporary-license/) získat dočasnou licenci.

### Q2: Kde najdu podporu pro Aspose.3D?

 A2: Připojte se[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) vyhledat pomoc a spojit se s komunitou.

### Q3: Je k dispozici bezplatná zkušební verze?

 A3: Ano, prozkoumejte funkce pomocí bezplatné zkušební verze na[Vydání Aspose.3D](https://releases.aspose.com/).

### Q4: Jak koupím Aspose.3D pro .NET?

 A4: Přejděte na[Aspose Nákupní stránku](https://purchase.aspose.com/buy) pro licenční možnosti a podrobnosti o nákupu.

### Q5: Kde najdu podrobnou dokumentaci k Aspose.3D pro .NET?

 A5: Viz komplexní[Aspose.3D .NET dokumentace](https://reference.aspose.com/3d/net/) pro podrobné informace.