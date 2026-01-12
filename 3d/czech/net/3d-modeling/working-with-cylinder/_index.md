---
date: 2026-01-12
description: Naučte se, jak vytvořit válec se šikmým dnem a jak exportovat 3D model
  ve formátu OBJ pomocí Aspose.3D pro .NET. Postupujte podle tohoto krok‑za‑krokem
  průvodce a ovládněte 3D modelování.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: Jak vytvořit střihový spodní válec pomocí Aspose.3D pro .NET
url: /cs/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Přizpůsobený válec se šikmým dnem

## Úvod
Vítejte v našem komplexním průvodci, kde **se naučíte vytvářet modely válců se šikmým dnem** pomocí Aspose.3D pro .NET. Ať už vytváříte herní asset, mechanickou součást nebo vizuální demo, tento tutoriál vám přesně ukáže, jak tvarovat dno válce, aplikovat šikmost a nakonec **exportovat 3D model OBJ** soubor pro použití v jakémkoli následném pipeline. Projděme si společně každý krok, abyste během několika minut mohli začít vytvářet vlastní geometrie.

## Rychlé odpovědi
- **Co je válec se šikmým dnem?** Válec, jehož spodní plocha je nakloněná (šikmá) místo rovné.  
- **Která knihovna se používá?** Aspose.3D pro .NET.  
- **Jak exportuji model?** Použijte `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Potřebuji licenci?** K dispozici je zkušební verze; pro produkční nasazení je vyžadována komerční licence.  
- **Jaké předpoklady jsou vyžadovány?** Vývojové prostředí .NET a NuGet balíček Aspose.3D.

## Co je válec se šikmým dnem?
Válec se šikmým dnem je standardní válcová síť, jejíž spodní plocha byla transformována operací šikmosti. To vám umožní vytvářet úhlové základny, rampy nebo vlastní spojky bez ruční úpravy vrcholů.

## Proč použít Aspose.3D pro tento úkol?
- **Plná kontrola** nad parametry geometrie (poloměr, výška, segmenty).  
- **Vestavěná podpora šikmosti** prostřednictvím vlastnosti `ShearBottom`, která vás ušetří od nízkoúrovňové manipulace s meshem.  
- **Export jedním kliknutím** do populárních formátů jako OBJ, FBX a STL, což usnadňuje integraci s ostatními nástroji.

## Předpoklady
Než se pustíme dál, ujistěte se, že máte:

- Základní znalosti C# a .NET.  
- Aspose.3D pro .NET nainstalováno. Můžete jej stáhnout **[zde](https://releases.aspose.com/3d/net/)**.  
- IDE kompatibilní s .NET (Visual Studio, Rider nebo VS Code).

## Importujte jmenné prostory
Ve vašem souboru C# začněte importováním potřebných jmenných prostorů:

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

## Krok 1: Vytvořte scénu
Nejprve vytvořte novou 3‑D scénu, která bude obsahovat všechny naše objekty.

```csharp
Scene scene = new Scene();
```

## Krok 2: Vytvořte válec 1
Vytvořte hlavní válec, který přizpůsobíme šikmým dnem.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Krok 3: Přizpůsobte šikmý dno pro válec 1
Aplikujte šikmost, povolte generování fan‑u a upravte další vlastnosti pro dosažení požadovaného tvaru.

```csharp
// Shear 47.5deg in the xy plane (z‑axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## Krok 4: Přidejte válec 1 do scény
Umístěte přizpůsobený válec do scény a posuňte jej mírně doprava, aby bylo možné vidět oba objekty vedle sebe.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## Krok 5: Vytvořte válec 2
Vytvořte druhý, jednoduchý válec pro srovnání.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Krok 6: Přidejte válec 2 do scény
Přidejte druhý válec bez jakékoli vlastní šikmosti — to pomůže ilustrovat efekt předchozích kroků.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## Krok 7: Uložte scénu
Nakonec exportujte celou scénu jako OBJ soubor, aby bylo možné jej otevřít v Blenderu, Maye nebo jakémkoli jiném 3‑D prohlížeči.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## Časté problémy a tipy
- **Hodnoty šikmosti**: `Vector2` přijímá faktory šikmosti X a Y. Hodnota `0.83` odpovídá přibližně 47,5°, ale můžete ji upravit pro různé úhly.  
- **Cesta exportu**: Ujistěte se, že složka, kterou zadáte, existuje a máte oprávnění k zápisu; jinak `scene.Save` vyhodí výjimku.  
- **Výkon**: Pro velmi vysoký počet segmentů válců zvažte snížení počtu segmentů (`20` v příkladu), aby velikost OBJ souboru zůstala zvládnutelná.

## Často kladené otázky

### Je Aspose.3D pro .NET vhodný pro začátečníky?
Rozhodně! Aspose.3D pro .NET nabízí uživatelsky přívětivé API, které je přístupné jak pro začátečníky, tak pro zkušené vývojáře.

### Mohu na válce použít různé úhly šikmosti?
Ano, můžete individuálně přizpůsobit `ShearBottom` pro každý válec, což vám umožní dosáhnout jedinečných efektů.

### Je k dispozici zkušební verze?
Ano, můžete si vyzkoušet bezplatnou zkušební verzi **[zde](https://releases.aspose.com/)**.

### Kde mohu najít další podporu?
Navštivte **[forum Aspose.3D](https://forum.aspose.com/c/3d/18)** pro komunitní podporu a diskuze.

### Jak mohu získat dočasnou licenci?
Získejte svou dočasnou licenci **[zde](https://purchase.aspose.com/temporary-license/)**.

**Další otázky a odpovědi**

**Q: Jak změním exportní formát na FBX?**  
A: Nahraďte `FileFormat.WavefrontOBJ` za `FileFormat.FBX` v volání `scene.Save`.

**Q: Můžu po exportu animovat válec?**  
A: OBJ nepodporuje animaci; použijte FBX nebo GLTF, pokud potřebujete animovaná data.

**Q: Co když potřebuji větší poloměr válce?**  
A: Upravit první dva parametry konstruktoru `Cylinder` (např. `new Cylinder(4, 4, …)`).

## Závěr
Nyní ovládáte, jak **vytvářet modely válců se šikmým dnem** a exportovat je jako OBJ soubory pomocí Aspose.3D pro .NET. Experimentujte s různými hodnotami šikmosti, počty segmentů a formáty exportu, aby vyhovovaly potřebám vašeho projektu. Šťastné modelování!

---

**Last Updated:** 2026-01-12  
**Testováno s:** Aspose.3D pro .NET 24.11 (nejnovější v době psaní)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}