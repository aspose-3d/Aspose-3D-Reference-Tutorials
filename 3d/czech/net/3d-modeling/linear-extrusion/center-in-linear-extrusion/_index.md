---
date: 2026-01-07
description: Naučte se, jak přidat podkladovou rovinu při lineárním extrudování pomocí
  Aspose.3D pro .NET a exportovat soubory Wavefront OBJ. Ovládněte techniky centrování
  a zakotvení v 3‑D modelování.
linktitle: Add Ground Plane and Center in Linear Extrusion
second_title: Aspose.3D .NET API
title: Přidat podkladovou rovinu a střed v lineární extruzi
url: /cs/net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Přidání zemní roviny a centrování při lineárním vytahování

## Úvod

Vítejte v tomto komplexním průvodci, který vás provede ovládáním lineárního vytahování pomocí Aspose.3D pro .NET. Pokud chcete **přidat zemní rovinu** k vašim modelům a **exportovat soubory Wavefront OBJ** při zachování centrovaného vytahování, jste na správném místě. V tomto tutoriálu se podrobně zaměříme na techniku lineárního vytahování, konkrétně na aspekt centrování a na to, jak zemní rovina pomáhá lépe vizualizovat výsledek.

## Rychlé odpovědi
- **Co přináší “přidání zemní roviny”?** Poskytuje vizuální referenci, která usnadňuje vidět, kde se vytahování nachází v rovině X‑Z.  
- **Jaký formát se používá pro export modelu?** Scéna se ukládá jako soubor Wavefront OBJ (`FileFormat.WavefrontOBJ`).  
- **Potřebuji licenci pro spuštění kódu?** Pro vývoj stačí bezplatná zkušební verze; pro produkci je vyžadována trvalá licence.  
- **Mohu změnit délku vytahování?** Ano – upravte druhý parametr `LinearExtrusion`.  
- **Je centrování volitelné?** Nastavením `Center = true` se vytahování vycentruje kolem profilu; `false` jej zarovná na jednu stranu.

## Předpoklady

Než se pustíme do této vzrušující cesty, ujistěte se, že máte splněny následující předpoklady:

- Základní znalost programovacího jazyka C#.  
- Nainstalované Visual Studio na vašem počítači.  
- Knihovnu Aspose.3D pro .NET, kterou si můžete stáhnout z [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/).  
- Přístup k [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/) pro referenci během celého tutoriálu.

## Import jmenných prostorů

Na úvod si naimportujeme potřebné jmenné prostory. Ty vytvoří základ pro naše 3D modelování.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Krok 1: Inicializace základního profilu

Definujeme obdélníkový profil, který bude následně vytahován. `RoundingRadius` přidá jemný zaoblení rohů.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Krok 2: Vytvoření 3D scény

Objekt `Scene` funguje jako kontejner pro veškerou geometrii, světla a kamery.

```csharp
Scene scene = new Scene();
```

## Krok 3: Vytvoření levých a pravých uzlů

Pod kořenem vytvoříme dva sourozenecké uzly. Jeden ukáže vytahování **bez** centrování, druhý **s** centrováním. Levý uzel také posuneme, aby se oba příklady nepřekrývaly.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## Krok 4: Provedení lineárního vytahování na levém uzlu (bez centra)

Zde vytahujeme profil bez centrování. Všimněte si příznaku `Center = false`.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## Krok 5: Přidání zemní roviny pro referenci (levý uzel)

Přidáním tenkého kvádru vytvoříme **zemní rovinu**, která jasně ukazuje, jak se vytahování nachází na základně.

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## Krok 6: Provedení lineárního vytahování na pravém uzlu (s centrem)

Nyní vytahujeme stejný profil, ale povolíme centrování. Geometrie bude symetricky umístěna kolem počátku profilu.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## Krok 7: Přidání zemní roviny pro referenci (pravý uzel)

Druhá zemní rovina je přidána k pravému uzlu, aby vizuální srovnání zůstalo konzistentní.

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## Krok 8: Export souboru Wavefront OBJ

Nakonec **exportujeme Wavefront OBJ**, aby výsledek mohl být otevřen v libovolném standardním 3‑D prohlížeči.

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Proč přidávat zemní rovinu?

Přidání zemní roviny poskytuje okamžitou vizuální nápovědu o výšce a zarovnání vytahování. Je to zvláště užitečné, když potřebujete porovnat centrované a necentrované výsledky, jak je ukázáno v tomto tutoriálu.

## Časté problémy a tipy

- **Zemní rovina není vidět:** Ujistěte se, že tloušťka roviny (`0.01` v konstruktoru `Box`) je dostatečně malá, aby nezakrývala vytahování, ale zároveň dostatečně velká, aby byla vykreslena.  
- **Export selže:** Ověřte, že výstupní adresář existuje a máte oprávnění k zápisu.  
- **Centrované vytahování se jeví posunuté:** Zkontrolujte vlastnost `Center`; `true` vycentruje profil, `false` jej zarovná na jednu stranu.

## Často kladené otázky

### Q1: Mohu použít Aspose.3D pro .NET s jinými programovacími jazyky?

A1: Aspose.3D primárně podporuje .NET jazyky jako C# a VB.NET.

### Q2: Kde mohu najít podporu pro dotazy týkající se Aspose.3D?

A2: Navštivte [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) pro specializovanou podporu a diskuse.

### Q3: Je k dispozici bezplatná zkušební verze Aspose.3D pro .NET?

A3: Ano, bezplatnou zkušební verzi získáte [zde](https://releases.aspose.com/).

### Q4: Jak mohu získat dočasnou licenci pro Aspose.3D pro .NET?

A4: Dočasnou licenci můžete získat [zde](https://purchase.aspose.com/temporary-license/).

### Q5: Kde mohu zakoupit licenci Aspose.3D pro .NET?

A5: Licenci si můžete koupit [zde](https://purchase.aspose.com/buy).

### Q6: Můžu exportovat scénu do jiných formátů než OBJ?

A6: Ano, Aspose.3D podporuje mnoho formátů, například STL, FBX a GLTF. Stačí změnit hodnotu výčtu `FileFormat` v metodě `Save`.

### Q7: Jak změním počet řezů (slices) při vytahování?

A7: Upravením vlastnosti `Slices` v konstruktoru `LinearExtrusion` můžete ovlivnit hustotu sítě.

---

**Poslední aktualizace:** 2026-01-07  
**Testováno s:** Aspose.3D pro .NET nejnovější verze  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}