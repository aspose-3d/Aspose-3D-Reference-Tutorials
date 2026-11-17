---
date: 2026-11-17
description: Hogyan csökkentsük a 3D modell méretét egy sphere mesh generálásával
  Java-ban és a Google Draco-val az Aspose.3D segítségével. Ismerje meg a teljes munkafolyamatot
  percek alatt.
images:
- /java/3d-mesh-data/compress-meshes-google-draco/og-image.png
keywords:
- create sphere mesh
- how to compress 3d
- reduce 3d model size
- aspose 3d java
- compress 3d mesh
lastmod: 2026-11-17
linktitle: Hogyan csökkentsük a 3D modell méretét – sphere mesh létrehozása Java-ban
  a Google Draco használatával
og_description: Sphere mesh létrehozása és 3D modell tömörítése Java-val az Aspose.3D
  és a Google Draco használatával. Ez a bemutató megmutatja, hogyan generáljon egy
  sphere-t, exportálja .drc formátumba, és percek alatt érjen el akár 95%-os méretcsökkentést.
og_image_alt: 'Developer guide: Reduce 3d model size with Java sphere mesh and Draco
  compression'
og_title: Sphere mesh létrehozása és 3D modell tömörítése Java-val és Draco-val
schemas:
- author: Aspose
  dateModified: '2026-11-17'
  description: How to reduce 3d model size by generating a sphere mesh in Java and
    compressing it with Google Draco via Aspose.3D. Learn the full workflow in minutes.
  headline: How to reduce 3d model size with a Java sphere mesh and Draco
  type: TechArticle
- description: How to reduce 3d model size by generating a sphere mesh in Java and
    compressing it with Google Draco via Aspose.3D. Learn the full workflow in minutes.
  name: How to reduce 3d model size with a Java sphere mesh and Draco
  steps:
  - name: set up the project
    text: Create a new Java project (any IDE works) and add all Aspose.3D JARs to
      the classpath. Keep your source files in a package such as `com.example.draco`
      for clarity.
  - name: how to create sphere mesh in Java
    text: 'The `Sphere` class is Aspose.3D''s built‑in geometry generator that produces
      a triangulated mesh with a configurable radius and tessellation. > **Pro tip:**
      The `Sphere` class generates a triangulated mesh with a default radius of 1.0.
      You can pass custom radius, tessellation, or material parameters '
  - name: export the mesh to Draco format
    text: After the sphere is added to a `Scene` object, call `scene.save("sphere.drc",
      SaveFormat.Draco)`. Aspose.3D automatically selects optimal compression settings,
      but you can fine‑tune them by adjusting `DracoCompressionOptions` if you need
      the smallest possible file. `DracoCompressionOptions` lets you
  - name: verify the output
    text: Open the generated `.drc` file with a Draco viewer (e.g., three.js `DRACOLoader`)
      to ensure the geometry renders correctly. You’ll notice a dramatic reduction
      in file size—often a factor of ten or more.
  type: HowTo
- questions:
  - answer: Yes, Aspose.3D supports OBJ, FBX, STL, GLTF, and many others, making it
      a versatile choice for **Aspose 3d export** pipelines.
    question: Is Aspose.3D compatible with different 3d file formats?
  - answer: Absolutely. Draco offers native libraries for C++, Python, and JavaScript.
      This tutorial focuses on Java, but the concepts apply across languages.
    question: Can I use Google Draco for compression in other programming languages?
  - answer: Visit the **[Aspose.3D Java documentation](https://reference.aspose.com/3d/java/)**
      for full API references and more examples.
    question: Where can I find additional Aspose.3D documentation?
  - answer: Explore temporary licensing options on the **[Aspose temporary license
      page](https://purchase.aspose.com/temporary-license/)**.
    question: How do I obtain a temporary license for Aspose.3D?
  - answer: Yes, join the discussion at the **[Aspose.3D Forum](https://forum.aspose.com/c/3d/18)**.
    question: Is there a community forum for Aspose.3D support?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- reduce 3d model size
- Aspose.3D
- Java 3D compression
- Google Draco
- sphere mesh
title: Hogyan csökkentsük a 3D modell méretét Java sphere mesh és Draco használatával
url: /hu/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hogyan csökkentsük a 3d modell méretét Java gömb hálóval és Draco

## Bevezetés

Az Aspose.3D for Java egy könyvtár, amely lehetővé teszi 3‑D modellek létrehozását, manipulálását és konvertálását közvetlenül Java kódból. Ha gyors módot keres a **3d modell méretének csökkentésére**, miközben továbbra is magas minőségű geometriát biztosít, a megfelelő helyen jár. Ebben az útmutatóban végigvezetjük a gömb háló generálását **Aspose.3D for Java** segítségével, majd a háló tömörítését **Google Draco** használatával. A végére egy kész `.drc` fájlt kap, amely drámaian kisebb az eredetinél, így tökéletes web‑alapú megjelenítők, mobil játékok vagy bármely sávszélesség‑korlátozott Java alkalmazás számára.

## Gyors válaszok

- **Mi a bemutató témája?** Gömb háló létrehozása Java-ban és tömörítése Google Draco-val az Aspose.3D segítségével.  
- **Elsődleges könyvtár?** Aspose.3D for Java (használva a háló létrehozásához és a Draco exportáláshoz is).  
- **Tipikus megvalósítási idő?** Körülbelül 10‑15 perc egy egyszerű gömbhöz.  
- **Kulcsfontosságú előfeltétel?** Java fejlesztői környezet az Aspose.3D JAR‑okkal a classpath‑on.  
- **Eredmény?** Egy `.drc` fájl, amely **csökkenti a 3d modell méretét** akár 95 %-kal egy nem tömörített hálóhoz képest.

## Hogyan csökkentsük a 3d modell méretét?

Töltse be a gömböt, és tömörítse két egyszerű lépésben. Először **létrehozza a gömb hálót** a `new Sphere(1.0, 32, 32)` kóddal. Ezután a jelenetet közvetlenül Draco formátumba exportálja a `scene.save("sphere.drc", SaveFormat.Draco)` használatával. Az Aspose.3D automatikusan kezeli a geometria kvantálását és a csúcsok deduplikálását, így a fájlok általában 80‑95 %-kal kisebbek, miközben megőrzik a vizuális hűséget.

A `Sphere` osztály az Aspose.3D beépített geometria generátora, amely háromszögelt gömb hálót hoz létre. Elfogad egy sugár és tesszellációs paramétereket, lehetővé téve a részletesség szintjének szabályozását a tömörítés előtt.

## Mi a „reduce 3d model size” a 3d fejlesztés kontextusában?

A **3d modell méretének csökkentése** azt jelenti, hogy a továbbítandó vagy tárolandó geometriai adatmennyiséget csökkentjük, anélkül, hogy észrevehetően rontaná a vizuális minőséget. A Draco ezt úgy éri el, hogy a csúcspozíciókat, normálvektorokat és egyéb attribútumokat egy nagyon kompakt bináris formátumban kódolja. Az Aspose.3D-vel kombinálva a teljes munkafolyamat a Java környezetben marad, így nem kell natív binárisokkal bajlódni.

## Miért használjunk Google Draco háló tömörítést az Aspose.3D-vel?

A Google Draco és az Aspose.3D kombinációja hatékony csővezetéket biztosít, amely drámaian lecsökkenti a háló fájlok méretét, miközben könnyen integrálható Java projektekbe. A könyvtár kezeli az összes alacsony szintű kódolást, így a fejlesztők a geometria létrehozására koncentrálhatnak anélkül, hogy natív Draco binárisokkal kellene foglalkozniuk, ami gyorsabb fejlesztést és kisebb eszközöket eredményez web és mobil számára.

- **Masszív méretcsökkentés:** A Draco akár 95 %-kal is lecsökkentheti a háló adatokat tipikus modellek esetén, egy 5 MB-os OBJ-t 0,3 MB-os `.drc`‑vé alakítva.  
- **Gyors futásidejű dekódolás:** Az olyan motorok, mint a Unity, Unreal és a three.js natívan dekódolják a Draco‑t, ami gyorsabb betöltési időket eredményez.  
- **Zökkenőmentes Java integráció:** Az Aspose.3D elrejti a natív Draco könyvtárat, lehetővé téve, hogy a Java ökoszisztémában maradjon.  
- **Egyetlen helyen elérhető Aspose 3D export:** Ugyanaz az API, amelyet a geometria létrehozásához használ, kezeli az exportot is, egyszerűsítve a csővezetéket.  

Az Aspose.3D támogat **50+ bemeneti és kimeneti formátumot** — beleértve az OBJ, FBX, STL, GLTF és sok más formátumot — és képes több száz oldalas modelleket feldolgozni anélkül, hogy a teljes fájlt a memóriába töltené.

## Előfeltételek

- **Java Development Kit (JDK)** – 8-as vagy újabb verzió.  
- **Aspose.3D for Java** – töltse le a legújabb JAR‑okat az **[Aspose 3D Java kiadási oldalról](https://releases.aspose.com/3d/java/)**.  
- **Alapvető ismeretek a Google Draco-val** – az Aspose.3D csomagolót fogja használni, így nincs szükség natív Draco beállításra.

## Csomagok importálása

```java
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Sphere;


import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

## Lépésről‑lépésre útmutató

### 1. lépés: a projekt beállítása

Hozzon létre egy új Java projektet (bármely IDE működik), és adja hozzá az összes Aspose.3D JAR‑t a classpath‑hoz. Tartsa a forrásfájlokat egy, például `com.example.draco` csomagban a tisztaság érdekében.

### 2. lépés: hogyan hozzunk létre gömb hálót Java-ban

A `Sphere` osztály az Aspose.3D beépített geometria generátora, amely háromszögelt gömb hálót hoz létre.  

```java
import java.nio.file.Files;
import java.nio.file.Paths;
import com.aspose.threed.Sphere;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.FileFormat;

// ExStart:Encode3DMeshinGoogleDraco
// The path to the documents directory.
String MyDir = "Your Document Directory";

// Create a sphere
Sphere sphere = new Sphere();

// Encode the sphere to Google Draco raw data using optimal compression level.
DracoSaveOptions opt = new DracoSaveOptions();
opt.setCompressionLevel(DracoCompressionLevel.OPTIMAL);
byte[] b = FileFormat.DRACO.encode(sphere.toMesh(), opt);

// Save the raw bytes to file
Files.write(Paths.get(MyDir, "SphereMeshtoDRC_Out.drc"), b);
// ExEnd:Encode3DMeshinGoogleDraco
```

> **Pro tipp:** A `Sphere` osztály egy alapértelmezett 1.0 sugárral rendelkező háromszögelt hálót generál. Egyedi sugár, tesszelláció vagy anyag paramétereket adhat meg, ha a tömörítés előtt más részletességi szintre van szüksége.

### 3. lépés: a háló exportálása Draco formátumba

A `Scene` osztály egy teljes 3‑D jelenetet képvisel, amely tartalmazhat hálókat, fényeket és kamerákat. A `DracoCompressionOptions` osztály lehetővé teszi a Draco tömörítési beállítások testreszabását, például a kvantálást és a tömörítési szintet. Miután a gömb hozzá lett adva egy `Scene` objektumhoz, hívja a `scene.save("sphere.drc", SaveFormat.Draco)` metódust. Az Aspose.3D automatikusan kiválasztja az optimális tömörítési beállításokat, de finomhangolhatja őket a `DracoCompressionOptions` módosításával, ha a lehető legkisebb fájlt szeretné. A `DracoCompressionOptions` lehetővé teszi, hogy

### 4. lépés: a kimenet ellenőrzése

A `DRACOLoader` egy three.js segédprogram, amely Draco‑tömörített `.drc` fájlokat tölt be, és WebGL‑kompatibilis geometriává alakítja őket. Nyissa meg a generált `.drc` fájlt egy Draco nézővel (pl. three.js `DRACOLoader`) a geometria helyes megjelenítésének ellenőrzéséhez. Drámai fájlméret‑csökkenést fog észrevenni — gyakran tízszeres vagy nagyobb.

## Általános felhasználási esetek

| Forgatókönyv | Miért csökkentsük a modell méretét? | Hogyan segít ez az útmutató |
|--------------|--------------------------------------|-----------------------------|
| Web‑alapú termékkonfigurátorok | Gyorsabb oldalbetöltés lassú kapcsolatokon | Draco‑tömörített `.drc` fájlok másodpercek alatt betöltődnek |
| Mobil AR/VR alkalmazások | Alacsonyabb memóriahasználat az eszközökön | Kisebb hálók segítik az alkalmazás válaszkészségét |
| Felhőben renderelt jelenetek | Csökkentik a sávszélesség költségeit | Egy kattintásos export az Aspose.3D‑ról Draco‑ra |

## Gyakori problémák és megoldások

| Probléma | Ok | Megoldás |
|----------|----|----------|
| **`NoClassDefFoundError` for Draco classes** | Az Aspose.3D JAR‑ok nincsenek a classpath‑on | Ellenőrizze, hogy *az összes* Aspose.3D JAR fájl be legyen vonva, és a verzió megegyezik a dokumentációval. |
| **Output file is empty** | `MyDir` egy nem létező mappára mutat | Hozza létre a könyvtárat programozottan (`Files.createDirectories(Paths.get(MyDir))`) a fájl írása előtt. |
| **Compressed mesh looks distorted** | Alacsony tömörítési szint vagy elégtelen tesszelláció használata | Váltson `DracoCompressionLevel.OPTIMAL`‑ra, és növelje a gömb tesszellációját (pl. `new Sphere(1.0, 64, 64)`). A `DracoCompressionLevel.OPTIMAL` a legmagasabb tömörítési minőséget választja a Draco kimenethez. |

## Gyakran ismételt kérdések

**Q: Az Aspose.3D kompatibilis különböző 3d fájlformátumokkal?**  
A: Igen, az Aspose.3D támogatja az OBJ, FBX, STL, GLTF és sok más formátumot, így sokoldalú választás a **Aspose 3d export** csővezetékekhez.

**Q: Használhatom a Google Draco‑t tömörítésre más programozási nyelvekben?**  
A: Természetesen. A Draco natív könyvtárakat kínál C++, Python és JavaScript nyelvekhez. Ez az útmutató a Java-ra fókuszál, de a koncepciók más nyelvekre is alkalmazhatók.

**Q: Hol találok további Aspose.3D dokumentációt?**  
A: Látogassa meg a **[Aspose.3D Java dokumentációt](https://reference.aspose.com/3d/java/)** a teljes API referenciákért és további példákért.

**Q: Hogyan szerezhetek ideiglenes licencet az Aspose.3D-hez?**  
A: Tekintse meg az ideiglenes licencelési lehetőségeket a **[Aspose ideiglenes licenc oldalán](https://purchase.aspose.com/temporary-license/)**.

**Q: Van közösségi fórum az Aspose.3D támogatásához?**  
A: Igen, csatlakozzon a beszélgetéshez a **[Aspose.3D Fórumon](https://forum.aspose.com/c/3d/18)**.

## Összegzés

Ebben az útmutatóban bemutattuk, hogyan **csökkenthetjük a 3d modell méretét** egy Java-ban létrehozott gömb hálóval, majd a Google Draco-val az Aspose.3D segítségével tömörítve. A rövid lépések követésével drámaian lecsökkentheti a háló fájlokat, javíthatja a betöltési időket, és Java‑alapú 3d alkalmazásait válaszkész és sávszélesség‑barát állapotban tarthatja.

---

**Utolsó frissítés:** 2026-11-17  
**Tesztelt verzió:** Aspose.3D for Java 24.12 (latest)  
**Szerző:** Aspose

## Kapcsolódó útmutatók

- [3D fájlméret csökkentése – Jelenetek tömörítése Aspose.3D for Java használatával](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [Draco pontfelhő generálása gömbökkel az Aspose.3D for Java segítségével](/3d/java/point-clouds/generate-point-clouds-spheres-java/)
- [Ismerje meg, hogyan trianguláljon hálókat optimalizált rendereléshez Java‑ban az Aspose.3D használatával](/3d/java/geometry/triangulate-meshes-for-optimized-rendering/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}