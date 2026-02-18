---
date: 2026-02-12
description: Tanulja meg, hogyan exportálhatja a jelenetet FBX formátumba, és hogyan
  szerezhet be 3D jelenetinformációkat az Aspose.3D for Java segítségével. Ez a lépésről‑lépésre
  útmutató bemutatja az alkalmazás nevének beállítását, a mértékegységek meghatározását
  és a jelenet FBX‑be exportálását.
linktitle: How to Save FBX and Retrieve 3D Scene Info in Java
second_title: Aspose.3D Java API
title: Hogyan exportáljunk egy jelenetet FBX-be, és hogyan nyerjünk ki 3D-s jelenetinformációkat
  Java-ban
url: /hu/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hogyan exportáljunk jelenetet FBX-be, és nyerjünk ki 3D jelenet információkat Java-ban

## Bevezetés

Ha egy világos, gyakorlati útmutatót keresel arra, **hogyan exportáljunk jelenetet FBX-be**, miközben hasznos metaadatokat nyersz ki a 3D jeleneteidből, jó helyen jársz. Ebben az útmutatóban lépésről‑lépésre végigvezetünk a **Aspose.3D Java** könyvtár használatával: a jelenet létrehozásától, **az alkalmazás nevének beállításáig**, **a mértékegységek meghatározásáig**, egészen a **jelenet FBX‑be exportálásáig**. A végére egy használatra kész FBX‑fájlt kapsz, amely tartalmazza a szükséges eszközinformációkat a további feldolgozási csővezetékekhez.

## Gyors válaszok
- **Mi a fő cél?** Egy olyan jelenet exportálása FBX‑be, amely egyedi eszközinformációkat tartalmaz.  
- **Melyik könyvtárat használjuk?** Aspose.3D for Java.  
- **Szükségem van licencre?** Fejlesztéshez egy ingyenes próba elegendő; termeléshez kereskedelmi licenc szükséges.  
- **Módosíthatom a mértékegységeket?** Igen – használd a `setUnitName` és `setUnitScaleFactor` metódusokat.  
- **Hol kerül mentésre a kimenet?** A `scene.save(...)`‑ben megadott útvonalra.

## Előfeltételek

Mielőtt elkezdenénk, győződj meg róla, hogy rendelkezel:

- Alapos ismeretekkel a Java alap szintaxisáról.  
- **Aspose.3D for Java** letöltve és a projektedhez hozzáadva (letöltheted a hivatalos) [Aspose 3D letöltési oldalról](https://releases.aspose.com/3d/java/).  
- Kedvenc Java IDE‑ddel (IntelliJ IDEA, Eclipse, NetBeans, stb.) megfelelően konfigurálva.

## Csomagok importálása

A Java forrásfájlodban importáld az Aspose.3D osztályokat, amelyek a jelenetkezelést és a fájlformátum‑támogatást biztosítják.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Pro tipp:** Tartsd a importlistát minimálisra, hogy elkerüld a felesleges függőségeket és javítsd a fordítási időt.

## Mi a folyamat egy FBX‑fájl mentéséhez?

Az alábbiakban egy tömör, lépésről‑lépésre útmutatót találsz, amely megmutatja, **hogyan adjunk hozzá eszközinformációkat** egy jelenethez, majd **exportáljuk a jelenetet FBX‑be**.

### 1. lépés: 3D jelenet inicializálása

Először hozz létre egy üres `Scene` objektumot. Ez lesz a tároló minden geometria, fény, kamera és eszközmetaadat számára.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### 2. lépés: Alkalmazás‑ és gyártói információk beállítása

Egyedi metaadatok hozzáadása segíti a downstream eszközöket a fájl forrásának azonosításában. Itt **beállítjuk az alkalmazás nevét** és a gyártót az `AssetInfo` objektummal.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Miért fontos:** Sok csővezeték szűri vagy címkézi az eszközöket a származó alkalmazás alapján, így ez a lépés elengedhetetlen nagy projektek esetén.

### 3. lépés: Mértékegységek meghatározása

Az Aspose.3D lehetővé teszi, hogy megadd a jeleneted által használt egységrendszert. Ebben a példában egy ókori egyiptomi „pole” egységet használunk egy egyedi skálafaktorral.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Tipp:** Állítsd a `unitScaleFactor`‑t a modellek valós méretéhez; az 1.0 egy 1‑to‑1 leképezést jelent a választott egységgel.

### 4. lépés: Jelenet exportálása FBX‑be

Miután az eszközinformációk csatolva lettek, mentjük a jelenetet FBX‑fájlként. A `FileFormat.FBX7500ASCII` opció ember‑olvasható ASCII FBX‑et hoz létre, ami hibakereséskor hasznos.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddAssetInformationToScene
```

> **Ne feledd:** Cseréld le a `"Your Document Directory"`‑t egy abszolút útvonalra vagy a projekt munkakönyvtárához relatív útvonalra.

### 5. lépés: Sikerüzenet kiírása

Egy egyszerű konzolüzenet megerősíti, hogy a művelet sikeres volt, és megadja, hová íródott a fájl.

```java
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
```

## Miért exportáljunk jelenetet FBX‑be az Aspose.3D‑val?

Az FBX‑be exportálás gyakori követelmény, mivel az FBX széles körben támogatott játékmotorok, DCC‑eszközök és AR/VR csővezetékek által. Az Aspose.3D teljes kontrollt ad az exportált fájl felett – metaadatok, egységek és geometria – anélkül, hogy nehéz 3D‑szerkesztő alkalmazásra lenne szükség. Ez gyors és megbízható automatizált eszközgenerálást, kötegelt feldolgozást és szerver‑oldali konverziókat tesz lehetővé.

## Gyakori felhasználási esetek

- **Játékeszköz‑csővezetékek** – a készítő információinak beágyazása közvetlenül az FBX‑fájlokba a verziókövetéshez.  
- **Építészeti vizualizáció** – projektspecifikus egységek tárolása a méretezési hibák elkerülése érdekében a renderelő motorokba való importáláskor.  
- **Automatizált jelentéskészítés** – FBX‑fájlok generálása futás közben metaadatokkal, amelyeket a downstream analitikai eszközök olvasni tudnak.  
- **Felhőalapú 3D szolgáltatások** – programozottan jelenetek létrehozása és exportálása GUI nélkül, tökéletes SaaS platformokhoz.

## Hibaelhárítás és tippek

| Probléma | Megoldás |
|----------|----------|
| **A fájl nem található a mentés után** | Ellenőrizd, hogy a `MyDir` egy létező mappára mutat-e, és hogy az alkalmazásnak van‑e írási joga. |
| **Az egységek helytelenül jelennek meg külső nézőben** | Ellenőrizd a `unitScaleFactor`‑t; egyes nézők az alapegységként a métert várják. |
| **Az eszközmetaadat hiányzik** | Győződj meg róla, hogy a `scene.getAssetInfo()`‑t **a mentés előtt** hívod; a `save()` után végzett módosítások nem kerülnek mentésre. |
| **Teljesítménybottleneck nagy jeleneteknél** | Használd a `scene.optimize()`‑t a mentés előtt a memóriahasználat csökkentéséhez. |
| **Az ASCII FBX túl nagy** | Válts bináris FBX‑re a `FileFormat.FBX7500` használatával (lásd a GYIK‑ot). |

## Gyakran feltett kérdések

**K: Hogyan változtathatom meg a kimeneti formátumot bináris FBX‑re?**  
V: Cseréld le a `FileFormat.FBX7500ASCII`‑t `FileFormat.FBX7500`‑ra a `scene.save(...)` hívásakor.

**K: Hozzáadhatok egyedi felhasználó‑definiált metaadatokat a beépített eszközmezőkön kívül?**  
V: Igen, használhatod a `scene.getUserData().add("Key", "Value")`‑t további kulcs‑érték párok beágyazásához.

**K: Támogatja az Aspose.3D más exportformátumokat, például OBJ vagy GLTF?**  
V: Igen. Egyszerűen változtasd meg a `FileFormat` enumot `OBJ`‑ra vagy `GLTF2`‑re, ahogy szükséges.

**K: Milyen Java verzió szükséges?**  
V: Az Aspose.3D for Java támogatja a Java 8‑at és az azt követő verziókat.

**K: Lehetséges meglévő FBX‑et betölteni, módosítani az eszközinformációkat, majd újra menteni?**  
V: Természetesen. Töltsd be a fájlt a `new Scene("input.fbx")`‑val, módosítsd a `scene.getAssetInfo()`‑t, majd mentsd el.

## Összegzés

Most már egy komplett, termelés‑kész munkafolyamatod van a **jelenet FBX‑be exportálásához**, miközben értékes eszközinformációkat ágyazol be, mint például az alkalmazás neve, a gyártó és egyedi mértékegységek. Ez a megközelítés egyszerűsíti az eszközkezelést, csökkenti a kézi adminisztrációt, és biztosítja, hogy a downstream eszközök megkapják a szükséges kontextust. Nyugodtan fedezz fel más exportformátumokat, adj hozzá egyedi felhasználói adatokat, vagy integráld ezt a kódot nagyobb automatizálási csővezetékekbe.

---

**Utoljára frissítve:** 2026-02-12  
**Tesztelve:** Aspose.3D for Java 24.11  
**Szerző:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}