---
title: Przechwytywanie rzutni w scenach 3D
linktitle: Przechwytywanie rzutni w scenach 3D
second_title: Aspose.3D API .NET
description: Naucz się przechwytywać wspaniałe rzutnie 3D za pomocą Aspose.3D dla .NET. Przewodnik krok po kroku dotyczący elastycznego renderowania scen.
weight: 11
url: /pl/net/rendering/capture-viewport/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Przechwytywanie rzutni w scenach 3D

## Wstęp

W dziedzinie grafiki i wizualizacji 3D przechwytywanie rzutni jest niezbędną umiejętnością, która zwiększa głębię i szczegółowość scen. Aspose.3D dla .NET zapewnia solidne rozwiązanie do renderowania i manipulowania scenami 3D. Ten samouczek poprowadzi Cię przez proces przechwytywania rzutni w scenach 3D przy użyciu Aspose.3D, umożliwiając z łatwością tworzenie oszałamiających wizualizacji.

## Warunki wstępne

Zanim przejdziesz do samouczka, upewnij się, że spełniasz następujące wymagania wstępne:

-  Biblioteka Aspose.3D dla .NET: Upewnij się, że masz zainstalowaną bibliotekę Aspose.3D. Można go pobrać z[Tutaj](https://releases.aspose.com/3d/net/).

## Importuj przestrzenie nazw

Aby rozpocząć, zaimportuj niezbędne przestrzenie nazw do swojego projektu .NET:

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

Rozpocznij od załadowania istniejącej sceny 3D do swojego projektu. Poniższy fragment kodu demonstruje to:

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

## Krok 2: Utwórz kamerę

Następnie utwórz instancję kamery i ustaw jej pozycję oraz cel:

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

## Krok 3: Dodaj oświetlenie do sceny

Wzbogać swoją scenę, dodając źródło światła. Poniższy fragment kodu pokazuje, jak utworzyć światło punktowe:

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

## Krok 4: Skonfiguruj moduł renderujący i cel renderowania

Skonfiguruj moduł renderujący i utwórz cel renderowania do przechwytywania sceny:

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    renderer.EnableShadows = false;

    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // ... (kontynuacja w kolejnych krokach)
    }
}
```

## Krok 5: Zdefiniuj rzutnie i renderowanie

Zdefiniuj rzutnie i renderuj scenę, aby wygenerować obrazy wyjściowe:

```csharp
Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-1viewports_out.png", ImageFormat.Png);
```

## Krok 6: Modyfikuj rzutnie i renderuj ponownie

Zmodyfikuj rzutnie i ponownie wyrenderuj scenę, demonstrując elastyczność Aspose.3D:

```csharp
vp.Area = new RelativeRectangle() { ScaleWidth = 0.5f, ScaleHeight = 1 };
rt.CreateViewport(camera, new RelativeRectangle() { ScaleX = 0.5f, ScaleWidth = 0.5f, ScaleHeight = 1 });
camera.FieldOfView = 90;
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-2viewports_out.png", ImageFormat.Png);
```

Kontynuuj eksperymentowanie z różnymi konfiguracjami, aby osiągnąć pożądane efekty wizualne.

## Wniosek

tym samouczku zbadaliśmy proces przechwytywania rzutni w scenach 3D przy użyciu Aspose.3D dla .NET. Wykorzystując jego zaawansowane funkcje, możesz wznieść swoje projekty graficzne 3D na nowy poziom, zapewniając urzekające wrażenia wizualne.

## Często zadawane pytania

### P1: Czy Aspose.3D jest kompatybilny z innymi formatami plików 3D?

Odpowiedź 1: Tak, Aspose.3D obsługuje różne formaty plików 3D, zapewniając kompatybilność z szeroką gamą narzędzi projektowych.

### P2: Czy mogę używać Aspose.3D do tworzenia gier?

Odpowiedź 2: Chociaż Aspose.3D jest przeznaczony głównie do grafiki i wizualizacji, jego funkcjonalności mogą uzupełniać pewne aspekty tworzenia gier.

### P3: Gdzie mogę znaleźć dodatkowe przykłady i dokumentację?

 A3: Poznaj kompleksowość[Dokumentacja Aspose.3D](https://reference.aspose.com/3d/net/) aby uzyskać więcej przykładów i szczegółowych informacji.

### P4: Czy dostępny jest bezpłatny okres próbny?

 Odpowiedź 4: Tak, możesz uzyskać dostęp do bezpłatnego okresu próbnego[Tutaj](https://releases.aspose.com/).

### P5: Jak mogę szukać pomocy lub uczestniczyć w społeczności?

 A5: Dołącz do społeczności Aspose.3D na[forum wsparcia](https://forum.aspose.com/c/3d/18) za pomoc i współpracę.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
