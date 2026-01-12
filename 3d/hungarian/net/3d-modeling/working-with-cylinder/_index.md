---
date: 2026-01-12
description: Ismerje meg, hogyan hozhat létre nyíró aljzsilindert, és hogyan exportálhat
  3D modellt OBJ formátumban az Aspose.3D for .NET segítségével. Kövesse ezt a lépésről‑lépésre
  útmutatót a 3D modellezés elsajátításához.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: Hogyan hozzunk létre nyíró aljú hengert az Aspose.3D .NET-hez
url: /hu/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Testreszabott Vágott Aljú Henger

## Bevezetés
Üdvözöljük átfogó útmutatónkban, ahol **meg fogja tanulni, hogyan hozzon létre vágott aljú henger** modelleket az Aspose.3D for .NET segítségével. Akár játékeszközt, akár mechanikai alkatrészt, vagy vizuális demót épít, ez a tutorial pontosan megmutatja, hogyan formálja meg a henger alját, alkalmazzon vágást, és végül **exportálja a 3D modell OBJ** fájlt bármely további csővezetékhez. Lépjünk végig együtt minden lépésen, hogy percek alatt testreszabott geometriát tudjon előállítani.

## Gyors válaszok
- **Mi az a vágott aljú henger?** Egy henger, amelynek alulja ferde (vágott), nem pedig sík.  
- **Melyik könyvtárat használja?** Aspose.3D for .NET.  
- **Hogyan exportálom a modellt?** Használja a `scene.Save(..., FileFormat.WavefrontOBJ)` metódust.  
- **Szükségem van licencre?** Elérhető próba, a kereskedelmi licenc szükséges a termeléshez.  
- **Milyen előfeltételek szükségesek?** .NET fejlesztői környezet és az Aspose.3D NuGet csomag.

## Mi az a vágott aljú henger?
A vágott aljú henger egy szabványos hengeres háló, amelynek alulja egy vágási művelettel lett átalakítva. Ez lehetővé teszi szögletes alapok, rámpák vagy egyedi csatlakozók létrehozását anélkül, hogy kézzel szerkesztené a csúcsokat.

## Miért használja az Aspose.3D‑t ehhez a feladathoz?
- **Teljes irányítás** a geometriai paraméterek (sugár, magasság, szegmensek) felett.  
- **Beépített vágás támogatás** a `ShearBottom` tulajdonságon keresztül, amely megkíméli az alacsony szintű háló manipulációtól.  
- **Egykattintásos export** népszerű formátumokba, mint OBJ, FBX és STL, ami zökkenőmentessé teszi az integrációt más eszközökkel.

## Előfeltételek
Mielőtt belemerülnénk, győződjön meg róla, hogy rendelkezik:

- Alapvető C# és .NET ismeretekkel.  
- Telepített Aspose.3D for .NET. Letöltheti **[itt](https://releases.aspose.com/3d/net/)**.  
- .NET‑kompatibilis IDE‑vel (Visual Studio, Rider vagy VS Code).

## Névtér importálása
A C# fájlban kezdje a szükséges névterek importálásával:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## 1. lépés: Jelenet létrehozása
Először hozzon létre egy új 3‑D jelenetet, amely tartalmazni fogja az összes objektumot.

```csharp
Scene scene = new Scene();
```

## 2. lépés: Henger 1 létrehozása
Hozza létre az elsődleges hengert, amelyet a vágott aljával testreszabunk.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## 3. lépés: Vágott alj testreszabása a Henger 1‑hez
Alkalmazza a vágást, engedélyezze a szélvédő-generálást, és állítsa be a többi tulajdonságot a kívánt forma eléréséhez.

```csharp
// Shear 47.5deg in the xy plane (z‑axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## 4. lépés: Henger 1 hozzáadása a jelenethez
Helyezze el a testreszabott hengert a jelenetben, és mozgassa egy kicsit jobbra, hogy mindkét objektumot egymás mellett láthassuk.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## 5. lépés: Henger 2 létrehozása
Hozzon létre egy második, egyszerű hengert összehasonlítás céljából.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## 6. lépés: Henger 2 hozzáadása a jelenethez
Adja hozzá a második hengert egyedi vágás nélkül – ez segít bemutatni az előző lépések hatását.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## 7. lépés: Jelenet mentése
Végül exportálja az egész jelenetet OBJ fájlként, hogy megnyithassa Blenderben, Mayában vagy bármely más 3‑D megjelenítőben.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## Gyakori problémák és tippek
- **Vágási értékek**: A `Vector2` X és Y vágási tényezőket vesz fel. A `0.83` érték nagyjából 47,5°-nek felel meg, de különböző szögekhez módosítható.  
- **Export útvonal**: Győződjön meg róla, hogy a megadott mappa létezik és van írási jogosultsága; ellenkező esetben a `scene.Save` kivételt dob.  
- **Teljesítmény**: Nagyon sok szegmensű hengerek esetén fontolja meg a szegmens szám csökkentését (`20` a példában), hogy az OBJ fájl mérete kezelhető maradjon.

## Gyakran ismételt kérdések

### Alkalmas-e az Aspose.3D for .NET kezdőknek?
Teljesen! Az Aspose.3D for .NET felhasználóbarát API‑t kínál, amely mind a kezdők, mind a tapasztalt fejlesztők számára hozzáférhető.

### Alkalmazhatok különböző vágási szögeket a hengerekre?
Igen, egyenként testreszabhatja a `ShearBottom` értékét minden hengerhez, így egyedi hatásokat érhet el.

### Elérhető-e próba verzió?
Igen, a ingyenes próba verziót **[itt](https://releases.aspose.com/)** tekintheti meg.

### Hol találok további támogatást?
Látogassa meg az **[Aspose.3D fórumot](https://forum.aspose.com/c/3d/18)** a közösségi támogatás és megbeszélések érdekében.

### Hogyan szerezhetek ideiglenes licencet?
Szerezze meg ideiglenes licencét **[itt](https://purchase.aspose.com/temporary-license/)**.

**További kérdések és válaszok**

**Q: Hogyan változtathatom meg az export formátumot FBX‑re?**  
A: Cserélje le a `FileFormat.WavefrontOBJ`-t `FileFormat.FBX`-re a `scene.Save` hívásban.

**Q: Animálhatom a hengert export után?**  
A: Az OBJ nem támogat animációt; használjon FBX‑et vagy GLTF‑et, ha animált adat szükséges.

**Q: Mi a teendő, ha nagyobb henger sugárra van szükség?**  
A: Állítsa be a `Cylinder` konstruktor első két paraméterét (pl. `new Cylinder(4, 4, …)`).

## Összegzés
Most már elsajátította, hogyan **hozzon létre vágott aljú henger** modelleket, és exportálja őket OBJ fájlként az Aspose.3D for .NET segítségével. Kísérletezzen különböző vágási értékekkel, szegmens számokkal és export formátumokkal, hogy megfeleljenek projektje igényeinek. Boldog modellezést!

---

**Utolsó frissítés:** 2026-01-12  
**Tesztelve:** Aspose.3D for .NET 24.11 (a legújabb a kiadás időpontjában)  
**Szerző:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}