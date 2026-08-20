---
date: 2026-05-24
description: Naučte se, jak vytvořit 3D extruzi se slices pomocí Aspose.3D for Java.
  Tento krok‑za‑krokem průvodce pokrývá lineární extruzi, nastavení poloměru zaoblení
  a export do OBJ.
keywords:
- create 3d extrusion java
- Aspose 3D slices
- linear extrusion Java
linktitle: Vytvořte 3D extruzi se slices – Aspose.3D for Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  headline: Create 3D Extrusion with Slices – Aspose.3D for Java
  type: TechArticle
- description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  name: Create 3D Extrusion with Slices – Aspose.3D for Java
  steps:
  - name: Set up the scene and define the profile
    text: '`RectangleShape` is a class that defines a 2‑D rectangle profile. First
      we create a `RectangleShape` and give it a **rounding radius** so the corners
      are smooth. `Scene` is the root container for all nodes and geometry. Then we
      initialise a new `Scene` that will hold all geometry.'
  - name: Create child node objects for each extrusion
    text: '`Node` represents an element in the scene graph that can hold geometry
      and transformations. Every piece of geometry lives under a `Node`. Here we generate
      two sibling nodes – one for a low‑slice extrusion and another for a high‑slice
      extrusion – and move the left node a little to the side so the res'
  - name: Perform linear extrusion and set slices
    text: '`LinearExtrusion` is the class that creates a solid by sweeping a profile
      linearly. `LinearExtrusion` is Aspose.3D''s class that generates a solid by
      extruding a 2‑D profile along a straight line. Using an **anonymous inner class**
      we call `setSlices` to control the smoothness. The left node gets onl'
  - name: Export OBJ – save the scene
    text: Finally we write the scene to a Wavefront OBJ file, a format widely supported
      by 3‑D editors and game engines. This demonstrates the **export OBJ Java** capability
      of Aspose.3D.
  type: HowTo
- questions:
  - answer: You can download the library [here](https://releases.aspose.com/3d/java/).
    question: How can I download Aspose.3D for Java?
  - answer: Refer to the documentation [here](https://reference.aspose.com/3d/java/).
    question: Where can I find the documentation for Aspose.3D?
  - answer: Yes, you can explore a free trial [here](https://releases.aspose.com/).
    question: Is there a free trial available?
  - answer: Visit the support forum [here](https://forum.aspose.com/c/3d/18).
    question: How can I get support for Aspose.3D?
  - answer: Yes, a temporary license can be obtained [here](https://purchase.aspose.com/temporary-license/).
    question: Can I purchase a temporary license?
  type: FAQPage
second_title: Aspose.3D Java API
title: Vytvořte 3D extruzi se slices – Aspose.3D for Java
url: /cs/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Vytvořte 3D extruzi s řezy – Aspose.3D pro Javu

## Úvod

Pokud potřebujete **vytvořit 3D extruzi** objektů, které vypadají hladce a přesně, klíčové je řídit počet řezů. V tomto tutoriálu vás provedeme, jak specifikovat řezy při provádění lineární extruze pomocí Aspose.3D pro Javu. Uvidíte, proč je počet řezů důležitý, jak nastavit poloměr zaoblení a jak exportovat výsledek jako OBJ soubor, který lze použít v jakémkoli 3‑D pipeline.

## Rychlé odpovědi
- **Co řídí „řezy“?** Počet mezilehlých průřezů používaných k aproximaci povrchu extruze.  
- **Která metoda nastavuje počet řezů?** `LinearExtrusion.setSlices(int)`  
- **Mohu změnit poloměr zaoblení profilu?** Ano, pomocí `RectangleShape.setRoundingRadius(double)`  
- **Jaký formát souboru se v tomto příkladu používá?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **Potřebuji licenci pro spuštění kódu?** Bezplatná zkušební verze stačí pro hodnocení; pro produkci je vyžadována komerční licence.

`LinearExtrusion.setSlices(int)` určuje, kolik mezilehlých řezů extruze vygeneruje.  
`RectangleShape.setRoundingRadius(double)` definuje poloměr rohu obdélníkového profilu.

## Jak vytvořit 3D extruzi v Javě s řezy?

Nahrajte svůj 2‑D profil, zvolte počet řezů, nastavte poloměr zaoblení a zavolejte `save` – celý pracovní postup se vejde do několika řádků. Aspose.3D pro Javu automaticky zpracuje tvorbu geometrie, interpolaci řezů a export do OBJ, takže se můžete soustředit na vizuální kvalitu místo nízkoúrovňových výpočtů mesh.

## Co je lineární extruze s řezy?

Lineární extruze s řezy převádí plochý 2‑D tvar na 3‑D těleso tím, že jej provleče podél přímky a generuje nastavitelný počet mezilehlých průřezů. Počet řezů přímo ovlivňuje, jak hladce jsou vykresleny zakřivené hrany, například zaoblené rohy.

## Proč použít Aspose.3D pro Javu k vytvoření 3D extruze?

Aspose.3D poskytuje **plnou programovou kontrolu** nad každým parametrem extruze, podporuje **více než 50 vstupních a výstupních formátů** (včetně OBJ, FBX, STL a GLTF) a dokáže zpracovat **modely o stovkách stránek** bez načítání celého souboru do paměti. Běží na jakékoli platformě s podporou Javy, nevyžaduje nativní DLL a zaručuje deterministické výsledky na Windows, Linuxu i macOS.

## Požadavky

1. **Java Development Kit** – Nainstalovaný JDK 8 nebo vyšší.  
2. **Aspose.3D pro Javu** – Stáhněte knihovnu z oficiálního webu [zde](https://releases.aspose.com/3d/java/).  
3. IDE nebo textový editor dle vašeho výběru.

## Importovat balíčky

Přidejte do svého projektu jmenný prostor Aspose.3D, abyste měli přístup ke třídám 3‑D modelování.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Průvodce krok za krokem

### Krok 1: Nastavit scénu a definovat profil

`RectangleShape` je třída, která definuje 2‑D profil obdélníku.  
Nejprve vytvoříme `RectangleShape` a přiřadíme mu **poloměr zaoblení**, aby byly rohy hladké.  
`Scene` je kořenový kontejner pro všechny uzly a geometrii.  
Poté inicializujeme novou `Scene`, která bude obsahovat veškerou geometrii.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Krok 2: Vytvořit podřízené uzly pro každou extruzi

`Node` představuje prvek ve scénovém grafu, který může obsahovat geometrii a transformace.  
Každý kus geometrie žije pod `Node`. Zde vytvoříme dva sourozenecké uzly – jeden pro extruzi s nízkým počtem řezů a druhý pro extruzi s vysokým počtem řezů – a posuneme levý uzel mírně do strany, aby byly výsledky snadno porovnatelné.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Krok 3: Provedení lineární extruze a nastavení řezů

`LinearExtrusion` je třída, která vytváří těleso provlečením profilu lineárně.  
`LinearExtrusion` je třída Aspose.3D, která generuje těleso extruzí 2‑D profilu podél přímky. Pomocí **anonymní vnitřní třídy** zavoláme `setSlices`, abychom řídili hladkost. Levý uzel dostane pouze 2 řezy (hrubé), zatímco pravý uzel dostane 10 řezů (hladké).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Krok 4: Exportovat OBJ – uložit scénu

Na závěr zapíšeme scénu do souboru Wavefront OBJ, formátu široce podporovaného 3‑D editory a herními enginy. Tím demonstrujeme schopnost **exportu OBJ v Javě** v Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Časté problémy a řešení

| Problém | Proč se to stane | Řešení |
|---------|------------------|--------|
| **Extruze vypadá plochá** | Počet řezů nastaven na 1 nebo 0 | Zajistěte, že `setSlices` je zavoláno s hodnotou ≥ 2. |
| **Zaoblené rohy vypadají zubatě** | Poloměr zaoblení je příliš malý vzhledem k počtu řezů | Zvyšte buď poloměr, nebo počet řezů pro hladší křivky. |
| **Soubor nebyl při ukládání nalezen** | `MyDir` ukazuje na neexistující složku | Vytvořte složku předem nebo použijte absolutní cestu. |

## Často kladené otázky

**Q: Jak si mohu stáhnout Aspose.3D pro Javu?**  
A: Knihovnu můžete stáhnout [zde](https://releases.aspose.com/3d/java/).

**Q: Kde najdu dokumentaci k Aspose.3D?**  
A: Dokumentaci najdete [zde](https://reference.aspose.com/3d/java/).

**Q: Je k dispozici bezplatná zkušební verze?**  
A: Ano, můžete vyzkoušet bezplatnou verzi [zde](https://releases.aspose.com/).

**Q: Jak mohu získat podporu pro Aspose.3D?**  
A: Navštivte fórum podpory [zde](https://forum.aspose.com/c/3d/18).

**Q: Mohu zakoupit dočasnou licenci?**  
A: Ano, dočasnou licenci lze získat [zde](https://purchase.aspose.com/temporary-license/).

**Poslední aktualizace:** 2026-05-24  
**Testováno s:** Aspose.3D pro Javu 24.11 (nejnovější v době psaní)  
**Autor:** Aspose

## Související tutoriály

- [Vytvořit 3D extruzi v Javě s Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Jak nastavit směr v lineární extruzi s Aspose.3D pro Javu](/3d/java/linear-extrusion/setting-direction/)
- [Vytvořit 3D scénu s twistem v lineární extruzi – Aspose.3D pro Javu](/3d/java/linear-extrusion/applying-twist/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}