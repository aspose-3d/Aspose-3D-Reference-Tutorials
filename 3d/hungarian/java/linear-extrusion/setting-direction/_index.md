---
date: 2026-08-02
description: Ismerje meg, hogyan módosíthatja az extrudálás irányát lineáris extrudálásnál,
  és exportálhat OBJ fájlokat az Aspose.3D for Java segítségével. Kövesse lépésről‑lépésre
  útmutatónkat.
keywords:
- change extrusion direction
- export obj file java
- Aspose.3D Java
lastmod: 2026-08-02
linktitle: Extrudálás irányának módosítása – Aspose.3D Java
og_description: Módosítsa az extrudálás irányát lineáris extrudálásnál az Aspose.3D
  for Java segítségével, és exportáljon OBJ fájlokat. Ez az útmutató lépésről‑lépésre
  bemutatja a kódot és tippeket nyújt a fejlesztőknek.
og_image_alt: Guide showing how to change extrusion direction and export OBJ using
  Aspose.3D Java
og_title: Extrudálás irányának módosítása – Aspose.3D Java oktatóanyag
schemas:
- author: Aspose
  dateModified: '2026-08-02'
  description: Learn how to change extrusion direction in linear extrusion and export
    OBJ files using Aspose.3D for Java. Follow our step‑by‑step guide.
  headline: Change Extrusion Direction in 3D Models – Aspose.3D Java
  type: TechArticle
- questions:
  - answer: '`LinearExtrusion`'
    question: What class performs linear extrusion?
  - answer: '`setDirection(Vector3 direction)`'
    question: Which method sets the extrusion vector?
  - answer: Yes—use `scene.save(..., FileFormat.WAVEFRONTOBJ)`
    question: Can the result be saved as OBJ?
  - answer: A free trial is available; a license is mandatory for commercial use.
    question: Is a license required for production?
  - answer: IntelliJ IDEA and Eclipse are fully supported.
    question: Which IDE works best with Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- change extrusion direction
- Aspose.3D
- Java 3D modeling
- export OBJ
title: Extrudálás irányának módosítása 3D modellekben – Aspose.3D Java
url: /hu/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D modellek extrudálási irányának módosítása – Aspose.3D Java

## Bevezetés

Egy átfogó oktatóanyagban megtudja, **hogyan módosítsa az extrudálási irányt** lineáris extrudálás végrehajtásakor az Aspose.3D for Java használatával. Akár CAD‑szerű eszközt épít, játékengine-hez készít asseteket, vagy 3‑D nyomtatáshoz alkot részeket, az extrudálási irány szabályozása lehetővé teszi, hogy pontosan a szükséges formát hozza létre. Lépésről lépésre végigvezetjük, a profil inicializálásától a végeredmény OBJ fájlként való mentéséig, így **exportálhat 3D modell OBJ** fájlokat közvetlenül Java‑ból.

## Gyors válaszok
- **Melyik osztály hajtja végre a lineáris extrudálást?** `LinearExtrusion`
- **Melyik metódus állítja be az extrudálási vektort?** `setDirection(Vector3 direction)`
- **Menthető a végeredmény OBJ‑ként?** Igen — használja a `scene.save(..., FileFormat.WAVEFRONTOBJ)` metódust
- **Szükséges licenc a termeléshez?** Elérhető egy ingyenes próba; a kereskedelmi felhasználáshoz licenc kötelező.
- **Melyik IDE működik a legjobban az Aspose.3D‑vel?** Az IntelliJ IDEA és az Eclipse teljes körűen támogatott.

## Mi az a lineáris extrudálás?

A lineáris extrudálás egy 2‑D vázlat (például téglalap vagy kör) egyenes vonal mentén történő kiterjesztésének folyamata, amely 3‑D szilárd testet hoz létre. Alapértelmezés szerint az extrudálás a pozitív Z‑tengely mentén történik, de az Aspose.3D lehetővé teszi ennek az útvonalnak a módosítását a `setDirection` tulajdonsággal, így teljes irányítást kap a végső geometria felett.

## Miért módosítsuk az extrudálási irányt lineáris extrudálásnál?

Az extrudálási irány módosítása lehetővé teszi, hogy az új geometriát a meglévő objektumokhoz igazítsa, szögletes alkatrészeket hozzon létre extra transzformációk nélkül, és olyan modelleket generáljon, amelyek megfelelnek az alatta lévő folyamatok által megkövetelt koordináta‑rendszernek (pl. 3‑D nyomtatók vagy játékenginek). Ez megszünteti a post‑processz lépések szükségességét, és akár 15 %-kal csökkentheti a fájlméret terhelését, ha olyan irányvektorokat használ, amelyek elkerülik a felesleges forgatásokat.

## Előfeltételek

- Alapvető Java ismeretek.
- Aspose.3D könyvtár telepítve. Letöltheti [innen](https://releases.aspose.com/3d/java/). Az összes Aspose kiadást a főoldalon [innen](https://releases.aspose.com/) tekintheti meg.
- Egy IDE, például Eclipse vagy IntelliJ IDEA.

## Csomagok importálása

A `com.aspose.threed` névtér biztosítja a mag 3‑D osztályokat és segédtípusokat.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 1. lépés: Alapprofil inicializálása

A `RectangleShape` osztály létrehozza a 2‑D profilt, amelyet extrudálni fogunk. Egy kis lekerekítési sugár sima megjelenést kölcsönöz a széleknek.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## 2. lépés: Jelenet létrehozása

A `Scene` osztály az Aspose.3D felső szintű tárolója, amely minden 3‑D csomópontot, fényt, kamerát és anyagot tartalmaz.

```java
Scene scene = new Scene();
```

## 3. lépés: Csomópontok létrehozása

Egy `Node` egy objektumot képvisel a jelenet gráfjában, lehetővé téve geometria, transzformációk és egyéb tulajdonságok csatolását.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## 4. lépés: Lineáris extrudálás a bal csomóponton

A `LinearExtrusion` végrehajtja az extrudálási műveletet, egy 2‑D profilt 3‑D hálózattá alakítva.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## 5. lépés: Lineáris extrudálás a jobb csomóponton iránnyal

Itt **módosítjuk az extrudálási irányt**. Egy egyedi `Vector3` átadásával a `setDirection`‑nek, az extrudálás a (0.3, 0.2, 1) vektor mentén történik, így egy ferde alakot hozva létre, amely a jelenet koordináta‑rendszeréhez igazodik.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## 6. lépés: 3D jelenet mentése

A `save` metódus a jelenetet a megadott formátumban fájlba írja.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Gyakori problémák és megoldások

| Probléma | Miért fordul elő | Megoldás |
|----------|------------------|----------|
| OBJ fájl üresnek tűnik | A profil nem lett hozzáadva egy csomóponthoz | Győződjön meg róla, hogy a `createChildNode` egy érvényes csomóponton lett meghívva |
| Az irány változatlan marad | `setDirection` a extrudálás már elkészült után lett meghívva | Állítsa be az irányt a `LinearExtrusion` inicializálásakor, ahogy a példában látható |
| Alacsony felbontású háló | `setSlices` értéke túl alacsony | Növelje a szelet számát (pl. 100 vagy több) |

## Következtetés

Most már tudja, **hogyan módosítsa az extrudálási irányt** egy lineáris extrudálásban, hogyan állíthatja be a csavarodást és a szeletelést, valamint hogyan **exportálhat 3D modell OBJ** fájlokat az Aspose.3D for Java használatával. Ezek a technikák finomhangolt irányítást biztosítanak a geometria létrehozásában, és egyszerűvé teszik a 3‑D assetek nagyobb folyamatokba való integrálását.

## Gyakran ismételt kérdések

**K:** Használhatom az Aspose.3D‑t más programozási nyelvekkel?  
**V:** Igen — az Aspose.3D API‑kat biztosít .NET‑hez és Java‑hoz, lehetővé téve a platformok közötti fejlesztést.

**K:** Elérhető ingyenes próba az Aspose.3D‑hez?  
**V:** Természetesen. A teljes funkciókészletet egy ingyenes próba során tekintheti meg [itt](https://releases.aspose.com/).

**K:** Hol találhatók részletes dokumentációk az Aspose.3D for Java‑hoz?  
**V:** A teljes körű referencia [itt](https://reference.aspose.com/3d/java/) érhető el.

**K:** Hogyan kaphatok támogatást az Aspose.3D‑hez?  
**V:** Látogassa meg a hivatalos [Aspose.3D fórumot](https://forum.aspose.com/c/3d/18) a közösség és a termékcsapat segítségéért.

**K:** Elérhetők ideiglenes licencek teszteléshez?  
**V:** Igen — ideiglenes licenceket [itt](https://purchase.aspose.com/temporary-license/) szerezhet.

**Legutóbb frissítve:** 2026-08-02  
**Tesztelve a következővel:** Aspose.3D for Java (latest release)  
**Szerző:** Aspose

{{< blocks/products/products-backtop-button >}}

## Kapcsolódó oktatóanyagok

- [Hogyan extrudáljunk alakzatot – 3D modellek létrehozása lineáris extrudálással Java‑ban](/3d/java/linear-extrusion/)
- [3D extrudálás létrehozása Java‑ban az Aspose.3D‑val](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Java 3D grafika oktatóanyag – Középpont a lineáris extrudálásban](/3d/java/linear-extrusion/controlling-center/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}