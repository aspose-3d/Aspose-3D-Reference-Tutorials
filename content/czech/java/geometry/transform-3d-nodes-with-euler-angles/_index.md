---
title: Transformujte 3D uzly pomocí Eulerových úhlů v Javě pomocí Aspose.3D
linktitle: Transformujte 3D uzly pomocí Eulerových úhlů v Javě pomocí Aspose.3D
second_title: Aspose.3D Java API
description: Prozkoumejte svět 3D transformací v Javě s Aspose.3D. Postupujte podle našeho podrobného průvodce a přidejte do svých 3D uzlů dynamické Eulerovy úhly.
type: docs
weight: 19
url: /cs/java/geometry/transform-3d-nodes-with-euler-angles/
---
## Úvod

Vítejte v tomto podrobném tutoriálu o transformaci 3D uzlů pomocí Eulerových úhlů v Javě pomocí Aspose.3D. V této příručce se ponoříme do procesu přidávání transformací do 3D uzlu pomocí Eulerových úhlů k dosažení dynamického umístění a orientace.

## Předpoklady

Než se pustíme do výukového programu, ujistěte se, že máte splněny následující předpoklady:

- Základní znalost programování v Javě.
- Java Development Kit (JDK) nainstalovaný na vašem počítači.
-  Knihovna Aspose.3D, kterou můžete získat[Aspose.3D Java dokumentace](https://reference.aspose.com/3d/java/).

## Importujte balíčky

 Začněte importováním potřebných balíčků do vašeho projektu Java. Ujistěte se, že knihovna Aspose.3D je správně přidána do vaší třídy. Pokud jste si ji ještě nestáhli, najdete odkaz ke stažení[tady](https://releases.aspose.com/3d/java/).

```java
import com.aspose.threed.*;
```

## Krok 1. Inicializujte scénu a uzel

```java
// ExStart:AddTransformationToNodeByEulerAngles
// Inicializujte objekt scény
Scene scene = new Scene();

// Inicializujte objekt třídy Node
Node cubeNode = new Node("cube");
```

## Krok 2. Vytvořte síť a nastavte geometrii

```java
// Volejte Common class create mesh pomocí metody polygon builder pro nastavení instance mesh
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Bodový uzel ke geometrii sítě
cubeNode.setEntity(mesh);
```

## Krok 3. Nastavte Eulerovy úhly a překlad

```java
// Eulerovy úhly
cubeNode.getTransform().setEulerAngles(new Vector3(0.3, 0.1, -0.5));

// Nastavte překlad
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## Krok 4. Přidejte uzel do scény

```java
// Přidejte kostku na scénu
scene.getRootNode().getChildNodes().add(cubeNode);
```

## Krok 5. Uložte 3D scénu

```java
// Cesta k adresáři dokumentů.
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";

//Uložte 3D scénu v podporovaných formátech souborů
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByEulerAngles
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

Ujistěte se, že jste nahradili "Your Document Directory" příslušnou cestou na vašem počítači.

## Závěr

Gratulujeme! Úspěšně jste transformovali 3D uzly pomocí Eulerových úhlů v Javě s Aspose.3D. Experimentujte s různými úhly a překlady a vytvořte dynamické a poutavé 3D scény.

## FAQ

### Q1: Mohu použít Aspose.3D for Java v komerčních projektech?

 A1: Ano, můžete. Navštivte[nákupní stránku](https://purchase.aspose.com/buy) pro podrobnosti o licencích.

### Q2: Kde najdu podporu pro Aspose.3D?

 A2:[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) je místem, kde hledat pomoc a spojit se s komunitou.

### Q3: Je k dispozici bezplatná zkušební verze?

 A3: Ano, můžete prozkoumat[zkušební verze zdarma](https://releases.aspose.com/) vyzkoušet možnosti Aspose.3D.

### Q4: Jak mohu získat dočasnou licenci?

 A4: Můžete získat dočasnou licenci[tady](https://purchase.aspose.com/temporary-license/).

### Q5: Kde najdu dokumentaci?

 A5:[dokumentace](https://reference.aspose.com/3d/java/) poskytuje komplexní návod k používání Aspose.3D pro Java.