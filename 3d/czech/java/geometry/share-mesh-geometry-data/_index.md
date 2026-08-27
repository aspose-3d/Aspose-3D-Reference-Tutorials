---
date: 2026-05-19
description: Zjistěte, jak převést mesh na FBX při nastavení material color a sdílení
  mesh geometry data v Java 3D pomocí Aspose.3D.
keywords:
- convert mesh to fbx
- how to export fbx
- how to set material
- export mesh to fbx
- aspose 3d tutorial
linktitle: Převést Mesh na FBX a nastavit Material Color v Java 3D
schemas:
- author: Aspose
  dateModified: '2026-05-19'
  description: Learn how to convert mesh to FBX while setting material color and sharing
    mesh geometry data in Java 3D using Aspose.3D.
  headline: Convert Mesh to FBX and Set Material Color in Java 3D
  type: TechArticle
- questions:
  - answer: Yes, the shared mesh can be animated via skeletal rigs or morph targets
      while each node retains its own material.
    question: Can I reuse the same mesh for animated characters?
  - answer: Absolutely, Aspose.3D writes full UV data, so textures map correctly in
      downstream tools.
    question: Does the FBX export preserve UV coordinates?
  - answer: The library can stream meshes exceeding 2 GB without loading the entire
      file into memory, making it suitable for large scenes.
    question: What is the maximum file size Aspose.3D can handle?
  - answer: Pass a different `FileFormat` enum value, such as `FileFormat.FBX201400ASCII`,
      to `scene.save`.
    question: How do I change the FBX version?
  - answer: Yes, you can create a new `Scene`, add the desired nodes, and then save
      that scene to FBX.
    question: Is it possible to export only a subset of nodes?
  type: FAQPage
second_title: Aspose.3D Java API
title: Převést Mesh na FBX a nastavit Material Color v Java 3D
url: /cs/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Převod sítě na FBX a nastavení barvy materiálu v Java 3D

## Úvod

Pokud vytváříte 3D aplikaci založenou na Javě, často budete potřebovat znovu použít stejnou geometrii napříč více objekty a přitom každé instanci dát jedinečný vzhled. V tomto tutoriálu se naučíte **jak převést mesh na FBX**, sdílet podkladovou geometrii sítě mezi několika uzly a **nastavit odlišnou barvu materiálu pro každý uzel**. Na konci budete mít připravenou scénu FBX, kterou můžete vložit do libovolného enginu nebo prohlížeče.

## Rychlé odpovědi
- **Jaký je hlavní cíl?** Převést mesh na FBX, sdílet geometrii sítě a nastavit odlišnou barvu materiálu pro každý uzel.  
- **Která knihovna je vyžadována?** Aspose.3D pro Java.  
- **Jak exportovat výsledek?** Uložit scénu jako soubor FBX pomocí `FileFormat.FBX7400ASCII`.  
- **Potřebuji licenci?** Pro produkční použití je vyžadována dočasná nebo plná licence.  
- **Jaká verze Javy funguje?** Jakékoli prostředí Java 8+.

## Co je **convert mesh to FBX**?

Převod mesh na FBX znamená vzít objekt sítě, který existuje v paměti, a zapsat jej do formátu souboru FBX, de‑facto standardu podporovaného programy Maya, Blender, Unity a mnoha dalšími 3D nástroji. Aspose.3D provádí těžkou práci, takže stačí zavolat `scene.save(...)` s odpovídajícím `FileFormat`.

## Proč sdílet data geometrie sítě?

Sdílení geometrie snižuje spotřebu paměti a urychluje vykreslování, protože podkladové vertex buffery jsou uloženy jen jednou. Tato technika je ideální pro scény s mnoha duplicitními objekty — například lesy, davy nebo modulární architekturu — kde se každá instance liší jen transformací nebo materiálem.

## Požadavky

Před tím, než se ponoříte do tutoriálu, ujistěte se, že máte následující:

- **Java Development Environment** — libovolné IDE nebo nastavení příkazové řádky s Java 8 nebo novější.  
- **Aspose.3D Library** — stáhněte nejnovější JAR z oficiálního webu: [here](https://releases.aspose.com/3d/java/).

## Import balíčků

Namespace `com.aspose.threed` obsahuje všechny třídy, které budete potřebovat k tvorbě scén, sítí a materiálů. Naimportujte tyto balíčky na začátku svého Java souboru, aby kompilátor mohl rozpoznat typy.

```java
import com.aspose.threed.*;
```

## Krok 1: Inicializace objektu scény (initialize scene java)

Třída `Scene` je vrcholovým kontejnerem Aspose.3D, který představuje celý 3D svět. Inicializací `Scene` získáte čisté plátno, na které můžete přidávat sítě, světla a kamery.

```java
// Initialize scene object
Scene scene = new Scene();
```

## Krok 2: Definice vektorů barev

`Vector3` představuje tříkomponentový vektor (X, Y, Z) používaný pro pozice, směry nebo barvy.  
Vytvořte pole objektů `Vector3`, které budou obsahovat hodnoty RGB. Každý vektor bude později přiřazen samostatnému uzlu, čímž každé instanci zajistíte vlastní odstín materiálu.

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## Krok 3: Vytvoření 3D sítě v Javě pomocí Polygon Builder (create 3d mesh java)

Třída `PolygonBuilder` vám umožňuje konstruovat síť definováním vrcholů a ploch ručně. Tato síť bude znovu použita napříč všemi uzly, což demonstruje, jak v praxi funguje sdílení geometrie.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Jak nastavit barvu materiálu pro každý uzel?

`LambertMaterial` je jednoduchý typ materiálu, který definuje difúzní barvu pro síť.  
Procházejte vektory barev, vytvořte pro každý záznam uzel krychle, přiřaďte mu čerstvý `LambertMaterial` s aktuální barvou a umístěte uzel pomocí transformační matice. Tento postup zajišťuje, že každý uzel zobrazí unikátní barvu, přičemž stále odkazuje na stejnou podkladovou síť.

```java
int idx = 0;
for(Vector3 color : colors) {
    // Initialize cube node object
    Node cube = new Node("cube");
    cube.setEntity(mesh);
    LambertMaterial mat = new LambertMaterial();
    // Set color
    mat.setDiffuseColor(color);
    // Set material
    cube.setMaterial(mat);
    // Set translation
    cube.getTransform().setTranslation(new Vector3(idx++ * 20, 0, 0));
    // Add cube node
    scene.getRootNode().addChildNode(cube);
}
```

## Krok 5: Uložení 3D scény (save scene fbx, convert mesh to fbx)

Zadejte adresář a název souboru pro uložení 3D scény v podporovaném formátu, v tomto případě FBX7400ASCII. Tento krok také demonstruje **convert mesh to FBX** tím, že uloží scénu se sdílenou geometrií na disk.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Časté problémy a tipy

- **Problémy s cestou** — Ujistěte se, že cesta k adresáři končí oddělovačem souboru (`/` nebo `\\`) před připojením názvu souboru.  
- **Inicializace licence** — Pokud zapomenete nastavit licenci Aspose.3D před voláním `scene.save`, knihovna bude pracovat v režimu zkušební verze a může vložit vodoznak.  
- **Přepis materiálů** — Opakované používání stejné instance `LambertMaterial` pro více uzlů způsobí, že všechny uzly sdílejí stejnou barvu. Vždy vytvořte nový materiál v každé iteraci, jak je ukázáno výše.  
- **Velké sítě** — Pro sítě s miliony vrcholů zvažte použití `MeshBuilder` s indexovanými polygonami, aby velikost souboru FBX zůstala zvládnutelná.

## Další často kladené otázky

**Q1: Mohu použít Aspose.3D s jinými Java frameworky?**  
A1: Ano, Aspose.3D je navrženo tak, aby hladce spolupracovalo s různými Java frameworky.

**Q2: Existují různé licenční možnosti pro Aspose.3D?**  
A2: Ano, možnosti licencování můžete prozkoumat [zde](https://purchase.aspose.com/buy).

**Q3: Jak získat podporu pro Aspose.3D?**  
A3: Navštivte fórum Aspose.3D [zde](https://forum.aspose.com/c/3d/18) pro podporu a diskuze.

**Q4: Je k dispozici bezplatná zkušební verze?**  
A4: Ano, bezplatnou zkušební verzi získáte [zde](https://releases.aspose.com/).

**Q5: Jak získat dočasnou licenci pro Aspose.3D?**  
A5: Dočasnou licenci můžete získat [zde](https://purchase.aspose.com/temporary-license/).

## Často kladené otázky

**Q: Mohu znovu použít stejnou síť pro animované postavy?**  
A: Ano, sdílená síť může být animována pomocí skeletálních rigů nebo morph targetů, přičemž každý uzel si zachová svůj vlastní materiál.

**Q: Zachovává export FBX UV souřadnice?**  
A: Rozhodně, Aspose.3D zapisuje kompletní UV data, takže textury se správně mapují v následných nástrojích.

**Q: Jaká je maximální velikost souboru, kterou Aspose.3D zvládne?**  
A: Knihovna dokáže streamovat sítě přesahující 2 GB, aniž by načítala celý soubor do paměti, což ji činí vhodnou pro velké scény.

**Q: Jak změnit verzi FBX?**  
A: Předávejte jinou hodnotu enumu `FileFormat`, například `FileFormat.FBX201400ASCII`, metodě `scene.save`.

**Q: Je možné exportovat jen podmnožinu uzlů?**  
A: Ano, můžete vytvořit novou `Scene`, přidat požadované uzly a poté tuto scénu uložit do FBX.

## Závěr

Gratulujeme! Úspěšně jste **převáděli mesh na FBX**, sdíleli data geometrie sítě mezi více uzly a nastavili individuální barvy materiálů pomocí Aspose.3D pro Java. Tento postup vám poskytuje lehkou, znovupoužitelnou architekturu sítě, kterou lze exportovat do libovolného pipeline kompatibilního s FBX.

---

**Poslední aktualizace:** 2026-05-19  
**Testováno s:** Aspose.3D 24.11 for Java  
**Autor:** Aspose  

{{< blocks/products/products-backtop-button >}}

## Související tutoriály

- [Jak rozdělit síť podle materiálu v Javě pomocí Aspose.3D](/3d/java/3d-mesh-data/split-meshes-by-material/)
- [Vložit texturu FBX v Javě — Použít materiály na 3D objekty s Aspose.3D](/3d/java/geometry/apply-materials-to-3d-objects/)
- [Jak exportovat scénu do FBX a získat informace o 3D scéně v Javě](/3d/java/3d-scenes-and-models/get-scene-information/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}