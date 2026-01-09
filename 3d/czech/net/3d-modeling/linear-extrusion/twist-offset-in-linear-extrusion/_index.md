---
date: 2026-01-09
description: Naučte se, jak vytvořit 3D scénu pomocí Aspose.3D pro .NET, včetně exportu
  do formátu Wavefront OBJ a jak zkroucení offsetu v lineární extruzi.
linktitle: Twist Offset in Linear Extrusion
second_title: Aspose.3D .NET API
title: Jak vytvořit 3D scénu s otočným posunem při lineárním extrudování
url: /cs/net/3d-modeling/linear-extrusion/twist-offset-in-linear-extrusion/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Vytvoření 3D scény: Twist Offset v lineárním extruzi

## Úvod

Pokud potřebujete **rychle vytvořit 3d scénu** objektů a přidat dynamickou geometrii, Aspose.3D pro .NET vám poskytne přesně ty nástroje, které potřebujete. V tomto **Aspose 3D tutoriálu** projdeme techniku *jak otočit offset* při provádění **lineárního extruze twistu** a nakonec **exportujeme soubory Wavefront OBJ**. Na konci budete mít plně vybavený 3‑D model připravený k renderování nebo dalšímu zpracování.

## Rychlé odpovědi
- **Co dělá “twist offset”?** Posouvá počáteční bod twistu podél osy extruze.  
- **Která metoda exportuje Wavefront OBJ?** `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Potřebuji licenci pro spuštění ukázky?** Dočasná licence stačí pro testování; pro produkci je vyžadována plná licence.  
- **Jaké verze .NET jsou podporovány?** .NET Framework 4.5+, .NET Core 3.1+, .NET 5/6+.  
- **Kolik řezů se doporučuje pro plynulé twisty?** Přibližně 100 řezů poskytuje dobrý poměr mezi kvalitou a výkonem.

## Co je **create 3d scene**?

Vytvoření 3‑D scény znamená postavit hierarchickou strukturu, která obsahuje geometrii, světla, kamery a transformace. Aspose.3D poskytuje třídu `Scene`, která funguje jako kořenový kontejner pro všechny uzly, které přidáte.

## Proč použít **linear extrusion twist**?

Lineární extruze s twistem vám umožní převést 2‑D profil na spirálový 3‑D objekt — ideální pro šrouby, pružiny nebo dekorativní sloupy. Přidání twist offsetu vám dává ještě větší kontrolu nad začátkem rotace, což umožňuje asymetrické návrhy.

## Předpoklady

Než se pustíme do práce, ujistěte se, že máte:

- Aspose.3D pro .NET knihovnu: Stáhněte a nainstalujte knihovnu ze [stránky vydání](https://releases.aspose.com/3d/net/).  
- Vývojové prostředí: Visual Studio 2022 (nebo jakékoli C# IDE) připravené pro .NET vývoj.

## Importujte jmenné prostory

Začněte importováním potřebných jmenných prostorů pro přístup k funkcím Aspose.3D.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Průvodce krok za krokem

### Krok 1: Inicializace základního profilu  

Použijeme obdélník s malým poloměrem zaoblení jako profil, který bude extrudován.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

### Krok 2: Vytvoření scény  

Toto je kontejner, kde **vytvoříme 3d scénu** uzly.

```csharp
Scene scene = new Scene();
```

### Krok 3: Vytvoření uzlů  

Do kořene jsou přidány dva sourozenecké uzly — jeden pro běžnou extruzi a jeden pro verzi s offsetem.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

### Krok 4: Lineární extruze na levém uzlu (základní twist)  

Zde demonstrujeme klasický **linear extrusion twist** bez jakéhokoli offsetu.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

### Krok 5: Lineární extruze na pravém uzlu s **Twist Offset**  

Nyní aplikujeme techniku **jak otočit offset** poskytnutím vektoru `TwistOffset`.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

### Krok 6: **Export Wavefront OBJ**  

Nakonec uložíme sestavenou scénu do OBJ souboru, abyste ji mohli zobrazit v libovolném standardním 3‑D prohlížeči.

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Časté problémy a tipy

- **Twist vypadá plochě?** Zvyšte hodnotu `Slices` pro hladší geometrii.  
- **Offset není viditelný?** Ujistěte se, že vektor `TwistOffset` není nulový a je zarovnán se směrem extruze.  
- **OBJ soubor postrádá textury?** OBJ ukládá jen geometrii; pro definice materiálů použijte soubory MTL, pokud jsou potřeba.

## Často kladené otázky

**Q: Můžu použít Aspose.3D pro .NET s jinými programovacími jazyky?**  
A: Aspose.3D primárně cílí na .NET jazyky, ale ekvivalentní knihovny existují pro Javu a další platformy.

**Q: Jak získám dočasnou licenci pro Aspose.3D pro .NET?**  
A: Navštivte [tento odkaz](https://purchase.aspose.com/temporary-license/) a získejte dočasnou licenci pro testovací účely.

**Q: Existuje komunitní fórum pro Aspose.3D pro .NET?**  
A: Rozhodně! Připojte se ke komunitě na [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) a komunikujte s ostatními vývojáři a hledejte pomoc.

**Q: Jsou k dispozici další příklady a dokumentace?**  
A: Prozkoumejte [dokumentaci](https://reference.aspose.com/3d/net/) pro rozsáhlé návody a příklady.

**Q: Kde si mohu zakoupit Aspose.3D pro .NET?**  
A: Přejděte na [tento odkaz](https://purchase.aspose.com/buy) a proveďte nákup, čímž odemknete plný potenciál Aspose.3D.

## Závěr

V tomto **aspose 3d tutoriálu** jste se naučili, jak **vytvořit 3d scénu**, aplikovat **linear extrusion twist**, ovládat **twist offset** a **exportovat Wavefront OBJ** soubory. Tyto techniky vám umožní přidat sofistikovanou, zkroucenou geometrii do jakéhokoli 3‑D projektu pomocí několika řádků kódu.

---

**Poslední aktualizace:** 2026-01-09  
**Testováno s:** Aspose.3D 24.11 pro .NET  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}