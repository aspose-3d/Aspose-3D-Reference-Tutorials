---
title: Použití vizuálních efektů ve 3D výřezech
linktitle: Použití vizuálních efektů ve 3D výřezech
second_title: Aspose.3D .NET API
description: Prozkoumejte svět 3D vizualizace s Aspose.3D pro .NET. Naučte se na své scény aplikovat podmanivé vizuální efekty pomocí výukových programů krok za krokem. Vylepšete své projekty pomocí pixelace, stupňů šedi, detekce okrajů a efektů rozmazání.
weight: 10
url: /cs/net/rendering/apply-visual-effects/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Použití vizuálních efektů ve 3D výřezech

## Úvod

Vylepšení vizuální přitažlivosti 3D scén je zásadním aspektem vytváření pohlcujících zážitků. Aspose.3D for .NET poskytuje výkonnou sadu nástrojů pro aplikaci vizuálních efektů na 3D výřezy. V tomto tutoriálu si projdeme procesem aplikace různých efektů na 3D scénu, včetně pixelace, stupňů šedi, detekce hran a rozostření.

## Předpoklady

Než se pustíte do výukového programu, ujistěte se, že máte následující:

- Pracovní znalost vývoje C# a .NET.
-  Nainstalovaná knihovna Aspose.3D for .NET. Můžete si jej stáhnout z[tady](https://releases.aspose.com/3d/net/).
- Soubor 3D scény (např. "scene.obj") pro experimentování.

## Importovat jmenné prostory

Chcete-li začít, importujte potřebné jmenné prostory pro Aspose.3D a další závislosti. Přidejte do kódu následující řádky:

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

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

 Načtěte svou 3D scénu pomocí`Scene` třída.

## Krok 2: Vytvořte kameru

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

Vytvořte instanci kamery a nastavte její polohu a cíl.

## Krok 3: Přidejte světlo do scény

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

Zaveďte osvětlení pro zvýšení vizuálních efektů.

## Krok 4: Vytvořte Renderer a Render Target

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    // Nakonfigurujte nastavení rendereru
    renderer.EnableShadows = false;

    // Vytvořte cíl vykreslení
    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // Nakonfigurujte výřez
        Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });

        // Vykreslete scénu do textury
        renderer.Render(rt);

        // Uložte vykreslenou texturu do souboru
        ((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "Original_viewport_out.png", ImageFormat.Png);

        // Pokračujte s efekty následného zpracování...
    }
}
```

Vytvořte vykreslovací modul a cíl vykreslení pro zachycení scény.

## Krok 5: Aplikujte efekty následného zpracování

### Krok 5.1 Efekt pixelace

```csharp
// Vytvořte efekt pixelace
PostProcessing pixelation = renderer.GetPostProcessing("pixelation");
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_pixelation_out.png", ImageFormat.Png);
```

Použijte efekt pixelace a uložte výsledek.

### Krok 5.2 Efekt stupňů šedi

```csharp
// Vytvořte efekt ve stupních šedi
PostProcessing grayscale = renderer.GetPostProcessing("grayscale");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale_out.png", ImageFormat.Png);
```

Použijte efekt ve stupních šedi a uložte výsledek.

### Krok 5.3 Kombinovat efekty

```csharp
// Kombinujte efekty ve stupních šedi a pixelace
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale+pixelation_out.png", ImageFormat.Png);
```

Kombinujte více efektů pro jedinečné výsledky.

### Krok 5.4 Efekt detekce hran

```csharp
// Vytvořte efekt detekce hran
PostProcessing edgedetection = renderer.GetPostProcessing("edge-detection");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(edgedetection);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_edgedetection_out.png", ImageFormat.Png);
```

Použijte efekt detekce hran a uložte výsledek.

### Krok 5.5 Efekt rozostření

```csharp
// Vytvořte efekt rozostření
PostProcessing blur = renderer.GetPostProcessing("blur");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(blur);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_blur_out.png", ImageFormat.Png);
```

Použijte efekt rozostření a uložte výsledek.

## Závěr

Experimentování s vizuálními efekty ve 3D výřezech dodává vašim scénám hloubku a kreativitu. Aspose.3D for .NET tento proces zjednodušuje a nabízí řadu efektů následného zpracování pro povýšení vašich projektů.

## FAQ

### Q1: Mohu použít více efektů současně?

Odpověď 1: Ano, můžete kombinovat různé efekty následného zpracování pro jedinečné a komplexní výsledky.

### Q2: Jak mohu upravit intenzitu vizuálních efektů?

A2: Každý efekt může mít parametry, které můžete vyladit, abyste řídili jeho intenzitu. Konkrétní podrobnosti naleznete v dokumentaci.

### Q3: Je Aspose.3D vhodný pro vývoj her?

A3: Zatímco Aspose.3D je primárně navržen pro 3D modelování a vykreslování, lze jej použít v určitých aspektech vývoje her.

### Q4: Jsou k dispozici další efekty následného zpracování?

A4: Aspose.3D poskytuje řadu vestavěných efektů následného zpracování a pomocí knihovny můžete vytvářet vlastní efekty.

### Q5: Mohu použít Aspose.3D pro komerční projekty?

 A5: Ano, můžete použít Aspose.3D pro komerční účely. Odkazovat na[nákupní stránku](https://purchase.aspose.com/buy) pro podrobnosti o licencích.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
