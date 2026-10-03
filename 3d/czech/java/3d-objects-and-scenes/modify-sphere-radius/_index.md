---
date: 2026-10-03
description: Naučte se, jak vytvořit kouli v Java a exportovat soubor OBJ pomocí Aspose.3D,
  přední Java 3D knihovny pro převod 3D modelů.
images:
- /java/3d-objects-and-scenes/modify-sphere-radius/og-image.png
keywords:
- create sphere java
- save 3d as obj
- java convert 3d model
- write obj file java
lastmod: 2026-10-03
linktitle: 'Vytvořit kouli v Java: převod 3D na OBJ pomocí Aspose.3D'
og_description: Naučte se, jak vytvořit kouli v Java a exportovat soubor OBJ pomocí
  Aspose.3D. Tento krok‑za‑krokem průvodce ukazuje, jak přidat kouli, změnit její
  poloměr a uložit jako OBJ.
og_image_alt: 'Guide: create sphere java and export OBJ using Aspose.3D'
og_title: Vytvořit kouli v Java – Export OBJ pomocí Aspose.3D
schemas:
- author: Aspose
  dateModified: '2026-10-03'
  description: Learn how to create sphere java and export OBJ file using Aspose.3D,
    the leading Java 3D library for converting 3D models.
  headline: 'Create sphere java: Convert 3D to OBJ with Aspose.3D'
  type: TechArticle
- description: Learn how to create sphere java and export OBJ file using Aspose.3D,
    the leading Java 3D library for converting 3D models.
  name: 'Create sphere java: Convert 3D to OBJ with Aspose.3D'
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
title: 'Vytvořit kouli v Java: převod 3D na OBJ pomocí Aspose.3D'
url: /cs/java/3d-objects-and-scenes/modify-sphere-radius/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Vytvořte kouli v Javě a exportujte do OBJ

## Úvod

V tomto tutoriálu se naučíte, jak **vytvořit kouli v Javě**, upravit její poloměr a poté **uložit 3D jako OBJ** pomocí knihovny Aspose.3D Java. Projdeme každý řádek kódu, vysvětlíme, proč je každý krok důležitý, a poskytneme vám praktické tipy, abyste mohli tento workflow s jistotou začlenit do her, CAD nástrojů nebo vědeckých vizualizací.

## Rychlé odpovědi
- **Jaký je hlavní cíl tohoto tutoriálu?** Ukázat, jak vytvořit kouli v Javě, upravit její velikost a exportovat model jako OBJ pomocí Javy.
- **Která knihovna poskytuje 3D funkčnost?** Aspose.3D, a full‑featured **java 3d library tutorial**.
- **Jak změním velikost koule?** Call `sphere.setRadius(double)` on the `Sphere` instance.
- **Mohu zapisovat soubor OBJ přímo z Javy?** Yes—use `scene.save("file.obj", FileFormat.WAVEFRONTOBJ)`.
- **Potřebuji licenci pro produkci?** A free trial is fine for development; a permanent license is required for commercial use.

## Co je Aspose.3D pro Javu?

Aspose.3D pro Javu je komplexní **java 3d library**, která umožňuje vývojářům vytvářet, upravovat a konvertovat 3D soubory bez externích závislostí. Podporuje více než **50 vstupních a výstupních formátů**—včetně OBJ, FBX, STL a GLTF—což umožňuje plynulou integraci do jakéhokoli 3‑D pipeline.

## Proč konvertovat 3D do OBJ?

Konverze do OBJ vám poskytuje univerzálně podporovanou, textovou reprezentaci geometrie, kterou může číst jakýkoli 3D nástroj, což je ideální pro rychlé prototypování, výměnu aktiv napříč platformami a snadné ladění dat vrcholů. Protože soubory OBJ jsou lehké a čitelné pro člověka, můžete je v případě potřeby prohlížet nebo upravovat pomocí jednoduchého textového editoru.

## Požadavky

- Základní znalost programování v Javě.  
- Knihovna Aspose.3D nainstalována – stáhněte ji z [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/).  
- JDK 8 nebo novější nainstalovaný na vašem vývojovém počítači.

## Import balíčků

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Sphere;

import java.io.IOException;
```

## Jak upravit poloměr koule v Javě?

`Sphere` je geometrický primitiv představující kouli v Aspose.3D.

Načtěte objekt `Sphere`, zavolejte `setRadius` s požadovanou hodnotou a poté uložte scénu jako OBJ — tento celý workflow lze provést v pěti stručných krocích. Přístup funguje pro jakýkoli číselný poloměr a zajišťuje, že exportovaný OBJ odráží přesně velikost, kterou zadáte.

### Krok 1: Inicializace scény

```java
// ExStart:WorkingWithSphereRadius

// initialize a scene
Scene scene = new Scene();
```

**Definition anchor:** Třída `Scene` je nejvyšší kontejner Aspose.3D, který obsahuje geometrii, světla a kamery pro 3D model. Vytvořením `Scene` získáte pracovní prostor, kde můžete přidávat a manipulovat s objekty.

Vytvořením `Scene` získáte kontejner pro veškerou geometrii, světla a kamery. Zde později **přidáme kouli do scény**.

### Krok 2: Inicializace koule

```java
// initialize a Sphere
Sphere sphere = new Sphere();
```

**Definition anchor:** Třída `Sphere` představuje geometrický primitiv koule s konfigurovatelným poloměrem, středem a materiálem. Ve výchozím nastavení má poloměr 1.0.

Objekt `Sphere` začíná s výchozím poloměrem 1.0. Považujte ho za prázdné plátno pro tvar, který chcete exportovat.

### Krok 3: Nastavte požadovaný poloměr

**Definition anchor:** Metoda `setRadius(double)` nastavuje poloměr koule ve stejných jednotkách, které používá scéna.  

```java
// set radius
sphere.setRadius(10);
```

Zde máme kód ve stylu **write obj file java**, který nastavuje přesný poloměr. Nahraďte `10` libovolnou hodnotou typu `double`, která odpovídá vašim návrhovým požadavkům.

### Krok 4: Přidejte kouli do scény

```java
// add sphere to the scene
scene.getRootNode().createChildNode(sphere);
```

Tento řádek **přidá kouli do scény** vytvořením podřízeného uzlu pod kořenovým uzlem. Je to okamžik, kdy se geometrie stane součástí grafu scény.

### Krok 5: Exportujte model jako OBJ

```java
// save scene
scene.save("sphere.obj", FileFormat.WAVEFRONTOBJ);
```

Metoda `save(String, FileFormat)` zapíše celou scénu do určeného souboru pomocí zvoleného formátu, například OBJ. Voláním `scene.save` **exportuje obj file java**‑style, efektivně **uloží scénu jako obj**. Vygenerovaný `sphere.obj` lze otevřít v libovolném standardním 3D prohlížeči.

## Časté problémy a řešení

| Issue | Solution |
|-------|----------|
| **Koule se v prohlížeči zobrazuje příliš malá** | Ověřte, že je hodnota poloměru nastavena správně; pamatujte, že jednotky jsou libovolné, pokud nepoužijete škálovací transformaci. |
| **Exportovaný OBJ nemá materiál** | Aspose.3D zapisuje pouze geometrii; přidejte materiál ke kouli, pokud potřebujete textury (`sphere.setMaterial(...)`). |
| **Výjimka licence za běhu** | Ujistěte se, že máte načtený buď dočasný, nebo trvalý licenční soubor před vytvořením `Scene`. |

## Často kladené otázky

**Q: Kde mohu najít dokumentaci pro Aspose.3D pro Javu?**  
A: Můžete se podívat na [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/) pro komplexní návod.

**Q: Jak si mohu stáhnout Aspose.3D pro Javu?**  
A: Stáhněte knihovnu ze stránky vydání: [Download Aspose.3D for Java](https://releases.aspose.com/3d/java/).

**Q: Je k dispozici bezplatná zkušební verze pro Aspose.3D pro Javu?**  
A: Ano, prozkoumejte funkce pomocí bezplatné zkušební verze na [Aspose.3D Free Trial](https://releases.aspose.com/).

**Q: Kde mohu získat podporu pro Aspose.3D pro Javu?**  
A: Připojte se ke komunitě Aspose na [Aspose.3D Support Forum](https://forum.aspose.com/c/3d/18) pro pomoc a diskuse.

**Q: Jak mohu získat dočasnou licenci pro Aspose.3D?**  
A: Získejte dočasnou licenci na stránce [Temporary License](https://purchase.aspose.com/temporary-license/).

**Q: Mohu tento kód použít s jinými 3D formáty, jako je STL?**  
A: Určitě – stačí změnit enum `FileFormat` při volání `scene.save`, např. `FileFormat.STL`.

---

**Poslední aktualizace:** 2026-10-03  
**Testováno s:** Aspose.3D for Java 24.11  
**Autor:** Aspose

## Související tutoriály

- [Jak nastavit normály na 3D objektech v Javě pomocí Aspose.3D Java API](/3d/java/geometry/set-up-normals-on-3d-objects/)
- [Jak vložit texturu do FBX v Javě – Použít materiály na 3D objekty pomocí Aspose.3D](/3d/java/geometry/apply-materials-to-3d-objects/)
- [Jak změnit orientaci roviny a exportovat OBJ v Javě](/3d/java/3d-scenes-and-models/change-plane-orientation/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}