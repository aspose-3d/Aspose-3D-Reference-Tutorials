---
title: Přizpůsobený ofsetový horní válec
linktitle: Přizpůsobený ofsetový horní válec
second_title: Aspose.3D .NET API
description: Prozkoumejte zázraky 3D grafiky s Aspose.3D pro .NET. Naučte se bez námahy vytvářet přizpůsobené ofsetové horní válce. Vylepšete své zkušenosti s kódováním hned teď!
type: docs
weight: 11
url: /cs/net/working-with-cylinder/customized-offset-top-cylinder/
---
## Úvod
Vítejte ve světě manipulace s 3D grafikou s Aspose.3D pro .NET! V tomto tutoriálu vás provedeme procesem vytváření přizpůsobeného ofsetového horního válce pomocí Aspose.3D, výkonné knihovny pro práci s 3D scénami, objekty a formáty v aplikacích .NET.
## Předpoklady
Než se pustíme do výukového programu, ujistěte se, že máte následující předpoklady:
- Základní znalost programovacího jazyka C#.
- Visual Studio nainstalované na vašem počítači.
- Knihovna Aspose.3D for .NET stažená a odkazovaná ve vašem projektu.
Nyní začněme s průvodcem krok za krokem!
## Importovat jmenné prostory
Nejprve se ujistěte, že jste do kódu C# importovali potřebné jmenné prostory:
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
```csharp
// Vytvořte scénu
Scene scene = new Scene();
```
Tím se inicializuje nová 3D scéna pomocí Aspose.3D.
## Krok 2: Inicializujte válec
```csharp
// Inicializujte válec
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
Zde vytvoříme válec se specifickými parametry, jako je poloměr, výška a řezy.
## Krok 3: Nastavte OffsetTop pro první válec
```csharp
// Nastavte OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```
Tím se nastaví přizpůsobený ofsetový vrchol pro první válec.
## Krok 4: Vytvořte ChildNode pro první válec
```csharp
// Vytvořte ChildNode
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
Do scény přidáme první válec jako podřízený uzel a upravíme jeho polohu.
## Krok 5: Inicializujte druhý válec
```csharp
//Inicializujte druhý válec bez přizpůsobeného OffsetTop
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
Druhý válec je inicializován bez přizpůsobené odsazené horní části.
## Krok 6: Vytvořte ChildNode pro druhý válec
```csharp
// Vytvořte ChildNode
scene.RootNode.CreateChildNode(cylinder2);
```
Druhý válec přidáme jako podřízený uzel do scény.
## Krok 7: Uložte scénu
```csharp
// Uložit
scene.Save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WavefrontOBJ);
```
Tím se uloží 3D scéna, včetně přizpůsobeného ofsetového horního válce, ve formátu Wavefront OBJ.
Nyní jste úspěšně vytvořili přizpůsobený ofsetový horní válec pomocí Aspose.3D pro .NET!
## Závěr
V tomto tutoriálu jsme prozkoumali základy práce s Aspose.3D pro .NET, abychom vytvořili přizpůsobený ofsetový horní válec. Tato knihovna otevírá nekonečné možnosti pro manipulaci s 3D grafikou ve vašich aplikacích .NET.
## Nejčastější dotazy
### Otázka: Kde najdu dokumentaci k Aspose.3D pro .NET?
 Odpověď: Dokumentace je k dispozici[tady](https://reference.aspose.com/3d/net/).
### Otázka: Jak si mohu stáhnout Aspose.3D pro .NET?
 A: Můžete si to stáhnout[tady](https://releases.aspose.com/3d/net/).
### Otázka: Je k dispozici bezplatná zkušební verze pro Aspose.3D pro .NET?
 Odpověď: Ano, můžete získat bezplatnou zkušební verzi[tady](https://releases.aspose.com/).
### Otázka: Kde mohu získat podporu pro Aspose.3D pro .NET?
 A: Navštivte[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) pro podporu.
### Otázka: Mohu získat dočasnou licenci pro Aspose.3D pro .NET?
 Odpověď: Ano, můžete získat dočasnou licenci[tady](https://purchase.aspose.com/temporary-license/).