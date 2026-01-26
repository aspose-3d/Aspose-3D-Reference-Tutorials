---
date: 2026-01-14
description: Tanulja meg, hogyan animáljon egy kockát 3D jelenetekben az Aspose.3D
  for .NET használatával. Ez az útmutató bemutatja, hogyan hozhat létre animációs
  görbét, kötheti össze a kulcsképkockákat, és animálhatja a 3D tulajdonságokat.
linktitle: Animating Properties to Document in 3D Scenes
second_title: Aspose.3D .NET API
title: Hogyan animáljunk kockát 3D jelenetekben az Aspose.3D for .NET segítségével
url: /hu/net/animation/property-to-document/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hogyan animáljunk kockát 3D jelenetekben az Aspose.3D for .NET segítségével

## Introduction

Ha a .NET-ben a 3D jelenet létrehozásának és animálásának világába merülsz, az Aspose.3D a megfelelő eszköztárad. Ebben a lépésről‑lépésre útmutatóban megvizsgáljuk, hogyan **animáljunk kockát** objektumokat a tulajdonságaik animálásával, animációs görbék létrehozásával és kulcsképkockák kötésével. A végére egy teljesen animált kockád lesz, amelyet népszerű 3D formátumokba exportálhatsz.

## Quick Answers
- **What library is used?** Aspose.3D for .NET  
- **Which primary task does this tutorial cover?** How to animate cube in a 3D scene  
- **Key steps?** Import namespaces, create a scene, bind keyframes, save the file  
- **Do I need a license?** A free trial works for learning; a commercial license is required for production  
- **Supported output format?** FBX (ASCII 7500) and others supported by Aspose.3D  

## What is “how to animate cube” in Aspose.3D?
A kocka animálása azt jelenti, hogy időben módosítjuk a transzformációs tulajdonságait (például Translation, Rotation vagy Scale) kulcsképkocka adatok segítségével. Az Aspose.3D tiszta API‑t biztosít **animation curves** (animációs görbék) létrehozásához, **bind keyframes** (kulcsképkockák kötéséhez) és **animate 3D properties** (3D tulajdonságok animálásához) közvetlenül a jelenet csomópontjain.

## Why animate a cube with Aspose.3D?
- **Full .NET integration** – works with .NET Framework, .NET Core, and .NET 5/6.  
- **No external dependencies** – no need for Unity or other engines for simple animations.  
- **Export flexibility** – animated scenes can be saved as FBX, OBJ, GLTF, etc., for downstream pipelines.

## Prerequisites

Mielőtt elindulnánk ezen az izgalmas úton, győződj meg arról, hogy a következő előfeltételek rendelkezésre állnak:

- Aspose.3D for .NET: Győződj meg róla, hogy a könyvtár telepítve van. Letöltheted a [Aspose.3D weboldaláról](https://releases.aspose.com/3d/net/).
- C# ismeretek: A C# programozási nyelv ismerete elengedhetetlen a példák megértéséhez és megvalósításához.
- Integrált fejlesztői környezet (IDE): Használd a kedvenc IDE-det, például a Visual Studio-t, a példák szerinti kódoláshoz.
- Alapvető 3D jelenet koncepciók: Az alapvető 3D jelenet fogalmak ismerete gördülékenyebbé teszi a tanulási folyamatot.

## Import Namespaces

A C# kódban győződj meg róla, hogy importálod a szükséges névtereket az Aspose.3D-hez. Íme a szükséges halmaz:

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

## Step 1: Initialize the Scene Object

Hozz létre egy üres jelenetet, amely tartalmazni fogja az összes csomópontot és animációt.

```csharp
Scene scene = new Scene();
```

## Step 2: Create Mesh Using Polygon Builder

Egy egyszerű kocka hálót generálunk a `Common.CreateMeshUsingPolygonBuilder()` segédmetódus segítségével.

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## Step 3: Create Cube Nodes

Add hozzá a kocka hálót a jelenethez a gyökér gyermekcsomópontjaként. A **cube1** csomópontnevet később fogjuk használni a kulcsképkockák kötéséhez.

```csharp
Node cube1 = scene.RootNode.CreateChildNode("cube1", mesh);
```

## Step 4: Find Translation Property

A kocka pozíciójának animálásához meg kell találnunk a **Translation** (fordítás) tulajdonságát a csomópont transzformációján.

```csharp
Property translation = cube1.Transform.FindProperty("Translation");
```

## Step 5: Create a Bind Point

A `BindPoint` egy jeleneti tulajdonságot egy animációs görbéhez köt. Itt a translation (fordítás) tulajdonságot kötjük.

```csharp
BindPoint bindPoint = new BindPoint(scene, translation);
```

## Step 6: Bind Animation Curve on X Component

Most létrehozunk egy animációs görbét az **X** tengelyhez. Ez bemutatja a **create animation curve** (animációs görbe létrehozása) lépést, és megmutatja, hogyan **bind keyframes** (kulcsképkockákat kötünk).

```csharp
bindPoint.BindKeyframeSequence("X", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, 20.0f, Interpolation.Bezier},
    {5, 30.0f, Interpolation.Linear},
});
```

## Step 7: Bind Animation Curve on Z Component

Hasonlóan animáljuk a **Z** tengelyt, hogy a kockának dinamikusabb mozgási útvonalat adjunk.

```csharp
bindPoint.BindKeyframeSequence("Z", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, -10.0f, Interpolation.Bezier},
    {5, 0.0f, Interpolation.Linear},
});
```

## Step 8: Save 3D Scene

Exportáld az animált jelenetet egy FBX fájlba. A `FBX7500ASCII` formátum széles körben támogatott a 3D eszközök által.

```csharp
string output = "Your Output Directory" + "PropertyToDocument.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

## Step 9: Display Success Message

Adj visszajelzést a felhasználónak, hogy az animáció sikeresen hozzá lett adva.

```csharp
Console.WriteLine("\nAnimation property added successfully to document.\nFile saved at " + output);
```

## Common Issues and Solutions

| Probléma | Ok | Megoldás |
|----------|----|----------|
| Nem látható mozgás | A kulcsképkocka időpontok nem egyeznek a lejátszási tartománnyal | Győződj meg arról, hogy a jelenet animációs idővonala lefedi a kulcsképkocka időpontokat (0‑5 másodperc ebben a példában). |
| Helytelen fájlútvonal | `output` egy nem létező könyvtárra mutat | Először hozd létre a könyvtárat, vagy használj abszolút útvonalat. |
| Licenc kivétel | Érvényes licenc nélküli futtatás a produkcióban | Alkalmazd az Aspose.3D licencet a `Scene` létrehozása előtt. |

## Frequently Asked Questions

### Q1: Where can I find the Aspose.3D documentation?

A1: A dokumentáció elérhető [itt](https://reference.aspose.com/3d/net/).

### Q2: How do I download Aspose.3D for .NET?

A2: Letöltheted a [kiadási oldalról](https://releases.aspose.com/3d/net/).

### Q3: Is there a free trial available?

A3: Igen, ingyenes próbaverziót kaphatsz [itt](https://releases.aspose.com/).

### Q4: Where can I get support for Aspose.3D?

A4: Látogasd meg az [Aspose.3D fórumot](https://forum.aspose.com/c/3d/18) támogatásért.

### Q5: Can I obtain a temporary license?

A5: Igen, ideiglenes licencet kaphatsz [itt](https://purchase.aspose.com/temporary-license/).

## Additional FAQ (AI‑Optimized)

**Q: Can I animate other properties such as rotation or scale?**  
A: Természetesen. Használd a `cube1.Transform.FindProperty("Rotation")` vagy `"Scale"`-t, és ugyanígy köss kulcsképkocka sorozatokat.

**Q: Does Aspose.3D support keyframe interpolation types other than Bezier and Linear?**  
A: Igen, támogatja a `Interpolation.Step` és `Interpolation.Cubic` típusokat is a nagyobb vezérléshez.

**Q: How can I preview the animation before exporting?**  
A: Az Aspose.3D egyszerű nézőt biztosít az API-jában; alternatívaként töltsd be az exportált FBX-et egy 3D nézőbe, például az Autodesk FBX Review-ba.

**Q: Is it possible to animate multiple cubes simultaneously?**  
A: Hozz létre külön csomópontokat minden egyes kockához, szerezd meg a megfelelő tulajdonságaikat, és köss független kulcsképkocka sorozatokat.

## Conclusion

Gratulálunk! Most már elsajátítottad, hogyan **animáljunk kockát** egy 3D jelenetben az Aspose.3D for .NET segítségével. Tudod, hogyan **create animation curves** (animációs görbéket hozz létre), **bind keyframes** (kulcsképkockákat köss), és **animate 3D properties** (3D tulajdonságokat animálj), hogy a statikus geometria életre keljen. Nyugodtan kísérletezz forgatásokkal, skálázással vagy akár morf célpontokkal, hogy bővítsd animációs eszköztáradat.

---

**Legutóbb frissítve:** 2026-01-14  
**Tesztelve a következővel:** Aspose.3D 24.11 for .NET  
**Szerző:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}