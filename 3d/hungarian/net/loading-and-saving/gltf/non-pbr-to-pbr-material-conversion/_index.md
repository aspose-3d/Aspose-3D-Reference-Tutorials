---
title: Nem PBR anyag átalakítás PBR-re
linktitle: Nem PBR anyag átalakítás PBR-re
second_title: Aspose.3D .NET API
description: Fedezze fel az Aspose.3D for .NET-et – A nem PBR anyagokat könnyedén konvertálja PBR-be. Átfogó oktatóanyag és hatékony API.
weight: 16
url: /hu/net/loading-and-saving/gltf/non-pbr-to-pbr-material-conversion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Nem PBR anyag átalakítás PBR-re

## Bevezetés

Üdvözöljük ebben a lépésről lépésre szóló útmutatóban az Aspose.3D for .NET használatáról a nem PBR (fizikai alapú renderelés) PBR anyagokká való konvertálásához. Az Aspose.3D egy hatékony API, amely lehetővé teszi a fejlesztők számára, hogy zökkenőmentesen dolgozzanak a 3D fájlformátumokkal .NET-alkalmazásaikban.

## Előfeltételek

Mielőtt belevágnánk az oktatóanyagba, győződjön meg arról, hogy rendelkezik a következő előfeltételekkel:

-  Aspose.3D for .NET: Győződjön meg arról, hogy telepítve van az Aspose.3D for .NET könyvtár. A letöltési linket megtalálod[itt](https://releases.aspose.com/3d/net/).

- A C# alapvető ismerete: Ez az oktatóanyag feltételezi, hogy alapvető ismeretekkel rendelkezik a C# programozásról.

- IDE (Integrated Development Environment): Válassza ki a kívánt IDE-t a .NET-fejlesztéshez, például a Visual Studio-t.

## Névterek importálása

A C# kódban kezdje a szükséges névterek importálásával:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## 1. lépés: Új 3D-s jelenet inicializálása

Kezdje új 3D-s jelenet létrehozásával a következő kóddal:

```csharp
// ExStart:Non_PBRtoPBRMaterial
// új 3D-s jelenet inicializálása
var scene = new Scene();
```

## 2. lépés: Hozzon létre egy 3D objektumot

Ezután hozzon létre egy 3D objektumot, például egy dobozt:

```csharp
var box = new Box();
scene.RootNode.CreateChildNode("box1", box).Material = new PhongMaterial() { DiffuseColor = new Vector3(1, 0, 1) };
```

## 3. lépés: Konfigurálja az Anyagátalakítást

Állítsa be az anyagátalakítási beállításokat a nem PBR-ből PBR-be való konverzióhoz:

```csharp
GltfSaveOptions options = new GltfSaveOptions(FileFormat.GLTF2);
options.MaterialConverter = delegate (Material material)
{
    PhongMaterial phongMaterial = (PhongMaterial)material;
    return new PbrMaterial() { Albedo = new Vector3(phongMaterial.DiffuseColor.x, phongMaterial.DiffuseColor.y, phongMaterial.DiffuseColor.z) };
};
```

## 4. lépés: Mentse el GLTF 2.0 formátumban

Mentse el a konvertált jelenetet GLTF 2.0 formátumban:

```csharp
scene.Save("Your Output Directory" + "Non_PBRtoPBRMaterial_Out.gltf", options);
// ExEnd:Non_PBRtoPBRMaterial
```

Ismételje meg ezeket a lépéseket az adott felhasználási esetnek megfelelően, biztosítva, hogy minden részlet megfelelően legyen konfigurálva.

## Következtetés

Gratulálunk! Sikeresen megtanulta, hogyan lehet nem PBR-t PBR anyagokká konvertálni az Aspose.3D for .NET használatával. Ez a hatékony eszköz végtelen lehetőségeket nyit meg a .NET-alkalmazások 3D-s grafikus manipulálásához.

## GYIK

### 1. kérdés: Az Aspose.3D kompatibilis az összes 3D fájlformátummal?

1. válasz: Igen, az Aspose.3D a 3D fájlformátumok széles skáláját támogatja, rugalmasságot biztosítva a projektekben.

### 2. kérdés: Használhatom az Aspose.3D-t kereskedelmi alkalmazásokhoz?

 A2: Abszolút! Az Aspose.3D kereskedelmi termék, és megvásárolhatja[itt](https://purchase.aspose.com/buy).

### 3. kérdés: Szükségem van ideiglenes licencre a teszteléshez?

 3. válasz: Igen, ideiglenes licencet szerezhet tesztelési célokra[itt](https://purchase.aspose.com/temporary-license/).

### 4. kérdés: Hol találok támogatást az Aspose.3D-hez?

 A4: Látogassa meg a[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) közösségi támogatásra és beszélgetésekre.

### 5. kérdés: Van ingyenes próbaverzió?

 5. válasz: Igen, felfedezhet egy ingyenes próbaverziót[itt](https://releases.aspose.com/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
