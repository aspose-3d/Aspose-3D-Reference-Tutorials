---
title: Střed v lineárním vytlačování
linktitle: Střed v lineárním vytlačování
second_title: Aspose.3D .NET API
description: Prozkoumejte svět 3D modelování s Aspose.3D pro .NET. Vycentrujte techniky lineárního vytlačování, vytvářejte úžasné návrhy a popusťte uzdu své kreativitě.
type: docs
weight: 10
url: /cs/net/linear-extrusion/center-in-linear-extrusion/
---
## Úvod

Vítejte v tomto komplexním průvodci o zvládnutí lineárního vytlačování pomocí Aspose.3D pro .NET. Pokud chcete zlepšit své dovednosti v oblasti 3D modelování a vytvořit úžasné výlisky, jste na správném místě. V tomto tutoriálu se ponoříme do techniky lineárního vytlačování, konkrétně se zaměříme na centrování, abychom dostali vaše návrhy na zcela novou úroveň.

## Předpoklady

Než se vydáme na tuto vzrušující cestu, ujistěte se, že máte splněny následující předpoklady:

- Základní znalost programovacího jazyka C#.
- Visual Studio nainstalované na vašem počítači.
-  Knihovna Aspose.3D for .NET, kterou si můžete stáhnout z[Aspose.3D .NET dokumentace](https://reference.aspose.com/3d/net/).
-  Ujistěte se, že máte přístup k[Aspose.3D .NET dokumentace](https://reference.aspose.com/3d/net/) pro referenci v celém tutoriálu.

## Importovat jmenné prostory

Abychom to nastartovali, importujme potřebné jmenné prostory. Ty položí základ pro naše mistrovské dílo 3D modelování.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Krok 1: Inicializujte základní profil

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Krok 2: Vytvořte 3D scénu

```csharp
Scene scene = new Scene();
```

## Krok 3: Vytvořte levý a pravý uzel

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## Krok 4: Proveďte lineární vysunutí na levém uzlu

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## Krok 5: Nastavte základní rovinu jako referenční

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## Krok 6: Proveďte lineární vytlačování na pravém uzlu

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## Krok 7: Nastavte základní rovinu jako referenční (pravý uzel)

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## Krok 8: Uložte 3D scénu

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Závěr

Gratulujeme! Úspěšně jste zvládli umění lineárního vytlačování s centrováním pomocí Aspose.3D pro .NET. Nebojte se experimentovat s různými parametry a prozkoumejte obrovské možnosti, které tato technika nabízí.

## FAQ

### Q1: Mohu používat Aspose.3D pro .NET s jinými programovacími jazyky?

A1: Aspose.3D primárně podporuje .NET jazyky jako C# a VB.NET.

### Q2: Kde najdu podporu pro dotazy související s Aspose.3D?

 A2: Navštivte[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) za obětavou podporu a diskuse.

### Q3: Je k dispozici bezplatná zkušební verze pro Aspose.3D pro .NET?

 A3: Ano, máte přístup k bezplatné zkušební verzi[tady](https://releases.aspose.com/).

### Q4: Jak mohu získat dočasnou licenci pro Aspose.3D for .NET?

 A4: Můžete získat dočasnou licenci[tady](https://purchase.aspose.com/temporary-license/).

### Q5: Kde mohu zakoupit licenci Aspose.3D for .NET?

 A5: Kupte si licenci[tady](https://purchase.aspose.com/buy).
