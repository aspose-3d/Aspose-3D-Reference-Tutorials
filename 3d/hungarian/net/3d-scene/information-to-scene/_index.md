---
date: 2026-01-12
description: Ismerje meg, hogyan adhat hozzá metaadatokat 3D jelenetekhez az Aspose.3D
  for .NET használatával, beleértve a gyártói információk hozzáadását és a 3D modellfájlok
  exportálását.
linktitle: 'How to Add Metadata: Extracting Information to Scene Assets'
second_title: Aspose.3D .NET API
title: 'Metaadatok hozzáadása: Információk kinyerése a jelenet eszközeibe'
url: /hu/net/3d-scene/information-to-scene/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hogyan adjunk hozzá metaadatokat: Információk kinyerése a jelenet eszközökbe

## Bevezetés

Ebben az átfogó oktatóanyagban megtudja, **hogyan adjon hozzá metaadatokat** a 3D jeleneteihez az Aspose.3D for .NET segítségével. A metaadatok hozzáadása, például a gyártó adatai, egyedi mérőegységek és egyéb eszközinformációk, informatívabbá, kereshetőbbé és készen állóvá teszi modelljeit az olyan downstream csővezetékekhez, mint a játék motorok vagy az AR/VR platformok.

## Gyors válaszok
- **Mi a fő cél?** Metaadatok (gyártói információk, egységek, egyedi címkék) beágyazása közvetlenül egy 3D jelenetbe.  
- **Melyik könyvtárat használja?** Aspose.3D for .NET.  
- **Exportálhatom a modellt a metaadatok hozzáadása után?** Igen – **exportálhat 3D modell** fájlokat, például menthet FBX formátumba.  
- **Szükségem van licencre?** Elérhető ingyenes próba; a kereskedelmi licenc szükséges a termeléshez.  
- **Mely .NET verziók támogatottak?** .NET Framework 4.5+, .NET Core 3.1+, .NET 5/6.

## Mi az a „hogyan adjunk hozzá metaadatokat” egy 3D jelenetben?

A metaadatok hozzáadása azt jelenti, hogy leíró információkat—például az alkalmazás nevét, a gyártót, a mérőegységeket vagy egyedi címkéket—csatolunk magához a jelenet fájlhoz. Ezek az adatok a modellel együtt utaznak, amikor **menti a jelenetet FBX‑ként** vagy más támogatott formátumban, lehetővé téve a downstream eszközök számára, hogy a kontextust külső fájlok nélkül értsék.

## Miért ágyazzunk be egyedi metaadatokat és gyártói információkat?

- **Kereshetőség:** Az eszközkezelő rendszerek szűrhetik a modelleket gyártó vagy egységtípus szerint.  
- **Interoperabilitás:** Az FBX‑et olvasó motorok automatikusan alkalmazhatják a helyes méretarányt, ha **meghatározza a mérőegységeket**.  
- **Márkaépítés:** Az alkalmazás nevének és a gyártónak a feltüntetése erősíti a tulajdonjogot és a licencmegfelelőséget.  

## Előkövetelmények

Mielőtt belemerülnénk, győződjön meg róla, hogy:

- Az Aspose.3D for .NET telepítve van. Letöltheti a [Aspose.3D for .NET oldalról](https://releases.aspose.com/3d/net/).

## Névterek importálása

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## 1. lépés: 3D jelenet inicializálása

```csharp
Scene scene = new Scene();
```

Hozzon létre egy új `Scene` objektumot, amely az összes geometriai és eszközinformációt tárolja.

## 2. lépés: Alkalmazás beállítása és **Gyártói információk hozzáadása**

```csharp
scene.AssetInfo.ApplicationName = "Egypt";
scene.AssetInfo.ApplicationVendor = "Manualdesk";
```

Itt ágyazzuk be a **alkalmazás nevét** és a **gyártói információkat**. Ez a **hogyan adjunk hozzá metaadatokat** alapvető része, amely azonosítja a modell forrását.

## 3. lépés: **Mérőegységek meghatározása** a pontos méretezéshez

```csharp
scene.AssetInfo.UnitName = "pole";
scene.AssetInfo.UnitScaleFactor = 0.6;
```

A `UnitName` és `UnitScaleFactor` megadásával azt mondja a downstream eszközöknek, hogy egy „oszlop” 0,6 méternek (60 cm) felel meg. Ez a lépés elengedhetetlen, amikor később **exportál 3D modell** fájlokat, hogy biztosítsa a helyes valós méreteket.

## 4. lépés: **Jelenet mentése FBX‑ként** – **Exportálja a 3D modellt** metaadatokkal

```csharp
var output = "Your Output Directory" + "InformationToScene.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

A `Save` hívás a jelenetet egy FBX fájlba írja, beágyazva az összes hozzáadott metaadatot. Ez bemutatja, hogyan **adjunk hozzá metaadatokat**, majd **mentse a jelenetet FBX‑ként**, hatékonyan **exportálva a 3D modellt** a teljes eszközinformációval.

## 5. lépés: Sikerüzenet megjelenítése

```csharp
Console.WriteLine("\nAsset information added successfully to Scene.\nFile saved at " + output);
```

Egy barátságos konzolos üzenet megerősíti, hogy a metaadatok kiírásra kerültek és megjelenik a fájl helye.

## Gyakori problémák és tippek

- **Helytelen egységarány:** Ellenőrizze duplán, hogy a `UnitScaleFactor` megfelel-e a valós konverziónak; ellenkező esetben az exportált modellek túl nagyok vagy túl kicsik lehetnek.  
- **Hiányzó gyártói információ:** Ha az `ApplicationVendor` üres, egyes megjelenítők „Ismeretlen” értéket mutatnak. Mindig állítsa be, ha lehetséges.  
- **Fájlútvonal hibák:** Győződjön meg róla, hogy a kimeneti könyvtár létezik; ellenkező esetben a `scene.Save` kivételt dob.

## Gyakran ismételt kérdések

### Q1: Használhatom az Aspose.3D for .NET-et más programozási nyelvekkel?

A1: Az Aspose.3D elsősorban .NET nyelveket támogat, de más nyelvekhez is felfedezhet interoperabilitási lehetőségeket.

### Q2: Elérhető ingyenes próba az Aspose.3D for .NET-hez?

A2: Igen, az ingyenes próbát [itt](https://releases.aspose.com/) érheti el.

### Q3: Hogyan kaphatok támogatást az Aspose.3D‑hez kapcsolódó kérdésekhez?

A3: Látogassa meg az [Aspose.3D fórumot](https://forum.aspose.com/c/3d/18) a közösségi és támogatási információkért.

### Q4: Vásárolhatok ideiglenes licencet az Aspose.3D for .NET-hez?

A4: Igen, ideiglenes licencet szerezhet [itt](https://purchase.aspose.com/temporary-license/).

### Q5: Hol találok részletes dokumentációt az Aspose.3D for .NET-hez?

A5: Tekintse meg a [dokumentációt](https://reference.aspose.com/3d/net/) a részletes információkért.

## Összegzés

Most már elsajátította, hogyan **adjunk hozzá metaadatokat** egy 3D jelenethez az Aspose.3D for .NET segítségével – az alkalmazás és a gyártó részleteinek beállításával, a **mérőegységek meghatározásával**, és végül a **jelenet FBX‑ként mentésével**, hogy **exportálja a 3D modell** fájlokat, amelyek minden értékes információt magukban hordoznak. Használja ezeket a technikákat, hogy eszközei gazdagabbak, kereshetőbbek legyenek, és készen álljanak bármilyen downstream munkafolyamatra.

---

**Last Updated:** 2026-01-12  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}