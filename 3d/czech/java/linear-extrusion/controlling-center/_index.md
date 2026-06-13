---
date: 2026-06-13
description: Naučte se tutoriál 3D grafiky v Javě o řízení středu v lineární extruzi
  s Aspose.3D, včetně nastavení poloměru zaoblení a uložení souboru OBJ v Javě.
keywords:
- create 3d mesh java
- set rounding radius
- export 3d model obj
- save obj file java
- aspose 3d export obj
linktitle: Řízení středu v lineární extruzi s Aspose.3D pro Javu
schemas:
- author: Aspose
  dateModified: '2026-06-13'
  description: Learn a java 3d graphics tutorial on controlling the center in linear
    extrusion with Aspose.3D, including how to set rounding radius and save OBJ file
    java.
  headline: Create 3D Mesh Java – Center in Linear Extrusion
  type: TechArticle
- description: Learn a java 3d graphics tutorial on controlling the center in linear
    extrusion with Aspose.3D, including how to set rounding radius and save OBJ file
    java.
  name: Create 3D Mesh Java – Center in Linear Extrusion
  steps:
  - name: Set Up the Base Profile
    text: First, create the 2‑D shape that will be extruded. Here we use a rectangle
      and **set rounding radius** to 0.3, which smooths the corners and demonstrates
      how to **round extrusion corners**.
  - name: Create a 3D Scene
    text: '**Scene** is the top‑level container that holds all 3‑D objects, lights,
      and cameras.'
  - name: Add Left and Right Nodes
    text: A **Node** represents a transformable object in the scene graph, allowing
      positioning and hierarchy.
  - name: Linear Extrusion – No Center (Left Node)
    text: '**LinearExtrusion** converts a 2‑D profile into a 3‑D mesh by sweeping
      it along a straight line. **setCenter(boolean)** toggles whether the extrusion
      is centered around the profile origin.'
  - name: Add a Ground Plane for Reference (Left Node)
    text: A thin box acts as a visual floor, helping you see the extrusion’s orientation.
  - name: Linear Extrusion – Centered (Right Node)
    text: Now repeat the extrusion, this time enabling `center`. The geometry will
      be symmetric around the profile’s origin, giving you a perfectly balanced **create
      3d mesh java** result.
  - name: Add a Ground Plane for Reference (Right Node)
    text: Same ground plane for the right side, making the comparison clear.
  - name: Save the 3D Scene
    text: Finally, export the entire scene to a Wavefront OBJ file – a format readily
      usable in most 3‑D editors. The `save` method automatically converts the mesh
      to the OBJ specification, allowing you to **save obj file java** without additional
      post‑processing.
  type: HowTo
- questions:
  - answer: It determines whether the extrusion is symmetric around the profile's
      origin.
    question: What does the center property do?
  - answer: A temporary license works for testing; a full license is required for
      production.
    question: Do I need a license to run the code?
  - answer: The scene is saved as a Wavefront OBJ file.
    question: Which file format is used for the result?
  - answer: Yes, use `setSlices(int)` on the `LinearExtrusion` object.
    question: Can I change the number of slices?
  - answer: Absolutely – it supports all modern Java versions.
    question: Is Aspose.3D compatible with Java 8+?
  type: FAQPage
second_title: Aspose.3D Java API
title: Vytvořit 3D Mesh v Javě – Střed v lineární extruzi
url: /cs/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Vytvoření 3D sítě Java – Střed v lineární extruzi

## Úvod

Pokud vytváříte 3‑D vizualizace v Javě, zvládnutí technik extruze je nezbytné. Tento **java 3d graphics tutorial** vám ukáže, jak **create 3d mesh java** objekty ovládat střed lineární extruze pomocí Aspose.3D pro Java. Na konci tohoto průvodce pochopíte, proč je vlastnost `center` důležitá, jak **set rounding radius**, a jak **save obj file java**‑kompatibilní výstup. Také uvidíte, jak **export 3d model obj** pro použití v jakémkoli hlavním 3‑D editoru.

## Rychlé odpovědi
- **Co dělá vlastnost center?** Určuje, zda je extruze symetrická kolem počátku profilu.  
- **Potřebuji licenci pro spuštění kódu?** Dočasná licence funguje pro testování; pro produkci je vyžadována plná licence.  
- **Jaký formát souboru se používá pro výsledek?** Scéna je uložena jako soubor Wavefront OBJ.  
- **Mohu změnit počet řezů?** Ano, použijte `setSlices(int)` na objektu `LinearExtrusion`.  
- **Je Aspose.3D kompatibilní s Java 8+?** Naprosto – podporuje všechny moderní verze Javy.

## Co je java 3d graphics tutorial?

**java 3d graphics tutorial** je průvodce krok za krokem, který vás učí, jak používat Java knihovny k vytváření, manipulaci a renderování trojrozměrných objektů. V tomto tutoriálu se naučíte **create 3d mesh java** převodem 2‑D profilu na kompletní 3‑D model, ovládat jeho centrální zarovnání, zaoblit rohy extruze a nakonec exportovat výsledek jako OBJ soubor, který může číst jakýkoli 3‑D program.

## Proč použít Aspose.3D pro Java?

Aspose.3D pro Java poskytuje vysoceúrovňové API, které eliminuje potřebu ručních výpočtů sítí, což vám umožní soustředit se na design místo na nízkoúrovňovou geometrii. Podporuje **více než 50 vstupních a výstupních formátů**—včetně OBJ, FBX, STL a GLTF—takže můžete **export 3d model obj** nebo jakýkoli jiný formát jedním voláním metody. Knihovna zpracovává scény o stovkách stránek bez načítání celého souboru do paměti, poskytuje **až 3× vyšší výkon** ve srovnání s čistými OpenGL pipeline na typickém serverovém hardwaru.

## Požadavky

1. **Java Development Environment** – Nainstalovaný JDK 8 nebo novější.  
2. **Aspose.3D for Java** – Stáhněte knihovnu a dokumentaci [zde](https://reference.aspose.com/3d/java/).  
3. **Document Directory** – Vytvořte složku na svém počítači pro ukládání generovaných souborů; budeme na ni odkazovat jako **„Your Document Directory.“**

## Import balíčků

Ve svém Java IDE importujte třídy Aspose.3D, které budete potřebovat. To poskytne kompilátoru přístup k funkcím extruze a tvorby scény.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Postupný průvodce

### Krok 1: Nastavení základního profilu

Nejprve vytvořte 2‑D tvar, který bude extrudován. Zde použijeme obdélník a **set rounding radius** na 0,3, což zaoblí rohy a ukazuje, jak **round extrusion corners**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### Krok 2: Vytvoření 3D scény

**Scene** je kontejner nejvyšší úrovně, který obsahuje všechny 3‑D objekty, světla a kamery.

```java
Scene scene = new Scene();
```

### Krok 3: Přidání levých a pravých uzlů

**Node** představuje transformovatelný objekt v grafu scény, umožňující umístění a hierarchii.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Krok 4: Lineární extruze – bez středu (levý uzel)

**LinearExtrusion** převádí 2‑D profil na 3‑D síť tím, že ho provádí podél přímé linie.  
**setCenter(boolean)** přepíná, zda je extruze centrovaná kolem počátku profilu.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

### Krok 5: Přidání podlahové roviny pro referenci (levý uzel)

Tenčí krabice funguje jako vizuální podlaha, pomáhá vám vidět orientaci extruze.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

### Krok 6: Lineární extruze – centrovaná (pravý uzel)

Nyní opakujte extruzi, tentokrát povolíte `center`. Geometrie bude symetrická kolem počátku profilu, což vám poskytne dokonale vyvážený výsledek **create 3d mesh java**.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

### Krok 7: Přidání podlahové roviny pro referenci (pravý uzel)

Stejná podlahová rovina pro pravou stranu, aby byl srovnání jasné.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

### Krok 8: Uložení 3D scény

Nakonec exportujte celou scénu do souboru Wavefront OBJ – formátu snadno použitelného ve většině 3‑D editorů. Metoda `save` automaticky převádí síť do specifikace OBJ, což vám umožní **save obj file java** bez dalšího post‑processingu.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Časté problémy a řešení

| Problém | Proč se to děje | Řešení |
|---------|----------------|--------|
| **Extruze se zdá posunutá** | `setCenter(false)` nechává profil ukotvený v jeho rohu. | Použijte `setCenter(true)` pro symetrické výsledky. |
| **Soubor OBJ je prázdný** | Cesta výstupního adresáře je nesprávná nebo chybí oprávnění k zápisu. | Ověřte, že `MyDir` ukazuje na existující složku a aplikace má právo zápisu. |
| **Zaoblené rohy vypadají ostré** | Poloměr zaoblení je příliš malý vzhledem k velikosti obdélníku. | Zvyšte hodnotu poloměru (např. `setRoundingRadius(0.5)`). |

## Často kladené otázky

### Q1: Mohu použít Aspose.3D pro Java v komerčních projektech?

A1: Ano, Aspose.3D pro Java je k dispozici pro komerční použití. Pro podrobnosti o licencování navštivte [zde](https://purchase.aspose.com/buy).

### Q2: Je k dispozici bezplatná zkušební verze?

A2: Ano, můžete vyzkoušet bezplatnou zkušební verzi Aspose.3D pro Java [zde](https://releases.aspose.com/).

### Q3: Kde mohu najít podporu pro Aspose.3D pro Java?

A3: Fórum komunity Aspose.3D je skvělým místem pro získání podpory a sdílení zkušeností. Navštivte fórum [zde](https://forum.aspose.com/c/3d/18).

### Q4: Potřebuji dočasnou licenci pro testování?

A4: Ano, pokud potřebujete dočasnou licenci pro testování, můžete ji získat [zde](https://purchase.aspose.com/temporary-license/).

### Q5: Kde najdu dokumentaci?

A5: Dokumentace pro Aspose.3D pro Java je k dispozici [zde](https://reference.aspose.com/3d/java/).

## Závěr

Po dokončení tohoto **java 3d graphics tutorial** nyní víte, jak **create 3d mesh java** objekty, ovládat střed lineární extruze, upravit poloměr zaoblení a **save obj file java** výstup pomocí Aspose.3D. Tyto techniky vám poskytují detailní kontrolu nad symetrií sítě, což je zásadní pro herní assety, CAD prototypy a vědecké vizualizace. Nebojte se experimentovat s různými profily, počty řezů a exportními formáty, abyste rozšířili svou 3‑D toolbox.

---

**Last Updated:** 2026-06-13  
**Tested With:** Aspose.3D for Java 24.11  
**Author:** Aspose

## Související tutoriály

- [Vytvoření 3D extruze Java s Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Jak nastavit směr v lineární extruzi s Aspose.3D pro Java](/3d/java/linear-extrusion/setting-direction/)
- [Vytvoření 3D scény s twistem v lineární extruzi – Aspose.3D pro Java](/3d/java/linear-extrusion/applying-twist/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}