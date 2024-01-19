---
title: Egyedi eltolásos felső henger
linktitle: Egyedi eltolásos felső henger
second_title: Aspose.3D .NET API
description: Fedezze fel a 3D-s grafika csodáit az Aspose.3D for .NET segítségével. Tanuljon meg könnyedén létrehozni testreszabott eltolt felső hengereket. Növelje kódolási élményét most!
type: docs
weight: 11
url: /hu/net/working-with-cylinder/customized-offset-top-cylinder/
---
## Bevezetés
Üdvözöljük a 3D grafikus manipuláció világában az Aspose.3D for .NET segítségével! Ebben az oktatóanyagban végigvezetjük a testreszabott eltolt felső henger létrehozásának folyamatán az Aspose.3D segítségével, amely egy hatékony könyvtár a 3D-s jelenetekkel, objektumokkal és formátumokkal való munkavégzéshez .NET-alkalmazásokban.
## Előfeltételek
Mielőtt belevágnánk az oktatóanyagba, győződjön meg arról, hogy rendelkezik a következő előfeltételekkel:
- C# programozási nyelv alapismerete.
- A Visual Studio telepítve van a gépedre.
- Aspose.3D for .NET könyvtár letöltve és hivatkozva a projektben.
Most pedig kezdjük a lépésről lépésre bemutatott útmutatóval!
## Névterek importálása
Először is importálja a szükséges névtereket a C# kódba:
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
## 1. lépés: Hozzon létre egy jelenetet
```csharp
// Hozzon létre egy jelenetet
Scene scene = new Scene();
```
Ez egy új 3D-s jelenetet inicializál az Aspose.3D használatával.
## 2. lépés: Inicializálja a hengert
```csharp
// Inicializálja a hengert
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
Itt létrehozunk egy hengert meghatározott paraméterekkel, például sugárral, magassággal és szeletekkel.
## 3. lépés: Állítsa be az OffsetTop értéket az első hengerhez
```csharp
// Állítsa be az OffsetTop beállítást
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```
Ezzel testreszabott eltolási csúcsot állít be az első hengerhez.
## 4. lépés: Hozzon létre ChildNode-ot az első hengerhez
```csharp
// Hozzon létre ChildNode
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
Az első hengert gyermekcsomópontként adjuk hozzá a jelenethez, módosítva a helyzetét.
## 5. lépés: Inicializálja a második hengert
```csharp
// második henger inicializálása testreszabott OffsetTop nélkül
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
Egy második henger inicializálása egyedi eltolt tető nélkül történik.
## 6. lépés: Hozzon létre ChildNode-ot a második hengerhez
```csharp
// Hozzon létre ChildNode
scene.RootNode.CreateChildNode(cylinder2);
```
A második hengert gyermekcsomópontként adjuk hozzá a jelenethez.
## 7. lépés: Mentse el a jelenetet
```csharp
// Megment
scene.Save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WavefrontOBJ);
```
Ez a 3D-s jelenetet, beleértve a testreszabott eltolásos felső hengert is, Wavefront OBJ formátumba menti.
Sikeresen létrehozott egy testreszabott eltolt felső hengert az Aspose.3D for .NET segítségével!
## Következtetés
Ebben az oktatóanyagban megvizsgáltuk az Aspose.3D for .NET-hez való használatának alapjait, hogy testreszabott eltolt felső hengert hozzon létre. Ez a könyvtár végtelen lehetőségeket nyit meg a .NET-alkalmazásokon belüli 3D grafikus manipulációhoz.
## GYIK
### K: Hol találom az Aspose.3D for .NET dokumentációját?
 V: A dokumentáció elérhető[itt](https://reference.aspose.com/3d/net/).
### K: Hogyan tölthetem le az Aspose.3D-t .NET-hez?
 V: Letöltheti[itt](https://releases.aspose.com/3d/net/).
### K: Elérhető ingyenes próbaverzió az Aspose.3D for .NET számára?
 V: Igen, ingyenes próbaverziót kaphat[itt](https://releases.aspose.com/).
### K: Hol kaphatok támogatást az Aspose.3D for .NET-hez?
 V: Látogassa meg a[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) támogatásért.
### K: Kaphatok ideiglenes licencet az Aspose.3D for .NET számára?
 V: Igen, kaphat ideiglenes engedélyt[itt](https://purchase.aspose.com/temporary-license/).