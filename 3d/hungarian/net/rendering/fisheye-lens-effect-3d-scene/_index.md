---
title: Halszem lencse effektus alkalmazása az Aspose.3D segítségével .NET-hez
linktitle: Halszem lencse effektus alkalmazása 3D-s jelenetre
second_title: Aspose.3D .NET API
description: Fokozza 3D jeleneteit az Aspose.3D for .NET segítségével! Ismerje meg lépésről lépésre, hogyan alkalmazhat elbűvölő halszem lencsehatást. Letöltés most!
weight: 12
url: /hu/net/rendering/fisheye-lens-effect-3d-scene/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Halszem lencse effektus alkalmazása az Aspose.3D segítségével .NET-hez

## Bevezetés
Szeretné javítani 3D jelenete vizuális vonzerejét? Merüljön el a halszem lencse effektusok lenyűgöző világában az Aspose.3D for .NET segítségével. Ez az oktatóanyag lépésről lépésre végigvezeti Önt abban, hogyan alkalmazzon halszem-lencse-effektust a 3D-s jelenetekhez, így egyedi és magával ragadó perspektívát ad.
## Előfeltételek
Mielőtt elkezdené, győződjön meg arról, hogy a következő előfeltételek teljesülnek:
-  Aspose.3D for .NET: Győződjön meg arról, hogy telepítve van a .NET Aspose.3D könyvtára. Ha nem, akkor letöltheti[itt](https://releases.aspose.com/3d/net/).
-  Minta 3D jelenet: Egy minta 3D jelenetfájllal (VirtualCity.glb) fogunk dolgozni. Használhatja saját jelenetét, vagy letöltheti a mintát a[Aspose.3D dokumentáció](https://reference.aspose.com/3d/net/).
## Névterek importálása
A .NET-projektben tartalmazza az Aspose.3D funkciók eléréséhez szükséges névtereket. Adja hozzá a következő névtereket a kód elejéhez:
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
## 1. lépés: Töltse be a 3D jelenetet
Töltse be a 3D jelenet fájlt a projektbe a következő kóddal:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## 2. lépés: A kamera és a fények beállítása
Hozzon létre egy kamerát és fényeket, hogy javítsa a jelenet vizuális aspektusait. Szükség szerint állítsa be az olyan paramétereket, mint a NearPlane, FarPlane és RotationMode:
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light() { Color = new Vector3(Color.CadetBlue) }).Transform.Translation = new Vector3(49, 0, 49);
```
## 3. lépés: Hozzon létre renderelőt és renderelő célokat
Állítsa be a renderelőt és hozzon létre renderelési célokat kockatérképhez és 2D textúrához:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    IRenderTexture final = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(false, 32, 0, 0), 1024, 1024);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
```
## 4. lépés: Alkalmazza a Fisheye Lens Effect
Hajtsa végre a halszem lencse effektus utófeldolgozását a renderelt kockatérképen:
```csharp
PostProcessing fisheye = renderer.GetPostProcessing("fisheye");
fisheye.FindProperty("fov").Value = 360.0;
fisheye.Input = rt.Targets[0];
renderer.Execute(fisheye, final);
((ITexture2D)final.Targets[0]).Save("Your Output Directory" + "fisheye.png", ImageFormat.Png);
```
## Következtetés
Gratulálunk! Sikeresen alkalmazta a halszem lencse effektust a 3D-s jeleneten az Aspose.3D for .NET használatával. Kísérletezzen különböző jelenetekkel és paraméterekkel, hogy szabadjára engedje kreativitását.
## Gyakran Ismételt Kérdések
### Alkalmazhatom a halszem-effektust bármely 3D-s jelenetre?
Igen, a halszem effektust bármilyen 3D jelenetre alkalmazhatja. Az optimális eredmény érdekében győződjön meg arról, hogy a jelenet megfelelően van betöltve és megvilágítva.
### Mi a jelentősége a látómező (fov) 360 fokos beállításának?
A 360 fokos látómező teljes gömb alakú vetítést biztosít, lenyűgöző halszem hatást keltve.
### Hogyan szabhatom testre a világítást a 3D-s jelenetemben?
A kívánt fényhatások elérése érdekében beállíthatja a lámpák tulajdonságait, például helyzetét, típusát és színét.
### Van-e korlátozás a feldolgozható 3D-s jelenet méretére?
A 3D-s jelenet méretét elsősorban a rendszer erőforrásai korlátozzák. Győződjön meg arról, hogy a hardver képes kezelni a jelenet méretét.
### Használhatok más kimeneti formátumot a PNG helyett a halszem effektus eredményéhez?
Igen, módosíthatja a kódot, hogy a kimenetet az igényeinek megfelelően különböző képformátumokba mentse.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
