---
title: Snadné vykreslování 3D panoramat pomocí Aspose.3D pro .NET
linktitle: Vykreslování panoramatického pohledu na 3D scénu
second_title: Aspose.3D .NET API
description: Naučte se vytvářet úžasné 3D panoramatické pohledy pomocí Aspose.3D for .NET. Postupujte podle našeho podrobného průvodce pro pohlcující vykreslování scény.
weight: 13
url: /cs/net/rendering/render-panorama-view/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Snadné vykreslování 3D panoramat pomocí Aspose.3D pro .NET

## Úvod
Vytváření úchvatných 3D scén a jejich vykreslování do panoramatických pohledů se stalo základním aspektem moderních aplikací. Aspose.3D for .NET poskytuje robustní řešení pro vývojáře, kteří chtějí bezproblémově integrovat možnosti 3D vykreslování do svých projektů. V tomto tutoriálu prozkoumáme proces vykreslování panoramatického pohledu na 3D scénu pomocí Aspose.3D for .NET.
## Předpoklady
Než se pustíte do výukového programu, ujistěte se, že máte splněny následující předpoklady:
-  Aspose.3D for .NET: Stáhněte a nainstalujte knihovnu Aspose.3D. Můžete najít knihovnu a dokumentaci[tady](https://releases.aspose.com/3d/net/).
- Vývojové prostředí .NET: Ujistěte se, že máte na svém počítači nastavené funkční vývojové prostředí .NET.
- Ukázka 3D scény: Stáhněte si ukázkový soubor 3D scény, například „VirtualCity.glb“, který použijeme pro vykreslení panoramatického pohledu.
## Importovat jmenné prostory
Ve svém projektu .NET importujte potřebné jmenné prostory pro práci s Aspose.3D:
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
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
Načtěte 3D scénu pomocí Aspose.3D. Nahraďte "VirtualCity.glb" cestou k požadovanému souboru 3D scény.
## Krok 2: Nastavte kameru a světla
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light()
{
    Color = new Vector3(Color.CadetBlue)
}).Transform.Translation = new Vector3(49, 0, 49);
```
Nastavte fotoaparát a světla tak, aby správně zachytily 3D scénu.
## Krok 3: Vytvořte Renderer a Render Targets
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    IRenderTexture final = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(false, 32, 0, 0), 1024 * 3, 1024);
```
Vytvořte vykreslovací modul a definujte cíle vykreslení pro krychlovou mapu a konečný panoramatický snímek.
## Krok 4: Nakonfigurujte Viewport a Render
```csharp
rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
renderer.Render(rt);
```
Nakonfigurujte výřez pomocí kamery a vykreslete mapu krychle.
## Krok 5: Použijte následné zpracování pro panoramatické zobrazení
```csharp
PostProcessing equirectangular = renderer.GetPostProcessing("equirectangular");
equirectangular.Input = rt.Targets[0];
renderer.Execute(equirectangular, final);
```
Pro vytvoření panoramatického pohledu použijte následné zpracování ekvidaktulární projekce.
## Krok 6: Uložte vykreslené panorama
```csharp
((ITexture2D)final.Targets[0]).Save("Your Output Directory" + "panorama.png", ImageFormat.Png);
```
Uložte vykreslený panoramatický obraz do určeného výstupního adresáře.
## Závěr
Aspose.3D for .NET se vykreslování panoramatického pohledu na 3D scénu stává přímočarým procesem. Vylepšete své aplikace bezproblémovým začleněním pohlcujících 3D vizualizací.
## Často kladené otázky
### Otázka: Mohu použít svou vlastní 3D scénu pro vykreslování panoramat?
Ano, jednoduše nahraďte cestu k souboru ukázkové scény cestou k vaší vlastní 3D scéně.
### Otázka: Jsou k dispozici další efekty následného zpracování?
Aspose.3D for .NET poskytuje různé efekty následného zpracování pro vylepšení vašich vykreslených obrázků.
### Otázka: Jak mohu optimalizovat výkon vykreslování?
Upravte parametry vykreslování a cílové rozměry na základě požadavků vaší aplikace.
### Otázka: Mohu tento výukový program integrovat do webové aplikace?
Ano, začleněním Aspose.3D for .NET do vašeho webového projektu .NET.
### Otázka: Existuje komunitní fórum pro podporu Aspose.3D?
 Ano, navštivte[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) za podporu komunity.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
