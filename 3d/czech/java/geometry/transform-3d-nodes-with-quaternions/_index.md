---
date: 2025-12-15
description: Naučte se, jak převést model do formátu FBX a uložit scénu jako FBX pomocí
  Aspose.3D pro Javu. Tento krok‑za‑krokem průvodce ukazuje kvaternionové transformace
  3D uzlů.
linktitle: Convert Model to FBX with Quaternions in Java using Aspose.3D
second_title: Aspose.3D Java API
title: Převést model na FBX s kvaterniony v Javě pomocí Aspose.3D
url: /cs/java/geometry/transform-3d-nodes-with-quaternions/
weight: 20
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Převod modelu do FBX s kvaterniony v Javě pomocí Aspose.3D

## Úvod

Pokud potřebujete **převést model do FBX** a zároveň aplikovat plynulé otáčení, jste na správném místě. V tomto tutoriálu projdeme kompletním příkladem v Javě, který používá Aspose.3D k vytvoření krychle, jejímu otáčení pomocí kvaternionů a nakonec **uložení scény jako FBX**. Na konci budete mít znovupoužitelný vzor pro jakýkoli 3‑D objekt, který chcete exportovat do formátu FBX.

## Rychlé odpovědi
- **Jaká knihovna zajišťuje export FBX?** Aspose.3D for Java  
- **Jaký typ transformace se používá?** Rotace založená na kvaternionu pro plynulou interpolaci  
- **Potřebuji licenci pro produkci?** Ano, je vyžadována komerční licence (k dispozici bezplatná zkušební verze)  
- **Mohu exportovat i jiné formáty?** Ano, Aspose.3D podporuje OBJ, STL, GLTF a další  
- **Je kód multiplatformní?** Rozhodně – Java běží na Windows, Linuxu i macOS  

## Předpoklady

Než se ponoříme do tutoriálu, ujistěte se, že máte následující předpoklady:

- Základní znalost programování v Javě.  
- Aspose.3D pro Javu nainstalováno. Můžete si jej stáhnout [zde](https://releases.aspose.com/3d/java/).  
- Adresář dokumentů nastavený pro ukládání vašich 3D scén.

## Import balíčků

V této sekci naimportujeme potřebné balíčky pro zahájení 3D transformací pomocí Aspose.3D.

```java
import com.aspose.threed.*;
```

## Krok 1: Inicializace objektu Scene

Nejprve vytvořte objekt scény, který bude sloužit jako kontejner pro vaše 3D prvky.

```java
Scene scene = new Scene();
```

## Krok 2: Inicializace objektu třídy Node

Nyní vytvořte objekt třídy node, v tomto případě představující krychli.

```java
Node cubeNode = new Node("cube");
```

## Krok 3: Vytvoření Mesh pomocí Polygon Builder

Využijte společnou třídu k vytvoření mesh pomocí metody polygon builder.

```java
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Krok 4: Nastavení geometrie Mesh

Přiřaďte vytvořený mesh k uzlu krychle.

```java
cubeNode.setEntity(mesh);
```

## Krok 5: Nastavení rotace pomocí kvaternionu

Aplikujte rotaci na uzel krychle pomocí kvaternionů. Kvaterniony zabraňují gimbal locku a poskytují plynulé, kontinuální otáčení.

```java
cubeNode.getTransform().setRotation(Quaternion.fromRotation(new Vector3(0, 1, 0), new Vector3(0.3, 0.5, 0.1)));
```

## Krok 6: Nastavení translace

Určete translaci pro uzel krychle, aby se objevil na požadované pozici ve scéně.

```java
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## Krok 7: Přidání krychle do scény

Začleňte uzel krychle do hierarchie scény.

```java
scene.getRootNode().getChildNodes().add(cubeNode);
```

## Krok 8: Uložení 3D scény – Převod modelu do FBX

Nyní skutečně **převádíme model do FBX** uložením scény ve formátu FBX. Toto také demonstruje workflow „uložit scénu jako FBX“.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

## Proč používat kvaterniony pro export FBX?

Kvaterniony vám poskytují:

- **Plynulou interpolaci** mezi orientacemi, nezbytnou pro animace.  
- **Žádný gimbal lock**, který může při použití Eulerových úhlů poškozovat rotace.  
- **Kompaktní reprezentaci**, šetří paměť ve velkých scénách.

Tyto výhody činí kvaternion‑řízené transformace preferovanou volbou, když chcete **převést model do FBX** pro herní enginy nebo vizualizační pipeline.

## Časté problémy a řešení

| Problém | Příčina | Řešení |
|-------|-------|-----|
| Soubor FBX se zobrazuje se špatnou orientací | Rotace aplikována kolem špatné osy | Ověřte vektory osy předané do `Quaternion.fromRotation` |
| Soubor nebyl uložen | Neplatná cesta k adresáři | Ujistěte se, že `MyDir` ukazuje na existující zapisovatelný adresář |
| Výjimka licence | Chybějící nebo vypršená licence | Použijte dočasnou licenci z portálu Aspose (viz FAQ) |

## Často kladené otázky

### Q1: Mohu používat Aspose.3D pro Javu zdarma?

A1: Aspose.3D pro Javu nabízí bezplatnou zkušební verzi. Najdete ji [zde](https://releases.aspose.com/).

### Q2: Kde najdu dokumentaci pro Aspose.3D pro Javu?

A2: Dokumentace je k dispozici [zde](https://reference.aspose.com/3d/java/).

### Q3: Jak získám podporu pro Aspose.3D pro Javu?

A3: Navštivte [forum Aspose.3D](https://forum.aspose.com/c/3d/18) pro podporu.

### Q4: Jsou k dispozici dočasné licence?

A4: Ano, dočasnou licenci můžete získat [zde](https://purchase.aspose.com/temporary-license/).

### Q5: Kde mohu zakoupit Aspose.3D pro Javu?

A5: Můžete si jej koupit [zde](https://purchase.aspose.com/buy).

### Q6: Mohu exportovat do jiných formátů kromě FBX?

A6: Ano, Aspose.3D podporuje OBJ, STL, GLTF a další. Stačí změnit výčtový typ `FileFormat` v volání `save`.

### Q7: Je možné animovat krychli před exportem?

A7: Rozhodně. Můžete vytvořit objekt `Animation`, přidat klíčové snímky do transformace uzlu a poté exportovat animovanou scénu do FBX.

## Závěr

Gratulujeme! Naučili jste se, jak **převést model do FBX** aplikací rotací pomocí kvaternionů a následně **uložit scénu jako FBX** pomocí Aspose.3D pro Javu. Klidně experimentujte s různými mesh, osami rotace a formáty exportu, aby vyhovovaly potřebám vašeho projektu.

---

**Poslední aktualizace:** 2025-12-15  
**Testováno s:** Aspose.3D 24.11 for Java  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}