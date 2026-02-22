---
date: 2026-02-22
description: Tanulja meg, hogyan hozhat létre 3D extrudálást szeletekkel az Aspose.3D
  for Java segítségével. Ez a lépésről‑lépésre útmutató a lineáris extrudálást, a
  lekerekítési sugár beállítását és az OBJ exportálását tárgyalja.
linktitle: Create 3D Extrusion with Slices – Aspose.3D for Java
second_title: Aspose.3D Java API
title: 3D extrúzió létrehozása szeletekkel – Aspose.3D for Java
url: /hu/java/linear-extrusion/specifying-slices/
weight: 13
---

 to keep markdown formatting, code fences not present, just placeholders.

Let's craft translation.

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D Extrudálás létrehozása szeletekkel – Aspose.3D for Java

## Bevezetés

Ha **3d extrudálás** objektumokat kell létrehoznod, amelyek simák és pontosak, a szeletek számának szabályozása a kulcs. Ebben az útmutatóban végigvezetünk, hogyan adhatók meg a szeletek lineáris extrudálás során az Aspose.3D for Java használatával. Meg fogod érteni, miért fontos a szeletszám, hogyan állítható be a lekerekítési sugár, és hogyan exportálható az eredmény OBJ fájlként, amely bármely 3D folyamatban felhasználható.

## Gyors válaszok
- **Mit szabályoz a „szeletek” beállítása?** A köztes keresztmetszetek száma, amelyet a felület közelítésére használnak.  
- **Melyik metódus állítja be a szeletszámot?** `LinearExtrusion.setSlices(int)`  
- **Megváltoztathatom a profil lekerekítési sugarát?** Igen, a `RectangleShape.setRoundingRadius(double)` segítségével  
- **Milyen fájlformátumot használ ez a példa?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **Szükség van licencre a kód futtatásához?** Egy ingyenes próba a kiértékeléshez elegendő; a gyártási környezethez kereskedelmi licenc szükséges.

## Mi az a lineáris extrudálás szeletekkel?

A lineáris extrudálás egy 2‑D profilt (például egy téglalapot) nyújt ki egy egyenes mentén, hogy 3‑D szilárd testet hozzon létre. A **szeletek** megadásával azt mondod meg az Aspose.3D‑nek, hány köztes lépést generáljon, ami közvetlenül befolyásolja a görbületek, például egy lekerekített téglalap, simaságát.

## Miért használjuk az Aspose.3D for Java‑t 3d extrudálás létrehozásához?

* **Teljes irányítás** – Programozottan állítható a szeletszám, a lekerekítési sugár és az export formátum.  
* **Keresztplatformos** – Bármely Java‑képességű környezetben működik natív függőségek nélkül.  
* **Export rugalmasság** – Közvetlenül menthető OBJ, FBX, STL és számos más formátumba.

## Előkövetelmények

1. **Java Development Kit** – JDK 8 vagy újabb telepítve.  
2. **Aspose.3D for Java** – Töltsd le a könyvtárat a hivatalos oldalról [itt](https://releases.aspose.com/3d/java/).  
3. Egy IDE vagy szövegszerkesztő a választásod szerint.

## Csomagok importálása

Add hozzá az Aspose.3D névteret a projektedhez, hogy elérhesd a 3‑D modellező osztályokat.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Lépésről‑lépésre útmutató

### 1. lépés: A jelenet beállítása és a profil meghatározása

Először létrehozunk egy `RectangleShape`‑t, és megadunk neki egy **lekerekítési sugarat**, hogy a sarkok simák legyenek. Ezután inicializálunk egy új `Scene`‑t, amely a teljes geometriát tárolja.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### 2. lépés: **Gyermek csomópont** objektumok létrehozása minden extrudáláshoz

Minden geometriai elem egy `Node` alatt él. Itt két testvér csomópontot generálunk – egyet alacsony szeletszámú extrudáláshoz és egyet magas szeletszámú extrudáláshoz – és a bal csomópontot egy kicsit oldalra toljuk, hogy az eredmények könnyen összehasonlíthatók legyenek.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### 3. lépés: Lineáris extrudálás végrehajtása és **szeletek beállítása**

Most ténylegesen **3d extrudálás** objektumokat hozunk létre. A `LinearExtrusion` konstruktor a profilt és az extrudálási mélységet veszi át. Egy **névtelen belső osztály** segítségével meghívjuk a `setSlices`‑t a simaság szabályozásához. A bal csomópont csak 2 szeletet kap (durva), míg a jobb csomópont 10 szeletet (sima).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### 4. lépés: **OBJ exportálása** – a jelenet mentése

Végül a jelenetet egy Wavefront OBJ fájlba írjuk, amelyet széles körben támogatnak a 3‑D szerkesztők és játékmotorok. Ez bemutatja az Aspose.3D **export obj java** képességét.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Gyakori problémák és megoldások

| Probléma | Miért fordul elő | Megoldás |
|----------|------------------|----------|
| **Az extrudálás laposnak tűnik** | A szeletszám 1‑re vagy 0‑ra van állítva | Győződj meg róla, hogy a `setSlices` értéke ≥ 2. |
| **A lekerekített sarkok szaggatottak** | A lekerekítési sugár túl kicsi a szeletszámhoz képest | Növeld vagy a sugarat, vagy a szeletszámot a simább ívekért. |
| **Fájl nem található mentéskor** | `MyDir` egy nem létező mappára mutat | Hozd létre a könyvtárat előre, vagy használj abszolút elérési utat. |

## Gyakran feltett kérdések

**Q: Hogyan tölthetem le az Aspose.3D for Java‑t?**  
A: A könyvtárat [itt](https://releases.aspose.com/3d/java/) töltheted le.

**Q: Hol találom az Aspose.3D dokumentációját?**  
A: A dokumentációt [itt](https://reference.aspose.com/3d/java/) érheted el.

**Q: Elérhető ingyenes próba?**  
A: Igen, egy ingyenes próbát [itt](https://releases.aspose.com/) felfedezhetsz.

**Q: Hogyan kaphatok támogatást az Aspose.3D‑hez?**  
A: Látogasd meg a támogatási fórumot [itt](https://forum.aspose.com/c/3d/18).

**Q: Vásárolhatok ideiglenes licencet?**  
A: Igen, ideiglenes licencet [itt](https://purchase.aspose.com/temporary-license/) szerezhetsz.

---

**Utolsó frissítés:** 2026-02-22  
**Tesztelt verzió:** Aspose.3D for Java 24.11 (a kiadás időpontjában a legújabb)  
**Szerző:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}