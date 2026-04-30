---
date: 2026-03-28
description: Tanulja meg, hogyan listázhatja az anyag tulajdonságait, módosíthatja
  a diffúz színt, és változtathat a 3D anyag attribútumain az Aspose.3D for .NET segítségével.
  Lépésről‑lépésre kódpéldák is szerepelnek.
linktitle: List Material Properties in 3D Scenes with Aspose.3D
second_title: Aspose.3D .NET API
title: Anyagtulajdonságok listázása 3D jelenetekben az Aspose.3D segítségével
url: /hu/net/3d-scene/set-3d-properties/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D jelenetek anyagtulajdonságainak listázása az Aspose.3D-val

## Bevezetés

Ha **anyagtulajdonságokat** kell listáznod egy 3D modellnél, és aztán finomhangolni szeretnéd például a diffúz színt, jó helyen vagy. Az Aspose.3D for .NET egy tiszta, objektum‑orientált API-t biztosít, amely lehetővé teszi az anyagtulajdonságok vizsgálatát, lekérdezését és módosítását anélkül, hogy elhagynád a C# kódodat. Ebben az útmutatóban végigvezetünk a jelenet betöltésén, az anyagtulajdonságok felsorolásán, és a diffúz komponenshez hasonló értékek módosításán – hogy pontosan olyan megjelenést adhass a modelljeidnek, amilyet szeretnél.

## Gyors válaszok
- **Mi a fő cél?** Anyagtulajdonságok listázása és módosítása (pl. diffúz szín).  
- **Melyik könyvtár szükséges?** Aspose.3D for .NET.  
- **Szükségem van licencre?** Ideiglenes vagy teljes licenc szükséges a termelésben való használathoz.  
- **Támogatott fájlformátumok?** FBX, OBJ, STL, STL‑ASCII, 3MF és továbbiak.  
- **Átlagos megvalósítási idő?** Körülbelül 10‑15 perc egy egyszerű tulajdonság‑listázó szkripthez.

## Mi az a **anyagtulajdonságok listázása**?
Az anyagtulajdonságok listázása azt jelenti, hogy végigiterálunk egy anyag `PropertyCollection`‑jén, hogy kiolvassuk minden tulajdonság nevét és aktuális értékét. Ez hasznos hibakereséshez, vizuális ellenőrzéshez, vagy olyan UI vezérlők létrehozásához, amelyek lehetővé teszik a felhasználók számára az anyagbeállítások futás közbeni finomhangolását.

## Miért használjuk az Aspose.3D-t **anyagtulajdonságok eléréséhez**?
- **Nincsenek külső konverterek** – közvetlenül a natív .NET objektumokkal dolgozhatsz.  
- **Gazdag tulajdonságmodell** – támogatja az egyedi FBX‑specifikus attribútumokat a szabványos PBR értékek mellett.  
- **Keresztplatformos** – működik .NET Framework, .NET Core és .NET 5/6+ környezetekben.  

## Előfeltételek

- Aspose.3D for .NET telepítve a projektedben. Letöltheted [itt](https://releases.aspose.com/3d/net/).
- Egy mappa a lemezen, amely a 3‑D forrásfájljaidat tartalmazza (pl. egy beágyazott textúrákkal rendelkező FBX fájl).

Miután az alapok rendben vannak, merüljünk el a kódban.

## Névterek importálása

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## 1. lépés: 3D jelenet betöltése

```csharp
//ExStart: Load3DScene
string dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
//ExEnd: Load3DScene
```

## 2. lépés: Az első csomópont **anyagtulajdonságainak** elérése

```csharp
//ExStart: AccessMaterialProperties
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//ExEnd: AccessMaterialProperties
```

## 3. lépés: **Anyagtulajdonságok listázása** – minden név/érték pár megtekintése

```csharp
//ExStart: ListAllProperties
foreach (var prop in props)
{
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}

//or using ordinal for loop
for (int i = 0; i < props.Count; i++)
{
    var prop = props[i];
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}
//ExEnd: ListAllProperties
```

## 4. lépés: **Hogyan változtassuk meg a diffúz színt** – a Diffuse tulajdonság módosítása

```csharp
//ExStart: GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//modify property value by name
props["Diffuse"] = new Vector3(1, 0, 1); // sets a magenta diffuse color
//ExEnd: GetModifyPropertyByName
```

## 5. lépés: **Tulajdonság lekérése név alapján** – erősen típusos példány beszerzése

```csharp
//ExStart: GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//ExEnd: GetPropertyInstanceByName
```

## 6. lépés: Tulajdonság saját tulajdonságainak bejárása (haladó)

```csharp
//ExStart: TraversePropertyProperties
Console.WriteLine("Property flags = {0}", pdiffuse.GetProperty("flags"));

//and some properties that only defined in FBX file:
Console.WriteLine("Label = {0}", pdiffuse.GetProperty("label"));
Console.WriteLine("Type Name = {0}", pdiffuse.GetProperty("typeName"));

//traversal on property's property is possible
foreach (var pp in pdiffuse.Properties)
{
    Console.WriteLine("Diffuse.{0} = {1}", pp.Name, pp.Value);
}
//ExEnd: TraversePropertyProperties
```

## Hogyan **változtassuk meg a 3D anyag színét** a diffúz színen kívül
Ha a spekuláris, ambient vagy emisszív színeket szeretnéd módosítani, egyszerűen cseréld le a `"Diffuse"`‑t `"Specular"`‑ra vagy `"Ambient"`‑ra a fenti `props["..."]` hozzárendelésben. Ugyanazok a `Vector3` vagy `Vector4` struktúrák érvényesek.

## Hogyan **frissítsük az anyag színét C#-ban**
Egy anyag vizuális megjelenésének módosítása lényegében a megfelelő tulajdonság frissítését jelenti a `PropertyCollection`‑ben. Akár a diffúz, spekuláris vagy bármely egyedi színattribútumot szeretnéd módosítani, a minta ugyanaz marad:

1. A tulajdonság lekérése a pontos név alapján (kis‑nagybetű érzékeny).  
2. Új `Vector3` (RGB) vagy `Vector4` (RGBA) érték hozzárendelése.  

Mivel az API közvetlenül a C# objektumokkal dolgozik, **anyag szín frissítése C#-ban** kódot használhatsz köztes fájlok vagy konverterek nélkül. Ez tökéletes a valós‑idő szerkesztők vagy kötegelt feldolgozási folyamatok számára.

## Gyakori hibák és tippek
- **Tulajdonság név kis‑nagybetű érzékenység** – az Aspose.3D tulajdonságkulcsok kis‑nagybetű érzékenyek; használd a listázási kimenetben megjelenő pontos nevet.  
- **Hiányzó tulajdonság** – nem minden anyag teszi elérhetővé az összes PBR attribútumot. Ellenőrizd a `props.ContainsKey("Specular")`‑t, mielőtt hozzáférnél.  
- **Változások mentése** – a tulajdonságok módosítása után hívd a `scene.Save("output.fbx");`‑t a változások mentéséhez.

## Összegzés

Most már megtanultad, hogyan **listázhatod az anyagtulajdonságokat**, **lekérheted egy tulajdonságot név alapján**, és **módosíthatod a diffúz színt** (vagy bármely más anyagattribútumot) az Aspose.3D for .NET segítségével. Kísérletezz különböző tulajdonságtípusokkal, hogy finomhangold a 3‑D eszközeid megjelenését, és ne feledd, hogy **anyag szín frissítése C#-ban** egyetlen kódsorral is megoldható.

## Gyakran ismételt kérdések

### K1: Használhatom az Aspose.3D for .NET-et más 3D fájlformátumokkal?
A1: Igen, az Aspose.3D számos 3D fájlformátumot támogat, többek között FBX, STL és még sok más.

### K2: Hogyan szerezhetek ideiglenes licencet az Aspose.3D for .NET-hez?
A2: Látogasd meg [itt](https://purchase.aspose.com/temporary-license/) a licenc megszerzéséhez.

### K3: Van közösségi fórum az Aspose.3D felhasználók számára?
A3: Igen, támogatást és megbeszéléseket találsz a [Aspose.3D fórumon](https://forum.aspose.com/c/3d/18).

### K4: Hol találok részletes dokumentációt az Aspose.3D for .NET-hez?
A4: Tekintsd meg a [dokumentációt](https://reference.aspose.com/3d/net/) a teljes körű útmutatáshoz.

### K5: Próbálhatom-e ingyenesen az Aspose.3D for .NET-et vásárlás előtt?
A5: Természetesen! Töltsd le a [ingyenes próbaverziót](https://releases.aspose.com/), hogy felfedezd a funkciókat.

## Gyakran Ismételt Kérdések

**Q: Mit jelent a `Vector3(1, 0, 1)`?**  
A: A diffúz színt magentára állítja (vörös = 1, zöld = 0, kék = 1) lineáris színtérben.

**Q: Hívnom kell a `scene.Save`‑t a tulajdonságok módosítása után?**  
A: Igen, a jelenet mentése a módosításokat lemezre írja; különben a változások csak memóriában maradnak.

**Q: Listázhatok-e egyedi FBX attribútumokat?**  
A: Természetesen. A `PropertyCollection` tartalmazni fog minden egyedi attribútumot, amelyhez a `GetProperty("customName")`‑val férhetsz hozzá.

**Q: Van‑e mód a több anyag kötegelt frissítésére?**  
A: Iterálj a `scene.RootNode.ChildNodes`‑on, és ismételd meg a tulajdonság‑módosítási lépéseket minden anyagra.

**Q: Támogatja-e az Aspose.3D a .NET 6‑ot?**  
A: Igen, a könyvtár teljes mértékben kompatibilis a .NET 6‑tal és újabb verziókkal.

**Last Updated:** 2026-03-28  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}