---
title: Vytvoření ventilátorového válce
linktitle: Vytvoření ventilátorového válce
second_title: Aspose.3D .NET API
description: Odemkněte svět 3D designu s Aspose.3D pro .NET! Vytvářejte úžasné válce s ventilátorem a bez ventilátoru bez námahy. Stáhněte si zkušební verzi.
type: docs
weight: 10
url: /cs/net/working-with-cylinder/create-fan-cylinder/
---
## Úvod
Vítejte ve světě 3D modelování a vizualizace s Aspose.3D pro .NET! V tomto podrobném průvodci prozkoumáme, jak vytvořit podmanivý válec ventilátoru pomocí Aspose.3D pro .NET. Aspose.3D je výkonná knihovna, která poskytuje rozsáhlé možnosti pro práci s 3D obsahem v aplikacích .NET.
## Předpoklady
Než se ponoříme do vzrušujícího světa 3D modelování, ujistěte se, že máte následující předpoklady:
- Základní znalost programování .NET.
- Visual Studio nainstalované na vašem počítači.
-  Aspose.3D for .NET knihovna, kterou si můžete stáhnout[tady](https://releases.aspose.com/3d/net/).
- Skutečný zájem o uvolnění vaší kreativity prostřednictvím 3D designu.
## Importovat jmenné prostory
Začněme tím, že naimportujeme potřebné jmenné prostory, aby byla funkce Aspose.3D dostupná ve vašem projektu .NET.
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
// Importujte jmenné prostory Aspose.3D
```
Nyní, když jsme vše připraveni, pojďme si rozdělit proces vytváření ventilátorového válce na zvládnutelné kroky.
## Krok 1: Vytvořte scénu
```csharp
// Vytvořte scénu
Scene scene = new Scene();
```
Začněte inicializací nové 3D scény. To slouží jako plátno, kde náš válec ventilátoru ožije.
## Krok 2: Vytvořte ventilátorový válec
```csharp
// Vytvořte válec
var fan = new Cylinder(2, 2, 10, 20, 1, false);
```
Definujte vlastnosti válce ventilátoru a určete parametry, jako je poloměr, výška a rozlišení.
## Krok 3: Přizpůsobte vlastnosti ventilátorového válce
```csharp
// Nastavte GenerateFanCylinder na true
fan.GenerateFanCylinder = true;
// Nastavte ThetaLength
fan.ThetaLength = MathUtils.ToRadian(270);
```
Přizpůsobte si válec ventilátoru povolením generování části ventilátoru a úpravou úhlového vychýlení pomocí ThetaLength.
## Krok 4: Umístěte ventilátorový válec do scény
```csharp
// Vytvořte ChildNode
scene.RootNode.CreateChildNode(fan).Transform.Translation = new Vector3(10, 0, 0);
```
Přidejte válec vějíře jako podřízený uzel do kořenového uzlu scény a umístěte jej do 3D prostoru.
## Krok 5: Vytvořte válec bez ventilátoru
```csharp
// Vytvořte válec bez ventilátoru
var nonfan = new Cylinder(2, 2, 10, 20, 1, false);
```
Prozkoumejte flexibilitu Aspose.3D vytvořením válce bez ventilátorové části.
## Krok 6: Přizpůsobte vlastnosti válce bez ventilátoru
```csharp
// Nastavte GenerateFanCylinder na hodnotu false
nonfan.GenerateFanCylinder = false;
// Nastavte ThetaLength
nonfan.ThetaLength = MathUtils.ToRadian(270);
```
Rozlište neventilátorový válec vypnutím generování ventilátorové části.
## Krok 7: Umístěte válec bez ventilátoru do scény
```csharp
// Vytvořte ChildNode
scene.RootNode.CreateChildNode(nonfan);
```
Podobně přidejte válec bez vějíře jako podřízený uzel do kořenového uzlu scény.
## Krok 8: Uložte scénu
```csharp
// Uložit scénu
scene.Save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WavefrontOBJ);
```
Uložte své mistrovské dílo v požadovaném formátu a umístění. Nyní jste úspěšně vytvořili vějířový a neventilátorový válec pomocí Aspose.3D pro .NET!
## Závěr
Gratulujeme k dokončení tohoto praktického průvodce 3D modelováním pomocí Aspose.3D pro .NET! Popustili jste uzdu své kreativitě v digitální sféře, s lehkostí vyrábíte válce s ventilátorem i bez ventilátoru.
## Často kladené otázky
### Mohu použít Aspose.3D pro .NET s jinými frameworky .NET?
Ano, Aspose.3D je kompatibilní s různými .NET frameworky a poskytuje všestrannost ve vašich vývojových projektech.
### Je k dispozici bezplatná zkušební verze pro Aspose.3D pro .NET?
 Ano, můžete vyzkoušet bezplatnou zkušební verzi[tady](https://releases.aspose.com/).
### Kde najdu podrobnou dokumentaci k Aspose.3D pro .NET?
 Dokumentace je k dispozici[tady](https://reference.aspose.com/3d/net/).
### Jak mohu získat podporu pro Aspose.3D pro .NET?
 Navštivte fórum podpory[tady](https://forum.aspose.com/c/3d/18)za pomoc od komunity a odborníků Aspose.
### Jsou pro Aspose.3D pro .NET dostupné dočasné licence?
 Ano, dočasné licence lze získat[tady](https://purchase.aspose.com/temporary-license/).