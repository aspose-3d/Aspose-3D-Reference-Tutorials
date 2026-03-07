---
date: 2026-03-07
description: Naučte se, jak vytvořit UV souřadnice a jak generovat UV pro 3D modely
  v Javě pomocí Aspose.3D a exportovat soubor OBJ v Javě v jednoduchém průvodci krok
  za krokem.
linktitle: Generate UV Coordinates for Texture Mapping in Java 3D Models
second_title: Aspose.3D Java API
title: Jak vytvořit UV souřadnice pro 3D modely v Javě
url: /cs/java/polygon/generate-uv-coordinates/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak vytvořit UV souřadnice pro Java 3D modely

## Úvod

Pokud hledáte **how to create uv** souřadnice pro mapování textur v Java 3D modelu, jste na správném místě. V tomto tutoriálu vás provedeme přesnými kroky potřebnými k ručnímu generování UV dat pomocí Aspose.3D, připojení k mesh a nakonec **export OBJ file Java**‑kompatibilní geometrie. Na konci pochopíte, proč je UV mapování důležité, jak jej generovat programově a jak výsledek ověřit v běžném OBJ prohlížeči.

## Rychlé odpovědi
- **What is UV mapping?** Jedná se o proces přiřazování 2‑D texturovacích souřadnic (U & V) k 3‑D vrcholům.  
- **Which library helps you generate UV in Java?** Aspose.3D for Java.  
- **Do I need a license to try this?** K dispozici je bezplatná zkušební verze; licence je vyžadována pro produkční použití.  
- **Can I export the result as OBJ?** Ano – použijte `scene.save(..., FileFormat.WAVEFRONTOBJ)`.  
- **What are the main steps?** Vytvořit scénu, vytvořit mesh, vygenerovat UV, připojit je a uložit.

## Co je UV mapování a proč ho potřebujeme?

UV mapování vám umožňuje obalit 2‑D obrázek (texturu) kolem 3‑D objektu. Bez správných UV souřadnic se textury jeví jako natažené, nesprávně zarovnané nebo úplně chybějící. Ruční generování UV vám dává plnou kontrolu nad tím, jak jsou textury projekovány, což je nezbytné pro hry, simulace a jakoukoli vizuálně bohatou Java aplikaci.

## Předpoklady

- Základní znalost programování v Java.  
- Aspose.3D for Java nainstalováno – můžete jej stáhnout [zde](https://releases.aspose.com/3d/java/).  
- Java IDE (IntelliJ IDEA, Eclipse, VS Code atd.) nastavené s Aspose.3D JAR soubory na classpathu.

## Import balíčků

Ve vašem Java projektu importujte potřebné třídy Aspose.3D. Tyto importy vám poskytují přístup k správě scény, manipulaci s mesh a zpracování vertex elementů.

```java
import com.aspose.threed.Box;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Mesh;
import com.aspose.threed.Node;
import com.aspose.threed.PolygonModifier;
import com.aspose.threed.Scene;
import com.aspose.threed.VertexElement;
import com.aspose.threed.VertexElementType;
```

## Průvodce krok za krokem

### Krok 1: Nastavte cestu k adresáři dokumentu

Definujte, kam bude vygenerovaný OBJ soubor uložen.

```java
String MyDir = "Your Document Directory";
```

> **Pro tip:** Použijte absolutní cestu nebo `System.getProperty("user.dir")`, abyste se vyhnuli překvapením s relativními cestami.

### Krok 2: Vytvořte scénu

`Scene` je kontejner nejvyšší úrovně pro všechny 3‑D objekty.

```java
Scene scene = new Scene();
```

### Krok 3: Vytvořte mesh

Začneme jednoduchým box mesh a úmyslně odstraníme veškerá vestavěná UV data, abychom simulovali mesh, který postrádá texturové souřadnice.

```java
Mesh mesh = (new Box()).toMesh();
mesh.getVertexElements().remove(mesh.getElement(VertexElementType.UV));
```

### Krok 4: Jak ručně generovat UV souřadnice

Aspose.3D poskytuje `PolygonModifier.generateUV`, který vytváří základní rovinné UV rozložení pro libovolný mesh.

```java
VertexElement uv = PolygonModifier.generateUV(mesh);
```

### Krok 5: Připojte UV data k mesh

Nyní připojte vygenerovaný UV element zpět k mesh, aby se stal součástí vertex dat.

```java
mesh.addElement(uv);
```

### Krok 6: Vytvořte uzel a přidejte mesh do scény

`Node` představuje instanci objektu v grafu scény. Přidání mesh do uzlu ho učiní renderovatelným.

```java
Node node = scene.getRootNode().createChildNode(mesh);
```

### Krok 7: Jak exportovat OBJ soubor v Java

Nakonec zapište celou scénu — včetně nově vytvořených UV souřadnic — do OBJ souboru, který lze otevřít prakticky v jakémkoli 3‑D nástroji.

```java
scene.save(MyDir + "test.obj", FileFormat.WAVEFRONTOBJ);
```

> **Co očekávat:** Otevření `test.obj` v prohlížeči jako Blender by mělo zobrazit box s výchozím UV rozložením, připravený pro jakoukoli aplikovanou texturu.

## Časté problémy a řešení

| Problém | Důvod | Řešení |
|-------|--------|-----|
| **UV jsou v prohlížeči chybějící** | Mesh stále obsahuje starý UV element. | Ujistěte se, že jste odstranili původní UV (`mesh.getVertexElements().remove(...)`) před generováním nových. |
| **Chyba: soubor nenalezen** | `MyDir` ukazuje na neexistující složku. | Nejprve vytvořte adresář nebo použijte `new File(MyDir).mkdirs();`. |
| **Výjimka licence** | Spuštění bez platné licence v produkci. | Použijte dočasnou nebo trvalou licenci, jak je popsáno v dokumentaci Aspose. |

## Často kladené otázky

### Q1: Mohu použít Aspose.3D pro Java s jinými programovacími jazyky?

A1: Aspose.3D je primárně navrženo pro Java, ale Aspose také nabízí .NET, C++ a další jazykové vazby. Podívejte se na oficiální dokumentaci pro jazykově specifické API.

### Q2: Je k dispozici zkušební verze Aspose.3D?

A2: Ano, můžete prozkoumat funkce Aspose.3D pomocí bezplatné zkušební verze dostupné [zde](https://releases.aspose.com/).

### Q3: Jak mohu získat podporu pro Aspose.3D?

A3: Navštivte fórum Aspose.3D [zde](https://forum.aspose.com/c/3d/18), kde získáte podporu komunity a můžete se zapojit s ostatními uživateli.

### Q4: Kde najdu komplexní dokumentaci pro Aspose.3D?

A4: Dokumentace je dostupná [zde](https://reference.aspose.com/3d/java/).

### Q5: Mohu zakoupit dočasnou licenci pro Aspose.3D?

A5: Ano, dočasnou licenci můžete získat [zde](https://purchase.aspose.com/temporary-license/).

---

**Poslední aktualizace:** 2026-03-07  
**Testováno s:** Aspose.3D for Java 24.11 (nejnovější v době psaní)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}