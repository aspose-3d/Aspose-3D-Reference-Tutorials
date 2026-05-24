---
date: 2026-05-24
description: Ismerje meg, hogyan hozhat létre 3D extrudálást szeletekkel az Aspose.3D
  for Java használatával. Ez a lépésről‑lépésre útmutató a linear extrusion, a set
  rounding radius és az OBJ exportálását tárgyalja.
keywords:
- create 3d extrusion java
- Aspose 3D slices
- linear extrusion Java
linktitle: 3D Extrusion létrehozása szeletekkel – Aspose.3D for Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  headline: Create 3D Extrusion with Slices – Aspose.3D for Java
  type: TechArticle
- description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  name: Create 3D Extrusion with Slices – Aspose.3D for Java
  steps:
  - name: Set up the scene and define the profile
    text: '`RectangleShape` is a class that defines a 2‑D rectangle profile. First
      we create a `RectangleShape` and give it a **rounding radius** so the corners
      are smooth. `Scene` is the root container for all nodes and geometry. Then we
      initialise a new `Scene` that will hold all geometry.'
  - name: Create child node objects for each extrusion
    text: '`Node` represents an element in the scene graph that can hold geometry
      and transformations. Every piece of geometry lives under a `Node`. Here we generate
      two sibling nodes – one for a low‑slice extrusion and another for a high‑slice
      extrusion – and move the left node a little to the side so the res'
  - name: Perform linear extrusion and set slices
    text: '`LinearExtrusion` is the class that creates a solid by sweeping a profile
      linearly. `LinearExtrusion` is Aspose.3D''s class that generates a solid by
      extruding a 2‑D profile along a straight line. Using an **anonymous inner class**
      we call `setSlices` to control the smoothness. The left node gets onl'
  - name: Export OBJ – save the scene
    text: Finally we write the scene to a Wavefront OBJ file, a format widely supported
      by 3‑D editors and game engines. This demonstrates the **export OBJ Java** capability
      of Aspose.3D.
  type: HowTo
- questions:
  - answer: You can download the library [here](https://releases.aspose.com/3d/java/).
    question: How can I download Aspose.3D for Java?
  - answer: Refer to the documentation [here](https://reference.aspose.com/3d/java/).
    question: Where can I find the documentation for Aspose.3D?
  - answer: Yes, you can explore a free trial [here](https://releases.aspose.com/).
    question: Is there a free trial available?
  - answer: Visit the support forum [here](https://forum.aspose.com/c/3d/18).
    question: How can I get support for Aspose.3D?
  - answer: Yes, a temporary license can be obtained [here](https://purchase.aspose.com/temporary-license/).
    question: Can I purchase a temporary license?
  type: FAQPage
second_title: Aspose.3D Java API
title: 3D Extrusion létrehozása szeletekkel – Aspose.3D for Java
url: /hu/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D Extrudálás létrehozása szeletekkel – Aspose.3D for Java

## Bevezetés

Ha **create 3d extrusion** objektumokat szeretnél létrehozni, amelyek simák és pontosak, a szeletek számának szabályozása a kulcs. Ebben az útmutatóban végigvezetünk, hogyan adhatók meg a szeletek egy lineáris extrudálás során az Aspose.3D for Java használatával. Meg fogod érteni, miért fontos a szeletszám, hogyan állítható be a lekerekítési sugár, és hogyan exportálható az eredmény OBJ fájlként, amely bármely 3‑D csővezetékben felhasználható.

## Gyors válaszok
- **Mi szabályozza a „slices”?** A köztes keresztmetszetek száma, amelyet az extrudálás felületének közelítésére használnak.  
- **Melyik metódus állítja be a szeletszámot?** `LinearExtrusion.setSlices(int)`  
- **Módosíthatom a profil lekerekítési sugarát?** Igen, a `RectangleShape.setRoundingRadius(double)` segítségével  
- **Milyen fájlformátumot használ ez a példa?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **Szükségem van licencre a kód futtatásához?** Egy ingyenes próba a kiértékeléshez elegendő; a termeléshez kereskedelmi licenc szükséges.

`LinearExtrusion.setSlices(int)` beállítja, hogy hány köztes szeletet generál az extrudálás.  
`RectangleShape.setRoundingRadius(double)` definiálja a téglalap profil sarkainak sugarát.

## Hogyan hozhatunk létre 3d extrusion Java-val szeletekkel?

Töltsd be a 2‑D profilodat, válaszd ki a szeletszámot, állítsd be a lekerekítési sugarat, és hívd a `save`‑et – az egész munkafolyamat néhány sorba fér. Az Aspose.3D for Java automatikusan kezeli a geometria létrehozását, a szelet interpolációt és az OBJ exportot, így a vizuális minőségre koncentrálhatsz az alacsony szintű háló számítások helyett.

## Mi az a lineáris extrudálás szeletekkel?

A szeletekkel ellátott lineáris extrudálás egy lapos 2‑D alakzatot 3‑D szilárddá alakít azáltal, hogy egy egyenes vonal mentén húzza, miközben egy beállítható számú köztes keresztmetszetet generál. A szeletszám közvetlenül befolyásolja, milyen simán jelennek meg a görbült élek, például a lekerekített sarkok.

## Miért használjuk az Aspose.3D for Java-t 3d extrusion létrehozásához?

Az Aspose.3D **teljes programozási vezérlést** biztosít minden extrudálási paraméter felett, támogat **50+ bemeneti és kimeneti formátumot** (beleértve az OBJ, FBX, STL és GLTF formátumokat), és képes **több száz oldalas modelleket** feldolgozni anélkül, hogy a teljes fájlt a memóriába töltené. Bármely Java‑t támogató platformon fut, nem igényel natív DLL‑eket, és determinisztikus eredményeket garantál Windows, Linux és macOS rendszereken.

## Előfeltételek

1. **Java Development Kit** – JDK 8 vagy újabb telepítve.  
2. **Aspose.3D for Java** – Töltsd le a könyvtárat a hivatalos oldalról [itt](https://releases.aspose.com/3d/java/).  
3. Egy IDE vagy szövegszerkesztő a választásod szerint.

## Csomagok importálása

Add the Aspose.3D névteret a projektedhez, hogy hozzáférhess a 3‑D modellező osztályokhoz.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Lépésről‑lépésre útmutató

### 1. lépés: A jelenet beállítása és a profil meghatározása

`RectangleShape` egy osztály, amely egy 2‑D téglalap profilt definiál.  
Először létrehozzuk a `RectangleShape`‑t, és **lekerekítési sugarat** adunk neki, hogy a sarkok simák legyenek.  
`Scene` a gyökérkonténer minden csomópont és geometria számára.  
Ezután inicializálunk egy új `Scene`‑t, amely az összes geometriát tartalmazni fogja.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### 2. lépés: Gyermek‑csomópont objektumok létrehozása minden extrudáláshoz

`Node` egy elemet képvisel a jelenet gráfjában, amely geometriát és transzformációkat tarthat.  
Minden geometria egy `Node` alatt él. Itt két testvér csomópontot generálunk – egyet alacsony szeletű extrudáláshoz, egyet magas szeletű extrudáláshoz – és a bal csomópontot egy kicsit eltoljuk oldalra, hogy az eredmények könnyen összehasonlíthatók legyenek.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### 3. lépés: Lineáris extrudálás végrehajtása és szeletek beállítása

`LinearExtrusion` egy osztály, amely egy profilt lineárisan szívogatva hoz létre szilárdot.  
`LinearExtrusion` az Aspose.3D osztálya, amely egy 2‑D profilt egy egyenes vonal mentén extrudálva generál szilárdot. Egy **anonymous inner class**‑t használva hívjuk a `setSlices`‑t a simaság szabályozásához. A bal csomópont csak 2 szeletet kap (durva), míg a jobb csomópont 10 szeletet (sima).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### 4. lépés: OBJ exportálása – a jelenet mentése

Végül a jelenetet egy Wavefront OBJ fájlba írjuk, amely formátumot széles körben támogatják a 3‑D szerkesztők és játékmotorok. Ez demonstrálja az Aspose.3D **export OBJ Java** képességét.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Gyakori problémák és megoldások

| Probléma | Miért fordul elő | Megoldás |
|----------|------------------|----------|
| **Az extrudálás laposnak tűnik** | A szeletszám 1‑re vagy 0‑ra van állítva | Győződj meg arról, hogy a `setSlices` értéke ≥ 2. |
| **A lekerekített sarkok szaggatottnak látszanak** | A lekerekítési sugár túl kicsi a szeletszámhoz képest | Növeld a sugarat vagy a szeletszámot a simább ívekhez. |
| **Fájl nem található mentéskor** | `MyDir` egy nem létező mappára mutat | Hozd létre a könyvtárat előre, vagy használj abszolút elérési utat. |

## Gyakran ismételt kérdések

**Q: Hogyan tölthetem le az Aspose.3D for Java‑t?**  
A: Letöltheted a könyvtárat [itt](https://releases.aspose.com/3d/java/).

**Q: Hol találom meg az Aspose.3D dokumentációját?**  
A: Tekintsd meg a dokumentációt [itt](https://reference.aspose.com/3d/java/).

**Q: Van elérhető ingyenes próba?**  
A: Igen, egy ingyenes próbát felfedezhetsz [itt](https://releases.aspose.com/).

**Q: Hogyan kaphatok támogatást az Aspose.3D‑hez?**  
A: Látogasd meg a támogatási fórumot [itt](https://forum.aspose.com/c/3d/18).

**Q: Vásárolhatok ideiglenes licencet?**  
A: Igen, ideiglenes licencet szerezhetsz [itt](https://purchase.aspose.com/temporary-license/).

---

**Legutóbb frissítve:** 2026-05-24  
**Tesztelve a következővel:** Aspose.3D for Java 24.11 (legújabb a megírás időpontjában)  
**Szerző:** Aspose

## Kapcsolódó útmutatók

- [3D Extrudálás létrehozása Java-val az Aspose.3D segítségével](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Hogyan állítsuk be az irányt lineáris extrudálásnál az Aspose.3D for Java használatával](/3d/java/linear-extrusion/setting-direction/)
- [3D jelenet létrehozása csavarral lineáris extrudálásban – Aspose.3D for Java](/3d/java/linear-extrusion/applying-twist/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}