---
date: 2025-12-18
description: Naučte se, jak vytvořit 3D scénu a uložit soubor OBJ pomocí Aspose.3D
  pro Javu. Postupujte podle našeho krok‑za‑krokem průvodce pro směr lineární extruze.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Vytvořte 3D scénu – nastavte směr extruze Aspose.3D Java
url: /cs/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Vytvoření 3D scény – nastavení směru extruze Aspose.3D Java

## Úvod

V tomto tutoriálu se naučíte **jak vytvořit 3D scénu** objektů a ovládat směr extruze pomocí Aspose.3D pro Java. Ať už vytváříte architektonické vizualizace, prototypy produktů nebo herní assety, zvládnutí lineární extruze vám poskytne flexibilitu rychle modelovat složité tvary. Provedeme vás každým krokem, od přidání uzlů v Javě až po **export 3D modelu obj** souborů, abyste výsledek viděli okamžitě.

## Rychlé odpovědi
- **Co znamená “create 3d scene”?** Jedná se o inicializaci objektu Aspose.3D `Scene`, který bude obsahovat veškerou geometrii, světla a kamery.  
- **Jak nastavit směr extruze?** Použijte metodu `setDirection(Vector3)` na instanci `LinearExtrusion`.  
- **Jaký formát použít pro export?** Formát OBJ (`FileFormat.WAVEFRONTOBJ`) je široce podporován pro 3‑D pracovní postupy.  
- **Potřebuji licenci pro Aspose.3D?** Pro vývoj stačí bezplatná zkušební verze; pro produkci je vyžadována komerční licence.  
- **Mohu v Javě přidat více uzlů?** Ano – použijte `scene.getRootNode().createChildNode()` a přidejte tolik objektů, kolik potřebujete.

## Co je workflow “create 3d scene”?

Workflow **create 3d scene** začíná prázdným objektem `Scene`, přidává geometrii (např. extrudované profily), umisťuje ji pomocí transformací a nakonec ukládá scénu do souborového formátu, jako je OBJ. Tento vzor je základem většiny 3‑D aplikací postavených na Aspose.3D.

## Proč nastavit směr extruze?

Nastavení směru extruze vám umožní naklonit, otočit nebo zkosit tvar během samotné extruze, čímž získáte kontrolu nad konečnou geometrií bez dalšího post‑processingu. Je to zvláště užitečné pro:

- Vytváření kuželovitých sloupů nebo potrubí na míru.  
- Zarovnání extruzí s nestmi osami v mechanických součástech.  
- Generování uměleckých tvarů pro vizuální efekty.

## Předpoklady

Než se pustíme dál, ujistěte se, že máte:

- Základní znalosti Javy.  
- Nainstalovanou knihovnu Aspose.3D – stáhněte ji [zde](https://releases.aspose.com/3d/java/).  
- IDE, jako je Eclipse nebo IntelliJ IDEA.

## Import balíčků

Nejprve importujte požadované třídy Aspose.3D:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Krok 1: Inicializace základního profilu

Vytvořte 2‑D profil, který bude extrudován. V tomto příkladu použijeme zaoblený obdélník:

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

> **Pro tip:** Upravením poloměru zaoblení ovlivníte, jak ostré nebo hladké budou rohy obdélníku před extruzí.

## Krok 2: Vytvoření scény

Nyní **create 3d scene**, která bude hostovat naše objekty:

```java
Scene scene = new Scene();
```

## Krok 3: Přidání uzlů v Javě – umístění objektů

Přidáme dva podřízené uzly (levý a pravý) k kořenovému uzlu scény a posuneme levý trochu do strany:

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Krok 4: Jak extrudovat – levý uzel (výchozí směr)

Extrudujte profil na levém uzlu pomocí výchozího směru podél osy Z. Také nastavíme úplný 360° otáčení a zvýšíme počet řezů pro hladkost:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Krok 5: Jak nastavit směr – pravý uzel

Zde **how to set direction** pomocí vlastního `Vector3`. Tento vektor nakloní extruzi směrem k vektoru (0.3, 0.2, 1):

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Krok 6: Uložení OBJ souboru – export 3D modelu

Nakonec **save obj file**, abyste výsledek viděli v libovolném 3‑D prohlížeči:

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Po otevření vygenerovaného OBJ souboru uvidíte dva extrudované obdélníky: jeden s výchozím směrem a druhý nakloněný podle nastaveného vektoru.

## Časté problémy a řešení

| Problém | Důvod | Řešení |
|---------|-------|--------|
| OBJ soubor je prázdný | Scéna nebyla uložena nebo je špatná cesta | Ověřte, že `MyDir` ukazuje na zapisovatelnou složku a název souboru končí na `.obj`. |
| Extruze vypadá plochá | `setSlices` nastaveno příliš nízko | Zvyšte `setSlices` (např. na 200) pro hladší geometrii. |
| Směr se nezdá změněn | Vektor není normalizován | Použijte normalizovaný `Vector3` nebo upravte hodnoty tak, aby odrážely požadovaný náklon. |

## Často kladené otázky

### Q1: Mohu používat Aspose.3D i v jiných programovacích jazycích?
A1: Aspose.3D podporuje různé jazyky, včetně .NET a Javy.

### Q2: Je k dispozici bezplatná zkušební verze Aspose.3D?
A2: Ano, funkce Aspose.3D můžete vyzkoušet zdarma [zde](https://releases.aspose.com/).

### Q3: Kde najdu podrobnou dokumentaci k Aspose.3D pro Javu?
A3: Kompletní dokumentace je k dispozici [zde](https://reference.aspose.com/3d/java/).

### Q4: Jak získám podporu pro Aspose.3D?
A4: Navštivte [Aspose.3D fórum](https://forum.aspose.com/c/3d/18) pro jakoukoli pomoc nebo dotazy.

### Q5: Existují dočasné licence pro Aspose.3D?
A5: Ano, dočasnou licenci můžete získat [zde](https://purchase.aspose.com/temporary-license/).

---

**Poslední aktualizace:** 2025-12-18  
**Testováno s:** Aspose.3D 24.11 pro Javu  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}