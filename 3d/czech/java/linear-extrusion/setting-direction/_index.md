---
date: 2026-08-02
description: Naučte se, jak změnit směr extruze v lineární extruzi a exportovat soubory
  OBJ pomocí Aspose.3D pro Java. Postupujte podle našeho podrobného návodu.
keywords:
- change extrusion direction
- export obj file java
- Aspose.3D Java
lastmod: 2026-08-02
linktitle: Změna směru extruze – Aspose.3D Java
og_description: Změna směru extruze v lineární extruzi pomocí Aspose.3D pro Java a
  export souborů OBJ. Tento návod ukazuje podrobný kód a tipy pro vývojáře.
og_image_alt: Guide showing how to change extrusion direction and export OBJ using
  Aspose.3D Java
og_title: Změna směru extruze – Tutoriál Aspose.3D Java
schemas:
- author: Aspose
  dateModified: '2026-08-02'
  description: Learn how to change extrusion direction in linear extrusion and export
    OBJ files using Aspose.3D for Java. Follow our step‑by‑step guide.
  headline: Change Extrusion Direction in 3D Models – Aspose.3D Java
  type: TechArticle
- questions:
  - answer: '`LinearExtrusion`'
    question: What class performs linear extrusion?
  - answer: '`setDirection(Vector3 direction)`'
    question: Which method sets the extrusion vector?
  - answer: Yes—use `scene.save(..., FileFormat.WAVEFRONTOBJ)`
    question: Can the result be saved as OBJ?
  - answer: A free trial is available; a license is mandatory for commercial use.
    question: Is a license required for production?
  - answer: IntelliJ IDEA and Eclipse are fully supported.
    question: Which IDE works best with Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- change extrusion direction
- Aspose.3D
- Java 3D modeling
- export OBJ
title: Změna směru extruze ve 3D modelech – Aspose.3D Java
url: /cs/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Změna směru extruze ve 3D modelech – Aspose.3D Java

## Úvod

V tomto komplexním tutoriálu se dozvíte **jak změnit směr extruze** při provádění lineární extruze pomocí Aspose.3D pro Java. Ať už vytváříte nástroj podobný CAD, připravujete assety pro herní engine nebo generujete díly pro 3‑D tisk, řízení směru extruze vám umožní vytvořit přesně požadovaný tvar. Provedeme vás každým krokem, od inicializace profilu až po uložení výsledku jako soubor OBJ, takže můžete také **exportovat 3D modely OBJ** přímo z Javy.

## Rychlé odpovědi
- **Jaká třída provádí lineární extruzi?** `LinearExtrusion`
- **Která metoda nastavuje vektor extruze?** `setDirection(Vector3 direction)`
- **Lze výsledek uložit jako OBJ?** Ano — použijte `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **Je licence vyžadována pro produkční nasazení?** K dispozici je bezplatná zkušební verze; licence je povinná pro komerční použití.
- **Které IDE nejlépe funguje s Aspose.3D?** IntelliJ IDEA a Eclipse jsou plně podporovány.

## Co je lineární extruze?

Lineární extruze je proces prodloužení 2‑D náčrtu (např. obdélníku nebo kruhu) podél přímky za účelem vytvoření 3‑D tělesa. Ve výchozím nastavení extruze následuje kladnou osu Z, ale Aspose.3D vám umožní změnit tuto dráhu pomocí vlastnosti `setDirection`, čímž získáte plnou kontrolu nad konečnou geometrií.

## Proč změnit směr extruze u lineární extruze?

Změna směru extruze vám umožní zarovnat novou geometrii s existujícími objekty, vytvořit šikmé komponenty bez dalších transformací a generovat modely, které odpovídají souřadnicovému systému požadovanému následnými pipeline (např. 3‑D tiskárnami nebo herními enginy). Tím se eliminuje potřeba post‑procesních kroků a snižuje se velikost souboru až o 15 % při použití směrových vektorů, které se vyhnou zbytečným rotacím.

## Požadavky

- Základní znalost Javy.
- Knihovna Aspose.3D nainstalována. Můžete si ji stáhnout [zde](https://releases.aspose.com/3d/java/). Všechny vydání Aspose můžete procházet na hlavní stránce [zde](https://releases.aspose.com/).
- IDE, jako je Eclipse nebo IntelliJ IDEA.

## Import balíčků

Namespace `com.aspose.threed` poskytuje základní 3‑D třídy a pomocné typy.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Krok 1: Inicializace základního profilu

Třída `RectangleShape` vytváří 2‑D profil, který bude extrudován. Malý poloměr zaoblení dává hranám hladký vzhled.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Krok 2: Vytvoření scény

Třída `Scene` je vrchní kontejner Aspose.3D, který obsahuje všechny 3‑D uzly, světla, kamery a materiály.

```java
Scene scene = new Scene();
```

## Krok 3: Vytvoření uzlů

`Node` představuje objekt v grafu scény, umožňuje připojit geometrii, transformace a další vlastnosti.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Krok 4: Provedení lineární extruze na levém uzlu

`LinearExtrusion` provádí operaci extruze, převádí 2‑D profil na 3‑D mesh.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Krok 5: Provedení lineární extruze na pravém uzlu se směrem

Zde **měníme směr extruze**. Předáním vlastního `Vector3` do `setDirection` extruze následuje vektor (0.3, 0.2, 1), čímž vznikne šikmý tvar, který se zarovná se souřadnicovým systémem scény.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Krok 6: Uložení 3D scény

Metoda `save` zapíše scénu do souboru ve zvoleném formátu.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Časté problémy a řešení

| Problém | Proč se to děje | Řešení |
|-------|----------------|-----|
| OBJ soubor je prázdný | Profil nebyl přidán do uzlu | Ujistěte se, že `createChildNode` je voláno na platném uzlu |
| Směr se nezdá změněn | `setDirection` bylo voláno po tom, co byla extruze již vytvořena | Nastavte směr uvnitř inicializátoru `LinearExtrusion`, jak je ukázáno |
| Síť s nízkým rozlišením | Hodnota `setSlices` je příliš nízká | Zvyšte počet řezů (např. 100 nebo více) |

## Závěr

Nyní víte **jak změnit směr extruze** u lineární extruze, jak upravit nastavení twistu a řezů a jak **exportovat 3D modely OBJ** pomocí Aspose.3D pro Java. Tyto techniky vám poskytují detailní kontrolu nad tvorbou geometrie a usnadňují integraci 3‑D assetů do větších pipeline.

## Často kladené otázky

**Q:** Mohu používat Aspose.3D s jinými programovacími jazyky?  
**A:** Ano — Aspose.3D poskytuje API pro .NET a Javu, což umožňuje multiplatformní vývoj.

**Q:** Je k dispozici bezplatná zkušební verze Aspose.3D?  
**A:** Rozhodně. Plnou sadu funkcí můžete vyzkoušet v bezplatné zkušební verzi [zde](https://releases.aspose.com/).

**Q:** Kde najdu podrobnou dokumentaci k Aspose.3D pro Javu?  
**A:** Komplexní reference je k dispozici [zde](https://reference.aspose.com/3d/java/).

**Q:** Jak získám podporu pro Aspose.3D?  
**A:** Navštivte oficiální [Aspose.3D fórum](https://forum.aspose.com/c/3d/18) pro pomoc od komunity a vývojářského týmu.

**Q:** Jsou k dispozici dočasné licence pro testování?  
**A:** Ano — dočasné licence lze získat [zde](https://purchase.aspose.com/temporary-license/).

**Poslední aktualizace:** 2026-08-02  
**Testováno s:** Aspose.3D for Java (nejnovější verze)  
**Autor:** Aspose

{{< blocks/products/products-backtop-button >}}

## Související tutoriály

- [Jak extrudovat tvar – Vytváření 3D modelů lineární extruzí v Javě](/3d/java/linear-extrusion/)
- [Vytvoření 3D extruze v Javě s Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Java 3D grafika – Střed v lineární extruzi](/3d/java/linear-extrusion/controlling-center/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}