---
date: 2026-04-03
description: Tanulja meg, hogyan hozhat létre hengeres ventilátor alakzatot Java-ban
  az Aspose.3D segítségével. Ez az útmutató lefedi a Java 3D modellezést és az OBJ
  fájl mentésének Java technikáit.
keywords:
- create cylinder fan shape
- save obj file java
- aspose 3d export obj
linktitle: Hogyan hozhatunk létre hengeres ventilátor alakot az Aspose.3D for Java
  segítségével
second_title: Aspose.3D Java API
title: Hogyan készítsünk hengeres ventilátor alakot az Aspose.3D for Java segítségével
url: /hu/java/cylinders/creating-fan-cylinders/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hogyan hozzunk létre hengeres ventilátor alakzatot az Aspose.3D for Java segítségével

## Bevezetés

Készen állsz arra, hogy elsajátítsd, **hogyan hozz létre hengeres ventilátor alakzatot** egy Java környezetben? Ebben az útmutatóban minden lépésen végigvezetünk – a jelenet beállításától a Wavefront OBJ fájl exportálásáig – az Aspose.3D használatával. Akár játékeszközt, CAD prototípust építesz, vagy csak 3D geometria kísérletezel, látni fogod, milyen egyszerű a Java 3D modellezés ezzel a hatékony könyvtárral.

## Gyors válaszok
- **Mi a fő cél?** Testreszabható ventilátor alakú henger létrehozása és OBJ fájlként mentése.  
- **Melyik könyvtárat használjuk?** Aspose.3D for Java.  
- **Szükség van licencre?** Egy ingyenes próba a fejlesztéshez elegendő; a termeléshez kereskedelmi licenc szükséges.  
- **Mik a előfeltételek?** Telepített JDK és az Aspose.3D Java csomag hozzáadva a projektedhez.  
- **Exportálhatok más formátumokat is?** Igen – az Aspose.3D sok formátumot támogat; ebben a példában a Wavefront OBJ-t használjuk.

## Mi az a ventilátor henger?

A ventilátor henger egy részlegesen felületű henger, ahol a kör alapjának egy szektora hiányzik, így „ventilátor” nyílást hozva létre. Ez a geometria hasznos szeletek, műszerfalak vagy egyedi mechanikai alkatrészek megjelenítéséhez.

## Miért használjuk az Aspose.3D-t Java 3D modellezéshez?

Az Aspose.3D egy tiszta, objektum‑orientált API-t biztosít, amely elrejti a 3D grafika alacsony szintű matematikáját. A tervezésre koncentrálhatsz a fájlformátum sajátosságai helyett, és a könyvtár automatikusan kezeli a **save obj file java** műveleteket.

## Előfeltételek

Mielőtt belemerülnénk, győződj meg róla, hogy rendelkezel:

- **Java Development Kit (JDK)** – töltsd le [itt](https://www.oracle.com/java/technologies/javase-downloads.html).  
- **Aspose.3D for Java** – szerezd be a legújabb JAR-t a [letöltési hivatkozásból](https://releases.aspose.com/3d/java/).  

Add the Aspose.3D JAR to your project’s classpath.

## Csomagok importálása

Kezdjük a szükséges osztályok importálásával. Ez hozzáférést biztosít a 3D jelenethez, a geometriai primitívekhez és a segédmetódusokhoz.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 1. lépés: Jelenet létrehozása

Először egy új `Scene` példányt hozunk létre. A jelenetet tekintheted egy tárolónak, amely az összes 3D objektumot, fényt és kamerát tartalmazza.

```java
// ExStart:2
// Create a Scene
Scene scene = new Scene();
// ExEnd:2
```

## 2. lépés: Ventilátor henger létrehozása (hogyan hozzunk létre hengert)

Most felépítjük magát a ventilátor hengert. A konstruktor paraméterei határozzák meg a sugár, magasság, felosztás (tessellation) és azt, hogy a geometria ventilátorként legyen-e generálva.

```java
// ExStart:3
// Create a cylinder with fan
Cylinder fan = new Cylinder(2, 2, 10, 20, 1, false);
fan.setGenerateFanCylinder(true);
fan.setThetaLength(MathUtils.toRadian(270.0));
// ExEnd:3
```

> **Pro tipp:** Állítsd be a `setThetaLength` értékét a nyílásszög módosításához. 270° egy háromnegyedes ventilátort hoz létre; 180° egy félhenger lenne.

## 3. lépés: A ventilátor henger elhelyezése

Ezután hozzáadjuk a ventilátor hengert a jelenethez, és egy kényelmes helyre helyezzük. A transzláció koordinátái a (X, Y, Z) sorrendben vannak.

```java
// ExStart:4
// Create ChildNode and set translation
scene.getRootNode().createChildNode(fan).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

## 4. lépés: Nem‑ventilátor henger létrehozása (java 3d modellezési összehasonlítás)

Az Aspose.3D rugalmasságának bemutatására egy szabályos hengert is létrehozunk, amelynek nincs ventilátor nyílása.

```java
// ExStart:5
// Create a cylinder without a fan
Cylinder nonfan = new Cylinder(2, 2, 10, 20, 1, false);
// Create ChildNode
scene.getRootNode().createChildNode(nonfan);
// ExEnd:5
```

## 5. lépés: Jelenet mentése (java save obj file)

Végül exportáljuk a teljes jelenetet egy Wavefront OBJ fájlba. Ez a formátum széles körben támogatott a legtöbb 3D szerkesztő és játék motor által.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

> **Megjegyzés:** Cseréld le a `"Your Document Directory"`-t egy abszolút vagy relatív útvonalra, ahol írási jogosultsággal rendelkezel.

## Hogyan mentünk OBJ fájlt Java-ban az Aspose 3D használatával

Az Aspose.3D `Scene.save` metódusa automatikusan kezeli a **aspose 3d export obj** folyamatot. Csak meg kell adnod a célfájl nevét és a `FileFormat.WAVEFRONTOBJ` enum értéket, ahogy az előző lépésben láttad.

## Gyakori problémák és megoldások

| Probléma | Ok | Megoldás |
|----------|----|----------|
| OBJ fájl üres | A jelenet nincs mentve vagy az útvonal helytelen | Ellenőrizd, hogy a kimeneti könyvtár létezik és írási jogosultsággal rendelkezik. |
| A ventilátor nyílása hibás | Hibás `ThetaLength` érték | Használd a `MathUtils.toRadian(degrees)`-t a szükséges pontos szög beállításához. |
| Fordítási hibák | Hiányzó Aspose.3D JAR a classpath-ban | Add the JAR to your project’s `libs` folder and include it in the build path. |

## Gyakran feltett kérdések

**K: Az Aspose.3D kompatibilis más Java 3D könyvtárakkal?**  
V: Igen, az Aspose.3D együtt tud működni olyan könyvtárakkal, mint a Java 3D vagy a jMonkeyEngine, lehetővé téve egyedi geometria integrálását nagyobb folyamatokba.

**K: Testreszabhatom tovább a ventilátor henger megjelenését?**  
V: Természetesen. Anyagokat, textúrákat és megvilágítást alkalmazhatsz a node `Material` és `Light` gyűjteményeinek elérésével.

**K: Hol kaphatok további támogatást?**  
V: Látogasd meg az [Aspose.3D fórumot](https://forum.aspose.com/c/3d/18) a közösségi segítségért és hivatalos válaszokért.

**K: Elérhető ingyenes próba?**  
V: Igen, a vásárlás előtt egy [ingyenes próbát](https://releases.aspose.com/) használhatsz az Aspose.3D felfedezéséhez.

**K: Hogyan szerezhetek ideiglenes licencet teszteléshez?**  
V: Szerezz egyet [itt](https://purchase.aspose.com/temporary-license/), hogy a fejlesztés során teljes funkcionalitást kapj.

---

**Utoljára frissítve:** 2026-04-03  
**Tesztelve:** Aspose.3D 24.11 for Java  
**Szerző:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}