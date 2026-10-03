---
date: 2026-10-03
description: Ismerje meg, hogyan hozhat létre sphere java-t és exportálhat OBJ fájlt
  az Aspose.3D használatával, a vezető Java 3D library a 3D modellek konvertálásához.
images:
- /java/3d-objects-and-scenes/modify-sphere-radius/og-image.png
keywords:
- create sphere java
- save 3d as obj
- java convert 3d model
- write obj file java
lastmod: 2026-10-03
linktitle: 'Sphere java létrehozása: 3D konvertálása OBJ-re az Aspose.3D segítségével'
og_description: Ismerje meg, hogyan hozhat létre sphere java-t és exportálhat OBJ
  fájlt az Aspose.3D használatával. Ez a step‑by‑step útmutató bemutatja a gömb hozzáadását,
  a sugár módosítását és az OBJ formátumba mentést.
og_image_alt: 'Guide: create sphere java and export OBJ using Aspose.3D'
og_title: Sphere java – OBJ exportálása az Aspose.3D segítségével
schemas:
- author: Aspose
  dateModified: '2026-10-03'
  description: Learn how to create sphere java and export OBJ file using Aspose.3D,
    the leading Java 3D library for converting 3D models.
  headline: 'Create sphere java: Convert 3D to OBJ with Aspose.3D'
  type: TechArticle
- description: Learn how to create sphere java and export OBJ file using Aspose.3D,
    the leading Java 3D library for converting 3D models.
  name: 'Create sphere java: Convert 3D to OBJ with Aspose.3D'
  steps:
  - name: Initialize a Scene
    text: '**Definition anchor:** The `Scene` class is Aspose.3D''s top‑level container
      that holds geometry, lights, and cameras for a 3D model. Creating a `Scene`
      gives you a workspace where you can add and manipulate objects. Creating a `Scene`
      gives you a container for all geometry, lights, and cameras. This'
  - name: Initialize a Sphere
    text: '**Definition anchor:** The `Sphere` class represents a geometric sphere
      primitive with a configurable radius, center, and material. By default it starts
      with a radius of 1.0. A `Sphere` object starts with a default radius of 1.0.
      Think of it as a blank canvas for the shape you want to export.'
  - name: Set the Desired Radius
    text: The `setRadius(double)` method updates the sphere’s size by assigning a
      new radius value in the same units used by the scene. Here we **write obj file
      java**‑style code that sets the exact radius. Replace `10` with any `double`
      value that matches your design requirements.
  - name: Add Sphere to the Scene
    text: This line **adds sphere to scene** by creating a child node under the root
      node. It’s the moment the geometry becomes part of the scene graph.
  - name: Export the Model as OBJ
    text: The `save(String, FileFormat)` method writes the entire scene to the specified
      file using the chosen format, such as OBJ. Calling `scene.save` **exports obj
      file java**‑style, effectively **save scene as obj**. The generated `sphere.obj`
      can be opened in any standard 3D viewer.
  type: HowTo
- questions:
  - answer: You can refer to the [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/)
      for comprehensive guidance.
    question: Where can I find the documentation for Aspose.3D for Java?
  - answer: 'Download the library from the releases page: [Download Aspose.3D for
      Java](https://releases.aspose.com/3d/java/).'
    question: How do I download Aspose.3D for Java?
  - answer: Yes, explore the features with a free trial by visiting [Aspose.3D Free
      Trial](https://releases.aspose.com/).
    question: Is there a free trial available for Aspose.3D for Java?
  - answer: Join the Aspose community at [Aspose.3D Support Forum](https://forum.aspose.com/c/3d/18)
      for assistance and discussions.
    question: Where can I get support for Aspose.3D for Java?
  - answer: Get a temporary license by visiting [Temporary License](https://purchase.aspose.com/temporary-license/).
    question: How can I obtain a temporary license for Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- modify sphere radius
- export OBJ
- aspose.3d
- java 3d
- 3d conversion
title: 'Sphere java létrehozása: 3D konvertálása OBJ-re az Aspose.3D segítségével'
url: /hu/java/3d-objects-and-scenes/modify-sphere-radius/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Létrehozni gömböt Java-ban és exportálni OBJ-be

## Bevezetés

Ebben az útmutatóban megtanulod, hogyan **create sphere java**, állítsd be a sugárát, majd **save 3d as obj** használva az Aspose.3D Java könyvtárat. Végigvezetünk minden kódsoron, elmagyarázzuk, miért fontos az egyes lépések, és gyakorlati tippeket adunk, hogy magabiztosan beépíthesd ezt a munkafolyamatot játékokba, CAD eszközökbe vagy tudományos vizualizációkba.

## Gyors válaszok
- **Mi a fő célja ennek az útmutatónak?** Az, hogy bemutassa, hogyan kell create sphere java, módosítani a méretét, és exportálni a modellt OBJ formátumban Java használatával.
- **Melyik könyvtár biztosítja a 3D funkcionalitást?** Aspose.3D, egy teljes körű **java 3d library tutorial**.
- **Hogyan változtathatom meg a gömb méretét?** Hívd meg a `sphere.setRadius(double)` metódust a `Sphere` példányon.
- **Írhatok OBJ fájlt közvetlenül Java-ból?** Igen—használd a `scene.save("file.obj", FileFormat.WAVEFRONTOBJ)` metódust.
- **Szükségem van licencre a termeléshez?** Fejlesztéshez egy ingyenes próba elegendő; kereskedelmi használathoz állandó licenc szükséges.

## Mi az Aspose.3D for Java?

Az Aspose.3D for Java egy átfogó **java 3d library**, amely lehetővé teszi a fejlesztők számára, hogy külső függőségek nélkül hozzanak létre, szerkesszenek és konvertáljanak 3D fájlokat. Több mint **50 bemeneti és kimeneti formátumot** támogat, többek között OBJ, FBX, STL és GLTF, így zökkenőmentes integrációt biztosít bármely 3‑D csővezetékbe.

## Miért konvertáljuk a 3D-t OBJ-be?

Az OBJ-be konvertálás egy univerzálisan támogatott, egyszerű szöveges reprezentációt biztosít a geometriáról, amelyet bármely 3D eszköz be tud olvasni, így ideális gyors prototípusfejlesztéshez, platformok közötti eszközcserehez és a csúcspontadatok egyszerű hibakereséséhez. Mivel az OBJ fájlok könnyűek és ember által olvashatóak, szükség esetén egyszerű szövegszerkesztővel is megtekinthetők vagy módosíthatók.

## Előfeltételek

- Alapvető Java programozási ismeretek.  
- Aspose.3D könyvtár telepítve – töltsd le a [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/) oldalról.  
- JDK 8 vagy újabb telepítve a fejlesztői gépeden.

## Csomagok importálása

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Sphere;

import java.io.IOException;
```

## Hogyan módosítsuk a gömb sugarát Java-ban?

A `Sphere` egy geometriai primitív, amely egy gömböt reprezentál az Aspose.3D-ben.

Töltsd be a `Sphere` objektumot, hívd meg a `setRadius` metódust a kívánt értékkel, majd mentsd el a jelenetet OBJ-ként – ez a teljes munkafolyamat öt tömör lépésben elvégezhető. A megközelítés bármely numerikus sugárral működik, és garantálja, hogy az exportált OBJ pontosan a megadott méretet tükrözze.

### 1. lépés: Jelenet inicializálása

```java
// ExStart:WorkingWithSphereRadius

// initialize a scene
Scene scene = new Scene();
```

**Definíció horgony:** A `Scene` osztály az Aspose.3D legfelső szintű tárolója, amely geometriát, fényeket és kamerákat tartalmaz egy 3D modellhez. Egy `Scene` létrehozása egy munkaterületet ad, ahol objektumokat adhatsz hozzá és manipulálhatsz.

A `Scene` létrehozása egy tárolót biztosít minden geometriához, fényhez és kamerához. Itt fogjuk később **add sphere to scene**.

### 2. lépés: Gömb inicializálása

```java
// initialize a Sphere
Sphere sphere = new Sphere();
```

**Definíció horgony:** A `Sphere` osztály egy geometriai gömb primitívet reprezentál, amelynek sugara, középpontja és anyaga konfigurálható. Alapértelmezés szerint 1,0-es sugárral indul.

A `Sphere` objektum alapértelmezett sugara 1,0. Tekintsd úgy, mint egy üres vászonra a kívánt alak exportálásához.

### 3. lépés: A kívánt sugár beállítása

**Definíció horgony:** A `setRadius(double)` metódus beállítja a gömb sugarát ugyanabban a mértékegységben, amelyet a jelenet használ.

```java
// set radius
sphere.setRadius(10);
```

Itt **write obj file java**‑stílusú kódot írunk, amely beállítja a pontos sugarat. Cseréld le a `10`‑et bármely `double` értékre, amely megfelel a tervezési követelményeknek.

### 4. lépés: Gömb hozzáadása a jelenethez

```java
// add sphere to the scene
scene.getRootNode().createChildNode(sphere);
```

Ez a sor **adds sphere to scene** egy gyermekcsomópont létrehozásával a gyökércsomópont alatt. Ez az a pillanat, amikor a geometria a jelenet gráfjának részévé válik.

### 5. lépés: Modell exportálása OBJ-ként

```java
// save scene
scene.save("sphere.obj", FileFormat.WAVEFRONTOBJ);
```

A `save(String, FileFormat)` metódus az egész jelenetet a megadott fájlba írja a választott formátummal, például OBJ. A `scene.save` meghívása **exports obj file java**‑stílusban, hatékonyan **save scene as obj**. A létrehozott `sphere.obj` bármely szabványos 3D megjelenítőben megnyitható.

## Gyakori problémák és megoldások

| Probléma | Megoldás |
|-------|----------|
| **Sphere appears too small in the viewer** | Ellenőrizd, hogy a sugár értéke helyesen van beállítva; ne feledd, hogy a mértékegységek tetszőlegesek, hacsak nem alkalmazol skálázási transzformációt. |
| **Exported OBJ has no material** | Az Aspose.3D csak geometriát ír; adj anyagot a gömbhöz, ha textúrára van szükség (`sphere.setMaterial(...)`). |
| **License exception at runtime** | Győződj meg róla, hogy a `Scene` létrehozása előtt betöltöttél egy ideiglenes vagy állandó licencfájlt. |

## Gyakran ismételt kérdések

**K: Hol találom az Aspose.3D for Java dokumentációját?**  
V: A [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/) részletes útmutatót nyújt.

**K: Hogyan tölthetem le az Aspose.3D for Java-t?**  
V: Töltsd le a könyvtárat a kiadások oldaláról: [Download Aspose.3D for Java](https://releases.aspose.com/3d/java/).

**K: Van ingyenes próba az Aspose.3D for Java-hoz?**  
V: Igen, a funkciókat ingyenes próba verzióval is kipróbálhatod a [Aspose.3D Free Trial](https://releases.aspose.com/) oldalon.

**K: Hol kaphatok támogatást az Aspose.3D for Java-hoz?**  
V: Csatlakozz az Aspose közösséghez a [Aspose.3D Support Forum](https://forum.aspose.com/c/3d/18) oldalon segítségért és megbeszélésekért.

**K: Hogyan szerezhetek ideiglenes licencet az Aspose.3D-hez?**  
V: Ideiglenes licencet a [Temporary License](https://purchase.aspose.com/temporary-license/) oldalon kaphatsz.

**K: Használhatom ezt a kódot más 3D formátumokkal, például STL-lel?**  
V: Természetesen – csak cseréld le a `FileFormat` enumot a `scene.save` hívásakor, pl. `FileFormat.STL`.

---

**Utolsó frissítés:** 2026-10-03  
**Tesztelve ezzel:** Aspose.3D for Java 24.11  
**Szerző:** Aspose

## Kapcsolódó útmutatók

- [Hogyan állítsuk be a normálvektorokat 3D objektumokon Java-ban az Aspose.3D Java API használatával](/3d/java/geometry/set-up-normals-on-3d-objects/)
- [Hogyan ágyazzunk be textúrát FBX-be Java-val – Anyagok alkalmazása 3D objektumokra az Aspose.3D használatával](/3d/java/geometry/apply-materials-to-3d-objects/)
- [Hogyan változtassuk meg a sík orientációját és exportáljuk OBJ-be Java-ban](/3d/java/3d-scenes-and-models/change-plane-orientation/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}