---
date: 2026-02-20
description: Naučte se tutoriál Java 3D grafiky o řízení středu při lineárním extrudování
  s Aspose.3D, včetně toho, jak nastavit poloměr zaoblení a uložit soubor OBJ v Javě.
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Java 3D grafika – Střed v lineární extruzi
url: /cs/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java 3D Grafický tutoriál – Střed v lineární extruzi

## Úvod

Pokud vytváříte 3D vizualizace v Javě, zvládnutí technik extruze je nezbytné. Tento **java 3d graphics tutorial** vás provede řízením středu lineární extruze pomocí Aspose.3D pro Java, takže můžete vytvářet přesné, symetrické modely bez další matematiky. Na konci tohoto průvodce pochopíte, proč je důležitá vlastnost `center`, jak **set rounding radius**, a jak **save OBJ file java**‑compatible output.

## Rychlé odpovědi
- **Co dělá vlastnost center?** Určuje, zda je extruze symetrická kolem počátku profilu.  
- **Potřebuji licenci pro spuštění kódu?** Dočasná licence funguje pro testování; pro produkci je vyžadována plná licence.  
- **Jaký formát souboru se používá pro výsledek?** Scéna je uložena jako soubor Wavefront OBJ.  
- **Mohu změnit počet řezů?** Ano, použijte `setSlices(int)` na objektu `LinearExtrusion`.  
- **Je Aspose.3D kompatibilní s Java 8+?** Naprosto – podporuje všechny moderní verze Javy.

## Co je java 3d graphics tutorial?

**java 3d graphics tutorial** vysvětluje krok za krokem, jak používat Java knihovny k vytváření, manipulaci a renderování trojrozměrných objektů. V tomto případě se zaměřujeme na extrusion API Aspose.3D, které převádí 2‑D profily na plnohodnotné 3‑D sítě.

## Proč použít Aspose.3D pro Java?

- **High‑level API** – Není nutné psát nízkoúrovňové výpočty sítí.  
- **Cross‑format support** – Export do OBJ, FBX, STL a dalších.  
- **Performance‑optimized** – Efektivně zpracovává velké scény.  
- **Rich documentation** – Obsahuje příklady jako ten níže.

## Požadavky

1. **Java Development Environment** – Nainstalovaný JDK 8 nebo novější.  
2. **Aspose.3D for Java** – Stáhněte knihovnu a dokumentaci [zde](https://reference.aspose.com/3d/java/).  
3. **Document Directory** – Vytvořte složku ve svém počítači pro ukládání generovaných souborů; budeme na ni odkazovat jako **„Your Document Directory.“**

## Import balíčků

Ve svém Java IDE importujte třídy Aspose.3D, které budete potřebovat. To poskytne kompilátoru přístup k funkcím extruze a tvorby scény.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Postupný průvodce

### Krok 1: Nastavte základní profil

Nejprve vytvořte 2‑D tvar, který bude extrudován. Zde použijeme obdélník a **set rounding radius** na 0,3, což zaoblí rohy.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### Krok 2: Vytvořte 3D scénu

Objekt `Scene` funguje jako kontejner pro všechny 3‑D uzly, světla a kamery.

```java
Scene scene = new Scene();
```

### Krok 3: Přidejte levý a pravý uzel

Umístíme dva samostatné uzly vedle sebe, abyste mohli porovnat extruzi se středem a bez něj.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Krok 4: Lineární extruze – Bez středu (levý uzel)

Vytvořte extruzi na levém uzlu, vypněte centrování a omezte síť na tři řezy pro low‑poly náhled.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

### Krok 5: Přidejte podkladovou rovinu pro referenci (levý uzel)

Tenký kvádr slouží jako vizuální podlaha, která vám pomůže vidět orientaci extruze.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

### Krok 6: Lineární extruze – Centrovaná (pravý uzel)

Nyní opakujte extruzi, tentokrát povolíte `center`. Geometrie bude symetrická kolem počátku profilu.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

### Krok 7: Přidejte podkladovou rovinu pro referenci (pravý uzel)

Stejná podkladová rovina pro pravou stranu, aby byl srovnání jasné.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

### Krok 8: Uložte 3D scénu

Nakonec exportujte celou scénu do souboru Wavefront OBJ – formátu, který lze snadno použít ve většině 3‑D editorů.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Časté problémy a řešení

| Problém | Proč se to děje | Řešení |
|---------|----------------|--------|
| **Extruze se zdá posunutá** | `setCenter(false)` ponechá profil ukotvený v jeho rohu. | Použijte `setCenter(true)` pro symetrické výsledky. |
| **Soubor OBJ je prázdný** | Cesta k výstupnímu adresáři je nesprávná nebo chybí oprávnění k zápisu. | Ověřte, že `MyDir` ukazuje na existující složku a aplikace má právo zápisu. |
| **Zaoblené rohy vypadají ostré** | Poloměr zaoblení je příliš malý vzhledem k velikosti obdélníku. | Zvyšte hodnotu poloměru (např. `setRoundingRadius(0.5)`). |

## Často kladené otázky

### Q1: Mohu používat Aspose.3D pro Java v komerčních projektech?

A1: Ano, Aspose.3D pro Java je k dispozici pro komerční použití. Pro podrobnosti o licencování navštivte [zde](https://purchase.aspose.com/buy).

### Q2: Je k dispozici bezplatná zkušební verze?

A2: Ano, můžete si vyzkoušet bezplatnou zkušební verzi Aspose.3D pro Java [zde](https://releases.aspose.com/).

### Q3: Kde mohu najít podporu pro Aspose.3D pro Java?

A3: Fórum komunity Aspose.3D je skvělé místo, kde získat podporu a sdílet své zkušenosti. Navštivte fórum [zde](https://forum.aspose.com/c/3d/18).

### Q4: Potřebuji dočasnou licenci pro testování?

A4: Ano, pokud potřebujete dočasnou licenci pro testovací účely, můžete ji získat [zde](https://purchase.aspose.com/temporary-license/).

### Q5: Kde mohu najít dokumentaci?

A5: Dokumentace pro Aspose.3D pro Java je k dispozici [zde](https://reference.aspose.com/3d/java/).

## Závěr

Po dokončení tohoto **java 3d graphics tutorial** nyní víte, jak řídit střed lineární extruze, upravit poloměr zaoblení a **save OBJ file java** výstup pomocí Aspose.3D. Tyto techniky vám poskytují detailní kontrolu nad symetrií sítě, což je zásadní pro herní assety, CAD prototypy a vědecké vizualizace. Neváhejte experimentovat s různými profily, počty řezů a exportními formáty a rozšířit tak svou 3‑D toolbox.

---

**Poslední aktualizace:** 2026-02-20  
**Testováno s:** Aspose.3D for Java 24.11  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}