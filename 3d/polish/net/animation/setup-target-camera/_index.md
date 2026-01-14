---
date: 2026-01-14
description: Dowiedz się, jak dodać kamerę do sceny i wyeksportować scenę jako FBX
  przy użyciu Aspose.3D dla .NET – krok po kroku przewodnik, jak ustawić cele kamery
  i tworzyć animacje 3D.
linktitle: Add Camera to Scene and Set Up Targets for 3D Animation
second_title: Aspose.3D .NET API
title: Dodaj kamerę do sceny i ustaw cele dla animacji 3D
url: /pl/net/animation/setup-target-camera/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Dodaj kamerę do sceny i ustaw cele dla animacji 3D

## Wprowadzenie

Jeśli tworzysz animację 3D, pierwszą rzeczą, której potrzebujesz, jest dobrze ustawiona kamera. W tym samouczku nauczysz się **jak dodać kamerę do sceny**, określić jej cel i w końcu **wyeksportować scenę jako FBX** przy użyciu Aspose.3D dla .NET. Przejdziemy przez każdy krok, wyjaśnimy, dlaczego jest to ważne, i podamy praktyczne wskazówki, abyś mógł tworzyć atrakcyjne animacje 3D z pewnością.

## Szybkie odpowiedzi
- **Jaki jest pierwszy krok, aby dodać kamerę?** Zainicjalizuj obiekt `Scene`, który będzie hostował węzeł kamery.  
- **Jaki format pliku jest używany do eksportu w tym przewodniku?** FBX (`.fbx`).  
- **Czy potrzebuję licencji, aby uruchomić przykładowy kod?** Darmowa wersja próbna wystarcza do oceny; licencja komercyjna jest wymagana w produkcji.  
- **Jakie wersje .NET są obsługiwane?** .NET Framework 4.5+, .NET Core 3.1+, .NET 5/6+.  
- **Czy mogę zmienić pozycję kamery po jej utworzeniu?** Tak – zmodyfikuj `cameraNode.Transform.Translation` w dowolnym momencie.

## Czym jest **add camera to scene**?
Dodanie kamery do sceny oznacza stworzenie encji `Camera`, podłączenie jej do węzła w grafie sceny oraz ustawienie jej tak, aby „patrzyła na” punkt docelowy. Definiuje to perspektywę obserwatora podczas renderowania lub eksportu sceny.

## Dlaczego ustawiać cele kamery i eksportować jako FBX?
- **Kontrola punktu widzenia** – precyzyjne ustawienie kamery pozwala ująć animację dokładnie tak, jak sobie wyobrażasz.  
- **Interoperacyjność** – FBX jest szeroko wspierany przez silniki gier, Maya, Blender i inne narzędzia 3D, co ułatwia udostępnianie zasobów.  
- **Ponowne użycie zasobów** – po zapisaniu kamery i jej celu możesz ponownie wykorzystać scenę w wielu projektach.

## Wymagania wstępne

Zanim zanurzysz się w samouczek, upewnij się, że masz następujące wymagania wstępne:

- Podstawowa znajomość C# i platformy .NET.  
- Zainstalowana biblioteka Aspose.3D dla .NET. Możesz ją pobrać [tutaj](https://releases.aspose.com/3d/net/).  
- Środowisko programistyczne gotowe do programowania 3D.

## Importuj przestrzenie nazw

Aby rozpocząć proces, zaimportuj niezbędne przestrzenie nazw do swojego projektu. Te przestrzenie nazw są niezbędne do wykorzystania możliwości Aspose.3D dla .NET:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

## Przewodnik krok po kroku

### Krok 1: Zainicjalizuj obiekt sceny

Rozpocznij od zainicjowania obiektu sceny. Służy on jako płótno, na którym ożyje Twoja animacja 3D.

```csharp
// ExStart:SetupTargetAndCamera
// Initialize scene object
Scene scene = new Scene();
```

### Krok 2: Utwórz węzeł kamery

Następnie utwórz węzeł podrzędny, który będzie przechowywał kamerę. Nadanie węzłowi znaczącej nazwy pomaga utrzymać hierarchię sceny w porządku.

```csharp
// Get a child node object
Node cameraNode = scene.RootNode.CreateChildNode("camera", new Camera());
```

### Krok 3: Ustaw pozycję kamery

Określ translację dla węzła kamery. To ustala początkową pozycję kamery w przestrzeni 3D.

```csharp
// Set camera node translation
cameraNode.Transform.Translation = new Vector3(100, 20, 0);
```

### Krok 4: Zdefiniuj cel kamery

Kamera potrzebuje punktu docelowego, na który ma patrzeć. Tworzymy kolejny węzeł podrzędny, który pełni rolę punktu ogniskowego i przypisujemy go do właściwości `Target` kamery.

```csharp
cameraNode.GetEntity<Camera>().Target = scene.RootNode.CreateChildNode("target");
```

### Krok 5: Zapisz skonfigurowaną scenę

Na koniec wyeksportuj scenę do pliku FBX (lub innego obsługiwanego formatu). Zastąp `"Your Output Directory"` rzeczywistą ścieżką, w której chcesz zapisać plik.

```csharp
var output = "Your Output Directory" + "camera-test.fbx";
scene.Save(output);
```

## Typowe problemy i rozwiązania

| Problem | Rozwiązanie |
|-------|----------|
| **Kamera pojawia się pod niewłaściwym kątem** | Sprawdź, czy węzeł docelowy jest umieszczony tam, gdzie tego oczekujesz. Możesz także ustawić `cameraNode.GetEntity<Camera>().UpVector`, aby kontrolować orientację. |
| **Wyeksportowany FBX nie otwiera się w innych narzędziach** | Upewnij się, że używasz najnowszej wersji Aspose.3D (biblioteka automatycznie zapisuje kompatybilną wersję FBX). |
| **Błąd: ścieżka nie znaleziona przy `scene.Save`** | Użyj ścieżki bezwzględnej lub upewnij się, że katalog wyjściowy istnieje przed wywołaniem `Save`. |

## FAQ

### Q1: Czy Aspose.3D jest kompatybilny z innymi narzędziami do modelowania 3D?

Aspose.3D obsługuje różne formaty plików, zapewniając kompatybilność z popularnymi narzędziami do modelowania 3D.

### Q2: Czy mogę używać Aspose.3D do tworzenia gier?

Zdecydowanie! Aspose.3D umożliwia programistom łatwe tworzenie zasobów 3D do gier.

### Q3: Gdzie mogę znaleźć dodatkowe wsparcie dla Aspose.3D?

Odwiedź [forum Aspose.3D](https://forum.aspose.com/c/3d/18), aby uzyskać wsparcie społeczności i dyskusje.

### Q4: Czy dostępna jest darmowa wersja próbna?

Tak, możesz wypróbować darmową wersję próbną [tutaj](https://releases.aspose.com/).

### Q5: Jak uzyskać tymczasową licencję?

Uzyskaj tymczasową licencję [tutaj](https://purchase.aspose.com/temporary-license/).

## Podsumowanie

Teraz wiesz, jak **add camera to scene**, ustawić jej cel i wyeksportować wynik jako plik FBX przy użyciu Aspose.3D dla .NET. Mając te podstawy, możesz zacząć tworzyć bardziej złożone animacje, eksperymentować z wieloma kamerami i integrować wyeksportowane sceny z silnikami gier lub pipeline'ami efektów wizualnych.

---

**Ostatnia aktualizacja:** 2026-01-14  
**Testowano z:** Aspose.3D 24.11 for .NET (latest at time of writing)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}