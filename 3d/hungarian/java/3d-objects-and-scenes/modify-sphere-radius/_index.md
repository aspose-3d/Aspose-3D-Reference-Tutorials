---
date: 2025-11-30
description: Ismerje meg, hogyan használja az Aspose-t Java-ban egy 3D gömb sugarának
  módosításához. Ez a lépésről‑lépésre útmutató bemutatja az Aspose.3D Java könyvtárat,
  a sugár beállítását, a gömb hozzáadását a jelenethez, valamint az OBJ fájl Java‑ban
  történő írását.
language: hu
linktitle: 'How to Use Aspose: Modify 3D Sphere Radius in Java with Aspose.3D'
second_title: Aspose.3D Java API
title: 'Hogyan használjuk az Aspose-t: 3D gömb sugarának módosítása Java-ban az Aspose.3D
  segítségével'
url: /java/3d-objects-and-scenes/modify-sphere-radius/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hogyan használjuk az Aspose-ot: 3D gömb sugárának módosítása Java-ban az Aspose.3D-val

## Bevezetés

Ha **hogyan használjuk az Aspose-ot** szeretnéd megtudni 3D modellekkel Java-ban, jó helyen jársz. Ebben az útmutatóban lépésről lépésre végigvezetünk a gömb méretének módosításán, a jelenethez való hozzáadásán, és végül egy OBJ fájl írásán a **Aspose.3D Java könyvtár** segítségével. A végére egy újrahasználható kódrészletet kapsz, amelyet bármely Java‑alapú 3D alkalmazásba beilleszthetsz.

## Gyors válaszok
- **Mi a fő célja ennek az útmutatónak?** Az, hogy bemutassa, hogyan módosítható egy gömb sugara az Aspose.3D Java-ban.  
- **Melyik könyvtárat használjuk?** Az Aspose.3D Java könyvtár (egy teljes funkcionalitású **java 3d library**).  
- **Hogyan állítható be a sugár?** Hívd meg a `sphere.setRadius(double)` metódust egy `Sphere` objektumon.  
- **Exportálhatok OBJ formátumba?** Igen – használd a `scene.save("file.obj", FileFormat.WAVEFRONTOBJ)` hívást.  
- **Szükség van licencre?** Fejlesztéshez egy ingyenes próba elegendő; a termeléshez licenc szükséges.

## Mi az Aspose.3D Java-hoz?

Az Aspose.3D egy **java 3d library**, amely lehetővé teszi a fejlesztők számára 3D fájlok létrehozását, szerkesztését és konvertálását külső függőségek nélkül. Támogatja a népszerű formátumokat, mint az OBJ, FBX, STL és mások, így ideális játékokhoz, CAD eszközökhöz és tudományos megjelenítésekhez.

## Miért használjuk az Aspose.3D-t a gömb méretének módosításához?

- **Nincs szükség natív 3D motorra** – minden művelet az objektummodellen történik.  
- **Keresztplatformos** – működik minden Java‑t futtató operációs rendszeren.  
- **Nagy pontosságú geometria** – pontos sugárértékek állíthatók be, nem csak hozzávetőleges méretezés.  

## Előfeltételek

- Alapvető Java programozási ismeretek.  
- Aspose.3D könyvtár telepítve – letölthető a [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/) oldalról.  
- Java Development Kit (JDK) telepítve a gépeden.

## Csomagok importálása

A kezdéshez importáld a szükséges osztályokat a Java projektedbe:

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Sphere;

import java.io.IOException;
```

## 1. lépés: Jelenet inicializálása

```java
// ExStart:WorkingWithSphereRadius

// initialize a scene
Scene scene = new Scene();
```

Itt létrehozunk egy új **3D jelenetet**, amely a teljes geometriánkat tartalmazza.

## 2. lépés: Gömb inicializálása

```java
// initialize a Sphere
Sphere sphere = new Sphere();
```

A `Sphere` objektum egy tökéletes gömb primitívet képvisel. Jelen alapértelmezett 1.0 sugárral rendelkezik.

## 3. lépés: Gömb sugárának beállítása

```java
// set radius
sphere.setRadius(10);
```

Ez a sor bemutatja, **hogyan állítható be a sugár**. A `10` értéket bármely `double` értékre cserélheted a kívánt méret eléréséhez.

## 4. lépés: Gömb hozzáadása a jelenethez

```java
// add sphere to the scene
scene.getRootNode().createChildNode(sphere);
```

A hívás **hozzáadja a gömböt a jelenethez** (vagy „add sphere to scene”) egy gyermekcsomópont létrehozásával a gyökércsomópont alatt.

## 5. lépés: OBJ fájl írása Java-ban

```java
// save scene
scene.save("sphere.obj", FileFormat.WAVEFRONTOBJ);
```

Végül **OBJ fájlt írunk Java** stílusban a `scene.save` használatával. A kimeneti `sphere.obj` fájl bármely, a Wavefront OBJ formátumot támogató 3D megjelenítőben megnyitható.

## Gyakori problémák és megoldások

| Probléma | Megoldás |
|----------|----------|
| **A gömb túl kicsinek tűnik a megjelenítőben** | Ellenőrizd, hogy a sugár értéke helyesen van-e beállítva; tartsd szem előtt, hogy a mértékegységek tetszőlegesek, hacsak nem alkalmazol méretezési transzformációt. |
| **Az exportált OBJ-nak nincs anyaga** | Az Aspose.3D csak geometriát ír; ha textúrára van szükséged, adj anyagot a gömbhöz (`sphere.setMaterial(...)`). |
| **Licenc kivétel futásidőben** | Győződj meg róla, hogy a `Scene` létrehozása előtt betöltöttél egy ideiglenes vagy állandó licencfájlt. |

## Gyakran Ismételt Kérdések

### K: Hol találom az Aspose.3D for Java dokumentációját?

V: A részletes információkért és használati útmutatóért tekintsd meg a [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/) oldalt K: Hogyan tölthetem le az Asp for Java-t?

V: Töltsd le a könyvtárat a kiadási oldalról: [Download Aspose.3D for Java](https://releases.aspose.com/3d/java/).

### K: Van ingyenes próba az Aspose.3D for Java-hoz?

V: Igen, a funkciókat ingyenes próba verzióval is kipróbálhatod a [Aspose.3D Free Trial](https://releases.aspose.com/) oldalon.

### K: Hol kaphatok támogatást az Aspose.3D for Java-hoz?

V: Csatlakozz az Aspose közösséghez a [Aspose.3D Support Forum](https://forum.aspose.com/c/3d/18) oldalon segítségért és megbeszélésekért.

### K: Hogyan szerezhetek ideiglenes licencet az Aspose.3D-hez?

V: licencet a [Temporary License](https://purchase.aspose.com/temporary-license/) oldalon szerezhetsz.

### K: Használhatom ezt a kódot más 3D formátumokkal, például STL-lel?

V: Természetesen – csak cseréld le a `FileFormat` enumot a `scene.save` hívásakor, például `FileFormat.STL`.

## Összegzés

Most már elsajátítottad, **hogyan használjuk az Aspose-ot** a gömb sugárának módosításához, a jelenethez való hozzáadásához, és az eredmény OBJ fájlként való exportálásához Java-ban. Nyugodtan kísérletezz más primitívekkel, alkalmazz anyagokat, vagy láncolj több transzformációt a gazdagabb 3D modellek építéséhez.

---

**Last Updated:** 2025-11-30  
**Tested With:** Aspose.3D for Java 24.11  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}