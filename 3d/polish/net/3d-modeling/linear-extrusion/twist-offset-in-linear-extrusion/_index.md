---
title: Przesunięcie skrętu w wytłaczaniu liniowym
linktitle: Przesunięcie skrętu w wytłaczaniu liniowym
second_title: Aspose.3D API .NET
description: Odkryj magię Aspose.3D dla .NET dzięki naszemu przewodnikowi krok po kroku na temat przesunięcia skrętu w wytłaczaniu liniowym. Podnieś poziom swoich projektów 3D bez wysiłku.
weight: 15
url: /pl/net/3d-modeling/linear-extrusion/twist-offset-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Przesunięcie skrętu w wytłaczaniu liniowym

## Wstęp

Witamy w świecie Aspose.3D dla .NET, wszechstronnej biblioteki umożliwiającej programistom łatwą obsługę manipulacji 3D. W tym samouczku zagłębimy się w jedną z intrygujących funkcji - „Przesunięcie skrętu w wytłaczaniu liniowym”. Jeśli jesteś gotowy, aby podnieść swoje umiejętności programowania 3D, przejdźmy do rzeczy!

## Warunki wstępne

Zanim wyruszymy w tę ekscytującą podróż, upewnij się, że spełniasz następujące wymagania wstępne:

-  Biblioteka Aspose.3D dla .NET: Pobierz i zainstaluj bibliotekę z[strona wydania](https://releases.aspose.com/3d/net/).

- Twoje środowisko programistyczne: Upewnij się, że środowisko programistyczne jest skonfigurowane i gotowe do użycia.

## Importuj przestrzenie nazw

Zacznij od zaimportowania niezbędnych przestrzeni nazw, aby uzyskać dostęp do funkcjonalności zapewnianej przez Aspose.3D dla .NET. W Twoim kodzie może to wyglądać następująco:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Podzielmy teraz przykład na łatwe do wykonania kroki, aby opanować przesunięcie skrętu w wytłaczaniu liniowym:

## Krok 1: Zainicjuj profil podstawowy

Rozpocznij od utworzenia profilu podstawowego, którego przykładem jest kształt prostokąta o określonym promieniu zaokrąglenia.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Krok 2: Utwórz scenę

Wygeneruj scenę 3D, w której będą hostowane Twoje węzły i kształty.

```csharp
Scene scene = new Scene();
```

## Krok 3: Utwórz węzły

Twórz węzły w scenie, zarówno po lewej, jak i po prawej stronie.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

## Krok 4: Wyciągnięcie liniowe na lewym węźle

Wykonaj wytłaczanie liniowe w lewym węźle, korzystając z właściwości skrętu i plasterków.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## Krok 5: Wyciągnięcie liniowe na prawym węźle z przesunięciem skrętu

W prawym węźle wykonaj wytłaczanie liniowe, używając właściwości skrętu, przesunięcia skrętu i plasterków.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

## Krok 6: Zapisz scenę 3D

Zapisz scenę 3D w żądanym katalogu wyjściowym, określając format pliku jako WavefrontOBJ.

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Gratulacje! Pomyślnie zaimplementowałeś przesunięcie skrętu w wytłaczaniu liniowym przy użyciu Aspose.3D dla .NET.

## Wniosek

W tym samouczku zbadaliśmy potężne możliwości Aspose.3D dla .NET, szczególnie skupiając się na przesunięciu skrętu w wytłaczaniu liniowym. Dzięki tym nowo odkrytym umiejętnościom jesteś dobrze przygotowany do nadawania dynamiki swoim projektom 3D.

## Często zadawane pytania

### P1: Czy mogę używać Aspose.3D dla .NET z innymi językami programowania?

Odpowiedź 1: Aspose.3D obsługuje głównie języki .NET, ale Aspose udostępnia podobne biblioteki dla Java i innych platform.

### P2: Jak uzyskać tymczasową licencję na Aspose.3D dla .NET?

 A2: Odwiedź[ten link](https://purchase.aspose.com/temporary-license/)nabyć tymczasową licencję do celów testowych.

### P3: Czy istnieje forum społecznościowe dla Aspose.3D dla .NET?

 A3: Absolutnie! Dołącz do społeczności na[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) nawiązać kontakt z innymi programistami i poprosić o pomoc.

### P4: Czy dostępne są dodatkowe przykłady i dokumentacja?

 A4: Poznaj[dokumentacja](https://reference.aspose.com/3d/net/) obszerne przewodniki i przykłady.

### P5: Gdzie mogę kupić Aspose.3D dla .NET?

 A5: Udaj się do[ten link](https://purchase.aspose.com/buy) aby dokonać zakupu i odblokować pełny potencjał Aspose.3D.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
