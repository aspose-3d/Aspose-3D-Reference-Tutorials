---
title: Twist Offset u lineárního vytlačování
linktitle: Twist Offset u lineárního vytlačování
second_title: Aspose.3D .NET API
description: Prozkoumejte kouzlo Aspose.3D pro .NET pomocí našeho podrobného průvodce o Twist Offsetu v lineárním vytlačování. Zvyšte své 3D projekty bez námahy.
type: docs
weight: 15
url: /cs/net/linear-extrusion/twist-offset-in-linear-extrusion/
---
## Úvod

Vítejte ve světě Aspose.3D for .NET, všestranné knihovny, která umožňuje vývojářům snadno zvládnout 3D manipulaci. V tomto tutoriálu se ponoříme do jedné ze zajímavých funkcí - "Twist Offset in Linear Extrusion." Pokud jste připraveni zlepšit své 3D programovací dovednosti, pojďme se ponořit přímo do toho!

## Předpoklady

Než se vydáme na tuto vzrušující cestu, ujistěte se, že máte splněny následující předpoklady:

-  Aspose.3D for .NET Library: Stáhněte a nainstalujte knihovnu z[stránka vydání](https://releases.aspose.com/3d/net/).

- Vaše vývojové prostředí: Ujistěte se, že je vaše vývojové prostředí nastaveno a připraveno k provozu.

## Importovat jmenné prostory

Začněte importem potřebných jmenných prostorů pro přístup k funkcím poskytovaným Aspose.3D pro .NET. Ve vašem kódu to může vypadat takto:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Nyní rozeberme příklad do zvládnutelných kroků pro zvládnutí kroucení offsetu v lineárním vytlačování:

## Krok 1: Inicializujte základní profil

Začněte vytvořením základního profilu, jehož příkladem je obdélníkový tvar se zadaným poloměrem zaoblení.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Krok 2: Vytvořte scénu

Vygenerujte 3D scénu pro umístění uzlů a tvarů.

```csharp
Scene scene = new Scene();
```

## Krok 3: Vytvořte uzly

Vytvořte uzly ve scéně, levé i pravé.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

## Krok 4: Lineární vytlačování na levém uzlu

Proveďte lineární vysunutí na levém uzlu pomocí vlastnosti twist and slices.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## Krok 5: Lineární vytlačování na pravém uzlu s Twist Offsetem

V pravém uzlu proveďte lineární vysunutí pomocí vlastností kroucení, kroucení offsetu a řezů.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

## Krok 6: Uložte 3D scénu

Uložte 3D scénu do požadovaného výstupního adresáře a určete formát souboru jako WavefrontOBJ.

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Gratulujeme! Úspěšně jste implementovali Twist Offset v Linear Extrusion pomocí Aspose.3D for .NET.

## Závěr

V tomto tutoriálu jsme prozkoumali výkonné možnosti Aspose.3D pro .NET, konkrétně se zaměřením na Twist Offset v Linear Extrusion. S těmito nově nalezenými dovednostmi jste dobře vybaveni k tomu, abyste do svých 3D projektů vlili dynamiku.

## FAQ

### Q1: Mohu používat Aspose.3D pro .NET s jinými programovacími jazyky?

A1: Aspose.3D primárně podporuje jazyky .NET, ale Aspose poskytuje podobné knihovny pro Java a další platformy.

### Q2: Jak získám dočasnou licenci pro Aspose.3D for .NET?

 A2: Návštěva[tento odkaz](https://purchase.aspose.com/temporary-license/) získat dočasnou licenci pro testovací účely.

### Q3: Existuje komunitní fórum pro Aspose.3D pro .NET?

A3: Rozhodně! Připojte se ke komunitě na[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) spojit se s ostatními vývojáři a vyhledat pomoc.

### Q4: Jsou k dispozici další příklady a dokumentace?

 A4: Prozkoumejte[dokumentace](https://reference.aspose.com/3d/net/) pro rozsáhlé návody a příklady.

### Q5: Kde mohu zakoupit Aspose.3D pro .NET?

 A5: Zamiřte[tento odkaz](https://purchase.aspose.com/buy) provést nákup a odemknout plný potenciál Aspose.3D.