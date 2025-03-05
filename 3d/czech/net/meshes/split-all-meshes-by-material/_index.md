---
title: Rozdělení všech sítí scény podle materiálu
linktitle: Rozdělení všech sítí scény podle materiálu
second_title: Aspose.3D .NET API
description: Naučte se, jak rozdělit 3D sítě podle materiálu pomocí Aspose.3D for .NET. Postupujte podle našeho podrobného průvodce pro efektivní organizaci a správu 3D modelů.
type: docs
weight: 21
url: /cs/net/meshes/split-all-meshes-by-material/
---
## Úvod
Vítejte v tomto podrobném průvodci o rozdělení všech sítí 3D scény podle materiálu pomocí Aspose.3D for .NET. Pokud pracujete s 3D modely a chcete efektivně organizovat sítě na základě materiálů, je tento výukový program právě pro vás. Aspose.3D je výkonná knihovna .NET, která poskytuje řadu funkcí pro práci s 3D soubory, což z ní činí vynikající volbu pro vývojáře.
## Předpoklady
Než se pustíte do výukového programu, ujistěte se, že máte následující předpoklady:
- Základní znalost programovacího jazyka C#.
- Visual Studio nainstalované na vašem počítači.
-  Aspose.3D pro knihovnu .NET. Můžete si jej stáhnout z[tady](https://releases.aspose.com/3d/net/).
- Vstupní 3D soubor (například „test.fbx“), který chcete rozdělit.
## Importovat jmenné prostory
Začněte importováním potřebných jmenných prostorů do vašeho projektu C#:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```
## Krok 1: Načtěte 3D soubor
```csharp
// Cesta k adresáři dokumentů.
string input = RunExamples.GetDataFilePath("test.fbx");
// Načtěte 3D soubor
Scene scene = new Scene(input);
```
 V tomto kroku načteme 3D soubor pomocí Aspose.3D's`Scene` třída.
## Krok 2: Rozdělte všechny sítě
```csharp
// Rozdělte všechny sítě
PolygonModifier.SplitMesh(scene, SplitMeshPolicy.CloneData);
```
 Zde používáme`SplitMesh` metoda z`PolygonModifier` třídy rozdělit všechny sítě na základě materiálu.
## Krok 3: Uložte rozdělenou scénu
```csharp
// Uložení souboru
var output = "Your Output Directory" + "test-splitted.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```
Uložte upravenou scénu do nového souboru, abyste zachovali změny.
## Krok 4: Zobrazte zprávu o úspěchu
```csharp
// Zobrazit zprávu o úspěchu
Console.WriteLine("\nSplitting all meshes of a scene per material successfully.\nFile saved at " + output);
```
Vytiskněte zprávu o úspěchu oznamující, že operace byla úspěšně dokončena.
## Závěr
Gratulujeme! Úspěšně jste se naučili, jak rozdělit všechny sítě 3D scény podle materiálu pomocí Aspose.3D for .NET. To může být cenná technika pro organizaci a správu složitých 3D modelů.
## Nejčastější dotazy
### 1. Mohu používat Aspose.3D pro .NET s jinými programovacími jazyky?
Aspose.3D je primárně navržen pro .NET, ale poskytuje interoperabilitu s jinými jazyky prostřednictvím jazykových vazeb .NET.
### 2. Je k dispozici zkušební verze?
 Ano, máte přístup k bezplatné zkušební verzi[tady](https://releases.aspose.com/).
### 3. Kde najdu další příklady a dokumentaci?
 Prozkoumejte komplexní dokumentaci na[Aspose.3D dokumentace](https://reference.aspose.com/3d/net/).
### 4. Jak mohu získat podporu pro Aspose.3D?
 Navštivte[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) za podporu komunity a diskuze.
### 5. Mohu získat dočasnou licenci?
 Ano, můžete získat dočasnou licenci[tady](https://purchase.aspose.com/temporary-license/).