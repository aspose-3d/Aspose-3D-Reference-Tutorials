---
date: 2026-04-12
description: Dowiedz się, jak tworzyć sceny z sześcianami i zapisywać scenę jako FBX
  przy użyciu Aspose.3D dla .NET – przewodnik krok po kroku, wymagania wstępne i przykłady
  kodu.
keywords:
- how to create cube
- how to export fbx
- add mesh to node
- export scene as fbx
- save scene as fbx
linktitle: Tworzenie scen z sześcianami
second_title: Aspose.3D .NET API
title: Jak tworzyć sceny sześcianów przy użyciu Aspose.3D dla .NET
url: /pl/net/geometry-and-hierarchy/create-cube-scenes/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak tworzyć sceny sześcianu przy użyciu Aspose.3D dla .NET

## Wstęp

Gotowy, aby ożywić prosty sześcian 3‑D? W tym samouczku nauczysz się **tworzyć sceny sześcianu** przy użyciu Aspose.3D dla .NET, wyeksportować model jako plik FBX i zobaczyć wynik od razu. Niezależnie od tego, czy prototypujesz zasób gry, czy wizualizujesz dane, poniższe kroki zapewnią solidną podstawę, którą możesz rozbudować o tekstury, oświetlenie lub animację.

## Szybkie odpowiedzi
- **Co obejmuje samouczek?** Tworzenie siatki sześcianu, dodawanie siatki do węzła i zapisywanie sceny jako plik FBX.  
- **Jakiej biblioteki wymaga?** Aspose.3D dla .NET (dostępna darmowa wersja próbna).  
- **Czy potrzebna jest licencja do uruchomienia przykładu?** Tymczasowa lub próbna licencja działa w trakcie rozwoju i testów.  
- **Jakie IDE mogę używać?** Dowolne IDE kompatybilne z .NET (Visual Studio, Rider, VS Code).  
- **Jak długo to zajmuje?** Około 10 minut na napisanie, skompilowanie i uruchomienie kodu.

## Jak tworzyć sceny sześcianu przy użyciu Aspose.3D

Scena sześcianu to „Hello World” grafiki 3‑D. Pozwala zweryfikować, że Twój pipeline – od tworzenia siatki po **eksport sceny jako FBX** – działa poprawnie. Poniżej przeprowadzimy Cię przez każdy krok, wyjaśnimy „dlaczego” i pokażemy dokładnie, gdzie umieścić kod.

## Czym jest scena sześcianu 3D?

Scena sześcianu 3D to minimalny model trójwymiarowy składający się z pojedynczej geometrii sześcianu umieszczonej w grafie sceny. Służy jako „Hello World” grafiki 3D, pozwalając zweryfikować, że Twój pipeline – od tworzenia siatki po eksport pliku – działa poprawnie.

## Dlaczego tworzyć sceny sześcianu przy użyciu Aspose.3D?

* **Wsparcie wielu formatów:** Eksport do FBX, STL, OBJ i wielu innych formatów bez dodatkowych konwerterów.  
* **Czyste API .NET:** Brak zależności natywnych, idealne dla programistów C#.  
* **Bogaty zestaw funkcji:** Wbudowane kreatory siatek, obsługa materiałów i zarządzanie hierarchią sceny.  
* **Szybkie prototypowanie:** Napisz kilka linii kodu i uzyskaj gotowy plik 3D.  

## Wymagania wstępne

1. **Biblioteka Aspose.3D dla .NET** – pobierz i zainstaluj z [dokumentacji Aspose](https://reference.aspose.com/3d/net/).  
2. **Środowisko programistyczne** – Visual Studio 2022, Rider lub dowolny edytor obsługujący .NET 6+.  
3. **Podstawowa znajomość C#** – powinieneś być zaznajomiony z klasami, obiektami i aplikacjami konsolowymi.

## Importowanie przestrzeni nazw

Najpierw dodaj wymagane instrukcje `using`, aby kompilator wiedział, gdzie znajdują się typy Aspose.3D.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
```

## Przewodnik krok po kroku

### Krok 1: Inicjalizacja sceny

Utwórz pusty obiekt `Scene`, który będzie przechowywał wszystkie węzły, siatki, światła i kamery.

```csharp
// ExStart:CreateCubeScene
// Initialize scene object
Scene scene = new Scene();
```

### Krok 2: Utwórz węzeł dla sześcianu

`Node` pełni rolę kontenera dla geometrii. Nadaj mu przyjazną nazwę, aby później móc go odnaleźć w hierarchii.

```csharp
// Initialize Node class object
Node cubeNode = new Node("cube");
```

### Krok 3: Zbuduj siatkę

Aspose.3D udostępnia pomocnika o nazwie `Common`, który może wygenerować siatkę sześcianu przy użyciu kreatora wielokątów. Dzięki temu nie musisz ręcznie definiować wierzchołków i ścian.

```csharp
// Call Common class create mesh using polygon builder method to set mesh instance 
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

### Krok 4: Dodaj siatkę do węzła

Przypisz właśnie utworzoną siatkę do właściwości `Entity` węzła. Łączy to geometrię z grafem sceny.

```csharp
// Point node to the Mesh geometry
cubeNode.Entity = mesh;
```

### Krok 5: Dodaj węzeł do sceny

Wstaw węzeł sześcianu do korzenia sceny, aby stał się częścią końcowego wyniku.

```csharp
// Add Node to a scene
scene.RootNode.ChildNodes.Add(cubeNode);
```

### Krok 6: Jak wyeksportować FBX (zapisz scenę jako FBX)

Wybierz ścieżkę wyjściową i wyeksportuj scenę. Tutaj używamy formatu ASCII FBX 7400, który jest szeroko wspierany przez edytory 3D.

```csharp
// The path to the documents directory.
var output = "Your Output Directory" + "CubeScene.fbx";

// Save 3D scene in the supported file formats
scene.Save(output, FileFormat.FBX7400ASCII);
```

### Krok 7: Wyświetl komunikat sukcesu

Podaj użytkownikowi wyraźne potwierdzenie, że plik został zapisany pomyślnie.

```csharp
Console.WriteLine("\nCube Scene created successfully.\nFile saved at " + output);
```

## Typowe problemy i rozwiązania

| Problem | Dlaczego się pojawia | Rozwiązanie |
|-------|----------------|-----|
| **Błąd pliku nie znaleziono** podczas uruchamiania `scene.Save` | Katalog wyjściowy nie istnieje lub nie masz uprawnień do zapisu. | Utwórz najpierw katalog (`Directory.CreateDirectory`) lub użyj własnej ścieżki bezwzględnej. |
| **Pusty plik** po eksporcie | Siatka nie została dołączona do węzła lub węzeł nie został dodany do sceny. | Upewnij się, że wykonano `cubeNode.Entity = mesh;` oraz `scene.RootNode.ChildNodes.Add(cubeNode);`. |
| **Nieprawidłowy format** przy otwieraniu w przeglądarce | Użycie niewłaściwej wartości wyliczenia `FileFormat`. | Użyj `FileFormat.FBX7400ASCII` dla ASCII FBX lub `FileFormat.FBX7400Binary` dla binarnego. |

## Najczęściej zadawane pytania

**P: Czy Aspose.3D jest kompatybilny z różnymi formatami plików 3D?**  
O: Tak, Aspose.3D obsługuje FBX, STL, OBJ, GLTF i wiele innych, umożliwiając **zapis sceny jako FBX** lub w innych formatach jedną linią kodu.

**P: Czy mogę dostosować wygląd sześcianu?**  
O: Oczywiście. Możesz przypisać `Material` do siatki, zmienić jej kolor lub zastosować teksturę przy użyciu klasy `Material`.

**P: Gdzie mogę znaleźć dodatkowe wsparcie i zasoby?**  
O: Odwiedź [forum Aspose.3D](https://forum.aspose.com/c/3d/18) w celu uzyskania pomocy społeczności i dyskusji.

**P: Czy dostępna jest darmowa wersja próbna?**  
O: Tak, możesz wypróbować darmową wersję próbną [tutaj](https://releases.aspose.com/).

**P: Jak mogę uzyskać tymczasową licencję dla Aspose.3D?**  
O: Uzyskaj tymczasową licencję [tutaj](https://purchase.aspose.com/temporary-license/).

## Zakończenie

W tym przewodniku pokazaliśmy **jak tworzyć sceny sześcianu** krok po kroku, od inicjalizacji `Scene` po **eksport sceny jako FBX**. Masz teraz solidną bazę do eksperymentowania z bardziej złożonymi geometriami, dodawania tekstur, świateł i nawet animowania modeli. Kontynuuj eksplorację API Aspose.3D – możliwości są praktycznie nieograniczone.

---

**Ostatnia aktualizacja:** 2026-04-12  
**Testowano z:** Aspose.3D dla .NET 24.11 (najnowsza w momencie pisania)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}