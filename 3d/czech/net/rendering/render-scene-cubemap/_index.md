---
title: Vykreslování scény do mapy krychle se šesti tvářemi
linktitle: Vykreslování scény do mapy krychle se šesti tvářemi
second_title: Aspose.3D .NET API
description: Vytvářejte úžasné cubemaps s Aspose.3D pro .NET. Postupujte podle našeho podrobného průvodce pro vykreslování 3D scén do podmanivých šestistěnných krychlových map.
weight: 14
url: /cs/net/rendering/render-scene-cubemap/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Vykreslování scény do mapy krychle se šesti tvářemi

## Úvod
Vítejte v tomto podrobném průvodci vykreslováním scény do mapy krychle se šesti plochami pomocí Aspose.3D pro .NET. V tomto tutoriálu vás provedeme procesem vytváření úžasné mapy krychle vykreslením 3D scény. Aspose.3D je výkonné rozhraní .NET API, které zjednodušuje manipulaci s 3D grafikou, as tímto průvodcem využijete jeho schopnosti k vytvoření úchvatných map cubemap.
## Předpoklady
Než se pustíme do výukového programu, ujistěte se, že máte splněny následující předpoklady:
- Pracovní znalost vývoje C# a .NET.
-  Aspose.3D pro .NET nainstalován. Můžete si jej stáhnout[tady](https://releases.aspose.com/3d/net/).
- Soubor 3D scény ve formátu GLB (např. „VirtualCity.glb“) pro vykreslení.
## Importovat jmenné prostory
Začněte importováním potřebných jmenných prostorů pro Aspose.3D do vašeho kódu C#:
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
## Krok 1: Načtěte scénu
Načtěte soubor 3D scény pomocí následujícího kódu:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## Krok 2: Vytvořte fotoaparát a světla
Vytvořte kameru a dvě světla pro osvětlení scény:
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
## Krok 3: Vytvořte Renderer a Render Target
Vytvořte renderer a cíl vykreslení mapy krychle s texturou hloubky:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
    ITextureCubemap cubemap = rt.Targets[0] as ITextureCubemap;
```
## Krok 4: Uložte Cubemap Faces
Uložte každou plochu mapy krychle na disk se zadanými názvy souborů:
```csharp
CubeFaceData<string> fileNames = new CubeFaceData<string>()
{
    Right = "Your Output Directory" + "right.png",
    Left = "Your Output Directory" + "left.png",
    Back = "Your Output Directory" + "back.png",
    Front = "Your Output Directory" + "front.png",
    Bottom = "Your Output Directory" + "bottom.png",
    Top = "Your Output Directory" + "top.png"
};
cubemap.Save(fileNames, ImageFormat.Png);
```
## Závěr
Gratulujeme! Úspěšně jste vyrenderovali 3D scénu do cubemap pomocí Aspose.3D for .NET. Prozkoumejte další možnosti přizpůsobení a vylepšete své 3D grafické projekty pomocí tohoto výkonného API.
## Často kladené otázky
### Otázka: Mohu použít Aspose.3D pro .NET s jinými formáty 3D souborů?
Ano, Aspose.3D podporuje různé formáty 3D souborů a poskytuje flexibilitu ve vašich projektech.
### Otázka: Jak mohu získat podporu pro Aspose.3D?
 Navštivte[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) za podporu komunity a diskuze.
### Otázka: Je k dispozici bezplatná zkušební verze?
 Ano, máte přístup k bezplatné zkušební verzi[tady](https://releases.aspose.com/).
### Otázka: Mohu renderovat scény s animacemi pomocí Aspose.3D?
Absolutně! Aspose.3D podporuje vykreslování animovaných 3D scén.
### Otázka: Kde najdu podrobnou dokumentaci?
 Odkazovat na[Aspose.3D dokumentace](https://reference.aspose.com/3d/net/) pro podrobné informace.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
