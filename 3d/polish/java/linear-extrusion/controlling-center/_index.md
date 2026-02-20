---
date: 2026-02-20
description: Poznaj samouczek grafiki 3D w Javie dotyczący sterowania środkiem przy
  liniowej ekstruzji z Aspose.3D, w tym jak ustawić promień zaokrąglenia i zapisać
  plik OBJ w Javie.
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Samouczek grafiki 3D w Javie – Środek w ekstruzji liniowej
url: /pl/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Poradnik Java 3D Graphics – Środek w Ekstruzji Liniowej

## Wprowadzenie

Jeśli tworzysz wizualizacje 3D w Javie, opanowanie technik ekstruzji jest niezbędne. Ten **java 3d graphics tutorial** prowadzi Cię przez kontrolowanie środka ekstruzji liniowej przy użyciu Aspose.3D for Java, dzięki czemu możesz tworzyć precyzyjne, symetryczne modele bez dodatkowych obliczeń. Po zakończeniu tego przewodnika zrozumiesz, dlaczego właściwość `center` ma znaczenie, jak **set rounding radius**, oraz jak **save OBJ file java**‑compatible output.

## Szybkie odpowiedzi
- **Co robi właściwość center?** Określa, czy ekstruzja jest symetryczna względem początku profilu.  
- **Czy potrzebuję licencji do uruchomienia kodu?** Tymczasowa licencja działa w testach; pełna licencja jest wymagana w produkcji.  
- **Jaki format pliku jest używany dla wyniku?** Scena jest zapisywana jako plik Wavefront OBJ.  
- **Czy mogę zmienić liczbę warstw?** Tak, użyj `setSlices(int)` na obiekcie `LinearExtrusion`.  
- **Czy Aspose.3D jest kompatybilny z Java 8+?** Absolutnie – obsługuje wszystkie nowoczesne wersje Javy.

## Czym jest java 3d graphics tutorial?

**java 3d graphics tutorial** wyjaśnia krok po kroku, jak używać bibliotek Java do tworzenia, manipulowania i renderowania trójwymiarowych obiektów. W tym przypadku skupiamy się na API ekstruzji Aspose.3D, które zamienia profile 2‑D w pełnoprawne siatki 3‑D.

## Dlaczego używać Aspose.3D for Java?

- **High‑level API** – Nie trzeba pisać niskopoziomowych obliczeń siatek.  
- **Cross‑format support** – Eksport do OBJ, FBX, STL i innych.  
- **Performance‑optimized** – Efektywnie obsługuje duże sceny.  
- **Rich documentation** – Zawiera przykłady, takie jak poniżej.

## Prerequisites

1. **Java Development Environment** – Zainstalowany JDK 8 lub nowszy.  
2. **Aspose.3D for Java** – Pobierz bibliotekę i dokumentację [tutaj](https://reference.aspose.com/3d/java/).  
3. **Document Directory** – Utwórz folder na swoim komputerze do przechowywania wygenerowanych plików; będziemy go nazywać **„Your Document Directory.”**

## Importowanie pakietów

W swoim środowisku IDE Java zaimportuj klasy Aspose.3D, które będą potrzebne. Dzięki temu kompilator uzyska dostęp do funkcji ekstruzji i budowania scen.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Przewodnik krok po kroku

### Krok 1: Przygotuj profil bazowy

Najpierw utwórz kształt 2‑D, który zostanie wyekstruzowany. Tutaj używamy prostokąta i **set rounding radius** na 0,3, co wygładza narożniki.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### Krok 2: Utwórz scenę 3D

Obiekt `Scene` pełni rolę kontenera dla wszystkich węzłów 3‑D, świateł i kamer.

```java
Scene scene = new Scene();
```

### Krok 3: Dodaj węzły lewy i prawy

Umieścimy dwa oddzielne węzły obok siebie, abyś mógł porównać ekstruzję z centrowaniem i bez niego.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Krok 4: Ekstruzja liniowa – bez środka (węzeł lewy)

Utwórz ekstruzję na lewym węźle, wyłącz centrowanie i ogranicz siatkę do trzech warstw, aby uzyskać podgląd low‑poly.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

### Krok 5: Dodaj płaszczyznę podłoża jako odniesienie (węzeł lewy)

Cienka kostka pełni rolę wizualnej podłogi, pomagając zobaczyć orientację ekstruzji.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

### Krok 6: Ekstruzja liniowa – ze środkiem (węzeł prawy)

Teraz powtórz ekstruzję, tym razem włączając `center`. Geometria będzie symetryczna względem początku profilu.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

### Krok 7: Dodaj płaszczyznę podłoża jako odniesienie (węzeł prawy)

Ta sama płaszczyzna podłoża po prawej stronie, aby porównanie było jasne.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

### Krok 8: Zapisz scenę 3D

Na koniec wyeksportuj całą scenę do pliku Wavefront OBJ – formatu łatwo używalnego w większości edytorów 3‑D.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Typowe problemy i rozwiązania

| Problem | Dlaczego się pojawia | Rozwiązanie |
|---------|----------------------|-------------|
| **Extrusion appears offset** | `setCenter(false)` pozostawia profil zakotwiczony w jego rogu. | Użyj `setCenter(true)`, aby uzyskać wyniki symetryczne. |
| **OBJ file is empty** | Ścieżka do katalogu wyjściowego jest niepoprawna lub brakuje uprawnień do zapisu. | Sprawdź, czy `MyDir` wskazuje istniejący folder i aplikacja ma dostęp do zapisu. |
| **Rounded corners look sharp** | Promień zaokrąglenia jest zbyt mały w stosunku do rozmiaru prostokąta. | Zwiększ wartość promienia (np. `setRoundingRadius(0.5)`). |

## Najczęściej zadawane pytania

### Q1: Czy mogę używać Aspose.3D for Java w projektach komercyjnych?

A1: Tak, Aspose.3D for Java jest dostępny do użytku komercyjnego. Szczegóły licencjonowania znajdziesz [tutaj](https://purchase.aspose.com/buy).

### Q2: Czy dostępna jest darmowa wersja próbna?

A2: Tak, możesz wypróbować darmową wersję Aspose.3D for Java [tutaj](https://releases.aspose.com/).

### Q3: Gdzie mogę znaleźć wsparcie dla Aspose.3D for Java?

A3: Forum społeczności Aspose.3D to świetne miejsce, aby uzyskać wsparcie i podzielić się doświadczeniami. Odwiedź forum [tutaj](https://forum.aspose.com/c/3d/18).

### Q4: Czy potrzebuję tymczasowej licencji do testów?

A4: Tak, jeśli potrzebujesz tymczasowej licencji do testów, możesz ją uzyskać [tutaj](https://purchase.aspose.com/temporary-license/).

### Q5: Gdzie mogę znaleźć dokumentację?

A5: Dokumentacja Aspose.3D for Java jest dostępna [tutaj](https://reference.aspose.com/3d/java/).

## Zakończenie

Po ukończeniu tego **java 3d graphics tutorial** wiesz już, jak kontrolować środek ekstruzji liniowej, regulować promień zaokrąglenia i **save OBJ file java** przy użyciu Aspose.3D. Te techniki dają precyzyjną kontrolę nad symetrią siatki, co jest kluczowe dla zasobów gier, prototypów CAD i wizualizacji naukowych. Śmiało eksperymentuj z różnymi profilami, liczbą warstw i formatami eksportu, aby rozbudować swoją skrzynkę narzędziową 3‑D.

---

**Last Updated:** 2026-02-20  
**Tested With:** Aspose.3D for Java 24.11  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}