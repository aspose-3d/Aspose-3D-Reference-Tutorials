---
date: 2026-03-13
description: Naučte se, jak pomocí Aspose.3D pro Javu vytvořit 3D válec, krabici a
  další primitivní modely a uložit scénu ve formátu FBX.
linktitle: Building Primitive 3D Models with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Jak vytvořit 3D válec a další primitivní 3D modely pomocí Aspose.3D pro Javu
url: /cs/java/primitive-3d-models/building-primitive-3d-models/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Vytváření primitivních 3D modelů pomocí Aspose.3D pro Java

## Úvod

Pokud jste někdy potřebovali **vytvořit 3D válec** objekty (nebo jakýkoli jiný základní tvar) přímo z Java kódu, Aspose.3D to udělá bez problémů. V tomto tutoriálu projdeme celý pracovní postup – od nastavení prostředí až po uložení finální scény jako souboru FBX – abyste mohli okamžitě začít programově generovat 3D geometrie.

## Rychlé odpovědi
- **Jaká knihovna mi umožní vytvořit 3D válec v Javě?** Aspose.3D for Java.
- **Do jakého formátu mohu exportovat scénu?** FBX (ASCII 7500) pomocí `FileFormat.FBX7500ASCII`.
- **Potřebuji licenci pro vývoj?** Bezplatná zkušební verze funguje pro testování; pro produkci je vyžadována trvalá licence.
- **Jaké hlavní primitivy jsou podporovány?** Box, Cylinder, Sphere, Cone a další.
- **Je kód kompatibilní s Java 8 a novějšími?** Ano, Aspose.3D cílí na JDK 8+.

## Co je primitivní 3D válec?

Primitivní válec je základní geometrický tvar definovaný poloměrem a výškou. V mnoha 3D pipelinech slouží jako stavební blok pro složitější modely, jako jsou potrubí, kola nebo architektonické sloupy. Aspose.3D poskytuje připravenou třídu `Cylinder`, takže nemusíte ručně počítat vrcholy.

## Proč použít Aspose.3D pro Java?

- **Plnohodnotný 3D engine** – podporuje import/export populárních formátů (FBX, OBJ, STL, atd.).
- **Čisté Java API** – bez nativních závislostí, ideální pro multiplatformní projekty.
- **Robustní graf scény** – umožňuje hierarchické uspořádání objektů.
- **Jednoduché licencování** – začněte s bezplatnou zkušební verzí, poté přejděte na trvalou licenci.

## Požadavky

Než se ponoříte do kódu, ujistěte se, že máte:

1. **Java Development Kit (JDK)** – nainstalovaný JDK 8 nebo novější na vašem počítači.  
2. **Aspose.3D for Java library** – stáhněte a nainstalujte ji ze [stránky ke stažení](https://releases.aspose.com/3d/java/).  

## Import balíčků

Začněte importováním hlavního jmenného prostoru Aspose.3D. To vám poskytne přístup k `Scene`, `Box`, `Cylinder` a konstantám formátů souborů.

```java
import com.aspose.threed.*;
```

Nyní, když je knihovna odkazována, vytvořme scénu a přidejme nějakou primitivní geometrii.

## Jak vytvořit 3D válec a další primitivy ve scéně

### Krok 1: Inicializace objektu Scene

Nejprve potřebujeme kontejner `Scene`, který bude obsahovat všechny naše 3D uzly.

```java
// The path to the documents directory.
String myDir = "Your Document Directory";

// Initialize a Scene object
Scene scene = new Scene();
```

### Krok 2: Vytvoření 3D modelu krabice

Primitivní krabice je užitečná pro testování souřadnicového systému. Zde ji přidáme jako potomka kořenového uzlu scény.

```java
// Create a Box model
scene.getRootNode().createChildNode("box", new Box());
```

### Krok 3: Vytvoření 3D modelu válce

Nyní skutečně **vytvoříme 3D válec** geometrii. Třída `Cylinder` má rozumné výchozí rozměry, ale můžete upravit poloměr a výšku pomocí jejího konstruktoru, pokud je to potřeba.

```java
// Create a Cylinder model
scene.getRootNode().createChildNode("cylinder", new Cylinder());
```

### Krok 4: Uložení výkresu ve formátu FBX

Po sestavení scény ji exportujte, aby ji mohly číst další nástroje (např. Unity, Blender). Používáme formát `FBX7500ASCII`, který je široce podporován.

```java
// Save drawing in the FBX format
myDir = myDir + "test.fbx";
scene.save(myDir, FileFormat.FBX7500ASCII);
```

## Časté problémy a řešení

| Problém | Proč se stane | Řešení |
|---------|----------------|--------|
| **Soubor nenalezen** při ukládání | `myDir` ukazuje na neexistující složku | Ujistěte se, že složka existuje, nebo ji vytvořte pomocí `new File(myDir).mkdirs();` |
| **Prázdná scéna** po exportu | Nebyl přidán žádný uzel před voláním `save` | Ověřte, že jsou volány `createChildNode` (debugujte pomocí `scene.getRootNode().getChildCount()` ) |
| **Výjimka licence** | Spuštění bez platné licence v produkci | Použijte dočasnou nebo trvalou licenci pomocí `License license = new License(); license.setLicense("Aspose.3D.Java.lic");` |

## Často kladené otázky

**Q: Mohu použít Aspose.3D pro Java s jinými programovacími jazyky?**  
A: Aspose.3D primárně podporuje Javu, ale jsou k dispozici verze pro jiné jazyky jako .NET.

**Q: Je Aspose.3D vhodný pro složité úlohy 3D modelování?**  
A: Rozhodně! Aspose.3D poskytuje komplexní sadu funkcí, což ho činí vhodným jak pro jednoduché, tak pro složité úlohy 3D modelování.

**Q: Kde mohu najít další pomoc a podporu?**  
A: Navštivte [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) pro komunitní podporu a diskuse.

**Q: Mohu vyzkoušet Aspose.3D před nákupem?**  
A: Ano, můžete vyzkoušet [bezplatnou zkušební verzi](https://releases.aspose.com/) před rozhodnutím o koupi.

**Q: Jak získám dočasnou licenci pro Aspose.3D?**  
A: Dočasnou licenci můžete získat na [temporary license](https://purchase.aspose.com/temporary-license/) stránce Aspose.3D.

## Závěr

Nyní jste se naučili, jak **vytvořit 3D válec**, krabici a další primitivní modely pomocí Aspose.3D pro Java a jak **uložit scénu jako FBX** pro další použití. Klidně experimentujte s dalšími primitivy (Sphere, Cone atd.) a prozkoumejte přiřazení materiálů, aby vaše modely vypadaly realisticky.

---

**Poslední aktualizace:** 2026-03-13  
**Testováno s:** Aspose.3D for Java 24.11 (nejnovější v době psaní)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}