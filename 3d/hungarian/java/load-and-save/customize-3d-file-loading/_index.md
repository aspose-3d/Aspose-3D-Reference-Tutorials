---
title: Testreszabhatja a 3D fájlbetöltést Java nyelven az Aspose.3D LoadOptions segítségével
linktitle: Testreszabhatja a 3D fájlbetöltést Java nyelven az Aspose.3D LoadOptions segítségével
second_title: Aspose.3D Java API
description: Javítsa 3D-s fájlbetöltését Java nyelven az Aspose.3D testreszabható LoadOptions segítségével. Ismerje meg a 3DS, OBJ, STL, U3D, glTF, PLY, X és az opcionális FBX testreszabását lépésről lépésre.
weight: 12
url: /hu/java/load-and-save/customize-3d-file-loading/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Testreszabhatja a 3D fájlbetöltést Java nyelven az Aspose.3D LoadOptions segítségével

## Bevezetés

3D-s tervezés és fejlesztés folyamatosan változó környezetében a 3D-s fájlformátumok hatékony kezelése kulcsfontosságú. Az Aspose.3D for Java hatékony megoldást kínál a különféle 3D fájlformátumok betöltésének testreszabására. Ez az oktatóanyag végigvezeti Önt a 3D-s fájlok Java nyelven történő betöltésének testreszabásán az Aspose.3D LoadOptions segítségével.

## Előfeltételek

Mielőtt belevágna a testreszabási folyamatba, győződjön meg arról, hogy rendelkezik a következőkkel:

- A Java programozás alapvető ismerete.
- Telepített Java Development Kit (JDK).
-  Aspose.3D for Java könyvtár letöltve. Meg lehet szerezni[itt](https://releases.aspose.com/3d/java/).
- Ismerje meg a 3D fájlformátumokat, például a 3DS, OBJ, STL, U3D, glTF, PLY, X és FBX.

## Csomagok importálása

Java-projektjében feltétlenül importálja a szükséges Aspose.3D csomagokat:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## A 3D fájlbetöltés testreszabása

### 1. lépés: A 3DS fájlbetöltés testreszabása

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

### 2. lépés: Az OBJ fájl betöltésének testreszabása

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### 3. lépés: Az STL fájl betöltésének testreszabása

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### 4. lépés: Az U3D fájlbetöltés testreszabása

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### 5. lépés: A glTF fájlbetöltés testreszabása

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### 6. lépés: A PLY fájl betöltésének testreszabása

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### 7. lépés: Az X fájl betöltésének testreszabása

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### 8. lépés: FBX-fájlbetöltés testreszabása (opcionális)

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

## Következtetés

A 3D fájlbetöltés Java nyelven történő testreszabása az Aspose.3D LoadOptions szolgáltatásával lehetővé teszi a fejlesztők számára, hogy az importálási folyamatot a konkrét követelményekhez igazítsák. Legyen szó animációs transzformációk módosításáról, koordinátarendszerek átfordításáról vagy külső függőségek kezeléséről, az Aspose.3D biztosítja a zökkenőmentes integrációhoz szükséges rugalmasságot.

## GYIK

### 1. kérdés: Hol találom az Aspose.3D for Java dokumentációt?

 V1: A dokumentáció elérhető[itt](https://reference.aspose.com/3d/java/).

### 2. kérdés: Hogyan tölthetem le az Aspose.3D for Java-t?

 V2: Letöltheti[itt](https://releases.aspose.com/3d/java/).

### 3. kérdés: Van ingyenes próbaverzió?

 3. válasz: Igen, hozzáférhet az ingyenes próbaverzióhoz[itt](https://releases.aspose.com/).

### 4. kérdés: Hol kaphatok támogatást az Aspose.3D for Java számára?

 4. válasz: Látogassa meg a támogatási fórumot[itt](https://forum.aspose.com/c/3d/18).

### 5. kérdés: Szükségem van ideiglenes licencre a teszteléshez?

 V5: Igen, szerezzen ideiglenes engedélyt[itt](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
