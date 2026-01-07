---
date: 2026-01-07
description: Naučte se, jak lineárně extrudovat 2D profil a exportovat 3D model ve
  formátu OBJ pomocí Aspose.3D pro .NET. Tento tutoriál o lineární extruzi vás provede
  krok za krokem.
linktitle: Performing Linear Extrusion
second_title: Aspose.3D .NET API
title: Jak lineárně extrudovat pomocí Aspose.3D pro .NET
url: /cs/net/3d-modeling/linear-extrusion/performing-linear-extrusion/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak provést lineární extruzi pomocí Aspose.3D pro .NET

## Úvod

Vítejte v našem **návodu na lineární extruzi**! V tomto průvodci se dozvíte, **jak provést lineární extruzi** 2‑D profilu a proměnit jej na plnohodnotný 3‑D objekt pomocí Aspose.3D pro .NET. Ať už vytváříte aplikaci ve stylu CAD, nebo jen potřebujete **export 3d model obj** soubory pro další zpracování, tento krok‑za‑krokem návod vám dodá jistotu přidat výkonné vytváření geometrie do vašich projektů.

## Rychlé odpovědi
- **Co je lineární extruze?** Rozšíření 2‑D tvaru podél přímé dráhy za účelem vytvoření 3‑D tělesa.  
- **Kterou knihovnu používáme?** Aspose.3D pro .NET.  
- **Potřebuji licenci?** Dočasná licence stačí pro testování; plná licence je vyžadována pro produkci.  
- **Mohu exportovat do OBJ?** Ano – finální scéna je uložena jako soubor Wavefront OBJ.  
- **Kolik řádků kódu?** Méně než 30 řádků C# plus vysvětlující komentáře.

## Co je lineární extruze?

Lineární extruze vezme plochý profil (např. obdélník nebo kruh) a provede jej podél přímé čáry, přičemž lze volitelně přidat otáčení, škálování nebo posuny. Výsledkem je těleso, které lze renderovat, upravovat nebo exportovat pro použití v jiných 3‑D nástrojích.

## Proč použít Aspose.3D pro lineární extruzi?

* **Zero‑dependency:** Není potřeba externí CAD jádra.  
* **Plná podpora .NET:** Funguje s .NET Framework, .NET Core i .NET 5/6+.  
* **Flexibilita exportu:** Přímé uložení do OBJ, STL, FBX a mnoha dalších formátů.  
* **Bohaté API:** Ovládejte řezy, otáčení a posuny pomocí několika vlastností.

## Předpoklady

Než začnete, ujistěte se, že máte:

1. **Aspose.3D nainstalováno** – stáhněte jej z [zde](https://releases.aspose.com/3d/net/).  
2. **Přístup k dokumentaci** – postupujte podle průvodce nastavením [zde](https://reference.aspose.com/3d/net/).  
3. Vývojové prostředí .NET (Visual Studio, VS Code nebo Rider) s potřebnými jmennými prostory zahrnutými.

## Import jmenných prostorů

Zahrňte nezbytné jmenné prostory pro odemknutí funkčnosti Aspose.3D:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Tyto jmenné prostory vám poskytují přístup k `Scene`, `LinearExtrusion`, `RectangleShape` a pomocným třídám jako `Vector3`.

## Provádění lineární extruze

Níže je kompletní pracovní postup. Každý krok je vysvětlen běžným jazykem před odpovídajícím blokem kódu, takže můžete postupovat bez hádání, co kód dělá.

### Krok 1: Inicializace základního profilu

Nejprve vytvořte 2‑D tvar, který bude extrudován. V tomto příkladu používáme obdélník s malým poloměrem zaoblení.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

*Proč je to důležité:* Profil určuje průřez finálního 3‑D objektu. Upravením `RoundingRadius`, šířky nebo výšky získáte různé siluety.

### Krok 2: Aplikace lineární extruze

Nyní profil protáhneme o 10 jednotek podél osy Z, přidáme 100 řezů pro hladkost, vycentrujeme geometrii a použijeme plný 360° otáčivý twist s posunem.

```csharp
var extrusion = new LinearExtrusion(profile, 10) { Slices = 100, Center = true, Twist = 360, TwistOffset = new Vector3(10, 0, 0) };
```

*Tip:* Experimentujte s `Slices`, abyste našli rovnováhu mezi výkonem a vizuální kvalitou, a vyzkoušejte `Twist` pro spirálové efekty.

### Krok 3: Vytvoření scény

`Scene` funguje jako kontejner pro všechny 3‑D entity – představte si ji jako plátno.

```csharp
Scene scene = new Scene();
```

### Krok 4: Přidání extruze do scény

Připojte extrudovanou geometrii ke kořenovému uzlu scény, aby se stala součástí renderovatelné hierarchie.

```csharp
scene.RootNode.CreateChildNode(extrusion);
```

### Krok 5: Uložení 3‑D modelu

Nakonec exportujte scénu do široce podporovaného OBJ souboru. Tím demonstrujeme schopnost **export 3d model obj** v Aspose.3D.

```csharp
scene.Save(RunExamples.GetOutputFilePath("LinearExtrusion.obj"), FileFormat.WavefrontOBJ);
```

Když otevřete výsledný `LinearExtrusion.obj` v libovolném 3‑D prohlížeči, uvidíte zkroucený obdélníkový hranol – právě to, co kód popisuje.

## Časté problémy a tipy

| Problém | Proč se vyskytuje | Jak opravit |
|---------|-------------------|-------------|
| **Profil není viditelný** | Zapomněli jste přidat extruzi do scény. | Ujistěte se, že je voláno `CreateChildNode`. |
| **Twist vypadá plochý** | `Slices` je příliš nízký, což vede k hrubé geometrii. | Zvyšte `Slices` (např. na 200) pro hladší twist. |
| **Export selže** | Výstupní složka neexistuje nebo chybí oprávnění k zápisu. | Použijte `RunExamples.GetOutputFilePath` nebo vytvořte složku ručně. |
| **Neočekávané škálování** | `Center` nastaven na `false` posouvá geometrii. | Nastavte `Center = true`, pokud nepotřebujete posun. |

## Často kladené otázky

### Q1: Je Aspose.3D vhodné pro začátečníky?

A1: Rozhodně! Aspose.3D nabízí uživatelsky přívětivé API a tento návod vás provede základy lineární extruze.

### Q2: Mohu Aspose.3D použít v komerčních projektech?

A2: Ano, Aspose.3D má licenční možnosti pro osobní i komerční použití. Podrobnosti najdete [zde](https://purchase.aspose.com/buy).

### Q3: Jak získám dočasné licence pro testování?

A3: Navštivte [tento odkaz](https://purchase.aspose.com/temporary-license/) a získejte dočasné licence pro testovací účely.

### Q4: Kde najdu komunitní podporu?

A4: Připojte se k [Aspose.3D fóru](https://forum.aspose.com/c/3d/18), kde můžete získat pomoc od aktivní komunity.

### Q5: Je k dispozici bezplatná zkušební verze?

A5: Samozřejmě! Stáhněte si bezplatnou zkušební verzi [zde](https://releases.aspose.com/) a vyzkoušejte schopnosti Aspose.3D na vlastní kůži.

---

**Poslední aktualizace:** 2026-01-07  
**Testováno s:** Aspose.3D 24.11 pro .NET  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}