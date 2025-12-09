---
date: 2025-12-06
description: Ismerje meg, hogyan menthet FBX fájlokat és hogyan kérdezheti le a jelenet
  információit az Aspose.3D for Java használatával. Ez a lépésről‑lépésre útmutató
  bemutatja az alkalmazás nevének beállítását, a mértékegységek meghatározását és
  a jelenet FBX‑be exportálását.
linktitle: How to Save FBX and Retrieve 3D Scene Info in Java
second_title: Aspose.3D Java API
title: Hogyan menthetünk FBX-et és szerezhetünk vissza 3D-s jelenetinformációkat Java-ban
url: /hu/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hogyan mentse el az FBX-et és szerezze meg a 3D jelenet információit Java-ban

## Bevezetés

Ha egy világos, gyakorlati útmutatót keres arra, **hogyan mentse el az fbx** fájlokat, miközben hasznos metaadatokat nyer ki a 3D jeleneteiből, jó helyen jár. Ebben a bemutatóban lépésről‑lépésre végigvezetjük a **Aspose.3D Java** könyvtár használatával: a jelenet létrehozásától, **az alkalmazás nevének beállításán**, **a mértékegységek meghatározásán**, egészen a **jelenet FBX‑be exportálásáig**. A végére egy használatra kész FBX fájlt kap, amely tartalmazza a downstream csővezetékekhez szükséges eszközinformációkat.

## Gyors válaszok
- **Mi a fő cél?** Egy FBX fájl mentése, amely egyedi eszközinformációkat tartalmaz.  
- **Melyik könyvtárat használja?** Aspose.3D for Java.  
- **Szükségem van licencre?** Egy ingyenes próba a fejlesztéshez elegendő; a termeléshez kereskedelmi licenc szükséges.  
- **Módosíthatom a mértékegységeket?** Igen – használja a `setUnitName` és `setUnitScaleFactor` metódusokat.  
- **Hol kerül mentésre a kimenet?** A `scene.save(...)`‑ben megadott útvonalra.

## Előfeltételek

Mielőtt elkezdenénk, győződjön meg róla, hogy rendelkezik:

- Alapos ismeretek a Java alap szintaxisáról.  
- **Aspose.3D for Java** letöltve és a projektjéhez hozzáadva (letöltheti a hivatalos) [Aspose 3D letöltési oldalról](https://releases.aspose.com/3d/java/).  
- Kedvenc Java IDE-je (IntelliJ IDEA, Eclipse, NetBeans, stb.) megfelelően beállítva.

## Csomagok importálása

A Java forrásfájlban importálja az Aspose.3D osztályokat, amelyek a jelenetkezelést és a fájlformátum‑támogatást biztosítják.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Pro tipp:** Tartsa a importlistát minimálisra, hogy elkerülje a felesleges függőségeket és javítsa a fordítási időket.

## Mi a folyamat az FBX fájl mentéséhez?

Az alábbi tömör, lépésről‑lépésre bemutatott útmutató megmutatja, **hogyan adjon hozzá eszközinformációkat** egy jelenethez, majd **exportálja a jelenetet FBX‑be**.

### 1. lépés: 3D jelenet inicializálása

Először hozzon létre egy üres `Scene` objektumot. Ez lesz a tároló minden geometria, fény, kamera és eszközmetaadat számára.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### 2. lépés: Alkalmazás és gyártó információ beállítása

Az egyedi metaadatok hozzáadása segíti a downstream eszközöket a fájl forrásának azonosításában. Itt **beállítjuk az alkalmazás nevét** és a gyártót az `AssetInfo` objektummal.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Miért fontos:** Sok pipeline szűri vagy címkézi az eszközöket a származási alkalmazás alapján, ezért ez a lépés elengedhetetlen nagy projektek esetén.

### 3. lépés: Mértékegységek meghatározása

Az Aspose.3D lehetővé teszi a jelenet által használt egységrendszer megadását. Ebben a példában egy ókori egyiptomi „pole” egységet használunk egy egyedi skálafaktorral.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Tipp:** Állítsa be a `unitScaleFactor`‑t úgy, hogy megfeleljen modelljei valós méretének; az 1.0 egy 1‑to‑1 leképezést jelent a választott egységgel.

### 4. lépés: Jelenet exportálása FBX-be

Miután az eszközinformációk csatolva lettek, mentjük a jelenetet FBX fájlként. A `FileFormat.FBX7500ASCII` opció ember‑olvasható ASCII FBX‑et hoz létre, ami hibakereséskor hasznos.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddAssetInformationToScene
```

> **Ne feledje:** Cserélje le a `"Your Document Directory"`‑t egy abszolút útvonalra vagy a projekt munkakönyvtárához relatív útvonalra.

### 5. lépés: Sikerüzenet kiírása

Egy egyszerű konzolkimenet megerősíti, hogy a művelet sikeres volt, és megmutatja, hová íródott a fájl.

```java
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
```

## Gyakori felhasználási esetek

- **Játék eszköz pipeline‑ok** – a készítő információ beágyazása közvetlenül az FBX fájlokba a verziókövetéshez.  
- **Építészeti vizualizáció** – projekt‑specifikus egységek tárolása a méretezési hibák elkerülése érdekében a renderelő motorokba importáláskor.  
- **Automatizált jelentés** – FBX fájlok valós időben generálása metaadatokkal, amelyeket a downstream analitikai eszközök olvashatnak.

## Hibaelhárítás és tippek

| Probléma | Megoldás |
|----------|----------|
| **Fájl nem található a mentés után** | Ellenőrizze, hogy a `MyDir` egy létező mappára mutat, és hogy az alkalmazásnak van írási joga. |
| **Az egységek helytelenül jelennek meg külső megjelenítőben** | Ellenőrizze újra a `unitScaleFactor`‑t; egyes megjelenítők alapegységként a métert várják. |
| **Az eszközmetaadat hiányzik** | Győződjön meg róla, hogy a `scene.getAssetInfo()`‑t **a mentés előtt** hívja; a `save()` után végzett módosítások nem kerülnek mentésre. |

## GyIK

### Q1: Az Aspose.3D kompatibilis minden Java IDE-vel?

A1: Igen, az Aspose.3D úgy lett tervezve, hogy zökkenőmentesen működjön minden nagyobb Java IDE-vel.

### Q2: Használhatom az Aspose.3D‑t kereskedelmi projektekhez?

A2: Természetesen. Az Aspose.3D kereskedelmi licenceket kínál fejlesztőknek, biztosítva, hogy megfeleljen a licencelési követelményeknek.

### Q3: Hol találok további támogatást az Aspose.3D-hez?

A3: Bármilyen kérdés vagy segítség esetén látogassa meg a [Aspose.3D fórumot](https://forum.aspose.com/c/3d/18).

### Q4: Van ingyenes próba az Aspose.3D-hez?

A4: Igen, a funkciókat egy ingyenes próba segítségével is felfedezheti, amely [itt](https://releases.aspose.com/) érhető el.

### Q5: Hogyan szerezhetek ideiglenes licencet az Aspose.3D-hez?

A5: Ideiglenes, tesztelési célú licencet [itt](https://purchase.aspose.com/temporary-license/) kaphat.

## Gyakran Ismételt Kérdések

**Q: Hogyan változtathatom meg a kimeneti formátumot bináris FBX‑re?**  
A: Cserélje le a `FileFormat.FBX7500ASCII`‑t `FileFormat.FBX7500`‑ra a `scene.save(...)` hívásakor.

**Q: Hozzáadhatok egyedi, felhasználó‑definiált metaadatokat a beépített eszközmezőkön kívül?**  
A: Igen, használja a `scene.getUserData().add("Key", "Value")`‑t további kulcs‑érték párok beágyazásához.

**Q: Támogatja az Aspose.3D más exportformátumokat, például OBJ vagy GLTF?**  
A: Igen. Egyszerűen változtassa meg a `FileFormat` enum értékét `OBJ` vagy `GLTF2`‑re, ahogy szükséges.

**Q: Milyen Java verzió szükséges?**  
A: Az Aspose.3D for Java támogatja a Java 8‑at és az azt követő verziókat.

**Q: Lehetséges meglévő FBX‑t betölteni, módosítani az eszközinformációkat, majd újra menteni?**  
A: Teljesen lehetséges. Töltse be a fájlt a `new Scene("input.fbx")`‑val, módosítsa a `scene.getAssetInfo()`‑t, majd mentse el.

---

**Legutóbb frissítve:** 2025-12-06  
**Tesztelve ezzel:** Aspose.3D for Java 24.11  
**Szerző:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}