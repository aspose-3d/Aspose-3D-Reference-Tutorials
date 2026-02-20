---
date: 2026-02-20
description: Tanulj egy Java 3D grafikai oktatót a középpont vezérléséről lineáris
  extrudálásnál az Aspose.3D-vel, beleértve, hogyan állítsd be a lekerekítési sugár
  értékét és hogyan mentsd el az OBJ fájlt Java-ban.
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Java 3D grafika útmutató – Középpont a lineáris extrúzióban
url: /hu/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java 3D grafikai útmutató – Középpont a lineáris extrúzióban

## Bevezetés

Ha Java‑ban 3D vizualizációkat építesz, az extrúzió technikák elsajátítása elengedhetetlen. Ez a **java 3d graphics tutorial** végigvezet a lineáris extrúzió középpontjának vezérlésén az Aspose.3D for Java segítségével, így pontos, szimmetrikus modelleket hozhatsz létre extra számítások nélkül. A útmutató végére megérted, miért fontos a `center` tulajdonság, hogyan **állítsd be a lekerekítési sugár** értékét, és hogyan **mentsd el az OBJ fájlt java**‑kompatibilis formátumban.

## Gyors válaszok
- **Mit csinál a center tulajdonság?** Meghatározza, hogy az extrúzió szimmetrikus‑e a profil eredeténél.  
- **Szükségem van licencre a kód futtatásához?** Ideiglenes licenc teszteléshez elegendő; teljes licenc a termeléshez kötelező.  
- **Milyen fájlformátumot használ a végeredmény?** A jelenet Wavefront OBJ fájlként kerül mentésre.  
- **Megváltoztathatom a szeletek számát?** Igen, használd a `setSlices(int)` metódust a `LinearExtrusion` objektumon.  
- **Az Aspose.3D kompatibilis a Java 8+ verziókkal?** Teljesen – támogatja az összes modern Java verziót.

## Mi az a java 3d graphics tutorial?

Egy **java 3d graphics tutorial** lépésről‑lépésre bemutatja, hogyan használj Java könyvtárakat háromdimenziós objektumok létrehozásához, manipulálásához és rendereléséhez. Ebben az esetben az Aspose.3D extrúzió API‑ra fókuszálunk, amely a 2‑D profilokat teljes értékű 3‑D hálózatokká alakítja.

## Miért használjuk az Aspose.3D for Java‑t?

- **Magas szintű API** – Nem kell alacsony szintű hálózatszámításokat írni.  
- **Kereszt‑formátum támogatás** – Exportálás OBJ, FBX, STL és további formátumokba.  
- **Teljesítmény‑optimalizált** – Nagy jeleneteket hatékonyan kezel.  
- **Gazdag dokumentáció** – Példákat tartalmaz, mint az alább látható.

## Előfeltételek

Mielőtt belevágnál, győződj meg róla, hogy a következők rendelkezésre állnak:

1. **Java fejlesztői környezet** – Telepített JDK 8 vagy újabb.  
2. **Aspose.3D for Java** – Töltsd le a könyvtárat és a dokumentációt [itt](https://reference.aspose.com/3d/java/).  
3. **Dokumentum könyvtár** – Hozz létre egy mappát a gépeden a generált fájlok tárolására; ezt **„Your Document Directory”**‑nek nevezzük.

## Csomagok importálása

A Java IDE‑dben importáld az Aspose.3D osztályokat, amikre szükséged lesz. Ez hozzáférést biztosít a fordítónak az extrúzió és a jelenet‑építés funkciókhoz.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Lépés‑ről‑lépésre útmutató

### 1. lépés: Alap profil beállítása

Először hozd létre a 2‑D alakzatot, amelyet extrudálni szeretnél. Itt egy téglalapot használunk, és **beállítjuk a lekerekítési sugár** értékét 0,3‑ra, ami kisimítja a sarkokat.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### 2. lépés: 3D jelenet létrehozása

A `Scene` objektum a konténer minden 3‑D csomópont, fény és kamera számára.

```java
Scene scene = new Scene();
```

### 3. lépés: Bal és jobb csomópontok hozzáadása

Két különálló csomópontot helyezünk el egymás mellett, hogy össze tudd hasonlítani az extrúziót középpont nélkül és középponttal.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### 4. lépés: Lineáris extrúzió – Nincs középpont (Bal csomópont)

Hozd létre az extrúziót a bal csomóponton, tiltsd le a középpontot, és korlátozd a hálót három szeletre egy alacsony poligonszámú előnézethez.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

### 5. lépés: Referenciapontként föld sík hozzáadása (Bal csomópont)

Egy vékony doboz szolgál vizuális padlóként, segítve az extrúzió tájolásának megértését.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

### 6. lépés: Lineáris extrúzió – Középponttal (Jobb csomópont)

Most ismételd meg az extrúziót, de ezúttal engedélyezd a `center` beállítást. A geometria szimmetrikus lesz a profil eredeténél.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

### 7. lépés: Referenciapontként föld sík hozzáadása (Jobb csomópont)

Ugyanaz a föld sík a jobb oldalra, így a összehasonlítás egyértelmű.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

### 8. lépés: 3D jelenet mentése

Végül exportáld a teljes jelenetet Wavefront OBJ fájlba – egy formátumba, amely szinte minden 3‑D szerkesztőben használható.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Gyakori problémák és megoldások

| Probléma | Miért fordul elő | Megoldás |
|----------|------------------|----------|
| **Az extrúzió el van tolva** | `setCenter(false)` a profilt a sarkán rögzíti. | Használd a `setCenter(true)`‑t a szimmetrikus eredményhez. |
| **Az OBJ fájl üres** | A kimeneti könyvtár útvonala hibás vagy nincs írási jogosultság. | Ellenőrizd, hogy a `MyDir` egy létező mappára mutat, és az alkalmazásnak van írási joga. |
| **A lekerekített sarkok élesek** | A lekerekítési sugár túl kicsi a téglalap méretéhez képest. | Növeld a sugár értékét (pl. `setRoundingRadius(0.5)`). |

## Gyakran feltett kérdések

### Q1: Használhatom az Aspose.3D for Java‑t kereskedelmi projektekben?

A1: Igen, az Aspose.3D for Java kereskedelmi felhasználásra is elérhető. A licencelési részletekért látogass el [ide](https://purchase.aspose.com/buy).

### Q2: Van ingyenes próba verzió?

A2: Igen, az Aspose.3D for Java ingyenes próbaverzióját [itt](https://releases.aspose.com/) töltheted le.

### Q3: Hol találok támogatást az Aspose.3D for Java‑hoz?

A3: Az Aspose.3D közösségi fórum kiváló hely a támogatás keresésére és tapasztalatok megosztására. Látogasd meg a fórumot [ide](https://forum.aspose.com/c/3d/18).

### Q4: Szükségem van ideiglenes licencre a teszteléshez?

A4: Igen, ha ideiglenes licencre van szükséged teszteléshez, azt [itt](https://purchase.aspose.com/temporary-license/) szerezheted be.

### Q5: Hol találom a dokumentációt?

A5: Az Aspose.3D for Java dokumentációja elérhető [itt](https://reference.aspose.com/3d/java/).

## Összegzés

A **java 3d graphics tutorial** elvégzésével most már tudod, hogyan szabályozd a lineáris extrúzió középpontját, állítsd be a lekerekítési sugár értékét, és **mentsd el az OBJ fájlt java**‑kompatibilis formátumban az Aspose.3D segítségével. Ezek a technikák finomhangolt kontrollt biztosítanak a háló szimmetriája felett, ami kulcsfontosságú játékeszközök, CAD prototípusok és tudományos vizualizációk esetén. Nyugodtan kísérletezz különböző profilokkal, szeletszámokkal és export formátumokkal, hogy bővítsd 3‑D eszköztáradat.

---

**Utolsó frissítés:** 2026-02-20  
**Tesztelt verzió:** Aspose.3D for Java 24.11  
**Szerző:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}