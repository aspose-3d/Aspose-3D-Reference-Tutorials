---
title: Renderowanie obrazu modelu 3D z kamery
linktitle: Renderowanie obrazu modelu 3D z kamery
second_title: Aspose.3D API .NET
description: Poznaj świat renderowania 3D dzięki Aspose.3D dla .NET. Dowiedz się, jak łatwo tworzyć urzekające wizualizacje, korzystając z naszego przewodnika krok po kroku.
type: docs
weight: 11
url: /pl/net/rendering/render-3d-model-image/
---
## Wstęp
Tworzenie oszałamiających wizualizacji 3D jest ekscytującym aspektem tworzenia oprogramowania, a dzięki Aspose.3D dla .NET możesz ożywić swoje modele 3D. W tym samouczku poprowadzimy Cię przez renderowanie obrazu modelu 3D z kamery przy użyciu Aspose.3D, dostarczając instrukcje krok po kroku i cenne spostrzeżenia.
## Warunki wstępne
Zanim zagłębimy się w proces renderowania, upewnij się, że spełnione są następujące wymagania wstępne:
-  Biblioteka Aspose.3D dla .NET: Pobierz i zainstaluj bibliotekę z[link do pobrania](https://releases.aspose.com/3d/net/).
- Model 3D: Przygotuj plik modelu 3D (np. Aspose3D.obj), który chcesz wyrenderować.
- Środowisko programistyczne .NET: Upewnij się, że masz gotowe działające środowisko programistyczne .NET.
## Importuj przestrzenie nazw
W swoim projekcie .NET uwzględnij niezbędne przestrzenie nazw dla Aspose.3D:
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
## Krok 1: Załaduj scenę 3D
```csharp
Scene scene = new Scene();
var path = RunExamples.GetDataFilePath("Aspose3D.obj");
scene.Open(path);
```
## Krok 2: Utwórz kamerę
```csharp
Camera cam = new Camera(ProjectionType.Perspective);
cam.NearPlane = 1;
cam.FarPlane = 500;
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(170, 16, 130);
cam.LookAt = new Vector3(28, 0, -30);
```
## Krok 3: Dodaj światła do sceny
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
## Krok 4: Określ opcje renderowania obrazu
```csharp
ImageRenderOptions opt = new ImageRenderOptions();
opt.BackgroundColor = Color.AliceBlue;
opt.AssetDirectories.Add("Your Document Directory" + "textures");
opt.EnableShadows = true;
```
## Krok 5: Renderuj scenę
```csharp
scene.Render(cam, "Your Output Directory" + "Render3DModelImageFromCamera.png", new Size(1024, 1024), ImageFormat.Png, opt);
```
## Wniosek
Gratulacje! Pomyślnie wyrenderowałeś obraz modelu 3D z kamery przy użyciu Aspose.3D dla .NET. Możesz eksperymentować z różnymi modelami, kątami kamery i ustawieniami oświetlenia, aby ulepszyć swoje wizualizacje 3D.
## Często zadawane pytania
### P: Czy mogę używać Aspose.3D dla .NET z innymi narzędziami do modelowania 3D?
Odp.: Aspose.3D obsługuje różne formaty modeli 3D, dzięki czemu jest kompatybilny z wieloma popularnymi narzędziami do modelowania.
### P: Jak mogę rozwiązać problemy z renderowaniem?
 O: Sprawdź Aspose.3D[forum](https://forum.aspose.com/c/3d/18) w celu uzyskania wsparcia i rozwiązań typowych problemów z renderowaniem.
### P: Czy dostępny jest bezpłatny okres próbny?
 Odp.: Tak, możesz poznać funkcje Aspose.3D, uzyskując[bezpłatna wersja próbna](https://releases.aspose.com/).
### P: Gdzie mogę znaleźć obszerną dokumentację?
 Odp.: Patrz[dokumentacja](https://reference.aspose.com/3d/net/) aby uzyskać szczegółowe wskazówki dotyczące Aspose.3D dla .NET.
### P: Jak kupić Aspose.3D dla .NET?
 O: Odwiedź[strona zakupu](https://purchase.aspose.com/buy) aby nabyć licencję najlepiej odpowiadającą Twoim potrzebom.