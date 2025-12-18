---
date: 2025-12-18
description: Dowiedz się, jak dodać płaszczyznę podłoża i ustawić właściwość centrum
  w ekstruzji liniowej przy użyciu Aspose.3D dla Javy, z przykładami kodu krok po
  kroku.
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Jak dodać płaszczyznę podłoża i centrum sterowania w ekstruzji liniowej przy
  użyciu Aspose.3D dla Javy
url: /pl/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Kontrolowanie środka w ekstruzji liniowej przy użyciu Aspose.3D dla Javy

## Wprowadzenie

Podczas tworzenia scen 3D w Javie możliwość **dodania płaszczyzny podłoża** oraz precyzyjnego **ustawienia właściwości center** w ekstruzji liniowej może decydować o różnicy między płaskim prototypem a dopracowaną wizualizacją. W tym samouczku przeprowadzimy Cię przez cały proces kontrolowania środka ekstruzji oraz dodawania płaszczyzny podłoża przy użyciu Aspose.3D dla Javy. Zobaczysz, dlaczego jest to ważne, jak to skonfigurować oraz otrzymasz gotowy do uruchomienia przykład kodu, który możesz dostosować do własnych projektów.

## Szybkie odpowiedzi
- **Co robi „add ground plane”?** Tworzy cienką geometrię referencyjną, która pomaga zobaczyć pozycję ekstruzji względem osi świata.  
- **Jak ustawić środek ekstruzji liniowej?** Użyj metody `setCenter(boolean)` na obiekcie `LinearExtrusion`.  
- **Czy potrzebna jest licencja do uruchomienia przykładu?** Tymczasowa licencja wystarczy do testów; pełna licencja jest wymagana w produkcji.  
- **W jakim formacie zapisywany jest plik?** Przykład zapisuje do formatu Wavefront OBJ (`.obj`).  
- **Jakiej wersji Javy potrzebuję?** Java 8 lub nowsza jest wystarczająca.

## Co oznacza „add ground plane” w scenie 3D?

Dodanie płaszczyzny podłoża oznacza wstawienie cienkiej, prostokątnej geometrii (często pudełka o minimalnej grubości), które leży na płaszczyźnie X‑Z. Działa jako wizualna podłoga, ułatwiając ocenę wysokości i wyrównania innych obiektów, szczególnie przy eksperymentowaniu ze środkami ekstruzji.

## Dlaczego ustawia się właściwość center w ekstruzji liniowej?

Domyślnie ekstruzja liniowa zaczyna się od początku profilu. Ustawienie właściwości center (`setCenter(true)`) przesuwa profil tak, aby ekstruzja była wyśrodkowana wokół początku, co jest przydatne przy symetrycznych projektach lub gdy potrzebne jest spójne wyrównanie wielu obiektów.

## Wymagania wstępne

Zanim rozpoczniemy tę podróż po samouczku, upewnij się, że spełniasz następujące wymagania:

1. **Środowisko programistyczne Javy** – Upewnij się, że masz skonfigurowane środowisko programistyczne Javy na swoim komputerze.  
2. **Aspose.3D dla Javy** – Pobierz i zainstaluj bibliotekę Aspose.3D. Bibliotekę i jej dokumentację znajdziesz [tutaj](https://reference.aspose.com/3d/java/).  
3. **Katalog dokumentów** – Utwórz katalog do przechowywania swoich dokumentów Java. Nazwijmy go „Your Document Directory”.

## Importowanie pakietów

W swoim środowisku programistycznym Javy zaimportuj niezbędne pakiety dla Aspose.3D. Dzięki temu Twój kod będzie miał dostęp do funkcjonalności udostępnianych przez bibliotekę.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Krok 1: Konfiguracja profilu bazowego

Zainicjuj profil bazowy, który ma zostać wyekstruzowany. W tym przykładzie użyjemy kształtu prostokąta z promieniem zaokrąglenia 0,3.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Krok 2: Utworzenie sceny 3D

Zbuduj fundament swojego świata 3D, tworząc scenę.

```java
Scene scene = new Scene();
```

## Krok 3: Utworzenie węzłów lewego i prawego

Utwórz lewy i prawy węzeł w swojej scenie. Węzły te służą jako płótno dla obiektów 3D.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Krok 4: Ekstruzja liniowa z właściwością center (lewy węzeł)

Wykonaj ekstruzję liniową w lewym węźle **bez wyśrodkowania** i ustaw liczbę przekrojów na 3. Zwróć uwagę na wywołanie `setCenter(false)` – to tutaj **ustawiamy właściwość center** na *false*.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## Krok 5: Dodanie płaszczyzny podłoża dla odniesienia (lewy węzeł)

Ulepsz wizualizację, **dodając płaszczyznę podłoża** do lewego węzła. Cienka skrzynka pełni rolę podłogi, dzięki czemu wyraźnie widać wysokość ekstruzji.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## Krok 6: Ekstruzja liniowa z właściwością center (prawy węzeł)

Teraz wykonaj ekstruzję liniową w prawym węźle, tym razem **wyśrodkowując ekstruzję**. Wywołanie `setCenter(true)` pokazuje, jak **ustawić właściwość center** na *true*.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## Krok 7: Dodanie płaszczyzny podłoża dla odniesienia (prawy węzeł)

Podobnie jak po lewej stronie, dodaj płaszczyznę podłoża do prawego węzła, aby uzyskać spójną wizualną bazę.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## Krok 8: Zapis sceny 3D

Zapisz swoją scenę 3D w formacie Wavefront OBJ, aby móc ją otworzyć w dowolnym standardowym przeglądarce 3D.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Typowe problemy i rozwiązania

| Problem | Dlaczego się pojawia | Rozwiązanie |
|-------|----------------|-----|
| Płaszczyzna podłoża niewidoczna | Grubość pudełka jest zbyt mała w skali podglądu. | Zwiększ grubość (pierwszy parametr `Box`) lub oddal widok w przeglądarce. |
| Ekstruzja jest przesunięta | Wartość `setCenter` nie została ustawiona zgodnie z zamierzeniami. | Sprawdź ponownie wartość logiczną przekazywaną do `setCenter`. |
| Plik nie został zapisany | Nieprawidłowa ścieżka katalogu lub brak uprawnień do zapisu. | Zweryfikuj, czy `MyDir` wskazuje istniejący folder z prawami zapisu. |

## Najczęściej zadawane pytania

**Q1: Czy mogę używać Aspose.3D dla Javy w projektach komercyjnych?**  
A1: Tak, Aspose.3D dla Javy jest dostępny do użytku komercyjnego. Szczegóły licencjonowania znajdziesz [tutaj](https://purchase.aspose.com/buy).

**Q2: Czy dostępna jest darmowa wersja próbna?**  
A2: Tak, darmową wersję próbną Aspose.3D dla Javy możesz wypróbować [tutaj](https://releases.aspose.com/).

**Q3: Gdzie mogę uzyskać wsparcie dla Aspose.3D dla Javy?**  
A3: Forum społeczności Aspose.3D to świetne miejsce, aby uzyskać pomoc i podzielić się doświadczeniami. Odwiedź forum [tutaj](https://forum.aspose.com/c/3d/18).

**Q4: Czy potrzebuję tymczasowej licencji do testów?**  
A4: Tak, jeśli potrzebujesz tymczasowej licencji do testów, możesz ją uzyskać [tutaj](https://purchase.aspose.com/temporary-license/).

**Q5: Gdzie znajdę dokumentację?**  
A5: Dokumentację Aspose.3D dla Javy znajdziesz [tutaj](https://reference.aspose.com/3d/java/).

## Zakończenie

Kontrolowanie środka w ekstruzji liniowej **oraz** nauka **dodawania płaszczyzny podłoża** przy użyciu Aspose.3D dla Javy otwiera ekscytujące możliwości w rozwoju grafiki 3D. Postępując zgodnie z powyższymi krokami, masz teraz wzorzec, który możesz ponownie wykorzystać do tworzenia wyśrodkowanych ekstruzji, płaszczyzn referencyjnych i eksportowania wyniku do OBJ. Śmiało eksperymentuj z różnymi profilami, liczbą przekrojów i transformacjami, aby dopasować je do potrzeb własnych projektów.

---

**Ostatnia aktualizacja:** 2025-12-18  
**Testowane z:** Aspose.3D 24.11 dla Javy (najnowsza w momencie pisania)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}