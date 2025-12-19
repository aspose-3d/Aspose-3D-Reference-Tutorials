---
date: 2025-12-19
description: Naučte se, jak vytvořit 3D scénu a exportovat 3D OBJ pomocí Twist Offset
  v lineární extruzi s Aspose.3D pro Javu.
linktitle: Create 3d scene with Twist Offset – Aspose.3D Java
second_title: Aspose.3D Java API
title: Vytvořte 3D scénu s Twist Offset – Aspose.3D Java
url: /cs/java/linear-extrusion/using-twist-offset/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Vytvořte 3D scénu s Twist Offset – Aspose.3D pro Java

## Úvod

Ve světě dynamické 3D grafiky je naučit se **vytvořit 3D scénu** s lineární extruzí skutečným průlomem. S Aspose.3D pro Java můžete posunout své dovednosti v 3D modelování tím, že do procesu lineární extruze zapojíte funkci Twist Offset. Tento tutoriál vás provede kroky využití Twist Offset v lineární extruzi pomocí Aspose.3D pro Java a poskytne vám nástroje k vytvoření úchvatných 3D scén.

## Rychlé odpovědi
- **Co dělá Twist Offset?** Posouvá začátek otáčení podél cesty extruze, čímž vám dává větší kontrolu nad geometrií.  
- **Jaký formát souboru se používá pro export?** Příklad ukládá model jako Wavefront OBJ (`.obj`).  
- **Potřebuji licenci pro vývoj?** Pro testování stačí bezplatná zkušební verze; pro produkci je vyžadována komerční licence.  
- **Jaká verze Javy je požadována?** Java 8 nebo novější.  
- **Mohu změnit počet řezů?** Ano – metoda `setSlices` určuje hladkost otáčení.

## Předpoklady

Před započetím tutoriálu se ujistěte, že máte splněny následující předpoklady:

- Java prostředí: Ujistěte se, že máte na svém systému nastavené vývojové prostředí Java.  
- Aspose.3D pro Java: Stáhněte a nainstalujte knihovnu Aspose.3D z [odkazu ke stažení](https://releases.aspose.com/3d/java/).  
- Dokumentace: Seznamte se s [dokumentací Aspose.3D pro Java](https://reference.aspose.com/3d/java/).  

## Import balíčků

Ve svém Java projektu importujte potřebné balíčky, abyste mohli začít používat Aspose.3D pro Java. Zajistěte, aby byly zahrnuty požadované knihovny pro bezproblémovou integraci.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Krok 1: Nastavení prostředí

Začněte nastavením vývojového prostředí Java a ujistěte se, že Aspose.3D pro Java je správně nainstalováno.

## Krok 2: Inicializace základního profilu

Vytvořte základní profil pro extruzi, v tomto případě `RectangleShape` s poloměrem zaoblení 0,3.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
// Initialize the base profile to be extruded
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Krok 3: Vytvoření 3D scény

Sestavte 3D scénu, která bude hostit vaše extrudované objekty.

```java
// Create a scene
Scene scene = new Scene();
```

## Krok 4: Vytvoření uzlů

Generujte uzly ve scéně, které budou představovat různé entity.

```java
// Create left node
Node left = scene.getRootNode().createChildNode();
// Create right node
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Krok 5: Provedení lineární extruze

Použijte lineární extruzi na levém i pravém uzlu s různými vlastnostmi.

```java
// Perform linear extrusion on left node using twist and slices property
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// Perform linear extrusion on right node using twist, twist offset, and slices property
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

## Krok 6: Uložení 3D scény

Uložte nově vytvořenou 3D scénu ve specifikovaném formátu souboru.

```java
// Save 3D scene
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Jak uložit 3D model a exportovat 3D OBJ

Volání `scene.save` v předchozím kroku **uloží 3D model** jako soubor OBJ, což je široce podporovaný **formát exportu 3D OBJ**. Název souboru můžete změnit nebo zvolit jiný podporovaný formát (např. STL, FBX) úpravou výčtu `FileFormat`.

## Závěr

Gratulujeme! Úspěšně jste implementovali Twist Offset v lineární extruzi pomocí Aspose.3D pro Java. Tato výkonná funkce otevírá nové možnosti pro vaše 3D modelování, umožňuje vám **vytvořit 3D scénu** s propracovanými otáčkami a posuny a následně **uložit 3D model** ve formátu připraveném pro další zpracování.

## Často kladené otázky

### Q1: Mohu použít Aspose.3D pro Java v nekomerčních projektech?

A1: Ano, Aspose.3D pro Java může být používán jak v komerčních, tak v nekomerčních projektech. Podívejte se na [licenční možnosti](https://purchase.aspose.com/buy) pro více informací.

### Q2: Kde najdu podporu pro Aspose.3D pro Java?

A2: Navštivte [forum Aspose.3D pro Java](https://forum.aspose.com/c/3d/18), kde získáte pomoc a spojíte se s komunitou.

### Q3: Je k dispozici bezplatná zkušební verze Aspose.3D pro Java?

A3: Ano, můžete si vyzkoušet bezplatnou verzi na [stránce vydání](https://releases.aspose.com/).

### Q4: Jak získám dočasnou licenci pro Aspose.3D pro Java?

A4: Dočasnou licenci pro váš projekt získáte na [této stránce](https://purchase.aspose.com/temporary-license/).

### Q5: Existují další příklady a tutoriály?

A5: Ano, podívejte se do [dokumentace](https://reference.aspose.com/3d/java/) pro více příkladů a podrobných tutoriálů.

## Často kladené otázky

**Q: Je tento tutoriál součástí série tutoriálů Aspose 3D?**  
A: Ano – jedná se o oficiální **Aspose 3D tutoriál**, který demonstruje konkrétní funkci knihovny.

**Q: Mohu místo obdélníku použít jiný tvar?**  
A: Rozhodně. Jakákoli implementace `IProfile` (např. `CircleShape`, vlastní `PolygonShape`) může být extrudována.

**Q: Co se stane, když vynechám `setTwistOffset`?**  
A: Extruze začne otáčet od počátku profilu, což vede k symetrickému otáčení.

**Q: Jak zvýšit hladkost otáčení?**  
A: Zvyšte hodnotu předanou metodě `setSlices`; vyšší počet řezů vytváří hladší geometrii.

**Q: Jaké další formáty souborů mohu exportovat kromě OBJ?**  
A: Aspose.3D podporuje STL, FBX, GLTF, 3MF a několik dalších formátů prostřednictvím výčtu `FileFormat`.

---

**Poslední aktualizace:** 2025-12-19  
**Testováno s:** Aspose.3D 24.11 pro Java  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}