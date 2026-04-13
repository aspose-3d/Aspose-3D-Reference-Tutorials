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

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hogyan állítsuk be az irányt lineáris extrudálásnál azpose.3D for A Java segítségével

## Bevezetés

Ebben az átfogó oktatóanyagban megtudja, **hogyan állítsuk be az irányt**, amikor lineáris extrudálást hajt végre az Aspose.3D for Java-val. Akár CAD‑szerű eszköz épít, akár geometriai adatokat generál játék egy motorhoz, az extrudálás irányának vezérlése lehetővé teszi, hogy pontosan a kívánt alakzatot hozza létre. Lépésről lépésre végigvezetjük a folyamatot, a profil inicializálásától a végeredmény OBJ fájlba mentéséig, így **exportálni 3d modell obj** fájlokat is közvetlenül Java‑ból.

## Gyors válaszok
- **Mi a fő osztály a lineáris extrudáláshoz?** `LinearExtrusion`
- **Melyik metódus pontosan meg az extrudálás irányát?** `setDirection(Vector3 direction)`
- **Exportálhatom az eredményt OBJ-ként?** Igen, a `scene.save(..., FileFormat.WAVEFRONTOBJ)` használja
- **Szükségem van licencre a fejlesztéshez?** Ingyenes próba elérhető; a termeléshez licenc szükséges.
- **Melyik Java IDE működik a legjobban?** Az IntelliJ IDEA vagy az Eclipse teljesen támogatott.

## Mi az a lineáris extrudálás?

A lineáris extrudálás egy 2‑D profil (egy téglalap vagy kör) kinyújtását jelenti egy egyenes vonal mentén, így 3‑D szilárd testet hozva létre. Alapértelmezés szerint az extrudálás pozitív Z‑tengely mentén történik, de az Aspose.3D‑vel a `setDirection` tulajdonság segítségével megváltoztathatja ezt az útvonalat.

## Miért állítsa be az irányt a lineáris extrudálásnál?

Egyedi irány beállítás hasznos, ha:
- A geometria illesztése objektumokhoz a jelenetben.
- Dőlt vagy ferde alkatrészek létrehozása extra transzformációs lépések nélkül.
- modellek exportálása, amelyeknek egy meghatározott koordináta-rendszernek kell megfelelniük (Olyan 3-D nyomtatáshoz vagy játék motorokhoz).

## Előfeltételek

Mielőtt elkezdenénk, g meg róla, hogy rendelkezik:

- Alapvető Java ismeretekkel.
- Telepített Aspose.3D könyvtárral. Letöltheti [itt](https://releases.aspose.com/3d/java/).
- Egy IDE‑vel, például Eclipse‑szel vagy IntelliJ IDEA‑val.

## Csomagok importálása

Először importálja azokat a névtereket, hogy a fő 3-D osztályokat és segédtípusokat biztosítsák.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 1. lépés: Alapprofil inicializálása

Hozza létre a kinyújtandó alakzatot. Ebben a példában egy `RectangleShape`‑t használunk kis lekerekítési sugárral, hogy a szélek simábbak legyenek.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## 2. lépés: Jelenet létrehozása

A `Scene` objektum minden 3‑D csomópont, fény, kamera és anyag tárolója.

```java
Scene scene = new Scene();
```

## 3. lépés: Csomópontok létrehozása

Adjon hozzá két gyermek‑csomópontot a jelenet gyökeréhez — egyik a bal‑oldali extrudáláshoz, másik a jobb‑oldali extrudáláshoz. A jobb csomópont el van tolva, hogy a két objektum ne fedje egymást.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## 4. lépés: Lineáris kihúzás végrehajtása a bal oldali csomóponton

Extrudálja a profilt a bal csomóponton az alapértelmezett Z‑tengely irányában. Emellett egy teljes 360°‑os csavart is hozzáadunk, és növeljük a szelet‑számot a simább háló érdekében.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## 5. lépés: Lineáris kihúzás végrehajtása a jobb oldali csomóponton az iránnyal

Itt **állítjuk be az irányt**. Egy egyedi `Vector3` átadásával a `setDirection`‑nek, az extrudálás a (0.3, 0.2, 1) vektor mentén történik, így ferde alakzatot kapunk.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## 6. lépés: 3D jelenet mentése

Végül exportálja a jelenetet Wavefront OBJ formátumba. Ez a lépés bemutatja, hogyan **exportálni obj fájl java** projektekben, és egyszerűvé teszi az eredmény megtekintését bármely 3‑D megjelenítőben.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Gyakori problémák és megoldások

| Probléma | Miért fordul elő | Megoldás |
|----------|-------------------------------|
| Az OBJ fájl üresnek tűnik | A profil nem lett hozzáadva egy csomóponthoz | G mind meg róla, hogy a `createChildNode` egy érvényes csomópontra van meghívva |
| Az irány változatlan marad | `setDirection` metódust az extrudálás már kész után hívták meg | Állítsa be az irányt a `LinearExtrusion` inicializálásakor, ahogy a példában látható |
| Alacsony felbontású háló | `setSlices` értéke túl alacsony | Növelje a szeletek számát (pl. 100 vagy több) |

## Következtetés

Most már tudja, **hogyan állítsuk be az irányt** egy lineáris extrudálásnál, hogyan módosíthatja a csavart és a szelet beállításokat, valamint hogyan **exportálni 3d modell obj** fájlokat az Aspose.3D for Java segítségével. Ezek a technikák finomhangolt vezérlést biztosítanak a geometria létrehozásához, és egyszerűvé teszik a 3-D eszközök integrálását nagyobb munkafolyamatokba.

## GYIK

### Q1: Használhatom az Aspose.3D‑t más programozási nyelvekkel?

Igen: az Aspose.3D több programozási nyelvet támogat, köztük a .NET-et és a Java-t.

### Q2. Elérhető ingyenes próba az Aspose.3D-hez?

Igen, a funkciókat ingyenes próba [itt](https://releases.aspose.com/) kipróbálhatja.

### Q3: Hol találtok részletes dokumentációt az Aspose.3D for Java‑hoz?

A teljes dokumentáció [itt](https://reference.aspose.com/3d/java/) elérhető el.

### Q4: Hogyan kaphatok támogatást az Aspose.3D‑hez?

Látogasson el az [Aspose.3D fórumra](https://forum.aspose.com/c/3d/18) bármilyen segítség vagy kérdés esetén.

### Q5: Elérhetők ideiglenes licencek az Aspose.3D-hez?

Igen, ideiglenes licencet [itt](https://purchase.aspose.com/temporary-license/) szerezhet.

---

**Utolsó frissítés:** 2026-02-22  
**Tesztelve:** Aspose.3D for Java (legújabb kiadás)  
**Szerző:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
