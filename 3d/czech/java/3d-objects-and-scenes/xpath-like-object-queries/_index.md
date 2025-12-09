---
date: 2025-11-29
description: Naučte se, jak **vytvořit 3D scénu v Javě** a používat dotazy podobné
  XPath k **výběru objektů podle typu** v Aspose.3D pro Javu.
linktitle: Create 3D Scene Java – Apply XPath‑Like Queries with Aspose.3D
second_title: Aspose.3D Java API
title: Vytvořte 3D scénu v Javě – Použijte dotazy podobné XPath s Aspose.3D
url: /cs/java/3d-objects-and-scenes/xpath-like-object-queries/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Vytvořte 3D scénu v Javě – Použijte dotazy podobné XPath s Aspose.3D

## Úvod  

Pokud potřebujete **vytvořit 3d scénu java** aplikace, které manipulují se složitými hierarchiemi objektů, Aspose.3D pro Java vám poskytuje čistý, styl XPath způsob, jak přesně najít to, co potřebujete. V tomto tutoriálu projdeme vytvořením jednoduché scény, přidáním hierarchie uzlů a následným použitím dotazů podobných XPath k **výběru objektů podle typu** (například kamery nebo světla), ať už jsou kdekoliv ve stromu. Na konci budete pohodlně dotazovat, filtrovat a získávat 3‑D entity pomocí jediné výrazu.

## Rychlé odpovědi
- **Co mohu dotazovat?** Jakýkoli uzel nebo entitu (Camera, Light, Mesh, atd.) ve Scéně.  
- **Jak vybrat objekty podle typu?** Použijte výraz podobný XPath, např. `//*[(@Type='Camera')]`.  
- **Potřebuji licenci pro vývoj?** Pro testování stačí bezplatná zkušební verze; licence je vyžadována pro produkci.  
- **Která verze Javy je podporována?** Java 8 nebo novější.  
- **Kde si mohu stáhnout Aspose.3D?** Na oficiální stránce ke stažení uvedené v předpokladech.

## Předpoklady  

Než začneme, ujistěte se, že máte:

- Nainstalovaný Java Development Kit (JDK).  
- Knihovnu Aspose.3D pro Java staženou a nastavenou. Odkaz ke stažení najdete **[zde](https://releases.aspose.com/3d/java/)**.  
- Základní znalosti programování v Javě.  

## Import balíčků  

Nejprve importujte třídy Aspose.3D, které budete potřebovat. Tento krok zpřístupní knihovnu vašemu projektu.

```java
import com.aspose.threed.*;

import java.util.ArrayList;
import java.util.List;
```

## Co je dotaz podobný XPath v Aspose.3D?  

Aspose.3D implementuje podmnožinu syntaxe XPath, která funguje proti grafu scény. Místo XML uzlů cílí výrazy na instance **A3DObject** (uzly, kamery, světla, meshe atd.). To vám umožní psát výkonné filtry jako „všechny kamery“ nebo „objekty, jejichž název je ‘light’“ bez ručního procházení hierarchie.

## Proč používat dotazy podobné XPath k **výběru objektů podle typu**?  

- **Rychlost:** Jeden řádek nahradí desítky podmínek `if` a smyček.  
- **Čitelnost:** Dotaz čte jako přirozený jazyk.  
- **Flexibilita:** Změňte filtr, aniž byste zasahovali do kódu pro procházení.

## Průvodce krok za krokem  

### Krok 1: Vytvořte scénu pro testování  

Začneme prázdnou scénou, která bude hostit naši hierarchii.

```java
// ExStart:CreateScene
Scene s = new Scene();
// ExEnd:CreateScene
```

### Krok 2: Sestavte hierarchii uzlů  

Dále přidáme několik podřízených uzlů pod kořenový uzel. Některé uzly obsahují entitu **Camera** nebo **Light**, kterou později dotážeme.

```java
// ExStart:CreateHierarchy
Node a = s.getRootNode().createChildNode("a");
a.createChildNode("a1");
a.createChildNode("a2");
s.getRootNode().createChildNode("b");
Node c = s.getRootNode().createChildNode("c");
c.createChildNode("c1").addEntity(new Camera("cam"));
c.createChildNode("c2").addEntity(new Light("light"));
// ExEnd:CreateHierarchy
```

### Krok 3: Použijte dotazy podobné XPath  

Nyní zábavná část – použití řetězců ve stylu XPath k **výběru objektů podle typu** nebo názvu.

```java
// ExStart:XPathLikeObjectQueries
// Select objects that have type Camera or name is 'light' regardless of their location.
List<Object> objects = s.getRootNode().selectObjects("//*[(@Type = 'Camera') or (@Name = 'light')]");

// Select a single camera object under the child nodes of the node named 'c' under the root node
A3DObject c1 = (A3DObject) s.getRootNode().selectSingleObject("/c/*/<Camera>");

// Select the node named 'a1' under the root node, even if 'a1' is not a directly child node
A3DObject obj = (A3DObject) s.getRootNode().selectSingleObject("a1");

// Select the node itself, as '/' is selected directly on the root node
obj = (A3DObject) s.getRootNode().selectSingleObject("/");
// ExEnd:XPathLikeObjectQueries
```

**Vysvětlení klíčových výrazů**

- `//*[(@Type = 'Camera') or (@Name = 'light')]` – Najde každý objekt ve scéně, jehož atribut **type** je `Camera` **nebo** jehož atribut **name** je `light`. Jedná se o klasický příklad **výběru objektů podle typu**.  
- `/c/*/<Camera>` – Začne u kořene, přejde na uzel `c`, pak na libovolné dítě (`*`) a nakonec vybere entitu `<Camera>`.  
- `a1` – Zkratka, která prohledá celý strom a najde uzel pojmenovaný `a1`.  
- `/` – Vrátí samotný kořenový uzel.

### Běžné úskalí a tipy  

- **Rozlišování velikosti písmen:** Názvy atributů (`@Type`, `@Name`) jsou citlivé na velikost písmen.  
- **Entita vs. uzel:** Používejte syntaxi `<Camera>` jen tehdy, když potřebujete podkladovou entitu, nikoli jen uzel.  
- **Výkon:** U velmi velkých scén zúžte vyhledávací cestu (např. začněte od konkrétního podstromu), aby se zvýšila rychlost.

## Závěr  

Nyní víte, jak **vytvořit 3d scénu java** programy, které využívají dotazy podobné XPath k efektivnímu **výběru objektů podle typu**. Tento přístup škáluje od jednoduchých ukázek po produkční 3‑D aplikace, poskytuje jemnozrnné řízení procházení scény bez zbytečného kódu.

## Často kladené otázky  

**Q: Kde najdu dokumentaci k Aspose.3D pro Java?**  
A: Dokumentace je k dispozici **[zde](https://reference.aspose.com/3d/java/)**.

**Q: Jak si mohu stáhnout Aspose.3D pro Java?**  
A: Stáhnout ji můžete **[zde](https://releases.aspose.com/3d/java/)**.

**Q: Je k dispozici bezplatná zkušební verze?**  
A: Ano, bezplatnou zkušební verzi získáte **[zde](https://releases.aspose.com/)**.

**Q: Kde mohu získat podporu pro Aspose.3D pro Java?**  
A: Navštivte fórum podpory **[zde](https://forum.aspose.com/c/3d/18)**.

**Q: Potřebuji dočasnou licenci?**  
A: Dočasnou licenci získáte **[zde](https://purchase.aspose.com/temporary-license/)**.

**Q: Mohu dotazovat vlastní uživatelem definované vlastnosti?**  
A: Ano, můžete rozšířit XPath výraz o další `@` atributy, které přidáte k uzlům.

**Q: Funguje dotazovací engine s animovanými scénami?**  
A: Rozhodně – dotazy pracují na statické hierarchii; animace jsou připojeny ke stejným uzlům a jsou tedy zahrnuty ve výsledcích.

---

**Poslední aktualizace:** 2025-11-29  
**Testováno s:** Aspose.3D pro Java 24.11  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}