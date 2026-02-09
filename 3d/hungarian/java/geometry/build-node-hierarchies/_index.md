---
date: 2026-02-09
description: Tanulja meg, hogyan exportáljon FBX-et, és adjon hozzá mesh‑t egy csomóponthoz,
  miközben gyermekcsomókat hoz létre Java‑ban az Aspose.3D használatával.
linktitle: Build Node Hierarchies in 3D Scenes with Java and Aspose.3D
second_title: Aspose.3D Java API
title: Hogyan exportáljunk FBX-et és építsünk csomópont‑hierarchiákat Java‑ban
url: /hu/java/geometry/build-node-hierarchies/
weight: 16
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# FBX exportálása és csomópont‑hierarchiák építése Java‑ban az Aspose.3D segítségével

## Bevezetés

Ha egy világos, lépésről‑lépésre útmutatót keres a **FBX exportálására** Java‑alkalmazásból, jó helyen jár. Ebben a tutorialban megmutatjuk, hogyan építsen csomópont‑hierarchiákat, **mesh hozzáadását csomóponthoz**, és végül hogyan mentse a jelenetet FBX fájlként az Aspose.3D Java API‑val. Akár egy egyszerű prototípust, akár egy termelés‑kész 3D motor fejleszt, ezek a technikák teljes irányítást adnak a scene graph felett.

## Gyors válaszok
- **Mi a tutorial fő célja?** Az FBX exportálásának bemutatása csomópont‑hierarchiák felépítése után.  
- **Melyik könyvtárat használjuk?** Aspose.3D for Java.  
- **Szükségem van licencre?** A fejlesztéshez ingyenes próbaverzió is elegendő; a termeléshez kereskedelmi licenc szükséges.  
- **Milyen fájlformátum jön létre?** FBX (ASCII 7500).  
- **Testreszabhatom a csomópont‑transzformációkat?** Igen – a transláció, rotáció és skálázás mind támogatott.

## Mi az „FBX exportálása” az Aspose.3D kontextusában?

Az FBX exportálása azt jelenti, hogy a memóriában lévő scene graph‑ot, amelyet az Aspose.3D‑val épített, FBX fájllá alakítjuk, amely megnyitható népszerű 3D eszközökben, például Blender, Maya vagy Unity. Az API elvégzi a nehéz munkát, így Ön a jelenet létrehozására koncentrálhat.

## Miért építsünk csomópont‑hierarchiákat exportálás előtt?

A jól felépített csomópont‑hierarchia lehetővé teszi, hogy egy szülőcsomóponton egyszer alkalmazzon transzformációkat, amelyek automatikusan minden gyermekre is kihatnak. Ez csökkenti a kódupítást és tükrözi a valós objektum‑kapcsolatokat (például egy autó alváz és a hozzá tartozó kerekek gyermek‑csomópontként).

## Előfeltételek

Mielőtt belevágna, győződjön meg róla, hogy rendelkezik:

1. **Java fejlesztői környezet** – JDK 8+ és egy IDE vagy build eszköz, amit választ.  
2. **Aspose.3D for Java könyvtár** – Töltse le és telepítse a könyvtárat a [download page](https://releases.aspose.com/3d/java/).  
3. **Dokumentum könyvtár** – Mappa a gépén, ahová a generált FBX fájl mentésre kerül.

## Csomagok importálása

Kezdje el az Aspose.3D szükséges osztályainak importálásával:

```java
import com.aspose.threed.*;

```

## 1. lépés: A Scene objektum inicializálása

```java
// Initialize scene object
Scene scene = new Scene();
```

## 2. lépés: Gyermek csomópontok létrehozása és mesh hozzáadása csomóponthoz

Ebben a lépésben bemutatjuk, **hogyan hozzunk létre gyermek csomópontokat** és **mesh‑et adjunk csomóponthoz**.

```java
// Get a child node object
Node top = scene.getRootNode().createChildNode();

// Create the first cube node
Node cube1 = top.createChildNode("cube1");
Mesh mesh = Common.createMeshUsingPolygonBuilder(); // Use your mesh creation method
cube1.setEntity(mesh);
cube1.getTransform().setTranslation(new Vector3(-10, 0, 0));

// Create the second cube node
Node cube2 = top.createChildNode("cube2");
cube2.setEntity(mesh);
cube2.getTransform().setTranslation(new Vector3(10, 0, 0));
```

## 3. lépés: Rotáció alkalmazása a felső csomópontra

A szülőcsomópont forgatása automatikusan forgatja az összes gyermekét, ami a hierarchikus jelenetek alapvető előnye.

```java
// Rotate the top node, affecting all child nodes
top.getTransform().setRotation(Quaternion.fromEulerAngle(Math.PI, 4, 0));
```

## 4. lépés: 3D jelenet mentése – FBX exportálása

Most **mentjük a jelenetet FBX‑ként**, befejezve a „FBX exportálása” munkafolyamatot.

```java
// Save 3D scene in the supported file format (FBX in this case)
String MyDir = "Your Document Directory";
MyDir = MyDir + "NodeHierarchy.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nNode hierarchy added successfully to document.\nFile saved at " + MyDir);
```

### Várható eredmény
A kód futtatása egy **NodeHierarchy.fbx** nevű fájlt hoz létre a megadott könyvtárban. Nyissa meg bármely FBX‑kompatibilis megjelenítőben, hogy lássa a két kockát, amelyek a központi pivot bal és jobb oldalán helyezkednek el, és együtt forognak.

## Gyakori problémák és megoldások

| Probléma | Miért fordul elő | Megoldás |
|----------|------------------|----------|
| **File not found** hiba mentéskor | `MyDir` útvonal helytelen vagy hiányzik a záró elválasztó | Győződjön meg róla, hogy a könyvtár létezik, és a fájl elválasztóval (`/` vagy `\\`) végződik. |
| **Mesh not visible** export után | A mesh entitás nincs hozzárendelve, vagy a transláció a látótérből kívülre helyezi | Ellenőrizze a `cube1.setEntity(mesh)` hívást és a transláció értékeket. |
| **Rotation looks wrong** | A radiánok és fokok helytelen használata | `Quaternion.fromEulerAngle` radiánokat vár; ennek megfelelően módosítsa az értékeket. |

## Gyakran ismételt kérdések

**K: Az Aspose.3D for Java alkalmas kezdőknek?**  
**V:** Abszolút! Az API tiszta, objektum‑orientált megközelítéssel lett tervezve, ami könnyen tanulható, még ha új is a 3D programozásban.

**K: Használhatom az Aspose.3D for Java‑t kereskedelmi projektekhez?**  
**V:** Igen, használhatja. Látogassa meg a [purchase page](https://purchase.aspose.com/buy) a licenc részletekért.

**K: Hogyan kaphatok támogatást az Aspose.3D for Java‑hoz?**  
**V:** Csatlakozzon az [Aspose.3D forumhoz](https://forum.aspose.com/c/3d/18), hogy segítséget kapjon a közösségtől és az Aspose támogatási csapatától.

**K: Van ingyenes próbaverzió?**  
**V:** Természetesen! Fedezze fel a funkciókat az [free trial](https://releases.aspose.com/) segítségével, mielőtt elköteleződne.

**K: Hol találom a dokumentációt?**  
**V:** Lásd a [documentation](https://reference.aspose.com/3d/java/) a részletes információkért az Aspose.3D for Java‑ról.

## Következtetés

Az **FBX exportálásának** elsajátítása, a csomópont‑hierarchiák építése és a **mesh hozzáadása csomóponthoz** alapvető lépések a kifinomult 3D alkalmazások Java‑ban történő fejlesztéséhez. Az Aspose.3D egy erőteljes, licencbarát megoldást kínál, amely elrejti az alacsony szintű részleteket, miközben teljes irányítást biztosít a scene graph felett. Kísérletezzen különböző mesh‑ekkel, transzformációkkal és export formátumokkal, hogy még több lehetőséget nyisson meg.

---

**Last Updated:** 2026-02-09  
**Tested With:** Aspose.3D for Java 24.11  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}