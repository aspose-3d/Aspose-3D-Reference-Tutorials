---
title: Transformujte 3D uzly pomocí transformačních matic pomocí Aspose.3D
linktitle: Transformujte 3D uzly pomocí transformačních matic v Javě pomocí Aspose.3D
second_title: Aspose.3D Java API
description: Prozkoumejte svět 3D grafiky v Javě s Aspose.3D. Naučte se snadno transformovat uzly pomocí transformačních matic.
type: docs
weight: 21
url: /cs/java/geometry/transform-3d-nodes-with-matrices/
---
## Úvod

Vítejte v tomto podrobném průvodci o transformaci 3D uzlů pomocí transformačních matic v Javě pomocí Aspose.3D. Pokud jste vývojář v jazyce Java a chcete zlepšit své dovednosti v oblasti 3D grafiky a modelování, jste na správném místě. V tomto tutoriálu se ponoříme do procesu aplikace transformací na 3D uzly v rámci Aspose.3D.

## Předpoklady

Než začneme, ujistěte se, že máte následující předpoklady:

- Základní znalost programování v Javě.
-  Nainstalovaná knihovna Aspose.3D. Můžete si jej stáhnout z[tady](https://releases.aspose.com/3d/java/).
- Funkční integrované vývojové prostředí (IDE) pro vývoj v Javě.

## Importujte balíčky

Ve svém projektu Java importujte potřebné balíčky z Aspose.3D. Ujistěte se, že je váš projekt správně nakonfigurován pro použití knihovny Aspose.3D. Zde je vzorový příkaz k importu:

```java
import com.aspose.threed.*;

```

## Transformace 3D uzlů

### Krok 1: Inicializujte objekt scény

Začněte inicializací objektu scény, který slouží jako kontejner pro 3D prvky.

```java
Scene scene = new Scene();
```

### Krok 2: Inicializujte objekt třídy uzlu

Vytvořte objekt třídy Node, například krychli, který projde transformací.

```java
Node cubeNode = new Node("cube");
```

### Krok 3: Vytvořte síť pomocí Polygon Builder

Použijte třídu Common k vytvoření sítě pomocí metody polygon builder. Tím nastavíte instanci sítě pro krychli.

```java
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

### Krok 4: Bodový uzel na geometrii sítě

Vytvořenou síť přiřaďte uzlu krychle.

```java
cubeNode.setEntity(mesh);
```

### Krok 5: Nastavte vlastní matici překladu

Použijte vlastní matici překladu na uzel krychle. Tento příklad nastavuje transformační matici pro překlad.

```java
cubeNode.getTransform().setTransformMatrix(new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
));
```

### Krok 6: Přidejte kostku do scény

Zahrňte uzel krychle do kořenového uzlu scény.

```java
scene.getRootNode().addChildNode(cubeNode);
```

### Krok 7: Uložte 3D scénu

Zadejte adresář a název souboru pro uložení 3D scény v podporovaných formátech souborů, jako je FBX.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

## Závěr

Gratulujeme! Úspěšně jste se naučili, jak transformovat 3D uzly pomocí Aspose.3D v Javě. Experimentujte s různými maticemi a prozkoumejte nekonečné možnosti 3D grafiky.

## FAQ

### Q1: Mohu použít více transformací na jeden 3D uzel?

Odpověď 1: Ano, pro složité transformace můžete zřetězit více transformačních matic.

### Q2: Jak mohu otočit 3D objekt v Aspose.3D?

A2: Použijte příslušnou rotační matici v transformační matici pro požadované otočení.

### Otázka 3: Existuje omezení velikosti 3D scén, které mohu vytvořit?

Odpověď 3: Velikost vašich 3D scén může být omezena systémovými prostředky, ale Aspose.3D je navržen pro efektivitu.

### Q4: Kde najdu další příklady a dokumentaci?

 A4: Navštivte[Aspose.3D dokumentace](https://reference.aspose.com/3d/java/) pro více příkladů a podrobností.

### Q5: Jak získám dočasnou licenci pro Aspose.3D?

 A5: Můžete získat dočasnou licenci[tady](https://purchase.aspose.com/temporary-license/).