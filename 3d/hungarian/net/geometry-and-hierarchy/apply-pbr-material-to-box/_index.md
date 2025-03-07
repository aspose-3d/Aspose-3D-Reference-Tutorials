---
title: PBR anyag felvitele a dobozra
linktitle: PBR anyag felvitele a dobozra
second_title: Aspose.3D .NET API
description: Fedezze fel a 3D grafika világát az Aspose.3D for .NET segítségével. Hozzon létre magával ragadó jeleneteket erőfeszítés nélkül a fizikai alapú renderelő anyagok segítségével.
weight: 10
url: /hu/net/geometry-and-hierarchy/apply-pbr-material-to-box/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# PBR anyag felvitele a dobozra

## Bevezetés

Üdvözöljük a 3D grafika lenyűgöző világában! Ebben a lépésről lépésre bemutatjuk a hatékony Aspose.3D for .NET könyvtárat, és megtanuljuk, hogyan készítsünk lenyűgöző 3D-s jeleneteket fizikai alapú renderelés (PBR) anyagok segítségével. Az Aspose.3D leegyszerűsíti a 3D grafika összetett folyamatát, és lehetőségek tárházát nyitja meg a fejlesztők előtt.

## Előfeltételek

Mielőtt belevetnénk magunkat a 3D grafika izgalmas világába, győződjünk meg arról, hogy mindent beállítottunk:

### Töltse le és telepítse az Aspose.3D for .NET fájlt

 Meglátogatni a[Aspose.3D .NET dokumentációhoz](https://reference.aspose.com/3d/net/) a könyvtár letöltésével és telepítésével kapcsolatos részletes utasításokért.

### Szerezzen licencet

Az Aspose.3D teljes potenciáljának kiaknázásához szerezzen be érvényes licencet. Kaphat ideiglenes engedélyt[itt](https://purchase.aspose.com/temporary-license/) vagy vásároljon teljes licencet[itt](https://purchase.aspose.com/buy).

## Névterek importálása

Először is importálja a szükséges névtereket, hogy kihasználja az Aspose.3D for .NET képességeit:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## 1. lépés: Inicializáljon egy jelenetet

Kezdje a 3D-s jelenet inicializálásával a következő kódrészlet segítségével:

```csharp
Scene scene = new Scene();
```

## 2. lépés: Inicializálja a PBR-anyagot

Hozzon létre egy PBR anyagobjektumot a valósághű megjelenítés érdekében:

```csharp
PbrMaterial mat = new PbrMaterial();
```

## 3. lépés: Állítsa be az anyag tulajdonságait

Finomítsa az anyag tulajdonságait, hogy szinte fémessé és nagyon durvává tegye:

```csharp
mat.MetallicFactor = 0.9;
mat.RoughnessFactor = 0.9;
```

## 4. lépés: Hozzon létre egy dobozt

Hozzon létre egy dobozt, amelyre a PBR anyagot alkalmazza:

```csharp
var boxNode = scene.RootNode.CreateChildNode("box", new Box());
```

## 5. lépés: Vigye fel az anyagot a dobozra

Rendelje hozzá a PBR-anyagot a létrehozott doboz csomóponthoz:

```csharp
boxNode.Material = mat;
```

## 6. lépés: Mentse el a 3D-s jelenetet

Mentse a 3D jelenetet STL formátumba a kívánt kimeneti könyvtárral:

```csharp
scene.Save("Your Output Directory" + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
```

Gratulálunk! Sikeresen felvitt egy PBR-anyagot egy dobozra egy 3D-s jelenetben az Aspose.3D for .NET használatával.

## Következtetés

Az Aspose.3D for .NET segítségével a 3D-s grafikákba való belemerészkedés végtelen kreatív lehetőségeket nyit meg. Intuitív API-jával és robusztus funkcióival a vizuálisan lenyűgöző jelenetek létrehozása élvezetes élménnyé válik a fejlesztők számára.

## GYIK

### 1. kérdés: Az Aspose.3D kompatibilis más 3D fájlformátumokkal?

1. válasz: Igen, az Aspose.3D támogatja a különféle 3D fájlformátumokat, biztosítva a projektek rugalmasságát.

### 2. kérdés: Használhatom az Aspose.3D-t kereskedelmi alkalmazásokhoz?

A2: Abszolút! Az Aspose.3D kereskedelmi licenceket biztosít az alkalmazásokba való zökkenőmentes integrációhoz.

### 3. kérdés: Elérhető próbaverzió?

 3. válasz: Igen, felfedezheti az Aspose.3D képességeit az ingyenes próbaverzió letöltésével[itt](https://releases.aspose.com/).

### 4. kérdés: Hol találok közösségi támogatást és megbeszéléseket?

 4. válasz: Csatlakozzon az Aspose.3D közösséghez a címen[Aspose.3D fórumok](https://forum.aspose.com/c/3d/18) támogatásért és megbeszélésekért.

### 5. kérdés: Hogyan szerezhetek ideiglenes licencet az Aspose.3D-hez?

 V5: Kaphat ideiglenes engedélyt[itt](https://purchase.aspose.com/temporary-license/) értékelési célokra.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
