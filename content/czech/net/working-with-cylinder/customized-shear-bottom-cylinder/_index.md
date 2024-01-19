---
title: Přizpůsobený smykový spodní válec
linktitle: Přizpůsobený smykový spodní válec
second_title: Aspose.3D .NET API
description: Naučte se vytvářet přizpůsobené smykové spodní válce pomocí Aspose.3D for .NET s naším podrobným průvodcem krok za krokem. Zvyšte své dovednosti v oblasti 3D modelování ještě dnes!
type: docs
weight: 12
url: /cs/net/working-with-cylinder/customized-shear-bottom-cylinder/
---
## Úvod
Vítejte v našem komplexním průvodci vytvářením přizpůsobeného spodního válce smyku pomocí Aspose.3D pro .NET. Pokud chcete zlepšit své dovednosti v oblasti 3D modelování a přidat do svých projektů jedinečné funkce, jste na správném místě. V tomto tutoriálu vás provedeme procesem krok za krokem pomocí jasných vysvětlení a úryvků kódu.
## Předpoklady
Než se pustíme do výukového programu, ujistěte se, že máte následující:
- Základní znalost programování v C# a .NET.
-  Nainstalovaná knihovna Aspose.3D for .NET. Můžete si jej stáhnout[tady](https://releases.aspose.com/3d/net/).
- Vývojové prostředí nastavené pro programování .NET.
## Importovat jmenné prostory
kódu C# začněte importováním potřebných jmenných prostorů:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```
## Krok 1: Vytvořte scénu
Začněte vytvořením 3D scény pomocí Aspose.3D:
```csharp
Scene scene = new Scene();
```
## Krok 2: Vytvořte válec 1
Vygenerujte první válec a nastavte jeho vlastnosti:
```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
## Krok 3: Přizpůsobte smykové dno pro válec 1
Na první válec aplikujte přizpůsobené smykové dno:
```csharp
cylinder1.ShearBottom = new Vector2(0, 0.83); // Smyk 47,5 stupně v rovině xy (osa z)
```
## Krok 4: Přidejte válec 1 do scény
Přidejte do scény první válec a nastavte jeho překlad:
```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
## Krok 5: Vytvořte válec 2
Vygenerujte druhý válec s podobnými vlastnostmi:
```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
## Krok 6: Přidejte válec 2 do scény
Přidejte druhý válec do scény bez smykového dna:
```csharp
scene.RootNode.CreateChildNode(cylinder2);
```
## Krok 7: Uložte scénu
Uložte scénu jako soubor Wavefront OBJ do adresáře dokumentů:
```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```
## Závěr
Gratulujeme! Úspěšně jste vytvořili přizpůsobený smykový spodní válec pomocí Aspose.3D pro .NET. Tento tutoriál si kladl za cíl poskytnout průvodce krok za krokem pro uživatele s různou úrovní odborných znalostí v oblasti 3D modelování a programování.
## Často kladené otázky
### Je Aspose.3D for .NET vhodný pro začátečníky?
Absolutně! Aspose.3D for .NET nabízí uživatelsky přívětivé rozhraní, díky kterému je přístupné začátečníkům i zkušeným vývojářům.
### Mohu na válce použít různé úhly střihu?
Ano, spodní část nůžek můžete přizpůsobit pro každý válec individuálně, což vám umožní dosáhnout jedinečných efektů.
### Je k dispozici zkušební verze?
 Ano, můžete prozkoumat bezplatnou zkušební verzi[tady](https://releases.aspose.com/).
### Kde najdu další podporu?
 Navštivte[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) za podporu komunity a diskuze.
### Jak mohu získat dočasnou licenci?
 Získejte dočasnou licenci[tady](https://purchase.aspose.com/temporary-license/).