---
date: 2026-02-25
description: Naučte se, jak převrátit (otočit) souřadnicový systém a přizpůsobit import
  3D pomocí Aspose.3D LoadOptions v Javě. Podrobný krok‑za‑krokem návod pro 3DS, OBJ,
  STL, U3D, glTF, PLY, X a volitelně FBX.
linktitle: Customize 3D File Loading in Java with Aspose.3D LoadOptions
second_title: Aspose.3D Java API
title: Převrátit souřadnicový systém – Přizpůsobte načítání 3D souborů v Javě pomocí
  Aspose.3D
url: /cs/java/load-and-save/customize-3d-file-loading/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Převrácení souřadnicového systému – Přizpůsobení načítání 3D souborů v Javě s Aspose.3D

V neustále se vyvíjejícím prostředí 3D designu a vývoje je **převrácení souřadnicového systému** při importu modelů běžnou požadavkem. Ať už převádíte assety z pravotočivého na levotočivý systém nebo potřebujete zarovnat modely s konvencemi os vašeho enginu, Aspose.3D pro Javu vám poskytuje detailní kontrolu. Tento tutoriál vás provede, jak **přizpůsobit 3D import** pomocí `LoadOptions` z Aspose.3D, pokrývající nejoblíbenější formáty jako 3DS, OBJ, STL, U3D, glTF, PLY, X a volitelný FBX.

## Rychlé odpovědi
- **Co dělá „převrácení souřadnicového systému“?** Přepíná osy X/Y/Z tak, aby odpovídaly cílové souřadnicové konvenci.  
- **Které formáty podporují převrácení?** Všechny hlavní formáty (3DS, OBJ, STL, U3D, glTF, PLY, X, FBX) nabízejí možnost `setFlipCoordinateSystem`.  
- **Potřebuji další knihovny?** Pouze JAR Aspose.3D pro Javu; žádné externí konvertory nejsou vyžadovány.  
- **Mohu načíst materiály současně?** Ano — použijte `setEnableMaterials(true)` pro soubory OBJ.  
- **Je licence vyžadována pro produkci?** Platná licence Aspose.3D je potřeba pro nasazení mimo zkušební verzi.

## Co je „převrácení souřadnicového systému“?
Převrácení souřadnicového systému mění orientaci os používaných importovaným modelem. To je nezbytné, když zdrojový soubor používá jinou „handedness“ (pravotočivý vs. levotočivý) než váš renderovací engine, čímž se zabrání tomu, aby se modely jevily jako zrcadlové nebo převrácené.

## Proč přizpůsobit 3D import?
- Zachovat transformace animací (`setApplyAnimationTransform`).  
- Správně zpracovávat barvy (`setGammaCorrectedColor`).  
- Vyřešit cesty k externím zdrojům pomocí `getLookupPaths()`.  
- Optimalizovat využití paměti načítáním jen toho, co potřebujete.

## Požadavky

- Základní znalost programování v Javě.  
- Nainstalovaný Java Development Kit (JDK).  
- Stažená knihovna Aspose.3D pro Javu. Můžete ji získat [zde](https://releases.aspose.com/3d/java/).  
- Znalost 3D formátů souborů jako 3DS, OBJ, STL, U3D, glTF, PLY, X a FBX.

## Import balíčků

Ve vašem Java projektu se ujistěte, že importujete potřebné balíčky Aspose.3D:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Jak přizpůsobit 3D import pomocí LoadOptions

Níže jsou krok za krokem ukázky kódu, které demonstrují, jak povolit možnost **převrácení souřadnicového systému** pro každý podporovaný formát. Úryvky jsou připravené ke zkopírování do vašeho projektu; stačí nahradit `"Your Document Directory"` skutečnou cestou k vašim assetům.

### Krok 1: Přizpůsobení načítání souboru 3DS

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

### Krok 2: Přizpůsobení načítání souboru OBJ

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### Krok 3: Přizpůsobení načítání souboru STL

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### Krok 4: Přizpůsobení načítání souboru U3D

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### Krok 5: Přizpůsobení načítání souboru glTF

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### Krok 6: Přizpůsobení načítání souboru PLY

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### Krok 7: Přizpůsobení načítání souboru X

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### Krok 8: Přizpůsobení načítání souboru FBX (volitelné)

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

## Časté problémy a řešení
- **Model se po načtení jeví jako zrcadlový** — Ověřte, že `setFlipCoordinateSystem(true)` je nastaveno pro správný formát.  
- **Chybí materiály** — U souborů OBJ zajistěte `setEnableMaterials(true)` a že soubory materiálů (.mtl) jsou umístěny v jedné z cest pro vyhledávání.  
- **Texturové souřadnice jsou vzhůru nohama** — U glTF možná potřebujete `setFlipTexCoordV(true)` kromě převrácení os.  
- **Chyby souboru nenalezen** — Přidejte adresář obsahující externí zdroje (textury, pomocné soubory) do `loadOpts.getLookupPaths()`.

## Závěr

Využitím `LoadOptions` z Aspose.3D můžete **převrátit souřadnicový systém** a **přizpůsobit 3D import** pro prakticky každý hlavní formát. Tato úroveň kontroly eliminuje potřebu post‑processingových skriptů a zajišťuje, že vaše assety se vykreslí správně hned napoprvé.

## Často kladené otázky

### Q1: Kde najdu dokumentaci Aspose.3D pro Javu?
**A1:** Dokumentace je k dispozici [zde](https://reference.aspose.com/3d/java/).

### Q2: Jak si mohu stáhnout Aspose.3D pro Javu?
**A2:** Můžete si jej stáhnout [zde](https://releases.aspose.com/3d/java/).

### Q3: Je k dispozici bezplatná zkušební verze?
**A3:** Ano, bezplatnou zkušební verzi můžete získat [zde](https://releases.aspose.com/).

### Q4: Kde mohu získat podporu pro Aspose.3D pro Javu?
**A4:** Navštivte fórum podpory [zde](https://forum.aspose.com/c/3d/18).

### Q5: Potřebuji dočasnou licenci pro testování?
**A5:** Ano, získáte dočasnou licenci [zde](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Poslední aktualizace:** 2026-02-25  
**Testováno s:** Aspose.3D for Java 24.11 (latest)  
**Autor:** Aspose