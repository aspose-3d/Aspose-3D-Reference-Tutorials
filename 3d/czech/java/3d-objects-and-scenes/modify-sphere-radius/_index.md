---
date: 2026-07-27
description: Zjistěte, jak upravit poloměr koule v Javě a exportovat soubor OBJ v
  Javě pomocí Aspose.3D, přední knihovny Java 3D pro převod 3D na OBJ.
keywords:
- modify sphere radius java
- export obj file java
- aspose 3d java
lastmod: 2026-07-27
linktitle: 'Úprava poloměru koule v Javě: Převod 3D na OBJ pomocí Aspose.3D'
og_description: Upravte poloměr koule v Javě a exportujte soubor OBJ v Javě pomocí
  Aspose.3D. Tento tutoriál krok za krokem ukazuje, jak přidat kouli, změnit její
  velikost a uložit jako OBJ.
og_image_alt: 'Guide: modify sphere radius Java and export OBJ using Aspose.3D'
og_title: Úprava poloměru koule v Javě – Převod 3D na OBJ pomocí Aspose.3D
schemas:
- author: Aspose
  dateModified: '2026-07-27'
  description: Learn how to modify sphere radius Java and export OBJ file Java using
    Aspose.3D, the leading Java 3D library for converting 3D to OBJ.
  headline: 'Modify Sphere Radius Java: Convert 3D to OBJ with Aspose.3D'
  type: TechArticle
- description: Learn how to modify sphere radius Java and export OBJ file Java using
    Aspose.3D, the leading Java 3D library for converting 3D to OBJ.
  name: 'Modify Sphere Radius Java: Convert 3D to OBJ with Aspose.3D'
  steps:
  - name: Initialize a Scene
    text: '**Definition anchor:** The `Scene` class is Aspose.3D''s top‑level container
      that holds geometry, lights, and cameras for a 3D model. Creating a `Scene`
      gives you a workspace where you can add and manipulate objects. Creating a `Scene`
      gives you a container for all geometry, lights, and cameras. This'
  - name: Initialize a Sphere
    text: '**Definition anchor:** The `Sphere` class represents a geometric sphere
      primitive with a configurable radius, center, and material. By default it starts
      with a radius of 1.0. A `Sphere` object starts with a default radius of 1.0.
      Think of it as a blank canvas for the shape you want to export.'
  - name: Set the Desired Radius
    text: The `setRadius(double)` method updates the sphere’s size by assigning a
      new radius value in the same units used by the scene. Here we **write obj file
      java**‑style code that sets the exact radius. Replace `10` with any `double`
      value that matches your design requirements.
  - name: Add Sphere to the Scene
    text: This line **adds sphere to scene** by creating a child node under the root
      node. It’s the moment the geometry becomes part of the scene graph.
  - name: Export the Model as OBJ
    text: The `save(String, FileFormat)` method writes the entire scene to the specified
      file using the chosen format, such as OBJ. Calling `scene.save` **exports obj
      file java**‑style, effectively **save scene as obj**. The generated `sphere.obj`
      can be opened in any standard 3D viewer.
  type: HowTo
- questions:
  - answer: You can refer to the [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/)
      for comprehensive guidance.
    question: Where can I find the documentation for Aspose.3D for Java?
  - answer: 'Download the library from the releases page: [Download Aspose.3D for
      Java](https://releases.aspose.com/3d/java/).'
    question: How do I download Aspose.3D for Java?
  - answer: Yes, explore the features with a free trial by visiting [Aspose.3D Free
      Trial](https://releases.aspose.com/).
    question: Is there a free trial available for Aspose.3D for Java?
  - answer: Join the Aspose community at [Aspose.3D Support Forum](https://forum.aspose.com/c/3d/18)
      for assistance and discussions.
    question: Where can I get support for Aspose.3D for Java?
  - answer: Get a temporary license by visiting [Temporary License](https://purchase.aspose.com/temporary-license/).
    question: How can I obtain a temporary license for Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- modify sphere radius
- export OBJ
- aspose.3d
- java 3d
- 3d conversion
title: 'Úprava poloměru koule v Javě: Převod 3D na OBJ pomocí Aspose.3D'
url: /cs/java/3d-objects-and-scenes/modify-sphere-radius/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Převod 3D na OBJ: Přidání koule a úprava poloměru v Javě

## Úvod

Pokud potřebujete **rychle a programově upravit poloměr koule v Javě**, tento průvodce vám přesně ukáže, jak přidat kouli do scény, změnit její poloměr a zapsat výsledný OBJ soubor pomocí **Aspose.3D Java knihovny**. Projdeme každý řádek kódu, vysvětlíme, proč je každý krok důležitý, a poskytneme tipy, jak se vyhnout běžným úskalím — abyste mohli tento postup integrovat do her, CAD nástrojů nebo vědeckých vizualizací s jistotou.

## Rychlé odpovědi
- **Jaký je hlavní cíl tohoto tutoriálu?** Ukázat, jak převést 3D na OBJ vytvořením koule, úpravou jejího poloměru a exportem modelu v Javě.  
- **Která knihovna poskytuje 3D funkčnost?** Aspose.3D, kompletní **java 3d library tutorial**.  
- **Jak změním velikost koule?** Voláním `sphere.setRadius(double)` na instanci `Sphere`.  
- **Mohu z Java přímo zapsat OBJ soubor?** Ano — použijte `scene.save("file.obj", FileFormat.WAVEFRONTOBJ)`.  
- **Potřebuji licenci pro produkční nasazení?** Pro vývoj stačí bezplatná zkušební verze; pro komerční použití je vyžadována trvalá licence.

## Co je Aspose.3D pro Javu?

Aspose.3D pro Javu je komplexní **java 3d library**, která umožňuje vývojářům vytvářet, upravovat a převádět 3D soubory bez externích závislostí. Podporuje více než **50 vstupních a výstupních formátů** — včetně OBJ, FBX, STL a GLTF — což umožňuje bezproblémovou integraci do jakéhokoli 3‑D pipeline.

## Proč převádět 3D na OBJ?

Převod na OBJ poskytuje univerzálně čitelnou, textovou reprezentaci geometrie, kterou lze prohlížet, upravovat a importovat prakticky v jakékoli 3D aplikaci, což je ideální pro rychlé prototypování a výměnu aktiv napříč platformami.

- **Univerzální kompatibilita** – OBJ je podporován prakticky všemi 3D prohlížeči, herními enginy a modelovacími programy.  
- **Lehký export** – OBJ ukládá geometrii v prostém textovém formátu, který je snadno kontrolovatelný a laditelný.  
- **Flexibilita workflow** – Můžete generovat OBJ soubory za běhu z Java kódu na serveru, což umožňuje automatizované pipeline pro tvorbu aktiv.

## Předpoklady

- Základní znalost programování v Javě.  
- Nainstalovaná knihovna Aspose.3D — stáhněte ji z [dokumentace Aspose.3D pro Javu](https://reference.aspose.com/3d/java/).  
- Nainstalovaný JDK 8 nebo novější na vašem vývojovém počítači.

## Import balíčků

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Sphere;

import java.io.IOException;
```

## Jak upravit poloměr koule v Javě?

Načtěte objekt `Sphere`, zavolejte `setRadius` s požadovanou hodnotou a poté uložte scénu jako OBJ — tento celý workflow lze provést v pěti stručných krocích. Přístup funguje pro libovolný číselný poloměr a zaručuje, že exportovaný OBJ odráží přesně velikost, kterou zadáte.

### Krok 1: Inicializace scény

```java
// ExStart:WorkingWithSphereRadius

// initialize a scene
Scene scene = new Scene();
```

**Definiční kotva:** Třída `Scene` je nejvyšší kontejner Aspose.3D, který drží geometrii, světla a kamery pro 3D model. Vytvořením `Scene` získáte pracovní prostor, kde můžete přidávat a manipulovat s objekty.

Vytvořením `Scene` získáte kontejner pro veškerou geometrii, světla a kamery. Zde později **přidáme kouli do scény**.

### Krok 2: Inicializace koule

```java
// initialize a Sphere
Sphere sphere = new Sphere();
```

**Definiční kotva:** Třída `Sphere` představuje geometrický primitivní objekt koule s konfigurovatelným poloměrem, středem a materiálem. Ve výchozím nastavení má poloměr 1,0.

Objekt `Sphere` začíná s výchozím poloměrem 1,0. Považujte ho za čisté plátno pro tvar, který chcete exportovat.

### Krok 3: Nastavení požadovaného poloměru

Metoda `setRadius(double)` aktualizuje velikost koule přiřazením nové hodnoty poloměru ve stejných jednotkách, jaké používá scéna.

```java
// set radius
sphere.setRadius(10);
```

Zde **píšeme kód ve stylu write obj file java**, který nastaví přesný poloměr. Nahraďte `10` libovolnou `double` hodnotou, která odpovídá vašim návrhovým požadavkům.

### Krok 4: Přidání koule do scény

```java
// add sphere to the scene
scene.getRootNode().createChildNode(sphere);
```

Tento řádek **přidá kouli do scény** vytvořením podřízeného uzlu pod kořenovým uzlem. Je to okamžik, kdy se geometrie stane součástí grafu scény.

### Krok 5: Export modelu jako OBJ

Metoda `save(String, FileFormat)` zapíše celou scénu do zadaného souboru pomocí vybraného formátu, například OBJ.

```java
// save scene
scene.save("sphere.obj", FileFormat.WAVEFRONTOBJ);
```

Voláním `scene.save` **exportujete obj file java** — efektivně **uložíte scénu jako obj**. Vygenerovaný `sphere.obj` lze otevřít v libovolném standardním 3D prohlížeči.

## Časté problémy a řešení

| Problém | Řešení |
|-------|----------|
| **Koule se ve vieweru zobrazuje příliš malá** | Ověřte, že je hodnota poloměru nastavena správně; pamatujte, že jednotky jsou libovolné, pokud nepoužijete transformační měřítko. |
| **Exportovaný OBJ nemá materiál** | Aspose.3D zapisuje pouze geometrii; přidejte materiál ke kouli, pokud potřebujete textury (`sphere.setMaterial(...)`). |
| **Výjimka licence během běhu** | Ujistěte se, že máte načtený dočasný nebo trvalý licenční soubor před vytvořením `Scene`. |

## Často kladené otázky

**Q: Kde najdu dokumentaci k Aspose.3D pro Javu?**  
A: Můžete se podívat na [dokumentaci k Aspose.3D pro Javu](https://reference.aspose.com/3d/java/) pro komplexní návod.

**Q: Jak stáhnout Aspose.3D pro Javu?**  
A: Stáhněte knihovnu ze stránky vydání: [Stáhnout Aspose.3D pro Javu](https://releases.aspose.com/3d/java/).

**Q: Je k dispozici bezplatná zkušební verze Aspose.3D pro Javu?**  
A: Ano, prozkoumejte funkce s bezplatnou zkušební verzí na [Bezplatná zkušební verze Aspose.3D](https://releases.aspose.com/).

**Q: Kde mohu získat podporu pro Aspose.3D pro Javu?**  
A: Připojte se ke komunitě Aspose na [Fórum podpory Aspose.3D](https://forum.aspose.com/c/3d/18) pro pomoc a diskuze.

**Q: Jak získat dočasnou licenci pro Aspose.3D?**  
A: Získejte dočasnou licenci na stránce [Dočasná licence](https://purchase.aspose.com/temporary-license/).

**Q: Mohu použít tento kód s jinými 3D formáty, jako je STL?**  
A: Rozhodně — stačí změnit výčtový typ `FileFormat` při volání `scene.save`, např. `FileFormat.STL`.

**Poslední aktualizace:** 2026-07-27  
**Testováno s:** Aspose.3D pro Javu 24.11  
**Autor:** Aspose

## Související tutoriály

- [Jak nastavit normály na 3D objektech v Javě pomocí Aspose.3D Java API](/3d/java/geometry/set-up-normals-on-3d-objects/)
- [Jak vložit texturu do FBX v Javě – Použití materiálů na 3D objekty pomocí Aspose.3D](/3d/java/geometry/apply-materials-to-3d-objects/)
- [Jak změnit orientaci roviny a exportovat OBJ v Javě](/3d/java/3d-scenes-and-models/change-plane-orientation/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< blocks/products/products-backtop-button >}}
{{< /blocks/products/pf/main-wrap-class >}}