---
title: Középpontja a lineáris extrudálásban
linktitle: Középpontja a lineáris extrudálásban
second_title: Aspose.3D .NET API
description: Fedezze fel a 3D modellezés világát az Aspose.3D for .NET segítségével. Középre állítsa a lineáris extrudálási technikákat, készítsen lenyűgöző terveket, és engedje szabadjára kreativitását.
type: docs
weight: 10
url: /hu/net/linear-extrusion/center-in-linear-extrusion/
---
## Bevezetés

Üdvözöljük ebben az átfogó útmutatóban a lineáris extrudálás elsajátításáról az Aspose.3D for .NET használatával. Ha 3D modellezési készségeit szeretné fejleszteni, és lenyűgöző extrudálásokat szeretne készíteni, akkor jó helyen jár. Ebben az oktatóanyagban a lineáris extrudálási technikával foglalkozunk, különös tekintettel a központosítási szempontra, hogy a terveket egy teljesen új szintre emeljük.

## Előfeltételek

Mielőtt nekivágnánk ennek az izgalmas utazásnak, győződjön meg arról, hogy a következő előfeltételeket teljesíti:

- A C# programozási nyelv alapvető ismerete.
- A Visual Studio telepítve van a gépedre.
-  Aspose.3D for .NET könyvtár, amely letölthető a[Aspose.3D .NET dokumentáció](https://reference.aspose.com/3d/net/).
-  Győződjön meg arról, hogy rendelkezik hozzáféréssel a[Aspose.3D .NET dokumentáció](https://reference.aspose.com/3d/net/) referenciaként az oktatóanyagban.

## Névterek importálása

A dolgok elindításához importáljuk a szükséges névtereket. Ezek alapozzák meg 3D modellezési remekművünket.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## 1. lépés: Inicializálja az alapprofilt

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## 2. lépés: Hozzon létre egy 3D-s jelenetet

```csharp
Scene scene = new Scene();
```

## 3. lépés: Hozzon létre bal és jobb csomópontokat

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## 4. lépés: Hajtsa végre a lineáris extrudálást a bal csomóponton

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## 5. lépés: Állítsa be a talajsíkot referenciaként

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## 6. lépés: Hajtsa végre a lineáris extrudálást a jobb oldali csomóponton

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## 7. lépés: Állítsa be a talajsíkot referenciaként (jobb oldali csomópont)

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## 8. lépés: 3D-s jelenet mentése

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Következtetés

Gratulálunk! Sikeresen elsajátította a lineáris extrudálás művészetét a központosítással az Aspose.3D for .NET használatával. Nyugodtan kísérletezzen a különböző paraméterekkel, és fedezze fel a technika által kínált hatalmas lehetőségeket.

## GYIK

### 1. kérdés: Használhatom az Aspose.3D for .NET fájlt más programozási nyelvekkel?

1. válasz: Az Aspose.3D elsősorban a .NET nyelveket támogatja, mint például a C# és a VB.NET.

### 2. kérdés: Hol találok támogatást az Aspose.3D-vel kapcsolatos lekérdezésekhez?

 A2: Látogassa meg a[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) elkötelezett támogatásért és megbeszélésekért.

### 3. kérdés: Elérhető ingyenes próbaverzió az Aspose.3D for .NET számára?

 3. válasz: Igen, hozzáférhet az ingyenes próbaverzióhoz[itt](https://releases.aspose.com/).

### 4. kérdés: Hogyan szerezhetek ideiglenes licencet az Aspose.3D for .NET számára?

 V4: Kaphat ideiglenes engedélyt[itt](https://purchase.aspose.com/temporary-license/).

### 5. kérdés: Hol vásárolhatom meg az Aspose.3D for .NET licencet?

 V5: Vásárolja meg a licencét[itt](https://purchase.aspose.com/buy).
