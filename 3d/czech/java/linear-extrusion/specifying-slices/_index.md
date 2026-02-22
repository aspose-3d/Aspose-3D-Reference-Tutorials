---
date: 2026-02-22
description: Naučte se, jak vytvořit 3D extruzi s řezy pomocí Aspose.3D pro Javu.
  Tento krok‑za‑krokem průvodce pokrývá lineární extruzi, nastavení poloměru zaoblení
  a export do OBJ.
linktitle: Create 3D Extrusion with Slices – Aspose.3D for Java
second_title: Aspose.3D Java API
title: Vytvořte 3D extruzi pomocí řezů – Aspose.3D pro Javu
url: /cs/java/linear-extrusion/specifying-slices/
weight: 13
---

 produce final content.{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Vytvořte 3D extruzi pomocí řezů – Aspose.3D pro Java

## Úvod

Pokud potřebujete **vytvořit 3d extruzi** objektů, které vypadají hladce a přesně, klíčové je řídit počet řezů. V tomto tutoriálu vás provedeme tím, jak specifikovat řezy při provádění lineární extruze pomocí Aspose.3D pro Java. Uvidíte, proč je počet řezů důležitý, jak nastavit poloměr zaoblení a jak exportovat výsledek jako OBJ soubor, který lze použít v jakémkoli 3D pipeline.

## Rychlé odpovědi
- **Co řídí „slices“?** Počet mezikřížových průřezů používaných k aproximaci povrchu extruze.  
- **Která metoda nastavuje počet řezů?** `LinearExtrusion.setSlices(int)`  
- **Mohu změnit poloměr zaoblení profilu?** Ano, pomocí `RectangleShape.setRoundingRadius(double)`  
- **Jaký formát souboru se v tomto příkladu používá?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **Potřebuji licenci pro spuštění kódu?** Bezplatná zkušební verze stačí pro hodnocení; pro produkční nasazení je vyžadována komerční licence.

## Co je lineární extruze s řezy?

Lineární extruze vezme 2‑D profil (např. obdélník) a protáhne jej podél přímé čáry, čímž vytvoří 3‑D těleso. Zadáním **slices** řeknete Aspose.3D, kolik mezikroků má vygenerovat, což přímo ovlivňuje hladkost zakřivených hran, jako je zaoblený obdélník.

## Proč použít Aspose.3D pro Java k vytvoření 3d extruze?

* **Plná kontrola** – Můžete programově nastavit počet řezů, poloměr zaoblení a formát exportu.  
* **Cross‑platform** – Funguje v jakémkoli prostředí s podporou Javy bez nativních závislostí.  
* **Flexibilita exportu** – Přímé uložení do OBJ, FBX, STL a mnoha dalších formátů.

## Požadavky

1. **Java Development Kit** – Nainstalovaný JDK 8 nebo vyšší.  
2. **Aspose.3D for Java** – Stáhněte knihovnu z oficiálního webu [zde](https://releases.aspose.com/3d/java/).  
3. IDE nebo textový editor dle vašeho výběru.

## Import balíčků

Přidejte jmenný prostor Aspose.3D do svého projektu, abyste měli přístup ke třídám pro 3‑D modelování.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Krok‑za‑krokem průvodce

### Krok 1: Nastavte scénu a definujte profil

Nejprve vytvoříme `RectangleShape` a nastavíme mu **poloměr zaoblení**, aby byly rohy hladké. Poté inicializujeme novou `Scene`, která bude obsahovat veškerou geometrii.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Krok 2: **Vytvořte podřízené uzly** pro každou extruzi

Každý kus geometrie žije pod `Node`. Zde vytvoříme dva sourozenecké uzly – jeden pro extruzi s nízkým počtem řezů a druhý pro extruzi s vysokým počtem řezů – a posuneme levý uzel mírně do strany, aby bylo snadné porovnat výsledky.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Krok 3: Proveďte lineární extruzi a **nastavte řezy**

Nyní skutečně **vytvoříme 3d extruze** objekty. Konstruktor `LinearExtrusion` přijímá profil a hloubku extruze. Pomocí **anonymní vnitřní třídy** zavoláme `setSlices`, abychom řídili hladkost. Levý uzel dostane pouze 2 řezy (hrubý), zatímco pravý uzel dostane 10 řezů (hladký).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Krok 4: **Export OBJ** – uložení scény

Nakonec zapíšeme scénu do souboru Wavefront OBJ, formátu široce podporovaného 3‑D editory a herními enginy. Tím demonstrujeme schopnost **export obj java** v Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Časté problémy a řešení

| Problém | Proč se to děje | Řešení |
|-------|----------------|-----|
| **Extruze vypadá plochá** | Počet řezů nastaven na 1 nebo 0 | Ujistěte se, že `setSlices` je voláno s hodnotou ≥ 2. |
| **Zaoblené rohy vypadají zubatě** | Poloměr zaoblení je příliš malý vzhledem k počtu řezů | Zvyšte buď poloměr, nebo počet řezů pro hladší křivky. |
| **Soubor nebyl při uložení nalezen** | `MyDir` ukazuje na neexistující složku | Vytvořte složku předem nebo použijte absolutní cestu. |

## Často kladené otázky

**Q: Jak si mohu stáhnout Aspose.3D pro Java?**  
A: Knihovnu můžete stáhnout [zde](https://releases.aspose.com/3d/java/).

**Q: Kde najdu dokumentaci k Aspose.3D?**  
A: Dokumentaci najdete [zde](https://reference.aspose.com/3d/java/).

**Q: Je k dispozici bezplatná zkušební verze?**  
A: Ano, můžete si vyzkoušet bezplatnou verzi [zde](https://releases.aspose.com/).

**Q: Jak získám podporu pro Aspose.3D?**  
A: Navštivte fórum podpory [zde](https://forum.aspose.com/c/3d/18).

**Q: Mohu zakoupit dočasnou licenci?**  
A: Ano, dočasnou licenci lze získat [zde](https://purchase.aspose.com/temporary-license/).

---

**Poslední aktualizace:** 2026-02-22  
**Testováno s:** Aspose.3D for Java 24.11 (nejnovější v době psaní)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}