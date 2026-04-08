---
date: 2026-04-08
description: Naučte se, jak přidat kameru do scény a exportovat scénu jako FBX pomocí
  Aspose.3D pro .NET – krok za krokem průvodce nastavením cílů kamery a tvorbou 3D
  animací.
keywords:
- add camera to scene
- set camera target
- export scene as fbx
- how to add camera
- position camera in 3d
linktitle: Přidat kameru do scény a nastavit cíle pro 3D animaci
second_title: Aspose.3D .NET API
title: Přidejte kameru do scény a nastavte cíle pro 3D animaci
url: /cs/net/animation/setup-target-camera/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Přidání kamery do scény a nastavení cílů pro 3D animaci

## Úvod

Pokud vytváříte 3D animaci, první věc, kterou potřebujete, je dobře umístěná kamera. V tomto tutoriálu se naučíte **how to add camera to scene**, definovat její cíl a nakonec **export scene as FBX** pomocí Aspose.3D pro .NET. Provedeme vás každým krokem, vysvětlíme, proč je důležitý, a poskytneme praktické tipy, abyste mohli s jistotou vytvářet poutavé 3D animace. Na konci také pochopíte, jak **position camera in 3d** prostoru pro optimální zarámování.

## Rychlé odpovědi
- **Jaký je první krok k přidání kamery?** Inicializujte objekt `Scene`, který bude hostovat uzel kamery.  
- **Jaký formát souboru se používá pro export v tomto průvodci?** FBX (`.fbx`).  
- **Potřebuji licenci pro spuštění ukázkového kódu?** Bezplatná zkušební verze funguje pro hodnocení; pro produkci je vyžadována komerční licence.  
- **Jaké verze .NET jsou podporovány?** .NET Framework 4.5+, .NET Core 3.1+, .NET 5/6+.  
- **Mohu změnit pozici kamery po vytvoření?** Ano – upravte `cameraNode.Transform.Translation` kdykoli.

## Co je **add camera to scene**?
Přidání kamery do scény znamená vytvořit entitu `Camera`, připojit ji k uzlu ve scénovém grafu a umístit ji tak, aby „pohlížela“ na cílový bod. Tím se určuje perspektiva diváka při renderování nebo exportu scény.

## Proč nastavit cíle kamery a exportovat jako FBX?
- **Kontrola úhlu pohledu** – přesné umístění kamery vám umožní zarámovat animaci přesně tak, jak si představujete.  
- **Interoperabilita** – FBX je široce podporován herními enginy, Maya, Blender a dalšími 3D nástroji, což usnadňuje sdílení assetů.  
- **Znovupoužitelné assety** – jakmile jsou kamera a její cíl uloženy, můžete scénu použít v několika projektech.

## Běžné případy použití
- **Kinematické přechodové scény** ve hrách, kde pevná kamera sleduje postavu.  
- **Produktové vizualizace**, kde potřebujete stabilní úhel pohledu pro předvedení modelu z různých úhlů.  
- **Pre‑vizualizace** pro filmové nebo AR/VR projekty, umožňující designérům iterovat umístění kamery před finálním renderováním.

## Požadavky

Před ponořením se do tutoriálu se ujistěte, že máte následující požadavky:

- Základní znalost C# a .NET frameworku.  
- Nainstalovaná knihovna Aspose.3D pro .NET. Můžete si ji stáhnout [zde](https://releases.aspose.com/3d/net/).  
- Vývojové prostředí připravené na 3D programování.

## Importování jmenných prostorů

Pro zahájení procesu importujte potřebné jmenné prostory do svého projektu. Tyto jmenné prostory jsou nezbytné pro využití síly Aspose.3D pro .NET:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

## Průvodce krok za krokem

### Krok 1: Inicializace objektu Scene

Začněte inicializací objektu scény. Tento slouží jako plátno, kde vaše 3D animace ožije.

```csharp
// ExStart:SetupTargetAndCamera
// Initialize scene object
Scene scene = new Scene();
```

### Krok 2: Vytvoření uzlu kamery

Dále vytvořte podřízený uzel, který bude obsahovat kameru. Pojmenování uzlu smysluplně pomáhá udržet hierarchii scény uspořádanou.

```csharp
// Get a child node object
Node cameraNode = scene.RootNode.CreateChildNode("camera", new Camera());
```

### Krok 3: Umístění kamery

Zadejte translaci pro uzel kamery. To určuje počáteční pozici kamery ve 3D prostoru. Upravit hodnoty `Vector3` pro **position camera in 3d** podle potřeby pro váš záběr.

```csharp
// Set camera node translation
cameraNode.Transform.Translation = new Vector3(100, 20, 0);
```

### Krok 4: Definování cíle kamery

Kamera potřebuje cílový bod, na který se dívá. Vytvoříme další podřízený uzel, který funguje jako ohniskový bod, a přiřadíme jej k vlastnosti `Target` kamery. Takto **set camera target** pro stabilní pohled.

```csharp
cameraNode.GetEntity<Camera>().Target = scene.RootNode.CreateChildNode("target");
```

### Krok 5: Uložení nakonfigurované scény

Nakonec exportujte scénu do souboru FBX (nebo jakéhokoli jiného podporovaného formátu). Nahraďte `"Your Output Directory"` skutečnou cestou, kam chcete soubor uložit.

```csharp
var output = "Your Output Directory" + "camera-test.fbx";
scene.Save(output);
```

## Běžné problémy a řešení

| Problém | Řešení |
|-------|----------|
| **Kamera se zobrazuje pod špatným úhlem** | Ověřte, že cílový uzel je umístěn tam, kde očekáváte. Můžete také nastavit `cameraNode.GetEntity<Camera>().UpVector` pro kontrolu orientace. |
| **Exportovaný FBX se neotevírá v jiných nástrojích** | Ujistěte se, že používáte aktuální verzi Aspose.3D (knihovna automaticky zapisuje kompatibilní verzi FBX). |
| **Chyba 'cesta nenalezena' při `scene.Save`** | Použijte absolutní cestu nebo se ujistěte, že výstupní adresář existuje před voláním `Save`. |

## Často kladené otázky

**Q: Je Aspose.3D kompatibilní s jinými 3D modelovacími nástroji?**  
A: Aspose.3D podporuje různé formáty souborů, což zajišťuje kompatibilitu s populárními 3D modelovacími nástroji.

**Q: Mohu použít Aspose.3D pro vývoj her?**  
A: Rozhodně! Aspose.3D umožňuje vývojářům snadno vytvářet 3D assety pro hry.

**Q: Kde mohu najít další podporu pro Aspose.3D?**  
A: Navštivte [Aspose.3D fórum](https://forum.aspose.com/c/3d/18) pro komunitní podporu a diskuse.

**Q: Je k dispozici bezplatná zkušební verze?**  
A: Ano, můžete si vyzkoušet bezplatnou verzi [zde](https://releases.aspose.com/).

**Q: Jak získám dočasnou licenci?**  
A: Získejte dočasnou licenci [zde](https://purchase.aspose.com/temporary-license/).

## Závěr

Nyní jste se naučili, jak **add camera to scene**, nastavit její cíl a exportovat výsledek jako soubor FBX pomocí Aspose.3D pro .NET. S těmito základy můžete začít vytvářet bohatší animace, experimentovat s více kamerami a integrovat exportované scény do herních enginů nebo pipeline vizuálních efektů.

---

**Poslední aktualizace:** 2026-04-08  
**Testováno s:** Aspose.3D 24.11 for .NET (latest at time of writing)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}