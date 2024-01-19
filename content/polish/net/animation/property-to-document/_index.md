---
title: Animowanie właściwości w dokumencie w scenach 3D
linktitle: Animowanie właściwości w dokumencie w scenach 3D
second_title: Aspose.3D API .NET
description: Naucz się animować właściwości 3D za pomocą Aspose.3D dla .NET. Przewodnik krok po kroku dotyczący tworzenia dynamicznych scen.
type: docs
weight: 10
url: /pl/net/animation/property-to-document/
---
## Wstęp

Jeśli nurkujesz w świecie tworzenia i animacji scen 3D w .NET, Aspose.3D będzie Twoim ulubionym zestawem narzędzi. W tym przewodniku krok po kroku zbadamy proces animowania właściwości w scenach 3D przy użyciu Aspose.3D dla .NET. Na koniec będziesz wyposażony w wiedzę niezbędną do tchnięcia życia w Twoje projekty 3D.

## Warunki wstępne

Zanim wyruszymy w tę ekscytującą podróż, upewnij się, że spełniasz następujące wymagania wstępne:

- Aspose.3D dla .NET: Upewnij się, że masz zainstalowaną bibliotekę. Można go pobrać z[Witryna Aspose.3D](https://releases.aspose.com/3d/net/).

- Znajomość języka C#: Znajomość języka programowania C# jest niezbędna do zrozumienia i wdrożenia przykładów.

- Zintegrowane środowisko programistyczne (IDE): Użyj preferowanego środowiska IDE, takiego jak Visual Studio, do kodowania wraz z przykładami.

- Podstawowe koncepcje scen 3D: Znajomość podstawowych koncepcji scen 3D sprawi, że Twoja nauka stanie się płynniejsza.

## Importuj przestrzenie nazw

Upewnij się, że w kodzie C# zaimportowałeś niezbędne przestrzenie nazw dla Aspose.3D. Oto przykład:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose._3D.Examples.CSharp.Geometry_Hierarchy;
```

## Krok 1: Zainicjuj obiekt sceny

```csharp
Scene scene = new Scene();
```

## Krok 2: Utwórz siatkę za pomocą narzędzia Polygon Builder

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## Krok 3: Utwórz węzły kostki

```csharp
Node cube1 = scene.RootNode.CreateChildNode("cube1", mesh);
```

## Krok 4: Znajdź właściwość tłumaczenia

```csharp
Property translation = cube1.Transform.FindProperty("Translation");
```

## Krok 5: Utwórz punkt wiązania

```csharp
BindPoint bindPoint = new BindPoint(scene, translation);
```

## Krok 6: Powiąż krzywą animacji z komponentem X

```csharp
bindPoint.BindKeyframeSequence("X", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, 20.0f, Interpolation.Bezier},
    {5, 30.0f, Interpolation.Linear},
});
```

## Krok 7: Powiąż krzywą animacji z komponentem Z

```csharp
bindPoint.BindKeyframeSequence("Z", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, -10.0f, Interpolation.Bezier},
    {5, 0.0f, Interpolation.Linear},
});
```

## Krok 8: Zapisz scenę 3D

```csharp
string output = "Your Output Directory" + "PropertyToDocument.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

## Krok 9: Wyświetl komunikat o powodzeniu

```csharp
Console.WriteLine("\nAnimation property added successfully to document.\nFile saved at " + output);
```

## Wniosek

Gratulacje! Właśnie opanowałeś sztukę animowania właściwości w scenach 3D przy użyciu Aspose.3D dla .NET. Teraz pozwól swojej kreatywności płynąć, tchnąc życie w swoje dzieła 3D.

## Często Zadawane Pytania

### P1: Gdzie mogę znaleźć dokumentację Aspose.3D?

 Odpowiedź 1: Dokumentacja jest dostępna[Tutaj](https://reference.aspose.com/3d/net/).

### P2: Jak pobrać Aspose.3D dla .NET?

 A2: Możesz pobrać go z[strona wydania](https://releases.aspose.com/3d/net/).

### P3: Czy dostępny jest bezpłatny okres próbny?

 A3: Tak, możesz uzyskać bezpłatną wersję próbną[Tutaj](https://releases.aspose.com/).

### P4: Gdzie mogę uzyskać wsparcie dla Aspose.3D?

 A4: Odwiedź[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) dla wsparcia.

### P5: Czy mogę uzyskać licencję tymczasową?

 Odpowiedź 5: Tak, możesz uzyskać licencję tymczasową[Tutaj](https://purchase.aspose.com/temporary-license/).