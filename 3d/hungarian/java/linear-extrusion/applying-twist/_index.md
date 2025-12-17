---
date: 2025-12-17
description: Tanulja meg, hogyan hozhat létre csavart 3D modellt az Aspose.3D for
  Java segítségével lineáris extrúziós csavarral, és exportálja OBJ fájlba Java-ban.
  Kövesse lépésről‑lépésre útmutatónkat.
linktitle: Applying Twist in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Csavart 3D modell létrehozása – Csavart elfordítás alkalmazása lineáris extrúzióban
  az Aspose.3D for Java segítségével
url: /hu/java/linear-extrusion/applying-twist/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Csavart lineáris extrudálás alkalmazása az Aspose.3D for Java-val

## Bevezetés

Üdvözöljük ebben a lépés‑ről‑lépésre útmutatóban, amely bemutatja, **hogyan hozhatunk létre csavart 3D modellt** lineáris extrudálás közben alkalmazott csavarral az Aspose.3D for Java segítségével. Legyen szó építészeti vizualizációkról, játék‑eszközökről vagy mérnöki prototípusokról, egy csavar dinamikus, spirális megjelenést kölcsönöz a geometriai alakzatnak néhány kódsorral.

## Gyors válaszok
- **Mit jelent a „csavar” az extrudálásnál?** A profil körbeforgását jelenti az extrudálási tengely körül, miközben a forma kiterjed.  
- **Melyik API osztály kezeli a csavart?** A `LinearExtrusion` osztály biztosítja a `setTwist` metódust.  
- **Szükségem van licencre a példa futtatásához?** Egy ingyenes próba verzió elegendő az értékeléshez; a kereskedelmi licenc a termeléshez kötelező.  
- **Exportálhatom a végeredményt OBJ formátumban?** Igen, használja a `scene.save(..., FileFormat.WAVEFRONTOBJ)` hívást.  
- **Milyen Java verzió szükséges?** A Java 8 vagy újabb verzió teljes körűen támogatott.

## Előfeltételek

Mielőtt elkezdené a gyakorlati részt, győződjön meg arról, hogy a következő előfeltételek teljesülnek:

- Java fejlesztői környezet: Ellenőrizze, hogy a Java telepítve van a rendszerén.  
- Aspose.3D könyvtár: Töltse le és telepítse az Aspose.3D for Java könyvtárat a [letöltési hivatkozásról](https://releases.aspose.com/3d/java/).  
- Dokumentáció: Tekintse meg az [Aspose.3D dokumentációt](https://reference.aspose.com/3d/java/) a részletes útmutatásért.

## Csomagok importálása

A kódolás megkezdése előtt importálja a szükséges csomagokat a Java projektjébe. Az alábbi példa mutatja, hogyan:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Dokumentumkönyvtár beállítása

Először határozza meg, hogy hová mentse a generált 3D fájlt.

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## Alapprofil inicializálása

Ezután hozza létre a formát, amelyet extrudálni fog. Ebben a példában egy kis lekerekítéssel ellátott téglalapot használunk.

```java
// ExStart:InitializeBaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:InitializeBaseProfile
```

## Jelenet létrehozása

A `Scene` objektum a 3D csomópontok tárolója.

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
```

## Csomópontok létrehozása

Adjon hozzá két gyermek‑csomópontot a jelenethez – az egyik egyenes marad, a másik megkapja a csavart.

```java
// ExStart:CreateNodes
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CreateNodes
```

## Lineáris extrudálás csavarral

Most hajtjuk végre a **lineáris extrudálás csavart** mindkét csomóponton. A bal csomópont 0°‑os csavart (egyenes) kap, míg a jobb csomópont 90°‑os csavart, amely spirális alakzatot eredményez. Emellett beállítjuk a szeletek számát a sima geometria biztosításához.

```java
// ExStart:LinearExtrusionWithTwist
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd:LinearExtrusionWithTwist
```

## OBJ fájl exportálása Java‑ban

Végül mentse a jelenetet a széles körben támogatott OBJ formátumban. Ez bemutatja az Aspose.3D **OBJ fájl exportálása Java‑ban** képességét.

```java
// ExStart:Save3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:Save3DScene
```

## Miért fontos ez

Egy csavart 3D modell létrehozása erőteljes vizuális hatást biztosít anélkül, hogy külső modellező eszközökre lenne szükség. Különösen hasznos:

- **Mechanikai alkatrészek** esetén, amelyeknek csavart jellemzőkre van szükségük (pl. rugók, csavarok).  
- **Művészi tervezések** esetén, ahol egy finom spirál vizuális érdeklődést ad.  
- **Játék‑eszközök** esetén, amelyek előnyben részesítik az alacsony poligonszámú, procedurálisan generált geometriát.

## Gyakori problémák és tippek

| Probléma | Megoldás |
|----------|----------|
| A csavar lapos vagy hiányzik | Győződjön meg róla, hogy a `setSlices` értéke elég magas (pl. 100) a sima forgáshoz. |
| Az OBJ fájl nem nyílik meg a megjelenítőben | Ellenőrizze, hogy a kimeneti útvonal (`MyDir`) helyes, és a fájl írási jogosultsággal rendelkezik. |
| Váratlan méretezés | Nézze meg a forrásprofil egységrendszerét; az Aspose.3D alapértelmezés szerint méterben dolgozik. |

## Gyakran feltett kérdések

**K: Használhatom az Aspose.3D for Java‑t más 3D fájlformátumokkal is?**  
V: Igen, az Aspose.3D számos formátumot támogat, például FBX, STL, 3MF és még sok más.

**K: Hol találok támogatást az Aspose.3D for Java‑hoz?**  
V: Látogassa meg az [Aspose.3D fórumot](https://forum.aspose.com/c/3d/18) a közösségi segítségért és a hivatalos támogatásért.

**K: Elérhető ingyenes próba verzió?**  
V: Igen, letölthet egy próba verziót [innen](https://releases.aspose.com/).

**K: Hogyan szerezhetek ideiglenes licencet teszteléshez?**  
V: Ideiglenes licencet a [temporary license page](https://purchase.aspose.com/temporary-license/) oldalon kaphat.

**K: Hol vásárolhatok teljes licencet?**  
V: Az Aspose.3D for Java teljes licencét a [buying page](https://purchase.aspose.com/buy) oldalon vásárolhatja meg.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Utoljára frissítve:** 2025-12-17  
**Tesztelt verzió:** Aspose.3D 24.11 for Java  
**Szerző:** Aspose  

---