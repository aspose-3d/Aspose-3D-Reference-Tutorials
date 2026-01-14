---
date: 2026-01-14
description: Naučte se, jak přidat kameru do scény a exportovat scénu jako FBX pomocí
  Aspose.3D pro .NET – krok za krokem průvodce nastavením cílů kamery a vytvářením
  3D animací.
linktitle: Add Camera to Scene and Set Up Targets for 3D Animation
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

Pokud vytváříte 3D animaci, první věc, kterou potřebujete, je dobře umístěná kamera. V tomto tutoriálu se naučíte **jak přidat kameru do scény**, definovat její cíl a nakonec **exportovat scénu jako FBX** pomocí Aspose.3D pro .NET. Provedeme vás každým krokem, vysvětlíme, proč je to důležité, a poskytneme praktické tipy, abyste mohli s jistotou vytvářet poutavé 3D animace.

## Rychlé odpovědi
- **Jaký je první krok pro přidání kamery?** Inicializujte objekt `Scene`, který bude hostovat uzel kamery.  
- **Jaký formát souboru se používá pro export v tomto průvodci?** FBX (`.fbx`).  
- **Potřebuji licenci pro spuštění ukázkového kódu?** Bezplatná zkušební verze stačí pro hodnocení; pro produkci je vyžadována komerční licence.  
- **Jaké verze .NET jsou podporovány?** .NET Framework 4.5+, .NET Core 3.1+, .NET 5/6+.  
- **Mohu změnit pozici kamery po jejím vytvoření?** Ano – kdykoli můžete upravit `cameraNode.Transform.Translation`.

## Co je **add camera to scene**?
Přidání kamery do scény znamená vytvoření entity `Camera`, připojení k uzlu ve scénovém grafu a umístění tak, aby „směřovala“ na cílový bod. Tím se určuje perspektiva pozorovatele při renderování nebo exportu scény.

## Proč nastavit cíle kamery a exportovat jako FBX?
- **Ovládání úhlu pohledu** – přesné umístění kamery vám umožní zarámovat animaci přesně tak, jak si představujete.  
- **Interoperabilita** – FBX je široce podporován herními enginy, Maya, Blender a dalšími 3D nástroji, což usnadňuje sdílení aktiv.  
- **Znovupoužitelné assety** – jakmile jsou kamera a její cíl uloženy, můžete scénu znovu použít v několika projektech.

## Předpoklady

Než se ponoříte do tutoriálu, ujistěte se, že máte následující předpoklady:

- Základní znalost C# a .NET frameworku.  
- Knihovna Aspose.3D pro .NET nainstalována. Můžete si ji stáhnout [zde](https://releases.aspose.com/3d/net/).  
- Vývojové prostředí připravené pro 3D programování.

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

Začněte inicializací objektu scény. Slouží jako plátno, na kterém vaše 3D animace ožije.

```csharp
// ExStart:SetupTargetAndCamera
// Initialize scene object
Scene scene = new Scene();
```

### Krok 2: Vytvoření uzlu kamery

Dále vytvořte podřízený uzel, který bude držet kameru. Pojmenování uzlu smysluplně pomáhá udržet hierarchii scény uspořádanou.

```csharp
// Get a child node object
Node cameraNode = scene.RootNode.CreateChildNode("camera", new Camera());
```

### Krok 3: Umístění kamery

Určete translaci pro uzel kamery. To určuje počáteční pozici kamery ve 3D prostoru.

```csharp
// Set camera node translation
cameraNode.Transform.Translation = new Vector3(100, 20, 0);
```

### Krok 4: Definování cíle kamery

Kamera potřebuje cílový bod, na který se dívá. Vytvoříme další podřízený uzel, který funguje jako ohniskový bod, a přiřadíme jej k vlastnosti `Target` kamery.

```csharp
cameraNode.GetEntity<Camera>().Target = scene.RootNode.CreateChildNode("target");
```

### Krok 5: Uložení nakonfigurované scény

Nakonec exportujte scénu do souboru FBX (nebo jakéhokoli jiného podporovaného formátu). Nahraďte `"Your Output Directory"` skutečnou cestou, kam chcete soubor uložit.

```csharp
var output = "Your Output Directory" + "camera-test.fbx";
scene.Save(output);
```

## Časté problémy a řešení

| Problém | Řešení |
|-------|----------|
| **Kamera se zobrazuje pod špatným úhlem** | Ověřte, že cílový uzel je umístěn tam, kde očekáváte. Můžete také nastavit `cameraNode.GetEntity<Camera>().UpVector` pro kontrolu orientace. |
| **Exportovaný FBX se neotevírá v jiných nástrojích** | Ujistěte se, že používáte aktuální verzi Aspose.3D (knihovna automaticky zapisuje kompatibilní verzi FBX). |
| **Chyba 'cesta nenalezena' při `scene.Save`** | Použijte absolutní cestu nebo se ujistěte, že výstupní adresář existuje před voláním `Save`. |

## Často kladené otázky

### Q1: Je Aspose.3D kompatibilní s jinými 3D modelovacími nástroji?

A1: Aspose.3D podporuje různé formáty souborů, což zajišťuje kompatibilitu s populárními 3D modelovacími nástroji.

### Q2: Mohu použít Aspose.3D pro vývoj her?

A2: Rozhodně! Aspose.3D umožňuje vývojářům snadno vytvářet 3D assety pro hry.

### Q3: Kde mohu najít další podporu pro Aspose.3D?

A3: Navštivte [forum Aspose.3D](https://forum.aspose.com/c/3d/18) pro komunitní podporu a diskuze.

### Q4: Je k dispozici bezplatná zkušební verze?

A4: Ano, můžete vyzkoušet bezplatnou verzi [zde](https://releases.aspose.com/).

### Q5: Jak získám dočasnou licenci?

A5: Získejte dočasnou licenci [zde](https://purchase.aspose.com/temporary-license/).

## Závěr

Nyní jste se naučili, jak **přidat kameru do scény**, nastavit její cíl a exportovat výsledek jako soubor FBX pomocí Aspose.3D pro .NET. S těmito základy můžete začít vytvářet bohatší animace, experimentovat s více kamerami a integrovat exportované scény do herních enginů nebo pipeline vizuálních efektů.

---

**Last Updated:** 2026-01-14  
**Testováno s:** Aspose.3D 24.11 pro .NET (nejnovější v době psaní)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}