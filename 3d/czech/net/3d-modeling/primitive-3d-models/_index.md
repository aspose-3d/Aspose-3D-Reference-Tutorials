---
date: 2026-01-09
description: Naučte se, jak vytvářet 3D modely krabicových primitiv a jak ukládat
  FBX pomocí Aspose.3D pro .NET. Exportujte 3D modely do FBX bez námahy.
linktitle: How to Create Box Primitive 3D Model with Aspose.3D
second_title: Aspose.3D .NET API
title: Jak vytvořit primitivní 3D model krabice pomocí Aspose.3D
url: /cs/net/3d-modeling/primitive-3d-models/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Vytváření primitivních 3D modelů

## Úvod

Vítejte ve vzrušujícím světě 3D modelování s Aspose.3D pro .NET! V tomto komplexním tutoriálu vám ukážeme **jak vytvořit krabici** primitivní 3D modely, projdeme kroky **jak uložit FBX** a poskytneme vám jistotu **exportovat 3D model FBX** soubory pro použití v jakémkoli pipeline. Ať už jste zkušený vývojář nebo teprve začínáte, najdete jasné, akční pokyny, které můžete okamžitě použít.

## Rychlé odpovědi
- **Jaký je hlavní cíl?** Naučte se, jak vytvořit primitivní 3D modely krabice s Aspose.3D.  
- **Jaký formát se používá pro export?** Formát FBX (FileFormat.FBX7500ASCII).  
- **Potřebuji licenci?** K dispozici je bezplatná zkušební verze; licence je vyžadována pro produkční použití.  
- **Jaké prostředí je vyžadováno?** Jakékoli .NET vývojové prostředí kompatibilní s Aspose.3D.  
- **Jak dlouho to trvá?** Přibližně 10‑15 minut na vytvoření základní scény.

## Co je primitivní 3D model?

Primitivní 3D model je základní geometrický tvar – například krabice, koule nebo válec – používaný jako stavební blok pro složitější scény. Aspose.3D poskytuje připravené třídy, které vám umožní vytvořit tyto tvary jediným řádkem kódu.

## Proč používat Aspose.3D pro .NET?

- **Renderování bez závislostí** – není vyžadován žádný externí grafický engine.  
- **Bohatá podpora formátů** – export přímo do FBX, OBJ, STL a dalších.  
- **Plná integrace s .NET** – funguje s .NET Framework, .NET Core a .NET 5/6+.  

## Předpoklady

Než se ponoříme do fascinujícího světa 3D modelování, ujistěte se, že máte následující předpoklady:

- Aspose.3D pro .NET: Stáhněte a nainstalujte knihovnu Aspose.3D pro .NET z [odkazu ke stažení](https://releases.aspose.com/3d/net/).

- Vývojové prostředí: Nastavte .NET vývojové prostředí a zajistěte kompatibilitu s Aspose.3D.

Nyní, když máte vše potřebné, pojďme se vydat na cestu k vytváření primitivních 3D modelů krok za krokem.

## Importování jmenných prostorů

Začněte importováním potřebných jmenných prostorů pro přístup k funkcionalitě poskytované Aspose.3D:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```

S těmito jmennými prostory jste připraveni uvolnit sílu Aspose.3D ve vaší .NET aplikaci.

## Jak vytvořit primitivní 3D model krabice

### Krok 1: Inicializace objektu Scene

```csharp
// Initialize a Scene object
Scene scene = new Scene();
```

Vytvořte nový objekt scény, který slouží jako plátno pro vaše 3D mistrovské dílo.

### Krok 2: Vytvoření modelu krabice

```csharp
// Create a Box model
scene.RootNode.CreateChildNode("box", new Box());
```

Přidejte model krabice do kořene vaší scény. Toto je jádro **jak vytvořit krabici** geometrie. V případě potřeby můžete později upravit její rozměry.

### Krok 3: Vytvoření modelu válce

```csharp
// Create a Cylinder model
scene.RootNode.CreateChildNode("cylinder", new Cylinder());
```

Vylepšete svou scénu přidáním modelu válce. Upravte jeho parametry, aby dosáhl požadovaného tvaru a velikosti.

### Krok 4: Uložení výkresu ve formátu FBX (Jak uložit FBX)

```csharp
// Save drawing in the FBX format
var output = "Your Output Directory" + "test.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Zde ukazujeme **jak uložit FBX** – scéna je exportována jako soubor FBX, který můžete importovat do většiny 3D nástrojů. Tento krok také ukazuje, jak **exportovat 3D model FBX** pro následné pracovní postupy.

### Krok 5: Zobrazení úspěšné zprávy

```csharp
// Display success message
Console.WriteLine("\nBuilding a scene from primitive 3D models successfully.\nFile saved at " + output);
```

Oslavte svůj úspěch! Scéna byla úspěšně vytvořena z primitivních 3D modelů a soubor byl uložen.

## Časté problémy a řešení
- **Cesta k výstupu nebyla nalezena** – Ujistěte se, že adresář, který zadáte v `output`, existuje, nebo použijte `Path.Combine` s `Environment.CurrentDirectory`.  
- **Výjimka licence** – Pro produkční použití je vyžadována platná licence Aspose.3D; bezplatná zkušební verze funguje pro hodnocení.  
- **Nesprávná verze FBX** – Kód používá `FBX7500ASCII`; přepněte na jinou hodnotu výčtu `FileFormat`, pokud potřebujete jinou verzi.

## Často kladené otázky

### Q1: Mohu použít Aspose.3D pro .NET s jinými programovacími jazyky?

A1: Aspose.3D primárně podporuje .NET, ale jsou k dispozici i jiné verze pro Javu a další platformy.

### Q2: Je k dispozici bezplatná zkušební verze?

A2: Ano, můžete prozkoumat možnosti Aspose.3D pomocí [bezplatné zkušební verze](https://releases.aspose.com/).

### Q3: Kde mohu najít podporu pro Aspose.3D pro .NET?

A3: Navštivte [forum Aspose.3D](https://forum.aspose.com/c/3d/18) pro komunitní podporu a diskuse.

### Q4: Jak mohu získat dočasnou licenci?

A4: Dočasnou licenci můžete získat [zde](https://purchase.aspose.com/temporary-license/).

### Q5: Existují nějaké ukázkové tutoriály?

A5: Ano, prozkoumejte další tutoriály a příklady v [dokumentaci](https://reference.aspose.com/3d/net/).

## Často kladené otázky

**Q: Mohu exportovat scénu do jiných formátů než FBX?**  
A: Ano, Aspose.3D podporuje OBJ, STL, 3MF a mnoho dalších. Stačí změnit výčet `FileFormat` při volání `scene.Save()`.

**Q: Je možné přizpůsobit rozměry krabice?**  
A: Rozhodně. Použijte konstruktor `Box(double width, double height, double depth)` k nastavení vlastních rozměrů.

**Q: Potřebuji 64‑bitový OS pro spuštění exportovaného FBX souboru?**  
A: Ne, FBX soubor je platformně nezávislý; může jej otevřít jakýkoli moderní 3D prohlížeč.

**Q: Jak přidám materiály nebo textury k primitivům?**  
A: Vytvořte objekt `Material`, přiřaďte jej k vlastnosti `Material` uzlu a případně nastavte mapy textur.

## Závěr

Gratulujeme! Úspěšně jste se naučili **jak vytvořit krabici** primitivní 3D modely, uložili je jako FBX soubor a prozkoumali způsoby **exportovat 3D model FBX** pro další použití. Tento průvodce pokryl základy, ale možnosti jsou neomezené. Ponořte se hlouběji do [dokumentace](https://reference.aspose.com/3d/net/), abyste objevili pokročilé funkce jako osvětlení, animace a komplexní manipulaci s meshem.

---

**Last Updated:** 2026-01-09  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}