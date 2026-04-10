---
date: 2026-02-20
description: Naučte se, jak vytvořit 3D scénu a použít lineární extruzi s otáčením
  pomocí Aspose.3D pro Javu. Exportujte soubory OBJ s jednoduchým krok‑za‑krokem návodem.
linktitle: Create 3D Scene with Twist in Linear Extrusion – Aspose.3D for Java
second_title: Aspose.3D Java API
title: Vytvořte 3D scénu s twistem v lineární extruzi – Aspose.3D pro Java
url: /cs/java/linear-extrusion/applying-twist/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Vytvoření 3D scény s otáčením při lineární extruzi – Aspose.3D pro Java

## Úvod

V tomto praktickém **java 3d tutoriálu** se naučíte, jak **vytvořit 3d scénu**, aplikovat *lineární extruzi s otáčením* a nakonec **exportovat obj java** soubory pomocí Aspose.3D pro Java. Ať už vytváříte herní asset, CAD prototyp nebo vizuální efekt, přidání otáčení během extruze dodá vašim modelům dynamický, spirálovitý vzhled, který je obtížné dosáhnout čistou extruzí.

## Rychlé odpovědi
- **Co znamená „twist“ (otáčení) v extruzi?** Otáčí profil postupně podél cesty extruze.  
- **Která knihovna poskytuje funkci otáčení?** Aspose.3D pro Java.  
- **Mohu výsledek exportovat jako OBJ?** Ano – použijte `FileFormat.WAVEFRONTOBJ`.  
- **Potřebuji licenci pro tento tutoriál?** Pro produkční použití je vyžadována dočasná nebo plná licence.  
- **Jaká verze Javy je požadována?** Java 8 nebo vyšší.

## Co je „twist“ (otáčení) v lineární extruzi?

Otáčení je transformace, která otáčí každý řez extrudovaného tvaru o zadaný úhel. Řízením úhlu můžete vytvořit spirály, šrouby nebo jemné torze, které dodají vizuální zajímavost jinak plochým extruzím.

## Proč použít Aspose.3D pro Java?

- **Podpora napříč formáty:** Import a export desítek 3D formátů, včetně OBJ, FBX a STL.  
- **Čisté Java API:** Žádné nativní závislosti, což usnadňuje integraci do libovolného Java projektu.  
- **Vysoce výkonný geometrický engine:** Zvládá složité operace jako otáčení bez ztráty rychlosti.

## Předpoklady

- **Java Development Kit (JDK) 8+** nainstalovaný na vašem počítači.  
- **Aspose.3D pro Java** – stáhněte z [odkaz ke stažení](https://releases.aspose.com/3d/java/).  
- Základní znalost syntaxe Javy a 3‑D konceptů.  
- Přístup k oficiální [dokumentaci Aspose.3D](https://reference.aspose.com/3d/java/) pro referenci.

## Import balíčků

Nejprve přidejte požadované třídy Aspose.3D do svého projektu.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Krok 1: Nastavení adresáře dokumentu

Definujte, kam bude uložen vygenerovaný OBJ soubor. Nahraďte zástupný text skutečnou cestou k adresáři ve vašem systému.

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## Krok 2: Inicializace základního profilu

Vytvořte tvar, který bude extrudován. Zde používáme obdélník s malým poloměrem zaoblení, aby hrany měly měkčí vzhled.

```java
// ExStart:InitializeBaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:InitializeBaseProfile
```

## Krok 3: Vytvoření scény pro hostování uzlů

Objekt `Scene` je kontejner pro všechny 3‑D entity (meshe, světla, kamery atd.).  

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
```

## Krok 4: Přidání levých a pravých uzlů

Vytvoříme dva sourozenecké uzly: jeden bez otáčení (pro srovnání) a druhý s otáčením o 90 stupňů.

```java
// ExStart:CreateNodes
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CreateNodes
```

## Krok 5: Provedení lineární extruze s otáčením

Konstruktor `LinearExtrusion` přijímá profil a délku extruze.  
- `setTwist(0)` → žádná rotace (přímá extruze).  
- `setTwist(90)` → plná rotace o 90 stupňů podél délky.  
Oba uzly používají 100 řezů pro plynulou geometrii.

```java
// ExStart:LinearExtrusionWithTwist
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd:LinearExtrusionWithTwist
```

## Krok 6: Uložení 3D scény jako OBJ

Nakonec zapíšeme scénu do OBJ souboru, aby bylo možné ji zobrazit v libovolném standardním 3‑D prohlížeči.

```java
// ExStart:Save3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:Save3DScene
```

## Časté problémy a tipy

- **Chyby v cestě k souboru:** Ujistěte se, že `MyDir` končí oddělovačem cesty (`/` nebo `\\`) vhodným pro váš OS.  
- **Příliš velký úhel otáčení:** Úhly nad 360° mohou způsobit překrývající se geometrii; držte se rozmezí 0‑360° pro předvídatelné výsledky.  
- **Výkon:** Zvýšení `setSlices` zlepšuje plynulost, ale může zatížit paměť; 100 řezů je dobrá rovnováha pro většinu případů.

## Často kladené otázky (Originální)

### Q1: Mohu použít Aspose.3D pro Java k práci s jinými 3D formáty?

A1: Ano, Aspose.3D podporuje různé 3D formáty, což vám umožní importovat, exportovat a manipulovat s různorodými typy souborů.

### Q2: Kde najdu podporu pro Aspose.3D pro Java?

A2: Navštivte [forum Aspose.3D](https://forum.aspose.com/c/3d/18) pro komunitní podporu a diskuze.

### Q3: Je k dispozici bezplatná zkušební verze Aspose.3D pro Java?

A3: Ano, bezplatnou zkušební verzi získáte [zde](https://releases.aspose.com/).

### Q4: Jak získám dočasnou licenci pro Aspose.3D pro Java?

A4: Dočasnou licenci získáte na [stránce dočasných licencí](https://purchase.aspose.com/temporary-license/).

### Q5: Kde mohu zakoupit Aspose.3D pro Java?

A5: Zakoupit Aspose.3D pro Java můžete na [stránce nákupu](https://purchase.aspose.com/buy).

## Další FAQ (AI‑optimalizované)

**Q: Mohu změnit směr otáčení?**  
A: Ano – použijte záporný úhel v `setTwist()` pro otáčení opačným směrem.

**Q: Je možné aplikovat různé hodnoty otáčení podél extruze?**  
A: Aspose.3D aktuálně aplikuje jednotné otáčení; pro proměnné otáčení byste museli ručně generovat více segmentů.

**Q: Jak zobrazím exportovaný OBJ soubor?**  
A: Jakýkoli standardní 3‑D prohlížeč (např. Blender, MeshLab) dokáže otevřít OBJ soubory.

**Q: Podporuje knihovna mapování textur na otáčených extruzích?**  
A: Ano – po extruzi můžete přiřadit materiály nebo UV souřadnice k meshi uzlu.

## Závěr

Nyní jste **vytvořili 3D scénu**, aplikovali **lineární extruzi s otáčením** a exportovali výsledek jako OBJ soubor pomocí Aspose.3D pro Java. Experimentujte s různými profily, úhly otáčení a počty řezů a vytvořte tak jedinečné geometrie pro hry, simulace nebo 3‑D tisk.

---

**Poslední aktualizace:** 2026-02-20  
**Testováno s:** Aspose.3D pro Java 24.11  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}