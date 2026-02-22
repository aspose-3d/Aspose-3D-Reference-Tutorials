---
date: 2026-02-22
description: Tanulja meg, hogyan állíthatja be az irányt lineáris extrúzióban, és
  exportálhatja a 3D-s OBJ modellt az Aspose.3D for Java segítségével. Kövesse lépésről‑lépésre
  útmutatónkat.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Hogyan állítsuk be az irányt lineáris extrúzióban az Aspose.3D for Java segítségével
url: /hu/java/linear-extrusion/setting-direction/
weight: 12
---

 block placeholders.

Let's construct final answer.{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hogyan állítsuk be az irányt lineáris extrudálásnál az Aspose.3D for Java használatával

## Introduction

Ebben az átfogó oktatóanyagban megtudja, **hogyan állítsuk be az irányt**, amikor lineáris extrudálást hajt végre az Aspose.3D for Java-val. Akár CAD‑szerű eszközt épít, akár geometriai adatokat generál egy játék motorhoz, az extrudálás irányának vezérlése lehetővé teszi, hogy pontosan a kívánt alakzatot hozza létre. Lépésről lépésre végigvezetjük a folyamatot, a profil inicializálásától a végeredmény OBJ fájlba mentéséig, így **exportálni 3d modell obj** fájlokat is közvetlenül Java‑ból.

## Quick Answers
- **Mi a fő osztály a lineáris extrudáláshoz?** `LinearExtrusion`
- **Melyik metódus határozza meg az extrudálás irányát?** `setDirection(Vector3 direction)`
- **Exportálhatom az eredményt OBJ‑ként?** Igen, a `scene.save(..., FileFormat.WAVEFRONTOBJ)` használatával
- **Szükségem van licencre a fejlesztéshez?** Ingyenes próba elérhető; a termeléshez licenc szükséges.
- **Melyik Java IDE működik a legjobban?** Az IntelliJ IDEA vagy az Eclipse teljes mértékben támogatott.

## What is Linear Extrusion?

A lineáris extrudálás egy 2‑D profil (például egy téglalap vagy kör) kinyújtását jelenti egy egyenes vonal mentén, így 3‑D szilárd testet hozva létre. Alapértelmezés szerint az extrudálás a pozitív Z‑tengely mentén történik, de az Aspose.3D‑vel a `setDirection` tulajdonság segítségével megváltoztathatja ezt az útvonalat.

## Why Set Direction in Linear Extrusion?

Egyedi irány beállítása hasznos, ha:
- A geometria illesztése meglévő objektumokhoz a jelenetben.
- Dőlt vagy ferde alkatrészek létrehozása extra transzformációs lépések nélkül.
- Olyan modellek exportálása, amelyeknek egy meghatározott koordináta‑rendszernek kell megfelelniük (például 3‑D nyomtatáshoz vagy játék motorokhoz).

## Prerequisites

Mielőtt elkezdenénk, győződjön meg róla, hogy rendelkezik:

- Alapvető Java ismeretekkel.
- Telepített Aspose.3D könyvtárral. Letöltheti [itt](https://releases.aspose.com/3d/java/).
- Egy IDE‑vel, például Eclipse‑szel vagy IntelliJ IDEA‑val.

## Import Packages

Először importálja azokat a névtereket, amelyek a fő 3‑D osztályokat és segédtípusokat biztosítják.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Step 1: Initialize Base Profile

Hozza létre a kinyújtandó alakzatot. Ebben a példában egy `RectangleShape`‑t használunk kis lekerekítési sugárral, hogy a szélek simábbak legyenek.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Step 2: Create a Scene

A `Scene` objektum minden 3‑D csomópont, fény, kamera és anyag tárolója.

```java
Scene scene = new Scene();
```

## Step 3: Create Nodes

Adjon hozzá két gyermek‑csomópontot a jelenet gyökeréhez — egyik a bal‑oldali extrudáláshoz, másik a jobb‑oldali extrudáláshoz. A jobb csomópont el van tolva, hogy a két objektum ne fedje egymást.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Step 4: Perform Linear Extrusion on the Left Node

Extrudálja a profilt a bal csomóponton az alapértelmezett Z‑tengely irányában. Emellett egy teljes 360°‑os csavart is hozzáadunk, és növeljük a szelet‑számot a simább háló érdekében.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Step 5: Perform Linear Extrusion on the Right Node with Direction

Itt **állítjuk be az irányt**. Egy egyedi `Vector3` átadásával a `setDirection`‑nek, az extrudálás a (0.3, 0.2, 1) vektor mentén történik, így ferde alakzatot kapunk.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Step 6: Save 3D Scene

Végül exportálja a jelenetet Wavefront OBJ formátumba. Ez a lépés bemutatja, hogyan **exportálni obj fájl java** projektekben, és egyszerűvé teszi az eredmény megtekintését bármely 3‑D megjelenítőben.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Common Issues and Solutions

| Probléma | Miért fordul elő | Megoldás |
|----------|------------------|----------|
| Az OBJ fájl üresnek tűnik | A profil nem lett hozzáadva egy csomóponthoz | Győződjön meg róla, hogy a `createChildNode` egy érvényes csomópontra van meghívva |
| Az irány változatlan marad | `setDirection` metódust az extrudálás már elkészült után hívták meg | Állítsa be az irányt a `LinearExtrusion` inicializálásakor, ahogy a példában látható |
| Alacsony felbontású háló | `setSlices` értéke túl alacsony | Növelje a szeletek számát (pl. 100 vagy több) |

## Conclusion

Most már tudja, **hogyan állítsuk be az irányt** egy lineáris extrudálásnál, hogyan módosíthatja a csavart és a szelet beállításokat, valamint hogyan **exportálni 3d modell obj** fájlokat az Aspose.3D for Java segítségével. Ezek a technikák finomhangolt vezérlést biztosítanak a geometria létrehozásához, és egyszerűvé teszik a 3‑D eszközök integrálását nagyobb munkafolyamatokba.

## FAQ's

### Q1: Használhatom az Aspose.3D‑t más programozási nyelvekkel?

Igen: az Aspose.3D több programozási nyelvet támogat, köztük a .NET‑et és a Java‑t.

### Q2. Elérhető ingyenes próba az Aspose.3D‑hez?

Igen, a funkciókat ingyenes próba [itt](https://releases.aspose.com/) kipróbálhatja.

### Q3: Hol találok részletes dokumentációt az Aspose.3D for Java‑hoz?

A teljes dokumentáció [itt](https://reference.aspose.com/3d/java/) érhető el.

### Q4: Hogyan kaphatok támogatást az Aspose.3D‑hez?

Látogasson el az [Aspose.3D fórumra](https://forum.aspose.com/c/3d/18) bármilyen segítség vagy kérdés esetén.

### Q5: Elérhetők ideiglenes licencek az Aspose.3D‑hez?

Igen, ideiglenes licencet [itt](https://purchase.aspose.com/temporary-license/) szerezhet.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Utolsó frissítés:** 2026-02-22  
**Tesztelve:** Aspose.3D for Java (legújabb kiadás)  
**Szerző:** Aspose