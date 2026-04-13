---
date: 2026-02-22
description: Dowiedz się, jak tworzyć scenę 3D i eksportować ją przy użyciu Aspose.3D
  dla Javy z liniowym wyciągiem, skrętem i offsetem skrętu.
linktitle: Using Twist Offset in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Jak stworzyć scenę 3D z offsetem skrętu w ekstruzji liniowej przy użyciu Aspose.3D
  dla Javy
url: /pl/java/linear-extrusion/using-twist-offset/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Using Twist Offset in Linear Extrusion with Aspose.3D for Java

## Wstęp

W dynamicznym świecie grafiki 3D opanowanie sztuki **tworzenie sceny 3D** jest przełomem dla każdego projektu modelowania 3D w Javie. Dzięki Aspose.3D dla Javy można nie tylko liniowo ekstruować kształt, ale także dodać twist offset, aby uzyskać dostępwaną, skręconą geometrię. Ten samouczek przeprowadzi cię przez każdy krok kroku do **utwórz scenę 3d**, zastosowanie skrętu w liniowej ekstruzji oraz ostatecznego **eksportuj scenę 3d** do popularnego pliku OBJ.

## Szybkie odpowiedzi
- **Co robi Twist Offset?** Przesuwa punkt początkowy skrętu, wpływ na offsetowanie rotacji bocznej ekstruzji.
- **Która klasa wykonywania liniowej eksstruzję?** `LinearExtrusion` – można ustawić skręt, plastry oraz przesunięcie skrętu.
- **Czy mogę wyeksportować wynik?** Tak, wywołaj `scene.save(..., FileFormat.WAVEFRONTOBJ)`, aby wyeksportować scenę 3D.
- **Czy jest licencjat do rozwoju?** Tymczasowa licencja wystarczająca do testów; pełny licencjat jest wymagany w produkcji.
- **Jaka wersja Javy obsługuje?** każde środowisko uruchomieniowe Java8+ działa z najnowszą biblioteką Aspose.3D.

## Co to jest „utwórz scenę 3D” w Aspose.3D?
Tworzenie scen 3D oznaczają zwierzęta `Scene`, dopuszczalne (obiektów) do jej hierarchii oraz ostateczne zapisanie scen w odpowiednim pliku. To podstawa każdego pracy modelowania 3D w Javie.

## Po co stosować liniowy skręt wytłaczania z przesunięciem skrętu?
Dodanie skrętu podczas ekstruzji daje formy spiralne, takie jak elementy helikalne czy dekoracyjne uchwyty. Twist offset umożliwia sterowanie w niezależnych pozycjach, ustalając kontrolę nad ostatecznym kształtem — idealnym dla części, modeli artystycznych lub detali architektonicznych.

## Warunki wstępne

Zanim wypłyniesz w samouczek, nastąpi, że spełniasz odpowiednie wymagania:

- **Środowisko Java:** obciążenie się, że masz skonfigurowane środowisko programistyczne Java na swoim systemie.
- **Aspose.3D dla Javy:** Pobierz i zainstaluj bibliotekę Aspose.3D z [link do pobrania](https://releases.aspose.com/3d/java/).
- **Dokumentacja:** Zapoznaj się z [dokumentacją Aspose.3D for Java](https://reference.aspose.com/3d/java/).

## Importuj pakiety

W swoim projekcie Java zaimportuj niezbędne pakiety, aby rozpocząć korzystanie z Aspose.3D dla Javy. Upewnij się, że dołączasz wymagane biblioteki dla płynnej integracji.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Jak stworzyć scenę 3D – przewodnik krok po kroku

### Krok 1: Skonfiguruj środowisko
Rozpocznij od skonfigurowania środowiska programistycznego Java i upewnij się, że Aspose.3D dla Javy jest prawidłowo zainstalowany. Ten krok jest przeznaczony dla każdej pracy związanej z **java 3D modeling**.

### Krok 2: Zainicjuj profil podstawowy
Utwórz bazowy profil do ekstruzji, w tym przypadku `RectangleShape` z promieniem zaokrąglenia 0,3. Profil tworzący przekrój, który będzie przesuwany za pomocą prądu ekstruzji.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
// Initialize the base profile to be extruded
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### Krok 3: Utwórz scenę 3D
Zbuduj scenę 3D, aby pomieścić swoje wyekstruzowane obiekty. To miejsce, w którym **create child node** elementy reprezentujące poszczególne części geometrii.

```java
// Create a scene
Scene scene = new Scene();
```

### Krok 4: Utwórz węzły
Wygeneruj węzły w scenie, aby reprezentować różne podmioty. Tutaj tworzymy dwa węzły siostrzane — jeden dla zwykłej ekstruzji, a drugi wykorzystujący twist offset.

```java
// Create left node
Node left = scene.getRootNode().createChildNode();
// Create right node
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Krok 5: Wykonaj wytłaczanie liniowe ze skrętem i przesunięciem skrętu
Zastosuj liniową ekstruzję na obu węzłach. Lewy węzeł demonstruje podstawowy twist, podczas gdy prawy węzeł dodaje twist offset, aby pokazać dodatkową kontrolę, jaką daje ta funkcja.

```java
// Perform linear extrusion on left node using twist and slices property
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// Perform linear extrusion on right node using twist, twist offset, and slices property
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

> **Pro tip:** Dostosuj `setSlices()`, aby zwiększyć rozdzielczość siatki, gdy potrzebna jest płynniejsza krzywizna.

### Krok 6: Zapisz scenę 3D (eksportuj scenę 3D)
Na koniec wyeksportuj złożoną scenę do pliku OBJ, aby móc ją wyświetlić w dowolnym standardowym przeglądarce 3D lub zaimportować do innych pipeline'ów.

```java
// Save 3D scene
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Gdy kod uruchomi się pomyślnie, znajdziesz plik `TwistOffsetInLinearExtrusion.obj` w określonym katalogu, gotowy do otwarcia w narzędziach takich jak Blender, MeshLab czy dowolnym oprogramowaniu CAD.

## Typowe problemy i rozwiązania
| Problem | Dlaczego się pojawia | Rozwiązanie |
|-------|----------------|-----|
| **Scena zapisuje się jako pusty plik** | Ścieżka `MyDir` jest nieprawidłowa lub brakuje uprawnień do zapisu. | Zweryfikuj, czy katalog istnieje w ramach zapisów, lub skutków ubocznych. |
| **Twist wygląda płasko** | `setSlices()` jest zbyt skuteczne, co skutkuje grubą siatką. | Zwiększone przekrojów (np. 200), aby uzyskać płynniejsze skręty. |
| **Przesunięcie skrętu nie ma wpływu** | Wektor offsetu jest współliniowy z kierunkami Ekstruzji. | niezerowego komponentu X lub Y, aby zobaczyć przesunięcie offsetu. |

## Często zadawane pytania

### Q1: Czy można zastosować Aspose.3D dla Javy w projektach niekomercyjnych?
A1: Tak, Aspose.3D dla Javy może być używany zarówno w projektach komercyjnych, jak i niekomercyjnych. Sprawdź [opcje licencjonowania](https://purchase.aspose.com/buy) po więcej narzędzi.

### Q2: Gdzie mogę znaleźć wsparcie dla Aspose.3D dla Javy?
A2: Odwiedź [Aspose.3D for Java forum](https://forum.aspose.com/c/3d/18), aby uzyskać pomoc i połączyć się ze społecznością.

### Q3: Czy dostępna jest wersja próbna Aspose.3D dla Javy?
A3: Tak, możesz uzyskać bezpłatną wersję próbną z [stroną wydań] (https://releases.aspose.com/).

### Q4: Jak uzyskać tymczasową różnicę dla Aspose.3D dla Javy?
A4: dostęp tymczasową do swojego projektu, odwiedzając [ten link](https://purchase.aspose.com/temporary-license/).

### P5: Czy dostępne są dodatkowe przykłady i samouczki?
A5: Tak, odwołaj się do [dokumentacja](https://reference.aspose.com/3d/java/) po więcej pomysłów i szczegółowe samouczki.

---

**Aktualizacja Ostatnia:** 2026-02-22
**Testowano z:** Aspose.3D dla Java 24.11 (najnowsza)
**Autor:** Asponuj

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
