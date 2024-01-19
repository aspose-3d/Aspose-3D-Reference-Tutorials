---
title: Jelenet megjelenítése kockatérképbe hat arccal
linktitle: Jelenet megjelenítése kockatérképbe hat arccal
second_title: Aspose.3D .NET API
description: Lenyűgöző kockatérképek létrehozása az Aspose.3D for .NET segítségével. Kövesse lépésenkénti útmutatónkat a 3D-s jelenetek lenyűgöző, hatarcú kockatérképekké alakításához.
type: docs
weight: 14
url: /hu/net/rendering/render-scene-cubemap/
---
## Bevezetés
Üdvözöljük ebben a lépésről-lépésre szóló útmutatóban, amely egy jelenet hat arcú kockatérképpé való renderelésére vonatkozik az Aspose.3D for .NET használatával. Ebben az oktatóanyagban végigvezetjük a lenyűgöző kockatérkép létrehozásának folyamatán egy 3D-s jelenet renderelésével. Az Aspose.3D egy hatékony .NET API, amely leegyszerűsíti a 3D grafikus manipulációt, és ezzel az útmutatóval kihasználhatja a képességeit lenyűgöző kockatérképek létrehozásában.
## Előfeltételek
Mielőtt belevágnánk az oktatóanyagba, győződjön meg arról, hogy a következő előfeltételek teljesülnek:
- C# és .NET fejlesztési ismeretek.
-  Aspose.3D for .NET telepítve. Letöltheti[itt](https://releases.aspose.com/3d/net/).
- 3D jelenetfájl GLB formátumban (pl. "VirtualCity.glb") a megjelenítéshez.
## Névterek importálása
Kezdje azzal, hogy importálja az Aspose.3D szükséges névtereit a C# kódban:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Imaging;
using System.Linq;
using System.Text;
```
## 1. lépés: Töltse be a jelenetet
Töltse be a 3D-s jelenetfájlt a következő kóddal:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## 2. lépés: Hozza létre a kamerát és a fényeket
Hozzon létre egy kamerát és két lámpát a jelenet megvilágításához:
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light()
{
    Color = new Vector3(Color.CadetBlue)
}).Transform.Translation = new Vector3(49, 0, 49);
```
## 3. lépés: Hozzon létre renderelőt és renderelő célt
Hozzon létre egy megjelenítőt és egy kockatérkép renderelő célt mélységi textúrával:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
    ITextureCubemap cubemap = rt.Targets[0] as ITextureCubemap;
```
## 4. lépés: Mentse el a Cubemap arcokat
Mentse a kockatérkép minden oldalát a lemezre meghatározott fájlnevekkel:
```csharp
CubeFaceData<string> fileNames = new CubeFaceData<string>()
{
    Right = "Your Output Directory" + "right.png",
    Left = "Your Output Directory" + "left.png",
    Back = "Your Output Directory" + "back.png",
    Front = "Your Output Directory" + "front.png",
    Bottom = "Your Output Directory" + "bottom.png",
    Top = "Your Output Directory" + "top.png"
};
cubemap.Save(fileNames, ImageFormat.Png);
```
## Következtetés
Gratulálunk! Sikeresen megjelenített egy 3D-s jelenetet kockatérképben az Aspose.3D for .NET használatával. Fedezze fel a további testreszabási lehetőségeket, és javítsa 3D grafikus projektjeit ezzel a hatékony API-val.
## Gyakran Ismételt Kérdések
### K: Használhatom az Aspose.3D for .NET fájlt más 3D fájlformátumokkal?
Igen, az Aspose.3D különféle 3D fájlformátumokat támogat, rugalmasságot biztosítva a projektekben.
### K: Hogyan kaphatok támogatást az Aspose.3D-hez?
 Meglátogatni a[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) közösségi támogatásra és beszélgetésekre.
### K: Van ingyenes próbaverzió?
 Igen, hozzáférhet az ingyenes próbaverzióhoz[itt](https://releases.aspose.com/).
### K: Renderelhetek jeleneteket animációkkal az Aspose.3D használatával?
Teljesen! Az Aspose.3D támogatja az animált 3D jelenetek megjelenítését.
### K: Hol találok részletes dokumentációt?
 Utal[Aspose.3D dokumentáció](https://reference.aspose.com/3d/net/) mélyreható tájékoztatásért.