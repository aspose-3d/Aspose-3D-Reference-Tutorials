---
date: 2026-06-29
description: Naučte se, jak použít licenci Aspose 3D k vytvoření 3D scény se zkrouceným
  offsetem lineární extruze v Javě a exportovat ji jako soubor Wavefront OBJ.
keywords:
- aspose 3d license
- wavefront obj export
- linear extrusion twist
- java 3d modeling
linktitle: Použití zkroucení offsetu při lineární extruzi s Aspose.3D pro Javu
schemas:
- author: Aspose
  dateModified: '2026-06-29'
  description: Learn how to use an Aspose 3D license to create a 3D scene with twist
    offset linear extrusion in Java and export it as a Wavefront OBJ file.
  headline: Using Aspose 3D License for Twist Offset Extrusion in Java
  type: TechArticle
- description: Learn how to use an Aspose 3D license to create a 3D scene with twist
    offset linear extrusion in Java and export it as a Wavefront OBJ file.
  name: Using Aspose 3D License for Twist Offset Extrusion in Java
  steps:
  - name: Set Up the Environment
    text: Begin by setting up your Java development environment and ensuring that
      Aspose.3D for Java is correctly installed. This step is essential for any **java
      3d modeling** work.
  - name: Initialize the Base Profile
    text: '`RectangleShape` is a class representing a rectangular 2‑D shape used as
      an extrusion profile. Create a base profile for extrusion, in this case, a `RectangleShape`
      with a rounding radius of 0.3. The profile defines the cross‑section that will
      be swept along the extrusion path.'
  - name: Create a 3D Scene
    text: '`Scene` is the container that holds all nodes, lights, and cameras for
      your model. Building the scene first gives you a place to attach the extruded
      geometry.'
  - name: Create Nodes
    text: Generate nodes within the scene to represent different entities. Here we
      create two sibling nodes—one for a plain extrusion and another that uses a twist
      offset.
  - name: Perform Linear Extrusion with Twist and Twist Offset
    text: Apply linear extrusion on both nodes. The left node demonstrates a basic
      twist, while the right node adds a twist offset to illustrate the extra control
      you get with this feature. `setSlices(int)` sets the number of slices (segments)
      used to approximate the twist, controlling mesh resolution. > **Pr
  - name: Save the 3D Scene (Export 3d scene)
    text: '`save(String, FileFormat)` writes the scene to a file in the specified
      format. Finally, export the assembled scene to an OBJ file so you can view it
      in any standard 3D viewer or import it into other pipelines. CODE_BLOCK_PLACEHOLDER_6_END
      When the code runs successfully, you’ll find `TwistOffsetInLi'
  type: HowTo
- questions:
  - answer: Yes, Aspose.3D for Java can be used in both commercial and non‑commercial
      projects. Check the [licensing options](https://purchase.aspose.com/buy) for
      more details.
    question: Can I use Aspose.3D for Java in non‑commercial projects?
  - answer: Visit the [Aspose.3D for Java forum](https://forum.aspose.com/c/3d/18)
      to get assistance and connect with the community.
    question: Where can I find support for Aspose.3D for Java?
  - answer: Yes, you can explore a free trial version from the [releases page](https://releases.aspose.com/).
    question: Is there a free trial available for Aspose.3D for Java?
  - answer: Get a temporary license for your project by visiting [this link](https://purchase.aspose.com/temporary-license/).
    question: How do I obtain a temporary license for Aspose.3D for Java?
  - answer: Yes, refer to the [documentation](https://reference.aspose.com/3d/java/)
      for more examples and in‑depth tutorials.
    question: Are there additional examples and tutorials available?
  type: FAQPage
second_title: Aspose.3D Java API
title: Použití licence Aspose 3D pro zkroucení offsetu při lineární extruzi v Javě
url: /cs/java/linear-extrusion/using-twist-offset/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Použití licence Aspose 3D pro Twist Offset Extrusion v Javě

## Úvod

Vytvoření 3D scény v Javě je mnohem výkonnější, když zkombinujete **Aspose 3D license** s funkcemi lineárního extruze s rotací a offsetem rotace. Tento tutoriál vás provede každým krokem potřebným k **create 3D scene**, aplikaci twist offsetu a nakonec **export 3D scene** jako soubor Wavefront OBJ. S licencovanou verzí odemknete generování sítě v plném rozlišení, neomezenou velikost souboru a výkon úrovně komerčního nasazení.

## Rychlé odpovědi
- **Co dělá Twist Offset?** Posouvá počáteční bod rotace, což vám umožňuje offsetovat rotaci podél cesty extruze.  
- **Která třída provádí lineární extruzi?** `LinearExtrusion` – můžete na ní nastavit twist, slices a twist offset.  
- **Mohu výsledek exportovat?** Ano, zavolejte `scene.save(..., FileFormat.WAVEFRONTOBJ)`, abyste exportovali 3D scénu.  
- **Potřebuji pro vývoj licenci Aspose 3D?** Dočasná licence funguje pro testování; plná **Aspose 3D license** je vyžadována pro produkci a odstranění evaluačních vodoznaků.  
- **Jaká verze Javy je podporována?** Jakékoli prostředí Java 8+ funguje s nejnovější knihovnou Aspose.3D.

## Co je „create 3d scene“ v Aspose.3D?

`Scene` je nejvyšší objekt Aspose.3D představující kompletní 3D prostředí. Vytvoření 3D scény v Aspose.3D znamená vytvořit objekt `Scene`, přidat podřízené uzly, které obsahují geometrii, světla nebo kamery, a poté uložit hierarchii do souborového formátu, jako je OBJ. `Scene` slouží jako kořenový kontejner pro veškerý 3D obsah ve vaší Java aplikaci.

## Proč použít lineární extruzi s rotací a offsetem rotace?

`LinearExtrusion` je třída Aspose.3D pro tažení 2‑D profilu podél přímé linie za účelem vytvoření 3‑D geometrie. Použití s rotací přidává rotační komponentu a offset rotace vám umožňuje posunout, kde tato rotace začíná, což vám dává přesnou kontrolu nad spirálovými tvary, jako jsou šroubovité sloupy, dekorativní rukojeti nebo mechanické pružiny. Tato dodatečná kontrola je zvláště cenná v **java 3d modeling** pro mechanické součásti a umělecké návrhy.

## Předpoklady

- **Java Environment:** Ujistěte se, že máte na svém systému nastavené vývojové prostředí Java.  
- **Aspose.3D for Java:** Stáhněte a nainstalujte knihovnu Aspose.3D z [download link](https://releases.aspose.com/3d/java/).  
- **Documentation:** Seznamte se s [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/).  

## Importovat balíčky

Ve vašem Java projektu importujte potřebné balíčky, abyste mohli začít používat Aspose.3D pro Java. Ujistěte se, že zahrnujete požadované knihovny pro bezproblémovou integraci.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Jak vytvořit 3d scene – Průvodce krok za krokem

Pro vytvoření 3D scény s twist offset lineární extruzí v Javě nejprve nastavíte vývojové prostředí, poté definujete obdélníkový profil, vytvoříte objekt `Scene`, přidáte dva podřízené uzly, použijete `LinearExtrusion` s a bez offsetu a nakonec scénu uložíte jako soubor Wavefront OBJ. Postupujte podle níže uvedených sekcí s konkrétními úryvky kódu.

### Krok 1: Nastavení prostředí
Nejprve nastavte své vývojové prostředí Java a ujistěte se, že je Aspose.3D pro Java správně nainstalováno. Tento krok je nezbytný pro jakoukoli práci na **java 3d modeling**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
// Initialize the base profile to be extruded
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### Krok 2: Inicializace základního profilu
`RectangleShape` je třída představující obdélníkový 2‑D tvar použitého jako profil extruze. Vytvořte základní profil pro extruzi, v tomto případě `RectangleShape` s poloměrem zaoblení 0.3. Profil definuje průřez, který bude tažen podél cesty extruze.

```java
// Create a scene
Scene scene = new Scene();
```

### Krok 3: Vytvoření 3D scény
`Scene` je kontejner, který drží všechny uzly, světla a kamery vašeho modelu. Vytvoření scény jako první vám poskytne místo, kam můžete připojit extrudovanou geometrii.

```java
// Create left node
Node left = scene.getRootNode().createChildNode();
// Create right node
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Krok 4: Vytvoření uzlů
Vygenerujte uzly v rámci scény, které představují různé entity. Zde vytvoříme dva sourozenecké uzly — jeden pro jednoduchou extruzi a druhý, který používá offset rotace.

```java
// Perform linear extrusion on left node using twist and slices property
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// Perform linear extrusion on right node using twist, twist offset, and slices property
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

### Krok 5: Provedení lineární extruze s rotací a offsetem rotace
Aplikujte lineární extruzi na oba uzly. Levý uzel ukazuje základní rotaci, zatímco pravý uzel přidává offset rotace, aby ilustroval dodatečnou kontrolu, kterou tato funkce poskytuje. `setSlices(int)` nastavuje počet řezů (segmentů) použité k aproximaci rotace, čímž řídí rozlišení sítě.

```java
// Save 3D scene
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

> **Tip:** Upravit `setSlices()`, aby se zvýšilo rozlišení sítě, když potřebujete hladší zakřivení.

### Krok 6: Uložení 3D scény (Export 3d scene)
`save(String, FileFormat)` zapisuje scénu do souboru ve specifikovaném formátu. Nakonec exportujte sestavenou scénu do OBJ souboru, abyste ji mohli zobrazit v libovolném standardním 3D prohlížeči nebo importovat do dalších pipeline.

CODE_BLOCK_PLACEHOLDER_6_END

Po úspěšném spuštění kódu najdete soubor `TwistOffsetInLinearExtrusion.obj` ve zvoleném adresáři, připravený k otevření v nástrojích jako Blender, MeshLab nebo jakémkoli CAD softwaru.

## Běžné problémy a řešení
| Problém | Proč se to děje | Řešení |
|-------|----------------|-----|
| **Scéna se uloží jako prázdný soubor** | Cesta `MyDir` je nesprávná nebo chybí oprávnění k zápisu. | Ověřte, že adresář existuje a je zapisovatelný, nebo použijte absolutní cestu. |
| **Rotace vypadá plochá** | `setSlices()` je nastaveno příliš nízko, což vede k hrubé síti. | Zvyšte počet řezů (např. 200) pro hladší rotace. |
| **Offset rotace nemá žádný efekt** | Vektor offsetu je kolineární s směrem extruze. | Použijte nenulovou složku X nebo Y, aby se posun offsetu projevil. |

## Často kladené otázky

**Q: Mohu použít Aspose.3D pro Java v nekomerčních projektech?**  
A: Ano, Aspose.3D pro Java může být používán jak v komerčních, tak v nekomerčních projektech. Podívejte se na [licensing options](https://purchase.aspose.com/buy) pro více detailů.

**Q: Kde mohu najít podporu pro Aspose.3D pro Java?**  
A: Navštivte [Aspose.3D for Java forum](https://forum.aspose.com/c/3d/18) a získejte pomoc a spojte se s komunitou.

**Q: Je k dispozici bezplatná zkušební verze Aspose.3D pro Java?**  
A: Ano, můžete vyzkoušet bezplatnou verzi z [releases page](https://releases.aspose.com/).

**Q: Jak získat dočasnou licenci pro Aspose.3D pro Java?**  
A: Získejte dočasnou licenci pro svůj projekt na [this link](https://purchase.aspose.com/temporary-license/).

**Q: Existují další příklady a tutoriály?**  
A: Ano, podívejte se do [documentation](https://reference.aspose.com/3d/java/) pro více příkladů a podrobných tutoriálů.

---

**Last Updated:** 2026-06-29  
**Tested With:** Aspose.3D for Java 24.11 (latest)  
**Author:** Aspose

{{< blocks/products/products-backtop-button >}}

## Související tutoriály

- [Vytvořit 3D Extruzi v Javě s Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Vytvořit 3D scénu s rotací v lineární extruzi – Aspose.3D pro Java](/3d/java/linear-extrusion/applying-twist/)
- [Jak nastavit směr v lineární extruzi s Aspose.3D pro Java](/3d/java/linear-extrusion/setting-direction/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}