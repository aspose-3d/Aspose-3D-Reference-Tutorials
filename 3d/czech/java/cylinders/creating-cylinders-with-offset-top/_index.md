---
date: 2026-04-08
description: Naučte se, jak vytvořit válec s posunutým vrcholem v Aspose.3D pro Javu,
  přidat podřízený uzel v Javě, nastavit posunutý vrchol, vygenerovat 3D model a exportovat
  OBJ pomocí dočasné licence Aspose.
keywords:
- aspose temporary license
- generate 3d model
- add child node java
- java export obj
- set offset top
linktitle: Dočasná licence Aspose – Vytvořit válec s posunutým vrcholem (Java)
second_title: Aspose.3D Java API
title: Dočasná licence Aspose – Vytvořit válec s posunutým horním okrajem (Java)
url: /cs/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose Temporary License – Vytvoření válce s posunutým vrcholem (Java)

## Úvod

Pokud hledáte **create cylinder** objekty s vlastním posunutým vrcholem v 3D scéně založené na Javě, Aspose.3D proces zjednodušuje. V tomto tutoriálu projdeme každý krok – od nastavení scény po export finálního modelu jako soubor OBJ – abyste mohli integrovat válce s posunutým vrcholem do svých aplikací s jistotou. Na konci průvodce také pochopíte, jak **aspose temporary license** umožňuje vyhodnotit tyto funkce bez úplného nákupu.

## Rychlé odpovědi
- **Jaká knihovna se používá?** Aspose.3D for Java  
- **Mohu posunout vrchol válce?** Ano, pomocí `setOffsetTop`  
- **Jak přidám podřízený uzel v Javě?** Zavolejte `createChildNode` na kořenovém uzlu  
- **Do jakého formátu mohu exportovat?** Wavefront OBJ (`java export obj`)  
- **Potřebuji licenci pro testování?** **aspose temporary license** je k dispozici pro vyhodnocení  

## Co je Aspose Temporary License?

**aspose temporary license** je krátkodobý, bezplatný evaluační klíč, který odemyká kompletní sadu funkcí Aspose.3D pro Java během vývoje a testování. Odstraňuje vodoznaky hodnocení a umožňuje generovat soubory 3D modelů, jako jsou OBJ, STL nebo FBX, přesně jako placená licence.

## Proč používat Aspose.3D pro Java?

- **High‑level API:** Není nutné spravovat nízkoúrovňová data meshe.  
- **Cross‑platform:** Funguje v jakémkoli prostředí kompatibilním s JVM.  
- **Built‑in exporters:** Přímé ukládání do OBJ, STL, FBX a dalších.  
- **Extensible:** Snadno přidávejte podřízené uzly, aplikujte transformace a integrujte s dalšími Java knihovnami.  

## Požadavky

Before we dive in, make sure you have:

- **Java Development Kit (JDK)** – nainstalovaná kompatibilní verze.  
- **Aspose.3D for Java library** – stáhněte nejnovější JAR z oficiálního webu [here](https://releases.aspose.com/3d/java/).  
- IDE dle vašeho výběru (Eclipse, IntelliJ IDEA, NetBeans atd.).  

## Import balíčků

Nejprve importujte třídy, které budeme potřebovat. Umístěte tyto příkazy na začátek vašeho Java souboru:

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Postupný průvodce

### Krok 1: Vytvoření Java 3D scény

**java 3d scene** funguje jako kontejner pro všechny 3D objekty.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### Krok 2: Inicializace válce s posunutým vrcholem

Zde odpovídáme na otázku **how to create cylinder** s vlastním posunutím. Konstruktor určuje poloměr, výšku, řezy, vrstvy a zda je válec uzavřený. Poté posuneme vrchol pomocí `setOffsetTop`.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### Krok 3: Přidání podřízeného uzlu Java – Připojení první válce

Vytvoříme podřízený uzel pod kořenovým uzlem scény a přesuneme válec na požadovanou pozici.

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### Krok 4: Inicializace druhé válce (bez posunu)

Pro srovnání přidáme běžnou válcovou bez posunu.

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### Krok 5: Přidání podřízeného uzlu Java – Připojení druhé válce

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Krok 6: Java Export OBJ – Uložení scény jako OBJ

Nakonec **java export obj** celou scénu (obě válce) jako soubor Wavefront OBJ, který je široce podporován 3D nástroji.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

Po spuštění programu najdete `CustomizedOffsetTopCylinder.obj` ve zvoleném adresáři, připravený k otevření v Blenderu, Maya nebo jakémkoli jiném prohlížeči podporujícím OBJ.

## Jak vygenerovat 3D model a exportovat OBJ v Javě

Kombinace `Scene.save(..., FileFormat.WAVEFRONTOBJ)` a **aspose temporary license** vám umožní rychle **generate 3d model** soubory, aniž byste potřebovali externí konvertory. To je zvláště užitečné během prototypování nebo při sdílení assetů s designéry.

## Reálné příklady použití

- **Architectural visualisation:** Válce s posunutým vrcholem modelují sloupy, které se zužují směrem ke stropu.  
- **Mechanical parts:** Vytvářejte písty nebo pouzdra ozubených kol, kde je horní povrch úmyslně posunut.  
- **Game assets:** Produkujte různé tvary sloupů za běhu, čímž snižujete potřebu ručně vytvářených meshů.

## Časté problémy a řešení

| Problém | Důvod | Řešení |
|-------|--------|-----|
| **OBJ file is empty** | Scéna nebyla správně uložena nebo špatná cesta. | Ověřte, že výstupní adresář existuje a máte oprávnění k zápisu. |
| **Offset not applied** | Používáte starší verzi Aspose.3D. | Aktualizujte na nejnovější knihovnu, kde je podporováno `setOffsetTop`. |
| **Child node not visible** | Transformace nebyla aplikována. | Ujistěte se, že po vytvoření podřízeného uzlu zavoláte `getTransform().setTranslation`. |

## Často kladené otázky

**Q: Je Aspose.3D kompatibilní s různými Java IDE?**  
A: Ano, funguje bez problémů s Eclipse, IntelliJ IDEA, NetBeans a dalšími IDE.

**Q: Mohu aplikovat textury na vytvořené 3D objekty?**  
A: Rozhodně! Použijte třídu `Material` k přiřazení textur a vlastností povrchu.

**Q: Existují licenční možnosti pro Aspose.3D?**  
A: K dispozici je několik licenčních modelů; můžete si je prohlédnout [here](https://purchase.aspose.com/buy).

**Q: Jak mohu získat pomoc nebo sdílet zkušenosti?**  
A: Připojte se k fóru komunity Aspose.3D [here](https://forum.aspose.com/c/3d/18) pro podporu a diskuzi.

**Q: Je dočasná licence k dispozici pro testování?**  
A: Ano, **aspose temporary license** lze získat pro vyhodnocení [here](https://purchase.aspose.com/temporary-license/).

---

**Poslední aktualizace:** 2026-04-08  
**Testováno s:** Aspose.3D for Java 24.12 (nejnovější)  
**Autor:** Aspose

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}