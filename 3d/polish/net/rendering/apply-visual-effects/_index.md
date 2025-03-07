---
title: Stosowanie efektów wizualnych w rzutniach 3D
linktitle: Stosowanie efektów wizualnych w rzutniach 3D
second_title: Aspose.3D API .NET
description: Poznaj świat wizualizacji 3D dzięki Aspose.3D dla .NET. Naucz się stosować urzekające efekty wizualne do swoich scen, korzystając z samouczków krok po kroku. Ulepsz swoje projekty dzięki pikselacji, skali szarości, wykrywaniu krawędzi i efektom rozmycia.
weight: 10
url: /pl/net/rendering/apply-visual-effects/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Stosowanie efektów wizualnych w rzutniach 3D

## Wstęp

Poprawa atrakcyjności wizualnej scen 3D jest kluczowym aspektem tworzenia wciągających wrażeń. Aspose.3D dla .NET zapewnia potężny zestaw narzędzi do stosowania efektów wizualnych w rzutniach 3D. W tym samouczku omówimy proces stosowania różnych efektów do sceny 3D, w tym pikselizacji, skali szarości, wykrywania krawędzi i rozmycia.

## Warunki wstępne

Zanim zagłębisz się w samouczek, upewnij się, że posiadasz następujące informacje:

- Praktyczna znajomość programowania w C# i .NET.
-  Zainstalowana biblioteka Aspose.3D dla .NET. Można go pobrać z[Tutaj](https://releases.aspose.com/3d/net/).
- Plik sceny 3D (np. „scene.obj”) do eksperymentów.

## Importuj przestrzenie nazw

Aby rozpocząć, zaimportuj niezbędne przestrzenie nazw dla Aspose.3D i innych zależności. Dodaj następujące linie do swojego kodu:

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

## Krok 1: Załaduj istniejącą scenę 3D

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

 Załaduj scenę 3D za pomocą`Scene` klasa.

## Krok 2: Utwórz kamerę

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

Utwórz instancję kamery i ustaw jej pozycję oraz cel.

## Krok 3: Dodaj światło do sceny

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

Wprowadź oświetlenie, aby wzmocnić efekty wizualne.

## Krok 4: Utwórz moduł renderujący i cel renderowania

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    // Skonfiguruj ustawienia modułu renderującego
    renderer.EnableShadows = false;

    // Utwórz cel renderowania
    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // Skonfiguruj rzutnię
        Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });

        // Renderuj scenę do tekstury
        renderer.Render(rt);

        // Zapisz wyrenderowaną teksturę do pliku
        ((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "Original_viewport_out.png", ImageFormat.Png);

        // Kontynuuj efekty przetwarzania końcowego...
    }
}
```

Utwórz moduł renderujący i cel renderowania, aby przechwycić scenę.

## Krok 5: Zastosuj efekty przetwarzania końcowego

### Krok 5.1 Efekt pikselizacji

```csharp
// Utwórz efekt pikselacji
PostProcessing pixelation = renderer.GetPostProcessing("pixelation");
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_pixelation_out.png", ImageFormat.Png);
```

Zastosuj efekt pikselacji i zapisz wynik.

### Krok 5.2 Efekt skali szarości

```csharp
// Utwórz efekt skali szarości
PostProcessing grayscale = renderer.GetPostProcessing("grayscale");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale_out.png", ImageFormat.Png);
```

Zastosuj efekt skali szarości i zapisz wynik.

### Krok 5.3 Połącz efekty

```csharp
// Połącz efekty skali szarości i pikselizacji
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale+pixelation_out.png", ImageFormat.Png);
```

Połącz wiele efektów, aby uzyskać unikalne rezultaty.

### Krok 5.4 Efekt wykrywania krawędzi

```csharp
// Utwórz efekt wykrywania krawędzi
PostProcessing edgedetection = renderer.GetPostProcessing("edge-detection");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(edgedetection);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_edgedetection_out.png", ImageFormat.Png);
```

Zastosuj efekt wykrywania krawędzi i zapisz wynik.

### Krok 5.5 Efekt rozmycia

```csharp
// Utwórz efekt rozmycia
PostProcessing blur = renderer.GetPostProcessing("blur");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(blur);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_blur_out.png", ImageFormat.Png);
```

Zastosuj efekt rozmycia i zapisz wynik.

## Wniosek

Eksperymentowanie z efektami wizualnymi w rzutniach 3D dodaje scenom głębi i kreatywności. Aspose.3D dla .NET upraszcza ten proces, oferując szereg efektów przetwarzania końcowego, które podnoszą jakość Twoich projektów.

## Często zadawane pytania

### P1: Czy mogę zastosować wiele efektów jednocześnie?

Odpowiedź 1: Tak, możesz łączyć różne efekty przetwarzania końcowego, aby uzyskać unikalne i złożone wyniki.

### P2: Jak mogę dostosować intensywność efektów wizualnych?

Odpowiedź 2: Każdy efekt może mieć parametry, które możesz dostosować, aby kontrolować jego intensywność. Szczegółowe informacje można znaleźć w dokumentacji.

### P3: Czy Aspose.3D nadaje się do tworzenia gier?

Odpowiedź 3: Chociaż Aspose.3D jest przeznaczony głównie do modelowania i renderowania 3D, można go używać w niektórych aspektach tworzenia gier.

### P4: Czy dostępne są dodatkowe efekty przetwarzania końcowego?

O4: Aspose.3D zapewnia wiele wbudowanych efektów przetwarzania końcowego, a za pomocą biblioteki można tworzyć niestandardowe efekty.

### P5: Czy mogę używać Aspose.3D w projektach komercyjnych?

 O5: Tak, możesz używać Aspose.3D do celów komercyjnych. Patrz[strona zakupu](https://purchase.aspose.com/buy) w celu uzyskania szczegółów licencji.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
