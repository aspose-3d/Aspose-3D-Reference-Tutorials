---
title: Zachycení výřezů ve 3D scénách
linktitle: Zachycení výřezů ve 3D scénách
second_title: Aspose.3D .NET API
description: Naučte se zachytit úžasné 3D výřezy pomocí Aspose.3D for .NET. Podrobný průvodce pro flexibilní vykreslování scén.
type: docs
weight: 11
url: /cs/net/3d-viewports/capture-viewport/
---
## Úvod

oblasti 3D grafiky a vizualizace je zachycení výřezů základní dovedností, která zvyšuje hloubku a detaily vašich scén. Aspose.3D for .NET poskytuje robustní řešení pro vykreslování a manipulaci s 3D scénami. Tento tutoriál vás provede procesem zachycení výřezů ve 3D scénách pomocí Aspose.3D, což vám umožní snadno vytvářet úžasné vizualizace.

## Předpoklady

Než se pustíte do výukového programu, ujistěte se, že máte splněny následující předpoklady:

-  Aspose.3D for .NET Library: Ujistěte se, že máte nainstalovanou knihovnu Aspose.3D. Můžete si jej stáhnout z[tady](https://releases.aspose.com/3d/net/).

## Importovat jmenné prostory

Chcete-li začít, importujte potřebné jmenné prostory do svého projektu .NET:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using System.Drawing;
using System.Drawing.Imaging;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
```

## Krok 1: Načtěte existující 3D scénu

Začněte načtením existující 3D scény do vašeho projektu. Následující fragment kódu to ukazuje:

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

## Krok 2: Vytvořte kameru

Dále vytvořte instanci kamery a nastavte její polohu a cíl:

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

## Krok 3: Přidejte do scény osvětlení

Vylepšete svou scénu přidáním zdroje světla. Níže uvedený fragment kódu ukazuje, jak vytvořit bodové světlo:

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

## Krok 4: Nakonfigurujte Renderer a Render Target

Nastavte vykreslovací modul a vytvořte cíl vykreslení pro zachycení scény:

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    renderer.EnableShadows = false;

    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // ... (pokračování v dalších krocích)
    }
}
```

## Krok 5: Definujte výřezy a vykreslení

Definujte výřezy a vykreslete scénu pro generování výstupních obrázků:

```csharp
Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-1viewports_out.png", ImageFormat.Png);
```

## Krok 6: Upravte výřezy a znovu vykreslete

Upravte výřezy a vykreslete scénu ještě jednou, což demonstruje flexibilitu Aspose.3D:

```csharp
vp.Area = new RelativeRectangle() { ScaleWidth = 0.5f, ScaleHeight = 1 };
rt.CreateViewport(camera, new RelativeRectangle() { ScaleX = 0.5f, ScaleWidth = 0.5f, ScaleHeight = 1 });
camera.FieldOfView = 90;
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-2viewports_out.png", ImageFormat.Png);
```

Pokračujte v experimentování s různými konfiguracemi, abyste dosáhli požadovaných vizuálních efektů.

## Závěr

V tomto tutoriálu jsme prozkoumali proces zachycování výřezů ve 3D scénách pomocí Aspose.3D for .NET. Využitím jeho výkonných funkcí můžete pozvednout své 3D grafické projekty do nových výšin a poskytnout strhující vizuální zážitky.

## FAQ

### Q1: Je Aspose.3D kompatibilní s jinými 3D formáty souborů?

Odpověď 1: Ano, Aspose.3D podporuje různé formáty 3D souborů, což zajišťuje kompatibilitu s širokou řadou návrhových nástrojů.

### Q2: Mohu použít Aspose.3D pro vývoj her?

Odpověď 2: Zatímco Aspose.3D je primárně určen pro grafiku a vizualizaci, jeho funkce mohou doplňovat určité aspekty vývoje her.

### Q3: Kde najdu další příklady a dokumentaci?

 A3: Prozkoumejte komplexní[Aspose.3D dokumentace](https://reference.aspose.com/3d/net/) pro další příklady a podrobné informace.

### Q4: Je k dispozici bezplatná zkušební verze?

 A4: Ano, máte přístup k bezplatné zkušební verzi[tady](https://releases.aspose.com/).

### Q5: Jak mohu vyhledat pomoc nebo se zapojit do komunity?

 A5: Připojte se ke komunitě Aspose.3D na[Fórum podpory](https://forum.aspose.com/c/3d/18) za pomoc a spolupráci.