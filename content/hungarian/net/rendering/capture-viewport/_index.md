---
title: Nézőablakok rögzítése 3D-s jelenetekben
linktitle: Nézőablakok rögzítése 3D-s jelenetekben
second_title: Aspose.3D .NET API
description: Tanuljon meg lenyűgöző 3D-s nézetablakokat rögzíteni az Aspose.3D for .NET használatával. Lépésről lépésre szóló útmutató a jelenetek rugalmas megjelenítéséhez.
type: docs
weight: 11
url: /hu/net/rendering/capture-viewport/
---
## Bevezetés

A 3D-s grafika és vizualizáció területén a nézetablak rögzítése elengedhetetlen készség, amely javítja a jelenetek mélységét és részletességét. Az Aspose.3D for .NET robusztus megoldást kínál a 3D jelenetek megjelenítésére és manipulálására. Ez az oktatóanyag végigvezeti Önt a nézetablakok rögzítésének folyamatán 3D jelenetekben az Aspose.3D segítségével, lehetővé téve, hogy könnyedén készítsen lenyűgöző vizualizációkat.

## Előfeltételek

Mielőtt belevágna az oktatóanyagba, győződjön meg arról, hogy a következő előfeltételeket teljesítette:

-  Aspose.3D for .NET Library: Győződjön meg arról, hogy telepítve van az Aspose.3D könyvtár. Letöltheti innen[itt](https://releases.aspose.com/3d/net/).

## Névterek importálása

kezdéshez importálja a szükséges névtereket .NET-projektjébe:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using System.Drawing;
using System.Drawing.Imaging;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
```

## 1. lépés: Töltsön be egy meglévő 3D-s jelenetet

Kezdje egy meglévő 3D jelenet betöltésével a projektbe. A következő kódrészlet ezt szemlélteti:

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

## 2. lépés: Hozzon létre egy kamerát

Ezután hozzon létre egy példányt a kameráról, és állítsa be a pozícióját és a célját:

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

## 3. lépés: Adjon világítást a jelenethez

Fényforrás hozzáadásával tökéletesítse a jelenetet. Az alábbi kódrészlet megmutatja, hogyan lehet pontfényt létrehozni:

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

## 4. lépés: A Renderer és a Render Target konfigurálása

Állítsa be a renderelőt és hozzon létre egy renderelési célt a jelenet rögzítéséhez:

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    renderer.EnableShadows = false;

    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // ... (folytatás a következő lépésekben)
    }
}
```

## 5. lépés: A nézetablakok és a renderelés meghatározása

Határozza meg a nézetablakokat és jelenítse meg a jelenetet a kimeneti képek létrehozásához:

```csharp
Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-1viewports_out.png", ImageFormat.Png);
```

## 6. lépés: Módosítsa a nézetablakokat, és jelenítse meg újra

Módosítsa a nézetablakokat, és jelenítse meg ismét a jelenetet, demonstrálva az Aspose.3D rugalmasságát:

```csharp
vp.Area = new RelativeRectangle() { ScaleWidth = 0.5f, ScaleHeight = 1 };
rt.CreateViewport(camera, new RelativeRectangle() { ScaleX = 0.5f, ScaleWidth = 0.5f, ScaleHeight = 1 });
camera.FieldOfView = 90;
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-2viewports_out.png", ImageFormat.Png);
```

A kívánt vizuális effektusok elérése érdekében folytassa a kísérletezést a különböző konfigurációkkal.

## Következtetés

Ebben az oktatóanyagban megvizsgáltuk a nézetablak rögzítésének folyamatát 3D-s jelenetekben az Aspose.3D for .NET használatával. Hatékony funkcióit kihasználva új magasságokba emelheti 3D grafikai projektjeit, lenyűgöző vizuális élményt nyújtva.

## GYIK

### 1. kérdés: Az Aspose.3D kompatibilis más 3D fájlformátumokkal?

1. válasz: Igen, az Aspose.3D különféle 3D fájlformátumokat támogat, biztosítva ezzel a kompatibilitást a tervezési eszközök széles skálájával.

### 2. kérdés: Használhatom az Aspose.3D-t játékfejlesztéshez?

2. válasz: Míg az Aspose.3D elsősorban grafikára és megjelenítésre készült, funkciói kiegészíthetik a játékfejlesztés bizonyos aspektusait.

### 3. kérdés: Hol találhatok további példákat és dokumentációt?

 A3: Fedezze fel az átfogó[Aspose.3D dokumentáció](https://reference.aspose.com/3d/net/) további példákért és részletes információkért.

### 4. kérdés: Van ingyenes próbaverzió?

 4. válasz: Igen, hozzáférhet az ingyenes próbaverzióhoz[itt](https://releases.aspose.com/).

### 5. kérdés: Hogyan kérhetek segítséget vagy vehetek részt a közösségben?

 5. válasz: Csatlakozzon az Aspose.3D közösséghez a[támogatói fórum](https://forum.aspose.com/c/3d/18) segítségért és együttműködésért.