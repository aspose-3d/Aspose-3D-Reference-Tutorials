---
date: 2026-05-14
description: Naučte se, jak exportovat STL v Javě vytvořením 3D scény, aplikací realistických
  PBR materiálů pomocí Aspose.3D a uložením modelu pro renderování.
keywords:
- how to export stl
- Aspose 3D PBR materials
- Java 3D scene creation
linktitle: Jak exportovat STL v Javě – Vytvořte 3D scénu s Aspose.3D
schemas:
- author: Aspose
  dateModified: '2026-05-14'
  description: Learn how to export STL in Java by creating a 3D scene, applying realistic
    PBR materials with Aspose.3D, and saving the model for rendering.
  headline: How to Export STL in Java – Create 3D Scene with Aspose.3D
  type: TechArticle
- description: Learn how to export STL in Java by creating a 3D scene, applying realistic
    PBR materials with Aspose.3D, and saving the model for rendering.
  name: How to Export STL in Java – Create 3D Scene with Aspose.3D
  steps:
  - name: '**Java Development Environment** – JDK 8 or newer installed.'
    text: '**Java Development Environment** – JDK 8 or newer installed.'
  - name: '**Aspose.3D Library** – Download the latest JAR from the [download link](https://releases.aspose.com/3d/java/).'
    text: '**Aspose.3D Library** – Download the latest JAR from the [download link](https://releases.aspose.com/3d/java/).'
  - name: '**Documentation** – Familiarise yourself with the API via the official
      [documentation](https://reference.aspose.com/3d/java/).'
    text: '**Documentation** – Familiarise yourself with the API via the official
      [documentation](https://reference.aspose.com/3d/java/).'
  - name: '**Temporary License (Optional)** – If you don’t have a permanent license,
      obtain a [temporary license](https://purchase.aspose.com/temporary-license/)
      for testing.'
    text: '**Temporary License (Optional)** – If you don’t have a permanent license,
      obtain a [temporary license](https://purchase.aspose.com/temporary-license/)
      for testing.'
  type: HowTo
- questions:
  - answer: It’s the process of building a `Scene` object that holds geometry, lights,
      and cameras in a Java application.
    question: What does “create 3d scene java” mean?
  - answer: Aspose.3D provides a ready‑made `PbrMaterial` class.
    question: Which library handles PBR materials?
  - answer: Yes – the `Scene.save` method supports STL (ASCII and binary).
    question: Can I export the result as STL?
  - answer: A permanent Aspose.3D license is required for commercial use; a temporary
      license works for testing.
    question: Do I need a license for production?
  - answer: Any Java 8+ runtime is supported.
    question: What Java version is required?
  type: FAQPage
second_title: Aspose.3D Java API
title: Jak exportovat STL v Javě – Vytvořte 3D scénu s Aspose.3D
url: /cs/java/geometry/apply-pbr-materials-to-objects/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak exportovat STL v Javě – Vytvořit 3D scénu s Aspose.3D

## Úvod

V tomto praktickém tutoriálu se naučíte **jak exportovat STL** z Java aplikace tím, že vytvoříte kompletní 3D scénu, použijete materiály Physically Based Rendering (PBR) a výsledek uložíte pomocí Aspose.3D. Ať už cílíte na 3‑D tisk, pipeline herních enginů nebo vizualizaci produktů, níže uvedené kroky vám poskytnou opakovatelný, verzovaně řízený pracovní postup, který funguje na libovolném runtime Java 8+.

## Rychlé odpovědi
- **Co znamená “create 3d scene java”?** Jedná se o proces vytváření objektu `Scene`, který v Java aplikaci obsahuje geometrii, světla a kamery.  
- **Která knihovna zpracovává PBR materiály?** Aspose.3D poskytuje připravenou třídu `PbrMaterial`.  
- **Mohu výsledek exportovat jako STL?** Ano – metoda `Scene.save` podporuje STL (ASCII i binární).  
- **Potřebuji licenci pro produkci?** Pro komerční použití je vyžadována trvalá licence Aspose.3D; dočasná licence stačí pro testování.  
- **Jaká verze Javy je požadována?** Jakýkoli runtime Java 8+ je podporován.

## Jak vytvořit 3d scénu v Javě s Aspose.3D

`Scene` je hlavní třída kontejneru představující 3D dokument. Načtěte, nakonfigurujte a uložte scénu pomocí několika řádků kódu. Nejprve vytvoříte instanci `Scene`, poté připojíte geometrii a `PbrMaterial` a nakonec zavoláte `Scene.save` s formátem STL. Tento end‑to‑end tok vám umožní automatizovat generování assetů, aniž byste museli otevírat 3D editor.

## Co je 3D scéna v Javě?

*Scéna* je kontejner, který obsahuje všechny objekty (uzly), jejich geometrii, materiály, světla a kamery. Představte si ji jako virtuální jeviště, na které umisťujete své 3D modely. Třída `Scene` z Aspose.3D vám poskytuje čistý, objektově orientovaný způsob, jak toto jeviště programově vytvořit.

## Proč používat PBR materiály pro renderování 3D objektů v Javě?

PBR (Physically Based Rendering) napodobuje interakci světla ve skutečném světě pomocí parametrů metallic a roughness. Výsledkem je materiál, který vypadá konzistentně za jakýchkoli světelných podmínek, což je nezbytné pro realistickou vizualizaci produktů, AR/VR a moderní herní enginy. Ovládáním parametrů metallic, roughness, albedo a normálových map můžete dosáhnout široké škály povrchových úprav – od leštěného kovu po matný plast – bez ručního ladění shaderů.

## Požadavky

1. **Java vývojové prostředí** – Nainstalovaný JDK 8 nebo novější.  
2. **Aspose.3D knihovna** – Stáhněte nejnovější JAR z [odkazu ke stažení](https://releases.aspose.com/3d/java/).  
3. **Dokumentace** – Seznamte se s API prostřednictvím oficiální [dokumentace](https://reference.aspose.com/3d/java/).  
4. **Dočasná licence (volitelné)** – Pokud nemáte trvalou licenci, získejte [dočasnou licenci](https://purchase.aspose.com/temporary-license/) pro testování.

## Běžné případy použití

| Případ použití | Jak tutoriál pomáhá |
|----------------|---------------------|
| **3‑D tisk** | Export do STL vám umožní odeslat model přímo do sliceru. |
| **Pipeline herních assetů** | Parametry PBR materiálů odpovídají očekáváním moderních herních enginů. |
| **Produktový konfigurátor** | Automatizujte varianty barev/povrchových úprav úpravou hodnot metallic/roughness. |

## Import balíčků

Namespace `Aspose.3D` musí být importován, aby kompilátor mohl rozpoznat třídy použité v tutoriálu.

```java
import com.aspose.threed.*;
```

## Krok 1: Inicializace scény

`Scene` je hlavní kontejner pro veškerý 3D obsah. Vytvořením nové instance získáte čisté plátno, na které můžete přidávat geometrii, světla a kamery.

```java
// ExStart:InitializeScene
String MyDir = "Your Document Directory";
Scene scene = new Scene();
// ExEnd:InitializeScene
```

> **Tip:** Nechte `MyDir` ukazovat na zapisovatelnou složku; jinak volání `save` selže.

## Krok 2: Inicializace PBR materiálu

`PbrMaterial` definuje vlastnosti fyzicky založeného renderování, jako jsou metallic a roughness. `PbrMaterial` určuje metallic, roughness a další povrchové vlastnosti. Nastavení vysokého faktoru metallic (≈ 0.9) a roughness 0.9 poskytuje realistický vzhled kartáčovaného kovu.

```java
// ExStart:InitializePBRMaterial
PbrMaterial mat = new PbrMaterial();
mat.setMetallicFactor(0.9);
mat.setRoughnessFactor(0.9);
// ExEnd:InitializePBRMaterial
```

> **Proč tyto hodnoty?** Vysoký faktor metallic způsobí, že povrch se chová jako kov, zatímco vysoká hodnota roughness přidává jemnou difuzi, čímž zabraňuje dokonalému zrcadlovému povrchu.

## Krok 3: Vytvoření 3D objektu a aplikace materiálu

Zde vygenerujeme jednoduchou geometrii krabice, připojíme ji k kořenovému uzlu scény a přiřadíme `PbrMaterial`, který jsme právě vytvořili.

```java
// ExStart:Create3DObject
Node boxNode = scene.getRootNode().createChildNode("box", new Box());
boxNode.setMaterial(mat);
// ExEnd:Create3DObject
```

> **Častá chyba:** Zapomenutí nastavit materiál na uzlu způsobí, že objekt bude mít výchozí (ne‑PBR) vzhled.

## Krok 4: Uložení 3D scény (export STL)

`Scene.save` zapíše scénu do souboru ve zvoleném formátu. Exportujte celou scénu – včetně krabice vylepšené PBR – do souboru STL. STL je široce podporovaný formát pro 3‑D tisk a rychlé vizuální kontroly.

```java
// ExStart:Save3DScene
scene.save(MyDir + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
// ExEnd:Save3DScene
```

`FileFormat.STLBINARY` určuje binární výstup STL, který je menší než ASCII. Můžete také zvolit `FileFormat.STLASCII`, pokud je preferován soubor čitelný pro člověka.

## Proč je to důležité

Konzistentní parametry materiálu zajišťují, že každý vygenerovaný model vypadá stejně napříč různými prohlížeči a osvětlením. Automatizace vám umožní vytvářet velké dávky variant s minimálním úsilím, zatímco cross‑platform výstup STL zaručuje kompatibilitu s nástroji od Blenderu po slicery pro 3‑D tiskárny. Tyto výhody společně urychlují vývojové pipeline a snižují manuální chyby.

## Tipy pro řešení problémů

| Problém | Pravděpodobná příčina | Řešení |
|---------|-----------------------|--------|
| **Soubor nebyl uložen** | `MyDir` ukazuje na neexistující složku nebo nemá oprávnění k zápisu | Ověřte, že složka existuje a váš Java proces má právo zápisu |
| **Materiál vypadá plochý** | Hodnoty Metallic/Roughness jsou nastaveny na 0 | Zvyšte `setMetallicFactor` a/nebo `setRoughnessFactor` |
| **Soubor STL nelze otevřít** | Nesprávná vlajka formátu souboru (ASCII vs Binary) pro prohlížeč | Použijte odpovídající enum `FileFormat` pro cílový prohlížeč |

## Často kladené otázky

**Q:** Mohu použít Aspose.3D pro komerční projekty?  
**A:** Ano. Zakupte komerční licenci na [stránce nákupu](https://purchase.aspose.com/buy).

**Q:** Jak získám podporu pro Aspose.3D?  
**A:** Připojte se ke komunitě na [fóru Aspose.3D](https://forum.aspose.com/c/3d/18) pro bezplatnou pomoc, nebo otevřete ticket podpory s platnou licencí.

**Q:** Je k dispozici bezplatná zkušební verze?  
**A:** Rozhodně. Stáhněte si trial verzi ze [stránky s bezplatnou zkušební verzí](https://releases.aspose.com/).

**Q:** Kde najdu podrobnou dokumentaci pro Aspose.3D?  
**A:** Všechny reference API jsou k dispozici v oficiální [dokumentaci](https://reference.aspose.com/3d/java/).

**Q:** Jak získám dočasnou licenci pro testování?  
**A:** Požádejte o ni prostřednictvím [odkazu na dočasnou licenci](https://purchase.aspose.com/temporary-license/).

---

**Poslední aktualizace:** 2026-05-14  
**Testováno s:** Aspose.3D 24.12 (latest)  
**Autor:** Aspose  

{{< blocks/products/products-backtop-button >}}

## Související tutoriály

- [Vytvořit 3D scénu v Javě s Aspose 3D Java](/3d/java/3d-scenes-and-models/)
- [Jak exportovat scénu do FBX a získat informace o 3D scéně v Javě](/3d/java/3d-scenes-and-models/get-scene-information/)
- [Jak exportovat OBJ – úprava orientace roviny pro přesné umístění 3D scény v Javě](/3d/java/3d-scenes-and-models/change-plane-orientation/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}