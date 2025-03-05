---
title: Egyedi betöltési beállítások
linktitle: Egyedi betöltési beállítások
second_title: Aspose.3D .NET API
description: Fedezze fel a .NET-hez készült Aspose.3D-t, amely a tökéletes megoldás a 3D-s modellek zökkenőmentes betöltésére és mentésére.
type: docs
weight: 15
url: /hu/net/loading-and-saving/custom-load-options/
---
## Bevezetés

Üdvözöljük az Aspose.3D for .NET világában – egy hatékony könyvtár, amely képessé teszi a fejlesztőket a 3D fájlokkal való zökkenőmentes munkavégzésre. Ebben az oktatóanyagban a 3D-s modellek betöltésének és mentésének bonyolultságába fogunk beleásni, az egyéni betöltési lehetőségekre összpontosítva. Akár tapasztalt fejlesztő, akár újonc, ez az útmutató lépésről lépésre végigvezeti a folyamaton, biztosítva, hogy az Aspose.3D for .NET teljes potenciálját kihasználja.

## Előfeltételek

Mielőtt nekivágnánk ennek az útnak, győződjön meg arról, hogy a következő előfeltételeket teljesíti:

-  Aspose.3D for .NET: Győződjön meg arról, hogy a könyvtár telepítve van. Letöltheti[itt](https://releases.aspose.com/3d/net/).

- Dokumentumkönyvtár: Hozzon létre egy könyvtárat a 3D modellfájlok tárolására.

Most, hogy megvan a legfontosabb dolog, merüljünk el a 3D-s modellmanipuláció izgalmas világában!

## Névterek importálása

Először is importáljuk a szükséges névtereket. Ez megteremti a terepet az Aspose.3D birodalmába vezető utazásunkhoz.

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
```

## Betöltés és mentés - Egyéni betöltési lehetőségek

### 1. lépés: Discreet3DS fájlok betöltése

```csharp
private static void Discreet3DSLoadOption()
{
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();

    //Állítson be egyéni beállításokat
    loadOpts.ApplyAnimationTransform = true;
    loadOpts.FlipCoordinateSystem = true;
    loadOpts.GammaCorrectedColor = true;
    loadOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Fájl betöltése a betöltési beállításokkal
    var scene = Scene.FromFile("test.3ds", loadOpts);
}
```

### 2. lépés: OBJ fájlok betöltése

```csharp
private static void ObjLoadOption()
{
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();

    //Állítson be egyéni beállításokat
    loadObjOpts.EnableMaterials = true;
    loadObjOpts.FlipCoordinateSystem = true;
    loadObjOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Fájl betöltése a betöltési beállításokkal
    var scene = Scene.FromFile("test.obj", loadObjOpts);

}
```

### 3. lépés: STL fájlok betöltése

```csharp
private static void STLLoadOption()
{
    // A dokumentumok könyvtárának elérési útja.
    StlLoadOptions loadSTLOpts = new StlLoadOptions();

    //Állítson be egyéni beállításokat
    loadSTLOpts.FlipCoordinateSystem = true;
    loadSTLOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Fájl betöltése a betöltési beállításokkal
    var scene = Scene.FromFile("test.stl", loadSTLOpts);
}
```

### 4. lépés: U3D fájlok betöltése

```csharp
private static void U3DLoadOption()
{
    // A dokumentumok könyvtárának elérési útja.
    string dataDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();

    //Állítson be egyéni beállításokat
    loadU3DOpts.FlipCoordinateSystem = true;
    loadU3DOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Fájl betöltése a betöltési beállításokkal
    var scene = Scene.FromFile("test.u3d", loadU3DOpts);
}
```

### 5. lépés: glTF fájlok betöltése

```csharp
private static void glTFLoadOptions()
{
    // A dokumentumok könyvtárának elérési útja.
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();

    //Állítson be egyéni beállításokat
    loadOpt.FlipTexCoordV = true;
    scene.Open("Duck.gltf", loadOpt);
}
```

### 6. lépés: PLY fájlok betöltése

```csharp
private static void PlyLoadOptions()
{
    // A dokumentumok könyvtárának elérési útja.
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();

    //Állítson be egyéni beállításokat
    loadPLYOpts.FlipCoordinateSystem = true;
    scene.Open("vase-v2.ply", loadPLYOpts);
}
```

### 7. lépés: FBX fájlok betöltése

```csharp
private static void FBXLoadOptions()
{
    // A dokumentumok könyvtárának elérési útja.
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions() { KeepBuiltinGlobalSettings = true };

    //Állítson be egyéni beállításokat
    scene.Open("test.FBX", opt);

    // A GlobalSettingsben meghatározott kimeneti tulajdonságok az FBX fájlban
    foreach (Property property in scene.RootNode.AssetInfo.Properties)
    {
        Console.WriteLine(property);
    }
}
```

## Következtetés

Gratulálunk! Sikeresen navigált a 3D modellek betöltésének és mentésének bonyolult világában az Aspose.3D for .NET használatával. Ez az oktatóanyag különféle fájlformátumokat és azok egyéni betöltési lehetőségeit ismerteti, lehetővé téve a 3D-s eszközök egyszerű kezelését.

## GYIK

### 1. kérdés: Az Aspose.3D for .NET megfelelő kezdőknek?

A1: Abszolút! Az Aspose.3D for .NET felhasználóbarát felületet biztosít, így minden szintű fejlesztő számára elérhető.

### 2. kérdés: Használhatom az Aspose.3D-t kereskedelmi projektekhez?

2. válasz: Igen, az Aspose.3D for .NET kereskedelmi licenccel rendelkezik, amely lehetővé teszi a projektekben való használatát.

### 3. kérdés: Vannak-e korlátozások a támogatott fájlformátumokra vonatkozóan?

 3. válasz: Az Aspose.3D for .NET a népszerű 3D fájlformátumok széles skáláját támogatja, beleértve az OBJ, STL, FBX és egyebeket. Utal[dokumentáció](https://reference.aspose.com/3d/net/) átfogó listáért.

### 4. kérdés: Elérhető-e próbaverzió?

4. válasz: Igen, felfedezheti az Aspose.3D for .NET képességeit, ha letölti a[ingyenes próbaverzió](https://releases.aspose.com/).

### 5. kérdés: Hol kérhetek támogatást az Aspose.3D for .NET-hez?

 A5: Látogassa meg a[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) közösségi támogatásért és segítségért.