---
title: Stosowanie efektu obiektywu typu rybie oko w Aspose.3D dla .NET
linktitle: Stosowanie efektu obiektywu typu rybie oko do sceny 3D
second_title: Aspose.3D API .NET
description: Ulepsz swoje sceny 3D dzięki Aspose.3D dla .NET! Dowiedz się, jak krok po kroku zastosować urzekający efekt obiektywu typu rybie oko. Pobierz teraz!
weight: 12
url: /pl/net/rendering/fisheye-lens-effect-3d-scene/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Stosowanie efektu obiektywu typu rybie oko w Aspose.3D dla .NET

## Wstęp
Czy chcesz poprawić atrakcyjność wizualną swoich scen 3D? Zanurz się w fascynujący świat efektów obiektywu typu rybie oko dzięki Aspose.3D dla .NET. Ten samouczek poprowadzi Cię krok po kroku przez zastosowanie efektu obiektywu typu rybie oko do scen 3D, nadając im wyjątkową i urzekającą perspektywę.
## Warunki wstępne
Zanim zaczniemy, upewnij się, że spełnione są następujące wymagania wstępne:
-  Aspose.3D dla .NET: Upewnij się, że masz zainstalowaną bibliotekę Aspose.3D dla .NET. Jeśli nie, możesz go pobrać[Tutaj](https://releases.aspose.com/3d/net/).
-  Przykładowa scena 3D: Będziemy pracować z przykładowym plikiem sceny 3D (VirtualCity.glb). Możesz użyć własnej sceny lub pobrać próbkę z pliku[Dokumentacja Aspose.3D](https://reference.aspose.com/3d/net/).
## Importuj przestrzenie nazw
W swoim projekcie .NET uwzględnij niezbędne przestrzenie nazw, aby uzyskać dostęp do funkcjonalności Aspose.3D. Dodaj następujące przestrzenie nazw na początku kodu:
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
## Krok 1: Załaduj scenę 3D
Załaduj plik sceny 3D do swojego projektu, używając następującego kodu:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## Krok 2: Skonfiguruj kamerę i światła
Utwórz kamerę i światła, aby poprawić wizualne aspekty swojej sceny. W razie potrzeby dostosuj parametry, takie jak NearPlane, FarPlane i RotationMode:
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
## Krok 3: Utwórz moduł renderujący i elementy docelowe renderowania
Skonfiguruj moduł renderujący i utwórz cele renderowania dla mapy sześcianu i tekstury 2D:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    IRenderTexture final = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(false, 32, 0, 0), 1024, 1024);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
```
## Krok 4: Zastosuj efekt obiektywu typu rybie oko
Wykonaj obróbkę końcową efektu obiektywu typu rybie oko na wyrenderowanej mapie sześcianu:
```csharp
PostProcessing fisheye = renderer.GetPostProcessing("fisheye");
fisheye.FindProperty("fov").Value = 360.0;
fisheye.Input = rt.Targets[0];
renderer.Execute(fisheye, final);
((ITexture2D)final.Targets[0]).Save("Your Output Directory" + "fisheye.png", ImageFormat.Png);
```
## Wniosek
Gratulacje! Pomyślnie zastosowałeś efekt obiektywu typu rybie oko do swojej sceny 3D za pomocą Aspose.3D dla .NET. Eksperymentuj z różnymi scenami i parametrami, aby uwolnić swoją kreatywność.
## Często Zadawane Pytania
### Czy mogę zastosować efekt rybiego oka do dowolnej sceny 3D?
Tak, możesz zastosować efekt rybiego oka do dowolnej sceny 3D. Aby uzyskać optymalne rezultaty, upewnij się, że scena jest prawidłowo załadowana i oświetlona.
### Jakie znaczenie ma regulacja pola widzenia (fov) na 360 stopni?
Pole widzenia 360 stopni zapewnia pełną projekcję sferyczną, tworząc oszałamiający efekt rybiego oka.
### Jak mogę dostosować oświetlenie w mojej scenie 3D?
Możesz dostosować właściwości świateł, takie jak położenie, typ i kolor, aby uzyskać pożądane efekty świetlne.
### Czy istnieje ograniczenie rozmiaru sceny 3D, którą można przetworzyć?
Rozmiar sceny 3D jest ograniczony przede wszystkim zasobami systemowymi. Upewnij się, że Twój sprzęt jest w stanie obsłużyć rozmiar Twojej sceny.
### Czy mogę użyć innego formatu wyjściowego zamiast PNG, aby uzyskać efekt rybiego oka?
Tak, możesz zmodyfikować kod, aby zapisać dane wyjściowe w różnych formatach obrazu w zależności od wymagań.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
