---
date: 2026-04-12
description: Naučte se, jak vytvářet podřízené uzly, přidávat mesh k uzlu a exportovat
  FBX pomocí Aspose.3D Java API pro robustní 3D scénové grafy.
keywords:
- create child nodes
- how to export fbx
- add mesh to node
- java 3d scene graph
- save scene fbx
linktitle: Vytvořte hierarchie uzlů ve 3D scénách pomocí Javy a Aspose.3D
second_title: Aspose.3D Java API
title: Create Child Nodes and Export FBX in Java with Aspose.3D
url: /cs/java/geometry/build-node-hierarchies/
weight: 16
---

{{< blocks/products/pf/main-wrap-class >}}  
{{< blocks/products/pf/main-container >}}  
{{< blocks/products/pf/tutorial-page-section >}}  

# Jak exportovat FBX a vytvořit hierarchie uzlů v Javě s Aspose.3D  

## Úvod  

Pokud hledáte jasný, krok‑za‑krokem průvodce k **create child nodes**, **add mesh to node** a **how to export FBX** z Java aplikace, jste na správném místě. V tomto tutoriálu vás provedeme tvorbou **java 3d scene graph**, připojováním meshů, aplikací transformací a nakonec uložením scény jako souboru FBX pomocí Aspose.3D Java API. Ať už prototypujete jednoduchou ukázku nebo vyvíjíte produkčně připravený 3D engine, zvládnutí těchto konceptů vám poskytne plnou kontrolu nad hierarchií scény a exportním workflow.  

## Rychlé odpovědi  

- **Jaký je hlavní účel tohoto tutoriálu?** Demonstrace, jak **create child nodes**, připojit mesh a **export FBX** po vytvoření hierarchie uzlů.  
- **Která knihovna je použita?** Aspose.3D for Java.  
- **Potřebuji licenci?** Bezplatná zkušební verze funguje pro vývoj; pro produkci je vyžadována komerční licence.  
- **Jaký formát souboru je vytvořen?** FBX (ASCII 7500).  
- **Mohu přizpůsobit transformace uzlů?** Ano – translace, rotace a škálování jsou všechny podporovány.  

## Co znamená „create child nodes“ v kontextu Aspose.3D?  

Vytváření podřízených uzlů znamená přidání podřízených objektů `Node` k nadřazenému uzlu ve scénovém grafu. Tato hierarchická struktura vám umožní aplikovat transformaci jednou na úrovni rodiče a nechat ji automaticky ovlivnit všechny jeho potomky, což je nezbytné pro realistické vztahy objektů, například podvozek auta s otáčejícími se koly.  

## Proč vytvářet hierarchie uzlů před exportem?  

Dobře strukturovaná hierarchie snižuje duplicitní kód, zjednodušuje animaci a odráží vztahy ze skutečného světa. Když později **convert scene fbx** (nebo jakýkoli jiný formát), hierarchie je zachována, takže nástroje jako Blender, Maya nebo Unity přesně rozumí vztahům rodič‑potomek tak, jak jste je navrhli.  

## Běžné případy použití hierarchií uzlů  

| Případ použití | Proč hierarchie pomáhá | Typický výsledek |
|----------------|-----------------------|------------------|
| **Mechanické sestavy** (např. robotické rameno) | Otáčením základního uzlu se pohybují všechny připojené segmenty | Jednoduchá animace složitých mechanismů |
| **Rigy postav** | Kosti skeletu jsou podřízené uzly kořene | Konzistentní transformace póz |
| **Organizace scény** | Seskupení statických objektů pod uzlem „props“ | Čistší správa scény a selektivní export |
| **Přepínání úrovně detailu (LOD)** | Rodičovský uzel přepíná viditelnost podřízených meshů | Optimalizované renderování pro různé hardware |

## Požadavky  

1. **Java Development Environment** – JDK 8+ a IDE nebo nástroj pro sestavení dle vašeho výběru.  
2. **Aspose.3D for Java Library** – Stáhněte a nainstalujte knihovnu ze [download page](https://releases.aspose.com/3d/java/).  
3. **Document Directory** – Složka ve vašem počítači, kam bude uložen vygenerovaný soubor FBX.  

## Import balíčků  

Begin by importing the necessary Aspose.3D classes:  

```java
import com.aspose.threed.*;
```  

## Krok 1: Inicializace objektu Scene  

```java
// Initialize scene object
Scene scene = new Scene();
```  

## Krok 2: Vytvoření podřízených uzlů a přidání mesh do uzlu  

V tomto kroku demonstrujeme **how to create child nodes** a **add mesh to node** objekty.  

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

Otáčením rodičovského uzlu se automaticky otáčejí všechny jeho podřízené uzly, což je hlavní výhoda hierarchických scén.  

```java
// Rotate the top node, affecting all child nodes
top.getTransform().setRotation(Quaternion.fromEulerAngle(Math.PI, 4, 0));
```  

## Krok 4: Uložení 3D scény – Jak exportovat FBX  

Nyní **uložíme scénu jako FBX**, čímž dokončujeme workflow „how to export fbx“.  

```java
// Save 3D scene in the supported file format (FBX in this case)
String MyDir = "Your Document Directory";
MyDir = MyDir + "NodeHierarchy.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nNode hierarchy added successfully to document.\nFile saved at " + MyDir);
```  

### Očekávaný výsledek  

Spuštěním kódu se vytvoří soubor s názvem **NodeHierarchy.fbx** ve zadaném adresáři. Otevřete jej v libovolném prohlížeči kompatibilním s FBX a uvidíte dva krychle umístěné vlevo a vpravo od centrálního pivotu, všechny se otáčejí společně.  

## Běžné problémy a řešení  

| Problém | Proč k tomu dochází | Řešení |
|---------|---------------------|--------|
| **File not found** chyba při ukládání | `MyDir` cesta je nesprávná nebo chybí koncový oddělovač | Ujistěte se, že adresář existuje a končí souborovým oddělovačem (`/` nebo `\\`). |
| **Mesh not visible** po exportu | Entita mesh není přiřazena nebo translace ji posune mimo zorné pole | Ověřte `cube1.setEntity(mesh)` a zkontrolujte hodnoty translace. |
| **Rotation looks wrong** | Nesprávné použití radiánů místo stupňů | `Quaternion.fromEulerAngle` očekává radiány; upravte hodnoty podle toho. |

## Tipy pro řešení problémů  

- **Validate the directory**: Použijte `new File(MyDir).mkdirs();` před `scene.save`, pokud adresář nemusí existovat.  
- **Inspect the scene graph**: Zavolejte `scene.getRootNode().getChildren().size()`, abyste potvrdili, že byly přidány podřízené uzly.  
- **Check FBX version compatibility**: Některé starší nástroje podporují jen FBX 2013; můžete změnit formát na `FileFormat.FBX2013`, pokud je to potřeba.  

## Často kladené otázky  

**Q: Je Aspose.3D for Java vhodný pro začátečníky?**  
A: Rozhodně! API je navrženo s čistým, objektově orientovaným přístupem, který usnadňuje učení, i když jste nováčkem v 3D programování.  

**Q: Mohu používat Aspose.3D for Java pro komerční projekty?**  
A: Ano, můžete. Navštivte [purchase page](https://purchase.aspose.com/buy) pro podrobnosti o licencování.  

**Q: Jak mohu získat podporu pro Aspose.3D for Java?**  
A: Připojte se k [Aspose.3D forum](https://forum.aspose.com/c/3d/18), kde získáte pomoc od komunity a týmu podpory Aspose.  

**Q: Je k dispozici bezplatná zkušební verze?**  
A: Samozřejmě! Vyzkoušejte funkce pomocí [free trial](https://releases.aspose.com/) před závazkem.  

**Q: Kde mohu najít dokumentaci?**  
A: Podívejte se na [documentation](https://reference.aspose.com/3d/java/) pro podrobné informace o Aspose.3D for Java.  

## Závěr  

Zvládnutí **create child nodes**, **add mesh to node** a **how to export FBX** jsou nezbytné kroky k tvorbě sofistikovaných 3D aplikací v Javě. S Aspose.3D získáte výkonné, licencí přátelské řešení, které abstrahuje nízkoúrovňové detaily a zároveň vám poskytuje plnou kontrolu nad scénovým grafem. Experimentujte s různými mesh, transformacemi a exportními formáty a odhalte tak další možnosti.  

---  

**Poslední aktualizace:** 2026-04-12  
**Testováno s:** Aspose.3D for Java 24.11  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}  

{{< /blocks/products/pf/main-container >}}  
{{< /blocks/products/pf/main-wrap-class >}}  

{{< blocks/products/products-backtop-button >}}