---
title: Renderowanie sceny do mapy kostki z sześcioma ścianami
linktitle: Renderowanie sceny do mapy kostki z sześcioma ścianami
second_title: Aspose.3D API .NET
description: Twórz wspaniałe mapy kostek za pomocą Aspose.3D dla .NET. Postępuj zgodnie z naszym przewodnikiem krok po kroku dotyczącym renderowania scen 3D w urzekające mapy sześcianów o sześciu ściankach.
weight: 14
url: /pl/net/rendering/render-scene-cubemap/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Renderowanie sceny do mapy kostki z sześcioma ścianami

## Wstęp
Witamy w tym przewodniku krok po kroku dotyczącym renderowania sceny do mapy sześcianu z sześcioma ścianami przy użyciu Aspose.3D dla .NET. W tym samouczku przeprowadzimy Cię przez proces tworzenia wspaniałej mapy sześcianu poprzez renderowanie sceny 3D. Aspose.3D to potężny interfejs API .NET, który upraszcza manipulację grafiką 3D, a dzięki temu przewodnikowi wykorzystasz jego możliwości do tworzenia wciągających map sześcianów.
## Warunki wstępne
Zanim przejdziemy do samouczka, upewnij się, że spełniasz następujące wymagania wstępne:
- Praktyczna znajomość programowania w C# i .NET.
-  Zainstalowany Aspose.3D dla .NET. Możesz go pobrać[Tutaj](https://releases.aspose.com/3d/net/).
- Plik sceny 3D w formacie GLB (np. „VirtualCity.glb”) do renderowania.
## Importuj przestrzenie nazw
Zacznij od zaimportowania niezbędnych przestrzeni nazw dla Aspose.3D do swojego kodu C#:
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
## Krok 1: Załaduj scenę
Załaduj plik sceny 3D, używając następującego kodu:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## Krok 2: Utwórz kamerę i światła
Utwórz kamerę i dwa światła, aby oświetlić scenę:
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
## Krok 3: Utwórz moduł renderujący i cel renderowania
Utwórz moduł renderujący i cel renderowania mapy kostki z teksturą głębi:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
    ITextureCubemap cubemap = rt.Targets[0] as ITextureCubemap;
```
## Krok 4: Zapisz twarze Cubemap
Zapisz każdą ścianę sześcianu na dysku z określonymi nazwami plików:
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
## Wniosek
Gratulacje! Pomyślnie wyrenderowałeś scenę 3D do mapy sześcianu przy użyciu Aspose.3D dla .NET. Odkryj dalsze opcje dostosowywania i ulepszaj swoje projekty grafiki 3D dzięki temu potężnemu interfejsowi API.
## Często Zadawane Pytania
### P: Czy mogę używać Aspose.3D dla .NET z innymi formatami plików 3D?
Tak, Aspose.3D obsługuje różne formaty plików 3D, zapewniając elastyczność w Twoich projektach.
### P: Jak mogę uzyskać wsparcie dla Aspose.3D?
 Odwiedzić[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) za wsparcie społeczności i dyskusje.
### P: Czy dostępny jest bezpłatny okres próbny?
 Tak, możesz uzyskać dostęp do bezpłatnego okresu próbnego[Tutaj](https://releases.aspose.com/).
### P: Czy mogę renderować sceny z animacjami przy użyciu Aspose.3D?
Absolutnie! Aspose.3D obsługuje renderowanie animowanych scen 3D.
### P: Gdzie mogę znaleźć szczegółową dokumentację?
 Patrz[Dokumentacja Aspose.3D](https://reference.aspose.com/3d/net/) w celu uzyskania szczegółowych informacji.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
