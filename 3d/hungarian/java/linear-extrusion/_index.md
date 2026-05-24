---
date: 2026-05-24
description: Ismerje meg, hogyan extrudálhat alakzatot az Aspose.3D for Java segítségével.
  Ez a Java 3D modellezési útmutató bemutatja a lineáris extrudálást, a középpont
  vezérlését, az irányt, a szeleteket, a csavarást és még sok mást!
keywords:
- how to extrude shape
- java 3d geometry
- create 3d model java
- create solid from 2d
linktitle: 3D modellek létrehozása lineáris extrudálással Java-ban
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to extrude shape using Aspose.3D for Java. This java 3d modeling
    tutorial covers linear extrusion, center control, direction, slices, twist and
    more!
  headline: How to Extrude Shape - Creating 3D Models with Linear Extrusion in Java
  type: TechArticle
- description: Learn how to extrude shape using Aspose.3D for Java. This java 3d modeling
    tutorial covers linear extrusion, center control, direction, slices, twist and
    more!
  name: How to Extrude Shape - Creating 3D Models with Linear Extrusion in Java
  steps:
  - name: Define the 2‑D profile
    text: Create a `Polygon` or `Polyline` that represents the shape you want to extrude.
      *A `Polygon` represents a closed shape defined by vertices, while a `Polyline`
      is an open series of line segments.* Ready to get started? [Perform Linear Extrusion
      Now](./performing-linear-extrusion/) For a detailed tuto
  - name: Configure extrusion options
    text: 'Set the center, direction, slices, twist, and twist offset on an `Extrusion`
      object. *The `Extrusion` class encapsulates all parameters needed to generate
      a 3‑D mesh from a 2‑D profile.* Get hands‑on with center control: [Control Center
      in Linear Extrusion](./controlling-center/) Read more about cen'
  - name: Add the extrusion to the scene
    text: 'Instantiate a `Scene`, attach the extrusion mesh, and export to your desired
      format. *`Scene` is the container that holds all 3‑D objects and handles exporting
      to various file formats.* Ready to set the direction? [Explore Now](./setting-direction/)
      Learn more about direction: [Setting Direction in '
  - name: Export or render
    text: 'Use `Scene.save()` to write the model to OBJ, STL, or any supported format.
      *`Scene.save()` writes the entire scene to the specified file format, applying
      any necessary post‑processing.* Start specifying slices: [Learn More](./specifying-slices/)
      Detailed guide: [Specifying Slices in Linear Extrusio'
  type: HowTo
- questions:
  - answer: Yes, a valid Aspose license is required for production use, but a free
      trial is available for evaluation.
    question: Can I use Aspose.3D for Java in a commercial project?
  - answer: The library works with Java 8 and newer runtimes, including Java 11, 17,
      and 21.
    question: Which Java versions are supported?
  - answer: Aspose.3D handles mesh generation efficiently, but you can call `scene.dispose()`
      when you’re done with large scenes to free native resources.
    question: Do I need to manage memory for large extrusions?
  - answer: Absolutely – you can create several extrusion objects, position them independently,
      and add them to the same scene.
    question: Can I combine multiple extrusion operations in one model?
  - answer: Yes, the “Applying Twist” and “Using Twist Offset” tutorials demonstrate
      how to set both properties on the same extrusion object.
    question: Is there sample code for applying twist and twist offset together?
  type: FAQPage
second_title: Aspose.3D Java API
title: Alakzat extrudálása – 3D modellek létrehozása lineáris extrudálással Java-ban
url: /hu/java/linear-extrusion/
weight: 23
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hogyan extrudáljunk alakzatot – 3D modellek létrehozása lineáris extrudálással Java-ban

Ha valaha is elgondolkodtál **hogyan extrudáljunk alakzatot** egy Java alkalmazásban, jó helyen vagy. Ebben az útmutatóban végigvezetünk az Aspose.3D for Java lineáris extrudálási funkcióin, megmutatva, hogyan alakíthatsz egyszerű 2‑D profilokat teljes körű 3‑D modellekké. Legyen szó CAD‑stílusú megjelenítő, játékeszköz‑pipeline vagy egyszerű geometriai kísérletezésről, a lineáris extrudálás elsajátítása magabiztosságot ad komplex alakzatok néhány kódsorral történő létrehozásához.

## Gyors válaszok
- **Mi a lineáris extrudálás?** 2‑D vázlat 3‑D szilárd testté alakítása egy irány mentén kinyújtva.  
- **Melyik könyvtár segít?** Az Aspose.3D for Java folyékony API-t biztosít az extrudálási feladatokhoz.  
- **Szükségem van licencre?** Egy ingyenes próba a tanuláshoz elegendő; a kereskedelmi licenc a termeléshez kötelező.  
- **Milyen Java verzió szükséges?** Java 8 vagy újabb.  
- **Alkalmazhatok csavarást vagy eltolást?** Igen – az API natívan támogatja a csavarásszöget és a csavaráseltolást.

## Mi a „how to extrude shape” Java-ban?
Az `Extrusion` művelet az Aspose.3D alapfunkciója, amely egy sík kontúrt térfogatú hálózattá alakít. Egyszerűen fogalmazva, megad egy 2‑D profilt (például egy téglalapot vagy egy egyedi sokszöget), megmondja a motornak, milyen messzire húzza, és a könyvtár elkészíti a 3‑D geometriát.

## Miért használjuk az Aspose.3D for Java-t?
Az Aspose.3D **50+ bemeneti és kimeneti formátumot** támogat – többek között OBJ, STL, FBX és GLTF – és **10 000 csúcsot extrudálásonként** képes generálni anélkül, hogy az egész jelenetet betöltené a memóriába. A keresztplatformos motor Windows, Linux és macOS rendszereken fut, következetes eredményeket biztosítva, akár asztali munkaállomáson, akár fej nélküli CI szerveren.

## Előfeltételek
- Java 8 vagy újabb telepítve a fejlesztői gépén.  
- Maven vagy Gradle a függőségkezeléshez.  
- Aspose.3D for Java licencfájl (opcionális a próba verzióhoz).  

## Hogyan működik a lineáris extrudálás?
A lineáris extrudálás egy 3‑D szilárd testet hoz létre egy 2‑D profil egyenes vonal mentén történő elhúzásával. A motor először háromszögezi a profilt, majd minden szeletnél lemásolja az extrudálási tengely mentén, végül összefűzi a szeleteket, hogy vízzáró hálót alkosson. Ez a folyamat automatikusan kiszámítja a normálvektorokat és az UV koordinátákat, így a végeredményt további geometriai feldolgozás nélkül renderelheti.

## Mik a lineáris extrudálás kulcsparaméterei?
A lineáris extrudálás több paraméterrel testreszabható. A **center** meghatározza a profil forgáspontját az extrudálás előtt. A **direction** vektor beállítja az extrudálási tengelyt, alapértelmezés szerint a pozitív Z‑tengely. A **Slices** szabályozza, hogy hány köztes keresztmetszet jön létre, befolyásolva a csavart vagy kúpos alakzatok simaságát. A **Twist angle** fokozatosan elforgatja a profilt az elejétől a végéig, míg a **twist offset** lineáris eltolást ad a tengely mentén, spirálformákat lehetővé téve.

- **Center** – A profil elhelyezésének forgáspontja az extrudálás előtt.  
- **Direction** – Egy vektor, amely meghatározza az extrudálási tengelyt; alapértelmezett a pozitív Z‑tengely.  
- **Slices** – A köztes keresztmetszetek száma; több szelet simább átmenetet eredményez csavart vagy kúpos extrudálásoknál.  
- **Twist Angle** – A profilra az elejétől a végéig alkalmazott teljes forgatás fokban kifejezve.  
- **Twist Offset** – Lineáris eltolás, amely a profilt az extrudálási tengely mentén mozgatja csavarással együtt, spirál alakzatokat hozva létre.

## Lineáris extrudálás végrehajtása az Aspose.3D for Java-ban

Töltse be a profilját, állítsa be a paramétereket, és hagyja, hogy az API generálja a hálót. A következő lépések vázolják a tipikus munkafolyamatot.

### 1. lépés: A 2‑D profil meghatározása
Hozzon létre egy `Polygon` vagy `Polyline` objektumot, amely az extrudálni kívánt alakzatot ábrázolja.  
*A `Polygon` egy csúcsok által meghatározott zárt alakzat, míg a `Polyline` nyílt vonalszakaszok sorozata.*  
Készen áll a kezdésre? [Végezze el a lineáris extrudálást most](./performing-linear-extrusion/)  
Részletes útmutató: [Lineáris extrudálás végrehajtása az Aspose.3D for Java-ban](./performing-linear-extrusion/).

### 2. lépés: Extrudálási beállítások konfigurálása
Állítsa be a középpontot, irányt, szeleteket, csavarást és csavaráseltolást egy `Extrusion` objektumon.  
*A `Extrusion` osztály tartalmazza az összes paramétert, amely a 2‑D profilból 3‑D háló generálásához szükséges.*  
Gyakorlati középpont vezérlése: [Középpont vezérlése lineáris extrudálásban](./controlling-center/)  
További információ a középpont vezérlésről: [Középpont vezérlése lineáris extrudálásban az Aspose.3D for Java-val](./controlling-center/)

### 3. lépés: Extrudálás hozzáadása a jelenethez
Hozzon létre egy `Scene` példányt, csatolja az extrudálási hálót, és exportálja a kívánt formátumba.  
*`Scene` a konténer, amely az összes 3‑D objektumot tartalmazza és kezeli a különböző fájlformátumokba való exportálást.*  
Készen áll az irány beállítására? [Fedezze fel most](./setting-direction/)  
További információ az irányról: [Irány beállítása lineáris extrudálásban az Aspose.3D for Java-val](./setting-direction/)

### 4. lépés: Exportálás vagy renderelés
Használja a `Scene.save()` metódust a modell OBJ, STL vagy bármely támogatott formátumba írásához.  
*`Scene.save()` a teljes jelenetet a megadott fájlformátumba írja, szükség esetén post‑processzálást alkalmazva.*  
Kezdje el a szeletek megadását: [További információ](./specifying-slices/)  
Részletes útmutató: [Szeletek megadása lineáris extrudálásban az Aspose.3D for Java-val](./specifying-slices/)

## Hogyan alkalmazzunk csavarást egy extrudálásra?
Alkalmazzon csavarást a `twistAngle` tulajdonság beállításával az extrudálási beállításokban. A motor minden szeletet arányosan elforgat, spirálhatást hozva létre. A szög módosításával bármit előállíthat a finom torzítástól a teljes 360°-os spirálokig, ami díszítő elemekhez vagy funkcionális rugókhoz hasznos.  
Készen áll a csavaráshoz? [Alkalmazzon csavarást most](./applying-twist/)  
Teljes példa: [Csavarással való extrudálás lineáris extrudálásban az Aspose.3D for Java-val](./applying-twist/)

## Hogyan használjuk a csavaráseltolást spirál alakzatokhoz?
A csavaráseltolás minden szeletet az extrudálási tengely mentén mozgat elfordulás közben, spirál lépcsőt vagy csavarhúzó geometriát hozva létre. A csavarásszög pozitív eltolással kombinálva sima spirál emelkedőt eredményez, míg negatív eltolás csökkenő spirálokat hozhat létre. Ez a technika ideális menetek, rugók vagy művészi szalagok modellezéséhez.  
Fejlessze képességeit: [Ismerje meg a csavaráseltolást](./using-twist-offset/)  
Átfogó útmutató: [Csavaráseltolás használata lineáris extrudálásban az Aspose.3D for Java-val](./using-twist-offset/)

## Gyakori felhasználási esetek lineáris extrudáláshoz
- **Mechanikai alkatrészek** – Gyorsan generáljon csavarokat, tengelyeket és konzolokat egyszerű vázlatokból.  
- **Építészeti elemek** – Emelje ki a alaprajzokat falakká vagy oszlopokká BIM prototípusokhoz.  
- **Játékelemek** – Hozzon létre low‑poly tárgyakat, például kerítéseket, csöveket vagy díszítő sínek közvetlenül 2‑D művészeti anyagból.  
- **Oktatási eszközök** – Vizualizálja a matematikai felületeket paraméteres görbék extrudálásával.

## Gyakori problémák hibaelhárítása
- **Hiányzó felületek** – Győződjön meg róla, hogy a profil zárt hurkú; a nyitott kontúrok hézagokat eredményeznek.  
- **Túlzott memóriahasználat** – Csökkentse a `slices` számát vagy engedélyezze a `scene.setMemoryOptimization(true)` beállítást.  
- **Helytelen csavarásszög irány** – A pozitív szögek az extrudálási irány mentén nézve óramutató járásával megegyező irányba forgatnak; negatív értékekkel fordítható meg.

## Gyakran feltett kérdések

**Q: Használhatom az Aspose.3D for Java-t kereskedelmi projektben?**  
A: Igen, a termeléshez érvényes Aspose licenc szükséges, de az értékeléshez ingyenes próba elérhető.

**Q: Mely Java verziók támogatottak?**  
A: A könyvtár Java 8 és újabb futtatókörnyezetekkel működik, beleértve a Java 11, 17 és 21 verziókat.

**Q: Szükséges a memória kezelése nagy extrudálásoknál?**  
A: Az Aspose.3D hatékonyan kezeli a háló generálást, de nagy jelenetek után meghívhatja a `scene.dispose()`-t a natív erőforrások felszabadításához.

**Q: Kombinálhatok több extrudálási műveletet egy modellben?**  
A: Természetesen – létrehozhat több extrudálási objektumot, önállóan pozicionálhatja őket, és hozzáadhatja ugyanahhoz a jelenethez.

**Q: Van minta kód a csavaráss és csavaráseltolás együttes alkalmazására?**  
A: Igen, a „Csavarással való extrudálás” és a „Csavaráseltolás használata” útmutatók bemutatják, hogyan állítható be mindkét tulajdonság ugyanazon extrudálási objektumon.

**Utoljára frissítve:** 2026-05-24  
**Tesztelve a következővel:** Aspose.3D for Java 24.11  
**Szerző:** Aspose  

{{< blocks/products/products-backtop-button >}}

## Kapcsolódó útmutatók

- [Java 3D grafikai útmutató – Középpont lineáris extrudálásban](/3d/java/linear-extrusion/controlling-center/)
- [Hogyan állítsuk be az irányt lineáris extrudálásban az Aspose.3D for Java-val](/3d/java/linear-extrusion/setting-direction/)
- [3D extrudálás létrehozása szeletekkel – Aspose.3D for Java](/3d/java/linear-extrusion/specifying-slices/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}