---
date: 2026-02-09
description: Naučte se, jak exportovat FBX a přidat mesh do uzlu při vytváření poduzlů
  v Javě pomocí Aspose.3D.
linktitle: Build Node Hierarchies in 3D Scenes with Java and Aspose.3D
second_title: Aspose.3D Java API
title: Jak exportovat FBX a vytvářet hierarchie uzlů v Javě
url: /cs/java/geometry/build-node-hierarchies/
weight: 16
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak exportovat FBX a vytvořit hierarchie uzlů v Javě s Aspose.3D

## Úvod

Pokud hledáte jasný, krok‑za‑krokem průvodce **how to export FBX** z Java aplikace, jste na správném místě. V tomto tutoriálu vám ukážeme, jak vytvořit hierarchie uzlů, **add mesh to node**, a nakonec uložit scénu jako FBX soubor pomocí Aspose.3D Java API. Ať už vytváříte jednoduchý prototyp nebo produkčně připravený 3D engine, tyto techniky vám poskytnou plnou kontrolu nad vaším grafem scény.

## Rychlé odpovědi
- **What is the primary purpose of this tutorial?** Ukázka, jak exportovat FBX po vytvoření hierarchií uzlů.  
- **Which library is used?** Aspose.3D for Java.  
- **Do I need a license?** Bezplatná zkušební verze funguje pro vývoj; pro produkci je vyžadována komerční licence.  
- **What file format is produced?** FBX (ASCII 7500).  
- **Can I customize node transformations?** Ano – translace, rotace a škálování jsou všechny podporovány.

## Co znamená “how to export FBX” v kontextu Aspose.3D?

Exportování FBX znamená převod grafu scény v paměti, který vytvoříte pomocí Aspose.3D, do FBX souboru, který lze otevřít v populárních 3D nástrojích jako Blender, Maya nebo Unity. API provádí těžkou práci, takže se můžete soustředit na tvorbu scény.

## Proč vytvořit hierarchie uzlů před exportem?

Dobře strukturovaná hierarchie uzlů vám umožní aplikovat transformace jednou na nadřazený uzel, což automaticky ovlivní všechny jeho potomky. To snižuje duplicitní kód a odráží vztahy objektů ve skutečném světě (např. podvozek auta s koly jako podřízenými uzly).

## Požadavky

Než se pustíte do práce, ujistěte se, že máte:

1. **Java Development Environment** – JDK 8+ a IDE nebo nástroj pro sestavení dle vašeho výběru.  
2. **Aspose.3D for Java Library** – Stáhněte a nainstalujte knihovnu ze [download page](https://releases.aspose.com/3d/java/).  
3. **Document Directory** – Složka ve vašem počítači, kam bude uložen vygenerovaný FBX soubor.

## Import balíčků

Začněte importováním potřebných tříd Aspose.3D:

```java
import com.aspose.threed.*;

```

## Krok 1: Inicializace objektu Scene

```java
// Initialize scene object
Scene scene = new Scene();
```

## Krok 2: Vytvoření podřízených uzlů a přidání mesh do uzlu

V tomto kroku ukazujeme **how to create child nodes** a **add mesh to node** objekty.

```java
// Get a child node object
Node top = scene.getRootNode().createChildNode();

// Create the first cube node
Node cube1 = top.createChildNode("cube1");
Mesh mesh = Common.createMeshUsingPolygonBuilder(); // Use your mesh creation method
cube1.setEntity(mesh);
cube1.getTransform().setTranslation(new Vector3(-10, 0, 0));

// Create the second cube node
Node cube2 = top.createChildNode("cube2");
cube2.setEntity(mesh);
cube2.getTransform().setTranslation(new Vector3(10, 0, 0));
```

## Krok 3: Aplikace rotace na horní uzel

Rotace nadřazeného uzlu automaticky otáčí všechny jeho potomky, což je hlavní výhoda hierarchických scén.

```java
// Rotate the top node, affecting all child nodes
top.getTransform().setRotation(Quaternion.fromEulerAngle(Math.PI, 4, 0));
```

## Krok 4: Uložení 3D scény – How to Export FBX

Nyní **save scene as FBX**, dokončujeme workflow “how to export FBX”.

```java
// Save 3D scene in the supported file format (FBX in this case)
String MyDir = "Your Document Directory";
MyDir = MyDir + "NodeHierarchy.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nNode hierarchy added successfully to document.\nFile saved at " + MyDir);
```

### Očekávaný výsledek
Spuštěním kódu se vytvoří soubor s názvem **NodeHierarchy.fbx** ve zvoleném adresáři. Otevřete jej v libovolném FBX‑kompatibilním prohlížeči a uvidíte dva krychle umístěné vlevo a vpravo od centrálního pivotu, všechny rotující společně.

## Časté problémy a řešení

| Problém | Proč k tomu dochází | Řešení |
|-------|----------------|-----|
| **File not found** error when saving | `MyDir` cesta je nesprávná nebo chybí koncový oddělovač | Ujistěte se, že adresář existuje a končí souborovým oddělovačem (`/` nebo `\\`). |
| **Mesh not visible** after export | Entita mesh není přiřazena nebo translace ji posune mimo zorné pole | Ověřte `cube1.setEntity(mesh)` a zkontrolujte hodnoty translace. |
| **Rotation looks wrong** | Nesprávné použití radiánů místo stupňů | `Quaternion.fromEulerAngle` očekává radiány; upravte hodnoty podle toho. |

## Často kladené otázky

**Q: Je Aspose.3D pro Java vhodný pro začátečníky?**  
A: Rozhodně! API je navrženo s čistým, objektově orientovaným přístupem, který usnadňuje učení, i když jste v 3D programování nováčkem.

**Q: Mohu použít Aspose.3D pro Java v komerčních projektech?**  
A: Ano, můžete. Navštivte [purchase page](https://purchase.aspose.com/buy) pro podrobnosti o licencování.

**Q: Jak mohu získat podporu pro Aspose.3D pro Java?**  
A: Připojte se k [Aspose.3D forum](https://forum.aspose.com/c/3d/18) a získejte pomoc od komunity a týmu podpory Aspose.

**Q: Je k dispozici bezplatná zkušební verze?**  
A: Samozřejmě! Vyzkoušejte funkce pomocí [free trial](https://releases.aspose.com/) před závazkem.

**Q: Kde najdu dokumentaci?**  
A: Podívejte se na [documentation](https://reference.aspose.com/3d/java/) pro podrobné informace o Aspose.3D pro Java.

## Závěr

Ovládnutí **how to export FBX**, vytváření hierarchií uzlů a **adding mesh to node** jsou nezbytné kroky k tvorbě sofistikovaných 3D aplikací v Javě. S Aspose.3D získáte výkonné, licencemi přátelské řešení, které abstrahuje nízkoúrovňové detaily a zároveň vám poskytuje plnou kontrolu nad grafem scény. Experimentujte s různými meshemi, transformacemi a exportními formáty a odemkněte tak další možnosti.

---

**Poslední aktualizace:** 2026-02-09  
**Testováno s:** Aspose.3D for Java 24.11  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}