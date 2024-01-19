---
title: Optimalizujte ukládání 3D souborů v Javě pomocí Aspose.3D SaveOptions
linktitle: Optimalizujte ukládání 3D souborů v Javě pomocí Aspose.3D SaveOptions
second_title: Aspose.3D Java API
description: Naučte se optimalizovat ukládání 3D souborů v Javě pomocí Aspose.3D SaveOptions. Zvyšte výkon a přizpůsobte výstupy bez námahy.
type: docs
weight: 16
url: /cs/java/load-and-save/optimize-3d-file-saving/
---
## Úvod

Aspose.3D je knihovna Java s bohatými funkcemi, která umožňuje vývojářům bezproblémově pracovat s 3D modely. Pokud jde o ukládání 3D souborů, třída SaveOptions nabízí nepřeberné množství nastavení pro doladění výstupu podle vašich požadavků. V tomto tutoriálu prozkoumáme různé možnosti ukládání a jak je lze využít k optimalizaci procesu.

## Předpoklady

Než se pustíme do výukového programu, ujistěte se, že máte splněny následující předpoklady:

-  Aspose.3D for Java: Ujistěte se, že máte knihovnu Aspose.3D integrovanou do vašeho projektu Java. Můžete si jej stáhnout[tady](https://releases.aspose.com/3d/java/).

- Vývojové prostředí Java: Mějte na svém počítači nastavené funkční vývojové prostředí Java.

- Adresář dokumentů: Vytvořte adresář, kam chcete uložit 3D soubory, a poznamenejte si jeho cestu pro pozdější použití.

## Importujte balíčky

 Do svého projektu Java importujte potřebné balíčky pro práci s Aspose.3D. To zahrnuje`Scene` třída a různé třídy SaveOptions. Níže je uveden základní příklad:

```java
import com.aspose.threed.*;


import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

Nyní si každý příklad rozdělíme do několika kroků, abychom demonstrovali použití různých možností SaveOptions.

## Krok 1: Pretty Print v GLTF SaveOption

 The`prettyPrintInGltfSaveOption` umožňuje vygenerovat soubor GLTF s odsazeným obsahem JSON pro čitelnost pro člověka.

```java
public static void prettyPrintInGltfSaveOption() throws IOException {
    // Inicializujte 3D scénu
    Scene scene = new Scene(new Sphere());
    
    // Inicializujte GLTFSaveOptions
    GltfSaveOptions opt = new GltfSaveOptions(FileFormat.GLTF2);
    
    // Povolte pěkný tisk pro lepší čitelnost
    opt.setPrettyPrint(true);
    
    // Uložit 3D scénu
    scene.save("Your Document Directory" + "prettyPrintInGltfSaveOption.gltf", opt);
}
```

## Krok 2: HTML5 SaveOption

 The`html5SaveOption` metoda ukazuje, jak uložit 3D scénu jako soubor HTML5, včetně možností přizpůsobení.

```java
public static void html5SaveOption() throws IOException {
    // Inicializujte scénu
    Scene scene = new Scene();
    
    // Vytvořte podřízený uzel s válcem
    Node node = scene.getRootNode().createChildNode(new Cylinder());
    
    //Nastavte vlastnosti pro podřízený uzel
    LambertMaterial mat = new LambertMaterial();
    mat.setDiffuseColor(new Vector3(0.34, 0.59, 0.41));
    node.setMaterial(mat);
    
    // Přidejte do scény světlo
    Light light = new Light();
    light.setLightType(LightType.POINT);
    scene.getRootNode().createChildNode(light).getTransform().setTranslation(10, 0, 10);
    
    // Inicializujte HTML5SaveOptions
    Html5SaveOptions opt = new Html5SaveOptions();
    
    // Přizpůsobit možnosti (např. vypnout mřížku a uživatelské rozhraní)
    opt.setShowGrid(false);
    opt.setShowUI(false);
    
    // Uložte scénu jako soubor HTML5
    scene.save("Your Document Directory" + "html5SaveOption.html", FileFormat.HTML5);
}
```

 Pokračujte podobným rozdělením pro další metody SaveOptions, jako je např`colladaSaveOption`, `discreet3DSSaveOption`, `fbxSaveOption`, `objSaveOption`, `STLSaveOption`, `U3DSaveOption`, `glTFSaveOptions` , a`drcSaveOptions`.

## Závěr

Sledováním tohoto komplexního tutoriálu jste se naučili, jak optimalizovat ukládání 3D souborů v Javě pomocí Aspose.3D SaveOptions. Ať už vás zajímá pěkný tisk souborů GLTF nebo přizpůsobení výstupů HTML5, Aspose.3D vás vybaví nástroji pro vylepšení vašeho pracovního postupu 3D grafiky.

## FAQ

### Q1: Jak mohu vložit podklady do souboru glTF?

 A1: Chcete-li vložit položky, použijte`setEmbedAssets(true)` metoda v`GltfSaveOptions` třída.

###  Q2: Jaký je účel`setPositionBits` method in `DracoSaveOptions`?

 A2:`setPositionBits` metoda nastavuje kvantizační bity pro pozici v kompresním algoritmu Draco.

### Q3: Mohu exportovat normální data do souboru U3D?

 A3: Ano, můžete exportovat normální data nastavením`setExportNormals(true)` v`U3dSaveOptions` třída.

### Q4: Jak zruším ukládání souborů materiálu v exportu OBJ?

A4: Využijte`setFileSystem(new DummyFileSystem())` metoda v`ObjSaveOptions` třídy vyřadit soubory materiálu.

### Q5: Existuje způsob, jak uložit závislosti do místního adresáře v souboru OBJ?

 A5: Ano, použijte`setFileSystem(new LocalFileSystem(MyDir))` metoda v`ObjSaveOptions` třída pro místní uložení závislostí.