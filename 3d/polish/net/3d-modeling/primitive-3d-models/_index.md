---
date: 2026-03-26
description: Dowiedz się, jak tworzyć modele 3‑wymiarowych sześcianów i walców oraz
  zapisywać scenę w formacie FBX przy użyciu Aspose.3D dla .NET.
linktitle: Create 3D Box and Cylinder Models with Aspose.3D for .NET
second_title: Aspose.3D .NET API
title: 'Utwórz modele 3D: sześcianu i walca przy użyciu Aspose.3D dla .NET'
url: /pl/net/3d-modeling/primitive-3d-models/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Utwórz modele pudełka i walca 3D przy użyciu Aspose.3D

## Wprowadzenie

Witamy w ekscytującym świecie modelowania 3D z Aspose.3D dla .NET! W tym samouczku nauczysz się **jak utworzyć 3d box** prymitywy, dodać walec i wyeksportować całą scenę do formatu FBX. Niezależnie od tego, czy tworzysz szybki prototyp, czy gotowy do produkcji pipeline zasobów, te kroki zapewnią solidne podstawy do pracy z geometrią 3D w .NET.

## Szybkie odpowiedzi
- **Co obejmuje ten samouczek?** Tworzenie pudełka 3D, walca 3D i zapisywanie sceny jako plik FBX.  
- **Jakiej biblioteki wymaga?** Aspose.3D dla .NET (pobierz z oficjalnej strony).  
- **Jak długo trwa implementacja?** Około 10‑15 minut dla podstawowej sceny.  
- **Czy mogę dostosować wymiary?** Tak – konstruktory Box i Cylinder przyjmują parametry rozmiaru.  
- **Czy potrzebna jest licencja do produkcji?** Wymagana jest ważna licencja Aspose.3D dla wersji nie‑trial.

## Co to jest „create 3d box”?

Tworzenie pudełka 3D oznacza generowanie prostego sześcianu lub prostopadłościanu, który może służyć jako element budulcowy dla bardziej złożonych modeli. W Aspose.3D klasa `Box` reprezentuje ten prymityw i możesz dodać go do sceny jedną linią kodu.

## Dlaczego używać Aspose.3D do tego zadania?

- **Czyste API .NET:** Brak zależności natywnych, idealne dla projektów C# i VB.NET.  
- **Szerokie wsparcie formatów:** Eksport do FBX, OBJ, STL i wielu innych.  
- **Wysokopoziomowe prymitywy:** Box, Cylinder, Sphere itp., pozwalają skupić się na logice, a nie na niskopoziomowej konstrukcji siatek.  
- **Zoptymalizowana wydajność:** Efektywnie obsługuje duże sceny.

## Wymagania wstępne

Zanim zaczniemy, upewnij się, że masz:

- Aspose.3D dla .NET: Pobierz i zainstaluj bibliotekę z [linku do pobrania](https://releases.aspose.com/3d/net/).  
- Środowisko programistyczne .NET (Visual Studio, Rider lub VS Code) kompatybilne z wersją Aspose.3D, którą zainstalowałeś.

Teraz, gdy masz niezbędne elementy, rozpocznijmy budowanie sceny krok po kroku.

## Importowanie przestrzeni nazw

Zacznij od zaimportowania niezbędnych przestrzeni nazw, aby uzyskać dostęp do funkcjonalności oferowanej przez Aspose.3D:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```

Mając te przestrzenie nazw, jesteś gotowy, aby wykorzystać moc Aspose.3D w swojej aplikacji .NET.

## Krok 1: Inicjalizacja obiektu Scene

```csharp
// Initialize a Scene object
Scene scene = new Scene();
```

Obiekt `Scene` pełni rolę płótna, na którym będą znajdować się wszystkie elementy 3D.

## Krok 2: Utworzenie modelu pudełka

```csharp
// Create a Box model
scene.RootNode.CreateChildNode("box", new Box());
```

Ta linia dodaje prymityw **3D box** do korzenia Twojej sceny. Później możesz dostosować jego szerokość, wysokość i głębokość, przekazując parametry do konstruktora `Box`.

## Krok 3: Utworzenie modelu walca

```csharp
// Create a Cylinder model
scene.RootNode.CreateChildNode("cylinder", new Cylinder());
```

Walec uzupełnia pudełko i pokazuje, jak łatwo jest łączyć różne prymitywy.

## Krok 4: Zapis rysunku w formacie FBX

```csharp
// Save drawing in the FBX format
var output = "Your Output Directory" + "test.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Tutaj **konwertujemy model do FBX**, zapisując całą scenę jako plik FBX. Możesz swobodnie zmienić ścieżkę i nazwę pliku, aby dopasować je do struktury swojego projektu.

## Krok 5: Wyświetlenie komunikatu sukcesu

```csharp
// Display success message
Console.WriteLine("\nBuilding a scene from primitive 3D models successfully.\nFile saved at " + output);
```

Przyjazny komunikat w konsoli potwierdza, że operacja **build 3d scene** zakończyła się pomyślnie bez błędów.

## Typowe problemy i wskazówki

- **Katalog wyjściowy nie istnieje:** Upewnij się, że folder w `output` istnieje lub użyj `Directory.CreateDirectory()` przed zapisem.  
- **Licencja nie ustawiona:** W wersji nie‑trial wywołaj `License license = new License(); license.SetLicense("Aspose.3D.lic");` przed utworzeniem obiektu `Scene`.  
- **Niestandardowe wymiary:** Użyj `new Box(width, height, depth)` lub `new Cylinder(radius, height)`, aby kontrolować rozmiar.

## Podsumowanie

Gratulacje! Pomyślnie **create 3d box** i prymitywy walca, zbudowałeś prostą scenę i zapisałeś ją jako plik FBX przy użyciu Aspose.3D dla .NET. Podstawy znajdują się teraz w Twoim zestawie narzędzi i możesz przeglądać [dokumentację](https://reference.aspose.com/3d/net/) w celu poznania bardziej zaawansowanych funkcji, takich jak materiały, oświetlenie i animacja.

## Najczęściej zadawane pytania

### Q1: Czy mogę używać Aspose.3D dla .NET z innymi językami programowania?
A1: Aspose.3D głównie wspiera .NET, ale dostępne są inne wersje dla Javy i innych platform.

### Q2: Czy dostępna jest darmowa wersja próbna?
A2: Tak, możesz przetestować możliwości Aspose.3D korzystając z [darmowej wersji próbnej](https://releases.aspose.com/).

### Q3: Gdzie mogę znaleźć wsparcie dla Aspose.3D dla .NET?
A3: Odwiedź [forum Aspose.3D](https://forum.aspose.com/c/3d/18), aby uzyskać wsparcie społeczności i dyskusje.

### Q4: Jak mogę uzyskać tymczasową licencję?
A4: Tymczasową licencję możesz uzyskać [tutaj](https://purchase.aspose.com/temporary-license/).

### Q5: Czy dostępne są przykładowe samouczki?
A5: Tak, przeglądaj więcej samouczków i przykładów w [dokumentacji](https://reference.aspose.com/3d/net/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2026-03-26  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

---