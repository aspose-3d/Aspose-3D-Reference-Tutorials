---
date: 2026-04-12
description: Tanulja meg, hogyan hozhat létre kocka jeleneteket, és mentheti a jelenetet
  FBX formátumban az Aspose.3D for .NET használatával – lépésről‑lépésre útmutató,
  előfeltételek és kódminták.
keywords:
- how to create cube
- how to export fbx
- add mesh to node
- export scene as fbx
- save scene as fbx
linktitle: Kocka jelenetek létrehozása
second_title: Aspose.3D .NET API
title: Hogyan hozhatunk létre kocka jeleneteket az Aspose.3D .NET-hez
url: /hu/net/geometry-and-hierarchy/create-cube-scenes/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hogyan hozzunk létre kocka jeleneteket az Aspose.3D for .NET segítségével

## Bevezetés

Készen állsz, hogy életre kelts egy egyszerű 3‑D kockát? Ebben az útmutatóban megtanulod, hogyan **hozz létre kocka** jeleneteket az Aspose.3D for .NET segítségével, exportáld a modellt FBX fájlként, és azonnal lásd az eredményt. Akár játékeszközt prototípusolsz, akár adatot vizualizálsz, az alábbi lépések szilárd alapot adnak, amelyet textúrákkal, megvilágítással vagy animációval bővíthetsz.

## Gyors válaszok
- **A tutorial mit fed le?** Kocka háló létrehozása, háló hozzáadása a node-hoz, és a jelenet mentése FBX fájlként.  
- **Melyik könyvtár szükséges?** Aspose.3D for .NET (ingyenes próba elérhető).  
- **Szükségem van licencre a minta futtatásához?** Ideiglenes vagy próba licenc működik fejlesztéshez és teszteléshez.  
- **Milyen IDE-t használhatok?** Bármely .NET‑kompatibilis IDE (Visual Studio, Rider, VS Code).  
- **Mennyi időt vesz igénybe?** Körülbelül 10 perc a kód megírásához, fordításhoz és futtatáshoz.

## Hogyan hozzunk létre kocka jeleneteket az Aspose.3D segítségével

A kocka jelenet a 3‑D grafika “Hello World” példája. Lehetővé teszi, hogy ellenőrizd, hogy a folyamatod – a háló létrehozásától a **jelenet exportálásáig FBX‑ként** – helyesen működik-e. Az alábbiakban lépésről lépésre végigvezetünk, elmagyarázzuk a „miért” kérdést, és pontosan megmutatjuk, hová kell elhelyezni a kódot.

## Mi az a 3D kocka jelenet?

A 3D kocka jelenet egy minimális háromdimenziós modell, amely egyetlen kockageometriát tartalmaz egy jelenet gráfon belül. Ez a 3D grafika “Hello World” példája, amely lehetővé teszi, hogy ellenőrizd, hogy a folyamatod – a háló létrehozásától a fájl exportálásáig – helyesen működik-e.

## Miért hozzunk létre kocka jeleneteket az Aspose.3D segítségével?

* **Keresztformátum támogatás:** Exportálás FBX, STL, OBJ és számos más formátumba további konverterek nélkül.  
* **Tiszta .NET API:** Nincsenek natív függőségek, tökéletes C# fejlesztőknek.  
* **Gazdag funkciók:** Beépített hálóépítők, anyagkezelés és jelenet hierarchia kezelése.  
* **Gyors prototípus készítés:** Írj néhány sor kódot, és kapj egy használatra kész 3D fájlt.  

## Előfeltételek

1. **Aspose.3D for .NET Library** – töltsd le és telepítsd a [Aspose dokumentációból](https://reference.aspose.com/3d/net/).  
2. **Fejlesztői környezet** – Visual Studio 2022, Rider vagy bármely szerkesztő, amely támogatja a .NET 6+.  
3. **Alap C# ismeretek** – kényelmesen kell tudnod osztályokkal, objektumokkal és konzolos alkalmazásokkal dolgozni.

## Névterek importálása

Először add hozzá a szükséges `using` utasításokat, hogy a fordító tudja, hol találhatók az Aspose.3D típusok.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
```

## Lépésről‑lépésre útmutató

### 1. lépés: A Scene inicializálása

Hozz létre egy üres `Scene` objektumot, amely tartalmazni fogja az összes node-ot, hálót, fényt és kamerát.

```csharp
// ExStart:CreateCubeScene
// Initialize scene object
Scene scene = new Scene();
```

### 2. lépés: Node létrehozása a kockához

`Node` egy konténerként működik a geometria számára. Adj neki egy barátságos nevet, hogy később megtaláld a hierarchiában.

```csharp
// Initialize Node class object
Node cubeNode = new Node("cube");
```

### 3. lépés: Háló építése

Az Aspose.3D egy `Common` nevű segédeszközt biztosít, amely képes kocka hálót generálni egy poligonépítő segítségével. Ez megkímél a csúcsok és felületek kézi definiálásától.

```csharp
// Call Common class create mesh using polygon builder method to set mesh instance 
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

### 4. lépés: Háló hozzáadása a node-hoz

Rendeld hozzá a most létrehozott hálót a node `Entity` tulajdonságához. Ez összekapcsolja a geometriát a jelenet gráffal.

```csharp
// Point node to the Mesh geometry
cubeNode.Entity = mesh;
```

### 5. lépés: Node hozzáadása a Scene-hez

Helyezd be a kocka node-ot a scene gyökerébe, hogy a végső kimenet része legyen.

```csharp
// Add Node to a scene
scene.RootNode.ChildNodes.Add(cubeNode);
```

### 6. lépés: FBX exportálása (scene mentése FBX‑ként)

Válassz egy kimeneti útvonalat, és exportáld a scene-et. Itt az FBX 7400 ASCII formátumot használjuk, amelyet széles körben támogatnak a 3D szerkesztők.

```csharp
// The path to the documents directory.
var output = "Your Output Directory" + "CubeScene.fbx";

// Save 3D scene in the supported file formats
scene.Save(output, FileFormat.FBX7400ASCII);
```

### 7. lépés: Sikerüzenet megjelenítése

Adj a felhasználónak egyértelmű visszajelzést, hogy a fájl sikeresen íródott.

```csharp
Console.WriteLine("\nCube Scene created successfully.\nFile saved at " + output);
```

## Gyakori problémák és megoldások

| Probléma | Miért fordul elő | Megoldás |
|----------|------------------|----------|
| **File not found** hiba a `scene.Save` futtatásakor | A kimeneti könyvtár nem létezik vagy nincs írási jogosultságod. | Először hozd létre a könyvtárat (`Directory.CreateDirectory`), vagy használj egy saját abszolút útvonalat. |
| **Empty file** export után | A háló nem lett csatolva a node-hoz vagy a node nem lett hozzáadva a scene-hez. | Győződj meg róla, hogy a `cubeNode.Entity = mesh;` és a `scene.RootNode.ChildNodes.Add(cubeNode);` végrehajtásra kerül. |
| **Incorrect format** megnyitáskor egy megjelenítőben | A helytelen `FileFormat` enum érték használata. | `FileFormat.FBX7400ASCII` használata ASCII FBX-hez vagy `FileFormat.FBX7400Binary` binárishoz. |

## Gyakran Ismételt Kérdések

**K: Az Aspose.3D kompatibilis különböző 3D fájlformátumokkal?**  
A: Igen, az Aspose.3D támogatja az FBX, STL, OBJ, GLTF és még sok más formátumot, lehetővé téve, hogy **scene-et FBX‑ként ments** vagy más formátumokba egyetlen kódsorral.

**K: Testreszabhatom a kocka megjelenését?**  
A: Természetesen. Hozzárendelhetsz egy `Material`-t a hálóhoz, megváltoztathatod a színét, vagy textúrát alkalmazhatsz a `Material` osztály segítségével.

**K: Hol találok további támogatást és forrásokat?**  
A: Látogasd meg az [Aspose.3D fórumot](https://forum.aspose.com/c/3d/18) közösségi segítségért és megbeszélésekért.

**K: Elérhető ingyenes próba?**  
A: Igen, egy ingyenes próba verziót itt tekinthetsz meg [here](https://releases.aspose.com/).

**K: Hogyan szerezhetek ideiglenes licencet az Aspose.3D-hez?**  
A: Szerezz ideiglenes licencet [itt](https://purchase.aspose.com/temporary-license/).

## Következtetés

Ebben az útmutatóban bemutattuk, hogyan **hozzunk létre kocka** jeleneteket lépésről lépésre, a `Scene` inicializálásától a **jelenet exportálásáig FBX‑ként**. Most már szilárd alapod van a bonyolultabb geometriákkal való kísérletezéshez, textúrák, fények hozzáadásához és akár a modellek animálásához is. Folyamatosan fedezd fel az Aspose.3D API-t – a lehetőségek gyakorlatilag végtelenek.

---

**Utoljára frissítve:** 2026-04-12  
**Tesztelve:** Aspose.3D for .NET 24.11 (a legújabb a írás időpontjában)  
**Szerző:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}