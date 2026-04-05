---
date: 2026-02-25
description: Tanulja meg, hogyan fordítsa meg a koordináta rendszert, és testreszabja
  a 3D importot az Aspose.3D LoadOptions használatával Java-ban. Lépésről‑lépésre
  útmutató a 3DS, OBJ, STL, U3D, glTF, PLY, X, valamint opcionális FBX formátumokhoz.
linktitle: Customize 3D File Loading in Java with Aspose.3D LoadOptions
second_title: Aspose.3D Java API
title: Koordináta-rendszer megfordítása – 3D fájl betöltés testreszabása Java-ban
  az Aspose.3D segítségével
url: /hu/java/load-and-save/customize-3d-file-loading/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Koordináta-rendszer megfordítása – 3D fájl betöltés testreszabása Java-ban az Aspose.3D segítségével

A 3D tervezés és fejlesztés folyamatosan változó világában a modellek importálásakor a **koordináta-rendszer megfordítása** gyakori követelmény. Akár jobb‑kezes rendszerről bal‑kezesre konvertálja az eszközöket, akár a modelljeit a motorja tengelykonvencióihoz kell igazítania, az Aspose.3D for Java finomhangolt vezérlést biztosít. Ez a bemutató végigvezet a **3D import testreszabásán** az Aspose.3D `LoadOptions` használatával, lefedve a legnépszerűbb formátumokat, mint a 3DS, OBJ, STL, U3D, glTF, PLY, X, és az opcionális FBX.

## Gyors válaszok
- **Mi a “koordináta-rendszer megfordítása”?** Az X/Y/Z tengelyeket cseréli, hogy megfeleljen a cél koordináta-konvenciónak.  
- **Mely formátumok támogatják a megfordítást?** Minden fő formátum (3DS, OBJ, STL, U3D, glTF, PLY, X, FBX) rendelkezik `setFlipCoordinateSystem` opcióval.  
- **Szükség van extra könyvtárakra?** Csak az Aspose.3D for Java JAR; külső konvertálók nem szükségesek.  
- **Betölthetek anyagokat egyszerre?** Igen – használja a `setEnableMaterials(true)` opciót OBJ fájlokhoz.  
- **Szükséges licenc a termeléshez?** Érvényes Aspose.3D licenc szükséges a nem‑próba telepítésekhez.

## Mi a “koordináta-rendszer megfordítása”?
A koordináta-rendszer megfordítása megváltoztatja az importált modell által használt tengelyek orientációját. Ez akkor elengedhetetlen, ha a forrásfájl más kézességet (jobb‑kezes vs. bal‑kezes) használ, mint a renderelő motorja, megakadályozva, hogy a modellek tükröződve vagy fordítva jelenjenek meg.

## Miért testreszabjuk a 3D importot?
- Animációs transzformációk megőrzése (`setApplyAnimationTransform`).  
- A színkezelés helyes beállítása (`setGammaCorrectedColor`).  
- Külső erőforrás útvonalak feloldása a `getLookupPaths()` segítségével.  
- Memóriahasználat optimalizálása, csak a szükséges elemek betöltésével.

## Előfeltételek

- Alapvető Java programozási ismeretek.  
- Telepített Java Development Kit (JDK).  
- Aspose.3D for Java könyvtár letöltve. Letöltheti [itt](https://releases.aspose.com/3d/java/).  
- Ismerete a 3D fájlformátumoknak, mint a 3DS, OBJ, STL, U3D, glTF, PLY, X és FBX.

## Csomagok importálása

Java projektjében győződjön meg róla, hogy importálja a szükséges Aspose.3D csomagokat:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Hogyan testreszabjuk a 3D importot a LoadOptions használatával

Az alábbiakban lépésről‑lépésre kódrészletek láthatók, amelyek bemutatják, hogyan engedélyezhető a **koordináta-rendszer megfordítása** opció minden támogatott formátumhoz. A részletek készen állnak a projektbe másolásra; csak cserélje le a `"Your Document Directory"`-t a tényleges eszközök elérési útjára.

### 1. lépés: 3DS fájl betöltés testreszabása

```java
public static void discreet3DSLoadOption() {
    String MyDir = "Your Document Directory";
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();
    loadOpts.setApplyAnimationTransform(true);
    loadOpts.setFlipCoordinateSystem(true);
    loadOpts.setGammaCorrectedColor(true);
    loadOpts.getLookupPaths().add(MyDir);
}
```

### 2. lépés: OBJ fájl betöltés testreszabása

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### 3. lépés: STL fájl betöltés testreszabása

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### 4. lépés: U3D fájl betöltés testreszabása

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### 5. lépés: glTF fájl betöltés testreszabása

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### 6. lépés: PLY fájl betöltés testreszabása

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### 7. lépés: X fájl betöltés testreszabása

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### 8. lépés: FBX fájl betöltés testreszabása (opcionális)

```java
private static void FBXLoadOptions() throws IOException {
    String dataDir = "Your Document Directory";
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions();
    opt.setKeepBuiltinGlobalSettings(true);
    scene.open(dataDir + "test.FBX", opt);
    for(Property property:scene.getRootNode().getAssetInfo().getProperties()) {
        System.out.println(property);
    }
}
```

## Gyakori problémák és megoldások
- **A modell tükröződve jelenik meg a betöltés után** – Ellenőrizze, hogy a `setFlipCoordinateSystem(true)` a megfelelő formátumra van beállítva.  
- **Anyagok hiányoznak** – OBJ fájlok esetén győződjön meg róla, hogy a `setEnableMaterials(true)` be van állítva, és a material fájlok (.mtl) az egyik lookup útvonalban találhatók.  
- **A textúra koordináták fejjel lefelé vannak** – glTF esetén szükség lehet a `setFlipTexCoordV(true)` használatára a tengelyek megfordítása mellett.  
- **Fájl nem található hibák** – Adja hozzá a külső erőforrásokat (textúrák, segédfájlok) tartalmazó könyvtárat a `loadOpts.getLookupPaths()`-hez.

## Következtetés

Az Aspose.3D `LoadOptions` használatával **megfordíthatja a koordináta-rendszert** és **testreszabhatja a 3D importot** gyakorlatilag minden fő formátumhoz. Ez a szintű vezérlés megszünteti a post‑processing szkriptek szükségességét, és biztosítja, hogy az eszközei már az első alkalommal helyesen jelenjenek meg.

## Gyakran Ismételt Kérdések

### Q1: Hol találom az Aspose.3D for Java dokumentációt?
A dokumentáció elérhető [here](https://reference.aspose.com/3d/java/).

### Q2: Hogyan tölthetem le az Aspose.3D for Java-t?
Letöltheti [here](https://releases.aspose.com/3d/java/).

### Q3: Van elérhető ingyenes próba?
Igen, a ingyenes próbát [here](https://releases.aspose.com/).

### Q4: Hol kaphatok támogatást az Aspose.3D for Java-hoz?
Látogassa meg a támogatási fórumot [here](https://forum.aspose.com/c/3d/18).

### Q5: Szükségem van ideiglenes licencre a teszteléshez?
Igen, szerezze be az ideiglenes licencet [here](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Utolsó frissítés:** 2026-02-25  
**Tesztelve:** Aspose.3D for Java 24.11 (legújabb)  
**Szerző:** Aspose