---
date: 2025-12-09
description: Tanulja meg, hogyan adjon hozzá gyermekcsomópontot, helyezze el a 3D
  objektumokat, és mentse a jelenetet OBJ formátumban, miközben egyedi ventilátorhengereket
  hoz létre az Aspose.3D for Java segítségével.
language: hu
linktitle: Adding Child Node for Fan Cylinders with Aspose.3D Java
second_title: Aspose.3D Java API
title: Gyermekcsomópont hozzáadása a ventilátor hengerének építéséhez az Aspose.3D
  for Java-val
url: /java/cylinders/creating-fan-cylinders/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Gyermekcsomópont hozzáadása a ventilátor hengerkészítéshez az Aspose.3D for Java-val

## Bevezetés

Készen állsz **gyermekcsomópont hozzáadására** egy 3‑D jelenethez, és látványos ventilátor hengerek létrehozására? Ebben az útmutatóban minden lépést végigvezetünk – a jelenet beállításától, a 3D objektumok pozicionálásáig, egészen a **jelenet OBJ formátumba mentéséig** – az Aspose.3D for Java használatával. Akár egy játékeszközt finomítasz, akár egy gyors prototípust építesz, a bemutatott koncepciók szilárd irányítást adnak a 3‑D modellek felett.

## Gyors válaszok
- **Mi a “gyermekcsomópont hozzáadása”?** Új objektumot szúr be a jelenet gráfjába, örökölve a transzformációkat a szülőjétől.  
- **Hogyan tudok egy 3D objektumot pozicionálni?** A csomópont transzformációjára alkalmazott eltolással (vagy forgatással/méretezéssel).  
- **Melyik fájlformátumot használják az exportáláshoz?** A példa a modellt Wavefront OBJ fájlként menti.  
- **Szükségem van licencre a kód futtatásához?** Egy ingyenes próba a kiértékeléshez működik; licenc szükséges a termeléshez.  
- **Melyik IDE a legjobb?** Bármely Java IDE (IntelliJ IDEA, Eclipse, VS Code), amely támogatja a JDK 8+ verziót.

## Mi a “gyermekcsomópont hozzáadása” az Aspose.3D-ban?
A gyermekcsomópont hozzáadása azt jelenti, hogy egy új csomópontot hozunk létre egy már létező szülő alatt a jelenet hierarchiájában. A gyermek örökli a szülő koordináta‑rendszerét, így egyszerűen **pozicionálhatók a 3d objektum** példányok egymáshoz képest.

## Miért adjunk hozzá gyermekcsomópontot ventilátor hengerek építésekor?
- **Moduláris tervezés:** Minden henger (ventilátor vagy nem‑ventilátor) saját csomópontban él, ami egyszerűsíti a későbbi módosításokat.  
- **Transzformáció öröklése:** A szülő mozgatása, forgatása vagy méretezése esetén az összes gyermek automatikusan követi.  
- **Tisztább jelenet gráf:** Javítja az olvashatóságot és a hibakeresést összetett modellek esetén.

## Előkövetelmények

- **Java Development Kit (JDK)** – töltsd le a [hivatalos oldalról](https://www.oracle.com/java/technologies/javase-downloads.html).  
- **Aspose.3D for Java** – szerezd be a legújabb könyvtárat a [letöltési hivatkozásról](https://releases.aspose.com/3d/java/).

## Csomagok importálása

Kezdjük a szükséges csomagok importálásával a Java projektedbe. Ez a lépés elengedhetetlen az Aspose.3D által biztosított funkciók eléréséhez.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 1. lépés: Jelenet létrehozása

Először egy üres 3‑D jelenetet hozunk létre, amely minden objektumunkat befogja.

```java
// ExStart:2
// Create a Scene
Scene scene = new Scene();
// ExEnd:2
```

## 2. lépés: Ventilátor henger létrehozása

Ezután egy hengert építünk, amely ventilátorként (részleges szögben) lesz renderelve.

```java
// ExStart:3
// Create a cylinder with fan
Cylinder fan = new Cylinder(2, 2, 10, 20, 1, false);
fan.setGenerateFanCylinder(true);
fan.setThetaLength(MathUtils.toRadian(270.0));
// ExEnd:3
```

## 3. lépés: Gyermekcsomópont hozzáadása és 3D objektum pozicionálása

Most **gyermekcsomópontot adunk hozzá** a jelenethez, és **pozicionáljuk a 3d objektumot** a transzláció beállításával. Itt válik a ventilátor henger a jelenet gráf részévé.

```java
// ExStart:4
// Create ChildNode and set translation
scene.getRootNode().createChildNode(fan).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

## 4. lépés: Nem‑ventilátor henger létrehozása

Az Aspose.3D rugalmasságának bemutatására egy hagyományos hengert is létrehozunk, ventilátor nélkül, és egy újabb gyermekcsomópontként adjuk hozzá.

```java
// ExStart:5
// Create a cylinder without a fan
Cylinder nonfan = new Cylinder(2, 2, 10, 20, 1, false);
// Create ChildNode
scene.getRootNode().createChildNode(nonfan);
// ExEnd:5
```

## 5. lépés: Jelenet mentése OBJ formátumba

Végül **mentjük a jelenetet OBJ‑ként**, hogy a végeredményt bármely szabványos 3‑D megjelenítőben megtekinthesd.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

Gratulálunk! Sikeresen **hozzáadtad a gyermekcsomópontot**, pozicionáltad az objektumokat, és exportáltad a modellt.

## Gyakori problémák és tippek

| Probléma | Megoldás |
|----------|----------|
| **File not found** mentéskor | Győződj meg róla, hogy a célkönyvtár létezik, és van írási jogosultságod. |
| **Cylinder appears flat** | Ellenőrizd a sugár és magasság értékeket; az Aspose.3D ugyanabban a skálában várja az egységeket. |
| **Fan slice looks incomplete** | `ThetaLength` (radiánban) értékének módosításával állítsd be a kívánt szöget. |
| **Scene not visible in viewer** | Ellenőrizd, hogy az OBJ fájl a megfelelő `.mtl` (anyag) fájllal együtt lett-e mentve, ha szükséges. |

## Gyakran Ismételt Kérdések

**Q:** *Az Aspose.3D kompatibilis más Java könyvtárakkal a 3D modellezéshez?*  
**A:** Igen, az Aspose.3D más Java 3‑D könyvtárakkal együtt működik, lehetővé téve a funkciók kombinálását igény szerint.

**Q:** *Testreszabhatom a generált ventilátor hengerek megjelenését tovább?*  
**A:** Természetesen. Anyagokat, textúrákat és megvilágítást alkalmazhatsz a `Material` és `Light` osztályok használatával.

**Q:** *Hol találok további támogatást vagy segítséget az Aspose.3D-hez?*  
**A:** Látogasd meg az [Aspose.3D fórumot](https://forum.aspose.com/c/3d/18) a közösségi segítségért és hivatalos válaszokért.

**Q:** *Elérhető ingyenes próba az Aspose.3D-hez?*  
**A:** Igen, a vásárlás előtt felfedezheted az Aspose.3D-t egy [ingyenes próbával](https://releases.aspose.com/) .

**Q:** *Hogyan szerezhetek ideiglenes licencet az Aspose.3D-hez?*  
**A:** Ideiglenes licencet szerezhetsz [itt](https://purchase.aspose.com/temporary-license/) teszteléshez és fejlesztéshez.

## Következtetés

Ebben az útmutatóban bemutattuk, hogyan **adjunk hozzá gyermekcsomópontot**, **pozicionáljuk a 3d objektumot**, és **mentsük a jelenetet OBJ‑ként**, miközben testreszabott ventilátor hengereket hozunk létre az Aspose.3D for Java segítségével. Ezek az építőelemek rugalmasságot biztosítanak összetett 3‑D hierarchiák felépítéséhez és exportálásához bármely további munkafolyamat számára.

---

**Last Updated:** 2025-12-09  
**Tested With:** Aspose.3D 24.12 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}