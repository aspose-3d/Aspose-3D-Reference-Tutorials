---
date: 2026-02-17
description: Naučte se, jak převést síť do formátu FBX při nastavení barvy materiálu
  a sdílení geometrických dat sítě v Java 3D pomocí Aspose.3D.
linktitle: Convert Mesh to FBX and Set Material Color in Java 3D
second_title: Aspose.3D Java API
title: Převést síť na FBX a nastavit barvu materiálu v Java 3D
url: /cs/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Převod sítě na FBX a nastavení barvy materiálu v Java 3D

## Úvod

Pokud vytváříte 3D aplikaci založenou na Javě, často budete potřebovat znovu použít stejnou geometrii u více objektů a přitom každé instanci dát jedinečný vzhled. V tomto tutoriálu se naučíte **jak převést síť na FBX**, sdílet podkladovou geometrii sítě mezi několika uzly a **nastavit odlišnou barvu materiálu pro každý uzel**. Na konci budete mít připravenou scénu FBX připravenou k exportu, kterou můžete vložit do libovolného enginu nebo prohlížeče.

## Rychlé odpovědi
- **Jaký je hlavní cíl?** Převést síť na FBX, sdílet geometrii sítě a nastavit odlišnou barvu materiálu pro každý uzel.  
- **Která knihovna je vyžadována?** Aspose.3D pro Java.  
- **Jak exportuji výsledek?** Uložit scénu jako FBX soubor pomocí `FileFormat.FBX7400ASCII`.  
- **Potřebuji licenci?** Pro produkční použití je vyžadována dočasná nebo plná licence.  
- **Jaká verze Javy funguje?** Jakékoli prostředí Java 8+.

## Co je **convert mesh to FBX**?

`convert mesh to fbx` je proces, při kterém se objekt sítě vytvořený nebo upravený v paměti zapíše do formátu FBX, který je široce podporován 3D nástroji jako Maya, Blender a Unity. Aspose.3D provádí těžkou práci, takže stačí zavolat `scene.save(...)` s odpovídajícím `FileFormat`.

## Proč sdílet data geometrie sítě?

Sdílení geometrie snižuje spotřebu paměti a urychluje renderování, protože podkladové vertexové buffery jsou uloženy jen jednou. Tato technika je ideální pro scény s mnoha duplicitními objekty – například lesy, davy nebo modulární architekturu – kde se každá instance liší jen transformací nebo materiálem.

## Požadavky

Before we dive into the tutorial, make sure you have the following prerequisites in place:

- **Java Development Environment** – jakékoli IDE nebo nastavení příkazové řádky s Java 8 nebo novější.  
- **Aspose.3D Library** – stáhněte nejnovější JAR z oficiálního webu: [here](https://releases.aspose.com/3d/java/).

## Import balíčků

Begin by importing the necessary packages into your Java project. This step is crucial to access the functionalities provided by the Aspose.3D library.

```java
import com.aspose.threed.*;
```

## Krok 1: Inicializace objektu scény (initialize scene java)

Začneme proces inicializací objektu scény. Tento objekt bude sloužit jako plátno, na kterém se naše 3D magie rozvine.

```java
// Initialize scene object
Scene scene = new Scene();
```

## Krok 2: Definice vektorů barev

V tomto kroku definujeme pole vektorů barev, které budou aplikovány na různé prvky naší 3D scény.

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## Krok 3: Vytvoření 3D sítě v Javě pomocí Polygon Builder (create 3d mesh java)

Využijte třídu Common k vytvoření sítě pomocí metody polygon builder. Tato síť bude základem pro naše 3D prvky.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Jak nastavit barvu materiálu pro každý uzel?

Iterujte přes vektory barev, vytvořte kostkové uzly a nastavte atributy jako materiál, **set material color** a translaci. Toto je jádro řízení vizuálního vzhledu každé instance sítě.

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

Zadejte adresář a název souboru pro uložení 3D scény ve podporovaném formátu, v tomto případě FBX7400ASCII. Tento krok také demonstruje **convert mesh to FBX**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Časté úskalí a tipy

- **Problémy s cestou** – Ujistěte se, že cesta k adresáři končí oddělovačem souboru (`/` nebo `\\`) před připojením názvu souboru.  
- **Inicializace licence** – Pokud zapomenete nastavit licenci Aspose.3D před voláním `scene.save`, knihovna bude fungovat v režimu zkušební verze a může vložit vodoznak.  
- **Přepis materiálu** – Opakované používání stejné instance `LambertMaterial` pro více uzlů způsobí, že všechny uzly budou sdílet stejnou barvu. Vždy vytvořte nový materiál pro každou iteraci, jak je ukázáno výše.  
- **Velké sítě** – Pro sítě s miliony vrcholů zvažte použití `MeshBuilder` s indexovanými polygonami, aby velikost souboru FBX zůstala zvládnutelná.

## Často kladené otázky

**Q: Můžu exportovat scénu do jiných formátů než FBX?**  
A: Ano, Aspose.3D podporuje OBJ, STL, 3MF, GLTF a další. Stačí nahradit výčtový typ `FileFormat` v volání `save`.

**Q: Co když potřebuji změnit materiál po vytvoření scény?**  
A: Získejte uzel, upravte jeho `LambertMaterial` (např. `setDiffuseColor`) a scénu znovu uložte.

**Q: Zvládá knihovna velké sítě efektivně?**  
A: Aspose.3D používá optimalizované datové struktury; pro extrémně velké sítě však zvažte streamování nebo rozdělení scény.

**Q: Existuje způsob, jak animovat změnu barvy?**  
A: Ano, můžete animovat vlastnosti materiálu pomocí API `AnimationController`.

## Další často kladené otázky

**Q1: Můžu použít Aspose.3D s jinými Java frameworky?**  
A1: Ano, Aspose.3D je navrženo tak, aby spolupracovalo bez problémů s různými Java frameworky.

**Q2: Existují licenční možnosti pro Aspose.3D?**  
A2: Ano, můžete prozkoumat licenční možnosti [here](https://purchase.aspose.com/buy).

**Q3: Jak mohu získat podporu pro Aspose.3D?**  
A3: Navštivte Aspose.3D [forum](https://forum.aspose.com/c/3d/18) pro podporu a diskuse.

**Q4: Je k dispozici bezplatná zkušební verze?**  
A4: Ano, můžete získat bezplatnou zkušební verzi [here](https://releases.aspose.com/).

**Q5: Jak získám dočasnou licenci pro Aspose.3D?**  
A5: Dočasnou licenci můžete získat [here](https://purchase.aspose.com/temporary-license/).

## Závěr

Gratulujeme! Úspěšně jste **převáděli síť na FBX**, sdíleli data geometrie sítě mezi více uzly a nastavili individuální barvy materiálu pomocí Aspose.3D pro Java. Tento pracovní postup vám poskytuje lehkou, znovu použitelnou architekturu sítě, kterou lze exportovat do libovolného pipeline kompatibilního s FBX.

---

**Last Updated:** 2026-02-17  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}