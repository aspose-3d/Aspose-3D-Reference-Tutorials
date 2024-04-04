---
title: Vlastní možnosti uložení
linktitle: Vlastní možnosti uložení
second_title: Aspose.3D .NET API
description: Prozkoumejte sílu Aspose.3D pro .NET. Naučte se, jak přizpůsobit ukládání 3D scény pomocí podrobných průvodců ve formátech Collada, USD, 3DS, FBX, OBJ, STL, U3D, glTF, DRC a RVM.
type: docs
weight: 21
url: /cs/net/loading-and-saving/custom-save-options/
---
## Úvod

Vítejte ve světě Aspose.3D pro .NET! Pokud chcete vylepšit své možnosti 3D vývoje, jste na správném místě. V tomto tutoriálu se ponoříme do funkcí Načítání a Ukládání, konkrétně se zaměříme na Vlastní možnosti ukládání. Aspose.3D for .NET je výkonná knihovna, která umožňuje vývojářům efektivně manipulovat a ukládat 3D scény.

## Předpoklady

Než začneme zkoumat vzrušující funkce Aspose.3D, ujistěte se, že máte následující předpoklady:

- Základní znalost vývoje C# a .NET.
-  Nainstalovaná knihovna Aspose.3D for .NET. Můžete si jej stáhnout z[stránka vydání](https://releases.aspose.com/3d/net/).
- Vývojové prostředí nastavené pomocí sady Visual Studio nebo jakéhokoli jiného preferovaného IDE C#.

## Importovat jmenné prostory

Chcete-li začít, importujme potřebné jmenné prostory:

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose.ThreeD.Shading;
using System.Drawing;
```

Nyní, když jsme připravili scénu, rozdělme tutoriál do několika kroků.

## Krok 1: Možnost Collada Save

Začněme Collada, populárním 3D formátem souborů. Chcete-li přizpůsobit možnosti ukládání Collada, postupujte takto:

### 1. Nastavení adresáře:
   ```csharp
   string dataDir = "Your Document Directory";
   ```

### 2. Inicializujte možnosti ukládání Collada:
   ```csharp
   ColladaSaveOptions saveColladaOpts = new ColladaSaveOptions();
   ```

### 3. Konfigurace možností:
   ```csharp
   saveColladaOpts.Indented = true;
   saveColladaOpts.TransformStyle = ColladaTransformStyle.Matrix;
   saveColladaOpts.LookupPaths = new List<string>(new string[] { dataDir });
   ```

## Krok 2: Diskrétní možnost uložení 3DS

Nyní se podívejme na Discreet 3DS a jeho možnosti přizpůsobení:

### 1. Nastavení adresáře:
   ```csharp
   string dataDir = "Your Document Directory";
   ```

### 2. Inicializujte možnosti uložení 3DS:
   ```csharp
   Discreet3dsSaveOptions saveOpts = new Discreet3dsSaveOptions();
   ```

### 3. Konfigurace možností:
   ```csharp
   saveOpts.DuplicatedNameCounterBase = 2;
   // Další možnosti konfigurace...
   ```

Pokračujte v tomto podrobném přístupu k možnostem uložení FBX, OBJ, STL, U3D, glTF a DRC a každou si přizpůsobte podle svých požadavků.

## Krok 3: Možnosti uložení glTF

Nyní se zaměřme na glTF, formát široce používaný ve webových a mobilních aplikacích. Přizpůsobte si možnosti ukládání glTF pomocí těchto kroků:

### 1. Inicializujte objekt scény:
   ```csharp
   Scene scene = new Scene();
   scene.RootNode.CreateChildNode("sphere", new Sphere());
   ```

### 2. Nastavte možnosti ukládání glTF:
   ```csharp
   GltfSaveOptions opt = new GltfSaveOptions(FileContentType.ASCII);
   opt.EmbedAssets = true;
   opt.UseCommonMaterials = true;
   opt.BufferFile = "mybuf.bin";
   ```

### 3. Uložte soubor glTF:
   ```csharp
   scene.Save("Your Output Directory" + "glTFSaveOptions_out.gltf", opt);
   ```

Podobnou strukturu použijte pro další možnosti ukládání, jako je DRC a RVM.

## Závěr

Gratulujeme! Úspěšně jste prozkoumali vlastní možnosti ukládání v Aspose.3D pro .NET. Tato výkonná knihovna poskytuje nespočet možností, jak přizpůsobit proces ukládání 3D scény.

## FAQ

### Q1: Mohu použít Aspose.3D pro .NET s jinými frameworky .NET?

A1: Ano, Aspose.3D je kompatibilní s různými .NET frameworky, což zajišťuje flexibilitu ve vašem vývojovém prostředí.

### Q2: Jsou nějaké možnosti licencování dostupné pro Aspose.3D?

 A2: Ano, můžete prozkoumat možnosti licencování[tady](https://purchase.aspose.com/buy).

### Q3: Kde najdu podporu pro dotazy související s Aspose.3D?

 A3: Můžete hledat podporu na[Aspose.3D fórum](https://forum.aspose.com/c/3d/18).

### Q4: Je k dispozici bezplatná zkušební verze?

 A4: Ano, máte přístup k bezplatné zkušební verzi[tady](https://releases.aspose.com/).

### Q5: Jak mohu získat dočasnou licenci pro Aspose.3D?

 A5: Získejte dočasnou licenci[tady](https://purchase.aspose.com/temporary-license/).