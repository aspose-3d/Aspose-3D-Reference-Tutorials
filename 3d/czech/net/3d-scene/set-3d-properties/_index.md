---
date: 2026-03-28
description: Naučte se, jak vypsat vlastnosti materiálu, změnit difúzní barvu a upravit
  atributy 3D materiálu pomocí Aspose.3D pro .NET. Krok‑za‑krokem jsou zahrnuty příklady
  kódu.
linktitle: List Material Properties in 3D Scenes with Aspose.3D
second_title: Aspose.3D .NET API
title: Seznam vlastností materiálu ve 3D scénách s Aspose.3D
url: /cs/net/3d-scene/set-3d-properties/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Seznam vlastností materiálu ve 3D scénách s Aspose.3D

## Úvod

Pokud potřebujete **list material properties** 3D modelu a následně doladit například difúzní barvu, jste na správném místě. Aspose.3D pro .NET vám poskytuje čisté, objektově orientované API, které vám umožní prohlížet, získávat a měnit atributy materiálu přímo ve vašem C# kódu. V tomto tutoriálu si ukážeme, jak načíst scénu, vypsat její vlastnosti materiálu a změnit hodnoty, jako je difúzní komponenta — aby vaše modely měly přesně ten vzhled, který chcete.

## Rychlé odpovědi
- **Jaký je hlavní cíl?** Vypsat vlastnosti materiálu a upravit je (např. difúzní barvu).  
- **Která knihovna je vyžadována?** Aspose.3D pro .NET.  
- **Potřebuji licenci?** Pro produkční použití je vyžadována dočasná nebo plná licence.  
- **Podporované formáty souborů?** FBX, OBJ, STL, STL‑ASCII, 3MF a další.  
- **Typický čas implementace?** Přibližně 10‑15 minut pro základní skript vypisující vlastnosti.

## Co je **list material properties**?
Vypsání vlastností materiálu znamená iteraci přes `PropertyCollection` materiálu a čtení každého názvu vlastnosti a její aktuální hodnoty. To je užitečné pro ladění, vizuální kontrolu nebo tvorbu UI ovládacích prvků, které uživatelům umožní měnit nastavení materiálu za běhu.

## Proč použít Aspose.3D k **access material properties**?
- **Žádné externí konvertory** — pracujte přímo s nativními .NET objekty.  
- **Bohatý model vlastností** — podporuje vlastní FBX‑specifické atributy i standardní PBR hodnoty.  
- **Cross‑platform** — funguje na .NET Framework, .NET Core i .NET 5/6+.

## Předpoklady

- Aspose.3D pro .NET nainstalovaný ve vašem projektu. Stáhněte jej [zde](https://releases.aspose.com/3d/net/).
- Složka na disku, kde budete uchovávat své 3‑D zdrojové soubory (např. FBX soubor s vloženými texturami).

Nyní, když máte základní věci připravené, pojďme se ponořit do kódu.

## Importovat jmenné prostory

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

## Krok 1: Načíst 3D scénu

```csharp
//ExStart: Load3DScene
string dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
//ExEnd: Load3DScene
```

## Krok 2: **Access material properties** první uzlu

```csharp
//ExStart: AccessMaterialProperties
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//ExEnd: AccessMaterialProperties
```

## Krok 3: **List material properties** — zobrazit každý pár název/hodnota

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

## Krok 4: **How to change diffuse** — upravit vlastnost Diffuse

```csharp
//ExStart: GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//modify property value by name
props["Diffuse"] = new Vector3(1, 0, 1); // sets a magenta diffuse color
//ExEnd: GetModifyPropertyByName
```

## Krok 5: **Retrieve property by name** — získat silně typovanou instanci

```csharp
//ExStart: GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//ExEnd: GetPropertyInstanceByName
```

## Krok 6: Procházet podvlastnosti vlastnosti (pokročilé)

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

## Jak **change 3d material color** mimo difúzní
Pokud potřebujete ovlivnit spekulární, ambientní nebo emisivní barvy, jednoduše nahraďte `"Diffuse"` za `"Specular"` nebo `"Ambient"` v přiřazení `props["..."]` výše. Použijí se stejné struktury `Vector3` nebo `Vector4`.

## Jak **update material color in C#**
Změna vizuálního vzhledu materiálu spočívá v aktualizaci příslušné vlastnosti v `PropertyCollection`. Ať už chcete upravit difúzní, spekulární nebo jakýkoli vlastní barevný atribut, postup zůstává stejný:

1. Získejte vlastnost podle jejího přesného názvu (rozlišuje velká a malá písmena).  
2. Přiřaďte novou hodnotu `Vector3` (RGB) nebo `Vector4` (RGBA).  

Protože API pracuje přímo s C# objekty, můžete **update material color C#** přímo v kódu bez jakýchkoli mezisouborů nebo konvertorů. To je ideální pro editory v reálném čase nebo dávkové zpracování.

## Časté úskalí a tipy
- **Rozlišování velkých a malých písmen u názvů vlastností** — klíče v Aspose.3D jsou case‑sensitive; použijte přesně název z výpisu.  
- **Chybějící vlastnost** — ne všechny materiály vystavují každou PBR vlastnost. Před přístupem zkontrolujte `props.ContainsKey("Specular")`.  
- **Ukládání změn** — po úpravě vlastností zavolejte `scene.Save("output.fbx");`, aby se změny uložily.

## Závěr

Nyní jste se naučili, jak **list material properties**, **retrieve a property by name** a **change the diffuse color** (nebo jakýkoli jiný atribut materiálu) pomocí Aspose.3D pro .NET. Experimentujte s různými typy vlastností a dolaďte vzhled svých 3‑D assetů, a pamatujte, že **update material color C#** lze provést jediným řádkem kódu.

## Často kladené otázky

### Q1: Mohu použít Aspose.3D pro .NET s jinými 3D formáty souborů?

A1: Ano, Aspose.3D podporuje různé 3D formáty, včetně FBX, STL a mnoha dalších.

### Q2: Jak získám dočasnou licenci pro Aspose.3D pro .NET?

A2: Navštivte [zde](https://purchase.aspose.com/temporary-license/) a získejte dočasnou licenci.

### Q3: Existuje komunitní fórum pro uživatele Aspose.3D?

A3: Ano, podporu a diskuze najdete na [Aspose.3D fóru](https://forum.aspose.com/c/3d/18).

### Q4: Kde najdu podrobnou dokumentaci pro Aspose.3D pro .NET?

A4: Viz [dokumentace](https://reference.aspose.com/3d/net/) pro komplexní návod.

### Q5: Můžu si Aspose.3D pro .NET vyzkoušet zdarma před zakoupením?

A5: Samozřejmě! Stáhněte si [bezplatnou zkušební verzi](https://releases.aspose.com/) a prozkoumejte funkce.

## Často kladené otázky

**Q: Co představuje `Vector3(1, 0, 1)`?**  
A: Nastavuje difúzní barvu na purpurovou (červená = 1, zelená = 0, modrá = 1) v lineárním barevném prostoru.

**Q: Musím zavolat `scene.Save` po změně vlastností?**  
A: Ano, uložení scény zapíše úpravy na disk; jinak zůstávají pouze v paměti.

**Q: Mohu enumerovat vlastní FBX atributy?**  
A: Ano. `PropertyCollection` zahrnuje všechny vlastní atributy, ke kterým můžete přistupovat pomocí `GetProperty("customName")`.

**Q: Existuje způsob, jak hromadně aktualizovat více materiálů?**  
A: Procházejte `scene.RootNode.ChildNodes` a opakujte kroky úpravy vlastností pro každý materiál.

**Q: Podporuje Aspose.3D .NET 6?**  
A: Ano, knihovna je plně kompatibilní s .NET 6 a novějšími verzemi.

---

**Poslední aktualizace:** 2026-03-28  
**Testováno s:** Aspose.3D 24.11 pro .NET  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}