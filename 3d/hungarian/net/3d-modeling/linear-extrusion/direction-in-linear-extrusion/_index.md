---
title: Irány a lineáris extrudálásban
linktitle: Irány a lineáris extrudálásban
second_title: Aspose.3D .NET API
description: Fedezze fel a 3D modellezés világát az Aspose.3D for .NET segítségével. Tanulja meg az irányvonalas lineáris extrudálást, fokozza a kreativitást, és könnyedén készítsen magával ragadó alkalmazásokat.
type: docs
weight: 11
url: /hu/net/3d-modeling/linear-extrusion/direction-in-linear-extrusion/
---
## Bevezetés

A szoftverfejlesztés dinamikus világában a magával ragadó 3D-s modellek készítése nélkülözhetetlen készség. Az Aspose.3D for .NET robusztus eszközkészletet biztosít a fejlesztők számára, amelyekkel kiaknázhatják alkalmazásaikban a 3D modellezésben rejlő lehetőségeket. Ebben az oktatóanyagban elmélyülünk a lineáris extrudálás izgalmas világában, és felfedezzük az „Irány a lineáris extrudálásban” funkció árnyalatait.

## Előfeltételek

Mielőtt nekivágnánk ennek az izgalmas utazásnak, győződjön meg arról, hogy a következő előfeltételeket teljesíti:

-  Aspose.3D for .NET: Töltse le és telepítse a könyvtárat innen[Aspose.3D .NET dokumentáció](https://reference.aspose.com/3d/net/).

- Fejlesztői környezet: Győződjön meg arról, hogy be van állítva egy működő .NET fejlesztői környezet.

## Névterek importálása

.NET-projektben importálja a szükséges névtereket az Aspose.3D funkcióinak eléréséhez. Adja hozzá a következő sorokat a kód elejéhez:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## 1. lépés: Inicializálja az alapprofilt

Kezdje az extrudálandó alapprofil inicializálásával. Ebben a példában 0,3-as lekerekítési sugarú téglalap alakot hozunk létre.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## 2. lépés: Hozzon létre egy 3D-s jelenetet

Építse meg 3D-s remekműve alapját egy jelenet létrehozásával.

```csharp
Scene scene = new Scene();
```

## 3. lépés: Hozzon létre csomópontokat

Hozzon létre csomópontokat a jeleneten belül a 3D környezet különböző összetevőinek megjelenítéséhez.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(8, 0, 0);
```

## 4. lépés: Lineáris extrudálás irány nélkül

 Végezzen lineáris extrudálást a bal oldali csomóponton a`Twist` és`Slices` tulajdonságait.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## 5. lépés: Lineáris extrudálás iránnyal

 Bővítse ki az extrudálási lehetőségeket a`Direction` tulajdonság a jobb csomópontban.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, Direction = new Vector3(0.3, 0.2, 1) });
```

## 6. lépés: Mentse el a 3D-s jelenetet

 Őrizze meg alkotásait a 3D-s jelenet mentésével. Cserélje ki`"Your Output Directory"` a kívánt könyvtárral.

```csharp
scene.Save("Your Output Directory" + "DirectionInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Gratulálunk! Sikeresen megvalósította a lineáris extrudálást az Aspose.3D for .NET segítségével, amely mind a hagyományos, mind az irányított megközelítést feltárja.

## Következtetés

Ebben az oktatóanyagban a 3D modellezés lenyűgöző birodalmában navigáltunk az Aspose.3D for .NET használatával. A lineáris extrudálás irányokkal és anélkül végtelen lehetőségeket nyit a fejlesztők számára, akik vizuálisan lenyűgöző alkalmazásokat szeretnének létrehozni. Az Aspose.3D segítségével a 3D modellezés ereje karnyújtásnyira van.

## GYIK

### 1. kérdés: Hogyan szerezhetek ideiglenes licencet az Aspose.3D for .NET számára?

 A1: Látogassa meg[Aspose ideiglenes engedélye](https://purchase.aspose.com/temporary-license/) ideiglenes engedély megszerzéséhez.

### 2. kérdés: Hol találok támogatást az Aspose.3D-hez?

 A2: Csatlakozzon a[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) segítséget kérni és kapcsolatba lépni a közösséggel.

### 3. kérdés: Van ingyenes próbaverzió?

 3. válasz: Igen, fedezze fel a funkciókat egy ingyenes próbaverzióval a címen[Aspose.3D kiadások](https://releases.aspose.com/).

### 4. kérdés: Hogyan vásárolhatom meg az Aspose.3D-t .NET-hez?

 A4: Navigáljon a[Aspose vásárlási oldal](https://purchase.aspose.com/buy) az engedélyezési lehetőségekről és a vásárlás részleteiről.

### 5. kérdés: Hol találom az Aspose.3D for .NET részletes dokumentációját?

 V5: Lásd az átfogót[Aspose.3D .NET dokumentáció](https://reference.aspose.com/3d/net/) mélyreható tájékoztatásért.