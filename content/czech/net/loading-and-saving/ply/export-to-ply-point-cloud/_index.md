---
title: Export do formátu PLY jako mrak bodů
linktitle: Export do formátu PLY jako mrak bodů
second_title: Aspose.3D .NET API
description: Prozkoumejte svět 3D modelování s Aspose.3D pro .NET. Naučte se exportovat modely do formátu PLY bez námahy. Pozvedněte své projekty pomocí ohromujících vizuálů.
type: docs
weight: 16
url: /cs/net/loading-and-saving/ply/export-to-ply-point-cloud/
---
## Úvod
dynamickém světě 3D modelování a vývoje vyniká Aspose.3D for .NET jako výkonná sada nástrojů. Tento tutoriál vás provede procesem exportu 3D modelů do formátu PLY jako mračna bodů pomocí Aspose.3D for .NET. Pokud jste připraveni vylepšit své projekty ohromujícími vizuálními prvky, postupujte podle nich a odemkněte plný potenciál této všestranné knihovny.
## Předpoklady
Než se ponoříte do výukového programu, ujistěte se, že máte splněny následující předpoklady:
-  Aspose.3D for .NET: Stáhněte a nainstalujte knihovnu z[stránka ke stažení](https://releases.aspose.com/3d/net/).
- Vývojové prostředí: Nastavte si preferované vývojové prostředí .NET, jako je Visual Studio.
## Importovat jmenné prostory
Chcete-li začít s Aspose.3D pro .NET, importujte do svého projektu potřebné jmenné prostory:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```
## Krok 1: Vytvořte 3D model
Začněte vytvořením 3D modelu, který chcete exportovat jako mračno bodů. Vytvořme například kouli:
```csharp
Sphere sphere = new Sphere();
```
## Krok 2: Definujte nastavení exportu
Zadejte nastavení exportu, včetně formátu souboru (PLY) a povolte export do mračna bodů:
```csharp
PlySaveOptions saveOptions = new PlySaveOptions() { PointCloud = true };
```
## Krok 3: Nastavte cestu exportu
Určete adresář, kam chcete uložit exportovaný soubor PLY:
```csharp
string exportPath = "Your Document Directory" + "sphere.ply";
```
## Krok 4: Kódování a export
 Využijte`Encode` způsob exportu 3D modelu do formátu PLY:
```csharp
FileFormat.PLY.Encode(sphere, exportPath, saveOptions);
```
## Závěr
Gratulujeme! Úspěšně jste exportovali 3D model do formátu PLY jako mračno bodů pomocí Aspose.3D for .NET. To otevírá nekonečné možnosti pro integraci pohlcujících vizuálů do vašich aplikací.

## Nejčastější dotazy
### 1. Je Aspose.3D kompatibilní se všemi .NET frameworky?
Aspose.3D podporuje různé .NET frameworky, což zajišťuje kompatibilitu v celé řadě vývojových prostředí.
### 2. Mohu použít Aspose.3D pro komerční projekty?
 Absolutně! Aspose.3D nabízí flexibilní možnosti licencování, včetně komerčního využití. Podívejte se na[nákupní stránku](https://purchase.aspose.com/buy) pro detaily.
### 3. Jak mohu získat podporu pro Aspose.3D?
 Navštivte[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) spojit se s komunitou a získat pomoc od odborníků.
### 4. Je k dispozici bezplatná zkušební verze?
 Ano, prozkoumejte funkce pomocí a[zkušební verze zdarma](https://releases.aspose.com/) před přijetím závazku.
### 5. Jak získám dočasnou licenci?
 Pro dočasné licenční možnosti navštivte[tento odkaz](https://purchase.aspose.com/temporary-license/).