---
date: 2026-01-27
description: Naučte se, jak efektivně rozdělit síť podle materiálu v Javě s Aspose.3D.
  Tento průvodce vám ukáže, jak snížit počet draw callů a zlepšit výkon renderování
  při rozdělování sítě podle materiálu.
linktitle: How to Split Mesh by Material in Java Using Aspose.3D
second_title: Aspose.3D Java API
title: Jak rozdělit síť podle materiálu v Javě pomocí Aspose.3D
url: /cs/java/3d-mesh-data/split-meshes-by-material/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak rozdělit síť podle materiálu v Javě pomocí Aspose.3D

## Úvod

Pokud pracujete s 3D grafikou v Javě, rychle zjistíte, že zpracování velkých sítí může být úzkým místem výkonu — zejména když jedna síť obsahuje více materiálů. **Naučení se, jak rozdělit síť** podle materiálu vám umožní izolovat každou skup polygonů specifickou pro materiál, což zajišťuje rychlejší vykreslování, snadnější ořezávání a podrobnější kontrolu nad manipulací s texturami. V tomto tutoriálu vás provedeme přesnými kroky, jak **rozdělit síť podle materiálu** pomocí knihovny Aspose.3D, včetně praktických vysvětlení, tipů na snížení počtu draw callů a rad, jak zlepšit výkon vykreslování.

## Rychlé odpovědi
- **Co znamená „rozdělit síť podle materiálu“?** Odděluje jednu síť na více pod‑sítí, z nichž každá obsahuje polygony sdílející stejný materiál.
- **Proč použít Aspose.3D?** Poskytuje vysoce‑úrovňové, multiplatformní API, které abstrahuje nízko‑úrovňové formáty souborů a přitom zachovává výkon.
- **Jak dlouho trvá implementace?** Přibližně 10–15 minut kódování a testování.
- **Potřebuji licenci?** K dispozici je bezplatná zkušební verze; pro produkční použití je vyžadována komerční licence.
- **Jaká verze Javy je podporována?** Java 8 nebo vyšší.

## Co je rozdělení sítě?

Rozdělení sítě je proces rozdělení komplexní 3D sítě na menší, snadněji spravovatelné části. Když je rozdělení založeno na materiálu, každá vzniklá pod‑síť obsahuje pouze polygony, které odkazují na jeden materiál. Tento přístup snižuje počet draw callů, zlepšuje výkon vykreslování a zjednodušuje úkoly, jako je aplikace shaderů na úrovni materiálu.

## Proč rozdělit síť podle materiálu?

- **Výkon:** Vykreslovací enginy mohou seskupovat draw cally podle materiálu, čímž snižují změny stavu GPU.
- **Flexibilita:** Můžete aplikovat různé post‑processing efekty nebo kolizní logiku na úrovni materiálu.
- **Správa paměti:** Menší sítě se snáze streamují do a z paměti, což je klíčové pro mobilní nebo VR aplikace.
- **Snížený počet draw callů:** Méně změn stavu umožňuje GPU zpracovávat snímky efektivněji.
- **Zlepšený výkon vykreslování:** Izolace materiálů často vede k lepším výsledkům ořezávání a stínování.

## Předpoklady

Než se pustíme do kódu, ujistěte se, že máte následující:

- Základní znalosti programování v Javě.
- Knihovnu Aspose.3D pro Java nainstalovanou (stáhněte z [Aspose webu](https://releases.aspose.com/3d/java/)).
- IDE jako IntelliJ IDEA, Eclipse nebo VS Code nakonfigurované pro vývoj v Javě.

## Import balíčků

Nejprve importujte požadované třídy Aspose.3D a případné standardní utility Javy, které budete potřebovat:

```java
import com.aspose.threed.*;

import java.util.Arrays;
```

## Průvodce krok za krokem

Níže najdete stručný přehled každého kroku, s vysvětlením před kódem, abyste přesně věděli, co se děje.

### Krok 1: Vytvořte síť krabice

Začínáme jednoduchým geometrickým primitivem — krabicí, abychom jasně viděli, jak každá strana (rovina) získá svůj vlastní materiál později.

```java
// ExStart:SplitMeshbyMaterial

// Create a mesh of a box (composed of 6 planes)
Mesh box = (new Box()).toMesh();
```

### Krok 2: Vytvořte prvek materiálu

`VertexElementMaterial` ukládá indexy materiálů pro každý polygon. Připojením tohoto prvku k síti můžeme řídit, který materiál každá strana používá.

```java
// Create a material element on the box mesh
VertexElementMaterial mat = (VertexElementMaterial) box.createElement(VertexElementType.MATERIAL, MappingMode.POLYGON, ReferenceMode.INDEX);
```

### Krok 3: Specifikujte různé indexy materiálů

Zde přiřazujeme jedinečný index materiálu každé ze šesti rovin krabice. Pořadí v poli odpovídá pořadí polygonů generovaných primitivem `Box`.

```java
// Specify different material indices for each plane
mat.setIndices(new int[]{0, 1, 2, 3, 4, 5});
```

### Krok 4: Rozdělte síť na pod‑sítě

Volání `PolygonModifier.splitMesh` s `SplitMeshPolicy.CLONE_DATA` vytvoří novou pod‑síť pro každý odlišný index materiálu a zároveň zachová původní data vrcholů.

```java
// Split the mesh into 6 sub-meshes, each plane becoming a sub-mesh
Mesh[] planes = PolygonModifier.splitMesh(box, SplitMeshPolicy.CLONE_DATA);
```

### Krok 5: Aktualizujte indexy materiálů a rozdělte znovu

Pro demonstraci jiné strategie rozdělení seskupíme první tři roviny pod materiál 0 a zbývající tři pod materiál 1, poté rozdělíme pomocí `COMPACT_DATA`, abychom odstranili nepoužívané vrcholy.

```java
// Update material indices and split into 2 sub-meshes
mat.getIndices().clear();
mat.setIndices(new int[]{0, 0, 0, 1, 1, 1});
planes = PolygonModifier.splitMesh(box, SplitMeshPolicy.COMPACT_DATA);
```

### Krok 6: Potvrďte úspěch

Jednoduchá zpráva v konzoli vás informuje, že operace proběhla bez chyb.

```java
// Display success message
System.out.println("\nSplitting a mesh by specifying the material successfully.");
// ExEnd:SplitMeshbyMaterial
```

## Snížení počtu draw callů a zlepšení výkonu vykreslování

Přeměnou každého materiálu na vlastní síť umožníte grafickému potrubí vydat jeden draw call na materiál místo jednoho na polygon. Toto snížení počtu draw callů přímo vede k plynulejším snímkům, zejména na slabším hardware. Navíc politika `COMPACT_DATA` odstraňuje nepoužívané vrcholy, čímž dále snižuje šířku pásma paměti a pomáhá GPU renderovat efektivněji.

## Časté problémy a řešení

| Problém | Proč se to děje | Řešení |
|---------|----------------|--------|
| **Sub‑meshe obsahují duplicitní vrcholy** | Použití `CLONE_DATA` kopíruje všechna data vrcholů pro každou pod‑síť. | Přepněte na `COMPACT_DATA`, pokud chcete, aby sdílené vrcholy byly deduplikovány. |
| **Nesprávné přiřazení materiálu** | Délka pole index neodpovídá počtu polygonů. | Ověřte počet polygonů (např. krabice má 6) a poskytněte odpovídající pole indexů. |

## Často kladené otázky

**Q: Je Aspose.3D kompatibilní s jinými Java 3D knihovnami?**  
A: Ano, Aspose.3D může koexistovat s knihovnami jako Java 3D nebo jMonkeyEngine, což umožňuje import/export sítí mezi nimi.

**Q: Lze tuto techniku použít na složité modely se stovkami materiálů?**  
A: Rozhodně. Stejné API volání fungují bez ohledu na složitost sítě; jen se ujistěte, že vaše pole indexů správně odráží rozložení materiálů.

**Q: Kde najdu kompletní dokumentaci Aspose.3D pro Java?**  
A: Navštivte oficiální [Aspose.3D Java documentation](https://reference.aspose.com/3d/java/) pro podrobné reference API a další příklady.

**Q: Je k dispozici bezplatná zkušební verze Aspose.3D pro Java?**  
A: Ano, můžete si stáhnout zkušební verzi z [Aspose Releases page](https://releases.aspose.com/).

**Q: Jak získám podporu, pokud narazím na problémy?**  
A: Komunitní fórum Aspose ([Aspose.3D forum](https://forum.aspose.com/c/3d/18)) je vynikající místo, kde můžete klást otázky a získat pomoc jak od týmu Aspose, tak od dalších vývojářů.

---

**Poslední aktualizace:** 2026-01-27  
**Testováno s:** Aspose.3D for Java 24.11  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}