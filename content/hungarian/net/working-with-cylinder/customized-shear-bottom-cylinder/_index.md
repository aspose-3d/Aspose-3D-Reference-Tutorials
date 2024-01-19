---
title: Testreszabott nyíró alsó henger
linktitle: Testreszabott nyíró alsó henger
second_title: Aspose.3D .NET API
description: Ismerje meg, hogyan hozhat létre testreszabott nyírófenékhengereket az Aspose.3D for .NET használatával a részletes, lépésenkénti útmutatónk segítségével. Növelje 3D modellezési készségeit még ma!
type: docs
weight: 12
url: /hu/net/working-with-cylinder/customized-shear-bottom-cylinder/
---
## Bevezetés
Üdvözöljük átfogó útmutatónkban, amely az Aspose.3D for .NET-hez készült testreszabott nyírófenékhenger létrehozásáról szól. Ha fejleszteni szeretné 3D modellezési készségeit, és egyedi funkciókat szeretne hozzáadni projektjeihez, akkor jó helyen jár. Ebben az oktatóanyagban lépésről lépésre végigvezetjük a folyamaton, világos magyarázatok és kódrészletek segítségével.
## Előfeltételek
Mielőtt belevágnánk az oktatóanyagba, győződjön meg arról, hogy rendelkezik a következőkkel:
- A C# és .NET programozás alapvető ismerete.
-  Aspose.3D for .NET könyvtár telepítve. Letöltheti[itt](https://releases.aspose.com/3d/net/).
- NET programozáshoz beállított fejlesztői környezet.
## Névterek importálása
C# kódban kezdje a szükséges névterek importálásával:
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
Kezdje egy 3D-s jelenet létrehozásával az Aspose.3D segítségével:
```csharp
Scene scene = new Scene();
```
## 2. lépés: Hozzon létre 1. hengert
Készítse elő az első hengert, és állítsa be a tulajdonságait:
```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
## 3. lépés: A nyírófenék testreszabása az 1. hengerhez
Alkalmazzon testreszabott nyírófenéket az első hengerre:
```csharp
cylinder1.ShearBottom = new Vector2(0, 0.83); // Nyírás 47,5 fok az xy síkban (z tengely)
```
## 4. lépés: Adja hozzá az 1. hengert a jelenethez
Adja hozzá az első hengert a jelenethez, és állítsa be a fordítását:
```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
## 5. lépés: Hozza létre a 2. hengert
Hozzon létre egy második hengert hasonló tulajdonságokkal:
```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
## 6. lépés: Adja hozzá a 2. hengert a jelenethez
Adja hozzá a második hengert a jelenethez nyírófenék nélkül:
```csharp
scene.RootNode.CreateChildNode(cylinder2);
```
## 7. lépés: Mentse el a jelenetet
Mentse el a jelenetet Wavefront OBJ fájlként a dokumentumkönyvtárba:
```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```
## Következtetés
Gratulálunk! Sikeresen létrehozott egy testreszabott nyíró alsó hengert az Aspose.3D for .NET használatával. Ennek az oktatóanyagnak az volt a célja, hogy lépésről lépésre útmutatót nyújtson a 3D modellezés és programozás terén különböző szintű szakértelemmel rendelkező felhasználók számára.
## Gyakran Ismételt Kérdések
### Az Aspose.3D for .NET megfelelő kezdőknek?
Teljesen! Az Aspose.3D for .NET felhasználóbarát felületet kínál, így kezdők és tapasztalt fejlesztők számára is elérhető.
### Alkalmazhatok különböző nyírási szögeket a hengerekre?
Igen, minden hengerhez egyénileg testreszabhatja a nyírófenekét, így egyedi hatásokat érhet el.
### Létezik próbaverzió?
 Igen, felfedezheti az ingyenes próbaverziót[itt](https://releases.aspose.com/).
### Hol találhatok további támogatást?
 Meglátogatni a[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) közösségi támogatásra és beszélgetésekre.
### Hogyan szerezhetek ideiglenes engedélyt?
 Szerezze meg ideiglenes engedélyét[itt](https://purchase.aspose.com/temporary-license/).