---
title: Řezy v lineárním vytlačování
linktitle: Řezy v lineárním vytlačování
second_title: Aspose.3D .NET API
description: Prozkoumejte svět 3D designu s Aspose.3D pro .NET. Vytvářejte úžasné modely pomocí našeho výukového programu lineárního vytlačování.
weight: 13
url: /cs/net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Řezy v lineárním vytlačování

## Úvod

Vítejte ve světě 3D designu pomocí Aspose.3D pro .NET! Ať už jste zkušený vývojář nebo teprve začínáte, tento tutoriál vás provede procesem vytváření úžasných 3D vizualizací pomocí výkonné knihovny Aspose.3D.

## Předpoklady

Než se ponoříte do světa 3D designu s Aspose.3D, ujistěte se, že máte následující předpoklady:

-  Aspose.3D for .NET Library: Ujistěte se, že máte nainstalovanou knihovnu Aspose.3D. Můžete si jej stáhnout z[tady](https://releases.aspose.com/3d/net/).

- Integrované vývojové prostředí (IDE): Použijte jakékoli preferované IDE kompatibilní s vývojem .NET.

- Základní porozumění C#: Seznamte se se základy programovacího jazyka C#.

- Touha prozkoumat 3D design: Vášeň pro vytváření vizuálně úžasných 3D modelů!

## Importovat jmenné prostory

Chcete-li začít svou cestu 3D návrhu s Aspose.3D, budete muset importovat potřebné jmenné prostory. To zajistí, že váš kód bude mít přístup k požadovaným třídám a funkcím.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Lineární vytlačování - Řezy v lineárním vytlačování

Nyní se vrhneme na praktický příklad – Lineární vytlačování s plátky. Tato technika umožňuje vytvářet složité 3D modely s různou úrovní detailů.

### Krok 1: Inicializujte základní profil

```csharp
// ExStart:InitializeBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd:InitializeBaseProfile
```

### Krok 2: Vytvořte 3D scénu

```csharp
// ExStart:Create3DScene
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### Krok 3: Vytvořte levý a pravý uzel

```csharp
// ExStart:CreateLeftRightNodes
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### Krok 4: Proveďte lineární vysunutí na levém uzlu

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### Krok 5: Proveďte lineární vytlačování na pravém uzlu

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### Krok 6: Uložte 3D scénu

```csharp
// ExStart:Save3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
//ExEnd:Save3DScene
```

## Závěr

Gratulujeme! Úspěšně jste se naučili, jak provádět lineární vytlačování s řezy pomocí Aspose.3D pro .NET. Toto je jen začátek vaší cesty 3D designu s Aspose.3D – popusťte uzdu své kreativitě a prozkoumejte nekonečné možnosti!

## FAQ

### Q1: Mohu používat Aspose.3D pro .NET s jinými programovacími jazyky?

Odpověď 1: Aspose.3D je primárně navržen pro .NET, ale můžete prozkoumat možnosti interoperability s jazyky jako Python pomocí vazeb .NET.

### Q2: Kde najdu podrobnou dokumentaci k Aspose.3D pro .NET?

 A2: Viz dokumentace[tady](https://reference.aspose.com/3d/net/) pro podrobné informace o možnostech a použití Aspose.3D.

### Q3: Je k dispozici bezplatná zkušební verze pro Aspose.3D pro .NET?

 A3: Ano, můžete si stáhnout bezplatnou zkušební verzi[tady](https://releases.aspose.com/) prozkoumání funkcí knihovny před nákupem.

### Q4: Jak mohu získat technickou podporu pro Aspose.3D pro .NET?

 A4: Navštivte fórum Aspose.3D[tady](https://forum.aspose.com/c/3d/18) vyhledat pomoc a zapojit se do komunity.

### Q5: Mohu použít dočasnou licenci pro Aspose.3D for .NET?

 A5: Ano, získat dočasnou licenci[tady](https://purchase.aspose.com/temporary-license/) pro účely hodnocení.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
