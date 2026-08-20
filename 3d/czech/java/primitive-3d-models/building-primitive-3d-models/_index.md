---
date: 2026-06-03
description: Naučte se, jak exportovat scénu jako FBX a vytvořit 3D válec, krabici
  a další primitivní modely pomocí Aspose.3D for Java.
keywords:
- export scene as fbx
- convert 3d model fbx
- Aspose 3D primitives
- Java 3D modeling
linktitle: Vytváření primitivních 3D modelů pomocí Aspose.3D for Java
schemas:
- author: Aspose
  dateModified: '2026-06-03'
  description: Learn how to export scene as FBX and create 3D cylinder, box, and other
    primitive models using Aspose.3D for Java.
  headline: Export scene as FBX and build cylinder with Aspose.3D Java
  type: TechArticle
- description: Learn how to export scene as FBX and create 3D cylinder, box, and other
    primitive models using Aspose.3D for Java.
  name: Export scene as FBX and build cylinder with Aspose.3D Java
  steps:
  - name: Initialize a Scene Object
    text: The `Scene` class is Aspose.3D's top‑level container that holds all nodes,
      lights, cameras, and materials in memory.
  - name: Build a 3D box model
    text: The `Box` class represents a rectangular prism and is useful for testing
      the coordinate system. Adding it as a child of the scene’s root node positions
      it at the origin.
  - name: Create a 3D cylinder model
    text: The `Cylinder` class is Aspose.3D's built‑in cylinder primitive. It comes
      with default dimensions (radius = 1, height = 2) but you can customise them
      via its constructor.
  - name: Save the drawing in the FBX format
    text: After assembling the scene, export it so other tools (e.g., Unity, Blender)
      can read it. We use the `FBX7500ASCII` format, which is widely supported and
      human‑readable.
  type: HowTo
- questions:
  - answer: Aspose.3D primarily supports Java, but there are versions available for
      .NET and C++ as well.
    question: Can I use Aspose.3D for Java with other programming languages?
  - answer: Absolutely. It provides a comprehensive set of features—including mesh
      manipulation, material assignment, and animation—making it suitable for both
      simple primitives and intricate models.
    question: Is Aspose.3D suitable for complex 3D modeling tasks?
  - answer: Visit the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) for community
      support and discussions.
    question: Where can I find additional help and support?
  - answer: Yes, you can explore a [free trial](https://releases.aspose.com/) before
      making a purchase decision.
    question: Can I try Aspose.3D before purchasing?
  - answer: You can obtain a [temporary license](https://purchase.aspose.com/temporary-license/)
      for Aspose.3D through the website.
    question: How do I obtain a temporary license for Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
title: Exportovat scénu jako FBX a vytvořit válec pomocí Aspose.3D Java
url: /cs/java/primitive-3d-models/building-primitive-3d-models/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Exportovat scénu jako FBX a vytvořit válec pomocí Aspose.3D Java

## Úvod

Pokud jste někdy potřebovali **vytvořit 3D válec** (nebo jakýkoli jiný základní tvar) přímo z Java kódu, Aspose.3D to dělá bezbolestně. V tomto tutoriálu projdeme celý pracovní postup – od nastavení prostředí po **export scénu jako FBX** – abyste mohli okamžitě začít programově generovat 3D geometrie. Uvidíte, jak knihovna pracuje s primitivy, jak je uspořádat v grafu scény a jak uložit výsledek ve formátu, který může číst Unity, Blender nebo jakýkoli jiný 3D nástroj.

## Rychlé odpovědi
- **Která knihovna mi umožní vytvořit 3D válec v Javě?** Aspose.3D for Java.  
- **Do jakého formátu mohu exportovat scénu?** FBX (ASCII 7500) using `FileFormat.FBX7500ASCII`.  
- **Potřebuji licenci pro vývoj?** Bezplatná zkušební verze funguje pro testování; pro produkci je vyžadována trvalá licence.  
- **Jaké hlavní primitivy jsou podporovány?** Box, Cylinder, Sphere, Cone a více než 10 dalších tvarů.  
- **Je kód kompatibilní s Java 8 a novějšími?** Ano, Aspose.3D cílí na JDK 8+.

## Co je primitivní 3D válec?

Primitivní válec je základní geometrický tvar definovaný poloměrem a výškou. V mnoha 3D pipelinech slouží jako stavební blok pro složitější modely, jako jsou potrubí, kola nebo architektonické sloupy. Aspose.3D poskytuje připravenou třídu `Cylinder`, takže nemusíte ručně počítat vrcholy.

## Proč používat Aspose.3D pro Java?

Aspose.3D pro Java nabízí komplexní, čistě Java 3D engine, který eliminuje potřebu nativních knihoven, což ho činí ideálním pro vývoj napříč platformami. Podporuje širokou škálu formátů pro import a export, poskytuje robustní graf scény pro hierarchické uspořádání a zahrnuje vestavěné primitivy, které vám umožní vytvářet geometrii s minimálním kódem. Tyto funkce společně urychlují vývoj a snižují nároky na údržbu.

- **Full‑featured 3D engine** – supports import/export of **over 30** popular formats (FBX, OBJ, STL, GLTF, 3DS, etc.).  
- **Pure Java API** – žádné nativní závislosti, ideální pro projekty napříč platformami.  
- **Robust scene graph** – umožňuje hierarchické uspořádání objektů, což usnadňuje správu velkých scén.  
- **Easy licensing** – začněte s bezplatnou zkušební verzí, poté přejděte na trvalou licenci při nasazení.

## Požadavky

Před tím, než se ponoříte do kódu, ujistěte se, že máte:

1. **Java Development Kit (JDK)** – JDK 8 nebo novější nainstalovaný na vašem počítači.  
2. **Aspose.3D for Java library** – stáhněte a nainstalujte ji ze [download page](https://releases.aspose.com/3d/java/).  

## Import balíčků

Začněte importováním hlavního jmenného prostoru Aspose.3D. To vám poskytne přístup k `Scene`, `Box`, `Cylinder` a konstantám formátu souboru.

```java
import com.aspose.threed.*;
```

Nyní, když je knihovna referencována, vytvoříme scénu a přidáme nějakou primitivní geometrii.

## Jak exportovat scénu jako FBX a vytvořit 3D primitivy?

Načtěte nový objekt `Scene`, přidejte uzly s primitivy (Box, Cylinder, atd.) a poté zavolejte `save` s formátem FBX7500ASCII. Za pouhých několik řádků získáte plnohodnotný FBX soubor, který lze otevřít v jakémkoli hlavním 3D editoru, což umožňuje bezproblémovou integraci s herními enginy, renderovacími pipeline nebo AR/VR aplikacemi.

### Krok 1: Inicializace objektu Scene

`Scene` třída je nejvyšší kontejner Aspose.3D, který v paměti drží všechny uzly, světla, kamery a materiály.

```java
// The path to the documents directory.
String myDir = "Your Document Directory";

// Initialize a Scene object
Scene scene = new Scene();
```

### Krok 2: Vytvoření 3D modelu krabice

`Box` třída představuje pravoúhlý hranol a je užitečná pro testování souřadnicového systému. Přidáním jako potomka kořenového uzlu scény ji umístíte do počátku.

```java
// Create a Box model
scene.getRootNode().createChildNode("box", new Box());
```

### Krok 3: Vytvoření 3D modelu válce

`Cylinder` třída je vestavěný primitivní válec v Aspose.3D. Má výchozí rozměry (poloměr = 1, výška = 2), ale můžete je upravit pomocí jejího konstruktoru.

```java
// Create a Cylinder model
scene.getRootNode().createChildNode("cylinder", new Cylinder());
```

### Krok 4: Uložení výkresu ve formátu FBX

Po sestavení scény ji exportujte, aby ji ostatní nástroje (např. Unity, Blender) mohly číst. Používáme formát `FBX7500ASCII`, který je široce podporován a čitelný pro člověka.

```java
// Save drawing in the FBX format
myDir = myDir + "test.fbx";
scene.save(myDir, FileFormat.FBX7500ASCII);
```

## Časté problémy a řešení

| Problém | Proč k tomu dochází | Řešení |
|-------|----------------|-----|
| **File not found** při ukládání | `myDir` ukazuje na neexistující složku | Zajistěte, aby složka existovala, nebo ji vytvořte pomocí `new File(myDir).mkdirs();` |
| **Empty scene** po exportu | Před voláním `save` nebyly přidány žádné uzly | Ověřte, že jsou volány `createChildNode` (debugujte pomocí `scene.getRootNode().getChildCount()` ) |
| **License exception** | Spuštění bez platné licence v produkci | Použijte dočasnou nebo trvalou licenci pomocí `License license = new License(); license.setLicense("Aspose.3D.Java.lic");` |

## Často kladené otázky

**Q: Mohu použít Aspose.3D pro Java i s jinými programovacími jazyky?**  
A: Aspose.3D primárně podporuje Javu, ale jsou k dispozici i verze pro .NET a C++.

**Q: Je Aspose.3D vhodný pro složité úkoly 3D modelování?**  
A: Rozhodně. Poskytuje komplexní sadu funkcí – včetně manipulace s meshem, přiřazování materiálů a animací – což ho činí vhodným jak pro jednoduché primitivy, tak pro složité modely.

**Q: Kde mohu najít další pomoc a podporu?**  
A: Navštivte [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) pro komunitní podporu a diskuze.

**Q: Můžu vyzkoušet Aspose.3D před zakoupením?**  
A: Ano, můžete si vyzkoušet [free trial](https://releases.aspose.com/) před rozhodnutím o koupi.

**Q: Jak získám dočasnou licenci pro Aspose.3D?**  
A: Dočasnou licenci můžete získat na [temporary license](https://purchase.aspose.com/temporary-license/) pro Aspose.3D prostřednictvím webu.

## Závěr

Nyní jste se naučili, jak **exportovat scénu jako FBX** a jak **vytvořit 3D válec**, krabici a další primitivní modely pomocí Aspose.3D pro Java. Klidně experimentujte s dalšími primitivy, jako jsou Sphere, Cone nebo Torus, a prozkoumejte přiřazování materiálů, aby vaše modely vypadaly realisticky. Jakmile budete mít jistotu, můžete integrovat vygenerované FBX soubory do herních enginů, AR/VR pipeline nebo jakéhokoli dalšího 3D workflow.

---

**Poslední aktualizace:** 2026-06-03  
**Testováno s:** Aspose.3D for Java 24.11 (latest at time of writing)  
**Autor:** Aspose

## Související tutoriály

- [Jak exportovat scénu do FBX a získat informace o 3D scéně v Javě](/3d/java/3d-scenes-and-models/get-scene-information/)
- [Jak exportovat FBX a vytvořit hierarchie uzlů v Javě](/3d/java/geometry/build-node-hierarchies/)
- [Jak vytvořit modely válců s Aspose.3D pro Java](/3d/java/cylinders/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< blocks/products/products-backtop-button >}}
{{< /blocks/products/pf/main-wrap-class >}}