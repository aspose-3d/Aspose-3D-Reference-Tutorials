---
date: 2026-01-17
description: Naučte se, jak vypsat vlastnosti materiálu, změnit difúzní barvu a upravit
  atributy 3D materiálu pomocí Aspose.3D pro .NET. Krok‑za‑krokem jsou zahrnuty příklady
  kódu.
linktitle: List Material Properties in 3D Scenes with Aspose.3D
second_title: Aspose.3D .NET API
title: Seznam materiálových vlastností ve 3D scénách s Aspose.3D
url: /cs/net/3d-scene/set-3d-properties/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Seznam vlastností materiálu ve 3D scénách s Aspose.3D

## Úvod

Pokud potřebujete **vypsat vlastnosti materiálu** 3D modelu a poté doladit například difúzní barvu, jste na správném místě. Aspose.3D pro .NET vám poskytuje čisté, objektově orientované API, které vám umožní prozkoumat, získat a upravit atributy materiálu přímo ve vašem C# kódu. V tomto tutoriálu vás provedeme načtením scény, výčtem jejích vlastností materiálu a změnou hodnot, jako je difúzní komponenta – abyste mohli svým modelům dodat přesně požadovaný vzhled.

## Rychlé odpovědi
- **Jaký je hlavní cíl?** Seznam vlastností materiálu a jejich úprava (např. barva difúze).  
- **Která knihovna je vyžadována?** Aspose.3D pro .NET.  
- **Potřebuji licenci?** Pro produkční použití je vyžadována dočasná nebo plná licence.  
- **Podporované formáty souborů?** FBX, OBJ, STL, STL‑ASCII, 3MF a další.  
- **Typický čas implementace?** Přibližně 10‑15 minut pro základní skript výpisu vlastností.

## Co je **list material properties**?
Výpis vlastností materiálu znamená iteraci přes `PropertyCollection` materiálu a čtení každého názvu vlastnosti a její aktuální hodnoty. To je užitečné pro ladění, vizuální inspekci nebo tvorbu UI ovládacích prvků, které uživatelům umožní během běhu měnit nastavení materiálu.

## Proč použít Aspose.3D k **přístupu k vlastnostem materiálu**?
- **Žádné externí konvertory** – pracujte přímo s nativními .NET objekty.  
- **Bohatý model vlastností** – podporuje vlastní FBX‑specifické atributy kromě standardních PBR hodnot.  
- **Cross‑platform** – funguje na .NET Framework, .NET Core a .NET 5/6+.  

## Požadavky

- Aspose.3D pro .NET nainstalovaný ve vašem projektu. Stáhněte jej [zde](https://releases.aspose.com/3d/net/).
- Složka na disku, kde budete uchovávat své 3‑D zdrojové soubory (např. FBX soubor s vloženými texturami).

Nyní, když máte základy připravené, ponořme se do kódu.

## Importujte jmenné prostory

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

## Krok 1: Načtení 3D scény

```csharp
//ExStart: Load3DScene
string dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
//ExEnd: Load3DScene
```

## Krok 2: **Přístup k vlastnostem materiálu** prvního uzlu

```csharp
//ExStart: AccessMaterialProperties
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//ExEnd: AccessMaterialProperties
```

## Krok 3: **Seznam vlastností materiálu** – zobrazte každý pár název/hodnota

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

## Krok 4: **Jak změnit difúzní** – upravte vlastnost Diffuse

```csharp
//ExStart: GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//modify property value by name
props["Diffuse"] = new Vector3(1, 0, 1); // sets a magenta diffuse color
//ExEnd: GetModifyPropertyByName
```

## Krok 5: **Získat vlastnost podle názvu** – získat silně typovanou instanci

```csharp
//ExStart: GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//ExEnd: GetPropertyInstanceByName
```

## Krok 6: Procházet vlastní vlastnosti vlastnosti (pokročilé)

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

## Jak **změnit barvu 3D materiálu** mimo difúzi
Pokud potřebujete ovlivnit spekulární, ambientní nebo emisivní barvy, jednoduše nahraďte `"Diffuse"` řetězcem `"Specular"` nebo `"Ambient"` v přiřazení `props["..."]` výše. Stejné struktury `Vector3` nebo `Vector4` se použijí.

## Časté úskalí a tipy
- **Rozlišování velikosti písmen v názvu vlastnosti** – klíče vlastností Aspose.3D rozlišují velikost písmen; použijte přesný název z výpisu.
- **Chybějící vlastnost** – ne všechny materiály vystavují každou PBR atribut. Zkontrolujte `props.ContainsKey("Specular")` před přístupem.
- **Ukládání změn** – po úpravě vlastností zavolejte `scene.Save("output.fbx");` pro uložení změn.

## Závěr

Nyní jste se naučili, jak **vypsat vlastnosti materiálu**, **získat vlastnost podle názvu** a **změnit difúzní barvu** (nebo jakýkoli jiný atribut materiálu) pomocí Aspose.3D pro .NET. Experimentujte s různými typy vlastností a doladěte vzhled svých 3‑D aktiv.

## Často kladené otázky

### Q1: Mohu použít Aspose.3D pro .NET s jinými 3D formáty souborů?

A1: Ano, Aspose.3D podporuje různé 3D formáty souborů, včetně FBX, STL a mnoha dalších.

### Q2: Jak mohu získat dočasnou licenci pro Aspose.3D pro .NET?

A2: Navštivte [tuto stránku](https://purchase.aspose.com/temporary-license/) a získejte dočasnou licenci.

### Q3: Existuje komunitní fórum pro uživatele Aspose.3D?

A3: Ano, podporu a diskuze najdete na [fóru Aspose.3D](https://forum.aspose.com/c/3d/18).

### Q4: Kde najdu podrobnou dokumentaci pro Aspose.3D pro .NET?

A4: Odkaz na [dokumentaci](https://reference.aspose.com/3d/net/) poskytuje komplexní návod.

### Q5: Můžu si Aspose.3D pro .NET vyzkoušet zdarma před zakoupením?

A5: Samozřejmě! Stáhněte si [bezplatnou zkušební verzi](https://releases.aspose.com/) a prozkoumejte její funkce.

## Často kladené otázky

**Q: Co představuje `Vector3(1, 0, 1)`?**  
A: Nastavuje difúzní barvu na purpurovou (červená = 1, zelená = 0, modrá = 1) v lineárním barevném prostoru.

**Q: Musím zavolat `scene.Save` po změně vlastností?**  
A: Ano, uložení scény zapíše vaše úpravy na disk; jinak zůstávají pouze v paměti.

**Q: Mohu vyjmenovat vlastní FBX atributy?**  
A: Rozhodně. `PropertyCollection` zahrnuje všechny vlastní atributy, ke kterým můžete přistupovat pomocí `GetProperty("customName")`.

**Q: Existuje způsob, jak hromadně aktualizovat více materiálů?**  
A: Procházejte `scene.RootNode.ChildNodes` a opakujte kroky úpravy vlastností pro každý materiál.

**Q: Podporuje Aspose.3D .NET 6?**  
A: Ano, knihovna je plně kompatibilní s .NET 6 a novějšími verzemi.

**Last Updated:** 2026-01-17  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}