---
date: 2026-01-17
description: Tanulja meg, hogyan listázhatja az anyag tulajdonságait, megváltoztathatja
  a diffúz színt, és módosíthatja a 3D anyag attribútumait az Aspose.3D for .NET segítségével.
  Lépésről‑lépésre kódpéldák is szerepelnek.
linktitle: List Material Properties in 3D Scenes with Aspose.3D
second_title: Aspose.3D .NET API
title: Anyagjellemzők listázása 3D jelenetekben az Aspose.3D segítségével
url: /hu/net/3d-scene/set-3d-properties/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Anyag tulajdonságok felsorolása 3D jelenetekben az Aspose.3D segítségével

## Bevezetés

Ha **anyag tulajdonságok** listázására van szükséged egy 3D modellben, majd finomhangolni szeretnéd például a diffúz színt, jó helyen vagy. Az Aspose.3D for .NET tiszta, objektum‑orientált API‑t biztosít, amely lehetővé teszi az anyag attribútumok vizsgálatát, lekérését és módosítását anélkül, hogy elhagynád a C# kódodat. Ebben az útmutatóban végigvezetünk a jelenet betöltésén, az anyag tulajdonságainak felsorolásán, és a diffúz komponens értékének módosításán – így a modelleknek pontosan azt a megjelenést adhatod, amit szeretnél.

## Gyors válaszok
- **Mi a fő cél?** Anyag tulajdonságok felsorolása és módosítása (pl. diffúz szín).  
- **Melyik könyvtár szükséges?** Aspose.3D for .NET.  
- **Szükségem van licencre?** Ideiglenes vagy teljes licenc szükséges a termelési használathoz.  
- **Támogatott fájlformátumok?** FBX, OBJ, STL, STL‑ASCII, 3MF és továbbiak.  
- **Átlagos megvalósítási idő?** Körülbelül 10‑15 perc egy alap tulajdonság‑listázó szkripthez.

## Mi az a **list material properties**?
Az anyag tulajdonságainak listázása azt jelenti, hogy végigiterálunk egy anyag `PropertyCollection`‑jén, és kiolvassuk minden tulajdonság nevét és aktuális értékét. Ez hibakereséshez, vizuális ellenőrzéshez vagy olyan UI vezérlők építéséhez hasznos, amelyek lehetővé teszik a felhasználók számára az anyag beállításainak futásidőben történő finomhangolását.

## Miért használjuk az Aspose.3D‑t a **material properties** eléréséhez?
- **Nincs külső konverter** – közvetlenül natív .NET objektumokkal dolgozik.  
- **Gazdag tulajdonság modell** – támogatja az egyedi FBX‑specifikus attribútumokat a szabványos PBR értékek mellett.  
- **Cross‑platform** – működik .NET Framework, .NET Core és .NET 5/6+ környezetekben.  

## Előkövetelmények

- Aspose.3D for .NET telepítve a projektedben. Letöltheted [itt](https://releases.aspose.com/3d/net/).
- Egy mappa a lemezen a 3‑D forrásfájlok tárolásához (pl. egy beágyazott textúrákkal rendelkező FBX fájl).

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

## 2. lépés: **Material properties** elérése az első csomópontnál

```csharp
//ExStart: AccessMaterialProperties
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//ExEnd: AccessMaterialProperties
```

## 3. lépés: **List material properties** – minden név/érték pár megtekintése

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

## 4. lépés: **Hogyan változtassuk a diffúzt** – a Diffuse tulajdonság módosítása

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

## Hogyan **változtassuk a 3D anyag színét** a diffúzon túl
Ha a spekuláris, ambient vagy emisszív színeket is módosítani szeretnéd, egyszerűen cseréld le a `"Diffuse"`‑t `"Specular"`‑ra vagy `"Ambient"`‑ra a fenti `props["..."]` hozzárendelésben. Ugyanazok a `Vector3` vagy `Vector4` struktúrák alkalmazandók.

## Gyakori hibák és tippek
- **Tulajdonság név kis- és nagybetű érzékenység** – az Aspose.3D kulcsai kis- és nagybetű érzékenyek; használd a listázás kimenetében megjelenő pontos nevet.  
- **Hiányzó tulajdonság** – nem minden anyag teszi közzé az összes PBR attribútumot. Ellenőrizd a `props.ContainsKey("Specular")` kifejezést a hozzáférés előtt.  
- **Változások mentése** – a tulajdonságok módosítása után hívd a `scene.Save("output.fbx");` metódust a változások mentéséhez.

## Összegzés

Most már megtanultad, hogyan **listáld az anyag tulajdonságait**, **lekérj egy tulajdonságot név alapján**, és **módosítsd a diffúz színt** (vagy bármely más anyag attribútumot) az Aspose.3D for .NET segítségével. Kísérletezz különböző tulajdonság típusokkal, hogy finomhangold 3‑D eszközeid megjelenését.

## GYIK

### K1: Használhatom az Aspose.3D for .NET-et más 3D fájlformátumokkal?
**A1:** Igen, az Aspose.3D támogatja a különböző 3D fájlformátumokat, beleértve az FBX, STL és sok más.

### K2: Hogyan szerezhetek ideiglenes licencet az Aspose.3D for .NET-hez?
**A2:** Látogass el [ide](https://purchase.aspose.com/temporary-license/) az ideiglenes licenc megszerzéséhez.

### K3: Van közösségi fórum az Aspose.3D felhasználók számára?
**A3:** Igen, támogatást és megbeszéléseket találsz az [Aspose.3D fórumon](https://forum.aspose.com/c/3d/18).

### K4: Hol találok részletes dokumentációt az Aspose.3D for .NET-hez?
**A4:** Lásd a [dokumentációt](https://reference.aspose.com/3d/net/) a teljes útmutatóért.

### K5: Próbálhatom ingyenesen az Aspose.3D for .NET-et vásárlás előtt?
**A5:** Természetesen! Töltsd le a [ingyenes próbaverziót](https://releases.aspose.com/) a funkciók felfedezéséhez.

## Gyakran Ismételt Kérdések

**Q: Mi jelenti a `Vector3(1, 0, 1)`?**  
A: A diffúz színt magentára állítja (vörös = 1, zöld = 0, kék = 1) lineáris színterben.

**Q: Kell-e meghívni a `scene.Save`‑t a tulajdonságok módosítása után?**  
A: Igen, a jelenet mentése írja a módosításokat a lemezre; egyébként a változások csak memóriában maradnak.

**Q: Felsorolhatok egyedi FBX attribútumokat?**  
A: Természetesen. A `PropertyCollection` tartalmazza az egyedi attribútumokat, amelyeket a `GetProperty("customName")` segítségével érhetsz el.

**Q: Van mód több anyag kötegelt frissítésére?**  
A: Iterálj a `scene.RootNode.ChildNodes`‑on és ismételd meg a tulajdonság‑módosítási lépéseket minden anyagnál.

**Q: Támogatja az Aspose.3D a .NET 6-ot?**  
A: Igen, a könyvtár teljesen kompatibilis a .NET 6-tal és újabb verziókkal.

**Utolsó frissítés:** 2026-01-17  
**Tesztelve:** Aspose.3D 24.11 for .NET  
**Szerző:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}