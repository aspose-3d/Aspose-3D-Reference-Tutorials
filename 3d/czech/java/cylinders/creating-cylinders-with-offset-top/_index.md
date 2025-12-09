---
date: 2025-12-05
description: Naučte se, jak v Aspose.3D pro Javu vytvořit válcové modely s posunutými
  vršky, přidat kroky pro podřízený uzel v Javě a snadno exportovat soubory OBJ 3D
  modelů.
linktitle: How to Create Cylinder with Offset Top in Aspose.3D for Java
second_title: Aspose.3D Java API
title: Jak vytvořit válec s posunutým vrcholem v Aspose.3D pro Javu
url: /cs/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak vytvořit válec s posunutým vrcholem v Aspose.3D pro Java

## Úvod

Pokud hledáte **jak vytvořit válec** s vlastním posunutým vrcholem v 3D scéně založené na Javě, Aspose.3D proces zjednodušuje. V tomto tutoriálu projdeme každý krok – od nastavení scény po export finálního modelu jako OBJ souboru – abyste mohli s jistotou integrovat válce s posunutým vrcholem do svých aplikací.

## Rychlé odpovědi
- **Jaká knihovna se používá?** Aspose.3D pro Java  
- **Mohu posunout vrchol válce?** Ano, pomocí `setOffsetTop`  
- **Jak přidám podřízený uzel v Javě?** Zavolejte `createChildNode` na kořenovém uzlu  
- **Do jakého formátu mohu exportovat?** Wavefront OBJ (`export 3d model obj`)  
- **Potřebuji licenci pro testování?** Dočasná licence je k dispozici pro hodnocení  

## Co je “jak vytvořit válec” s posunutým vrcholem?

Vytvoření válce s posunutým vrcholem znamená, že horní kruhová plocha je posunuta vzhledem k základně, což vám umožní modelovat kuželovité nebo asymetrické tvary bez ruční manipulace s vrcholy. Aspose.3D poskytuje speciální konstruktor a vlastnost `OffsetTop`, která to umožňuje během několika řádků kódu.

## Proč použít Aspose.3D pro Java?

- **High‑level API:** Není nutné spravovat nízkoúrovňová data mesh.  
- **Cross‑platform:** Funguje v jakémkoli prostředí kompatibilním s JVM.  
- **Vestavěné exportéry:** Přímé uložení do OBJ, STL, FBX a dalších.  
- **Rozšiřitelnost:** Snadno přidávejte podřízené uzly, aplikujte transformace a integrujte s dalšími Java knihovnami.

## Předpoklady

Než začneme, ujistěte se, že máte:

- **Java Development Kit (JDK)** – nainstalovanou kompatibilní verzi.  
- **Aspose.3D pro Java knihovnu** – stáhněte nejnovější JAR z oficiálního webu [zde](https://releases.aspose.com/3d/java/).  
- IDE podle vašeho výběru (Eclipse, IntelliJ IDEA, NetBeans atd.).

## Import balíčků

Nejprve importujte třídy, které budeme potřebovat. Umístěte tyto příkazy na začátek vašeho Java souboru:

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Průvodce krok za krokem

### Krok 1: Vytvoření scény

Scéna funguje jako kontejner pro všechny 3D objekty.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### Krok 2: Inicializace válce s posunutým vrcholem

Zde odpovídáme na **jak vytvořit válec** s vlastním posunem. Konstruktor určuje poloměr, výšku, počet segmentů (slices), vrstev (stacks) a zda je válec uzavřený. Poté posuneme vrchol pomocí `setOffsetTop`.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### Krok 3: Jak **přidat podřízený uzel v Javě** – Připojení prvního válce

Vytvoříme podřízený uzel pod kořenovým uzlem scény a přesuneme válec na požadovanou pozici.

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### Krok 4: Inicializace druhého válce (bez posunu)

Pro srovnání přidáme běžný válec bez posunutí.

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### Krok 5: Jak **přidat podřízený uzel v Javě** – Připojení druhého válce

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Krok 6: Jak **exportovat 3d model OBJ** – Uložení scény

Nakonec exportujeme celou scénu (oba válce) jako Wavefront OBJ soubor, který je široce podporován 3D nástroji.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

Po spuštění programu najdete soubor `CustomizedOffsetTopCylinder.obj` ve zvoleném adresáři, připravený k otevření v Blenderu, Maya nebo jakémkoli jiném prohlížeči podporujícím OBJ.

## Časté problémy a řešení

| Problém | Důvod | Oprava |
|-------|--------|-----|
| **OBJ soubor je prázdný** | Scéna nebyla správně uložena nebo špatná cesta. | Ověřte, že výstupní adresář existuje a máte oprávnění k zápisu. |
| **Posun nebyl aplikován** | Používáte starší verzi Aspose.3D. | Aktualizujte na nejnovější knihovnu, kde je `setOffsetTop` podporováno. |
| **Podřízený uzel není viditelný** | Transformace nebyla aplikována. | Ujistěte se, že po vytvoření podřízeného uzlu zavoláte `getTransform().setTranslation`. |

## Často kladené otázky

**Q: Je Aspose.3D kompatibilní s různými Java IDE?**  
A: Ano, funguje bez problémů v Eclipse, IntelliJ IDEA, NetBeans a dalších IDE.

**Q: Mohu na vytvořené 3D objekty aplikovat textury?**  
A: Rozhodně! Použijte třídu `Material` k přiřazení textur a povrchových vlastností.

**Q: Jaké jsou licenční možnosti pro Aspose.3D?**  
A: K dispozici je několik licenčních modelů; můžete si je prohlédnout [zde](https://purchase.aspose.com/buy).

**Q: Jak mohu získat pomoc nebo sdílet zkušenosti?**  
A: Připojte se k fóru komunity Aspose.3D [zde](https://forum.aspose.com/c/3d/18) pro podporu a diskusi.

**Q: Je k dispozici dočasná licence pro testování?**  
A: Ano, dočasnou licenci můžete získat pro hodnocení [zde](https://purchase.aspose.com/temporary-license/).

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---
**Poslední aktualizace:** 2025-12-05  
**Testováno s:** Aspose.3D pro Java 24.12 (nejnovější)  
**Autor:** Aspose