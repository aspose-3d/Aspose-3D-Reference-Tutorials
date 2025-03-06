---
title: Použití efektu rybího oka pomocí Aspose.3D pro .NET
linktitle: Použití efektu rybího oka na 3D scénu
second_title: Aspose.3D .NET API
description: Vylepšete své 3D scény pomocí Aspose.3D pro .NET! Naučte se krok za krokem aplikovat efekt podmanivého rybího oka. Stáhnout teď!
weight: 12
url: /cs/net/rendering/fisheye-lens-effect-3d-scene/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Použití efektu rybího oka pomocí Aspose.3D pro .NET

## Úvod
Chcete zlepšit vizuální přitažlivost svých 3D scén? Ponořte se do fascinujícího světa efektů rybího oka s Aspose.3D pro .NET. Tento tutoriál vás krok za krokem provede tím, jak aplikovat efekt rybího oka na vaše 3D scény, což jim poskytne jedinečnou a podmanivou perspektivu.
## Předpoklady
Než začneme, ujistěte se, že máte splněny následující předpoklady:
-  Aspose.3D for .NET: Ujistěte se, že máte nainstalovanou knihovnu Aspose.3D pro .NET. Pokud ne, můžete si jej stáhnout[tady](https://releases.aspose.com/3d/net/).
-  Ukázka 3D scény: Budeme pracovat s ukázkovým souborem 3D scény (VirtualCity.glb). Můžete použít vlastní scénu nebo si stáhnout ukázku z[Aspose.3D dokumentace](https://reference.aspose.com/3d/net/).
## Importovat jmenné prostory
Ve svém projektu .NET zahrňte potřebné jmenné prostory pro přístup k funkcím Aspose.3D. Na začátek kódu přidejte následující jmenné prostory:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Imaging;
using System.Linq;
using System.Text;
```
## Krok 1: Načtěte 3D scénu
Načtěte soubor 3D scény do svého projektu pomocí následujícího kódu:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## Krok 2: Nastavte kameru a světla
Vytvořte kameru a světla pro vylepšení vizuálních aspektů vaší scény. Podle potřeby upravte parametry jako NearPlane, FarPlane a RotationMode:
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light() { Color = new Vector3(Color.CadetBlue) }).Transform.Translation = new Vector3(49, 0, 49);
```
## Krok 3: Vytvořte Renderer a Render Targets
Nastavte vykreslovací modul a vytvořte cíle vykreslení pro mapu krychle a 2D texturu:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    IRenderTexture final = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(false, 32, 0, 0), 1024, 1024);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
```
## Krok 4: Aplikujte efekt rybího oka
Proveďte následné zpracování efektu rybího oka na vykreslené mapě krychle:
```csharp
PostProcessing fisheye = renderer.GetPostProcessing("fisheye");
fisheye.FindProperty("fov").Value = 360.0;
fisheye.Input = rt.Targets[0];
renderer.Execute(fisheye, final);
((ITexture2D)final.Targets[0]).Save("Your Output Directory" + "fisheye.png", ImageFormat.Png);
```
## Závěr
Gratulujeme! Úspěšně jste na svou 3D scénu použili efekt rybího oka pomocí Aspose.3D for .NET. Experimentujte s různými scénami a parametry, abyste popustili uzdu své kreativitě.
## Často kladené otázky
### Mohu použít efekt rybího oka na jakoukoli 3D scénu?
Ano, efekt rybího oka můžete použít na jakoukoli 3D scénu. Pro optimální výsledky se ujistěte, že je scéna správně načtena a osvětlena.
### Jaký význam má nastavení zorného pole (fov) na 360 stupňů?
Zorné pole 360 stupňů zajišťuje kompletní sférickou projekci a vytváří úžasný efekt rybího oka.
### Jak mohu přizpůsobit osvětlení ve své 3D scéně?
Můžete upravit vlastnosti světel, jako je poloha, typ a barva, abyste dosáhli požadovaných světelných efektů.
### Existuje omezení velikosti 3D scény, kterou lze zpracovat?
Velikost 3D scény je primárně omezena systémovými prostředky. Ujistěte se, že váš hardware zvládne velikost vaší scény.
### Mohu pro výsledek efektu rybího oka použít jiný výstupní formát místo PNG?
Ano, kód můžete upravit a uložit výstup v různých formátech obrázků na základě vašich požadavků.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
