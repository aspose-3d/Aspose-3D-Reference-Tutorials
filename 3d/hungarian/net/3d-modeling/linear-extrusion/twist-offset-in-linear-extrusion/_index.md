---
date: 2026-03-23
description: Tanulja meg, hogyan adhat hozzá csavart a lineáris extrúzióhoz az Aspose.3D
  for .NET segítségével, és fedezze fel, hogyan használhatja az extrúziót ASP.NET
  3D modellezési projektekhez.
linktitle: Twist Offset in Linear Extrusion
second_title: Aspose.3D .NET API
title: Hogyan adhatunk csavart a lineáris extrúzióhoz az Aspose.3D for .NET segítségével
url: /hu/net/3d-modeling/linear-extrusion/twist-offset-in-linear-extrusion/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hogyan adjunk csavart elfordulást lineáris extrudáláshoz az Aspose.3D for .NET segítségével

## Bevezetés

Ha egyértelmű, lépésről‑lépésre útmutatót keresel arra, **hogyan adjunk csavart elfordulást** egy lineáris extrudáláshoz, jó helyen jársz. Ebben a bemutatóban végigvezetünk a teljes folyamaton az Aspose.3D for .NET használatával, megmutatva, **hogyan használjuk az extrudálást** dinamikus 3D alakzatok létrehozásához, amelyek tökéletesek *asp.net 3d modellezés* szcenáriókhoz. A végére egy kész, futtatható példát kapsz, amely bemutatja a csavart eltolást, szeleteket, és a végeredmény OBJ fájlba mentését.

## Gyors válaszok
- **Mit csinál a „twist offset”?** Az elfordulás kiindulópontját eltolja az extrudálás tengelye mentén.  
- **Szükségem van licencre a minta futtatásához?** Ideiglenes licenc teszteléshez elegendő; a teljes licenc a termeléshez kötelező.  
- **Mely .NET verziók támogatottak?** .NET Framework 4.5+, .NET Core 3.1+, .NET 5/6+.  
- **Megváltoztathatom a szeletek számát?** Igen — állítsd be a `Slices` tulajdonságot a háló simaságának szabályozásához.  
- **Az output formátum csak OBJ lehet?** Nem, az Aspose.3D számos formátumot támogat; az OBJ itt egyszerűség kedvéért van használva.

## Mi az a Twist Offset a lineáris extrudálásban?

A twist offset egy transzlációs eltolást határoz meg, amelyet a csavart műveletre alkalmazunk. Ahelyett, hogy a pontos extrudálás kiindulópontja körül forgatnánk, a geometria a megadott eltolásvektortól kezd el forogni, így nagyobb művészi kontrollt biztosítva a végső alakzat felett.

## Miért használjuk az Aspose.3D for .NET-et?

- **Teljes körű API** – Kezeli a profilokat, transzformációkat és számos fájlformátumot.  
- **Keresztplatformos** – Windows, Linux és macOS rendszereken működik .NET Core‑val.  
- **Teljesítmény‑optimalizált** – Tiszta hálókat generál manuális számítások nélkül.  
- **Kiváló dokumentáció** – Rengeteg példa a fejlesztés felgyorsításához.

## Előfeltételek

Mielőtt elkezdenénk, győződj meg róla, hogy rendelkezel:

- Aspose.3D for .NET könyvtárral: Töltsd le és telepítsd a könyvtárat a [release page](https://releases.aspose.com/3d/net/) oldalról.  
- Fejlesztői környezettel: Visual Studio, Rider vagy bármely C#‑t támogató IDE.

## Namespace-ek importálása

Először importáld a névtereket, amelyek hozzáférést biztosítanak a fő 3D osztályokhoz.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Ezek a nyilatkozatok elérhetővé teszik a `Scene`, `LinearExtrusion`, `Vector3` és más alapvető típusokat a kódban.

## Lépés‑ről‑lépésre útmutató

### 1. lépés: Alap profil inicializálása

Kezdünk egy egyszerű téglalap profillal, és adunk neki egy kis lekerekítési sugárat, hogy a szélek ne legyenek tökéletesen élesek.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

### 2. lépés: Jelenet létrehozása

A `Scene` egy tárolóként működik minden node, fény, kamera és geometria számára.

```csharp
Scene scene = new Scene();
```

### 3. lépés: Node-ok létrehozása

Két gyermek node‑t adunk a jelenet gyökeréhez — egyik a sima extrudáláshoz, a másik a csavart változathoz. A bal oldali node‑t eltoljuk az X‑tengelyen a vizuális elkülönítés érdekében.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

### 4. lépés: Lineáris extrudálás a bal node‑on (Twist Offset nélkül)

Itt egy alap extrudálást mutatunk be teljes 360°‑os csavarral és 100 szelettel a simaság érdekében.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

### 5. lépés: Lineáris extrudálás a jobb node‑on Twist Offset‑tel

Most egy `(3, 0, 0)` értékű twist offsetet alkalmazunk. Ez három egységgel eltolja a csavart az X‑tengelyen, így egy láthatóan eltolódott spirált hoz létre.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

### 6. lépés: 3D jelenet mentése

Végül a jelenetet egy OBJ fájlba írjuk. A kimeneti útvonalat a környezetednek megfelelően módosítsd.

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Gyakori problémák és megoldások

| Probléma | Miért fordul elő | Megoldás |
|----------|------------------|----------|
| **A csavar laposnak tűnik** | A `Slices` értéke túl alacsony, ezért durva a háló. | Növeld a `Slices` értékét (pl. 200) a simább forgásért. |
| **Az objektum nem középen van** | A `TwistOffset` világkoordinátákat használ; a node már el van tolva. | Alkalmazd az offsetet a node helyi transzformációjához képest, vagy igazítsd a node eltolását. |
| **A fájl nem mentődik** | Hibás kimeneti útvonal vagy hiányzó írási jogosultság. | Ellenőrizd, hogy a könyvtár létezik, és az alkalmazásnak van írási joga. |
| **Licenc kivétel** | Érvényes licenc hiányában futtatod a nem‑próbaverziót. | Tölts be egy ideiglenes vagy állandó licencet a jelenet létrehozása előtt. |

## Gyakran feltett kérdések

### Q1: Használhatom az Aspose.3D for .NET-et más programozási nyelvekkel?

A1: Az Aspose.3D elsősorban .NET nyelveket támogat, de az Aspose hasonló könyvtárakat kínál Java‑ra és más platformokra is.

### Q2: Hogyan szerezhetek ideiglenes licencet az Aspose.3D for .NET-hez?

A2: Látogasd meg a [this link](https://purchase.aspose.com/temporary-license/) oldalt, ahol teszteléshez ideiglenes licencet kaphatsz.

### Q3: Van közösségi fórum az Aspose.3D for .NET-hez?

A3: Természetesen! Csatlakozz a közösséghez a [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) oldalon, hogy más fejlesztőkkel beszélgess és segítséget kérj.

### Q4: Elérhetők további példák és dokumentáció?

A4: Tekintsd meg a [documentation](https://reference.aspose.com/3d/net/) oldalt, ahol részletes útmutatók és példák találhatók.

### Q5: Hol vásárolhatom meg az Aspose.3D for .NET-et?

A5: Látogasd meg a [this link](https://purchase.aspose.com/buy) oldalt, ahol megvásárolhatod és teljes körű hozzáférést kapsz az Aspose.3D-hez.

### Q6: Exportálhatom a modellt OBJ‑n kívül más formátumokba is?

A6: Igen — az Aspose.3D támogatja az FBX, STL, 3MF és sok más formátumot. Csak módosítsd a `FileFormat` enum értékét a `Save` hívásban.

### Q7: Miben különbözik a „how to add twist” egy szokásos forgatástól?

A7: A csavart fokozatosan forgatja a profilt az extrudálás hossza mentén, míg egy szokásos forgatás egyetlen statikus szöget alkalmaz. Az offset egy transzlációs eltolást ad hozzá, mielőtt a forgatás elkezdődne.

---

**Utoljára frissítve:** 2026-03-23  
**Tesztelve:** Aspose.3D for .NET (legújabb kiadás)  
**Szerző:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}