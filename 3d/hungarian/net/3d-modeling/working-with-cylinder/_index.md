---
date: 2026-03-26
description: Tanulja meg, hogyan hozhat létre hengert és exportálhat OBJ fájlt az
  Aspose.3D for .NET segítségével. Ez a kezdőknek szóló útmutató lefedi a 3D-s jelenet
  beállítását és az OBJ exportálást.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: Hogyan készítsünk hengert ferde aljjal – Aspose.3D a .NET-hez
url: /hu/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hogyan hozzunk létre hengert ferde alappal – Aspose.3D for .NET

## Bevezetés
Ha azon gondolkodsz, **hogyan lehet hengert** létrehozni egy testreszabott ferde alappal egy .NET környezetben, jó helyen jársz. Ebben az útmutatóban minden lépést végigvezetünk – a 3‑D jelenet beállításától a végső modell OBJ fájlként való exportálásáig – hogy fejleszd *kezdő 3D modellezési* képességeidet a **Aspose.3D for .NET** segítségével.

## Gyors válaszok
- **Mi a fő osztály egy 3D modell indításához?** `Scene` hozza létre a gyökérkonténert minden geometriai elemnek.  
- **Melyik metódus exportálja a modellt OBJ‑ba?** `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Szükség van licencre a teszteléshez?** Ingyenes próba elérhető — lásd a próba linket a GYIK‑ban.  
- **Módosíthatom a ferde szöget?** Igen, állítsd be a `ShearBottom` értékét egy `Vector2` segítségével.  
- **Alkalmas-e kezdőknek?** Teljesen; az API elrejti az alacsony szintű hálókezelést.

## Mi az a 3D jelenet?
Egy *3D jelenet* egy hierarchikus konténer, amely minden geometriai entitást, fényt, kamerát és transzformációt tartalmaz. Az Aspose.3D `Scene` osztálya tiszta módot biztosít a modellek szervezésére és későbbi exportálására.

## Miért exportáljunk OBJ‑ba?
Az OBJ egy széles körben támogatott, szöveges alapú formátum, amelyet sok 3‑D alkalmazás (Blender, Maya, Unity) képes beolvasni. OBJ‑ba exportálva megoszthatod vagy tovább szerkesztheted a henger modelljeidet a .NET‑en kívül.

## Előfeltételek
Mielőtt belemerülnénk, győződj meg róla, hogy rendelkezel:

- Alapvető C# és .NET fejlesztési ismeretekkel.  
- **Aspose.3D for .NET** telepítve – letöltheted **[itt](https://releases.aspose.com/3d/net/)**.  
- Egy .NET IDE‑vel (Visual Studio, Rider vagy VS Code) készen állva a kódolásra.

## Namespace‑ek importálása
Először hozd be a szükséges namespace‑eket, hogy az API típusai felismerésre kerüljenek.

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

## 1. lépés: 3D jelenet létrehozása
A `Scene` objektum a modell hierarchiád gyökereként működik.

```csharp
Scene scene = new Scene();
```

## 2. lépés: Cylinder 1 létrehozása
Létrehozzuk az első hengert 2‑es sugárral, 10‑es magassággal és 20 radiális szegmenssel.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## 3. lépés: Shear Bottom testreszabása Cylinder 1‑hez
Alkalmazz ferde transzformációt, engedélyezd a fan‑cylinder generálást, és állíts be további tulajdonságokat a kívánt alak eléréséhez.

```csharp
// Shear 47.5deg in the xy plane (z-axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## 4. lépés: Cylinder 1 hozzáadása a jelenethez
Helyezd el az első hengert egy kényelmes pozícióba egy transzlációs transzformációval.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## 5. lépés: Cylinder 2 létrehozása
A második henger ugyanazokkal az alapméretekkel készül, de egyedi ferde beállítás nélkül – tökéletes a párhuzamos összehasonlításhoz.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## 6. lépés: Cylinder 2 hozzáadása a jelenethez
Egyszerűen csatoljuk a második hengert a jelenet gráfjához.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## 7. lépés: A jelenet exportálása OBJ fájlként
Végül mentsük el az egész jelenetet egy OBJ fájlba, hogy bármely szabványos 3‑D nézőben megnyitható legyen.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## Gyakori problémák és megoldások
| Probléma | Miért fordul elő | Megoldás |
|----------|------------------|----------|
| **OBJ fájl üres** | A jelenethez nincs geometria csatolva. | Győződj meg róla, hogy mindkét hengert hozzáadtad a `scene.RootNode`‑hoz. |
| **A ferde nem megfelelő** | A `ShearBottom` a szög tangensét várja. | Használd a `Math.Tan(angleInRadians)`‑t vagy a megadott `0.83` értéket ~47,5°‑hez. |
| **Fájlútvonal hibák** | Érvénytelen vagy hiányzó könyvtár. | Használd a `Path.Combine(Environment.CurrentDirectory, "CustomizedShearBottomCylinder.obj")`‑t. |

## Gyakran ismételt kérdések
### Alkalmas-e az Aspose.3D for .NET kezdőknek?
Teljesen! Az Aspose.3D for .NET magas szintű API‑t kínál, amely elrejti a matematikailag nehéz 3‑D modellezési részeket, így bárki számára könnyen használható.

### Alkalmazhatok különböző ferde szögeket a hengerekhez?
Igen, minden `Cylinder` példány saját `ShearBottom` tulajdonsággal rendelkezik, így egyedi szöget rendelhetsz minden objektumhoz.

### Elérhető-e próba verzió?
Igen, a ingyenes próba verziót **[itt](https://releases.aspose.com/)** tudod felfedezni.

### Hol találok további támogatást?
Látogasd meg az **[Aspose.3D fórumot](https://forum.aspose.com/c/3d/18)** közösségi segítségért, kódmintákért és megbeszélésekért.

### Hogyan szerezhetek ideiglenes licencet?
Az ideiglenes licencet **[itt](https://purchase.aspose.com/temporary-license/)** kaphatod meg.

**További Q&A**

**Q: Hogyan exportáljam a modellt más formátumba, például STL‑be?**  
A: Cseréld le a `FileFormat.WavefrontOBJ`‑t `FileFormat.STL`‑re a `scene.Save` hívásban.

**Q: Animálhatom a hengereket a létrehozás után?**  
A: Igen, kulcskocka‑animációkat adhatsz a node transzformációkhoz az Aspose.3D által biztosított `Animation` osztályokkal.

**Q: Támogatja-e az API a .NET Core‑t?**  
A: A könyvtár teljes mértékben kompatibilis a .NET Core‑dal, a .NET 5+‑tel és a .NET 6+‑tel.

---

**Utoljára frissítve:** 2026-03-26  
**Tesztelve a következővel:** Aspose.3D for .NET (legújabb kiadás)  
**Szerző:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}