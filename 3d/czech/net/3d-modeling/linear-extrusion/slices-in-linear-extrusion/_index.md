---
date: 2026-03-23
description: Naučte se lineární extruzi s řezy pomocí Aspose.3D pro .NET. Vytvářejte
  podrobné 3D modely s krok‑za‑krokem ukázkami kódu.
linktitle: How to Linear Extrusion with Slices
second_title: Aspose.3D .NET API
title: Jak provést lineární extruzi s řezy pomocí Aspose.3D pro .NET
url: /cs/net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak provést Linear Extrusion s řezy pomocí Aspose.3D pro .NET

## Úvod

Vítejte ve světě 3D designu pomocí Aspose.3D pro .NET! V tomto tutoriálu objevíte **jak provést Linear Extrusion** s řezy, techniku, která vám umožní řídit úroveň detailu vašich modelů. Ať už jste zkušený vývojář nebo teprve začínáte, provedeme vás každým krokem, vysvětlíme, proč se daná akce provádí, a poskytneme praktické tipy, které můžete okamžitě použít.

## Rychlé odpovědi
- **Co je linear extrusion s řezy?** Jedná se o metodu rozšíření 2D profilu do 3D při specifikaci počtu mezilehlých průřezů (slices).  
- **Proč používat slices?** Více slices poskytuje hladší zakřivení; méně slices udržuje síť (mesh) lehkou.  
- **Požadavky?** Aspose.3D pro .NET, IDE kompatibilní s .NET a základní znalost C#.  
- **Typický čas běhu?** Ukázka běží za méně než sekundu na moderním PC.  
- **Výstupní formát?** Příklad ukládá do Wavefront OBJ, ale Aspose.3D podporuje mnoho formátů.

## Co je Linear Extrusion s řezy?

Linear extrusion vezme 2‑D tvar (profil) a protáhne jej podél přímky, čímž vytvoří 3‑D těleso. Vlastnost **Slices** určuje, kolik mezilehlých průřezů je vloženo mezi začátek a konec extruze, což ovlivňuje hladkost a počet polygonů.

## Proč používat slices v Linear Extrusion?

- **Kontrola hustoty mesh:** Jemně doladit rovnováhu mezi vizuální kvalitou a velikostí souboru.  
- **Optimalizace výkonu:** Použijte méně slices pro aplikace v reálném čase, více pro renderování ve vysokém rozlišení.  
- **Tvůrčí flexibilita:** Kombinujte různé počty slices na samostatných objektech, aby byl zdůrazněn záměr designu.

## Požadavky

Než se pustíte do práce, ujistěte se, že máte:

- Aspose.3D pro .NET knihovnu – stáhněte ji [zde](https://releases.aspose.com/3d/net/).  
- IDE, které podporuje C# (Visual Studio, Rider, VS Code, atd.).  
- Základní znalost syntaxe C# a objektově orientovaných konceptů.  
- Zvídavost experimentovat s 3‑D geometrií!

## Importování jmenných prostorů

Nejprve importujte jmenné prostory, které vám poskytují přístup k základním třídám Aspose.3D.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Postupný návod

### Krok 1: Inicializace základního profilu

Začínáme s jednoduchým obdélníkovým tvarem a přidáváme mu malý poloměr zaoblení, aby hrany nebyly dokonale ostré.

```csharp
// ExStart:InitializeBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd:InitializeBaseProfile
```

### Krok 2: Vytvoření 3D scény

`Scene` funguje jako kontejner pro všechny uzly, sítě (meshes), světla a kamery.

```csharp
// ExStart:Create3DScene
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### Krok 3: Přidání levých a pravých uzlů

Vytvoříme dva sourozenecké uzly pod kořenem scény. Levý uzel dostane nízký počet slices, pravý uzel vysoký počet slices, abyste mohli porovnat vizuální rozdíl.

```csharp
// ExStart:CreateLeftRightNodes
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### Krok 4: Provedení Linear Extrusion na levém uzlu (nízký detail)

Zde extrahujeme obdélník pouze s **2 slices**. To vytvoří hrubou síť – ideální pro rychlé náhledy.

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### Krok 5: Provedení Linear Extrusion na pravém uzlu (vysoký detail)

Nyní použijeme **10 slices** pro mnohem hladší výsledek. Všimněte si, jak se geometrie stává jemnější.

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### Krok 6: Uložení 3D scény

Nakonec zapíšete scénu do souboru OBJ. Nahraďte `"Your Output Directory"` platnou cestou na vašem počítači.

```csharp
// ExStart:Save3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
// ExEnd:Save3DScene
```

## Časté problémy a řešení

| Problém | Proč se to děje | Řešení |
|-------|----------------|-----|
| **Soubor nebyl vytvořen** | Cesta k výstupu je neplatná nebo chybí oprávnění k zápisu. | Použijte absolutní cestu a ujistěte se, že složka existuje. |
| **Objekt vypadá plochý** | `Slices` nastaveno na 1 nebo 0. | Nastavte `Slices` alespoň na 2 pro viditelnou extruzi. |
| **Neočekávaná geometrie** | Poloměr zaoblení je příliš velký pro velikost obdélníku. | Upravte `RoundingRadius` na hodnotu menší než polovina nejmenší strany obdélníku. |

## Často kladené otázky

**Q: Mohu změnit směr extruze?**  
A: Ano. Použijte vlastnost `Transform` na uzlu k otočení nebo posunutí extrudované geometrie před uložením.

**Q: Podporuje Aspose.3D jiné typy extruze?**  
A: Rozhodně. Kromě `LinearExtrusion` můžete použít `RevolveExtrusion`, `SweepExtrusion` a další.

**Q: Do jakých souborových formátů mohu exportovat?**  
A: Aspose.3D podporuje OBJ, STL, FBX, 3MF, Collada a mnoho dalších. Stačí změnit výčtový typ `FileFormat`.

**Q: Existuje způsob, jak programově nastavit materiál?**  
A: Ano. Po vytvoření uzlu přiřaďte `Material` do jeho kolekce `Entity`.

**Q: Jak počet slices ovlivňuje využití paměti?**  
A: Více slices zvyšuje počet vrcholů a ploch, což úměrně zvyšuje spotřebu paměti. Použijte profilování k nalezení optimálního počtu pro vaši cílovou platformu.

## Původní FAQ

### Q1: Mohu použít Aspose.3D pro .NET s jinými programovacími jazyky?

A1: Aspose.3D je primárně navrženo pro .NET, ale můžete prozkoumat možnosti interoperability s jazyky jako Python pomocí .NET vazeb.

### Q2: Kde mohu najít podrobnou dokumentaci pro Aspose.3D pro .NET?

A2: Odkazujte se na dokumentaci [zde](https://reference.aspose.com/3d/net/) pro podrobné informace o možnostech a použití Aspose.3D.

### Q3: Je k dispozici bezplatná zkušební verze Aspose.3D pro .NET?

A3: Ano, můžete získat bezplatnou zkušební verzi [zde](https://releases.aspose.com/) a prozkoumat funkce knihovny před zakoupením.

### Q4: Jak mohu získat technickou podporu pro Aspose.3D pro .NET?

A4: Navštivte fórum Aspose.3D [zde](https://forum.aspose.com/c/3d/18), kde můžete požádat o pomoc a zapojit se do komunity.

### Q5: Mohu použít dočasnou licenci pro Aspose.3D pro .NET?

A5: Ano, získáte dočasnou licenci [zde](https://purchase.aspose.com/temporary-license/) pro evaluační účely.

## Závěr

Nyní jste viděli **jak provést Linear Extrusion** s řezy pomocí Aspose.3D pro .NET, prozkoumali dopad různých počtů slices a naučili se, jak exportovat svou práci. Experimentujte s dalšími profily, hrajte si s hodnotou `Slices` a integrujte materiály nebo světla k vytvoření produkčně připravených 3‑D assetů.

---

**Poslední aktualizace:** 2026-03-23  
**Testováno s:** Aspose.3D 24.11 for .NET (latest at time of writing)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}