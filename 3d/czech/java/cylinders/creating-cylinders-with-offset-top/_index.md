---
date: 2026-02-07
description: Naučte se, jak v Aspose.3D pro Javu vytvářet modely válců s posunutými
  vršky, přidávat kroky pro podřízené uzly v Javě a snadno exportovat 3D modely do
  souborů OBJ.
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

Pokud hledáte **how to create cylinder** objekty s vlastním posunutým vrcholem v 3D scéně založené na Javě, Aspose.3D proces zjednodušuje. V tomto tutoriálu projdeme každý krok – od nastavení scény až po export finálního modelu jako souboru OBJ – abyste mohli s jistotou integrovat válce s posunutým vrcholem do svých aplikací. Na konci průvodce ovládnete, jak vytvořit válec s vlastními posuny pomocí několika řádků kódu.

## Rychlé odpovědi
- **Jaká knihovna se používá?** Aspose.3D for Java  
- **Mohu posunout vrchol válce?** Ano, pomocí `setOffsetTop`  
- **Jak přidám podřízený uzel v Javě?** Zavolejte `createChildNode` na kořenovém uzlu  
- **Do jakého formátu mohu exportovat?** Wavefront OBJ (`export 3d model obj`)  
- **Potřebuji licenci pro testování?** Dočasná licence je k dispozici pro hodnocení  

## Co je “how to create cylinder” s posunutým vrcholem?

Vytvoření válce s posunutým vrcholem znamená, že horní kruhová plocha je posunuta vzhledem k základně, což vám umožní modelovat kuželovité nebo asymetrické tvary bez ruční manipulace s vrcholy. Aspose.3D poskytuje dedikovaný konstruktor a vlastnost `OffsetTop`, která to umožňuje během několika řádků kódu.

## Proč použít Aspose.3D pro Java?

- **High‑level API:** Není potřeba spravovat data nízkoúrovňové sítě.  
- **Cross‑platform:** Funguje v jakémkoli prostředí kompatibilním s JVM.  
- **Built‑in exporters:** Přímé uložení do OBJ, STL, FBX a dalších.  
- **Extensible:** Snadno přidávejte podřízené uzly, aplikujte transformace a integrujte s dalšími Java knihovnami.

## Požadavky

- **Java Development Kit (JDK)** – nainstalovaná kompatibilní verze.  
- **Aspose.3D for Java library** – stáhněte nejnovější JAR z oficiálního webu [zde](https://releases.aspose.com/3d/java/).  
- IDE dle vašeho výběru (Eclipse, IntelliJ IDEA, NetBeans, atd.).

## Import balíčků

Nejprve importujte třídy, které budeme potřebovat. Umístěte tyto příkazy na začátek svého Java souboru:

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Postupný průvodce

### Krok 1: Vytvořit scénu

Scéna funguje jako kontejner pro všechny 3D objekty.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### Krok 2: Inicializovat válec s posunutým vrcholem

Zde odpovídáme na **how to create cylinder** s vlastním posunem. Konstruktor definuje poloměr, výšku, počet řezu, počet vrstev a zda je válec uzavřen. Poté posuneme horní část pomocí `setOffsetTop`.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### Krok 3: Jak **add child node Java** – Připojit první válec

Vytvoříme podřízený uzel pod kořenovým uzlem scény a přesuneme válec na požadovanou pozici.

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### Krok 4: Inicializovat druhý válec (bez posunu)

Pro srovnání přidáme běžný válec bez posunu.

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### Krok 5: Jak **add child node Java** – Připojit druhý válec

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Krok 6: Jak **export OBJ** – Uložit scénu jako OBJ

Nakonec exportujeme celou scénu (obě válce) jako soubor Wavefront OBJ, který je široce podporován 3D nástroji.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

Po spuštění programu najdete `CustomizedOffsetTopCylinder.obj` ve zvoleném adresáři, připravený k otevření v Blenderu, Maya nebo jakémkoli jiném prohlížeči kompatibilním s OBJ.

## Proč je to důležité – reálné případy použití

- **Architektonická vizualizace:** Válce s posunutým vrcholem jsou ideální pro modelování sloupů, které se zužují směrem ke stropu.  
- **Mechanické součásti:** Vytvořte písty nebo pouzdra ozubených kol, kde je horní povrch úmyslně posunut.  
- **Herní assety:** Rychle generujte různé tvary sloupů bez ruční tvorby sítí.

## Jak exportovat OBJ – uložit scénu jako OBJ

Schopnost Aspose 3D exportovat OBJ vám umožní sdílet modely s téměř jakýmkoli 3D pipeline. Použitím metody `scene.save(..., FileFormat.WAVEFRONTOBJ)` můžete **how to export obj** soubory přímo z Javy, čímž eliminujete potřebu třetích konvertorů.

## Jak přidat podřízený uzel Java – připojení geometrie

Přidávání podřízených uzlů je standardní způsob organizace grafu scény. Každé volání `createChildNode` vrací uzel, který může být transformován nezávisle, což je důvod, proč se vzor **add child node java** objevuje dvakrát v tomto tutoriálu.

## Export 3D modelu OBJ – pomocí Aspose 3D Export OBJ

Pokud potřebujete distribuovat své modely designérům, funkce **export 3d model obj** poskytuje lehkou, textovou reprezentaci, která funguje napříč všemi hlavními 3D aplikacemi. Stejný API‑volání použité v kroku 6 demonstruje workflow **aspose 3d export obj**.

## Časté problémy a řešení

| Problém | Důvod | Řešení |
|-------|--------|-----|
| **Soubor OBJ je prázdný** | Scéna nebyla správně uložena nebo je špatná cesta. | Zkontrolujte, že výstupní adresář existuje a máte oprávnění k zápisu. |
| **Posun nebyl aplikován** | Používáte starší verzi Aspose.3D. | Aktualizujte na nejnovější knihovnu, kde je podporována metoda `setOffsetTop`. |
| **Podřízený uzel není viditelný** | Transformace nebyla aplikována. | Ujistěte se, že po vytvoření podřízeného uzlu zavoláte `getTransform().setTranslation`. |

## Často kladené otázky

**Q: Je Aspose.3D kompatibilní s různými Java IDE?**  
A: Ano, funguje bez problémů s Eclipse, IntelliJ IDEA, NetBeans a dalšími IDE.

**Q: Mohu na vytvořené 3D objekty aplikovat textury?**  
A: Rozhodně! Použijte třídu `Material` k přiřazení textur a povrchových vlastností.

**Q: Existují licenční možnosti pro Aspose.3D?**  
A: K dispozici je několik licenčních modelů; můžete si je prohlédnout [zde](https://purchase.aspose.com/buy).

**Q: Jak mohu získat pomoc nebo sdílet zkušenosti?**  
A: Připojte se k fóru komunity Aspose.3D [zde](https://forum.aspose.com/c/3d/18) pro podporu a diskusi.

**Q: Je dočasná licence k dispozici pro testování?**  
A: Ano, dočasnou licenci lze získat pro hodnocení [zde](https://purchase.aspose.com/temporary-license/).

**Poslední aktualizace:** 2026-02-07  
**Testováno s:** Aspose.3D for Java 24.12 (latest)  
**Autor:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}