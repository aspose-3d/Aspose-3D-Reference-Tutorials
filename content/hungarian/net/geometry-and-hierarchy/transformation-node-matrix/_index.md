---
title: Csomópont átalakítása transzformációs mátrix segítségével 3D-s jelenetekben
linktitle: Csomópont átalakítása transzformációs mátrix segítségével 3D-s jelenetekben
second_title: Aspose.3D .NET API
description: Könnyedén alakíthatja át a csomópontokat 3D-s jelenetekben az Aspose.3D for .NET használatával. Ismerje meg a csomópont-átalakításokat lépésről lépésre az oktatóanyag segítségével.
type: docs
weight: 21
url: /hu/net/geometry-and-hierarchy/transformation-node-matrix/
---
## Bevezetés

A 3D grafika és vizualizáció dinamikus birodalmában a jeleneten belüli objektumok manipulálásának képessége döntő szempont. Az Aspose.3D for .NET lehetővé teszi a fejlesztők számára, hogy zökkenőmentesen átalakítsák a csomópontokat transzformációs mátrixok segítségével, kreativitást és vezérlési réteget adva a 3D-s jelenetekhez. Ez az oktatóanyag lépésről lépésre végigvezeti Önt egy csomópont 3D-s jelenetben történő átalakításának folyamatán.

## Előfeltételek

Mielőtt belevágna az oktatóanyagba, győződjön meg arról, hogy a következő előfeltételeket teljesítette:

1.  Aspose.3D for .NET Library: Győződjön meg arról, hogy az Aspose.3D könyvtár telepítve van a .NET projektben. Letöltheti[itt](https://releases.aspose.com/3d/net/).

2. Fejlesztési környezet: Állítson be egy működő .NET fejlesztői környezetet, és ha még nem tette meg, hozzon létre egy új projektet, ahol végrehajtja az átalakításokat.

## Névterek importálása

Kezdje a szükséges névterek importálásával a .NET-projektbe. Ezek a névterek biztosítják a 3D-s jelenetkezelés alapvető osztályait és módszereit.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

Most, hogy áttekintettük az alapokat, bontsuk le az átalakítási folyamatot egy lépésről lépésre szóló útmutatóra.

## 1. lépés: Inicializálja a jelenetet és a csomópontot

```csharp
// ExStart:AddTransformationToNodeByTransformationMatrix
// Jelenetobjektum inicializálása
Scene scene = new Scene();

// Node osztály objektum inicializálása
Node cubeNode = new Node("cube");
```

Ebben a lépésben létrehozunk egy új 3D-s jelenetet és a jeleneten belül egy "kocka" nevű csomópontot.

## 2. lépés: Háló létrehozása és geometria beállítása

```csharp
// Hívja a Common class create mesh-t a sokszögépítő metódussal a hálópéldány beállításához
Mesh mesh = Common.CreateMeshUsingPolygonBuilder(); 

// Pontcsomópont a Mesh geometriára
cubeNode.Entity = mesh;
```

Itt generálunk egy hálót a poligonépítő módszerrel, és hozzárendeljük a csomóponthoz, meghatározva a kockánk geometriáját.

## 3. lépés: Állítsa be az egyéni fordítási mátrixot

```csharp
// Egyéni fordítási mátrix beállítása
cubeNode.Transform.TransformMatrix = new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
);        
```

Határozzon meg egy egyéni fordítási mátrixot a csomópontra alkalmazott konkrét transzformáció meghatározásához. Állítsa be a mátrix értékeit a kívánt transzformációhoz.

## 4. lépés: Csomópont hozzáadása a jelenethez

```csharp
// Adjon hozzá kockát a jelenethez
scene.RootNode.ChildNodes.Add(cubeNode);            
```

Szerelje be a kocka csomópontot a jelenetbe, így az a teljes 3D környezet részévé válik.

## 5. lépés: Mentse el a jelenetet

```csharp
// A dokumentumok könyvtárának elérési útja.
var output = "Your Output Directory" + "TransformationToNode.fbx";

//Mentse a 3D jelenetet a támogatott fájlformátumokba
scene.Save(output, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByTransformationMatrix
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

Adja meg a kimeneti könyvtárat és a fájlnevet, majd mentse a 3D jelenetet a kívánt fájlformátumban. Ebben a példában FBX7500ASCII formátumban mentjük el.

## Következtetés

Gratulálunk! Sikeresen átalakított egy csomópontot transzformációs mátrix segítségével egy 3D-s jelenetben az Aspose.3D for .NET segítségével. Ez a képesség sokrétű és vizuálisan lenyűgöző 3D alkalmazások előtt nyit ajtót.

## GYIK

### 1. kérdés: Mi az a transzformációs mátrix a 3D grafikában?

1. válasz: A transzformációs mátrix egy matematikai ábrázolás, amelyet különféle transzformációk (fordítás, elforgatás, méretezés) alkalmazására alkalmaznak a 3D-s térben lévő objektumokra.

### 2. kérdés: Alkalmazhatok több átalakítást egyetlen csomóponton?

2. válasz: Igen, több transzformációt is kombinálhat úgy, hogy megszorozza a megfelelő mátrixokat, és alkalmazza az eredményt a csomópontra.

### 3. kérdés: Vannak más támogatott fájlformátumok a 3D jelenetek mentéséhez?

 3. válasz: Az Aspose.3D for .NET különféle fájlformátumokat támogat, beleértve az STL-t, GLTF-et, OBJ-t és egyebeket. Utal[dokumentáció](https://reference.aspose.com/3d/net/) átfogó listáért.

### 4. kérdés: Hogyan szerezhetek ideiglenes licencet az Aspose.3D for .NET számára?

 A4: Látogassa meg a[ideiglenes licenc oldal](https://purchase.aspose.com/temporary-license/) az Aspose webhelyén, hogy ideiglenes engedélyt szerezzen értékelési célokra.

### 5. kérdés: Hol kérhetek segítséget, vagy csatlakozhatok az Aspose.3D közösséghez?

A5: Látogassa meg a[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) kérdéseket feltenni, tapasztalatokat megosztani, és kapcsolatba lépni más fejlesztőkkel az Aspose.3D használatával.