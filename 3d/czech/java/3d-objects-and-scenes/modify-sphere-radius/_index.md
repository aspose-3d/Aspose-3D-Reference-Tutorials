---
date: 2025-11-30
description: Naučte se, jak používat Aspose v Javě k úpravě poloměru 3D koule. Tento
  krok‑za‑krokem průvodce pokrývá knihovnu Aspose.3D pro Javu, jak nastavit poloměr,
  přidat kouli do scény a zapsat soubor OBJ v Javě.
linktitle: 'How to Use Aspose: Modify 3D Sphere Radius in Java with Aspose.3D'
second_title: Aspose.3D Java API
title: 'Jak používat Aspose: úprava poloměru 3D koule v Javě pomocí Aspose.3D'
url: /cs/java/3d-objects-and-scenes/modify-sphere-radius/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak používat Aspose: Změna poloměru 3D koule v Javě pomocí Aspose.3D

## Úvod

Pokud hledáte **how to use Aspose** pro práci s 3D modely v Javě, jste na správném místě. V tomto tutoriálu vás provedeme všemi kroky potřebnými ke změně velikosti koule, jejímu přidání do scény a nakonec k zápisu OBJ souboru pomocí **Aspose.3D Java library**. Na konci budete mít znovupoužitelný úryvek, který můžete vložit do jakékoli Java‑založené 3D aplikace.

## Rychlé odpovědi
- **Jaký je hlavní účel tohoto průvodce?** Ukázat, jak v Javě pomocí Aspose.3D upravit poloměr koule.  
- **Kterou knihovnu používáme?** Aspose.3D Java library (plnohodnotná **java 3d library**).  
- **Jak nastavit poloměr?** Zavolejte `sphere.setRadius(double)` na objektu `Sphere`.  
- **Mohu exportovat do OBJ?** Ano – použijte `scene.save("file.obj", FileFormat.WAVEFRONTOBJ)`.  
- **Potřebuji licenci?** Bezplatná zkušební verze funguje pro vývoj; licence je vyžadována pro produkci.

## Co je Aspose.3D pro Javu?

Aspose.3D je **java 3d library**, která umožňuje vývojářům vytvářet, upravovat a konvertovat 3D soubory bez jakýchkoli externích závislostí. Podporuje populární formáty jako OBJ, FBX, STL a další, což ji činí ideální pro hry, CAD nástroje a vědecké vizualizace.

## Proč použít Aspose.3D ke změně velikosti koule?

- **Není vyžadován žádný nativní 3D engine** operace jsou prováděny na objektov  
- **Cross‑platform** – funguje na jakémkoli OS, který spouští Javu.  
- **High‑precision geometry** – můžete nastavit přesné hodnoty poloměru, ne jen přibližné škálování.  

## Předpoklady

Předtím, než se ponoříte, ujistěte se, že máte:

- Základní znalost programování v Javě.  
- Aspose.3D knihovna nainstalována – můžete ji stáhnout z [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/).  
- Java Development Kit (JDK) nainstalován na vašem počítači.

## Import balíčků

Pro začátek importujte potřebné třídy do vašeho Java projektu:

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Sphere;

import java.io.IOException;
```

## Krok 1: Inicializace scény

```java
// ExStart:WorkingWithSphereRadius

// initialize a scene
Scene scene = new Scene();
```

Zme novou **3D scene**, která bude obsahovat veškerou naši geometrii.

## Krok 2: Inicializace koule

```java
// initialize a Sphere
Sphere sphere = new Sphere();
```

Objekt `Sphere` představuje dokonalý primitivní tvar koule. V tuto chvíli používá výchozí poloměr 1.0.

## Krok 3: Jak nastavit poloměr koule

```java
// set radius
sphere.setRadius(10);
```

Tento řádek ukazuje **jak nastavit poloměr**. Můžete nahradit `10` libovolnou `double` hodnotou pro dosažení požadované velikosti.

## Krok 4: Přidání koule do scény

```java
// add sphere to the scene
scene.getRootNode().createChildNode(sphere);
```

Volání **adds sphere to scene** (nebo „add sphere to scene“) vytvoří podřízený uzel pod kořenovým uzlem.

## Krok 5: Zápis OBJ souboru v Javě

```java
// save scene
scene.save("sphere.obj", FileFormat.WAVEFRONTOBJ);
```

Nakonec **write OBJ file Java** styl pomocí `scene.save`. Výstupní soubor `sphere.obj` lze otevřít v jakémkoli 3D prohlížeči, který podporuje formát Wavefront OBJ.

## Časté problémy a řešení

| Problém | Řešení |
|---------|--------|
| **Koule se ve vieweru zobrazuje příliš malá** | Ověřte, že je hodnota poloměru nastavena správně; pamatujte, že jednotky jsou libovolné, pokud nepoužijete transformační škálování. |
| **Exportovaný OBJ nemá materiál** | Aspose.3D zapisuje pouze geometrii; přidejte materiál ke kouli, pokud potřebujete textury (`sphere.setMaterial(...)`). |
| **Výjimka licence za běhu** | Ujistěte se, že máte načtený buď dočasný, nebo trvalý licenční soubor před vytvořením `Scene`. |

## Často kladené otázky

### Q: Kde najdu dokumentaci pro Aspose.3D pro Javu?

A: Můžete se podívat na [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/) pro komplexní informace a pokyny k použití.

### Q: Jak stáhnu Aspose.3D pro Javu?

A: Stáhněte knihovnu ze stránky vydání: [Download Aspose.3D for Java](https://releases.aspose.com/3d/java/).

### Q: Je k dispozici bezplatná zkušební verze pro Aspose.3D pro Javu?

A: Ano, prozkoumejte funkce pomocí bezplatné zkušební verze na [Aspose.3D Free Trial](https://releases.aspose.com/).

### Q: Kde mohu získat podporu pro Aspose.3D pro Javu?

A: Připojte se ke komunitě Aspose na [Aspose.3D Support Forum](https://forum.aspose.com/c/3d/18) pro pomoc a diskuse.

### Q: Jak získat dočasnou licenci pro Aspose.3D?

A: Získejte dočasnou licenci na stránce [Temporary License](https://purchase.aspose.com/temporary-license/).

### Q: Mohu použít tento kód s jinými 3D formáty jako STL?

A: Určitě – stačí změnit enum `FileFormat` při volání `scene.save`, např. `FileFormat.STL`.

## Závěr

Nyní ovládáte **how to use Aspose** pro úpravu poloměru koule, její přidání do scény a export výsledku jako OBJ souboru v Javě. Klidně experimentujte s dalšími primitivy, aplikujte materiály nebo řaďte více transformací pro vytvoření bohatších 3D modelů.

---

**Last Updated:** 2025-11-30  
**Tested With:** Aspose.3D for Java 24.11  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}