---
date: 2026-06-13
description: Tanuljon egy java 3d grafikai útmutatót a center vezérléséről lineáris
  extrúzióban az Aspose.3D segítségével, beleértve, hogyan állítsa be a rounding radius-t
  és mentse el az OBJ fájlt java-ban.
keywords:
- create 3d mesh java
- set rounding radius
- export 3d model obj
- save obj file java
- aspose 3d export obj
linktitle: Center vezérlése lineáris extrúzióban az Aspose.3D for Java segítségével
schemas:
- author: Aspose
  dateModified: '2026-06-13'
  description: Learn a java 3d graphics tutorial on controlling the center in linear
    extrusion with Aspose.3D, including how to set rounding radius and save OBJ file
    java.
  headline: Create 3D Mesh Java – Center in Linear Extrusion
  type: TechArticle
- description: Learn a java 3d graphics tutorial on controlling the center in linear
    extrusion with Aspose.3D, including how to set rounding radius and save OBJ file
    java.
  name: Create 3D Mesh Java – Center in Linear Extrusion
  steps:
  - name: Set Up the Base Profile
    text: First, create the 2‑D shape that will be extruded. Here we use a rectangle
      and **set rounding radius** to 0.3, which smooths the corners and demonstrates
      how to **round extrusion corners**.
  - name: Create a 3D Scene
    text: '**Scene** is the top‑level container that holds all 3‑D objects, lights,
      and cameras.'
  - name: Add Left and Right Nodes
    text: A **Node** represents a transformable object in the scene graph, allowing
      positioning and hierarchy.
  - name: Linear Extrusion – No Center (Left Node)
    text: '**LinearExtrusion** converts a 2‑D profile into a 3‑D mesh by sweeping
      it along a straight line. **setCenter(boolean)** toggles whether the extrusion
      is centered around the profile origin.'
  - name: Add a Ground Plane for Reference (Left Node)
    text: A thin box acts as a visual floor, helping you see the extrusion’s orientation.
  - name: Linear Extrusion – Centered (Right Node)
    text: Now repeat the extrusion, this time enabling `center`. The geometry will
      be symmetric around the profile’s origin, giving you a perfectly balanced **create
      3d mesh java** result.
  - name: Add a Ground Plane for Reference (Right Node)
    text: Same ground plane for the right side, making the comparison clear.
  - name: Save the 3D Scene
    text: Finally, export the entire scene to a Wavefront OBJ file – a format readily
      usable in most 3‑D editors. The `save` method automatically converts the mesh
      to the OBJ specification, allowing you to **save obj file java** without additional
      post‑processing.
  type: HowTo
- questions:
  - answer: It determines whether the extrusion is symmetric around the profile's
      origin.
    question: What does the center property do?
  - answer: A temporary license works for testing; a full license is required for
      production.
    question: Do I need a license to run the code?
  - answer: The scene is saved as a Wavefront OBJ file.
    question: Which file format is used for the result?
  - answer: Yes, use `setSlices(int)` on the `LinearExtrusion` object.
    question: Can I change the number of slices?
  - answer: Absolutely – it supports all modern Java versions.
    question: Is Aspose.3D compatible with Java 8+?
  type: FAQPage
second_title: Aspose.3D Java API
title: 3D Mesh Java létrehozása – Center in Linear Extrusion
url: /hu/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D háló létrehozása Java‑ban – Középpont lineáris extrudálásban

## Bevezetés

Ha 3‑D vizualizációkat épít Java‑ban, az extrudálási technikák elsajátítása elengedhetetlen. Ez a **java 3d graphics tutorial** megmutatja, hogyan **create 3d mesh java** objektumokat hozhat létre a lineáris extrudálás középpontjának vezérlésével az Aspose.3D for Java segítségével. A útmutató végére megérti, miért fontos a `center` tulajdonság, hogyan **set rounding radius**, és hogyan **save obj file java**‑kompatibilis kimenetet ment. Emellett megtudja, hogyan **export 3d model obj**‑t exportáljon bármely nagyobb 3‑D szerkesztőben való használatra.

## Gyors válaszok
- **Mi a center tulajdonság feladata?** Meghatározza, hogy az extrudálás szimmetrikus‑e a profil eredete körül.  
- **Szükségem van licencre a kód futtatásához?** Ideiglenes licenc teszteléshez működik; teljes licenc szükséges a termeléshez.  
- **Milyen fájlformátumot használ a végeredmény?** A jelenet Wavefront OBJ fájlként mentődik.  
- **Módosíthatom a szeletek számát?** Igen, használja a `setSlices(int)` metódust a `LinearExtrusion` objektumon.  
- **Kompatibilis az Aspose.3D a Java 8+ verziókkal?** Teljesen – támogatja az összes modern Java verziót.

## Mi az a java 3d graphics tutorial?

A **java 3d graphics tutorial** egy lépésről‑lépésre útmutató, amely megtanítja, hogyan használjon Java‑könyvtárakat háromdimenziós objektumok létrehozásához, manipulálásához és megjelenítéséhez. Ebben az oktatóanyagban megtanulja, hogyan **create 3d mesh java** objektumokat hozhat létre egy 2‑D profil átalakításával teljes 3‑D modellé, hogyan szabályozhatja a középső igazítást, hogyan kerekítheti az extrudálás sarkait, és végül hogyan exportálja az eredményt OBJ fájlként, amelyet bármely 3‑D program be tud olvasni.

## Miért használjuk az Aspose.3D for Java‑t?

Az Aspose.3D for Java egy magas szintű API‑t biztosít, amely megszünteti a manuális háló számítások szükségességét, így a tervezésre koncentrálhat ahelyett, hogy alacsony szintű geometriával foglalkozna. Támogat **50+ bemeneti és kimeneti formátumot** – köztük OBJ, FBX, STL és GLTF – így egyetlen metódushívással **export 3d model obj** vagy bármely más formátumot exportálhat. A könyvtár több száz oldalas jeleneteket dolgoz fel anélkül, hogy a teljes fájlt a memóriába töltené, **akár 3‑szoros gyorsabb teljesítményt** nyújtva a nyers OpenGL csővezetékekhez képest tipikus szerverhardveren.

## Előfeltételek

1. **Java fejlesztői környezet** – JDK 8 vagy újabb telepítve.  
2. **Aspose.3D for Java** – Töltse le a könyvtárat és a dokumentációt [itt](https://reference.aspose.com/3d/java/).  
3. **Document Directory** – Hozzon létre egy mappát a gépén a generált fájlok tárolásához; a továbbiakban **„Your Document Directory”**‑ként hivatkozunk rá.

## Csomagok importálása

A Java IDE‑jában importálja a szükséges Aspose.3D osztályokat. Ez a fordítónak hozzáférést biztosít az extrudálás és a jelenet‑építés funkcióihoz.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Lépésről‑lépésre útmutató

### 1. lépés: Az alapprofil beállítása

Először hozza létre a 2‑D alakzatot, amelyet extrudálni fog. Itt egy téglalapot használunk, és **set rounding radius**‑t 0.3‑ra állítunk, ami lekerekíti a sarkokat, és bemutatja, hogyan **round extrusion corners**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### 2. lépés: 3D jelenet létrehozása

**Scene** a legfelső szintű tároló, amely az összes 3‑D objektumot, fényt és kamerát tartalmazza.

```java
Scene scene = new Scene();
```

### 3. lépés: Bal és jobb csomópontok hozzáadása

A **Node** egy átalakítható objektumot képvisel a jelenet gráfjában, lehetővé téve a pozicionálást és a hierarchiát.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### 4. lépés: Lineáris extrudálás – Középpont nélkül (Bal csomópont)

**LinearExtrusion** egy 2‑D profilt alakít 3‑D hálóvá egy egyenes vonal mentén történő szkenneléssel.  
**setCenter(boolean)** beállítja, hogy az extrudálás a profil eredete körül legyen‑e középre igazítva.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

### 5. lépés: Referenciához talaj sík hozzáadása (Bal csomópont)

Egy vékony doboz vizuális padlóként működik, segítve az extrudálás tájolásának láthatóságát.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

### 6. lépés: Lineáris extrudálás – Középre igazítva (Jobb csomópont)

Most ismételje meg az extrudálást, ezúttal engedélyezve a `center`‑t. A geometria a profil eredete körül szimmetrikus lesz, így egy tökéletesen kiegyensúlyozott **create 3d mesh java** eredményt kap.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

### 7. lépés: Referenciához talaj sík hozzáadása (Jobb csomópont)

Ugyanaz a talaj sík a jobb oldalra, így az összehasonlítás egyértelmű.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

### 8. lépés: 3D jelenet mentése

Végül exportálja az egész jelenetet egy Wavefront OBJ fájlba – egy formátumba, amely a legtöbb 3‑D szerkesztőben könnyen használható. A `save` metódus automatikusan átalakítja a hálót az OBJ specifikáció szerint, lehetővé téve, hogy **save obj file java**‑t végezzen további utófeldolgozás nélkül.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Gyakori problémák és megoldások

| Probléma | Miért fordul elő | Megoldás |
|----------|------------------|----------|
| **Az extrudálás eltolódott** | `setCenter(false)` a profilt a sarkához rögzíti. | Használja a `setCenter(true)`‑t a szimmetrikus eredményhez. |
| **Az OBJ fájl üres** | A kimeneti könyvtár útvonala helytelen vagy hiányzik az írási jogosultság. | Ellenőrizze, hogy a `MyDir` egy létező mappára mutat, és az alkalmazásnak van írási joga. |
| **A lekerekített sarkok élesnek tűnnek** | A lekerekítési sugár túl kicsi a téglalap méretéhez képest. | Növelje a sugár értékét (pl. `setRoundingRadius(0.5)`). |

## Gyakran feltett kérdések

### Q1: Használhatom az Aspose.3D for Java‑t kereskedelmi projektekben?

A1: Igen, az Aspose.3D for Java kereskedelmi felhasználásra is elérhető. A licenc részletekért látogasson el [itt](https://purchase.aspose.com/buy).

### Q2: Elérhető ingyenes próba?

A2: Igen, egy ingyenes próba verziót kipróbálhat az Aspose.3D for Java‑ból [itt](https://releases.aspose.com/).

### Q3: Hol találok támogatást az Aspose.3D for Java‑hoz?

A3: Az Aspose.3D közösségi fórum egy nagyszerű hely a támogatás keresésére és tapasztalatok megosztására. Látogassa meg a fórumot [itt](https://forum.aspose.com/c/3d/18).

### Q4: Szükségem van ideiglenes licencre a teszteléshez?

A4: Igen, ha ideiglenes licencre van szüksége tesztelési célból, azt [itt](https://purchase.aspose.com/temporary-license/) szerezheti be.

### Q5: Hol találom a dokumentációt?

A5: Az Aspose.3D for Java dokumentációja [itt](https://reference.aspose.com/3d/java/) érhető el.

## Összegzés

A **java 3d graphics tutorial** befejezésével most már tudja, hogyan **create 3d mesh java** objektumokat hozhat létre, hogyan szabályozhatja egy lineáris extrudálás középpontját, hogyan állíthatja be a lekerekítési sugarat, és hogyan **save obj file java** kimenetet generál az Aspose.3D segítségével. Ezek a technikák finomhangolt irányítást biztosítanak a háló szimmetriája felett, ami elengedhetetlen a játékeszközök, CAD prototípusok és tudományos vizualizációk számára. Nyugodtan kísérletezzen különböző profilokkal, szeletszámokkal és export formátumokkal, hogy bővítse 3‑D eszköztárát.

---

**Utolsó frissítés:** 2026-06-13  
**Tesztelt verzió:** Aspose.3D for Java 24.11  
**Szerző:** Aspose

## Kapcsolódó oktatóanyagok

- [3D extrudálás létrehozása Java-val az Aspose.3D segítségével](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Hogyan állítsuk be az irányt lineáris extrudálásnál az Aspose.3D for Java segítségével](/3d/java/linear-extrusion/setting-direction/)
- [3D jelenet létrehozása csavarral lineáris extrudálásban – Aspose.3D for Java](/3d/java/linear-extrusion/applying-twist/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}