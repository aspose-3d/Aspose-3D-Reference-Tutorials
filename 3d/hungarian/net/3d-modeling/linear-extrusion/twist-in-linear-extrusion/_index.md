---
date: 2026-03-23
description: Tanulja meg, hogyan hozhat létre csavart extrudálást az Aspose.3D for
  .NET segítségével. Ez a lépésről‑lépésre útmutató a lineáris extrudálás csavart
  technikáit mutatja be.
linktitle: Twist in Linear Extrusion
second_title: Aspose.3D .NET API
title: Hogyan készítsünk csavart extrudálást lineáris extrudálásban
url: /hu/net/3d-modeling/linear-extrusion/twist-in-linear-extrusion/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hogyan hozzunk létre extrudálást csavarral lineáris extrudálásban

## Introduction

Ha .NET alkalmazásokat építesz, amelyeknek szemrevaló 3D vizualizációra van szükségük, hamar rájössz, hogy a **how to create extrusion** alapvető készség. Az Aspose.3D for .NET tiszta, nagy teljesítményű API-t biztosít, amellyel egyszerű 2‑D profilokat fejlett 3‑D modellekké alakíthatsz – különösen, ha csavart adsz hozzá. Ebben az útmutatóban lépésről lépésre végigvezetünk, a jelenet beállításától a végső OBJ fájl mentéséig, hogy láthasd a lineáris extrudálás csavarral hatását a gyakorlatban.

## Quick Answers
- **Mi a fő osztály az extrudáláshoz?** `LinearExtrusion`
- **Melyik tulajdonság ad hozzá forgást?** `Twist`
- **Hány szelet ad sima eredményt?** Körülbelül 100 szelet (szükség szerint állítható)
- **Használhatok más alakzatokat?** Igen, bármely `IProfile`, például körök, sokszögek vagy egyedi görbék
- **Milyen fájlformátumot használ a példában?** Wavefront OBJ (`.obj`)

## Prerequisites

Mielőtt belemerülnénk, győződj meg róla, hogy a következőkkel rendelkezel:

- Aspose.3D for .NET telepítve van. Ha még nem töltötted le, szerezd be **[here](https://releases.aspose.com/3d/net/)**.
- Működő .NET fejlesztői környezet (Visual Studio, VS Code vagy bármely általad preferált IDE).
- Alapvető ismeretek a C# szintaxisról és az objektum‑orientált koncepciókról.

## Import Namespaces

Bármely .NET projektben a névterek helyes használata kulcsfontosságú. Kezdd a szükséges névterek importálásával, hogy hatékonyan kihasználhasd az Aspose.3D funkcióit. Íme egy kódrészlet, amely útmutatást ad:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Step‑by‑Step Guide

### Step 1: Initialize the Base Profile

Alapprofil inicializálása

Először definiáljuk azt a formát, amelyet extrudálni fogunk. Ebben a példában egy téglalapot használunk kis lekerekítési sugárral, hogy az élek enyhe ívet kapjanak.

```csharp
// Initialize the base profile to be extruded
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

### Step 2: Create a 3D Scene

3D jelenet létrehozása

`Scene` objektum a vászonként működik, ahol minden 3‑D entitás él. Gondolj rá, mint az extrudálás színpadára.

```csharp
// Create a scene 
Scene scene = new Scene();
```

### Step 3: Add Left and Right Nodes

Bal és jobb csomópontok hozzáadása

A csomópontok lehetővé teszik az objektumok hierarchikus szervezését. Két testvér csomópontot hozunk létre – egyet egyenes extrudáláshoz és egyet a csavart változathoz.

```csharp
// Create left node
var left = scene.RootNode.CreateChildNode();
// Create right node
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
```

### Step 4: Perform Linear Extrusion with Twist on the Left Node

Lineáris extrudálás csavarral a bal csomóponton

`Twist` tulajdonság szabályozza, hogy mennyire fordul el a profil az extrudálás során. **0**‑ra állítva klasszikus egyenes extrudálást kapunk.

```csharp
// Twist property defines the degree of the rotation while extruding the profile
// Perform linear extrusion on the left node using twist and slices property
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 0, Slices = 100 });
```

### Step 5: Perform Linear Extrusion with Twist on the Right Node

Lineáris extrudálás csavarral a jobb csomóponton

Most 90‑fokos csavart alkalmazunk ugyanarra a profilra. Ez egyértelműen bemutatja a **linear extrusion twist** hatást.

```csharp
// Perform linear extrusion on the right node using twist and slices property
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 90, Slices = 100 });
```

### Step 6: Save the 3D Scene

3D jelenet mentése

Végül exportáld a jelenetet egy olyan formátumba, amelyet bármely 3‑D megjelenítő képes megnyitni. A példa a Wavefront OBJ-t használja, de az Aspose.3D számos más formátumot is támogat.

```csharp
// Save 3D scene
scene.Save("Your Output Directory" + "TwistInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Why Use Linear Extrusion with a Twist?

- **Rapid prototyping:** 2‑D vázlatok 3‑D alkatrészekké alakítása manuális modellezés nélkül.
- **Design flexibility:** Állítsd be a `Twist` értékét spirálok, csavarszerű bordák vagy dekoratív elemek létrehozásához.
- **Performance‑friendly:** A `Slices` paraméter lehetővé teszi a vizuális hűség és a futási sebesség egyensúlyozását.

## Common Issues & Tips

- **Too many slices:** Bár 100 szelet sima megjelenést ad, a rendkívül magas értékek lassíthatják a renderelést. Tesztelj alacsonyabb számokkal, ha a teljesítmény aggályt jelent.
- **Negative twist values:** A negatív `Twist` az ellenkező irányba forgat – hasznos tükrözött tervekhez.
- **File paths:** Győződj meg róla, hogy a kimeneti könyvtár létezik és írási jogosultsággal rendelkezel; ellenkező esetben a `scene.Save` kivételt dob.

## Conclusion

Ebben az útmutatóban bemutattuk, hogyan kell **how to create extrusion** csavarral az Aspose.3D for .NET használatával. A `Twist` és `Slices` tulajdonságok beállításával számos alakzatot generálhatsz, az egyszerű csavart rudaktól a komplex csavarszerű struktúrákig, mindezt csak néhány kódsorral.

## Frequently Asked Questions

**Q: Alkalmazhatok lineáris extrudálást csavarral más alakzatokra?**  
A: Természetesen! Bármely osztály, amely implementálja az `IProfile`‑t – például `CircleShape`, `PolygonShape` vagy egy egyedi spline – csavarral extrudálható.

**Q: Mit jelent valójában a `Twist` tulajdonság?**  
A: A profilra az extrudálás hosszában alkalmazott teljes forgásszöget (fokban) adja meg.

**Q: A szeletek számának növelése befolyásolja a memóriahasználatot?**  
A: Igen, több szelet több csúcsot és felületet generál, ami több memóriát igényel, és alacsonyabb teljesítményű eszközökön a teljesítményt is befolyásolhatja.

**Q: Kombinálhatom a lineáris extrudálást más Aspose.3D funkciókkal?**  
A: Határozottan. Az extrudálás után anyagokat, textúrákat vagy akár Boolean műveleteket is alkalmazhatsz, hogy még gazdagabb modelleket hozz létre.

**Q: Hol kaphatok segítséget vagy beszélhetek ötletekről más fejlesztőkkel?**  
A: Csatlakozz az Aspose.3D közösséghez a **[Aspose Forum](https://forum.aspose.com/c/3d/18)** oldalon támogatás, minták és megbeszélések céljából.

---

**Last Updated:** 2026-03-23  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}