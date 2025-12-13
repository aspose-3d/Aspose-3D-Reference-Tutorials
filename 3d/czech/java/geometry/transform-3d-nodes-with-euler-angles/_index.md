---
date: 2025-12-13
description: Naučte se, jak používat Aspose 3D Java k transformaci 3D uzlů. Tento
  průvodce ukazuje, jak použít Eulerovy úhly, přidat 3D rotaci a nastavit translaci
  v Javě.
linktitle: Aspose 3D Java – Transform 3D Nodes with Euler Angles
second_title: Aspose.3D Java API
title: Aspose 3D Java – Transformovat 3D uzly pomocí Eulerových úhlů
url: /cs/java/geometry/transform-3d-nodes-with-euler-angles/
weight: 19
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Transformujte 3D uzly pomocí Eulerových úhlů v Javě s Aspose.3D

## Úvod

V tomto tutoriálu se dozvíte **jak použít aspose 3d java** k transformaci 3D uzlů aplikací Eulerových úhlů. Na konci průvodce budete schopni přidat 3D rotaci, nastavit translaci v Javě a vytvořit dynamické scény, které reagují na data v reálném čase.

## Rychlé odpovědi
- **Která knihovna provádí 3D transformace v Javě?** Aspose 3D for Java.  
- **Která metoda nastavuje rotaci pomocí Eulerových úhlů?** `setEulerAngles()` na transformaci uzlu.  
- **Jak přesunu uzel v prostoru?** Použijte `setTranslation()` s objektem `Vector3`.  
- **Potřebuji licenci pro produkční nasazení?** Ano, je vyžadována komerční licence Aspose 3D.  
- **Mohu exportovat do FBX?** Rozhodně – `scene.save(..., FileFormat.FBX7500ASCII)` funguje bez dalších úprav.

## Předpoklady

Než se pustíme do tutoriálu, ujistěte se, že máte připravené následující předpoklady:

- Základní znalosti programování v Javě.  
- Nainstalovaný Java Development Kit (JDK).  
- Knihovnu Aspose.3D, kterou můžete získat z [Aspose.3D Java Documentation](https://reference.aspose.com/3d/java/).

## Import balíčků

Začněte importováním potřebných balíčků do vašeho Java projektu. Ujistěte se, že je knihovna Aspose.3D správně přidána do classpath. Pokud jste ji ještě nestáhli, najdete odkaz ke stažení [zde](https://releases.aspose.com/3d/java/).

```java
import com.aspose.threed.*;
```

## aspose 3d java – Práce s Eulerovými úhly

### Krok 1. Inicializace scény a uzlu

Nejprve vytvořte scénu a uzel, který bude obsahovat geometrii, kterou chcete transformovat.

```java
// ExStart:AddTransformationToNodeByEulerAngles
// Initialize scene object
Scene scene = new Scene();

// Initialize Node class object
Node cubeNode = new Node("cube");
```

### Krok 2. Vytvoření mesh a nastavení geometrie

Dále vygenerujte jednoduchý mesh (v tomto případě krychli) a připojte jej k uzlu.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Point node to the Mesh geometry
cubeNode.setEntity(mesh);
```

## Přidání 3D rotace k uzlu

### Krok 3. Nastavení Eulerových úhlů a translace

Nyní aplikujeme rotaci pomocí Eulerových úhlů a zároveň posuneme uzel do viditelné pozice.

```java
// Euler angles
cubeNode.getTransform().setEulerAngles(new Vector3(0.3, 0.1, -0.5));

// Set translation
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## Nastavení translace v Javě – Umístění uzlu

Výše uvedený krok translace demonstruje **set translation java** v praxi: uzel je posunut o 20 jednotek podél osy Z, aby byl po vykreslení viditelný.

## Krok 4. Přidání uzlu do scény

Připojte transformovaný uzel k kořenovému uzlu scény.

```java
// Add cube to the scene
scene.getRootNode().getChildNodes().add(cubeNode);
```

## Krok 5. Uložení 3D scény

Nakonec exportujte scénu do souboru FBX (nebo jakéhokoli jiného podporovaného formátu).

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByEulerAngles
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

Nezapomeňte nahradit `"Your Document Directory"` vhodnou cestou na vašem počítači.

## Závěr

Gratulujeme! Úspěšně jste transformovali 3D uzly pomocí Eulerových úhlů v Javě s **aspose 3d java**. Experimentujte s různými úhly a translacemi a vytvářejte dynamické a poutavé 3D scény.

## Často kladené otázky

### Q1: Mohu používat Aspose.3D pro Java v komerčních projektech?

A1: Ano, můžete. Navštivte [stránku nákupu](https://purchase.aspose.com/buy) pro podrobnosti o licencování.

### Q2: Kde najdu podporu pro Aspose.3D?

A2: Fórum [Aspose.3D](https://forum.aspose.com/c/3d/18) je místem, kde můžete získat pomoc a spojit se s komunitou.

### Q3: Je k dispozici bezplatná zkušební verze?

A3: Ano, můžete vyzkoušet [bezplatnou verzi](https://releases.aspose.com/) a poznat možnosti Aspose.3D.

### Q4: Jak získám dočasnou licenci?

A4: Dočasnou licenci můžete získat [zde](https://purchase.aspose.com/temporary-license/).

### Q5: Kde najdu dokumentaci?

A5: Dokumentace na [odkaz](https://reference.aspose.com/3d/java/) poskytuje komplexní návod k používání Aspose.3D pro Java.

## Často kladené otázky

**Q: Jaký je rozdíl mezi Eulerovými úhly a rotací pomocí quaternionu?**  
A: Eulerovy úhly jsou intuitivní (pitch, yaw, roll), ale mohou trpět gimbal lockem, zatímco quaterniony tomuto problému předcházejí a jsou vhodnější pro plynulé interpolace.

**Q: Mohu řetězit více transformací na stejném uzlu?**  
A: Ano. Zavolejte `setEulerAngles`, `setTranslation` a `setScale` v libovolném pořadí; knihovna je spojí do jedné transformační matice.

**Q: Je možné exportovat do jiných formátů, jako OBJ nebo STL?**  
A: Rozhodně. Nahraďte `FileFormat.FBX7500ASCII` za `FileFormat.OBJ` nebo `FileFormat.STL` v metodě `scene.save`.

**Q: Jak aplikovat stejnou rotaci na několik uzlů najednou?**  
A: Vytvořte rodičovský uzel, aplikujte rotaci na něj a přidejte podřízené uzly. Všechny podřízené uzly zdědí transformaci.

**Q: Musím po uložení volat nějaké úklidové metody?**  
A: Java garbage collector zvládne většinu prostředků, ale můžete explicitně zavolat `scene.dispose()`, pokud pracujete s velkými scénami v dlouho běžící aplikaci.

---

**Poslední aktualizace:** 2025-12-13  
**Testováno s:** Aspose.3D 23.12 pro Java  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}