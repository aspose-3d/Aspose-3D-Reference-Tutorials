---
date: 2026-03-23
description: Naučte se, jak vytvořit extruzi pomocí Aspose.3D pro .NET, převést 2D
  profily na 3D sítě a exportovat do formátu Wavefront OBJ. Postupujte podle tohoto
  průvodce krok za krokem.
linktitle: Performing Linear Extrusion
second_title: Aspose.3D .NET API
title: Jak vytvořit extruzi v Aspose.3D pro .NET – krok za krokem
url: /cs/net/3d-modeling/linear-extrusion/performing-linear-extrusion/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Provádění lineární extruze

## Úvod:

Vydejte se na vzrušující cestu do světa 3D grafiky s Aspose.3D pro .NET, mocným nástrojem, který posune vaše vývojářské dovednosti na vyšší úroveň. V tomto tutoriálu **se naučíte, jak vytvořit extruzi** – fascinující techniku, která promění 2‑D profil na plnohodnotnou 3‑D síť. Provedeme vás každým krokem, od instalace Aspose.3D po export výsledku jako soubor Wavefront OBJ, abyste s jistotou **vytvářeli 3D z 2D** tvarů.

## Rychlé odpovědi
- **Co je lineární extruze?** Rozšíření 2‑D tvaru podél přímé dráhy tak, aby vznikl 3‑D objekt.  
- **Kterou knihovnu tento tutoriál používá?** Aspose.3D pro .NET.  
- **Jak uložit OBJ?** Použijte `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Mohu exportovat Wavefront OBJ?** Ano – formát je plně podporován.  
- **Potřebuji licenci?** Dočasná licence stačí pro testování; pro produkci je vyžadována komerční licence.

## Požadavky:

Než se ponoříte do kouzelného světa 3D manipulace, ujistěte se, že máte připravené následující požadavky:

1. **Instalace Aspose.3D** – *nainstalujte aspose 3d*  
   - Začněte stažením a instalací Aspose.3D pro .NET z [těchto stránek](https://releases.aspose.com/3d/net/).  
   - Postupujte podle instalačních pokynů uvedených v dokumentaci [zde](https://reference.aspose.com/3d/net/).

2. **Nastavení vývojového prostředí**  
   - Zajistěte, aby vaše vývojové prostředí bylo správně nakonfigurováno s požadovanými jmennými prostory pro Aspose.3D.

Nyní, když jste připraveni, pojďme se ponořit do magie Aspose.3D!

## Importujte jmenné prostory:

Zahrňte nezbytné jmenné prostory pro zahájení vaší 3D dobrodružství:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Tyto jmenné prostory tvoří základ vašeho 3D programování a poskytují přístup k nástrojům potřebným pro plynulou integraci funkcí Aspose.3D.

## Provádění lineární extruze:

Vytvořme fascinující 3D objekt pomocí lineární extruze s Aspose.3D. Postupujte podle následujících kroků:

### Jak vytvořit extruzi – Krok 1: Inicializace základního profilu
```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

Tento krok nastaví 2‑D profil, který bude sloužit jako základ pro naše 3‑D mistrovské dílo. Podle potřeby upravte parametry, aby tvar a forma odpovídaly vašim představám.

### Jak vytvořit extruzi – Krok 2: Lineární extruze
```csharp
var extrusion = new LinearExtrusion(profile, 10) { Slices = 100, Center = true, Twist = 360, TwistOffset = new Vector3(10, 0, 0) };
```

Zde se provádí lineární extruze, která vezme 2‑D profil a prodlouží jej ve třetí dimenzi. Experimentujte s parametry jako **Slices**, **Twist** a **TwistOffset**, abyste **generovali 3D síťové** variace odpovídající vašemu designu.

### Jak vytvořit extruzi – Krok 3: Vytvoření scény
```csharp
Scene scene = new Scene();
```

Vytvoří se prázdné plátno – scéna, ve které váš 3‑D objekt ožije.

### Jak vytvořit extruzi – Krok 4: Přidání extruze do scény
```csharp
scene.RootNode.CreateChildNode(extrusion);
```

Vaše extrudované mistrovské dílo je přidáno jako podřízený uzel do scény.

### Jak vytvořit extruzi – Krok 5: Uložení 3D scény
```csharp
scene.Save(RunExamples.GetOutputFilePath("LinearExtrusion.obj"), FileFormat.WavefrontOBJ);
```

Nakonec **jak uložit OBJ** – výsledek uložíme do populárního formátu Wavefront OBJ, který lze otevřít v téměř všech 3‑D editorech.

Nyní se podívejte na svůj 3D zázrak!

## Proč je to důležité

Lineární extruze je rychlý způsob, jak **vytvořit 3D z 2D** skic, ideální pro rychlé prototypování, architektonické modelování nebo generování tisknutelných sítí. Ovládnutím této techniky získáte všestranný workflow, který šetří čas a snižuje potřebu složitých modelovacích nástrojů.

## Časté úskalí a tipy

- **Příliš vysoké hodnoty Twist** mohou způsobit samopřekrytí. Pro většinu jednoduchých tvarů udržujte twist pod 720°.  
- **Nedostatečný počet slices** může vést k hranatému vzhledu. Zvyšte vlastnost `Slices` pro hladší výsledek.  
- **Nezapomeňte nastavit `Center = true`**, pokud chcete, aby extruze byla centrovaná kolem počátku profilu – to často usnadní následné umístění.

## Závěr:

Gratulujeme! Právě jste se dotkli povrchu potenciálu Aspose.3D. Tento tutoriál jen naznačuje rozsáhlý svět, který na vás čeká. Prozkoumejte dokumentaci, experimentujte s různými tvary a odhalte plný rozsah možností s Aspose.3D pro .NET.

## Často kladené otázky:

### Q1: Je Aspose.3D vhodné pro začátečníky?
A1: Rozhodně! Aspose.3D nabízí uživatelsky přívětivé prostředí a náš tutoriál vás provede základy.

### Q2: Mohu používat Aspose.3D pro komerční projekty?
A2: Ano, Aspose.3D má licenční možnosti jak pro osobní, tak pro komerční použití. Podrobnosti najdete [zde](https://purchase.aspose.com/buy).

### Q3: Jak získám dočasné licence pro testování?
A3: Navštivte [tento odkaz](https://purchase.aspose.com/temporary-license/) pro získání dočasných licencí určených k testovacím účelům.

### Q4: Kde mohu najít komunitní podporu?
A4: Připojte se k [Aspose.3D fóru](https://forum.aspose.com/c/3d/18), kde můžete komunikovat s živou komunitou a získat pomoc.

### Q5: Je k dispozici bezplatná zkušební verze?
A5: Samozřejmě! Stáhněte si bezplatnou zkušební verzi [zde](https://releases.aspose.com/) a vyzkoušejte si schopnosti Aspose.3D na vlastní kůži.

---

**Poslední aktualizace:** 2026-03-23  
**Testováno s:** Aspose.3D pro .NET (nejnovější verze)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}