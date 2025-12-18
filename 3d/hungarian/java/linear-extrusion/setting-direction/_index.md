---
date: 2025-12-18
description: Tanulja meg, hogyan hozhat létre 3D-s jelenetet és menthet OBJ fájlt
  az Aspose.3D for Java segítségével. Kövesse lépésről‑lépésre útmutatónkat a lineáris
  extrudálási irányhoz.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: 3D-színter létrehozása – Extrudálás irányának beállítása Aspose.3D Java
url: /hu/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D jelenet létrehozása – Extrudálási irány beállítása Aspose.3D Java

## Introduction

Ebben az útmutatóban megtanulja, hogyan **hozzon létre 3D jelenetet** objektumokat, és hogyan szabályozza az extrudálás irányát az Aspose.3D for Java segítségével. Akár építészeti vizualizációkat, termékprototípusokat vagy játékeszközöket készít, a lineáris extrudálás elsajátítása rugalmasságot biztosít a bonyolult formák gyors modellezéséhez. Lépésről lépésre végigvezetjük a folyamaton, a Java-ban történő csomópontok hozzáadásától a **3D modell OBJ exportálásáig**, hogy azonnal láthassa az eredményt.

## Quick Answers
- **Mi a jelentése a „create 3d scene” kifejezésnek?** Ez azt jelenti, hogy inicializál egy Aspose.3D `Scene` objektumot, amely az összes geometriai adatot, fényt és kamerát tartalmazza.  
- **Hogyan állíthatom be az extrudálás irányát?** Használja a `setDirection(Vector3)` metódust egy `LinearExtrusion` példányon.  
- **Melyik formátumot használjam az exportáláshoz?** Az OBJ formátum (`FileFormat.WAVEFRONTOBJ`) széles körben támogatott a ‑D munkafolyamatokban.  
- **Szükségem van licencre az Aspose.3D-hez?** A ingyenes próba verzió fejlesztéshez megfelelő; a gyártási környezethez kereskedelmi licenc szükséges.  
- **Hozzáadhatok további csomópontokat Java-ban?** Igen – használja a `scene.getRootNode().createChildNode()` metódust, hogy a szükséges számú objektumot hozzáadja.

## What is a “create 3d scene” workflow?

A **create 3d scene** munkafolyamat egy üres `Scene` objektummal kezdődik, hozzáadja a geometriát (például extrudált profilokat), átalakításokkal pozícionálja, majd végül elmenti a jelenetet egy, például OBJ formátumú fájlba. Ez a minta az Aspose.3D-vel épített legtöbb 3‑D alkalmazás gerince.

## Why set extrusion direction?

Az extrudálás irányának beállítása lehetővé teszi, hogy a forma extrudálás közben dőljön, forgasson vagy ferde legyen, így a végső geometria felett extra utófeldolgozás nélkül isányítható. Különösen hasznos:
- Tölcséres oszlopok vagy egyedi alakú csövek létrehozása.  
- Extrudálások igazítása nem szabványos tengelyekhez mechanikai alkatrészekben.  
- Művészi formák generálása vizuális effektekhez.

## Prerequisites

Mielőtt elkezdenénk, győződjön meg róla, hogy rendelkezik:
- Alapvető Java ismeretekkel.  
- Telepített Aspose.3D könyvtárral – töltse le [innen](https://releases.aspose.com/3d/java/).  
- Egy IDE-vel, például Eclipse vagy IntelliJ IDEA.

## Import Packages

Először importálja a szükséges Aspose.3D osztályokat:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Step 1: Initialize Base Profile

Hozza létre a 2‑D profilt, amelyet extrudálni fog. Ebben a példában egy lekerekített téglalapot használunk:

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

> **Pro tip:** Állítsa be a lekerekítési sugárértéket, hogy szabályozza, mennyire éles vagy sima lesz a téglalap sarkai az extrudálás előtt.

## Step 2: Create a Scene

Most **létrehozzuk a 3d jelenetet**, amely a objektumainkat fogja tartalmazni:

```java
Scene scene = new Scene();
```

## Step 3: Add Nodes Java – Positioning the Objects

Két gyermekcsomópontot (bal és jobb) adunk a jelenet gyökércsomópontjához, és a balikát egy kicsit oldalra helyezzük:

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Step 4: How to extrude – Left Node (default direction)

Extrudálja a profilt a bal csomóponton az alapértelmezett Z‑tengely irányában. Emellett beállítunk egy teljes 360°-os csavart, és növeljük a szeletek számát a simaság érdekében:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Step 5: How to set direction – Right Node

Itt **beállítjuk az irányt** egy egyedi `Vector3` megadásával. Ez a extrudálást a (0.3, 0.2, 1) vektor felé dönti:

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Step 6: Save OBJ file – Export 3D model

Végül **elmentjük az OBJ fájlt**, hogy az eredményt bármely 3‑D megjelenítőben láthassa:

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Amikor megnyitja a generált OBJ fájlt, két extrudált téglalapot fog látni: egyet az alapértelmezett irányban, a másikat a beállított vektor szerint döntve.

## Common Issues and Solutions

| Probléma | Ok | Megoldás |
|----------|----|----------|
| Az OBJ fájl üresnek tűnik | A jelenet nincs mentve vagy az útvonal helytelen | Ellenőrizze, hogy a `MyDir` írható mappára mutat, és a fájlnév `.obj`-re végződik. |
| Az extrudálás laposnak tűnik | `setSlices` túl alacsony | Növelje a `setSlices` értékét (pl. 200) a simább geometria érdekében. |
| Az irány változatlan marad | A vektor nincs normalizálva | Használjon normalizált `Vector3`-at, vagy állítsa be az értékeket a kívánt dőlésszög eléréséhez. |

## Frequently Asked Questions

### Q1: Használhatom az Aspose.3D-t más programozási nyelvekkel?
A1: Az Aspose3D számos nyelvet támogat, többek között a .NET-et és a Java-t.

### Q2: Elérhető ingyenes próba verzió az Aspose.3D-hez?
A2: Igen, az Aspose.3D funkcióit ingyenes próba verzióval [itt](https://releases.aspose.com/) tekintheti meg.

### Q3: Hol találhatók részletes dokumentációk az Aspose.3D Java-hoz?
A3: A teljes körű dokumentáció [itt](https://reference.aspose.com/3d/java/) érhető el.

### Q4: Hogyan kaphatok támogatást az Aspose.3D-hez?
A4: Látogassa meg az [Aspose.3D fórumot](https://forum.aspose.com/c/3d/18) bármilyen segítség vagy kérdés esetén.

### Q5: Elérhetők ideiglenes licencek az Aspose.3D-hez?
A5: Igen, ideiglenes licencet szerezhet [itt](https://purchase.aspose.com/temporary-license/).

---

**Last Updated:** 2025-12-18  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}