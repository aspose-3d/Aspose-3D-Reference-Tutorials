---
date: 2026-03-26
description: Naučte se, jak vytvořit válec a exportovat soubor OBJ pomocí Aspose.3D
  pro .NET. Tento průvodce vhodný pro začátečníky pokrývá nastavení 3D scény a export
  OBJ.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: Jak vytvořit válec se šikmým dnem – Aspose.3D pro .NET
url: /cs/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak vytvořit válec s roztaženým dnem – Aspose.3D pro .NET

## Úvod
Pokud se ptáte, **jak vytvořit válec** s přizpůsobeným roztaženým dnem v prostředí .NET, jste na správném místě. V tomto tutoriálu vás provedeme každým krokem — od nastavení 3‑D scény až po export finálního modelu jako souboru OBJ — abyste si mohli zlepšit své *základy 3D modelování* pomocí **Aspose.3D pro .NET**.

## Rychlé odpovědi
- **Jaká je hlavní třída pro zahájení 3D modelu?** `Scene` vytváří kořenový kontejner pro veškerou geometrii.  
- **Která metoda exportuje model do OBJ?** `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Potřebuji licenci pro testování?** K dispozici je bezplatná zkušební verze — viz odkaz na zkušební verzi v FAQ.  
- **Mohu změnit úhel roztažení?** Ano, upravte `ShearBottom` pomocí hodnoty `Vector2`.  
- **Je to vhodné pro začátečníky?** Rozhodně; API abstrahuje nízkoúrovňové zpracování mesh.

## Co je 3D scéna?
*3D scéna* je hierarchický kontejner, který obsahuje všechny geometrické entity, světla, kamery a transformace. V Aspose.3D třída `Scene` poskytuje čistý způsob, jak organizovat a později exportovat vaše modely.

## Proč exportovat do OBJ?
OBJ je široce podporovaný textový formát, který mohou importovat mnohé 3‑D aplikace (Blender, Maya, Unity). Export do OBJ vám umožní sdílet nebo dále upravovat vaše válecové modely mimo .NET.

## Požadavky
- Základní znalost C# a vývoje v .NET.  
- **Aspose.3D pro .NET** nainstalováno — můžete jej stáhnout **[zde](https://releases.aspose.com/3d/net/)**.  
- IDE pro .NET (Visual Studio, Rider nebo VS Code) připravené pro kódování.

## Importujte jmenné prostory
Nejprve přidejte požadované jmenné prostory do rozsahu, aby byly rozpoznány typy API.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Krok 1: Vytvořte 3D scénu
Objekt `Scene` funguje jako kořen vaší hierarchie modelu.

```csharp
Scene scene = new Scene();
```

## Krok 2: Vytvořte válec 1
Vytvoříme první válec s poloměrem 2, výškou 10 a 20 radiálními segmenty.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Krok 3: Přizpůsobte roztažené dno pro válec 1
Aplikujte transformaci roztažení, povolte generování fan‑cylindru a upravte další vlastnosti pro dosažení požadovaného tvaru.

```csharp
// Shear 47.5deg in the xy plane (z-axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## Krok 4: Přidejte válec 1 do scény
Umístěte první válec na vhodnou pozici pomocí transformačního posunu.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## Krok 5: Vytvořte válec 2
Druhý válec je vytvořen se stejnými základními rozměry, ale bez vlastního roztažení — ideální pro srovnání vedle sebe.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Krok 6: Přidejte válec 2 do scény
Jednoduše připojíme druhý válec ke grafu scény.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## Krok 7: Exportujte scénu jako soubor OBJ
Nakonec uložíme celou scénu do souboru OBJ, aby mohla být otevřena v libovolném standardním 3‑D prohlížeči.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## Časté problémy a řešení
| Problém | Proč k tomu dochází | Řešení |
|-------|----------------|-----|
| **OBJ soubor je prázdný** | Scéna nemá připojenou žádnou geometrii. | Ujistěte se, že oba válce jsou přidány do `scene.RootNode`. |
| **Roztažení vypadá špatně** | `ShearBottom` očekává tangens úhlu. | Použijte `Math.Tan(angleInRadians)` nebo hodnotu `0.83` pro ~47,5°. |
| **Chyby cesty k souboru** | Neplatný nebo chybějící adresář. | Použijte `Path.Combine(Environment.CurrentDirectory, "CustomizedShearBottomCylinder.obj")`. |

## Často kladené otázky
### Je Aspose.3D pro .NET vhodný pro začátečníky?
Rozhodně! Aspose.3D pro .NET nabízí vysoce úrovňové API, které abstrahuje matematicky náročné části 3‑D modelování, což jej činí přístupným pro vývojáře jakékoli úrovně.

### Mohu použít různé úhly roztažení na válcích?
Ano, každá instance `Cylinder` má svou vlastnost `ShearBottom`, takže můžete každému objektu přiřadit jedinečný úhel.

### Je k dispozici zkušební verze?
Ano, můžete si vyzkoušet bezplatnou zkušební verzi **[zde](https://releases.aspose.com/)**.

### Kde najdu další podporu?
Navštivte **[forum Aspose.3D](https://forum.aspose.com/c/3d/18)** pro komunitní pomoc, ukázky kódu a diskusi.

### Jak mohu získat dočasnou licenci?
Získejte svou dočasnou licenci **[zde](https://purchase.aspose.com/temporary-license/)**.

**Additional Q&A**

**Q: Jak exportuji model do jiného formátu, například STL?**  
A: Nahraďte `FileFormat.WavefrontOBJ` za `FileFormat.STL` v volání `scene.Save`.

**Q: Mohu animovat válce po jejich vytvoření?**  
A: Ano, můžete přidat animace klíčových snímků k transformacím uzlů pomocí tříd `Animation` poskytovaných Aspose.3D.

**Q: Podporuje API .NET Core?**  
A: Knihovna je plně kompatibilní s .NET Core, .NET 5+ a .NET 6+.

---

**Poslední aktualizace:** 2026-03-26  
**Testováno s:** Aspose.3D pro .NET (nejnovější verze)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}