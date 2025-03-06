---
title: Vytvořte 3D kostkovou scénu v Javě pomocí Aspose.3D
linktitle: Vytvořte 3D kostkovou scénu v Javě pomocí Aspose.3D
second_title: Aspose.3D Java API
description: Prozkoumejte zázraky grafiky 3D krychlových scén s Aspose.3D pro Javu. Vytvářejte úžasné scény bez námahy.
weight: 12
url: /cs/java/geometry/create-3d-cube-scene/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Vytvořte 3D kostkovou scénu v Javě pomocí Aspose.3D

## Úvod

Vítejte ve fascinujícím světě 3D grafiky v Javě pomocí Aspose.3D! V tomto tutoriálu vás provedeme procesem vytváření úžasné 3D scény s krychlí pomocí Aspose.3D for Java. Aspose.3D je výkonná Java knihovna, která poskytuje komplexní funkce pro práci s 3D modely a scénami.

## Předpoklady

Než se pustíme do tvorby 3D scény krychle, ujistěte se, že máte splněny následující předpoklady:

1.  Java Development Kit (JDK): Ujistěte se, že máte v systému nainstalovanou Javu. Nejnovější verzi si můžete stáhnout z[Web společnosti Oracle](https://www.oracle.com/java/).

2.  Aspose.3D for Java Library: Stáhněte a nainstalujte knihovnu Aspose.3D. Odkaz ke stažení najdete[tady](https://releases.aspose.com/3d/java/).

## Importujte balíčky

Začněte importováním potřebných balíčků do vašeho projektu Java:

```java
import java.io.File;

import com.aspose.threed.Box;
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Mesh;
import com.aspose.threed.Node;
import com.aspose.threed.Scene;
```

Nyní si rozdělme proces vytváření 3D krychlové scény do několika kroků.

## Krok 1: Inicializujte scénu

```java
// Inicializujte objekt scény
Scene scene = new Scene();
```

## Krok 2: Inicializujte Node a Mesh

```java
// Inicializujte objekt třídy Node
Node cubeNode = new Node("box");

// Volejte Common class create mesh pomocí metody polygon builder pro nastavení instance mesh
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Bodový uzel ke geometrii sítě
cubeNode.setEntity(mesh);
```

## Krok 3: Přidejte uzel do scény

```java
// Přidejte uzel do scény
scene.getRootNode().getChildNodes().add(cubeNode);
```

## Krok 4: Uložte 3D scénu

```java
// Cesta k adresáři dokumentů.
String MyDir = "Your Document Directory";
MyDir = MyDir + "CubeScene.fbx";

// Uložte 3D scénu v podporovaných formátech souborů
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Krok 5: Tisk zprávy o úspěchu

```java
System.out.println("\nCube Scene created successfully.\nFile saved at " + MyDir);
```

## Závěr

Gratulujeme! Úspěšně jste vytvořili scénu 3D krychle pomocí Aspose.3D for Java. Tento tutoriál poskytuje pevný základ pro objevování pokročilejších funkcí a uvolnění vaší kreativity ve světě 3D grafiky.

## FAQ

### Q1: Mohu použít Aspose.3D pro komerční projekty?

 A1: Ano, můžete. Zkontrolovat[nákupní stránku](https://purchase.aspose.com/buy) pro podrobnosti o licencích.

### Q2: Jak mohu získat podporu pro Aspose.3D?

 A2: Navštivte[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) za podporu komunity.

### Q3: Je k dispozici bezplatná zkušební verze?

 A3: Ano, můžete získat bezplatnou zkušební verzi[tady](https://releases.aspose.com/).

### Q4: Kde najdu dokumentaci k Aspose.3D?

 A4: Viz[Aspose.3D dokumentace](https://reference.aspose.com/3d/java/) pro podrobné informace.

### Q5: Jak získat dočasnou licenci pro Aspose.3D?

 A5: Můžete získat dočasnou licenci[tady](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
