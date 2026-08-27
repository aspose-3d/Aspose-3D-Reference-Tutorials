---
date: 2026-06-03
description: Ismerje meg, hogyan exportálhatja a jelenetet FBX formátumba, és hozhat
  létre 3D cylinder, box és egyéb primitive models az Aspose.3D for Java használatával.
keywords:
- export scene as fbx
- convert 3d model fbx
- Aspose 3D primitives
- Java 3D modeling
linktitle: Primitív 3D Models építése az Aspose.3D for Java segítségével
schemas:
- author: Aspose
  dateModified: '2026-06-03'
  description: Learn how to export scene as FBX and create 3D cylinder, box, and other
    primitive models using Aspose.3D for Java.
  headline: Export scene as FBX and build cylinder with Aspose.3D Java
  type: TechArticle
- description: Learn how to export scene as FBX and create 3D cylinder, box, and other
    primitive models using Aspose.3D for Java.
  name: Export scene as FBX and build cylinder with Aspose.3D Java
  steps:
  - name: Initialize a Scene Object
    text: The `Scene` class is Aspose.3D's top‑level container that holds all nodes,
      lights, cameras, and materials in memory.
  - name: Build a 3D box model
    text: The `Box` class represents a rectangular prism and is useful for testing
      the coordinate system. Adding it as a child of the scene’s root node positions
      it at the origin.
  - name: Create a 3D cylinder model
    text: The `Cylinder` class is Aspose.3D's built‑in cylinder primitive. It comes
      with default dimensions (radius = 1, height = 2) but you can customise them
      via its constructor.
  - name: Save the drawing in the FBX format
    text: After assembling the scene, export it so other tools (e.g., Unity, Blender)
      can read it. We use the `FBX7500ASCII` format, which is widely supported and
      human‑readable.
  type: HowTo
- questions:
  - answer: Aspose.3D primarily supports Java, but there are versions available for
      .NET and C++ as well.
    question: Can I use Aspose.3D for Java with other programming languages?
  - answer: Absolutely. It provides a comprehensive set of features—including mesh
      manipulation, material assignment, and animation—making it suitable for both
      simple primitives and intricate models.
    question: Is Aspose.3D suitable for complex 3D modeling tasks?
  - answer: Visit the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) for community
      support and discussions.
    question: Where can I find additional help and support?
  - answer: Yes, you can explore a [free trial](https://releases.aspose.com/) before
      making a purchase decision.
    question: Can I try Aspose.3D before purchasing?
  - answer: You can obtain a [temporary license](https://purchase.aspose.com/temporary-license/)
      for Aspose.3D through the website.
    question: How do I obtain a temporary license for Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
title: Exportálja a jelenetet FBX formátumba, és építsen hengert az Aspose.3D Java
  segítségével
url: /hu/java/primitive-3d-models/building-primitive-3d-models/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Exportálja a jelenetet FBX formátumba, és építsen hengert az Aspose.3D Java-val

## Bevezetés

Ha valaha is szüksége volt **3D henger** (vagy bármely más alapvető alakzat) közvetlenül Java kódból létrehozni, az Aspose.3D könnyűvé teszi a feladatot. Ebben az útmutatóban végigvezetjük a teljes munkafolyamatot – a környezet beállításától a **jelenet exportálása FBX**-ként – hogy azonnal programozottan generálhasson 3D geometriát. Meg fogja látni, hogyan kezeli a könyvtár az primitíveket, hogyan szervezi őket egy jelenet gráfba, és hogyan menti az eredményt olyan formátumban, amelyet a Unity, a Blender vagy bármely más 3D eszköz olvas.

## Gyors válaszok
- **Melyik könyvtár teszi lehetővé 3D henger létrehozását Java-ban?** Aspose.3D for Java.  
- **Milyen formátumba exportálhatom a jelenetet?** FBX (ASCII 7500) a `FileFormat.FBX7500ASCII` használatával.  
- **Szükségem van licencre a fejlesztéshez?** Egy ingyenes próba a teszteléshez működik; egy állandó licenc szükséges a termeléshez.  
- **Melyek a támogatott fő primitívek?** Box, Cylinder, Sphere, Cone, és több mint 10 további alakzat.  
- **Kompatibilis a kód a Java 8 és újabb verziókkal?** Igen, az Aspose.3D a JDK 8+ célpontja.

## Mi az a 3D henger primitív?

A henger primitív egy alapvető geometriai alakzat, amelyet sugár és magasság határoz meg. Sok 3D folyamatban építőelemként szolgál összetettebb modellekhez, mint például csövek, kerekek vagy építészeti oszlopok. Az Aspose.3D egy kész `Cylinder` osztályt biztosít, így nem kell manuálisan számolni a csúcsokat.

## Miért használjuk az Aspose.3D for Java-t?

Az Aspose.3D for Java egy átfogó, tisztán Java‑alapú 3D motorral rendelkezik, amely megszünteti a natív könyvtárak szükségességét, így ideális a platformközi fejlesztéshez. Széles körű import‑ és exportformátumokat támogat, robusztus jelenet gráfot biztosít a hierarchikus szervezéshez, és beépített primitíveket tartalmaz, amelyekkel minimális kóddal hozhat létre geometriát. Ezek a funkciók együtt felgyorsítják a fejlesztést és csökkentik a karbantartási terhet.

- **Teljes funkcionalitású 3D motor** – **több mint 30** népszerű formátum importálását/exportálását támogat (FBX, OBJ, STL, GLTF, 3DS, stb.).  
- **Pure Java API** – nincs natív függőség, tökéletes a platformközi projektekhez.  
- **Robusztus jelenet gráf** – lehetővé teszi az objektumok hierarchikus szervezését, így a nagy jelenetek könnyen kezelhetők.  
- **Egyszerű licencelés** – kezdje egy ingyenes próbalicenceléssel, majd frissítsen állandó licencre, amikor élőben használja.

## Előfeltételek

Mielőtt a kódba merülnél, győződj meg róla, hogy a következők telepítve vannak:

1. **Java Development Kit (JDK)** – JDK 8 vagy újabb telepítve a gépén.  
2. **Aspose.3D for Java library** – töltse le és telepítse a [download page](https://releases.aspose.com/3d/java/) oldalról.  

## Csomagok importálása

Kezdje a core Aspose.3D névtér importálásával. Ez hozzáférést biztosít a `Scene`, `Box`, `Cylinder` és a fájlformátum konstansokhoz.

```java
import com.aspose.threed.*;
```

Miután a könyvtár hivatkozásra került, hozzunk létre egy jelenetet, és adjunk hozzá némi primitív geometriát.

## Hogyan exportáljuk a jelenetet FBX formátumba és hozzunk létre 3D primitíveket?

Töltsön be egy új `Scene` objektumot, adjon hozzá primitív csomópontokat (Box, Cylinder, stb.), majd hívja meg a `save` metódust az FBX7500ASCII formátummal. Néhány sorban egy teljes funkcionalitású FBX fájlt kap, amely bármely nagyobb 3D szerkesztőben megnyitható, lehetővé téve a zökkenőmentes integrációt játék motorokkal, renderelési folyamatokkal vagy AR/VR alkalmazásokkal.

### 1. lépés: Jelenet objektum inicializálása

`Scene` osztály az Aspose.3D felső szintű tárolója, amely memóriában tartja az összes csomópontot, fényt, kamerát és anyagot.

```java
// The path to the documents directory.
String myDir = "Your Document Directory";

// Initialize a Scene object
Scene scene = new Scene();
```

### 2. lépés: 3D doboz modell felépítése

`Box` osztály egy téglalapprizmát képvisel, és hasznos a koordináta rendszer teszteléséhez. Gyökércsomópont gyermekeként hozzáadva a jelenethez, az eredetben helyezkedik el.

```java
// Create a Box model
scene.getRootNode().createChildNode("box", new Box());
```

### 3. lépés: 3D henger modell létrehozása

`Cylinder` osztály az Aspose.3D beépített henger primitívje. Alapértelmezett méretekkel (sugár = 1, magasság = 2) érkezik, de testreszabható a konstruktorán keresztül.

```java
// Create a Cylinder model
scene.getRootNode().createChildNode("cylinder", new Cylinder());
```

### 4. lépés: Rajz mentése FBX formátumban

A jelenet összeállítása után exportálja, hogy más eszközök (pl. Unity, Blender) is olvashassák. A `FBX7500ASCII` formátumot használjuk, amely széles körben támogatott és ember által olvasható.

```java
// Save drawing in the FBX format
myDir = myDir + "test.fbx";
scene.save(myDir, FileFormat.FBX7500ASCII);
```

## Gyakori problémák és megoldások

| Probléma | Miért fordul elő | Megoldás |
|----------|------------------|----------|
| **File not found** mentéskor | `myDir` egy nem létező mappára mutat | Győződjön meg róla, hogy a könyvtár létezik, vagy hozza létre a `new File(myDir).mkdirs();` segítségével |
| **Empty scene** export után | A `save` hívása előtt nem lettek csomópontok hozzáadva | Ellenőrizze, hogy a `createChildNode` hívások végrehajtásra kerülnek (debuggolás a `scene.getRootNode().getChildCount()` segítségével) |
| **License exception** | Érvényes licenc nélkül futtatás a termelésben | Alkalmazzon ideiglenes vagy állandó licencet a `License license = new License(); license.setLicense("Aspose.3D.Java.lic");` használatával |

## Gyakran feltett kérdések

**Q: Használhatom az Aspose.3D for Java-t más programozási nyelvekkel?**  
A: Az Aspose.3D elsősorban Java-t támogat, de elérhetők verziók .NET és C++ számára is.

**Q: Alkalmas az Aspose.3D összetett 3D modellezési feladatokra?**  
A: Teljes mértékben. Átfogó funkciókészletet biztosít – beleértve a háló manipulációt, anyag hozzárendelést és animációt – így alkalmas egyszerű primitívek és bonyolult modellek egyaránt.

**Q: Hol találok további segítséget és támogatást?**  
A: Látogassa meg az [Aspose.3D Fórumot](https://forum.aspose.com/c/3d/18) a közösségi támogatás és megbeszélésekért.

**Q: Kipróbálhatom az Aspose.3D-t vásárlás előtt?**  
A: Igen, felfedezhet egy [ingyenes próbát](https://releases.aspose.com/) a vásárlási döntés előtt.

**Q: Hogyan szerezhetek ideiglenes licencet az Aspose.3D-hez?**  
A: A weboldalon keresztül szerezhet [ideiglenes licencet](https://purchase.aspose.com/temporary-license/) az Aspose.3D-hez.

## Összegzés

Most már megtanulta, hogyan **exportálja a jelenetet FBX**-ként, és hogyan **hozzon létre 3D hengert**, dobozt és egyéb primitív modelleket az Aspose.3D for Java segítségével. Nyugodtan kísérletezzen további primitívekkel, például Sphere, Cone vagy Torus, és fedezze fel az anyag hozzárendeléseket, hogy modelljei valósághű megjelenést kapjanak. Amint magabiztos, integrálhatja a generált FBX fájlokat játék motorokba, AR/VR folyamatokba vagy bármely további 3D munkafolyamatba.

---

**Utoljára frissítve:** 2026-06-03  
**Tesztelve a következővel:** Aspose.3D for Java 24.11 (legújabb a írás időpontjában)  
**Szerző:** Aspose

## Kapcsolódó oktatóanyagok

- [Hogyan exportáljunk jelenetet FBX-be és nyerjünk ki 3D jelenet információt Java-ban](/3d/java/3d-scenes-and-models/get-scene-information/)
- [Hogyan exportáljunk FBX-et és építsünk csomópont hierarchiákat Java-ban](/3d/java/geometry/build-node-hierarchies/)
- [Hogyan hozzunk létre henger modelleket az Aspose.3D for Java-val](/3d/java/cylinders/)

{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< blocks/products/products-backtop-button >}}
{{< /blocks/products/pf/main-wrap-class >}}