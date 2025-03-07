---
title: Vykreslování obrazu 3D modelu z fotoaparátu
linktitle: Vykreslování obrazu 3D modelu z fotoaparátu
second_title: Aspose.3D .NET API
description: Prozkoumejte svět 3D vykreslování s Aspose.3D pro .NET. Naučte se, jak bez námahy vytvářet podmanivé vizualizace pomocí našeho podrobného průvodce.
weight: 11
url: /cs/net/rendering/render-3d-model-image/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Vykreslování obrazu 3D modelu z fotoaparátu

## Úvod
Vytváření úžasných 3D vizualizací je vzrušujícím aspektem vývoje softwaru as Aspose.3D for .NET můžete své 3D modely oživit. V tomto tutoriálu vás provedeme vykreslením obrazu 3D modelu z kamery pomocí Aspose.3D a poskytneme vám podrobné pokyny a cenné poznatky.
## Předpoklady
Než se pustíme do procesu vykreslování, ujistěte se, že máte splněny následující předpoklady:
-  Aspose.3D for .NET Library: Stáhněte a nainstalujte knihovnu z[odkaz ke stažení](https://releases.aspose.com/3d/net/).
- 3D model: Připravte soubor 3D modelu (např. Aspose3D.obj), který chcete vykreslit.
- Vývojové prostředí .NET: Ujistěte se, že máte připravené funkční vývojové prostředí .NET.
## Importovat jmenné prostory
Ve svém projektu .NET zahrňte potřebné jmenné prostory pro Aspose.3D:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Utilities;
using System.Drawing;
using System.Drawing.Imaging;
```
## Krok 1: Načtěte 3D scénu
```csharp
Scene scene = new Scene();
var path = RunExamples.GetDataFilePath("Aspose3D.obj");
scene.Open(path);
```
## Krok 2: Vytvořte kameru
```csharp
Camera cam = new Camera(ProjectionType.Perspective);
cam.NearPlane = 1;
cam.FarPlane = 500;
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(170, 16, 130);
cam.LookAt = new Vector3(28, 0, -30);
```
## Krok 3: Přidejte světla do scény
```csharp
scene.RootNode.CreateChildNode(new Light()
{
    LightType = LightType.Point,
    ConstantAttenuation = 0.3,
    Color = new Vector3(Color.White)
}).Transform.Translation = new Vector3(30, 10, 10);
scene.RootNode.CreateChildNode(new Light()
{
    LightType = LightType.Directional,
    ConstantAttenuation = 0.3,
    Direction = new Vector3(-0.3, -0.4, 0.3),
    Color = new Vector3(Color.White)
});
scene.RootNode.CreateChildNode(new Light()
{
    LightType = LightType.Spot,
    CastShadows = true,
    LookAt = new Vector3(28, 10, -30),
    Color = new Vector3(Color.White)
}).Transform.Translation = new Vector3(40, 10, 50);
```
## Krok 4: Zadejte možnosti vykreslení obrázku
```csharp
ImageRenderOptions opt = new ImageRenderOptions();
opt.BackgroundColor = Color.AliceBlue;
opt.AssetDirectories.Add("Your Document Directory" + "textures");
opt.EnableShadows = true;
```
## Krok 5: Renderujte scénu
```csharp
scene.Render(cam, "Your Output Directory" + "Render3DModelImageFromCamera.png", new Size(1024, 1024), ImageFormat.Png, opt);
```
## Závěr
Gratulujeme! Úspěšně jste vykreslili obrázek 3D modelu z kamery pomocí Aspose.3D for .NET. Nebojte se experimentovat s různými modely, úhly kamery a nastavením osvětlení, abyste vylepšili své 3D vizualizace.
## Nejčastější dotazy
### Otázka: Mohu používat Aspose.3D pro .NET s jinými nástroji pro 3D modelování?
Odpověď: Aspose.3D podporuje různé formáty 3D modelů, díky čemuž je kompatibilní s mnoha oblíbenými modelovacími nástroji.
### Otázka: Jak mohu vyřešit problémy s vykreslováním?
 A: Zkontrolujte Aspose.3D[Fórum](https://forum.aspose.com/c/3d/18) za podporu a řešení běžných problémů s vykreslováním.
### Otázka: Je k dispozici bezplatná zkušební verze?
Odpověď: Ano, funkce Aspose.3D můžete prozkoumat získáním a[zkušební verze zdarma](https://releases.aspose.com/).
### Otázka: Kde najdu komplexní dokumentaci?
 A: Viz[dokumentace](https://reference.aspose.com/3d/net/) pro hloubkové vedení Aspose.3D pro .NET.
### Otázka: Jak koupím Aspose.3D pro .NET?
 A: Navštivte[nákupní stránku](https://purchase.aspose.com/buy) získat licenci, která nejlépe vyhovuje vašim potřebám.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
