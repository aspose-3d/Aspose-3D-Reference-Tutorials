---
date: 2026-02-22
description: Dowiedz się, jak tworzyć wyciągnięcia 3D z przekrojami przy użyciu Aspose.3D
  dla Javy. Ten przewodnik krok po kroku obejmuje wyciąganie liniowe, ustawianie promienia
  zaokrąglenia oraz eksportowanie do formatu OBJ.
linktitle: Create 3D Extrusion with Slices – Aspose.3D for Java
second_title: Aspose.3D Java API
title: Tworzenie ekstruzji 3D z przekrojami – Aspose.3D dla Javy
url: /pl/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Tworzenie ekstruzji 3D z warstwami – Aspose.3D dla Javy

## Wstęp

Jeśli **tworzysz ekstruzję 3D** obiektów, które są gładko i wyodrębnione, to jest kontrolowane przez liczbę warstw. W tym samouczku przeprowadziliśmy Cię przez określenie warstw podczas wykonywania liniowej ekstruzji przy użyciu Aspose.3D dla Javy. Zobaczysz, dlaczego liczba warstw ma znaczenie, jak ustawić promień zaokrąglenia oraz jak wyeksportować jako plik wynikowy OBJ, który można zastosować w potoku 3D.

## Szybkie odpowiedzi
- **Co kontrolują „warstwy”?** Liczbę pośrednich przekrojów podstawowych do przybliżania powierzchni zewnętrznej ekstruzji.
- **Która metoda ustawiania warstw?** `LinearExtrusion.setSlices(int)`
- **Czy mogę zmienić promień zaokrąglenia profilu?** Tak, poprzez `RectangleShape.setRoundingRadius(double)`
- **Jaki format pliku jest używany w tym powstały?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)
- **Czy jest licencja do uruchomienia kodu?** Wersja próbna wystarczy do sprawdzenia; licencjat komercyjny jest wymagany w produkcji.

## Co to jest wytłaczanie liniowe z plasterkami?

Liniowa Ekstruzja przyjmuje profil 2‑D (np. Ideał) i następuje przejście do drugiej linii, tworzącej bryłę 3‑D. **warstwy**, obsługująsz Aspose.3D, ile pośrednich kroków ma wygenerować, co bezpośrednio wpływa na gładkość zakrzywionych krawędzi, takich jak zaokrąglony Delta.

## Po co używać Aspose.3D dla Java do tworzenia wytłoczeń 3D?

* **Pełna kontrola** – możesz dostosować program do warstw, promień zaokrąglenia i formatu eksportu.
* **Wieloplatformowość** – działa w każdym środowisku obsługującym Javę bez zależności natywnych.
* **Elastyczność eksportu** – bezpośrednio zapisuje do OBJ, FBX, STL i wielu innych formatów.

## Warunki wstępne

1. **Java Development Kit** – gotowy JDK 8 lub nowszy.
2. **Aspose.3D for Java** – pobierz bibliotekę z adaptacyjną stroną [tutaj](https://releases.aspose.com/3d/java/).
3. IDE lub edytor tekstu według własnego wyboru.

## Importuj pakiety

Dodaj przestrzeń nazw Aspose.3D do swojego projektu, aby uzyskać dostęp do klas modelowania 3-D.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Przewodnik krok po kroku

### Krok 1: Skonfiguruj scenę i zdefiniuj profil

Najpierw tworzymy `RectangleShape` i nadajemy mu **promień zaokrąglenia**, aby narożniki były gładkie. Następnie inicjalizujemy nową `Scene`, która będzie przechowywać całą geometrię.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Krok 2: Utwórz obiekty **węzła podrzędnego** dla każdego wytłoczenia

Każdy element geometrii znajduje się pod `Node`. Tutaj generujemy dwa węzły‑bracia – jeden dla ekstruzji o niskiej liczbie warstw i drugi dla ekstruzji o wysokiej liczbie warstw – i przesuwamy lewy węzeł nieco na bok, aby wyniki były łatwe do porównania.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Krok 3: Wykonaj wytłoczenie liniowe i **ustaw wycinki**

Teraz faktycznie **tworzymy obiekty ekstruzji 3D**. Konstruktor `LinearExtrusion` przyjmuje profil oraz głębokość ekstruzji. Korzystając z **anonimowej klasy wewnętrznej**, wywołujemy `setSlices`, aby kontrolować gładkość. Lewy węzeł otrzymuje tylko 2 warstwy (grubo), podczas gdy prawy węzeł otrzymuje 10 warstw (gładko).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Krok 4: Eksportuj OBJ** – zapisz scenę

Na koniec zapisujemy scenę do pliku Wavefront OBJ, formatu szeroko wspieranego przez edytory 3‑D i silniki gier. To demonstruje możliwość **export obj java** w Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Typowe problemy i rozwiązania

| Problem | Dlaczego się pojawia | Rozwiązanie |
|------------|----------------------|------------|
| **Ekstruzja wygląda płasko** | Liczba warstw ustawionych na 1 lub 0 | Pojawia się, że `setSlices` jest wywoływane z wartością ≥2. |
| **Zaokrąglony kąt i wygląd ząbkowanie** | Promień zaokrąglony zbyt mały w stosunku do liczby warstw | Podnoszone zarówno promień, jak i warstwy, aby uzyskać gładsze krzywe. |
| **Plik nie został znaleziony przy zapisie** | `MyDir` wskazujący na nieistniejący folder | Utworzenie katalogu wstępnego lub szczegółowego badania naukowego. |

## Często zadawane pytania

**P: Jak mogę pobrać Aspose.3D dla Javy?**  
O: Bibliotekę możesz pobrać [tutaj](https://releases.aspose.com/3d/java/).

**P: Gdzie mogę znaleźć dokumentację Aspose.3D?**  
O: Dokumentację znajdziesz [tutaj](https://reference.aspose.com/3d/java/).

**P: Czy dostępna jest wersja próbna?**  
O: Tak, wersję próbną możesz wypróbować [tutaj](https://releases.aspose.com/).

**P: Jak mogę uzyskać wsparcie dla Aspose.3D?**  
O: Odwiedź forum wsparcia [tutaj](https://forum.aspose.com/c/3d/18).

**P: Czy mogę kupić tymczasową licencję?**  
O: Tak, tymczasową licencję można nabyć [tutaj](https://purchase.aspose.com/temporary-license/).

---

**Ostatnia aktualizacja:** 2026-02-22  
**Testowano z:** Aspose.3D for Java 24.11 (najnowsza w momencie pisania)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}