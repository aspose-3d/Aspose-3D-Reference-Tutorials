---
title: Ventilátorhenger létrehozása
linktitle: Ventilátorhenger létrehozása
second_title: Aspose.3D .NET API
description: Fedezze fel a 3D-s tervezés világát az Aspose.3D for .NET segítségével! Lenyűgöző ventilátoros és nem ventilátoros hengereket készíthet könnyedén. Töltse le most a próbaverziót.
type: docs
weight: 10
url: /hu/net/working-with-cylinder/create-fan-cylinder/
---
## Bevezetés
Üdvözöljük a 3D modellezés és vizualizáció világában az Aspose.3D for .NET segítségével! Ebben a lépésenkénti útmutatóban megvizsgáljuk, hogyan hozhat létre lenyűgöző ventilátorhengert az Aspose.3D for .NET használatával. Az Aspose.3D egy hatékony könyvtár, amely kiterjedt lehetőségeket biztosít a .NET-alkalmazások 3D-s tartalommal való munkához.
## Előfeltételek
Mielőtt belevetnénk magunkat a 3D modellezés izgalmas világába, győződjön meg arról, hogy rendelkezik a következő előfeltételekkel:
- A .NET programozás alapvető ismerete.
- A Visual Studio telepítve van a gépedre.
-  Aspose.3D for .NET könyvtár, amelyet letölthet[itt](https://releases.aspose.com/3d/net/).
- Őszinte érdeklődés a kreativitás felszabadítása iránt a 3D tervezésen keresztül.
## Névterek importálása
Kezdjük a dolgokkal a szükséges névterek importálásával, hogy az Aspose.3D funkcionalitás elérhetővé váljon a .NET-projektben.
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
// Importálja az Aspose.3D névtereket
```
Most, hogy készen vagyunk, bontsuk le a ventilátorhenger létrehozásának folyamatát kezelhető lépésekre.
## 1. lépés: Hozzon létre egy jelenetet
```csharp
// Hozzon létre egy jelenetet
Scene scene = new Scene();
```
Kezdje egy új 3D-s jelenet inicializálásával. Ez a vászon, ahol a ventilátorhengerünk életre kel.
## 2. lépés: Hozzon létre egy ventilátorhengert
```csharp
// Hozzon létre egy hengert
var fan = new Cylinder(2, 2, 10, 20, 1, false);
```
Határozza meg ventilátorhengerének jellemzőit, olyan paraméterek megadásával, mint a sugár, magasság és felbontás.
## 3. lépés: A ventilátorhenger tulajdonságainak testreszabása
```csharp
// Állítsa igazra a GenerateFanCylinder-t
fan.GenerateFanCylinder = true;
// Állítsa be a ThetaLength-et
fan.ThetaLength = MathUtils.ToRadian(270);
```
Szabja testre ventilátorhengerét azáltal, hogy engedélyezi a ventilátorrész generálását, és állítsa be a szöglefutást a ThetaLength segítségével.
## 4. lépés: Helyezze el a ventilátorhengert a jelenetben
```csharp
// Hozzon létre ChildNode
scene.RootNode.CreateChildNode(fan).Transform.Translation = new Vector3(10, 0, 0);
```
Adja hozzá a ventilátorhengert gyermekcsomópontként a jelenet gyökércsomópontjához, és helyezze el a 3D térben.
## 5. lépés: Hozzon létre egy nem ventilátor hengert
```csharp
// Hozzon létre egy hengert ventilátor nélkül
var nonfan = new Cylinder(2, 2, 10, 20, 1, false);
```
Fedezze fel az Aspose.3D rugalmasságát egy ventilátorrész nélküli henger létrehozásával.
## 6. lépés: A nem ventilátor henger tulajdonságainak testreszabása
```csharp
// Állítsa a GenerateFanCylinder-t false értékre
nonfan.GenerateFanCylinder = false;
// Állítsa be a ThetaLength-et
nonfan.ThetaLength = MathUtils.ToRadian(270);
```
A ventilátor rész generálásának letiltásával különböztesse meg a nem ventilátor hengert.
## 7. lépés: Helyezze el a nem ventilátor hengert a jelenetben
```csharp
// Hozzon létre ChildNode
scene.RootNode.CreateChildNode(nonfan);
```
Hasonlóképpen adja hozzá a nem ventilátor hengert gyermekcsomópontként a jelenet gyökércsomópontjához.
## 8. lépés: Mentse el a jelenetet
```csharp
// Jelenet mentése
scene.Save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WavefrontOBJ);
```
Mentse el remekművét a kívánt formátumban és helyen. Sikeresen létrehozott egy ventilátor és nem ventilátor hengert az Aspose.3D for .NET használatával!
## Következtetés
Gratulálunk az Aspose.3D for .NET 3D-s modellezés gyakorlati útmutatójának elkészítéséhez! Felszabadította kreativitását a digitális világban, könnyedén készíthet ventilátort és nem ventilátor hengereket.
## Gyakran Ismételt Kérdések
### Használhatom az Aspose.3D for .NET fájlt más .NET keretrendszerekkel?
Igen, az Aspose.3D kompatibilis a különböző .NET keretrendszerekkel, sokoldalúságot biztosítva a fejlesztési projektekben.
### Létezik ingyenes próbaverzió az Aspose.3D for .NET számára?
 Igen, felfedezheti az ingyenes próbaverziót[itt](https://releases.aspose.com/).
### Hol találom az Aspose.3D for .NET részletes dokumentációját?
 A dokumentáció elérhető[itt](https://reference.aspose.com/3d/net/).
### Hogyan kaphatok támogatást az Aspose.3D for .NET-hez?
 Látogassa meg a támogatási fórumot[itt](https://forum.aspose.com/c/3d/18) közösség és az Aspose szakértői segítségért.
### Rendelkezésre állnak ideiglenes licencek az Aspose.3D for .NET számára?
 Igen, ideiglenes engedélyeket lehet szerezni[itt](https://purchase.aspose.com/temporary-license/).