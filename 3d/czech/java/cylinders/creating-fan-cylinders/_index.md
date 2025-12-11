---
date: 2025-12-09
description: Naučte se, jak přidat podřízený uzel, umístit 3D objekty a uložit scénu
  jako OBJ při vytváření vlastních ventilátorových válců pomocí Aspose.3D pro Javu.
language: cs
linktitle: Adding Child Node for Fan Cylinders with Aspose.3D Java
second_title: Aspose.3D Java API
title: Přidat podřízený uzel pro vytvoření fanových válců pomocí Aspose.3D pro Javu
url: /java/cylinders/creating-fan-cylinders/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Přidání podřízeného uzlu pro vytvoření větrných válců pomocí Aspose.3D pro Java

## Úvod

Jste připraveni **přidat podřízený uzel** do 3‑D scény a vytvořit poutavé větrné válce? V tomto tutoriálu projdeme každý krok — od nastavení scény, přes umístění 3D objektů, až po **uložení scény jako OBJ** — s využitím Aspose.3D pro Java. Ať už vylepšujete herní asset nebo stavíte rychlý prototyp, koncepty zde vám poskytnou pevnou kontrolu nad vašimi 3‑D modely.

## Rychlé odpovědi
- **Co dělá „add child node“?** Vkládá nový objekt do grafu scény a dědí transformace od svého rodiče.  
- **Jak mohu umístit 3D objekt?** Aplikací translace (nebo rotace/škálování) na transformaci uzlu.  
- **Jaký formát souboru se používá pro export?** Příklad ukládá model jako soubor Wavefront OBJ.  
- **Potřebuji licenci pro spuštění kódu?** Bezplatná zkušební verze stačí pro hodnocení; licence je vyžadována pro produkční nasazení.  
- **Jaké IDE je nejlepší?** Jakékoli Java IDE (IntelliJ IDEA, Eclipse, VS Code), které podporuje JDK 8+.

## Co je „add child node“ v Aspose.3D?
Přidání podřízeného uzlu znamená vytvoření nového uzlu pod existujícím rodičem v hierarchii scény. Podřízený dědí souřadnicový systém rodiče, což usnadňuje **position 3d object** instance relativně k sobě navzájem.

## Proč přidávat podřízený uzel při tvorbě větrných válců?
- **Modulární design:** Každý válec (větrný nebo ne‑větrný) žije ve svém vlastním uzlu, což zjednodušuje pozdější úpravy.  
- **Dědičnost transformací:** Posunutím, otočením nebo škálováním rodiče se automaticky upraví všechny podřízené uzly.  
- **Čistší graf scény:** Zlepšuje čitelnost a ladění složitých modelů.

## Předpoklady

- **Java Development Kit (JDK)** – stáhněte z [oficiálního webu](https://www.oracle.com/java/technologies/javase-downloads.html).  
- **Aspose.3D pro Java** – získejte nejnovější knihovnu z [odkazu ke stažení](https://releases.aspose.com/3d/java/).

## Import balíčků

Začněte importováním potřebných balíčků do vašeho Java projektu. Tento krok je klíčový pro přístup k funkcionalitám poskytovaným Aspose.3D.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Krok 1: Vytvoření scény

Nejprve vytvoříme prázdnou 3‑D scénu, která bude hostit všechny naše objekty.

```java
// ExStart:2
// Create a Scene
Scene scene = new Scene();
// ExEnd:2
```

## Krok 2: Vytvoření větrného válce

Dále vytvoříme válec, který bude vykreslen jako větrník (částečný úsek).

```java
// ExStart:3
// Create a cylinder with fan
Cylinder fan = new Cylinder(2, 2, 10, 20, 1, false);
fan.setGenerateFanCylinder(true);
fan.setThetaLength(MathUtils.toRadian(270.0));
// ExEnd:3
```

## Krok 3: Přidání podřízeného uzlu a umístění 3D objektu

Nyní **přidáme podřízený uzel** do scény a **umístíme 3d objekt** nastavením jeho translace. Zde se větrný válec stane součástí grafu scény.

```java
// ExStart:4
// Create ChildNode and set translation
scene.getRootNode().createChildNode(fan).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

## Krok 4: Vytvoření ne‑větrného válce

Abychom ukázali flexibilitu Aspose.3D, vytvoříme také běžný válec bez větrníku a přidáme jej jako další podřízený uzel.

```java
// ExStart:5
// Create a cylinder without a fan
Cylinder nonfan = new Cylinder(2, 2, 10, 20, 1, false);
// Create ChildNode
scene.getRootNode().createChildNode(nonfan);
// ExEnd:5
```

## Krok 5: Uložení scény jako OBJ

Nakonec **uložíme scénu jako OBJ**, abyste si výsledek mohli prohlédnout v libovolném standardním 3‑D prohlížeči.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

Gratulujeme! Úspěšně jste **přidali podřízený uzel**, umístili objekty a exportovali model.

## Časté problémy a tipy

| Problém | Řešení |
|-------|----------|
| **Soubor nebyl nalezen** při ukládání | Ujistěte se, že cílový adresář existuje a máte oprávnění k zápisu. |
| **Válec vypadá plochý** | Zkontrolujte hodnoty poloměru a výšky; Aspose.3D očekává jednotky ve stejném měřítku. |
| **Úsek větrníku vypadá neúplně** | Upravit `ThetaLength` (v radiánech) tak, aby pokrýval požadovaný úhel. |
| **Scéna se nezobrazuje v prohlížeči** | Ověřte, že OBJ soubor byl uložen s připojeným souborem `.mtl` (materiál), pokud je potřeba. |

## Často kladené otázky

**Q:** *Je Aspose.3D kompatibilní s jinými Java knihovnami pro 3D modelování?*  
**A:** Ano, Aspose.3D funguje vedle jiných Java 3‑D knihoven, což vám umožní kombinovat funkce podle potřeby.

**Q:** *Mohu dále přizpůsobit vzhled vygenerovaných větrných válců?*  
**A:** Rozhodně. Můžete aplikovat materiály, textury a osvětlení pomocí tříd `Material` a `Light`.

**Q:** *Kde najdu další podporu nebo pomoc pro Aspose.3D?*  
**A:** Navštivte [Aspose.3D fórum](https://forum.aspose.com/c/3d/18) pro komunitní pomoc a oficiální odpovědi.

**Q:** *Je k dispozici bezplatná zkušební verze Aspose.3D?*  
**A:** Ano, můžete si Aspose.3D vyzkoušet pomocí [bezplatné zkušební verze](https://releases.aspose.com/) před zakoupením.

**Q:** *Jak získám dočasnou licenci pro Aspose.3D?*  
**A:** Dočasnou licenci si můžete pořídit [zde](https://purchase.aspose.com/temporary-license/) pro testování a vývoj.

## Závěr

V tomto průvodci jsme ukázali, jak **přidat podřízený uzel**, **umístit 3d objekt** a **uložit scénu jako OBJ** při tvorbě vlastních větrných válců s Aspose.3D pro Java. Tyto stavební bloky vám poskytují flexibilitu pro vytváření složitých 3‑D hierarchií a jejich export do libovolného downstream workflow.

---

**Poslední aktualizace:** 2025-12-09  
**Testováno s:** Aspose.3D 24.12 pro Java  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}