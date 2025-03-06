---
title: Vezérlőközpont a Lineáris extrudálásban Aspose.3D for Java segítségével
linktitle: Vezérlőközpont a Lineáris extrudálásban Aspose.3D for Java segítségével
second_title: Aspose.3D Java API
description: Fedezze fel a 3D grafika világát Java nyelven az Aspose.3D segítségével. Könnyedén irányíthatja a középpontot lineáris extrudálással.
weight: 11
url: /hu/java/linear-extrusion/controlling-center/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Vezérlőközpont a Lineáris extrudálásban Aspose.3D for Java segítségével

## Bevezetés

3D grafika és a Java programozás világában a lineáris extrudálás során a központ vezérlése döntő szerepet játszik a kívánt hatások elérésében a projektekben. Az Aspose.3D for Java hatékony eszközkészletet biztosít az ilyen feladatok zökkenőmentes kezelésére. Ebben az oktatóanyagban belemerülünk a központ vezérlésének folyamatába a lineáris kihúzás során az Aspose.3D for Java használatával, az egyes lépéseket lebontva a zökkenőmentes és átfogó megértés érdekében.

## Előfeltételek

Mielőtt nekivágnánk ennek az oktatóanyagnak, győződjön meg arról, hogy a következő előfeltételek teljesülnek:

1. Java fejlesztői környezet: Győződjön meg arról, hogy be van állítva Java fejlesztői környezet a gépén.

2.  Aspose.3D for Java: Töltse le és telepítse az Aspose.3D könyvtárat. Megtalálható a könyvtár és a dokumentációja[itt](https://reference.aspose.com/3d/java/).

3. Dokumentumkönyvtár: Hozzon létre egy könyvtárat a Java dokumentumok tárolására. Nevezzük "Az Ön dokumentumkönyvtárának".

## Csomagok importálása

Java fejlesztői környezetben importálja az Aspose.3D szükséges csomagjait. Ez biztosítja, hogy kódja hozzáférjen a könyvtár által biztosított funkciókhoz.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 1. lépés: Állítsa be az alapprofilt

Inicializálja az extrudálandó alapprofilt. Ebben a példában 0,3-as lekerekítési sugarú téglalap alakot fogunk használni.

```java
// A dokumentumok könyvtárának elérési útja.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## 2. lépés: Hozzon létre egy 3D-s jelenetet

Építsd meg 3D-s világod alapjait egy jelenet létrehozásával.

```java
Scene scene = new Scene();
```

## 3. lépés: Hozzon létre bal és jobb csomópontokat

Hozzon létre bal és jobb csomópontokat a jeleneten belül. Ezek a csomópontok vászonként szolgálnak a 3D objektumok számára.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## 4. lépés: Lineáris extrudálás középső tulajdonsággal

Végezzen lineáris extrudálást a bal oldali csomóponton központosítás nélkül, és állítsa a szeletek számát 3-ra.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## 5. lépés: Állítsa be a talajsíkot referenciaként

Javítsa a vizuális megjelenítést egy alapsík hozzáadásával a bal csomóponthoz.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## 6. lépés: Lineáris extrudálás középső tulajdonsággal (jobb csomópont)

Hajtsa végre a lineáris kihúzást a jobb oldali csomóponton, ezúttal középre állítva az extrudálást, és ismét állítsa a szeletek számát 3-ra.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## 7. lépés: Állítsa be a talajsíkot referenciaként (jobb oldali csomópont)

A bal csomóponthoz hasonlóan referenciaként adjon hozzá egy alapsíkot a jobb oldali csomóponthoz.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## 8. lépés: Mentse el a 3D-s jelenetet

Mentse el 3D jelenetét Wavefront OBJ formátumban.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Következtetés

A központ lineáris extrudálással történő vezérlése az Aspose.3D for Java segítségével izgalmas lehetőségeket nyit meg a 3D-s grafika fejlesztésében. Ennek a lépésről-lépésre szóló útmutatónak a követésével megtanulta, hogyan kell kezelni a központi tulajdonságot, lehetővé téve a kívánt vizuális effektusok elérését a Java-projektekben.

## GYIK

### 1. kérdés: Használhatom az Aspose.3D for Java-t kereskedelmi projektekben?

 1. válasz: Igen, az Aspose.3D for Java kereskedelmi használatra elérhető. Az engedélyezés részleteiért látogasson el a webhelyre[itt](https://purchase.aspose.com/buy).

### 2. kérdés: Van ingyenes próbaverzió?

 2. válasz: Igen, kipróbálhatja az Aspose.3D for Java ingyenes próbaverzióját[itt](https://releases.aspose.com/).

### 3. kérdés: Hol találok támogatást az Aspose.3D for Java számára?

 3. válasz: Az Aspose.3D közösségi fórum egy nagyszerű hely, ahol támogatást kérhet és megoszthatja tapasztalatait. Látogassa meg a fórumot[itt](https://forum.aspose.com/c/3d/18).

### 4. kérdés: Szükségem van ideiglenes licencre a teszteléshez?

V4: Igen, ha tesztelési célból ideiglenes licencre van szüksége, beszerezhet egyet[itt](https://purchase.aspose.com/temporary-license/).

### 5. kérdés: Hol találom a dokumentációt?

 5. válasz: Az Aspose.3D for Java dokumentációja elérhető[itt](https://reference.aspose.com/3d/java/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
