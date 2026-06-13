---
date: 2026-06-13
description: Poznaj samouczek grafiki 3D w języku Java dotyczący sterowania środkiem
  w linear extrusion przy użyciu Aspose.3D, w tym jak ustawić rounding radius i zapisać
  plik OBJ w Javie.
keywords:
- create 3d mesh java
- set rounding radius
- export 3d model obj
- save obj file java
- aspose 3d export obj
linktitle: Sterowanie środkiem w linear extrusion przy użyciu Aspose.3D dla Java
schemas:
- author: Aspose
  dateModified: '2026-06-13'
  description: Learn a java 3d graphics tutorial on controlling the center in linear
    extrusion with Aspose.3D, including how to set rounding radius and save OBJ file
    java.
  headline: Create 3D Mesh Java – Center in Linear Extrusion
  type: TechArticle
- description: Learn a java 3d graphics tutorial on controlling the center in linear
    extrusion with Aspose.3D, including how to set rounding radius and save OBJ file
    java.
  name: Create 3D Mesh Java – Center in Linear Extrusion
  steps:
  - name: Set Up the Base Profile
    text: First, create the 2‑D shape that will be extruded. Here we use a rectangle
      and **set rounding radius** to 0.3, which smooths the corners and demonstrates
      how to **round extrusion corners**.
  - name: Create a 3D Scene
    text: '**Scene** is the top‑level container that holds all 3‑D objects, lights,
      and cameras.'
  - name: Add Left and Right Nodes
    text: A **Node** represents a transformable object in the scene graph, allowing
      positioning and hierarchy.
  - name: Linear Extrusion – No Center (Left Node)
    text: '**LinearExtrusion** converts a 2‑D profile into a 3‑D mesh by sweeping
      it along a straight line. **setCenter(boolean)** toggles whether the extrusion
      is centered around the profile origin.'
  - name: Add a Ground Plane for Reference (Left Node)
    text: A thin box acts as a visual floor, helping you see the extrusion’s orientation.
  - name: Linear Extrusion – Centered (Right Node)
    text: Now repeat the extrusion, this time enabling `center`. The geometry will
      be symmetric around the profile’s origin, giving you a perfectly balanced **create
      3d mesh java** result.
  - name: Add a Ground Plane for Reference (Right Node)
    text: Same ground plane for the right side, making the comparison clear.
  - name: Save the 3D Scene
    text: Finally, export the entire scene to a Wavefront OBJ file – a format readily
      usable in most 3‑D editors. The `save` method automatically converts the mesh
      to the OBJ specification, allowing you to **save obj file java** without additional
      post‑processing.
  type: HowTo
- questions:
  - answer: It determines whether the extrusion is symmetric around the profile's
      origin.
    question: What does the center property do?
  - answer: A temporary license works for testing; a full license is required for
      production.
    question: Do I need a license to run the code?
  - answer: The scene is saved as a Wavefront OBJ file.
    question: Which file format is used for the result?
  - answer: Yes, use `setSlices(int)` on the `LinearExtrusion` object.
    question: Can I change the number of slices?
  - answer: Absolutely – it supports all modern Java versions.
    question: Is Aspose.3D compatible with Java 8+?
  type: FAQPage
second_title: Aspose.3D Java API
title: Utwórz siatkę 3D Java – Center in Linear Extrusion
url: /pl/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Utwórz siatkę 3D w Javie – Środek w ekstruzji liniowej

## Wstęp

Jeśli tworzysz wizualizacje 3‑D w Javie, opanowanie technik ekstruzji jest niezbędne. Ten **java 3d graphics tutorial** pokazuje, jak **create 3d mesh java** obiekty, kontrolując środek ekstruzji liniowej za pomocą Aspose.3D for Java. Po zakończeniu tego przewodnika zrozumiesz, dlaczego właściwość `center` ma znaczenie, jak **set rounding radius**, oraz jak **save obj file java**‑kompatybilny wynik. Zobaczysz także, jak **export 3d model obj** do użycia w dowolnym głównym edytorze 3‑D.

## Szybkie odpowiedzi
- **Co robi właściwość center?** Określa, czy ekstruzja jest symetryczna względem początku profilu.  
- **Czy potrzebuję licencji, aby uruchomić kod?** Tymczasowa licencja działa w testach; pełna licencja jest wymagana w produkcji.  
- **Jaki format pliku jest używany dla wyniku?** Scena jest zapisywana jako plik Wavefront OBJ.  
- **Czy mogę zmienić liczbę przekrojów?** Tak, użyj `setSlices(int)` na obiekcie `LinearExtrusion`.  
- **Czy Aspose.3D jest kompatybilny z Java 8+?** Zdecydowanie – obsługuje wszystkie współczesne wersje Java.

## Czym jest java 3d graphics tutorial?

**java 3d graphics tutorial** to przewodnik krok po kroku, który uczy, jak używać bibliotek Java do tworzenia, manipulacji i renderowania trójwymiarowych obiektów. W tym tutorialu nauczysz się **create 3d mesh java** poprzez konwersję profilu 2‑D na pełny model 3‑D, kontrolować jego centralne wyrównanie, zaokrąglać narożniki ekstruzji i ostatecznie eksportować wynik jako plik OBJ, który może odczytać każdy program 3‑D.

## Dlaczego używać Aspose.3D for Java?

Aspose.3D for Java udostępnia wysokopoziomowe API, które eliminuje potrzebę ręcznych obliczeń siatek, pozwalając skupić się na projektowaniu, a nie na niskopoziomowej geometrii. Obsługuje **ponad 50 formatów wejściowych i wyjściowych** — w tym OBJ, FBX, STL i GLTF — dzięki czemu możesz **export 3d model obj** lub inny format jednym wywołaniem metody. Biblioteka przetwarza sceny liczące setki stron bez wczytywania całego pliku do pamięci, zapewniając **do 3× szybszą wydajność** w porównaniu z surowymi potokami OpenGL na typowym sprzęcie serwerowym.

## Wymagania wstępne

1. **Java Development Environment** – zainstalowany JDK 8 lub nowszy.  
2. **Aspose.3D for Java** – Pobierz bibliotekę i dokumentację [here](https://reference.aspose.com/3d/java/).  
3. **Document Directory** – Utwórz folder na swoim komputerze do przechowywania wygenerowanych plików; będziemy go nazywać **„Your Document Directory.”**

## Importowanie pakietów

W swoim IDE Java zaimportuj klasy Aspose.3D, które będą potrzebne. Dzięki temu kompilator uzyska dostęp do funkcji ekstruzji i budowania sceny.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Przewodnik krok po kroku

### Krok 1: Przygotuj profil bazowy

Najpierw utwórz kształt 2‑D, który będzie ekstruzowany. Tutaj używamy prostokąta i **set rounding radius** na 0,3, co wygładza narożniki i demonstruje, jak **round extrusion corners**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### Krok 2: Utwórz scenę 3D

**Scene** jest kontenerem najwyższego poziomu, który przechowuje wszystkie obiekty 3‑D, światła i kamery.

```java
Scene scene = new Scene();
```

### Krok 3: Dodaj węzły lewy i prawy

**Node** reprezentuje obiekt transformowalny w grafie sceny, umożliwiając pozycjonowanie i hierarchię.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Krok 4: Ekstruzja liniowa – bez środka (lewy węzeł)

**LinearExtrusion** przekształca profil 2‑D w siatkę 3‑D, przesuwając go wzdłuż prostej linii.  
**setCenter(boolean)** przełącza, czy ekstruzja jest wyśrodkowana względem początku profilu.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

### Krok 5: Dodaj płaszczyznę podłoża jako odniesienie (lewy węzeł)

Cienka skrzynka pełni rolę wizualnej podłogi, pomagając zobaczyć orientację ekstruzji.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

### Krok 6: Ekstruzja liniowa – wyśrodkowana (prawy węzeł)

Teraz powtórz ekstruzję, tym razem włączając `center`. Geometria będzie symetryczna względem początku profilu, dając idealnie zrównoważony wynik **create 3d mesh java**.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

### Krok 7: Dodaj płaszczyznę podłoża jako odniesienie (prawy węzeł)

Ta sama płaszczyzna podłoża po prawej stronie, aby porównanie było czytelne.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

### Krok 8: Zapisz scenę 3D

Na koniec wyeksportuj całą scenę do pliku Wavefront OBJ – formatu łatwo używanego w większości edytorów 3‑D. Metoda `save` automatycznie konwertuje siatkę do specyfikacji OBJ, umożliwiając **save obj file java** bez dodatkowego przetwarzania.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Typowe problemy i rozwiązania

| Problem | Dlaczego się pojawia | Rozwiązanie |
|---------|----------------------|-------------|
| **Ekstruzja jest przesunięta** | `setCenter(false)` pozostawia profil zakotwiczony w jego rogu. | Użyj `setCenter(true)`, aby uzyskać wyniki symetryczne. |
| **Plik OBJ jest pusty** | Ścieżka katalogu wyjściowego jest nieprawidłowa lub brakuje uprawnień do zapisu. | Sprawdź, czy `MyDir` wskazuje istniejący folder i aplikacja ma dostęp do zapisu. |
| **Zaokrąglone narożniki wyglądają ostro** | Promień zaokrąglenia jest zbyt mały w stosunku do rozmiaru prostokąta. | Zwiększ wartość promienia (np. `setRoundingRadius(0.5)`). |

## Najczęściej zadawane pytania

### Q1: Czy mogę używać Aspose.3D for Java w projektach komercyjnych?

A1: Tak, Aspose.3D for Java jest dostępny do użytku komercyjnego. Szczegóły licencjonowania znajdziesz [here](https://purchase.aspose.com/buy).

### Q2: Czy dostępna jest darmowa wersja próbna?

A2: Tak, możesz wypróbować darmową wersję próbną Aspose.3D for Java [here](https://releases.aspose.com/).

### Q3: Gdzie mogę znaleźć wsparcie dla Aspose.3D for Java?

A3: Forum społeczności Aspose.3D to świetne miejsce, aby uzyskać wsparcie i podzielić się doświadczeniami. Odwiedź forum [here](https://forum.aspose.com/c/3d/18).

### Q4: Czy potrzebuję tymczasowej licencji do testowania?

A4: Tak, jeśli potrzebujesz tymczasowej licencji do testów, możesz ją uzyskać [here](https://purchase.aspose.com/temporary-license/).

### Q5: Gdzie mogę znaleźć dokumentację?

A5: Dokumentacja Aspose.3D for Java jest dostępna [here](https://reference.aspose.com/3d/java/).

## Zakończenie

Po ukończeniu tego **java 3d graphics tutorial** wiesz już, jak tworzyć obiekty **create 3d mesh java**, kontrolować środek ekstruzji liniowej, regulować promień zaokrąglenia oraz **save obj file java** przy użyciu Aspose.3D. Techniki te dają precyzyjną kontrolę nad symetrią siatki, co jest kluczowe dla zasobów gier, prototypów CAD i wizualizacji naukowych. Śmiało eksperymentuj z różnymi profilami, liczbą przekrojów i formatami eksportu, aby rozbudować swoją skrzynkę narzędziową 3‑D.

---

**Ostatnia aktualizacja:** 2026-06-13  
**Testowano z:** Aspose.3D for Java 24.11  
**Autor:** Aspose

## Powiązane tutoriale

- [Utwórz ekstruzję 3D w Javie z Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Jak ustawić kierunek w ekstruzji liniowej z Aspose.3D for Java](/3d/java/linear-extrusion/setting-direction/)
- [Utwórz scenę 3D z obrotem w ekstruzji liniowej – Aspose.3D for Java](/3d/java/linear-extrusion/applying-twist/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}