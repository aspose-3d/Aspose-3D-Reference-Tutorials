---
date: 2026-03-31
description: Naučte se, jak převést 3D na OBJ přidáním koule do scény, úpravou jejího
  poloměru a exportem souboru OBJ v Javě pomocí Aspose.3D.
linktitle: 'Convert 3D to OBJ: Add Sphere & Modify Radius in Java'
second_title: Aspose.3D Java API
title: 'Převod 3D na OBJ: Přidat kouli a upravit poloměr v Javě'
url: /cs/java/3d-objects-and-scenes/modify-sphere-radius/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Převod 3D na OBJ: Přidání koule a úprava poloměru v Javě

## Úvod

Pokud potřebujete **převést 3D na OBJ** rychle a programově, tento průvodce vám přesně ukáže, jak přidat kouli do scény, změnit její poloměr a zapsat výsledný soubor OBJ pomocí **Aspose.3D Java library**. Projdeme každý řádek kódu, vysvětlíme, proč je každý krok důležitý, a poskytneme tipy, jak se vyhnout běžným úskalím — abyste mohli tento workflow integrovat do her, CAD nástrojů nebo vědeckých vizualizací s jistotou.

## Rychlé odpovědi
- **Jaký je hlavní cíl tohoto tutoriálu?** Ukázat, jak převést 3D na OBJ vytvořením koule, úpravou jejího poloměru a exportem modelu v Javě.  
- **Která knihovna poskytuje 3D funkčnost?** Aspose.3D, kompletní **java 3d library tutorial**.  
- **Jak změním velikost koule?** Zavolejte `sphere.setRadius(double)` na instanci `Sphere`.  
- **Mohu zapsat soubor OBJ přímo z Javy?** Ano — použijte `scene.save("file.obj", FileFormat.WAVEFRONTOBJ)`.  
- **Potřebuji licenci pro produkci?** Bezplatná zkušební verze stačí pro vývoj; pro komerční použití je vyžadována trvalá licence.

## Jak převést 3D na OBJ pomocí Aspose.3D

### Co je Aspose.3D pro Java?

Aspose.3D je **java 3d library**, která umožňuje vývojářům vytvářet, upravovat a převádět 3D soubory bez jakýchkoli externích závislostí. Podporuje populární formáty jako OBJ, FBX, STL a další, což z ní činí ideální řešení pro hry, CAD nástroje a vědecké vizualizace.

### Proč převádět 3D na OBJ?

- **Univerzální kompatibilita** – OBJ je podporován prakticky každým 3D prohlížečem, herním enginem i modelovacím softwarem.  
- **Lehký export** – OBJ ukládá geometrii v prostém textovém formátu, který je snadno kontrolovatelný a laditelný.  
- **Flexibilita workflow** – Můžete generovat soubory OBJ za běhu z Java kódu na serveru, což umožňuje automatizované pipeline pro tvorbu assetů.

## Požadavky

- Základní znalost programování v Javě.  
- Knihovna Aspose.3D nainstalována – stáhněte ji z [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/).  
- JDK 8 nebo novější nainstalováno na vašem vývojovém počítači.

## Import balíčků

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Sphere;

import java.io.IOException;
```

## Průvodce krok za krokem

### Krok 1: Inicializace scény

```java
// ExStart:WorkingWithSphereRadius

// initialize a scene
Scene scene = new Scene();
```

Vytvoření `Scene` vám poskytuje kontejner pro veškerou geometrii, světla a kamery. Zde později **přidáme kouli do scény**.

### Krok 2: Inicializace koule

```java
// initialize a Sphere
Sphere sphere = new Sphere();
```

`Sphere` objekt začíná s výchozím poloměrem 1,0. Považujte ho za prázdné plátno pro tvar, který chcete exportovat.

### Krok 3: Nastavení požadovaného poloměru

```java
// set radius
sphere.setRadius(10);
```

Zde **píšeme kód ve stylu obj file java**, který nastavuje přesný poloměr. Nahraďte `10` libovolnou `double` hodnotou, která odpovídá vašim požadavkům na design.

### Krok 4: Přidání koule do scény

```java
// add sphere to the scene
scene.getRootNode().createChildNode(sphere);
```

Tento řádek **přidá kouli do scény** vytvořením podřízeného uzlu pod kořenovým uzlem. Je to okamžik, kdy se geometrie stane součástí grafu scény.

### Krok 5: Export modelu jako OBJ

```java
// save scene
scene.save("sphere.obj", FileFormat.WAVEFRONTOBJ);
```

Voláním `scene.save` **exportujete obj file java**‑style, efektivně **uložíte scénu jako obj**. Vygenerovaný `sphere.obj` lze otevřít v libovolném standardním 3D prohlížeči.

## Časté problémy a řešení

| Problém | Řešení |
|-------|----------|
| **Koule se v prohlížeči jeví příliš malá** | Ověřte, že je hodnota poloměru nastavena správně; pamatujte, že jednotky jsou libovolné, pokud nepoužijete transformační škálování. |
| **Exportovaný OBJ nemá materiál** | Aspose.3D zapisuje pouze geometrii; přidejte materiál ke kouli, pokud potřebujete textury (`sphere.setMaterial(...)`). |
| **Výjimka licence za běhu** | Ujistěte se, že máte načtený buď dočasný, nebo trvalý licenční soubor před vytvořením `Scene`. |

## Často kladené otázky

### Q: Kde mohu najít dokumentaci pro Aspose.3D pro Java?

A: Můžete se podívat na [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/) pro komplexní návod.

### Q: Jak si mohu stáhnout Aspose.3D pro Java?

A: Stáhněte knihovnu ze stránky s vydáními: [Download Aspose.3D for Java](https://releases.aspose.com/3d/java/).

### Q: Je k dispozici bezplatná zkušební verze pro Aspose.3D pro Java?

A: Ano, prozkoumejte funkce s bezplatnou zkušební verzí na [Aspose.3D Free Trial](https://releases.aspose.com/).

### Q: Kde mohu získat podporu pro Aspose.3D pro Java?

A: Připojte se ke komunitě Aspose na [Aspose.3D Support Forum](https://forum.aspose.com/c/3d/18) pro pomoc a diskuze.

### Q: Jak mohu získat dočasnou licenci pro Aspose.3D?

A: Získejte dočasnou licenci na [Temporary License](https://purchase.aspose.com/temporary-license/).

### Q: Mohu tento kód použít s jinými 3D formáty jako STL?

A: Rozhodně – stačí změnit výčtový typ `FileFormat` při volání `scene.save`, např. `FileFormat.STL`.

## Závěr

Nyní víte, jak **převést 3D na OBJ** přidáním koule, úpravou jejího poloměru a exportem výsledku pomocí Aspose.3D v Javě. Experimentujte s dalšími primitivy, aplikujte materiály nebo řaďte více transformací pro tvorbu bohatších modelů. Kdykoli potřebujete **uložit scénu jako obj** nebo **zapsat obj file java**, použijte stejný postup.

---

**Poslední aktualizace:** 2026-03-31  
**Testováno s:** Aspose.3D for Java 24.11  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}