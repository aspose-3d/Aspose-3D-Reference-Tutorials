---
title: 3D hálók mentése egyéni bináris formátumban
linktitle: 3D hálók mentése egyéni bináris formátumban
second_title: Aspose.3D .NET API
description: Fedezze fel a 3D világát az Aspose.3D for .NET segítségével. Tanulja meg a hálók egyéni bináris formátumban történő mentését.
weight: 13
url: /hu/net/3d-scene/save-3d-meshes-binary-format/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D hálók mentése egyéni bináris formátumban

## Bevezetés

Üdvözöljük az Aspose.3D for .NET világában, egy hatékony könyvtár, amely lehetővé teszi a fejlesztők számára, hogy könnyedén dolgozzanak 3D fájlokkal. Ebben az oktatóanyagban a 3D hálók egyéni bináris formátumban történő mentésének folyamatát mutatjuk be az Aspose.3D for .NET használatával. Ez az útmutató feltételezi, hogy rendelkezik a C# alapvető ismereteivel, és ismeri az Aspose.3D könyvtárat.

## Előfeltételek

Mielőtt belevágnánk az oktatóanyagba, győződjön meg arról, hogy a helyén van a következők:

-  Aspose.3D for .NET: Győződjön meg arról, hogy telepítve van az Aspose.3D könyvtár. Letöltheti innen[itt](https://releases.aspose.com/3d/net/).

- Fejlesztési környezet: Állítsa be a kívánt C# fejlesztői környezetet, például a Visual Studio-t.

- Input 3D fájl: rendelkezzen egy 3D fájllal (pl. test.fbx), amelyet egyéni bináris formátumba szeretne konvertálni.

## Névterek importálása

A C# kódban adja meg az Aspose.3D funkciók eléréséhez szükséges névtereket:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
```

## 1. lépés: Töltsön be egy 3D fájlt

Töltse be a 3D fájlt az Aspose.3D segítségével. Ebben a példában egy "test.fbx" nevű fájlt töltünk be:

```csharp
Scene scene = Scene.FromFile("test.fbx");
```

## 2. lépés: Adja meg az egyéni bináris formátumot

Határozza meg annak az egyéni bináris formátumnak a szerkezetét, amelyben el szeretné menteni a 3D hálókat. A példa olyan struktúrát használ, amelyben a MeshBlock, a Vertex és a Triangle összetevők.

```csharp
// Egy csúcs memóriaelrendezése az
// float[3] pozíció;
// float[3] normál;
// float[3] uv;
var vertexDeclaration = new VertexDeclaration();
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Position);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Normal);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.UV);

```

## 3. lépés: Nyissa meg a fájlt íráshoz

Nyisson meg egy bináris fájlt íráshoz, ahol a konvertált 3D hálók mentésre kerülnek:

```csharp
using (var writer = new BinaryWriter(new FileStream("Your Output Directory" + "Save3DMeshesInCustomBinaryFormat_out", FileMode.Create, FileAccess.Write)))
```

## 4. lépés: Iteráljon csomópontokon és entitásokon keresztül

Látogassa meg a 3D jelenet minden csomópontját, és alakítsa át a háló entitásokat az egyéni bináris formátumba. Figyelmen kívül hagyja a fényeket, kamerákat és más nem hálós entitásokat:

```csharp
scene.RootNode.Accept(delegate(Node node)
{
    foreach (Entity entity in node.Entities)
    {
        if (!(entity is IMeshConvertible))
            continue;
        // ... (a feldolgozás folytatása)
    }
    return true;
});
```

## 5. lépés: Konvertálja és írjon vezérlőpontokat és háromszögeket

Minden egyes háló entitásnál konvertálja a vezérlőpontokat világtérré, és írja be őket a bináris fájlba a háromszög indexekkel együtt:

```csharp
Mesh m = ((IMeshConvertible)entity).ToMesh();

var triMesh = TriMesh.FromMesh(vertexDeclaration, m);


//A háló memória elrendezése a következő:
// float[16] transzformációs_mátrix;
// int csúcsok_száma;
// int indexek_száma;
// vertex[vertices_count] csúcsok;
// ushort[indexek_száma] indexek;


//írási átalakítás
var transform = node.GlobalTransform.TransformMatrix.ToArray();
for(int i = 0; i < transform.Length; i++)
    writer.Write((float)transform[i]);
//írja be a csúcsok/indexek számát
writer.Write(triMesh.VerticesCount);
writer.Write(triMesh.IndicesCount);
//csúcsokat és indexeket írjon
writer.Flush();
triMesh.WriteVerticesTo(writer.BaseStream);
triMesh.Write16bIndicesTo(writer.BaseStream);

```

## Következtetés

Ebben az oktatóanyagban a 3D hálók egyéni bináris formátumban történő mentésének folyamatát ismertettük az Aspose.3D for .NET használatával. Ez a hatékony könyvtár biztosítja a fejlesztők számára a 3D-s fájlok zökkenőmentes kezeléséhez szükséges eszközöket. Kísérletezzen különböző formátumokkal és beállításokkal, hogy kiaknázza az Aspose.3D teljes potenciálját projektjeiben.

## GYIK

### 1. kérdés: Használhatom az Aspose.3D for .NET fájlt más programozási nyelvekkel?

1. válasz: Az Aspose.3D elsősorban a .NET nyelveket támogatja, de felfedezhet más nyelvek kompatibilitási lehetőségeit is.

### 2. kérdés: Hol találhatok további példákat és forrásokat?

 A2: Az[Aspose.3D fórum](https://forum.aspose.com/c/3d/18)nagyszerű hely a támogatásra, a példákra és a közösséggel való kapcsolatra.

### 3. kérdés: Elérhető az Aspose.3D próbaverziója?

 3. válasz: Igen, ingyenes próbaverziót kaphat a webhelyről[itt](https://releases.aspose.com/).

### 4. kérdés: Hogyan szerezhetek ideiglenes licencet az Aspose.3D-hez?

 A4: Látogassa meg[ez a link](https://purchase.aspose.com/temporary-license/) ideiglenes engedélyt szerezni tesztelési célból.

### 5. kérdés: Megvásárolhatom az Aspose.3D-t .NET-hez?

 V5: Igen, megvásárolhatja az Aspose.3D-t a[vásárlási oldal](https://purchase.aspose.com/buy).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
