---
date: 2026-06-03
description: Dowiedz się, jak wyeksportować scenę jako FBX oraz tworzyć cylindry 3D,
  pudełka i inne modele prymitywne przy użyciu Aspose.3D for Java.
keywords:
- export scene as fbx
- convert 3d model fbx
- Aspose 3D primitives
- Java 3D modeling
linktitle: Tworzenie prymitywnych modeli 3D przy użyciu Aspose.3D for Java
schemas:
- author: Aspose
  dateModified: '2026-06-03'
  description: Learn how to export scene as FBX and create 3D cylinder, box, and other
    primitive models using Aspose.3D for Java.
  headline: Export scene as FBX and build cylinder with Aspose.3D Java
  type: TechArticle
- description: Learn how to export scene as FBX and create 3D cylinder, box, and other
    primitive models using Aspose.3D for Java.
  name: Export scene as FBX and build cylinder with Aspose.3D Java
  steps:
  - name: Initialize a Scene Object
    text: The `Scene` class is Aspose.3D's top‑level container that holds all nodes,
      lights, cameras, and materials in memory.
  - name: Build a 3D box model
    text: The `Box` class represents a rectangular prism and is useful for testing
      the coordinate system. Adding it as a child of the scene’s root node positions
      it at the origin.
  - name: Create a 3D cylinder model
    text: The `Cylinder` class is Aspose.3D's built‑in cylinder primitive. It comes
      with default dimensions (radius = 1, height = 2) but you can customise them
      via its constructor.
  - name: Save the drawing in the FBX format
    text: After assembling the scene, export it so other tools (e.g., Unity, Blender)
      can read it. We use the `FBX7500ASCII` format, which is widely supported and
      human‑readable.
  type: HowTo
- questions:
  - answer: Aspose.3D primarily supports Java, but there are versions available for
      .NET and C++ as well.
    question: Can I use Aspose.3D for Java with other programming languages?
  - answer: Absolutely. It provides a comprehensive set of features—including mesh
      manipulation, material assignment, and animation—making it suitable for both
      simple primitives and intricate models.
    question: Is Aspose.3D suitable for complex 3D modeling tasks?
  - answer: Visit the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) for community
      support and discussions.
    question: Where can I find additional help and support?
  - answer: Yes, you can explore a [free trial](https://releases.aspose.com/) before
      making a purchase decision.
    question: Can I try Aspose.3D before purchasing?
  - answer: You can obtain a [temporary license](https://purchase.aspose.com/temporary-license/)
      for Aspose.3D through the website.
    question: How do I obtain a temporary license for Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
title: Eksportuj scenę jako FBX i zbuduj cylinder przy użyciu Aspose.3D Java
url: /pl/java/primitive-3d-models/building-primitive-3d-models/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Eksportuj scenę jako FBX i zbuduj cylinder przy użyciu Aspose.3D Java

## Wprowadzenie

Jeśli kiedykolwiek potrzebowałeś **utworzyć cylinder 3D** (lub dowolny inny podstawowy kształt) bezpośrednio w kodzie Java, Aspose.3D sprawia, że zadanie jest bezproblemowe. W tym samouczku przeprowadzimy Cię przez cały proces — od konfiguracji środowiska po **eksport sceny jako FBX** — abyś od razu mógł generować geometrię 3D programowo. Zobaczysz, jak biblioteka obsługuje prymitywy, jak je organizować w grafie sceny oraz jak zapisać wynik w formacie, który może odczytać Unity, Blender lub inne narzędzie 3D.

## Szybkie odpowiedzi
- **Jaką bibliotekę mogę użyć do tworzenia cylindra 3D w Javie?** Aspose.3D for Java.  
- **Do jakiego formatu mogę wyeksportować scenę?** FBX (ASCII 7500) przy użyciu `FileFormat.FBX7500ASCII`.  
- **Czy potrzebuję licencji do rozwoju?** Darmowa wersja próbna działa do testów; stała licencja jest wymagana w produkcji.  
- **Jakie główne prymitywy są obsługiwane?** Box, Cylinder, Sphere, Cone oraz ponad 10 dodatkowych kształtów.  
- **Czy kod jest kompatybilny z Java 8 i nowszymi?** Tak, Aspose.3D obsługuje JDK 8+.

## Co to jest prymityw cylinder 3D?

Prymityw cylinder to podstawowy kształt geometryczny określany przez promień i wysokość. W wielu pipeline'ach 3D służy jako element budulcowy bardziej złożonych modeli, takich jak rury, koła czy kolumny architektoniczne. Aspose.3D udostępnia gotową klasę `Cylinder`, więc nie musisz ręcznie obliczać wierzchołków.

## Dlaczego warto używać Aspose.3D dla Java?

Aspose.3D for Java oferuje kompleksowy, czysto‑Java silnik 3D, który eliminuje potrzebę natywnych bibliotek, co czyni go idealnym do tworzenia aplikacji wieloplatformowych. Obsługuje szeroką gamę formatów importu i eksportu, zapewnia solidny graf sceny do organizacji hierarchicznej oraz zawiera wbudowane prymitywy, które pozwalają tworzyć geometrię przy minimalnym kodzie. Te funkcje razem przyspieszają rozwój i zmniejszają koszty utrzymania.

- **Pełnoprawny silnik 3D** – obsługuje import/eksport **ponad 30** popularnych formatów (FBX, OBJ, STL, GLTF, 3DS, itp.).  
- **Czyste API Java** – brak zależności natywnych, idealne dla projektów wieloplatformowych.  
- **Solidny graf sceny** – umożliwia hierarchiczną organizację obiektów, co ułatwia zarządzanie dużymi scenami.  
- **Łatwa licencja** – rozpocznij od wersji próbnej, a następnie przejdź na stałą licencję po uruchomieniu.

## Wymagania wstępne

Zanim zagłębisz się w kod, upewnij się, że masz:

1. **Java Development Kit (JDK)** – zainstalowany JDK 8 lub nowszy na Twoim komputerze.  
2. **Bibliotekę Aspose.3D for Java** – pobierz i zainstaluj ją ze [strony pobierania](https://releases.aspose.com/3d/java/).  

## Importowanie pakietów

Rozpocznij od zaimportowania głównego przestrzeni nazw Aspose.3D. Daje to dostęp do `Scene`, `Box`, `Cylinder` oraz stałych formatów plików.

```java
import com.aspose.threed.*;
```

Teraz, gdy biblioteka jest już zaimportowana, utwórzmy scenę i dodajmy kilka prymitywnej geometrii.

## Jak wyeksportować scenę jako FBX i utworzyć prymitywy 3D?

Załaduj nowy obiekt `Scene`, dodaj węzły prymitywne (Box, Cylinder, itp.), a następnie wywołaj `save` z formatem FBX7500ASCII. W zaledwie kilku linijkach uzyskasz w pełni funkcjonalny plik FBX, który można otworzyć w dowolnym głównym edytorze 3D, umożliwiając płynną integrację z silnikami gier, pipeline'ami renderującymi lub aplikacjami AR/VR.

### Krok 1: Zainicjalizuj obiekt Scene

Klasa `Scene` jest najwyższym kontenerem Aspose.3D, który przechowuje w pamięci wszystkie węzły, światła, kamery i materiały.

```java
// The path to the documents directory.
String myDir = "Your Document Directory";

// Initialize a Scene object
Scene scene = new Scene();
```

### Krok 2: Zbuduj model pudełka 3D

Klasa `Box` reprezentuje prostopadłościan i jest przydatna do testowania układu współrzędnych. Dodanie jej jako dziecka węzła głównego sceny umieszcza ją w punkcie zerowym.

```java
// Create a Box model
scene.getRootNode().createChildNode("box", new Box());
```

### Krok 3: Utwórz model cylindra 3D

Klasa `Cylinder` jest wbudowanym prymitywem cylindra w Aspose.3D. Ma domyślne wymiary (promień = 1, wysokość = 2), ale możesz je dostosować za pomocą konstruktora.

```java
// Create a Cylinder model
scene.getRootNode().createChildNode("cylinder", new Cylinder());
```

### Krok 4: Zapisz rysunek w formacie FBX

Po złożeniu sceny wyeksportuj ją, aby inne narzędzia (np. Unity, Blender) mogły ją odczytać. Używamy formatu `FBX7500ASCII`, który jest szeroko wspierany i czytelny dla człowieka.

```java
// Save drawing in the FBX format
myDir = myDir + "test.fbx";
scene.save(myDir, FileFormat.FBX7500ASCII);
```

## Typowe problemy i rozwiązania

| Problem | Dlaczego się pojawia | Rozwiązanie |
|-------|----------------|-----|
| **Plik nie znaleziony** przy zapisywaniu | `myDir` wskazuje na nieistniejący folder | Upewnij się, że katalog istnieje lub utwórz go za pomocą `new File(myDir).mkdirs();` |
| **Pusta scena** po eksporcie | Nie dodano żadnych węzłów przed wywołaniem `save` | Sprawdź, czy wywołania `createChildNode` są wykonywane (debuguj za pomocą `scene.getRootNode().getChildCount()` ) |
| **Wyjątek licencyjny** | Uruchamianie bez ważnej licencji w produkcji | Zastosuj tymczasową lub stałą licencję używając `License license = new License(); license.setLicense("Aspose.3D.Java.lic");` |

## Najczęściej zadawane pytania

**Q: Czy mogę używać Aspose.3D for Java z innymi językami programowania?**  
A: Aspose.3D głównie obsługuje Javę, ale dostępne są wersje dla .NET i C++.

**Q: Czy Aspose.3D jest odpowiedni do złożonych zadań modelowania 3D?**  
A: Zdecydowanie. Dostarcza kompleksowy zestaw funkcji — w tym manipulację siatką, przypisywanie materiałów i animację — co czyni go odpowiednim zarówno dla prostych prymitywów, jak i skomplikowanych modeli.

**Q: Gdzie mogę znaleźć dodatkową pomoc i wsparcie?**  
A: Odwiedź [Forum Aspose.3D](https://forum.aspose.com/c/3d/18) aby uzyskać wsparcie społeczności i dyskusje.

**Q: Czy mogę wypróbować Aspose.3D przed zakupem?**  
A: Tak, możesz wypróbować [bezpłatną wersję próbną](https://releases.aspose.com/) przed podjęciem decyzji o zakupie.

**Q: Jak uzyskać tymczasową licencję dla Aspose.3D?**  
A: Możesz uzyskać [tymczasową licencję](https://purchase.aspose.com/temporary-license/) dla Aspose.3D poprzez stronę internetową.

## Zakończenie

Teraz nauczyłeś się **eksportować scenę jako FBX** oraz **tworzyć cylinder 3D**, pudełko i inne modele prymitywne przy użyciu Aspose.3D for Java. Śmiało eksperymentuj z dodatkowymi prymitywami, takimi jak Sphere, Cone czy Torus, i badaj przypisywanie materiałów, aby nadać modelom realistyczny wygląd. Gdy poczujesz się pewnie, możesz zintegrować wygenerowane pliki FBX z silnikami gier, pipeline'ami AR/VR lub dowolnym dalszym przepływem pracy 3D.

---

**Last Updated:** 2026-06-03  
**Tested With:** Aspose.3D for Java 24.11 (latest at time of writing)  
**Author:** Aspose

## Powiązane samouczki

- [Jak wyeksportować scenę do FBX i pobrać informacje o scenie 3D w Javie](/3d/java/3d-scenes-and-models/get-scene-information/)
- [Jak wyeksportować FBX i zbudować hierarchie węzłów w Javie](/3d/java/geometry/build-node-hierarchies/)
- [Jak tworzyć modele cylindrów z Aspose.3D for Java](/3d/java/cylinders/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< blocks/products/products-backtop-button >}}
{{< /blocks/products/pf/main-wrap-class >}}