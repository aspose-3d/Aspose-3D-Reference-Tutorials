---
date: 2026-08-12
description: Jak generovat 3D pomocí Aspose.3D – vytvořit válec s posunutým vrcholem
  v jazyce Java, přidat podřízený uzel, nastavit posunutý vrchol, vygenerovat 3D model,
  exportovat OBJ a vyhodnotit pomocí dočasné licence.
keywords:
- how to generate 3d
- aspose temporary license
- export obj file
- set offset top
- java 3d cylinder
lastmod: 2026-08-12
linktitle: Jak generovat 3D – vytvořit válec s posunutým vrcholem (Java)
og_description: Jak generovat 3D s Aspose.3D pro Java. Naučte se posouvat vrcholy
  válců, přidávat podřízené uzly a exportovat OBJ pomocí dočasné licence.
og_image_alt: Guide showing Java code to create a cylinder with offset top and export
  OBJ using Aspose.3D
og_title: Jak generovat 3D – vytvořit válec s posunutým vrcholem (Java)
schemas:
- author: Aspose
  dateModified: '2026-08-12'
  description: How to generate 3d using Aspose.3D – create a cylinder with offset
    top in Java, add child node, set offset top, generate 3D model, export OBJ, and
    evaluate with a temporary license.
  headline: How to generate 3d – create cylinder with offset top (Java)
  type: TechArticle
- description: How to generate 3d using Aspose.3D – create a cylinder with offset
    top in Java, add child node, set offset top, generate 3D model, export OBJ, and
    evaluate with a temporary license.
  name: How to generate 3d – create cylinder with offset top (Java)
  steps:
  - name: Create a Java 3D scene
    text: '`Scene` is the top‑level container that holds all nodes, meshes, lights,
      and cameras in a 3‑D environment.'
  - name: Initialize cylinder with offset top
    text: '`Cylinder` represents a cylindrical mesh and provides properties such as
      radius, height, and offset.'
  - name: Add child node Java – attach the first cylinder
    text: '`Node` is an element in the scene graph that can hold geometry and transformations.'
  - name: Java export OBJ – save the scene as OBJ
    text: '`FileFormat` enumerates the supported export formats such as OBJ, STL,
      and FBX.'
  type: HowTo
- questions:
  - answer: Yes, it works seamlessly with Eclipse, IntelliJ IDEA, NetBeans, and other
      IDEs.
    question: Is Aspose.3D compatible with different Java IDEs?
  - answer: Absolutely! Use the `Material` class to assign textures and surface properties.
    question: Can I apply textures to the created 3D objects?
  - answer: Various licensing models are available; you can explore them **[Aspose
      purchase page](https://purchase.aspose.com/buy)**.
    question: Are there licensing options for Aspose.3D?
  - answer: Join the **[Aspose.3D community forum](https://forum.aspose.com/c/3d/18)**
      for support and discussion.
    question: How can I get help or share experiences?
  - answer: Yes, an **aspose temporary license** can be obtained for evaluation **[temporary
      license request page](https://purchase.aspose.com/temporary-license/)**.
    question: Is a temporary license available for testing?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- generate 3d
- aspose.3d
- java cylinder offset
title: Jak generovat 3D – vytvořit válec s posunutým vrcholem (Java)
url: /cs/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak generovat 3D – vytvořit válec s posunutým vrcholem (Java)

## Úvod

Pokud chcete **vytvořit válec** s vlastním posunutým vrcholem v 3D scéně založené na Javě, Aspose.3D proces zjednodušuje. V tomto tutoriálu projdeme každý krok – od nastavení scény po export finálního modelu jako souboru OBJ – abyste mohli integrovat válce s posunutým vrcholem do svých aplikací s jistotou. Na konci průvodce také pochopíte, jak **aspose temporary license** umožňuje vyhodnotit tyto funkce bez úplného zakoupení.

## Rychlé odpovědi
- **Jaká knihovna se používá?** Aspose.3D for Java  
- **Mohu posunout vrchol válce?** Ano, pomocí `setOffsetTop`  
- **Jak přidám podřízený uzel v Javě?** Zavolejte `createChildNode` na kořenovém uzlu  
- **Do jakého formátu mohu exportovat?** Wavefront OBJ (`export obj file`)  
- **Potřebuji licenci pro testování?** **aspose temporary license** je k dispozici pro vyhodnocení  

## Co je Aspose temporary license?

**aspose temporary license** je krátkodobý, bezplatný evaluační klíč, který odemkne kompletní sadu funkcí Aspose.3D pro Java během vývoje a testování. Odstraňuje evaluační vodoznaky a umožňuje generovat 3D soubory, jako OBJ, STL nebo FBX, přesně jako placená licence.

## Proč používat Aspose.3D pro Java?

Aspose.3D poskytuje vysoceúrovňové, multiplatformní API, které zjednodušuje tvorbu a export 3D. Obsahuje vestavěné exportéry pro více než 30 formátů, podporuje hierarchie scénových grafů a umožňuje soustředit se na geometrii místo nízkoúrovňové manipulace s meshem.

- **Vysoceúrovňové API:** Není potřeba spravovat nízkoúrovňová data meshe.  
- **Multiplatformní:** Funguje v jakémkoli prostředí kompatibilním s JVM.  
- **Vestavěné exportéry:** Přímé ukládání do OBJ, STL, FBX a dalších – Aspose.3D podporuje **30+** exportních formátů.  
- **Rozšiřitelné:** Snadno přidávejte podřízené uzly, aplikujte transformace a integrujte s dalšími Java knihovnami.  

## Předpoklady

- **Java Development Kit (JDK)** – nainstalovaná kompatibilní verze.  
- **Aspose.3D for Java library** – stáhněte nejnovější JAR z oficiální stránky **[Aspose.3D for Java download page](https://releases.aspose.com/3d/java/)**.  
- IDE dle vašeho výběru (Eclipse, IntelliJ IDEA, NetBeans, atd.).  

## Import balíčků

Následující importy přinášejí nezbytné třídy Aspose.3D potřebné k vytvoření a exportu válce.

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Průvodce krok za krokem

### Krok 1: Vytvořit Java 3D scénu

`Scene` je kontejner nejvyšší úrovně, který v 3‑D prostředí obsahuje všechny uzly, meshe, světla a kamery.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### Krok 2: Inicializovat válec s posunutým vrcholem

`Cylinder` představuje válcový mesh a poskytuje vlastnosti jako poloměr, výška a posunutí.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### Krok 3: Přidat podřízený uzel v Javě – připojit první válec

`Node` je prvek v grafu scény, který může obsahovat geometrii a transformace.

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### Krok 4: Inicializovat druhý válec (bez posunutí)

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### Krok 5: Přidat podřízený uzel v Javě – připojit druhý válec

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Krok 6: Java export OBJ – uložit scénu jako OBJ

`FileFormat` vyjmenovává podporované exportní formáty jako OBJ, STL a FBX.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

## Jak vygenerovat 3D model a exportovat OBJ v Javě

Pro vygenerování 3D modelu načtěte scénu, aplikujte potřebné transformace a poté zavolejte `scene.save("path/CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ)`. **aspose temporary license** odstraňuje evaluační vodoznak, což vám umožní vytvářet produkční OBJ soubory bez zakoupení plné licence.

## Reálné příklady použití

- **Architektonická vizualizace:** Válce s posunutým vrcholem modelují sloupy, které se směrem ke stropu zužují.  
- **Mechanické součásti:** Vytvářejte písty nebo pouzdra ozubených kol, kde je horní povrch úmyslně posunut.  
- **Herní assety:** Produkujte různorodé tvary sloupů za běhu, čímž snižujete potřebu ručně vytvářených meshů.  

## Časté problémy a řešení

| Problém | Příčina | Řešení |
|-------|--------|-----|
| **OBJ soubor je prázdný** | Scéna nebyla správně uložena nebo je špatná cesta. | Ověřte, že výstupní adresář existuje a máte oprávnění k zápisu. |
| **Posunutí nebylo aplikováno** | Používáte starší verzi Aspose.3D. | Aktualizujte na nejnovější knihovnu, kde je `setOffsetTop` podporováno. |
| **Podřízený uzel není viditelný** | Transformace nebyla aplikována. | Ujistěte se, že po vytvoření podřízeného uzlu zavoláte `getTransform().setTranslation`. |

## Často kladené otázky

**Q: Je Aspose.3D kompatibilní s různými Java IDE?**  
A: Ano, funguje bez problémů s Eclipse, IntelliJ IDEA, NetBeans a dalšími IDE.

**Q: Mohu na vytvořené 3D objekty aplikovat textury?**  
A: Rozhodně! Použijte třídu `Material` k přiřazení textur a povrchových vlastností.

**Q: Existují licenční možnosti pro Aspose.3D?**  
A: K dispozici jsou různé licenční modely; můžete je prozkoumat na **[Aspose purchase page](https://purchase.aspose.com/buy)**.

**Q: Jak mohu získat pomoc nebo sdílet zkušenosti?**  
A: Připojte se k **[Aspose.3D community forum](https://forum.aspose.com/c/3d/18)** pro podporu a diskuzi.

**Q: Je dočasná licence k dispozici pro testování?**  
A: Ano, **aspose temporary license** lze získat pro vyhodnocení na **[temporary license request page](https://purchase.aspose.com/temporary-license/)**.

**Poslední aktualizace:** 2026-08-12  
**Testováno s:** Aspose.3D for Java 24.12 (latest)  
**Autor:** Aspose

{{< blocks/products/products-backtop-button >}}

## Související tutoriály

- [How to Create Cylinder Models with Aspose.3D for Java](/3d/java/cylinders/)
- [How to create cylinder fan shape using Aspose.3D for Java](/3d/java/cylinders/creating-fan-cylinders/)
- [Create Child Nodes and Export FBX in Java with Aspose.3D](/3d/java/geometry/build-node-hierarchies/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}