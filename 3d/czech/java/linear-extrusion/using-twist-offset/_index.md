---
date: 2026-02-22
description: Naučte se, jak vytvořit 3D scénu a exportovat ji pomocí Aspose.3D pro
  Javu s lineárním extruzním zkroucením a posunem zkroucení.
linktitle: Using Twist Offset in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Jak vytvořit 3D scénu s Twist Offset při lineárním extrudování pomocí Aspose.3D
  pro Javu
url: /cs/java/linear-extrusion/using-twist-offset/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Použití Twist Offset při lineární extruzi s Aspose.3D pro Java

## Úvod

Ve dynamickém světě 3D grafiky je ovládnutí umění **create 3d scene** průlomem pro jakýkoli projekt 3D modelování v Javě. S Aspose.3D pro Java můžete nejen lineárně extrudovat tvary, ale také přidat twist offset pro vytvoření složité, zkroucené geometrie. Tento tutoriál vás provede všemi kroky potřebnými k **create 3d scene**, aplikaci lineárního twistu při extruzi a nakonec **export 3d scene** do běžného souboru OBJ.

## Rychlé odpovědi
- **Co dělá Twist Offset?** Posouvá počáteční bod twistu, což vám umožňuje posunout rotaci podél cesty extruze.  
- **Která třída provádí lineární extruzi?** `LinearExtrusion` – můžete na ní nastavit twist, slices a twist offset.  
- **Mohu výsledek exportovat?** Ano, zavolejte `scene.save(..., FileFormat.WAVEFRONTOBJ)` pro export 3D scény.  
- **Potřebuji licenci pro vývoj?** Dočasná licence stačí pro testování; plná licence je vyžadována pro produkci.  
- **Jaká verze Javy je podporována?** Jakékoli prostředí Java 8+ funguje s nejnovější knihovnou Aspose.3D.

## Co je „create 3d scene“ v Aspose.3D?
Vytvoření 3D scény znamená vytvoření instance objektu `Scene`, přidání uzlů (objektů) do jeho hierarchie a nakonec uložení scény do souborového formátu dle vašeho výběru. To je základ pro jakýkoli workflow 3D modelování v Javě.

## Proč použít lineární extruzi s twistem a twist offsetem?
Přidání twistu během extruze vám poskytne spirálové tvary, jako jsou šroubovité sloupy nebo dekorativní úchyty. Twist offset vám umožní zahájit twist na vlastní pozici, což nabízí jemnější kontrolu nad konečným tvarem – ideální pro mechanické součásti, umělecké modely nebo architektonické detaily.

## Předpoklady

Předtím, než se ponoříte do tutoriálu, ujistěte se, že máte následující předpoklady připravené:

- **Java prostředí:** Ujistěte se, že máte na svém systému nastavené vývojové prostředí Java.  
- **Aspose.3D pro Java:** Stáhněte a nainstalujte knihovnu Aspose.3D z [download link](https://releases.aspose.com/3d/java/).  
- **Dokumentace:** Seznamte se s [Aspose.3D pro Java dokumentací](https://reference.aspose.com/3d/java/).

## Import balíčků

Ve vašem Java projektu importujte potřebné balíčky, abyste mohli začít používat Aspose.3D pro Java. Ujistěte se, že zahrnujete požadované knihovny pro bezproblémovou integraci.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Jak vytvořit 3d scene – krok za krokem průvodce

### Krok 1: Nastavení prostředí
Začněte nastavením vašeho vývojového prostředí Java a ujistěte se, že Aspose.3D pro Java je správně nainstalováno. Tento krok je nezbytný pro jakoukoli práci s **java 3d modeling**.

### Krok 2: Inicializace základního profilu
Vytvořte základní profil pro extruzi, v tomto případě `RectangleShape` s poloměrem zaoblení 0,3. Profil definuje průřez, který bude veden podél cesty extruze.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
// Initialize the base profile to be extruded
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### Krok 3: Vytvoření 3D scény
Vytvořte 3D scénu, která bude obsahovat vaše extrudované objekty. Zde budete **create child node** prvky, které představují jednotlivé geometrické části.

```java
// Create a scene
Scene scene = new Scene();
```

### Krok 4: Vytvoření uzlů
Vygenerujte uzly ve scéně, které budou představovat různé entity. Zde vytvoříme dva sourozenecké uzly – jeden pro jednoduchou extruzi a druhý, který používá twist offset.

```java
// Create left node
Node left = scene.getRootNode().createChildNode();
// Create right node
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Krok 5: Provedení lineární extruze s twistem a twist offsetem
Aplikujte lineární extruzi na oba uzly. Levý uzel ukazuje základní twist, zatímco pravý uzel přidává twist offset, aby ilustroval další kontrolu, kterou tato funkce poskytuje.

```java
// Perform linear extrusion on left node using twist and slices property
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// Perform linear extrusion on right node using twist, twist offset, and slices property
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

> **Tip:** Upravte `setSlices()`, aby se zvýšila rozlišení sítě, když potřebujete hladší zakřivení.

### Krok 6: Uložení 3D scény (Export 3d scene)
Nakonec exportujte sestavenou scénu do souboru OBJ, abyste ji mohli zobrazit v libovolném standardním 3D prohlížeči nebo importovat do dalších pipeline.

```java
// Save 3D scene
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Po úspěšném spuštění kódu najdete `TwistOffsetInLinearExtrusion.obj` ve specifikovaném adresáři, připravený k otevření v nástrojích jako Blender, MeshLab nebo jakémkoli CAD softwaru.

## Časté problémy a řešení
| Problém | Proč se to stane | Řešení |
|-------|----------------|-----|
| **Scéna se uloží jako prázdný soubor** | `MyDir` cesta je nesprávná nebo chybí oprávnění k zápisu. | Ověřte, že adresář existuje a je zapisovatelný, nebo použijte absolutní cestu. |
| **Twist vypadá plochý** | `setSlices()` je příliš nízké, což vede k hrubé síti. | Zvyšte počet slice (např. 200) pro hladší twisty. |
| **Twist offset nemá žádný efekt** | Vektor offsetu je kolineární s směrem extruze. | Použijte nenulovou složku X nebo Y, abyste viděli posun offsetu. |

## Často kladené otázky

### Q1: Mohu používat Aspose.3D pro Java v nekomerčních projektech?
A1: Ano, Aspose.3D pro Java může být používáno jak v komerčních, tak v nekomerčních projektech. Podívejte se na [licensing options](https://purchase.aspose.com/buy) pro více detailů.

### Q2: Kde mohu najít podporu pro Aspose.3D pro Java?
A2: Navštivte [Aspose.3D pro Java fórum](https://forum.aspose.com/c/3d/18), kde získáte pomoc a spojíte se s komunitou.

### Q3: Je k dispozici bezplatná zkušební verze Aspose.3D pro Java?
A3: Ano, můžete vyzkoušet bezplatnou zkušební verzi na [releases page](https://releases.aspose.com/).

### Q4: Jak získám dočasnou licenci pro Aspose.3D pro Java?
A4: Získejte dočasnou licenci pro váš projekt na [this link](https://purchase.aspose.com/temporary-license/).

### Q5: Jsou k dispozici další příklady a tutoriály?
A5: Ano, podívejte se do [documentation](https://reference.aspose.com/3d/java/) pro více příkladů a podrobných tutoriálů.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Poslední aktualizace:** 2026-02-22  
**Testováno s:** Aspose.3D for Java 24.11 (latest)  
**Autor:** Aspose