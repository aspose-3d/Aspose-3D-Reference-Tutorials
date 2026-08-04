---
date: 2026-04-03
description: Naučte se, jak vytvořit tvar válcového větráku v Javě pomocí Aspose.3D.
  Tento průvodce pokrývá 3D modelování v Javě a techniky ukládání souborů OBJ v Javě.
keywords:
- create cylinder fan shape
- save obj file java
- aspose 3d export obj
linktitle: Jak vytvořit tvar válcového větráku pomocí Aspose.3D pro Javu
second_title: Aspose.3D Java API
title: Jak vytvořit tvar ventilátoru ve tvaru válce pomocí Aspose.3D pro Javu
url: /cs/java/cylinders/creating-fan-cylinders/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak vytvořit tvar ventilátoru válce pomocí Aspose.3D pro Java

## Úvod

Připraveni ovládnout **jak vytvořit tvar ventilátoru válce** v prostředí Java? V tomto tutoriálu vás provedeme každým krokem – od nastavení scény po export souboru Wavefront OBJ – pomocí Aspose.3D. Ať už vytváříte herní asset, CAD prototyp, nebo jen experimentujete s 3D geometrií, uvidíte, jak snadné může být modelování v Java 3D s touto výkonnou knihovnou.

## Rychlé odpovědi
- **Jaký je hlavní cíl?** Vytvořit přizpůsobitelný válcový ventilátor a uložit jej jako soubor OBJ.  
- **Která knihovna je použita?** Aspose.3D pro Java.  
- **Potřebuji licenci?** Bezplatná zkušební verze funguje pro vývoj; pro produkci je vyžadována komerční licence.  
- **Jaké jsou předpoklady?** Nainstalovaný JDK a přidaný balíček Aspose.3D Java do vašeho projektu.  
- **Mohu exportovat jiné formáty?** Ano – Aspose.3D podporuje mnoho formátů; tento příklad používá Wavefront OBJ.

## Co je ventilátorový válec?

Ventilátorový válec je část povrchu válce, kde je vynechán sektor kruhové základny, čímž vzniká „ventilátorové“ otvor. Tato geometrie je užitečná pro vizualizaci výseků, dashboardů nebo vlastních mechanických částí.

## Proč použít Aspose.3D pro modelování 3D v Javě?

Aspose.3D poskytuje čisté, objektově orientované API, které abstrahuje nízkoúrovňovou matematiku 3D grafiky. Můžete se soustředit na návrh místo detailů formátů souborů a knihovna automaticky provádí operace **save obj file java**.

## Předpoklady

Než se pustíme dál, ujistěte se, že máte:

- **Java Development Kit (JDK)** – stáhněte jej [zde](https://www.oracle.com/java/technologies/javase-downloads.html).  
- **Aspose.3D pro Java** – získejte nejnovější JAR z [odkazu ke stažení](https://releases.aspose.com/3d/java/).  

Přidejte JAR Aspose.3D do classpath vašeho projektu.

## Import balíčků

Začněte importováním potřebných tříd. To vám poskytne přístup k 3D scéně, geometrickým primitivům a utilitním metodám.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Krok 1: Vytvořit scénu

Nejprve vytvoříme novou `Scene`. Scéna je kontejner, který drží všechny vaše 3D objekty, světla a kamery.

```java
// ExStart:2
// Create a Scene
Scene scene = new Scene();
// ExEnd:2
```

## Krok 2: Vytvořit ventilátorový válec (jak vytvořit válec)

Nyní postavíme samotný ventilátorový válec. Parametry konstruktoru definují poloměr, výšku, tessellaci a zda je geometrie generována jako ventilátor.

```java
// ExStart:3
// Create a cylinder with fan
Cylinder fan = new Cylinder(2, 2, 10, 20, 1, false);
fan.setGenerateFanCylinder(true);
fan.setThetaLength(MathUtils.toRadian(270.0));
// ExEnd:3
```

> **Pro tip:** Upravit `setThetaLength` pro změnu úhlu otvoru. 270° vytvoří tříčtvrtinový ventilátor; 180° by dal půl‑válec.

## Krok 3: Umístit ventilátorový válec

Dále přidáme ventilátorový válec do scény a přesuneme jej na vhodné místo. Souřadnice translace jsou v pořadí (X, Y, Z).

```java
// ExStart:4
// Create ChildNode and set translation
scene.getRootNode().createChildNode(fan).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

## Krok 4: Vytvořit ne‑ventilátorový válec (porovnání modelování 3D v Javě)

Abychom ukázali flexibilitu Aspose.3D, vytvoříme také běžný válec bez otvoru ventilátoru.

```java
// ExStart:5
// Create a cylinder without a fan
Cylinder nonfan = new Cylinder(2, 2, 10, 20, 1, false);
// Create ChildNode
scene.getRootNode().createChildNode(nonfan);
// ExEnd:5
```

## Krok 5: Uložit scénu (uložení obj souboru v Javě)

Nakonec exportujeme celou scénu do souboru Wavefront OBJ. Tento formát je široce podporován většinou 3D editorů a herních engineů.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

> **Poznámka:** Nahraďte `"Your Document Directory"` absolutní nebo relativní cestou, kde máte oprávnění k zápisu.

## Jak uložit OBJ soubor v Javě pomocí Aspose 3D

Metoda `Scene.save` v Aspose.3D automaticky zpracuje proces **aspose 3d export obj**. Stačí zadat cílový název souboru a hodnotu výčtu `FileFormat.WAVEFRONTOBJ`, jak je ukázáno v předchozím kroku.

## Časté problémy a řešení

| Problém | Důvod | Řešení |
|-------|--------|-----|
| Soubor OBJ je prázdný | Scéna nebyla uložena nebo je cesta nesprávná | Ověřte, že výstupní adresář existuje a má právo zápisu. |
| Otevření ventilátoru vypadá špatně | Nesprávná hodnota `ThetaLength` | Použijte `MathUtils.toRadian(degrees)` pro nastavení přesného úhlu, který potřebujete. |
| Chyby při kompilaci | Chybějící JAR Aspose.3D v classpath | Přidejte JAR do složky `libs` vašeho projektu a zahrňte jej do cesty sestavení. |

## Často kladené otázky

**Q: Je Aspose.3D kompatibilní s jinými Java 3D knihovnami?**  
A: Ano, Aspose.3D může koexistovat s knihovnami jako Java 3D nebo jMonkeyEngine, což vám umožní integrovat vlastní geometrii do větších pipeline.

**Q: Mohu dále přizpůsobit vzhled ventilátorového válce?**  
A: Rozhodně. Můžete aplikovat materiály, textury a osvětlení přístupem k kolekcím `Material` a `Light` uzlu.

**Q: Kde mohu získat další podporu?**  
A: Navštivte [Aspose.3D fórum](https://forum.aspose.com/c/3d/18) pro komunitní pomoc a oficiální odpovědi.

**Q: Je k dispozici bezplatná zkušební verze?**  
A: Ano, můžete prozkoumat Aspose.3D pomocí [bezplatné zkušební verze](https://releases.aspose.com/) před zakoupením.

**Q: Jak získat dočasnou licenci pro testování?**  
A: Získejte ji [zde](https://purchase.aspose.com/temporary-license/) pro odemknutí plné funkčnosti během vývoje.

---

**Poslední aktualizace:** 2026-04-03  
**Testováno s:** Aspose.3D 24.11 pro Java  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}