---
date: 2026-02-22
description: Naučte se nastavit směr lineární extruze a exportovat 3D model ve formátu
  OBJ pomocí Aspose.3D pro Javu. Postupujte podle našeho krok‑za‑krokem průvodce.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Jak nastavit směr lineární extruze pomocí Aspose.3D pro Javu
url: /cs/java/linear-extrusion/setting-direction/
weight: 12
---

Author". Keep dates unchanged.

Thus:

**Poslední aktualizace:** 2026-02-22  
**Testováno s:** Aspose.3D for Java (latest release)  
**Autor:** Aspose

Now produce final content.

Check for any missed text: "step-by-step" etc. Already covered.

Make sure to keep markdown formatting.

Now craft final answer.{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak nastavit směr při lineární extruzi pomocí Aspose.3D pro Java

## Úvod

V tomto komplexním tutoriálu se dozvíte **jak nastavit směr** při provádění lineární extruze pomocí Aspose.3D pro Java. Ať už vytváříte nástroj podobný CAD nebo generujete geometrii pro herní engine, řízení směru extruze vám umožní vytvořit přesně ten tvar, který potřebujete. Provedeme vás každým krokem, od inicializace profilu až po uložení výsledku jako soubor OBJ, takže můžete také **exportovat 3d model obj** soubory přímo z Javy.

## Rychlé odpovědi
- **Jaká je hlavní třída pro lineární extruzi?** `LinearExtrusion`
- **Která metoda definuje směr extruze?** `setDirection(Vector3 direction)`
- **Mohu výsledek exportovat jako OBJ?** Ano, pomocí `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **Potřebuji licenci pro vývoj?** K dispozici je bezplatná zkušební verze; licence je vyžadována pro produkční nasazení.
- **Jaké IDE pro Java je nejlepší?** IntelliJ IDEA nebo Eclipse jsou plně podporovány.

## Co je lineární extruze?

Lineární extruze vezme 2‑D profil (například obdélník nebo kruh) a prodlouží jej podél přímky, čímž vytvoří 3‑D těleso. Ve výchozím nastavení extruze následuje kladnou osu Z, ale Aspose.3D vám umožní změnit tuto dráhu pomocí vlastnosti `setDirection`.

## Proč nastavit směr při lineární extruzi?

Nastavení vlastního směru je užitečné, když:
- Zarovnáváte geometrii s existujícími objekty ve scéně.
- Vytváříte šikmé nebo nakloněné díly bez dalších transformačních kroků.
- Exportujete modely, které musí odpovídat konkrétnímu souřadnicovému systému (např. pro 3‑D tisk nebo herní enginy).

## Požadavky

Než začneme, ujistěte se, že máte:

- Základní znalosti Javy.
- Nainstalovanou knihovnu Aspose.3D. Stáhnout ji můžete [zde](https://releases.aspose.com/3d/java/).
- IDE jako Eclipse nebo IntelliJ IDEA.

## Import balíčků

Nejprve importujte jmenné prostory, které poskytují základní 3‑D třídy a pomocné typy.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Krok 1: Inicializace základního profilu

Vytvořte tvar, který bude extrudován. V tomto příkladu používáme `RectangleShape` s malým poloměrem zaoblení, aby byly hrany hladké.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Krok 2: Vytvoření scény

Objekt `Scene` funguje jako kontejner pro všechny 3‑D uzly, světla, kamery a materiály.

```java
Scene scene = new Scene();
```

## Krok 3: Vytvoření uzlů

Přidejte dva podřízené uzly ke kořeni scény — jeden pro extruzi vlevo a jeden pro extruzi vpravo. Pravý uzel je posunut, aby se objekty nepřekrývaly.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Krok 4: Provedení lineární extruze na levém uzlu

Extrudujte profil na levém uzlu pomocí výchozího směru podél osy Z. Přidáme také plný 360° otáčení a zvýšíme počet řezů pro hladší síť.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Krok 5: Provedení lineární extruze na pravém uzlu se směrem

Zde **nastavíme směr**. Předáním vlastního `Vector3` do `setDirection` extruze následuje vektor (0.3, 0.2, 1), čímž vznikne šikmý tvar.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Krok 6: Uložení 3D scény

Nakonec exportujte scénu do formátu Wavefront OBJ. Tento krok ukazuje, jak **save obj file java** projekty a usnadňuje zobrazení výsledku v libovolném 3‑D prohlížeči.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Časté problémy a řešení

| Problém | Proč se to stane | Řešení |
|---------|------------------|--------|
| Soubor OBJ je prázdný | Profil nebyl přidán do uzlu | Ujistěte se, že `createChildNode` je voláno na platném uzlu |
| Směr se nezdá změněn | `setDirection` byl zavolán po vytvoření extruze | Nastavte směr uvnitř inicializátoru `LinearExtrusion`, jak je ukázáno |
| Síť má nízké rozlišení | Hodnota `setSlices` je příliš nízká | Zvyšte počet řezů (např. 100 nebo více) |

## Závěr

Nyní víte **jak nastavit směr** při lineární extruzi, jak upravit nastavení otáčení a řezů a jak **exportovat 3d model obj** soubory pomocí Aspose.3D pro Java. Tyto techniky vám poskytují detailní kontrolu nad tvorbou geometrie a usnadňují integraci 3‑D aktiv do širších pipeline.

## Často kladené otázky

### Q1: Mohu použít Aspose.3D s jinými programovacími jazyky?

A1: Aspose.3D podporuje různé programovací jazyky, včetně .NET a Javy.

### Q2: Je k dispozici bezplatná zkušební verze pro Aspose.3D?

A2: Ano, funkce Aspose.3D můžete vyzkoušet zdarma [zde](https://releases.aspose.com/).

### Q3: Kde najdu podrobnou dokumentaci pro Aspose.3D pro Java?

A3: Kompletní dokumentace je dostupná [zde](https://reference.aspose.com/3d/java/).

### Q4: Jak mohu získat podporu pro Aspose.3D?

A4: Navštivte [Aspose.3D fórum](https://forum.aspose.com/c/3d/18) pro jakoukoli pomoc nebo dotazy.

### Q5: Jsou k dispozici dočasné licence pro Aspose.3D?

A5: Ano, dočasnou licenci můžete získat [zde](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Poslední aktualizace:** 2026-02-22  
**Testováno s:** Aspose.3D for Java (latest release)  
**Autor:** Aspose