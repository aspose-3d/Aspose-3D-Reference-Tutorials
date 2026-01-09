---
date: 2026-01-09
description: Tanulja meg, hogyan hozhat létre 3D-s jelenetet és menthet 3D-s modellt
  az Aspose.3D for .NET használatával, beleértve a Wavefront OBJ exportálását és a
  lineáris extrudálás szeleteit.
linktitle: Create 3D Scene with Linear Extrusion Slices
second_title: Aspose.3D .NET API
title: 3D-színter létrehozása lineáris extrúziós szeletekkel
url: /hu/net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D jelenet létrehozása lineáris extrúziós szeletekkel

## Bevezetés

Üdvözöljük az Aspose.3D for .NET használatával a 3D tervezés világában! Ebben az útmutatóban **create 3d scene** objektumokat hozunk létre, lineáris extrúziót alkalmazunk egyedi szeletszámokkal, és végül **save 3d model**-t mentünk Wavefront OBJ fájlként. Akár gyors prototípust, akár termék‑kész vizualizációt épít, az alábbi lépések megmutatják, **how to use Aspose**-t a magas minőségű geometria közvetlen generálásához C#‑ból.

## Gyors válaszok
- **What does “create 3d scene” mean?** Ez azt jelenti, hogy egy Scene objektumot hozunk létre, amely tartalmazza az összes 3D entitást (hálókat, fényeket, kamerákat).  
- **Which format is used for export?** A példa **Wavefront OBJ** formátumba exportál (`export wavefront obj`).  
- **How many slices can I set?** Bármilyen egész számot beállíthat; a demó 2 és 10 szeletet mutat.  
- **Do I need a license?** Ideiglenes vagy teljes licenc szükséges a termelési használathoz.  
- **Can I run this on .NET Core?** Igen, az Aspose.3D támogatja a .NET Framework-öt és a .NET Core-t.

## Előfeltételek

Mielőtt belemerülne az Aspose.3D-vel a 3D tervezés világába, győződjön meg róla, hogy rendelkezik a következő előfeltételekkel:

- Aspose.3D for .NET könyvtár: Győződjön meg róla, hogy az Aspose.3D könyvtár telepítve van. Letöltheti [itt](https://releases.aspose.com/3d/net/).
- Integrált fejlesztőkörnyezet (IDE): Használjon bármelyik kedvelt, .NET fejlesztéshez kompatibilis IDE-t.
- Alapvető C# ismeretek: Ismerkedjen meg a C# programozási nyelv alapjaival.
- Vágy a 3D tervezés felfedezésére: Szenvedély a látványos 3D modellek létrehozásához!

## Névterek importálása

A 3D tervezési útja Aspose.3D-vel megkezdéséhez importálnia kell a szükséges névtereket. Ez biztosítja, hogy a kód hozzáférjen a szükséges osztályokhoz és funkciókhoz.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Hogyan hozzunk létre 3d scene-t lineáris extrúzióval

Az alábbiakban lépésről lépésre végigvezetjük a jelenet felépítéséhez, az extrúzió alkalmazásához, és **save 3d model** OBJ fájlként történő mentéséhez szükséges lépéseken. A magyarázatok beszélgetős stílusban íródtak, hogy könnyen követhesse őket.

### 1. lépés: Az alap profil inicializálása

Először definiáljuk a 2‑D alakzatot, amelyet extrudálni fogunk. Ebben az esetben egy lekerekített sarkú téglalap.

```csharp
// ExStart:InitializeBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd:InitializeBaseProfile
```

### 2. lépés: 3D jelenet létrehozása

A `Scene` objektum a geometria, fények és kamerák tárolója – a **creating a 3d scene** alapja.

```csharp
// ExStart:Create3DScene
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### 3. lépés: Bal és jobb csomópontok létrehozása

Két gyermekcsomópontot adunk a jelenet gyökeréhez. Az egyik alacsony szeletszámmal, a másik magasabb számmal fog dolgozni, így látható a vizuális különbség.

```csharp
// ExStart:CreateLeftRightNodes
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### 4. lépés: Lineáris extrúzió végrehajtása a bal csomóponton

Itt a téglalapot **2 slices**-szel extrudáljuk. Kevesebb szelet durvább megjelenést eredményez.

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### 5. lépés: Lineáris extrúzió végrehajtása a jobb csomóponton

Most ugyanazt a profilt extrudáljuk **10 slices**-szel, ami simább felületet eredményez.

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### 6. lépés: 3D jelenet mentése

Végül a jelenetet Wavefront OBJ fájlba exportáljuk. Ez bemutatja, **how to save obj** és **export wavefront obj** használatát az Aspose.3D-vel.

```csharp
// ExStart:Save3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
// ExEnd:Save3DScene
```

## Gyakori problémák és megoldások

| Probléma | Miért fordul elő | Megoldás |
|----------|------------------|----------|
| Az OBJ fájl üresnek tűnik | A kimeneti útvonal helytelen vagy hiányzik az írási jogosultság. | Ellenőrizze, hogy a könyvtár létezik, és az alkalmazásnak van írási joga. |
| A szeletek nem befolyásolják a simaságot | `Slices` értéke túl alacsony a geometria méretéhez. | Növelje a szeletszámot, vagy állítsa be a profil méreteit. |
| Licenc kivétel | Érvényes licenc nélküli futtatás nem‑próba verzióban. | Alkalmazzon ideiglenes vagy állandó licencet a következő kóddal: `License license = new License(); license.SetLicense("Aspose.3D.lic");` |

## Gyakran ismételt kérdések

**Q: Can I use Aspose.3D for .NET with other programming languages?**  
A: Az Aspose.3D elsősorban .NET-hez készült, de felfedezheti az interoperabilitási lehetőségeket olyan nyelvekkel, mint a Python .NET kötésekkel.

**Q: Where can I find detailed documentation for Aspose.3D for .NET?**  
A: A részletes dokumentációt megtalálja [itt](https://reference.aspose.com/3d/net/), amely alapos információkat nyújt az Aspose.3D képességeiről és használatáról.

**Q: Is there a free trial available for Aspose.3D for .NET?**  
A: Igen, a ingyenes próbaverziót [itt](https://releases.aspose.com/) szerezheti meg, hogy a könyvtár funkcióit megismerje a vásárlás előtt.

**Q: How can I get technical support for Aspose.3D for .NET?**  
A: Látogassa meg az Aspose.3D fórumot [itt](https://forum.aspose.com/c/3d/18), hogy segítséget kérjen és a közösséggel kapcsolatba lépjen.

**Q: Can I use a temporary license for Aspose.3D for .NET?**  
A: Igen, ideiglenes licencet szerezhet [itt](https://purchase.aspose.com/temporary-license/) értékelési célokra.

## Összegzés

Gratulálunk! Sikeresen megtanulta, hogyan **create 3d scene**, alkalmazzon lineáris extrúziót egyedi szeletszámokkal, és **save 3d model** Wavefront OBJ fájlként az Aspose.3D for .NET használatával. Ez csak a 3D tervezési útja kezdete — nyugodtan kísérletezzen különböző profilokkal, szeletszámokkal és export formátumokkal, hogy kiaknázza a **3d modeling c#** teljes potenciálját.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2026-01-09  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose