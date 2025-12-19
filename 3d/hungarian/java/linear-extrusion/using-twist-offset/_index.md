---
date: 2025-12-19
description: Ismerje meg, hogyan hozhat létre 3D-s jelenetet, és exportálhat 3D‑obj
  fájlt Twist Offset használatával lineáris extrúzióban az Aspose.3D for Java segítségével.
linktitle: Create 3d scene with Twist Offset – Aspose.3D Java
second_title: Aspose.3D Java API
title: 3D-s jelenet létrehozása Twist Offset-tel – Aspose.3D Java
url: /hu/java/linear-extrusion/using-twist-offset/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D jelenet létrehozása Twist Offset használatával – Aspose.3D for Java

## Introduction

A 3D grafika dinamikus világában a **create 3d scene** lineáris extrúzióval megtanulni igazi áttörés. Az Aspose.3D for Java segítségével fejlesztheti 3D modellezési képességeit, ha beépíti a Twist Offset funkciót a lineáris extrúziós folyamatba. Ez az útmutató végigvezeti a lépéseken, hogyan használja a Twist Offset-et a Linear Extrusion-ben az Aspose.3D for Java-val, és eszközöket biztosít a lenyűgöző 3D jelenetek létrehozásához.

## Quick Answers
- **Mi a Twist Offset funkció?** A csavart a extrúziós útvonal mentén eltolja, így nagyobb irányítást biztosít a geometria felett.  
- **Melyik fájlformátumot használja az export?** A példa a modellt Wavefront OBJ (`.obj`) formátumban menti.  
- **Szükség van licencre a fejlesztéshez?** A ingyenes próba verzió tesztelésre elegendő; a termeléshez kereskedelmi licenc szükséges.  
- **Milyen Java verzió szükséges?** Java 8 vagy újabb.  
- **Módosíthatom a szeletek számát?** Igen – a `setSlices` metódus határozza meg a csavar simaságát.

## Prerequisites

Mielőtt belemerülne az útmutatóba, győződjön meg róla, hogy a következő előfeltételek rendelkezésre állnak:

- Java környezet: Győződjön meg arról, hogy a rendszerén be van állítva egy Java fejlesztői környezet.  
- Aspose.3D for Java: Töltse le és telepítse az Aspose.3D könyvtárat a [download link](https://releases.aspose.com/3d/java/) címről.  
- Dokumentáció: Ismerkedjen meg az [Aspose.3D for Java dokumentációval](https://reference.aspose.com/3d/java/).  

## Import Packages

A Java projektjében importálja a szükséges csomagokat az Aspose.3D for Java használatának megkezdéséhez. Győződjön meg róla, hogy a zökkenőmentes integrációhoz szükséges könyvtárakat is belefoglalja.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Step 1: Set Up the Environment

Kezdje a Java fejlesztői környezet beállításával, és ellenőrizze, hogy az Aspose.3D for Java megfelelően telepítve van.

## Step 2: Initialize the Base Profile

Hozzon létre egy alap profilt az extrúzióhoz, ebben az esetben egy `RectangleShape`-t 0,3‑es lekerekítési sugárral.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
// Initialize the base profile to be extruded
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Step 3: Create a 3D Scene

Építsen egy 3D jelenetet, amely a extrudált objektumait tartalmazza.

```java
// Create a scene
Scene scene = new Scene();
```

## Step 4: Create Nodes

Hozzon létre csomópontokat a jelenetben a különböző entitások ábrázolásához.

```java
// Create left node
Node left = scene.getRootNode().createChildNode();
// Create right node
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Step 5: Perform Linear Extrusion

Használja a lineáris extrúziót mind a bal, mind a jobb csomópontokon különböző tulajdonságokkal.

```java
// Perform linear extrusion on left node using twist and slices property
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// Perform linear extrusion on right node using twist, twist offset, and slices property
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

## Step 6: Save the 3D Scene

Mentse el az újonnan létrehozott 3D jelenetet a megadott fájlformátummal.

```java
// Save 3D scene
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## How to save 3d model and export 3d obj

Az előző lépésben a `scene.save` hívás **saves the 3d model** OBJ fájlként, amely egy széles körben támogatott **export 3d obj** formátum. A fájlnevet megváltoztathatja, vagy más támogatott formátumot (pl. STL, FBX) választhat a `FileFormat` enum módosításával.

## Conclusion

Gratulálunk! Sikeresen megvalósította a Twist Offset-et a Linear Extrusion-ben az Aspose.3D for Java használatával. Ez a hatékony funkció új lehetőségeket nyit meg 3D modellezési tevékenységeihez, lehetővé téve, hogy **create 3d scene** összetett csavarokkal és eltolásokkal, majd **save 3d model** egy olyan formátumban, amely készen áll a további feldolgozási csővezetékekhez.

## FAQ's

### Q1: Can I use Aspose.3D for Java in non-commercial projects?

A1: Igen, az Aspose.3D for Java használható kereskedelmi és nem kereskedelmi projektekben egyaránt. További részletekért tekintse meg a [licencelési lehetőségeket](https://purchase.aspose.com/buy).

### Q2: Where can I find support for Aspose.3D for Java?

A2: Látogasson el az [Aspose.3D for Java fórumra](https://forum.aspose.com/c/3d/18), hogy segítséget kapjon és csatlakozzon a közösséghez.

### Q3: Is there a free trial available for Aspose.3D for Java?

A3: Igen, a [kiadások oldalán](https://releases.aspose.com/) elérhető egy ingyenes próba verzió.

### Q4: How do I obtain a temporary license for Aspose.3D for Java?

A4: Ideiglenes licencet szerezhet a projekthez a [következő hivatkozáson](https://purchase.aspose.com/temporary-license/) keresztül.

### Q5: Are there additional examples and tutorials available?

A5: Igen, további példákért és részletes útmutatókért tekintse meg a [dokumentációt](https://reference.aspose.com/3d/java/).

## Frequently Asked Questions

**Q: Ez az útmutató része egy Aspose 3d tutorial sorozatnak?**  
A: Igen – ez egy hivatalos **aspose 3d tutorial**, amely a könyvtár egy konkrét funkcióját mutatja be.

**Q: Használhatok más alakzatot a téglalap helyett?**  
A: Természetesen. Bármely `IProfile` megvalósítás (pl. `CircleShape`, egyedi `PolygonShape`) extrudálható.

**Q: Mi történik, ha kihagyom a `setTwistOffset`-et?**  
A: Az extrúzió a profil kiindulási pontjától kezd el csavarodni, ami szimmetrikus csavart eredményez.

**Q: Hogyan növelhetem a csavar simaságát?**  
A: Növelje a `setSlices`-nek átadott értéket; a nagyobb szeletszám simább geometriát eredményez.

**Q: Milyen egyéb fájlformátumokra exportálhatok az OBJ mellett?**  
A: Az Aspose.3D támogatja az STL, FBX, GLTF, 3MF és több más formátumot a `FileFormat` enumon keresztül.

---

**Last Updated:** 2025-12-19  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

## TARGET KEYWORDS:

**Primary Keyword (HIGHEST PRIORITY):**  
create 3d scene  

**Secondary Keywords (SUPPORTING):**  
save 3d model, export 3d obj, aspose 3d tutorial