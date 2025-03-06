---
title: Korzystanie z tokena anulowania
linktitle: Korzystanie z tokena anulowania
second_title: Aspose.3D API .NET
description: Poznaj płynny świat modelowania 3D dzięki Aspose.3D dla .NET. Naucz się efektywnie ładować i zapisywać dokumenty 3D za pomocą CancellationToken.
weight: 10
url: /pl/net/loading-and-saving/cancellation-token/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Korzystanie z tokena anulowania

## Wstęp

Witamy w naszym obszernym przewodniku na temat wykorzystania Aspose.3D dla .NET do ulepszenia projektów modelowania i renderowania 3D. Aspose.3D to potężna biblioteka, która umożliwia programistom .NET bezproblemową pracę z plikami 3D. W tym samouczku zagłębimy się w aspekty ładowania i zapisywania, koncentrując się w szczególności na wykorzystaniu tokena anulowania do wydajnego zarządzania zadaniami asynchronicznymi.

## Warunki wstępne

Zanim wyruszymy w tę podróż, upewnijmy się, że spełniliśmy następujące wymagania wstępne:

-  Aspose.3D dla .NET: Pobierz i zainstaluj bibliotekę z[Tutaj](https://releases.aspose.com/3d/net/).
- Środowisko .NET: Upewnij się, że masz skonfigurowane kompatybilne środowisko programistyczne .NET.
- Podstawowa znajomość języka C#: Zalecana jest znajomość języka programowania C#.

## Importuj przestrzenie nazw

Aby rozpocząć, upewnij się, że uwzględniłeś w projekcie niezbędne przestrzenie nazw. Te przestrzenie nazw zapewnią dostęp do funkcjonalności potrzebnych do manipulacji plikami 3D.

```csharp
using Aspose.ThreeD;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
```

## Ładowanie i zapisywanie - przy użyciu tokena anulowania

### Krok 1: Utwórz źródło tokenu anulowania

```csharp
// ExStart:Źródło tokenu anulowania

CancellationTokenSource cts = new CancellationTokenSource();
```

Tutaj tworzymy wystąpienie CancellationTokenSource, kluczowego komponentu do zarządzania anulowaniem w operacjach asynchronicznych.

### Krok 2: Zainicjuj scenę 3D

```csharp
Scene scene = new Scene();
```

Utwórz instancję klasy Scene. Będzie to płótno dla Twoich działań związanych z modelowaniem 3D.

### Krok 3: Ustaw limit czasu tokenu anulowania

```csharp
cts.CancelAfter(1000);
```

 Ustaw limit czasu anulowania za pomocą`CancelAfter` metoda. W tym przykładzie limit czasu ustawiono na 1000 milisekund (1 sekunda).

### Krok 4: Otwórz dokument 3D

```csharp
try
{
    scene.Open("Your Output Directory" + "document.fbx", cts.Token);
    Console.WriteLine("Import is done within 1000ms");
}
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
```

 Spróbuj otworzyć dokument 3D w określonym przedziale czasu. The`cts.Token` Parametr zapewnia, że operacja może zostać anulowana w przypadku przekroczenia ustawionego limitu czasu.

### Krok 5: Obsługa wyjątku importu

W przypadku wyjątku ImportException obsłuż go delikatnie, sprawdzając, czy został on spowodowany przez wyjątek OperationCanceledException.

```csharp
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
// ExEnd:CancellationTokenSource
```

## Wniosek

Gratulacje! Pomyślnie przeszedłeś przez proces używania Aspose.3D dla .NET z CancellationToken do zarządzania ładowaniem dokumentów 3D. Technika ta zapewnia wydajne i terminowe operacje importu, zwiększając ogólną wydajność aplikacji 3D.

## Często zadawane pytania

### P1: Czy Aspose.3D jest kompatybilny ze wszystkimi formatami plików 3D?

 O1: Aspose.3D obsługuje szeroką gamę formatów plików 3D, w tym FBX, STL, OBJ i inne. Patrz[dokumentacja](https://reference.aspose.com/3d/net/) dla pełnej listy.

### P2: Jak mogę uzyskać tymczasową licencję na Aspose.3D?

 A2: Uzyskaj tymczasową licencję, odwiedzając[ten link](https://purchase.aspose.com/temporary-license/).

### P3: Gdzie mogę znaleźć wsparcie dla Aspose.3D?

 A3: Dołącz do dyskusji społeczności na stronie[Forum Aspose.3D](https://forum.aspose.com/c/3d/18).

### P4: Czy mogę wypróbować Aspose.3D za darmo przed zakupem?

 Odpowiedź 4: Tak, poznaj funkcje dostępne w bezpłatnej wersji próbnej[Tutaj](https://releases.aspose.com/).

### P5: Jaka jest najnowsza wersja Aspose.3D dla .NET?

 A5: Bądź na bieżąco, sprawdzając[strona pobierania](https://releases.aspose.com/3d/net/) dla najnowszego wydania.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
