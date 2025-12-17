---
date: 2025-12-17
description: Naučte se, jak vytvořit zkroucený 3D model pomocí Aspose.3D pro Javu
  s lineárním extruzním zkroucením a exportovat soubor OBJ v Javě. Postupujte podle
  našeho krok za krokem průvodce.
linktitle: Applying Twist in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Vytvořte zkroucený 3D model – aplikace zkroucení v lineární extruzi s Aspose.3D
  pro Javu
url: /cs/java/linear-extrusion/applying-twist/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aplikace otáčení při lineární extruzi s Aspose.3D pro Java

## Introduction

Vítejte v tomto krok‑za‑krokem tutoriálu o **tom, jak vytvořit zkroucený 3D model** aplikací otáčení během lineární extruze pomocí Aspose.3D pro Java. Ať už vytváříte architektonické vizualizace, herní assety nebo inženýrské prototypy, přidání otáčení může vaší geometrii dodat dynamický, spirálovitý vzhled pomocí několika řádků kódu.

## Quick Answers
- **Co znamená „twist“ (otočení) při extruzi?** Rotuje profil kolem osy extruze, jak se tvar prodlužuje.  
- **Která třída API zpracovává otáčení?** `LinearExtrusion` poskytuje metodu `setTwist`.  
- **Potřebuji licenci pro spuštění příkladu?** Bezplatná zkušební verze stačí pro hodnocení; pro produkční nasazení je vyžadována komerční licence.  
- **Mohu výsledek exportovat jako OBJ?** Ano, použijte `scene.save(..., FileFormat.WAVEFRONTOBJ)`.  
- **Jaká verze Javy je vyžadována?** Java 8 nebo novější je plně podporována.

## Prerequisites

Než se ponoříte do tutoriálu, ujistěte se, že máte připraveny následující předpoklady:

- Vývojové prostředí Java: Ujistěte se, že máte na svém systému nainstalovanou Javu.  
- Knihovna Aspose.3D: Stáhněte a nainstalujte knihovnu Aspose.3D pro Java z [odkazu ke stažení](https://releases.aspose.com/3d/java/).  
- Dokumentace: Pro podrobné pokyny se podívejte na [dokumentaci Aspose.3D](https://reference.aspose.com/3d/java/).

## Import Packages

Před zahájením programování importujte potřebné balíčky do svého Java projektu. Zde je příklad, jak to provést:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Set Document Directory

Nejprve definujte, kam bude vygenerovaný 3D soubor uložen.

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## Initialize Base Profile

Dále vytvořte tvar, který bude extrudován. V tomto příkladu používáme obdélník s malým poloměrem zaoblení.

```java
// ExStart:InitializeBaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:InitializeBaseProfile
```

## Create a Scene

Objekt `Scene` funguje jako kontejner pro všechny 3D uzly.

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
```

## Create Nodes

Přidejte do scény dva podřízené uzly – jeden zůstane rovný, druhý dostane otáčení.

```java
// ExStart:CreateNodes
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CreateNodes
```

## Linear Extrusion Twist

Nyní provedeme **lineární extruzi s otáčením** na obou uzlech. Levý uzel získá 0° otáčení (rovný), zatímco pravý uzel získá 90° otáčení, čímž vznikne spirálovitý tvar. Také nastavíme počet řezů (slices), aby geometrie byla hladká.

```java
// ExStart:LinearExtrusionWithTwist
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd:LinearExtrusionWithTwist
```

## Export OBJ File Java

Nakonec uložte scénu do široce podporovaného formátu OBJ. Tím se demonstruje schopnost **exportu OBJ souboru v Javě** v Aspose.3D.

```java
// ExStart:Save3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:Save3DScene
```

## Why This Matters

Vytvoření zkrouceného 3D modelu vám poskytne silný vizuální efekt bez potřeby externích modelovacích nástrojů. Je to zvláště užitečné pro:

- **Mechanické součásti**, které vyžadují šroubovité prvky (např. pružiny, šrouby).  
- **Umělecké návrhy**, kde jemná spirála přidává vizuální zajímavost.  
- **Herní assety**, které těží z low‑poly, procedurálně generované geometrie.

## Common Issues & Tips

| Problém | Řešení |
|-------|----------|
| Otáčení se jeví jako ploché nebo chybí | Ujistěte se, že `setSlices` je dostatečně vysoké (např. 100) pro plynulou rotaci. |
| OBJ soubor se neotevírá ve vieweru | Zkontrolujte, že výstupní cesta (`MyDir`) je správná a soubor má oprávnění k zápisu. |
| Neočekávané škálování | Zkontrolujte jednotkový systém vašeho zdrojového profilu; Aspose.3D pracuje ve výchozím nastavení v metrech. |

## Frequently Asked Questions

**Q: Mohu použít Aspose.3D pro Java k práci s dalšími 3D formáty?**  
A: Ano, Aspose.3D podporuje širokou škálu formátů, jako jsou FBX, STL, 3MF a další.

**Q: Kde mohu najít podporu pro Aspose.3D pro Java?**  
A: Navštivte [forum Aspose.3D](https://forum.aspose.com/c/3d/18) pro komunitní pomoc a oficiální asistenci.

**Q: Je k dispozici bezplatná zkušební verze?**  
A: Ano, můžete si stáhnout zkušební verzi [zde](https://releases.aspose.com/).

**Q: Jak získám dočasnou licenci pro testování?**  
A: Získejte dočasnou licenci na [stránce dočasné licence](https://purchase.aspose.com/temporary-license/).

**Q: Kde mohu zakoupit plnou licenci?**  
A: Zakupte Aspose.3D pro Java na [stránce nákupu](https://purchase.aspose.com/buy).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2025-12-17  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

---