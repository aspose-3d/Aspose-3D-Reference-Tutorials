---
date: 2025-12-12
description: Naučte se nastavit barvu materiálu při sdílení dat o geometrii sítě a
  ukládání scény jako FBX v Java 3D pomocí Aspose.3D.
linktitle: Set Material Color and Share Mesh Geometry Data in Java 3D with Aspose.3D
second_title: Aspose.3D Java API
title: Nastavte barvu materiálu a sdílejte data geometrie sítě v Java 3D s Aspose.3D
url: /cs/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Nastavení barvy materiálu a sdílení geometrických dat mesh v Java 3D s Aspose.3D

## Úvod

Vydejte se na cestu do světa Java 3D s Aspose.3D, která otevírá možnosti pro tvorbu úchvatných vizualizací a pohlcujících zážitků. V tomto tutoriálu vás provedeme **tím, jak sdílet data geometrie mesh** v Java 3D pomocí Aspose.3D, a ukážeme vám přesně **jak nastavit barvu materiálu** pro každou instanci mesh. Postupujte pečlivě krok za krokem a na konci budete bez problémů vyměňovat data mesh mezi více uzly, řídit barvy a exportovat do FBX.

## Rychlé odpovědi
- **Jaký je hlavní cíl?** Nastavit barvu materiálu pro každý uzel a sdílet data geometrie mesh.  
- **Která knihovna je vyžadována?** Aspose.3D pro Java.  
- **Jak výsledek exportovat?** Uložit scénu jako soubor FBX (FBX7400ASCII).  
- **Potřebuji licenci?** Pro produkční použití je vyžadována dočasná nebo plná licence.  
- **Jaká verze Javy funguje?** Jakékoli prostředí Java 8+.

## Předpoklady

Než se pustíme do tutoriálu, ujistěte se, že máte připavené následující předpoklady:

- Vývojové prostředí Javy: Zajistěte, aby bylo na vašem systému nastavené vývojové prostředí Javy.  
- Knihovna Aspose.3D: Stáhněte a nainstalujte knihovnu Aspose.3D. Knihovnu najdete [zde](https://releases.aspose.com/3d/java/).

## Import balíčků

Začněte importováním potřebných balíčků do vašeho Java projektu. Tento krok je nezbytný pro přístup k funkcím poskytovaným knihovnou Aspose.3D.

```java
import com.aspose.threed.*;
```

## Krok 1: Inicializace objektu scény (initialize scene java)

Spusťte proces inicializací objektu scény. Ten bude sloužit jako plátno, na kterém se naše 3D kouzlo rozvine.

```java
// Initialize scene object
Scene scene = new Scene();
```

## Krok 2: Definice vektorů barev

V tomto kroku definujeme pole vektorů barev, které budou aplikovány na různé prvky naší 3D scény.

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## Krok 3: Vytvoření 3D mesh v Javě pomocí Polygon Builder (create 3d mesh java)

Využijte třídu Common k vytvoření mesh pomocí metody polygon builder. Tento mesh bude základem pro naše 3D prvky.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Jak nastavit barvu materiálu pro každý uzel?

Iterujte přes vektory barev, vytvořte uzly krychlí a nastavte atributy jako materiál, **nastavení barvy materiálu**, a translaci. Toto je jádro řízení vizuálního vzhledu každé instance mesh.

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

## Krok 5: Uložení 3D scény (save scene fbx, convert mesh to fbx)

Zadejte adresář a název souboru pro uložení 3D scény ve podporovaném formátu, v tomto případě FBX7400ASCII. Tento krok také ukazuje **konverzi mesh do FBX**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Závěr

Gratulujeme! Úspěšně jste **nastavili barvu materiálu**, sdíleli data geometrie mesh mezi více uzly a exportovali výsledek jako soubor FBX pomocí Aspose.3D pro Java. To otevírá nekonečné možnosti pro tvorbu vizuálně úchvatných a interaktivních 3D aplikací.

## Často kladené otázky

### Q1: Mohu používat Aspose.3D s jinými Java frameworky?

A1: Ano, Aspose.3D je navrženo tak, aby bez problémů fungovalo s různými Java frameworky.

### Q2: Existují licenční možnosti pro Aspose.3D?

A2: Ano, licenční možnosti můžete prozkoumat [zde](https://purchase.aspose.com/buy).

### Q3: Jak získám podporu pro Aspose.3D?

A3: Navštivte fórum Aspose.3D [zde](https://forum.aspose.com/c/3d/18) pro podporu a diskuze.

### Q4: Je k dispozici bezplatná zkušební verze?

A4: Ano, bezplatnou zkušební verzi získáte [zde](https://releases.aspose.com/).

### Q5: Jak získat dočasnou licenci pro Aspose.3D?

A5: Dočasnou licenci můžete získat [zde](https://purchase.aspose.com/temporary-license/).

## Další často kladené otázky

**Q: Můžu exportovat scénu do jiných formátů než FBX?**  
A: Ano, Aspose.3D podporuje OBJ, STL, 3MF a další. Stačí změnit výčtový typ `FileFormat` v metodě `save`.

**Q: Co když potřebuji změnit materiál po vytvoření scény?**  
A: Získejte uzel, upravte jeho `LambertMaterial` (např. `setDiffuseColor`) a scénu znovu uložte.

**Q: Dokáže knihovna efektivně pracovat s velkými mesh?**  
A: Aspose.3D používá optimalizované datové struktury; pro extrémně velké mesh však zvažte streamování nebo rozdělení scény.

**Q: Existuje způsob, jak animovat změnu barvy?**  
A: Ano, můžete animovat vlastnosti materiálu pomocí API `AnimationController`.

---

**Poslední aktualizace:** 2025-12-12  
**Testováno s:** Aspose.3D 24.11 pro Java  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}