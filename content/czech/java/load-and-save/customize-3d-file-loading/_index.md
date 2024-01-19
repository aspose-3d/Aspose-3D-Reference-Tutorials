---
title: Přizpůsobte si načítání 3D souborů v Javě pomocí Aspose.3D LoadOptions
linktitle: Přizpůsobte si načítání 3D souborů v Javě pomocí Aspose.3D LoadOptions
second_title: Aspose.3D Java API
description: Vylepšete načítání 3D souborů v Javě pomocí Aspose.3D přizpůsobitelných LoadOptions. Naučte se krok za krokem přizpůsobení pro 3DS, OBJ, STL, U3D, glTF, PLY, X a volitelný FBX.
type: docs
weight: 12
url: /cs/java/load-and-save/customize-3d-file-loading/
---
## Úvod

neustále se vyvíjejícím prostředí 3D designu a vývoje je efektivní manipulace s 3D formáty souborů zásadní. Aspose.3D for Java poskytuje výkonné řešení pro přizpůsobení načítání různých 3D formátů souborů. Tento tutoriál vás provede procesem přizpůsobení načítání 3D souborů v Javě pomocí LoadOptions Aspose.3D.

## Předpoklady

Než se ponoříte do procesu přizpůsobení, ujistěte se, že máte následující:

- Základní znalost programování v Javě.
- Nainstalovaný Java Development Kit (JDK).
-  Knihovna Aspose.3D pro Java stažena. Můžete jej získat[tady](https://releases.aspose.com/3d/java/).
- Znalost 3D formátů souborů, jako jsou 3DS, OBJ, STL, U3D, glTF, PLY, X a FBX.

## Importujte balíčky

Ve svém projektu Java se ujistěte, že importujete potřebné balíčky Aspose.3D:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Přizpůsobte načítání 3D souborů

### Krok 1: Přizpůsobte načítání souborů 3DS

```java
public static void discreet3DSLoadOption() {
    String MyDir = "Your Document Directory";
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();
    loadOpts.setApplyAnimationTransform(true);
    loadOpts.setFlipCoordinateSystem(true);
    loadOpts.setGammaCorrectedColor(true);
    loadOpts.getLookupPaths().add(MyDir);
}
```

### Krok 2: Přizpůsobte načítání souboru OBJ

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### Krok 3: Přizpůsobte načítání souborů STL

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### Krok 4: Přizpůsobte načítání souboru U3D

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### Krok 5: Přizpůsobte načítání souboru glTF

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### Krok 6: Přizpůsobte načítání souboru PLY

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### Krok 7: Přizpůsobte načítání souboru X

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### Krok 8: Přizpůsobte načítání souborů FBX (volitelné)

```java
private static void FBXLoadOptions() throws IOException {
    String dataDir = "Your Document Directory";
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions();
    opt.setKeepBuiltinGlobalSettings(true);
    scene.open(dataDir + "test.FBX", opt);
    for(Property property:scene.getRootNode().getAssetInfo().getProperties()) {
        System.out.println(property);
    }
}
```

## Závěr

Přizpůsobení načítání 3D souborů v Javě pomocí LoadOptions Aspose.3D umožňuje vývojářům přizpůsobit proces importu konkrétním požadavkům. Ať už se jedná o úpravu animačních transformací, překlápění souřadnicových systémů nebo zpracování externích závislostí, Aspose.3D poskytuje flexibilitu potřebnou pro bezproblémovou integraci.

## Nejčastější dotazy

### Q1: Kde najdu dokumentaci Aspose.3D for Java?

 A1: Dokumentace je k dispozici[tady](https://reference.aspose.com/3d/java/).

### Q2: Jak si mohu stáhnout Aspose.3D pro Java?

 A2: Můžete si to stáhnout[tady](https://releases.aspose.com/3d/java/).

### Q3: Je k dispozici bezplatná zkušební verze?

 A3: Ano, máte přístup k bezplatné zkušební verzi[tady](https://releases.aspose.com/).

### Q4: Kde mohu získat podporu pro Aspose.3D pro Java?

 A4: Navštivte fórum podpory[tady](https://forum.aspose.com/c/3d/18).

### Q5: Potřebuji pro testování dočasnou licenci?

 A5: Ano, získat dočasnou licenci[tady](https://purchase.aspose.com/temporary-license/).