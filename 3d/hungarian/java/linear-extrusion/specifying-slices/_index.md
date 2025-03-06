---
title: Szeletek megadása a Lineáris extrudálásban az Aspose.3D for Java segítségével
linktitle: Szeletek megadása a Lineáris extrudálásban az Aspose.3D for Java segítségével
second_title: Aspose.3D Java API
description: Tanuljon meg szeleteket megadni lineáris extrudálás során az Aspose.3D for Java használatával. Növelje 3D-s modellezési készségeit ezzel a lépésről lépésre bemutatott útmutatóval.
weight: 13
url: /hu/java/linear-extrusion/specifying-slices/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Szeletek megadása a Lineáris extrudálásban az Aspose.3D for Java segítségével

## Bevezetés

A bonyolult 3D-s modellek létrehozása gyakran nem csupán kreativitást igényel; megköveteli a rendelkezésére álló eszközök alapos megértését. Az Aspose.3D for Java játékot változtat ebben a tekintetben. Ebben az oktatóanyagban egy konkrét szempontra összpontosítunk – a szeletek megadására a lineáris extrudálás során.

## Előfeltételek

Mielőtt belevágna az oktatóanyagba, győződjön meg arról, hogy a következő előfeltételeket teljesítette:

1. Java környezet: Győződjön meg arról, hogy a rendszeren be van állítva Java fejlesztői környezet.
2.  Aspose.3D for Java: Töltse le és telepítse az Aspose.3D könyvtárat. A szükséges csomagokat megtalálod[itt](https://releases.aspose.com/3d/java/).

## Csomagok importálása

Java-projektjében importálja az Aspose.3D könyvtárat. Ez döntő fontosságú azokhoz a funkciókhoz való hozzáféréshez, amelyekkel dolgozni fogunk. Adja hozzá a következő importálási utasítást a kódhoz:

```java
import com.aspose.threed.*;

import java.io.IOException;
```

Most bontsuk fel a példát több lépésre.

## 1. lépés: Állítsa be a jelenetet

Inicializálja az extrudálandó alapprofilt, ebben az esetben a`RectangleShape` meghatározott kerekítési sugárral. Hozzon létre egy 3D-s jelenetet a munkavégzéshez.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

## 2. lépés: Hozzon létre csomópontokat

Bal és jobb csomópontok létrehozása a jeleneten belül. Állítsa be a bal oldali csomópont fordítását a térbeli eltérésekhez.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## 3. lépés: Lineáris extrudálás szeletekkel

Végezzen lineáris extrudálást mindkét csomóponton, és adja meg mindegyikhez a szeletek számát. Itt történik a varázslat.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

## 4. lépés: Mentse el a jelenetet

Mentse el a 3D jelenetet a kívánt formátumban, ebben az esetben egy Wavefront OBJ fájlban.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Következtetés

Gratulálunk! Sikeresen megtanulta, hogyan adhat meg szeleteket a lineáris kihúzás során az Aspose.3D for Java használatával. Ez a készség új lehetőségeket nyit meg a 3D modellezési utazás során.

## GYIK

### 1. kérdés: Hogyan tölthetem le az Aspose.3D for Java-t?

 V1: Letöltheti a könyvtárat[itt](https://releases.aspose.com/3d/java/).

### 2. kérdés: Hol találom az Aspose.3D dokumentációját?

 V2: Lásd a dokumentációt[itt](https://reference.aspose.com/3d/java/).

### 3. kérdés: Van ingyenes próbaverzió?

 3. válasz: Igen, felfedezheti az ingyenes próbaverziót[itt](https://releases.aspose.com/).

### 4. kérdés: Hogyan kaphatok támogatást az Aspose.3D-hez?

 4. válasz: Látogassa meg a támogatási fórumot[itt](https://forum.aspose.com/c/3d/18).

### 5. kérdés: Vásárolhatok ideiglenes licencet?

 V5: Igen, ideiglenes engedélyt lehet szerezni[itt](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
