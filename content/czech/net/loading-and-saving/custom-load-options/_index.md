---
title: Vlastní možnosti načítání
linktitle: Vlastní možnosti načítání
second_title: Aspose.3D .NET API
description: Prozkoumejte Aspose.3D for .NET, dokonalé řešení pro bezproblémové načítání a ukládání 3D modelů.
type: docs
weight: 15
url: /cs/net/loading-and-saving/custom-load-options/
---
## Úvod

Vítejte ve světě Aspose.3D for .NET – výkonné knihovny, která umožňuje vývojářům bezproblémově pracovat s 3D soubory. V tomto tutoriálu se ponoříme do složitosti načítání a ukládání 3D modelů a zaměříme se na vlastní možnosti načítání. Ať už jste zkušený vývojář nebo nováček, tento průvodce vás provede procesem krok za krokem a zajistí, že využijete plný potenciál Aspose.3D pro .NET.

## Předpoklady

Než se vydáme na tuto cestu, ujistěte se, že máte splněny následující předpoklady:

-  Aspose.3D for .NET: Ujistěte se, že máte nainstalovanou knihovnu. Můžete si jej stáhnout[tady](https://releases.aspose.com/3d/net/).

- Adresář dokumentů: Vytvořte adresář pro ukládání souborů 3D modelů.

Nyní, když máte to podstatné, pojďme se ponořit do vzrušujícího světa manipulace s 3D modely!

## Importovat jmenné prostory

Nejprve importujme potřebné jmenné prostory. To připraví půdu pro naši cestu do říše Aspose.3D.

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
```

## Načítání a ukládání – vlastní možnosti načítání

### Krok 1: Načtení souborů Discreet3DS

```csharp
private static void Discreet3DSLoadOption()
{
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();

    //Nastavte vlastní možnosti
    loadOpts.ApplyAnimationTransform = true;
    loadOpts.FlipCoordinateSystem = true;
    loadOpts.GammaCorrectedColor = true;
    loadOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Načíst soubor s možnostmi načtení
    var scene = Scene.FromFile("test.3ds", loadOpts);
}
```

### Krok 2: Načtení souborů OBJ

```csharp
private static void ObjLoadOption()
{
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();

    //Nastavte vlastní možnosti
    loadObjOpts.EnableMaterials = true;
    loadObjOpts.FlipCoordinateSystem = true;
    loadObjOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Načíst soubor s možnostmi načtení
    var scene = Scene.FromFile("test.obj", loadObjOpts);

}
```

### Krok 3: Načtení souborů STL

```csharp
private static void STLLoadOption()
{
    // Cesta k adresáři dokumentů.
    StlLoadOptions loadSTLOpts = new StlLoadOptions();

    //Nastavte vlastní možnosti
    loadSTLOpts.FlipCoordinateSystem = true;
    loadSTLOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Načíst soubor s možnostmi načtení
    var scene = Scene.FromFile("test.stl", loadSTLOpts);
}
```

### Krok 4: Načtení souborů U3D

```csharp
private static void U3DLoadOption()
{
    // Cesta k adresáři dokumentů.
    string dataDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();

    //Nastavte vlastní možnosti
    loadU3DOpts.FlipCoordinateSystem = true;
    loadU3DOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Načíst soubor s možnostmi načtení
    var scene = Scene.FromFile("test.u3d", loadU3DOpts);
}
```

### Krok 5: Načtení souborů glTF

```csharp
private static void glTFLoadOptions()
{
    // Cesta k adresáři dokumentů.
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();

    //Nastavte vlastní možnosti
    loadOpt.FlipTexCoordV = true;
    scene.Open("Duck.gltf", loadOpt);
}
```

### Krok 6: Načtení souborů PLY

```csharp
private static void PlyLoadOptions()
{
    // Cesta k adresáři dokumentů.
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();

    //Nastavte vlastní možnosti
    loadPLYOpts.FlipCoordinateSystem = true;
    scene.Open("vase-v2.ply", loadPLYOpts);
}
```

### Krok 7: Načtení souborů FBX

```csharp
private static void FBXLoadOptions()
{
    // Cesta k adresáři dokumentů.
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions() { KeepBuiltinGlobalSettings = true };

    //Nastavte vlastní možnosti
    scene.Open("test.FBX", opt);

    // Vlastnosti výstupu definované v GlobalSettings v souboru FBX
    foreach (Property property in scene.RootNode.AssetInfo.Properties)
    {
        Console.WriteLine(property);
    }
}
```

## Závěr

Gratulujeme! Úspěšně jste prošli složitým světem načítání a ukládání 3D modelů pomocí Aspose.3D for .NET. Tento výukový program se zabýval různými formáty souborů a jejich vlastními možnostmi načítání, což vám umožňuje snadno manipulovat s 3D prvky.

## FAQ

### Q1: Je Aspose.3D for .NET vhodný pro začátečníky?

A1: Rozhodně! Aspose.3D for .NET poskytuje uživatelsky přívětivé rozhraní, takže je přístupné pro vývojáře všech úrovní.

### Q2: Mohu použít Aspose.3D pro komerční projekty?

Odpověď 2: Ano, Aspose.3D for .NET je dodáván s komerční licencí, která vám umožňuje používat jej ve vašich projektech.

### Otázka 3: Existují nějaká omezení podporovaných formátů souborů?

 Odpověď 3: Aspose.3D for .NET podporuje širokou škálu oblíbených 3D formátů souborů, včetně OBJ, STL, FBX a dalších. Odkazovat na[dokumentace](https://reference.aspose.com/3d/net/) pro úplný seznam.

### Q4: Je k dispozici zkušební verze?

A4: Ano, můžete prozkoumat možnosti Aspose.3D pro .NET stažením souboru[zkušební verze zdarma](https://releases.aspose.com/).

### Q5: Kde mohu hledat podporu pro Aspose.3D pro .NET?

 A5: Navštivte[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) za podporu a pomoc komunity.