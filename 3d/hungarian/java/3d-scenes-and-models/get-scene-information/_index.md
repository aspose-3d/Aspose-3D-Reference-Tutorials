---
date: 2026-09-08
description: Ismerje meg, hogyan definiálhatja a mértékegységeket és exportálhat egy
  jelenetet FBX-be Java használatával az Aspose.3D segítségével. Ez a lépésről‑lépésre
  útmutató bemutatja az alkalmazás nevének beállítását, a mérési egységek megadását
  és a 3D-s jelenet információinak lekérdezését.
keywords:
- how to define units
- export scene to fbx
- how to set application name
- define measurement units
lastmod: 2026-09-08
linktitle: Hogyan mentse el az FBX-et és kérdezze le a 3D-s jelenet információit Java-ban
og_description: Ismerje meg, hogyan definiálhatja a mértékegységeket és exportálhat
  egy jelenetet FBX-be Java-ban az Aspose.3D segítségével. Az útmutató néhány lépésben
  bemutatja az alkalmazás nevének beállítását, a mérési egységek megadását és a 3D-s
  jelenet információinak lekérdezését.
og_image_alt: Guide showing how to define units and export a 3D scene to FBX using
  Aspose.3D Java
og_title: Hogyan definiáljuk a mértékegységeket és exportáljuk a jelenetet FBX-be
  Java-ban
schemas:
- author: Aspose
  dateModified: '2026-09-08'
  description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  headline: How to define units and export scene to FBX in Java
  type: TechArticle
- description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  name: How to define units and export scene to FBX in Java
  steps:
  - name: initialize a 3D scene
    text: The `Scene` class is Aspose.3D's top‑level container that represents an
      entire 3D scene, including geometry, lights, cameras, and metadata. First, create
      an empty `Scene` object. This will be the container for all geometry, lights,
      cameras, and asset metadata.
  - name: define measurement units
    text: The unit system determines the real‑world scale of the scene; Aspose.3D
      lets you specify a unit name and a scale factor relative to meters. In this
      example we use an ancient Egyptian unit called “pole” with a custom scale factor.
      > **Tip:** Adjust `unitScaleFactor` to match the real‑world size of yo
  - name: export scene to FBX
    text: Now that the asset information is attached, we save the scene as an FBX
      file. The `FileFormat.FBX7500ASCII` option produces a human‑readable ASCII FBX,
      which is handy for debugging. > **Remember:** Replace `"Your Document Directory"`
      with an absolute path or a path relative to your project's working
  type: HowTo
- questions:
  - answer: Replace `FileFormat.FBX7500ASCII` with `FileFormat.FBX7500` when calling
      `scene.save(...)`.
    question: How do I change the output format to binary FBX?
  - answer: Yes, use `scene.getUserData().add("Key", "Value")` to embed additional
      key‑value pairs.
    question: Can I add custom user‑defined metadata beyond the built‑in asset fields?
  - answer: It does. Simply change the `FileFormat` enum to `OBJ` or `GLTF2` as needed.
    question: Does Aspose.3D support other export formats like OBJ or GLTF?
  - answer: Aspose.3D for Java supports Java 8 and later.
    question: What version of Java is required?
  - answer: Absolutely. Load the file with `new Scene("input.fbx")`, modify `scene.getAssetInfo()`,
      then save.
    question: Is it possible to load an existing FBX, modify its asset info, and resave?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- export scene to fbx
- Aspose.3D
- Java 3D
- define units
- 3D asset metadata
title: Hogyan definiáljuk a mértékegységeket és exportáljuk a jelenetet FBX-be Java-ban
url: /hu/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hogyan definiáljunk egységeket és exportáljunk jelenetet FBX-be Java-ban

## Bevezetés

Ha egy világos, gyakorlati útmutatót keresel arra, **hogyan definiáljunk egységeket** és **exportáljunk egy jelenetet FBX-be**, miközben hasznos metaadatokat nyersz ki a 3D jeleneteidből, jó helyen jársz. Ebben az oktatóanyagban lépésről lépésre végigvezetünk a **Aspose.3D for Java** könyvtár használatával: egy jelenet létrehozásától, **az alkalmazás nevének beállítása**, **mérőegységek definiálása**, egészen a **jelenet exportálása FBX-be**-ig. A végére egy használatra kész FBX fájlt kapsz, amely tartalmazza a szükséges asset információkat a downstream folyamatokhoz.

## Gyors válaszok
- **Mi a fő cél?** Exportálj egy jelenetet FBX-be, amely egyedi asset információkat tartalmaz.  
- **Melyik könyvtár van használatban?** Aspose.3D for Java.  
- **Szükségem van licencre?** Egy ingyenes próba működik fejlesztéshez; egy kereskedelmi licenc szükséges a termeléshez.  
- **Módosíthatom a mérőegységeket?** Igen – használd a `setUnitName` és `setUnitScaleFactor` metódusokat.  
- **Hol kerül mentésre a kimenet?** A `scene.save(...)`‑ben megadott útvonalra.  

## Előkövetelmények

Mielőtt elkezdenénk, győződj meg róla, hogy rendelkezel:

- Alapos ismeretek a Java alapszintű szintaxisáról.  
- **Aspose.3D for Java** letöltve és hozzáadva a projektedhez (letöltheted a hivatalos) [Aspose 3D letöltési oldal](https://releases.aspose.com/3d/java/).  
- A kedvenc Java IDE-d (IntelliJ IDEA, Eclipse, NetBeans, stb.) megfelelően konfigurálva.

## Csomagok importálása

A Java forrásfájlodban importáld az Aspose.3D osztályokat, amelyek a jelenetkezelést és a fájlformátum támogatást biztosítják.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Pro tipp:** Tartsd minimálisra az import listát, hogy elkerüld a felesleges függőségeket és javítsd a fordítási időt.

## Mi a folyamat egy FBX fájl mentéséhez?

Egy jelenet FBX fájlként való mentéséhez létrehozol egy `Scene`‑t, beállítod a kívánt asset metaadatokat, definiálod a mérőegységet, majd meghívod a `scene.save(path, FileFormat.FBX7500ASCII)`‑t. Ez a sorozat geometriai adatokat, anyagokat és metaadatokat ír egy ASCII FBX‑be, amelyet a downstream eszközök megtekinthetnek vagy importálhatnak.

### 1. lépés: 3D jelenet inicializálása

A `Scene` osztály az Aspose.3D legfelső szintű tárolója, amely egy teljes 3D jelenetet képvisel, beleértve a geometriát, fényeket, kamerákat és metaadatokat. Először hozz létre egy üres `Scene` objektumot. Ez lesz a tároló minden geometria, fény, kamera és asset metaadat számára.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Hogyan állítsuk be az alkalmazás nevét Java-ban

Az `AssetInfo` objektum metaadatokat tárol, mint például az alkalmazás neve, a gyártó és a verzió a jelenethez. Egyedi metaadatok hozzáadása segíti a downstream eszközöket a fájl forrásának azonosításában. Használd az `AssetInfo` objektumot az **alkalmazás nevének beállításához** (és a gyártóhoz), mielőtt mentenéd a fájlt.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Miért fontos:** Sok pipeline szűri vagy címkézi az asseteket a forrásalkalmazás alapján, így ez a lépés elengedhetetlen nagy projektek esetén.

### 3. lépés: mérőegységek definiálása

Az egységrendszer határozza meg a jelenet valós méretarányát; az Aspose.3D lehetővé teszi egy egységnév és egy méterhez viszonyított skálafaktor megadását. Ebben a példában egy ókori egyiptomi „pole” egységet használunk egy egyedi skálafaktorral.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Tipp:** Állítsd be a `unitScaleFactor`‑t a modelljeid valós méretéhez; az 1.0 egy 1‑az‑1‑es leképezést jelent a kiválasztott egységgel.

### 4. lépés: jelenet exportálása FBX-be

Miután az asset információk csatolva lettek, mentjük a jelenetet FBX fájlként. A `FileFormat.FBX7500ASCII` opció egy ember által olvasható ASCII FBX‑t hoz létre, ami hasznos a hibakereséshez.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
// ExEnd:AddAssetInformationToScene
```

> **Ne feledd:** Cseréld le a `"Your Document Directory"`‑t egy abszolút útvonalra vagy a projekted munkakönyvtárához relatív útvonalra.

## Miért exportáljunk jelenetet FBX-be az Aspose.3D-val?

Az Aspose.3D **50+ bemeneti és kimeneti formátumot** támogat, és képes több száz oldalas jeleneteket feldolgozni anélkül, hogy a teljes fájlt a memóriába töltené, így teljes kontrollt biztosít az exportált fájl felett – metaadatok, egységek és geometria – anélkül, hogy nehéz 3D szerkesztő alkalmazásra lenne szükség. Ez a automatizált asset generálást, kötegelt feldolgozást és szerver‑oldali konverziókat gyorsá és megbízhatóvá teszi.

## Gyakori felhasználási esetek

- **Játék asset pipeline‑ok** – ágyazz be a készítő információkat közvetlenül az FBX fájlokba a verziókövetéshez.  
- **Építészeti vizualizáció** – tárold a projektspecifikus egységeket, hogy elkerüld a méretezési hibákat a renderelő motorokba importáláskor.  
- **Automatizált jelentéskészítés** – generálj FBX fájlokat menet közben metaadatokkal, amelyeket a downstream analitikai eszközök olvashatnak.  
- **Felhőalapú 3D szolgáltatások** – programozottan hozz létre és exportálj jeleneteket GUI nélkül, tökéletes SaaS platformokhoz.  

## Hibaelhárítás és tippek

| Probléma | Megoldás |
|----------|----------|
| **A mentés után a fájl nem található** | Ellenőrizd, hogy a `MyDir` egy létező mappára mutat-e, és hogy az alkalmazásodnak van-e írási jogosultsága. |
| **Az egységek helytelennek jelennek meg külső nézőben** | Ellenőrizd újra a `unitScaleFactor`‑t; egyes nézők a métert alapegységként várják. |
| **Az asset metaadatok hiányoznak** | Győződj meg róla, hogy a `scene.getAssetInfo()`‑t **mentés előtt** hívod; a `save()` után végzett módosítások nem lesznek mentve. |
| **Teljesítménybottleneck nagy jeleneteknél** | Használd a `scene.optimize()`‑t mentés előtt a memóriahasználat csökkentéséhez. |
| **Az ASCII FBX túl nagy** | Válts bináris FBX-re a `FileFormat.FBX7500` használatával (lásd a GYIK‑ot). |

## Gyakran feltett kérdések

**K: Hogyan változtathatom meg a kimeneti formátumot bináris FBX-re?**  
V: Cseréld le a `FileFormat.FBX7500ASCII`‑t `FileFormat.FBX7500`‑ra a `scene.save(...)` hívásakor.

**K: Hozzáadhatok egyedi felhasználó‑definiált metaadatokat a beépített asset mezőkön kívül?**  
V: Igen, használd a `scene.getUserData().add("Key", "Value")`‑t további kulcs‑érték párok beágyazásához.

**K: Támogatja az Aspose.3D más export formátumokat, például OBJ vagy GLTF?**  
V: Igen. Egyszerűen változtasd meg a `FileFormat` enumot `OBJ` vagy `GLTF2` értékre, ahogy szükséges.

**K: Milyen Java verzió szükséges?**  
V: Az Aspose.3D for Java támogatja a Java 8‑at és újabb verziókat.

**K: Lehet meglévő FBX‑t betölteni, módosítani az asset információkat, majd újra menteni?**  
V: Természetesen. Töltsd be a fájlt a `new Scene("input.fbx")`‑val, módosítsd a `scene.getAssetInfo()`‑t, majd mentsd.

---

**Utolsó frissítés:** 2026-09-08  
**Tesztelve a következővel:** Aspose.3D for Java 24.11  
**Szerző:** Aspose

## Kapcsolódó oktatóanyagok

- [3D fájlméret csökkentése – Jelenetek tömörítése az Aspose.3D for Java-val](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [Hogyan állítsuk be a vector3 színt Java-ban: Diffúz szín módosítása és 3D tulajdonságok kezelése Java jelenetekben az Aspose.3D használatával](/3d/java/3d-scenes-and-models/managing-3d-properties-scenes/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}