---
date: 2025-12-13
description: Tanulja meg, hogyan használja az Aspose 3D Java-t 3D csomópontok átalakításához.
  Ez az útmutató bemutatja, hogyan használja az Euler‑szögeket, adjon hozzá 3D forgatást,
  és állítson be transzlációt Java‑ban.
linktitle: Aspose 3D Java – Transform 3D Nodes with Euler Angles
second_title: Aspose.3D Java API
title: Aspose 3D Java – 3D csomópontok átalakítása Euler-szögekkel
url: /hu/java/geometry/transform-3d-nodes-with-euler-angles/
weight: 19
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D csomópontok transzformálása Euler‑szögekkel Java‑ban az Aspose.3D használatával

## Introduction

Ebben az útmutatóban megtudod, **hogyan kell használni az aspose 3d java**‑t 3D csomópontok transzformálásához Euler‑szögek alkalmazásával. A útmutató végére képes leszel 3D forgatást hozzáadni, **set translation java**‑t beállítani, és dinamikus jeleneteket létrehozni, amelyek valós‑idő adatokra reagálnak.

## Quick Answers
- **Melyik könyvtár kezeli a 3D transzformációkat Java‑ban?** Aspose 3D for Java.  
- **Melyik metódus állítja be a forgatást Euler‑szögekkel?** `setEulerAngles()` a csomópont transzformációján.  
- **Hogyan mozgathatok egy csomópontot a térben?** Használd a `setTranslation()`‑t egy `Vector3`‑al.  
- **Szükségem van licencre a termeléshez?** Igen, egy kereskedelmi Aspose 3D licenc szükséges.  
- **Exportálhatok FBX‑be?** Természetesen – a `scene.save(..., FileFormat.FBX7500ASCII)` azonnal működik.

## Prerequisites

Mielőtt belemerülnénk az útmutatóba, győződj meg róla, hogy a következő előfeltételek adottak:

- Alapvető Java programozási ismeretek.  
- Java Development Kit (JDK) telepítve a gépeden.  
- Aspose.3D könyvtár, amelyet a [Aspose.3D Java Documentation](https://reference.aspose.com/3d/java/) oldalról szerezhetsz be.

## Import Packages

Kezdjük a szükséges csomagok importálásával a Java projektedbe. Győződj meg róla, hogy az Aspose.3D könyvtár helyesen hozzá van adva a classpath‑hoz. Ha még nem töltötted le, a letöltési linket megtalálod [itt](https://releases.aspose.com/3d/java/).

```java
import com.aspose.threed.*;
```

## aspose 3d java – Working with Euler Angles

### Step 1. Initialize Scene and Node

Először hozz létre egy jelenetet és egy csomópontot, amely a transzformálni kívánt geometriát fogja tartalmazni.

```java
// ExStart:AddTransformationToNodeByEulerAngles
// Initialize scene object
Scene scene = new Scene();

// Initialize Node class object
Node cubeNode = new Node("cube");
```

### Step 2. Create Mesh and Set Geometry

Ezután generálj egy egyszerű hálót (ebben az esetben egy kockát), és csatold a csomóponthoz.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Point node to the Mesh geometry
cubeNode.setEntity(mesh);
```

## Add Rotation 3D to a Node

### Step 3. Set Euler Angles and Translation

Most alkalmazzuk a forgatást Euler‑szögekkel, és a csomópontot egy látható pozícióba helyezzük.

```java
// Euler angles
cubeNode.getTransform().setEulerAngles(new Vector3(0.3, 0.1, -0.5));

// Set translation
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## Set Translation Java – Positioning the Node

A fenti fordítási lépés bemutatja a **set translation java** gyakorlatban: a csomópont 20 egységgel eltolódik a Z‑tengely mentén, hogy a renderelés után látható legyen.

## Step 4. Add Node to Scene

Csatold a transzformált csomópontot a jelenet gyökércsomópontjához.

```java
// Add cube to the scene
scene.getRootNode().getChildNodes().add(cubeNode);
```

## Step 5. Save 3D Scene

Végül exportáld a jelenetet egy FBX fájlba (vagy bármely más támogatott formátumba).

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByEulerAngles
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

Győződj meg róla, hogy a `"Your Document Directory"`‑t a géped megfelelő elérési útjára cseréled.

## Conclusion

Gratulálunk! Sikeresen transzformáltad a 3D csomópontokat Euler‑szögekkel Java‑ban a **aspose 3d java** segítségével. Kísérletezz különböző szögekkel és fordításokkal, hogy dinamikus és lebilincselő 3D jeleneteket hozz létre.

## FAQ's

### Q1: Használhatom az Aspose.3D for Java‑t kereskedelmi projektekben?

A1: Igen, használhatod. Látogasd meg a [purchase page](https://purchase.aspose.com/buy) oldalt a licencelési részletekért.

### Q2: Hol találok támogatást az Aspose.3D‑hez?

A2: A [Aspose.3D forum](https://forum.aspose.com/c/3d/18) a megfelelő hely a segítségkéréshez és a közösséggel való kapcsolattartáshoz.

### Q3: Van ingyenes próbaverzió?

A3: Igen, a [free trial](https://releases.aspose.com/) segítségével kipróbálhatod az Aspose.3D képességeit.

### Q4: Hogyan szerezhetek ideiglenes licencet?

A4: Ideiglenes licencet [itt](https://purchase.aspose.com/temporary-license/) szerezhetsz.

### Q5: Hol találom a dokumentációt?

A5: A [documentation](https://reference.aspose.com/3d/java/) átfogó útmutatót nyújt az Aspose.3D for Java használatához.

## Frequently Asked Questions

**Q: Mi a különbség az Euler‑szögek és a kvaternion forgatás között?**  
A: Az Euler‑szögek intuitívak (dőlésszög, irány, görbület), de gimbal lock‑ot okozhatnak, míg a kvaterniók elkerülik ezt a problémát és jobb sima interpolációkat biztosítanak.

**Q: Láncolhatok több transzformációt ugyanazon a csomóponton?**  
A: Igen. Hívd meg a `setEulerAngles`, `setTranslation` és `setScale` metódusokat tetszőleges sorrendben; a könyvtár egyetlen transzformációs mátrixba egyesíti őket.

**Q: Lehet más formátumokba, például OBJ vagy STL, exportálni?**  
A: Természetesen. Cseréld le a `FileFormat.FBX7500ASCII`‑t `FileFormat.OBJ`‑ra vagy `FileFormat.STL`‑re a `scene.save` hívásban.

**Q: Hogyan alkalmazhatom ugyanazt a forgatást több csomópontra egyszerre?**  
A: Hozz létre egy szülőcsomópontot, alkalmazd a forgatást a szülőre, majd helyezd el alatta a gyermekcsomópontokat. Minden gyermek örökli a transzformációt.

**Q: Szükséges-e valamilyen takarítási metódust hívni a mentés után?**  
A: A Java szemétgyűjtője a legtöbb erőforrást kezel, de nagy jelenetek esetén hosszú‑távú alkalmazásban explicit módon meghívhatod a `scene.dispose()`‑t.

---

**Last Updated:** 2025-12-13  
**Tested With:** Aspose.3D 23.12 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}