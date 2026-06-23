---
date: 2026-06-23
description: Zjistěte, jak vytvořit podřízené uzly, přidat mesh do uzlu a exportovat
  FBX pomocí schopností java 3d scene graph v Aspose.3D Java API.
keywords:
- java 3d scene graph
- how to export fbx
- add mesh to node
- how to create child nodes
- save scene as fbx
- convert scene to fbx
linktitle: Vytvořte hierarchie uzlů ve 3D scénách pomocí Javy a Aspose.3D
schemas:
- author: Aspose
  dateModified: '2026-06-23'
  description: Learn how to create child nodes, add mesh to node, and export FBX using
    the java 3d scene graph capabilities of Aspose.3D Java API.
  headline: 'java 3d scene graph: Create Child Nodes and Export FBX in Java with Aspose.3D'
  type: TechArticle
- description: Learn how to create child nodes, add mesh to node, and export FBX using
    the java 3d scene graph capabilities of Aspose.3D Java API.
  name: 'java 3d scene graph: Create Child Nodes and Export FBX in Java with Aspose.3D'
  steps:
  - name: '**Java Development Environment** – JDK 8+ and an IDE or build tool of your
      choice.'
    text: '**Java Development Environment** – JDK 8+ and an IDE or build tool of your
      choice.'
  - name: '**Aspose.3D for Java Library** – Download and install the library from
      the [download page](https://releases.aspose.com/3d/java/).'
    text: '**Aspose.3D for Java Library** – Download and install the library from
      the [download page](https://releases.aspose.com/3d/java/).'
  - name: '**Document Directory** – A folder on your machine where the generated FBX
      file will be saved.'
    text: '**Document Directory** – A folder on your machine where the generated FBX
      file will be saved.'
  type: HowTo
- questions:
  - answer: Absolutely! The API is designed with a clean, object‑oriented approach
      that makes it easy to learn, even if you’re new to 3D programming.
    question: Is Aspose.3D for Java suitable for beginners?
  - answer: Yes, you can. Visit the [purchase page](https://purchase.aspose.com/buy)
      for licensing details.
    question: Can I use Aspose.3D for Java for commercial projects?
  - answer: Join the [Aspose.3D forum](https://forum.aspose.com/c/3d/18) to get assistance
      from the community and Aspose support team.
    question: How can I get support for Aspose.3D for Java?
  - answer: Certainly! Explore the features with the [free trial](https://releases.aspose.com/)
      before making a commitment.
    question: Is there a free trial available?
  - answer: Refer to the [documentation](https://reference.aspose.com/3d/java/) for
      detailed information on Aspose.3D for Java.
    question: Where can I find the documentation?
  type: FAQPage
second_title: Aspose.3D Java API
title: 'java 3d scene graph: Vytvořte podřízené uzly a exportujte FBX v Javě s Aspose.3D'
url: /cs/java/geometry/build-node-hierarchies/
weight: 16
---

{{< blocks/products/pf/main-wrap-class >}}

## Související tutoriály

- [Vytvořit Mesh Aspose Java – Transformovat 3D uzly pomocí Eulerových úhlů](/3d/java/geometry/transform-3d-nodes-with-euler-angles/)
- [Vytvořit 3D scénu Java – Použít PBR materiály s Aspose.3D](/3d/java/geometry/apply-pbr-materials-to-objects/)
- [Jak exportovat scénu do FBX a získat informace o 3D scéně v Javě](/3d/java/3d-scenes-and-models/get-scene-information/)


{{< /blocks/products/pf/tutorial-page-section >}}  
{{< blocks/products/pf/tutorial-page-section >}}  

# Jak exportovat FBX a vytvořit hierarchie uzlů v Javě s Aspose.3D  

## Úvod  

Pokud hledáte jasný, krok‑za‑krokem průvodce k **vytvoření podřízených uzlů**, **přidání meshe do uzlu** a **jak exportovat FBX** z Java aplikace, jste na správném místě. V tomto tutoriálu projdeme tvorbu **java 3d scénového grafu**, připojování meshů, aplikaci transformací a nakonec uložení scény jako souboru FBX pomocí Aspose.3D Java API. Ať už prototypujete jednoduchou ukázku nebo vyvíjíte produkčně připravený 3D engine, zvládnutí těchto konceptů vám poskytne plnou kontrolu nad hierarchií scény a exportním workflow.  

## Rychlé odpovědi  
- **Jaký je hlavní účel tohoto tutoriálu?** Ukázat, jak **vytvořit podřízené uzly**, připojit meshe a **exportovat FBX** po vytvoření hierarchie uzlů.  
- **Která knihovna je použita?** Aspose.3D pro Java.  
- **Potřebuji licenci?** Bezplatná zkušební verze funguje pro vývoj; pro produkci je vyžadována komerční licence.  
- **Jaký formát souboru je vytvořen?** FBX (ASCII 7500).  
- **Mohu přizpůsobit transformace uzlů?** Ano – translace, rotace a škálování jsou plně podporovány.  

## Co je java 3d scénový graf?  

**java 3d scénový graf** je hierarchická datová struktura, která představuje objekty (`Node`s) a jejich vztahy v 3D světě. Organizací objektů jako páry rodič‑potomek můžete aplikovat jedinou transformaci na rodiče a nechat ji kaskádovat na všechny potomky, což zjednodušuje animaci a správu scény.  

## Proč vytvářet hierarchie uzlů před exportem?  

Dobře strukturovaná hierarchie snižuje duplicitní kód, zjednodušuje animaci a odráží vztahy ve skutečném světě. Když později **převádíte scénu do FBX** (nebo jiného formátu), hierarchie je zachována, takže nástroje jako Blender, Maya nebo Unity přesně rozpoznají vztahy rodič‑potomek tak, jak jste je navrhli.  

## Kvantifikované výhody Aspose.3D  

Aspose.3D podporuje **více než 30 formátů pro import a export** – včetně FBX, OBJ, STL, 3DS a Collada – a dokáže zpracovat **scény o stovkách stránek** bez načítání celého souboru do paměti. Knihovna vykresluje meshe až **60 fps** na standardním hardware, což umožňuje náhled v reálném čase během vývoje.  

## Běžné případy použití hierarchií uzlů  

| Případ použití | Proč hierarchie pomáhá | Typický výsledek |
|----------------|-----------------------|------------------|
| **Mechanické sestavy (např. robotické rameno)** | Otáčením základního uzlu se pohybují všechny připojené segmenty | Jednoduchá animace složitých mechanismů |
| **Rigy postav** | Kosti skeletu jsou podřízené uzly kořene | Konzistentní transformace póz |
| **Organizace scény** | Skupinování statických objektů pod uzlem „props“ | Čistší správa scény a selektivní export |
| **Přepínání úrovně detailu (LOD)** | Rodičovský uzel přepíná viditelnost podřízených meshů | Optimalizované renderování pro různé hardware |

## Požadavky  

1. **Java vývojové prostředí** – JDK 8+ a IDE nebo build nástroj dle vašeho výběru.  
2. **Aspose.3D pro Java knihovna** – Stáhněte a nainstalujte knihovnu ze [stránky ke stažení](https://releases.aspose.com/3d/java/).  
3. **Adresář dokumentů** – Složka ve vašem počítači, kam bude uložen vygenerovaný soubor FBX.  

## Import balíčků  

Namespace `com.aspose.threed` poskytuje všechny třídy, které budete potřebovat pro tvorbu scény, manipulaci s uzly a export souborů. Před zahájením importujte následující balíčky:  

```java
import com.aspose.threed.*;
```  

## Krok 1: Inicializace objektu scény  

Třída `Scene` je kontejner nejvyšší úrovně, který obsahuje celou 3D hierarchii. Vytvořením instance `Scene` se alokuje kořenový uzel a připraví interní datové struktury pro meshe, světla a kamery.  

```java
// Initialize scene object
Scene scene = new Scene();
```  

## Krok 2: Vytvoření podřízených uzlů a přidání meshe do uzlu  

V tomto kroku ukážeme **jak vytvořit podřízené uzly** a **přidat mesh do uzlu**. Třída `Node` představuje jeden prvek v hierarchii, zatímco třída `Mesh` ukládá geometrická data, jako jsou vrcholy a plochy.  

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

Otáčením rodičovského uzlu se automaticky otáčí všechny jeho podřízené uzly, což je hlavní výhoda hierarchických scén. Použijte třídu `Quaternion` k definování rotace v radiánech pro plynulou interpolaci.  

```java
// Rotate the top node, affecting all child nodes
top.getTransform().setRotation(Quaternion.fromEulerAngle(Math.PI, 4, 0));
```  

## Krok 4: Uložení 3D scény – Jak exportovat FBX  

Nyní **uložíme scénu jako FBX**, čímž dokončíme workflow „jak exportovat fbx“. Metoda `Scene.save` přijímá cestu k souboru a výčtový typ `FileFormat`, který vám umožní vybrat mezi FBX 2013, FBX 2014 nebo nejnovějším formátem ASCII 7500. Výčtový typ `FileFormat` uvádí podporované exportní formáty, jako jsou FBX2013, FBX2014 a ASCII 7500.  

```java
// Save 3D scene in the supported file format (FBX in this case)
String MyDir = "Your Document Directory";
MyDir = MyDir + "NodeHierarchy.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nNode hierarchy added successfully to document.\nFile saved at " + MyDir);
```  

### Očekávaný výsledek  

Spuštěním kódu se vytvoří soubor **NodeHierarchy.fbx** ve zvoleném adresáři. Otevřete jej v libovolném FBX‑kompatibilním prohlížeči a uvidíte dva krychle umístěné vlevo a vpravo od centrálního pivotu, všechny rotující společně.  

## Běžné problémy a řešení  

| Problém | Proč se vyskytuje | Řešení |
|---------|-------------------|--------|
| **Chyba soubor nenalezen při ukládání** | Cesta MyDir je nesprávná nebo chybí koncový oddělovač | Ujistěte se, že adresář existuje a končí souborovým oddělovačem (`/` nebo `\\`). |
| **Mesh není po exportu viditelný** | Entita mesh není přiřazena nebo překlad ji posune mimo zorné pole | Ověřte `cube1.setEntity(mesh)` a zkontrolujte hodnoty translace. |
| **Rotace vypadá špatně** | Nesprávné použití radiánů místo stupňů | `Quaternion.fromEulerAngle` očekává radiány; upravte hodnoty podle toho. |

## Tipy pro odstraňování problémů  

- **Ověřte adresář**: Použijte `new File(MyDir).mkdirs();` před `scene.save`, pokud složka nemusí existovat.  
- **Prozkoumejte scénový graf**: Zavolejte `scene.getRootNode().getChildren().size()`, abyste potvrdili, že podřízené uzly byly přidány.  
- **Zkontrolujte kompatibilitu verze FBX**: Některé starší nástroje podporují jen FBX 2013; v případě potřeby můžete změnit formát na `FileFormat.FBX2013`.  

## Často kladené otázky  

**Q: Je Aspose.3D pro Java vhodný pro začátečníky?**  
A: Rozhodně! API je navrženo s čistým, objektově orientovaným přístupem, který usnadňuje učení, i když jste v 3D programování nováčkem.  

**Q: Mohu použít Aspose.3D pro Java v komerčních projektech?**  
A: Ano, můžete. Navštivte [stránku nákupu](https://purchase.aspose.com/buy) pro podrobnosti o licencování.  

**Q: Jak mohu získat podporu pro Aspose.3D pro Java?**  
A: Připojte se k [fóru Aspose.3D](https://forum.aspose.com/c/3d/18), kde získáte pomoc od komunity a týmu podpory Aspose.  

**Q: Je k dispozici bezplatná zkušební verze?**  
A: Samozřejmě! Vyzkoušejte funkce pomocí [bezplatné zkušební verze](https://releases.aspose.com/) před závazkem.  

**Q: Kde mohu najít dokumentaci?**  
A: Podívejte se na [dokumentaci](https://reference.aspose.com/3d/java/) pro podrobné informace o Aspose.3D pro Java.  

## Závěr  

Zvládnutí **vytvoření podřízených uzlů**, **přidání meshe do uzlu** a **jak exportovat FBX** jsou nezbytné kroky k tvorbě sofistikovaných 3D aplikací v Javě. S Aspose.3D získáte výkonné, licencemi přátelské řešení, které abstrahuje nízkoúrovňové detaily a zároveň vám poskytuje plnou kontrolu nad java 3d scénovým grafem. Experimentujte s různými meshemi, transformacemi a exportními formáty a odhalte tak další možnosti.  

---  

**Poslední aktualizace:** 2026-06-23  
**Testováno s:** Aspose.3D pro Java 24.11  
**Autor:** Aspose  

{{< /blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/products-backtop-button >}}
{{< /blocks/products/pf/main-container >}}