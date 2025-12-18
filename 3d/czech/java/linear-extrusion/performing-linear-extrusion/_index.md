---
date: 2025-12-18
description: Naučte se, jak v Javě pomocí Aspose.3D extrudovat tvar, vytvořit 3D scénu
  a snadno exportovat soubory Wavefront OBJ.
linktitle: How to Extrude Shape in Java with Aspose.3D Linear Extrusion
second_title: Aspose.3D Java API
title: Jak extrudovat tvar v Javě s lineární extruzí Aspose.3D
url: /cs/java/linear-extrusion/performing-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Provádění lineární extruze v Aspose.3D pro Java

## Úvod

Vítejte v tomto komplexním tutoriálu o **how to extrude shape** v Aspose.3D pro Java! Pokud chcete zlepšit své dovednosti v 3D modelování pomocí Javy, jste na správném místě. Provedeme vás tvorbou 3D scény, provedením lineární extruze a exportem výsledku jako souboru Wavefront OBJ – vše s jasnými, krok za krokem ukázkami kódu.

## Rychlé odpovědi
- **What is linear extrusion?** Rozšíření 2D profilu podél přímé dráhy k vytvoření 3D tělesa.  
- **Which library handles this in Java?** Aspose.3D for Java.  
- **Can I export to OBJ?** Ano, pomocí funkce exportu Wavefront OBJ.  
- **Do I need a license for development?** Bezplatná zkušební verze stačí pro testování; licence je vyžadována pro produkci.  
- **What Java version is required?** Java 1.6 nebo novější.

## Co je “how to extrude shape”?
Lineární extruze je základní technika v **3d modeling java**, která převádí plochý profil – například obdélník – na objemový objekt tažením podél definované vzdálenosti. Tato metoda se široce používá pro tvorbu mechanických součástí, architektonických prvků a dekorativních modelů.

## Proč použít Aspose.3D pro lineární extruzi?
- **Full control** nad geometrií (řezy, otáčení, posun).  
- **Seamless integration** s Java projekty – bez nativních závislostí.  
- **Built‑in exporters** pro oblíbené formáty, včetně Wavefront OBJ, což usnadňuje **generate 3d model** soubory pro následné zpracování.

## Předpoklady

Než se pustíte do tutoriálu, ujistěte se, že máte následující předpoklady:

1. **Java Development Environment** – JDK (1.6 nebo novější) a vaše oblíbené IDE.  
2. **Aspose.3D Library** – stáhněte a nainstalujte knihovnu z oficiálního webu **[here](https://releases.aspose.com/3d/java/)**.

## Import balíčků

Jakmile máte nastavené vývojové prostředí a nainstalovanou knihovnu Aspose.3D, importujte potřebný balíček:

```java
import com.aspose.threed.*;
```

### Krok 1: Nastavení adresáře dokumentu

Definujte složku, kam budou ukládány vygenerované soubory:

```java
String MyDir = "Your Document Directory";
```

> Tím se zajistí, že operace **generate 3d model** zapíše OBJ soubor na známé místo.

### Krok 2: Inicializace základního tvaru

Vytvořte obdélník, který bude sloužit jako profil extruze:

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

Můžete upravit poloměr zaoblení pro získání zaoblených rohů nebo nastavit `0` pro dokonalý obdélník.

### Krok 3: Provedení lineární extruze

Nyní extrahujeme obdélník podél osy Z, přidáme řezy, povolíme centrování a aplikujeme otáčení s posunem:

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

- **Extrusion length** – `10` jednotek.  
- **Slices** – `100` pro hladkou geometrii.  
- **Twist** – `360°` vytváří plnou rotaci.  
- **Twist offset** – posouvá počátek otáčení na `(10, 0, 0)`.

### Krok 4: Vytvoření 3D scény

Vytvořte kontejner scény a přidejte extruzi jako podřízený uzel. Tento krok **creates 3d scene**, který může obsahovat více objektů:

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

### Krok 5: Uložení 3D scény

Exportujte scénu do souboru Wavefront OBJ. Toto demonstruje schopnosti **wavefront obj export** a **save 3d obj**:

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Po spuštění kódu najdete `LinearExtrusion.obj` ve složce, kterou jste určili, připravený k otevření v libovolném 3D prohlížeči nebo dalšímu zpracování.

## Časté problémy a řešení

| Problém | Důvod | Řešení |
|-------|--------|-----|
| Soubor OBJ je prázdný | Cesta k výstupnímu adresáři je nesprávná nebo není zapisovatelná | Ověřte, že `MyDir` ukazuje na existující složku s oprávněním k zápisu. |
| Otáčení nebylo aplikováno | `setCenter(true)` vynecháno | Zajistěte, aby bylo centrování povoleno, nebo upravte hodnoty `setTwistOffset`. |
| Chyba kompilace u `LinearExtrusion` | Používáte starší verzi Aspose.3D | Aktualizujte na nejnovější verzi Aspose.3D. |

## Často kladené otázky

**Q: Je Aspose.3D kompatibilní se všemi verzemi Javy?**  
A: Aspose.3D funguje s Java 1.6 a novější.

**Q: Mohu použít Aspose.3D pro komerční projekty?**  
A: Ano, komerční použití je povoleno s platnou licencí. Licenci můžete získat **[here](https://purchase.aspose.com/buy)**.

**Q: Kde mohu získat podporu, pokud narazím na problémy?**  
A: Navštivte **[Aspose.3D forum](https://forum.aspose.com/c/3d/18)** pro komunitní pomoc nebo zakupte **[temporary license](https://purchase.aspose.com/temporary-license/)** pro prémiovou podporu.

**Q: Jaké další funkce 3D modelování poskytuje Aspose.3D?**  
A: Knihovna zahrnuje manipulaci s meshem, Boolean operace, mapování textur a další. Kompletní seznam najdete **[here](https://reference.aspose.com/3d/java/)**.

**Q: Je k dispozici bezplatná zkušební verze?**  
A: Ano, můžete si stáhnout zkušební verzi **[here](https://releases.aspose.com/)**.

## Závěr

Nyní jste se naučili **how to extrude shape** pomocí Aspose.3D pro Java, vytvořili 3D scénu a exportovali výsledek jako soubor Wavefront OBJ. Tato technika otevírá dveře k široké škále projektů **3d modeling java** – od jednoduchých součástí po složité sestavy. Prozkoumejte další funkce, jako jsou Boolean operace nebo mapování textur, a dále obohacujte své modely.

---

**Poslední aktualizace:** 2025-12-18  
**Testováno s:** Aspose.3D 24.11 for Java  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

## TARGET KEYWORDS:

**Primary Keyword (HIGHEST PRIORITY):**
how to extrude shape

**Secondary Keywords (SUPPORTING):**
create 3d scene, 3d modeling java, generate 3d model, wavefront obj export, save 3d obj