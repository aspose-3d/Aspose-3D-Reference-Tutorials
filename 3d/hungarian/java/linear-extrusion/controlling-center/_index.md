---
date: 2025-12-18
description: Tanulja meg, hogyan adjon hozzá alap síkot, és állítsa be a középpont
  tulajdonságot lineáris extrúzióban az Aspose.3D for Java segítségével, lépésről
  lépésre kódpéldákkal.
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Hogyan adjon hozzá föld síkot és vezérlőközpontot lineáris extrúzióhoz az Aspose.3D
  for Java használatával
url: /hu/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Középpont vezérlése lineáris extrudálásnál az Aspose.3D for Java használatával

## Bevezetés

Amikor 3D jeleneteket építesz Java-ban, a **ground plane hozzáadása** és a lineáris extrudálás **center property** pontos beállítása jelentősen befolyásolhatja, hogy egy lapos prototípus vagy egy kifinomult vizuális megjelenés jön létre. Ebben az útmutatóban végigvezetünk a teljes folyamaton, hogyan vezérelheted az extrudálás középpontját és hogyan adhatod hozzá a ground plane-t az Aspose.3D for Java használatával. Megtudod, miért fontos ez, hogyan állíthatod be, és kapsz egy kész‑futtatható kódrészletet, amelyet saját projektjeidhez adaptálhatsz.

## Gyors válaszok
- **Mi csinál a “add ground plane”?** Létrehoz egy vékony referenciageometriát, amely segít látni az extrudálás helyzetét a világ tengelyeihez képest.  
- **Hogyan állíthatom be egy lineáris extrudálás középpontját?** Használd a `setCenter(boolean)` metódust a `LinearExtrusion` objektumon.  
- **Szükségem van licencre a minta futtatásához?** Egy ideiglenes licenc teszteléshez elegendő; a teljes licenc a termeléshez szükséges.  
- **Milyen fájlformátumot használ a mentés?** A példa Wavefront OBJ (`.obj`) formátumba ment.  
- **Milyen Java verzió szükséges?** Java 8 vagy újabb elegendő.

## Mi az a “add ground plane” egy 3D jelenetben?

A ground plane hozzáadása azt jelenti, hogy egy vékony téglalap alakú geometriát (gyakran egy minimális vastagságú dobo helyezünk el az X‑Z síkon. Ez vizuális padlóként működik, megkönnyítve más objektumok magasságának és igazításának megítélését, különösen extrudálási középpontok kísérletezésekor.

## Miért állítsuk be a center property-t egy lineáris extrudálásnál?

Alapértelmezés szerint egy lineáris extrudálás a profil eredetétől indul. A center property (`setCenter(true)`) beállítása eltolja a profilt, így az extrudálás az eredet körül középre kerül, ami szimmetrikus tervekhez vagy több objektum egységes igazításához hasznos.

## Előkövetelmények

Mielőtt elkezdenénk ezt az útmutatót, győződj meg róla, hogy a következő előkövetelmények teljesülnek:

1. **Java fejlesztői környezet** – Győződj meg róla, hogy a gépeden be van állítva egy Java fejlesztői környezet.  
2. **Aspose.3D for Java** – Töltsd le és telepítsd az Aspose.3D könyvtárat. A könyvtárat és a dokumentációt [itt](https://reference.aspose.com/3d/java/) találod.  
3. **Dokumentum könyvtár** – Hozz létre egy könyvtárat a Java dokumentumaid tárolásához. Hívjuk „Your Document Directory”-nek.

## Csomagok importálása

A Java fejlesztői környezetedben importáld a szükséges Aspose.3D csomagokat. Ez biztosítja, hogy a kódod hozzáférjen a könyvtár által nyújtott funkciókhoz.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 1. lépés: Az alap profil beállítása

Inicializáld az extrudálandó alap profilt. Ebben a példában egy 0,3 sugárú lekerekített téglalap alakzatot használunk.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## 2. lépés: 3D jelenet létrehozása

Építsd fel a 3D világod alapját egy jelenet létrehozásával.

```java
Scene scene = new Scene();
```

## 3. lépés: Bal és jobb csomópontok létrehozása

Hozz létre bal és jobb csomópontokat a jelenetben. Ezek a csomópontok szolgálnak a 3D objektumok vásznaként.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## 4. lépés: Lineáris extrudálás center property-vel (Bal csomópont)

Végezz lineáris extrudálást a bal csomóponton **középpont nélkül**, és állítsd be a szeletek számát 3-ra. Vedd észre a `setCenter(false)` hívást – itt **a center property** *false*-ra van állítva.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## 5. lépés: Ground plane hozzáadása referenciaként (Bal csomópont)

Javítsd a vizuális megjelenítést a bal csomóponthoz **ground plane** hozzáadásával. A vékony doboz padlóként működik, így egyértelműen látható az extrudálás magassága.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## 6. lépés: Lineáris extrudálás center property-vel (Jobb csomópont)

Most végezz lineáris extrudálást a jobb csomóponton, ezúttal **középre igazítva az extrudálást**. A `setCenter(true)` hívás azt mutatja, hogyan **a center property** *true*-ra van állítva.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## 7. lépés: Ground plane hozzáadása referenciaként (Jobb csomópont)

A bal oldalhoz hasonlóan adj hozzá egy ground plane-t a jobb csomóponthoz is, hogy egységes vizuális alapot kapj.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## 8. lépés: A 3D jelenet mentése

Mentsd el a 3D jelenetedet Wavefront OBJ formátumban, hogy bármely szabványos 3D megjelenítőben megtekinthető legyen.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Gyakori problémák és megoldások

| Probléma | Miért fordul elő | Megoldás |
|----------|------------------|----------|
| A ground plane nem látható | A doboz vastagsága túl kicsi a néző skálájához képest. | Növeld a vastagságot (a `Box` első paramétere) vagy zoomolj ki a nézőben. |
| Az extrudálás eltolódott | A `setCenter` értéke nem a kívánt módon van beállítva. | Ellenőrizd a `setCenter`-nek átadott boolean értéket. |
| A fájl nem mentődik | Hibás könyvtárútvonal vagy hiányzó írási jogosultság. | Győződj meg róla, hogy a `MyDir` egy létező, írási jogosultsággal rendelkező mappára mutat. |

## Gyakran feltett kérdések

**Q1: Használhatom az Aspose.3D for Java-t kereskedelmi projektekben?**  
A1: Igen, az Aspose.3D for Java kereskedelmi felhasználásra is elérhető. A licenc részletekért látogasd meg [itt](https://purchase.aspose.com/buy).

**Q2: Van elérhető ingyenes próba?**  
A2: Igen, az Aspose.3D for Java ingyenes próbaverzióját [itt](https://releases.aspose.com/) tekintheted meg.

**Q3: Hol találok támogatást az Aspose.3D for Java-hoz?**  
A3: Az Aspose.3D közösségi fórum egy nagyszerű hely a támogatás keresésére és tapasztalatok megosztására. Látogasd meg a fórumot [itt](https://forum.aspose.com/c/3d/18).

**Q4: Szükségem van ideiglenes licencre a teszteléshez?**  
A4: Igen, ha ideiglenes licencre van szükséged tesztelési célból, azt [itt](https://purchase.aspose.com/temporary-license/) szerezheted be.

**Q5: Hol találom a dokumentációt?**  
A5: Az Aspose.3D for Java dokumentációja [itt](https://reference.aspose.com/3d/java/) érhető el.

## Összegzés

A lineáris extrudálás középpontjának vezérlése **és** a **ground plane** hozzáadásának megtanulása az Aspose.3D for Java-val izgalmas lehetőségeket nyit a 3D grafikai fejlesztésben. A fenti lépések követésével most egy újrahasználható mintát kaptál középre igazított extrudálások, vizuális referenciaplane-ok létrehozásához, valamint az eredmény OBJ formátumba exportálásához. Nyugodtan kísérletezz különböző profilokkal, szeletszámokkal és transzformációkkal, hogy a saját projekted igényeihez illeszkedjen.

---

**Utolsó frissítés:** 2025-12-18  
**Tesztelve:** Aspose.3D 24.11 for Java (a legfrissebb a írás időpontjában)  
**Szerző:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}