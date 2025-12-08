---
date: 2025-12-08
description: Naučte se, jak vytvořit 3D scénu v Javě, aplikovat realistické PBR materiály
  pomocí Aspose.3D a uložit 3D model ve formátu STL pro renderování 3D objektů v Javě.
language: cs
linktitle: Create 3D Scene Java – Apply PBR Materials with Aspose.3D
second_title: Aspose.3D Java API
title: 'Vytvořte 3D scénu v Javě: aplikujte PBR materiály s Aspose.3D'
url: /java/geometry/apply-pbr-materials-to-objects/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Vytvořte 3D scénu v Javě – Použijte PBR materiály s Aspose.3D

## Úvod

V tomto praktickém tutoriálu se naučíte **jak vytvořit 3D scénu v Javě** a obohatit ji o materiály Physically Based Rendering (PBR) pomocí knihovny Aspose.3D. Na konci průvodce budete schopni renderovat realistické povrchy a **uložit 3D model STL** pro další použití v jakémkoli 3D pipeline.

## Rychlé odpovědi
- **Co znamená “create 3d scene java”?** Jedná se o proces vytváření objektu Scene, který v Java aplikaci obsahuje geometrii, světla a kamery.  
- **Která knihovna zpracovává PBR materiály?** Aspose.3D poskytuje připravenou třídu `PbrMaterial`.  
- **Mohu výsledek exportovat jako STL?** Ano – metoda `Scene.save` podporuje STL (ASCII i binární).  
- **Potřebuji licenci pro produkci?** Pro komerční použití je vyžadována trvalá licence Aspose.3D; dočasná licence stačí pro testování.  
- **Jaká verze Javy je vyžadována?** Jakékoli prostředí Java 8+ je podporováno.

## Co je 3D scéna v Javě?

*Scéna* je kontejner, který obsahuje všechny objekty (uzly), jejich geometrii, materiály, světla a kamery. Představte si ji jako virtuální jeviště, na které umisťujete své 3D modely. Třída `Scene` z Aspose.3D vám poskytuje čistý, objektově orientovaný způsob, jak toto jeviště programově vytvořit.

## Proč používat PBR materiály při renderování 3D objektů v Javě?

PBR (Physically Based Rendering) napodobuje interakci světla ve skutečném světě pomocí parametrů jako jsou faktory metalic a drsnosti. Výsledkem je přesvědčivější vzhled za různých světelných podmínek, což je zvláště cenné pro vizualizaci produktů, hry nebo AR/VR zážitky.

## Požadavky

Než se pustíme dál, ujistěte se, že máte následující:

1. **Java vývojové prostředí** – nainstalovaný JDK 8 nebo novější.  
2. **Knihovna Aspose.3D** – Stáhněte nejnovější JAR z [odkazu ke stažení](https://releases.aspose.com/3d/java/).  
3. **Dokumentace** – Seznamte se s API prostřednictvím oficiální [dokumentace](https://reference.aspose.com/3d/java/).  
4. **Dočasná licence (volitelné)** – Pokud nemáte trvalou licenci, získejte [dočasnou licenci](https://purchase.aspose.com/temporary-license/) pro testování.

## Import balíčků

Přidejte jmenný prostor Aspose.3D do vašeho Java zdrojového souboru:

```java
import com.aspose.threed.*;
```

## Krok 1: Inicializace scény

Vytvořte scénu, která bude sloužit jako plátno pro vaši geometrii a materiály.

```java
// ExStart:InitializeScene
String MyDir = "Your Document Directory";
Scene scene = new Scene();
// ExEnd:InitializeScene
```

> **Tip:** Nechte `MyDir` ukazovat na zapisovatelnou složku; jinak volání `save` selže.

## Krok 2: Inicializace PBR materiálu

Nakonfigurujte PBR materiál s hodnotami metalic a drsnosti, které poskytují téměř kovový vzhled.

```java
// ExStart:InitializePBRMaterial
PbrMaterial mat = new PbrMaterial();
mat.setMetallicFactor(0.9);
mat.setRoughnessFactor(0.9);
// ExEnd:InitializePBRMaterial
```

> **Proč tyto hodnoty?** Vysoký faktor metalic (≈ 0.9) způsobí, že povrch se chová jako kov, zatímco vysoká drsnost (≈ 0.9) přidává jemnou difuzi, čímž zabraňuje dokonalému zrcadlovému povrchu.

## Krok 3: Vytvoření 3D objektu a aplikace materiálu

Zde vygenerujeme jednoduchou geometrii krabice, připojíme ji k kořenovému uzlu scény a přiřadíme PBR materiál, který jsme právě vytvořili.

```java
// ExStart:Create3DObject
Node boxNode = scene.getRootNode().createChildNode("box", new Box());
boxNode.setMaterial(mat);
// ExEnd:Create3DObject
```

> **Častá chyba:** Zapomenutí nastavit materiál na uzlu způsobí, že objekt bude mít výchozí (ne‑PBR) vzhled.

## Krok 4: Uložení 3D scény (export STL)

Exportujte celou scénu — včetně krabice vylepšené PBR — do souboru STL. STL je široce podporovaný formát pro 3‑D tisk a rychlé vizuální kontroly.

```java
// ExStart:Save3DScene
scene.save(MyDir + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
// ExEnd:Save3DScene
```

Můžete také zvolit `FileFormat.STLBINARY`, pokud je požadována menší velikost souboru.

## Časté problémy a řešení

| **Problém** | **Pravděpodobná příčina** | **Řešení** |
|-------------|---------------------------|------------|
| **Soubor nebyl uložen** | `MyDir` ukazuje na neexistující složku nebo nemá oprávnění k zápisu | Ověřte, že složka existuje a váš Java proces má oprávnění k zápisu |
| **Materiál vypadá plochý** | Hodnoty Metallic/Roughness jsou nastaveny na 0 | Zvyšte `setMetallicFactor` a/nebo `setRoughnessFactor` |
| **Soubor STL nelze otevřít** | Špatná vlajka formátu souboru (ASCII vs Binary) pro prohlížeč | Použijte odpovídající výčet `FileFormat` pro váš cílový prohlížeč |

## Často kladené otázky

**Q: Mohu používat Aspose.3D pro komerční projekty?**  
A: Ano. Zakupte komerční licenci na [stránce nákupu](https://purchase.aspose.com/buy).

**Q: Jak získám podporu pro Aspose.3D?**  
A: Připojte se ke komunitě na [fóru Aspose.3D](https://forum.aspose.com/c/3d/18) pro bezplatnou pomoc, nebo otevřete ticket podpory s platnou licencí.

**Q: Je k dispozici bezplatná zkušební verze?**  
A: Rozhodně. Stáhněte si zkušební verzi ze [stránky s bezplatnou zkuškou](https://releases.aspose.com/).

**Q: Kde najdu podrobnou dokumentaci pro Aspose.3D?**  
A: Všechny reference API jsou k dispozici v oficiální [dokumentaci](https://reference.aspose.com/3d/java/).

**Q: Jak získám dočasnou licenci pro testování?**A: Požádejte o ni prostřednictvím [odkazu na dočasnou licenci](https://purchase.aspose.com/temporary-license/).

## Závěr

Nyní jste **vytvořili 3D scénu v Javě**, aplikovali realistický PBR materiál a exportovali výsledek jako soubor STL pomocí Aspose.3D. Tento workflow vám poskytuje pevný základ pro tvorbu bohatších vizualizací, přípravu aktiv pro 3‑D tisk nebo nasazení modelů do herních enginů.

---

**Poslední aktualizace:** 2025-12-08  
**Testováno s:** Aspose.3D 24.12 (nejnovější)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}