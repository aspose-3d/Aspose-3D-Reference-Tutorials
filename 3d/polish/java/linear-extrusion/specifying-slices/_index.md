---
date: 2026-05-24
description: Dowiedz się, jak tworzyć ekstruzję 3D z przekrojami przy użyciu Aspose.3D
  for Java. Ten przewodnik krok po kroku obejmuje ekstruzję liniową, ustawianie promienia
  zaokrąglenia oraz eksport do formatu OBJ.
keywords:
- create 3d extrusion java
- Aspose 3D slices
- linear extrusion Java
linktitle: Tworzenie ekstruzji 3D z przekrojami – Aspose.3D for Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  headline: Create 3D Extrusion with Slices – Aspose.3D for Java
  type: TechArticle
- description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  name: Create 3D Extrusion with Slices – Aspose.3D for Java
  steps:
  - name: Set up the scene and define the profile
    text: '`RectangleShape` is a class that defines a 2‑D rectangle profile. First
      we create a `RectangleShape` and give it a **rounding radius** so the corners
      are smooth. `Scene` is the root container for all nodes and geometry. Then we
      initialise a new `Scene` that will hold all geometry.'
  - name: Create child node objects for each extrusion
    text: '`Node` represents an element in the scene graph that can hold geometry
      and transformations. Every piece of geometry lives under a `Node`. Here we generate
      two sibling nodes – one for a low‑slice extrusion and another for a high‑slice
      extrusion – and move the left node a little to the side so the res'
  - name: Perform linear extrusion and set slices
    text: '`LinearExtrusion` is the class that creates a solid by sweeping a profile
      linearly. `LinearExtrusion` is Aspose.3D''s class that generates a solid by
      extruding a 2‑D profile along a straight line. Using an **anonymous inner class**
      we call `setSlices` to control the smoothness. The left node gets onl'
  - name: Export OBJ – save the scene
    text: Finally we write the scene to a Wavefront OBJ file, a format widely supported
      by 3‑D editors and game engines. This demonstrates the **export OBJ Java** capability
      of Aspose.3D.
  type: HowTo
- questions:
  - answer: You can download the library [here](https://releases.aspose.com/3d/java/).
    question: How can I download Aspose.3D for Java?
  - answer: Refer to the documentation [here](https://reference.aspose.com/3d/java/).
    question: Where can I find the documentation for Aspose.3D?
  - answer: Yes, you can explore a free trial [here](https://releases.aspose.com/).
    question: Is there a free trial available?
  - answer: Visit the support forum [here](https://forum.aspose.com/c/3d/18).
    question: How can I get support for Aspose.3D?
  - answer: Yes, a temporary license can be obtained [here](https://purchase.aspose.com/temporary-license/).
    question: Can I purchase a temporary license?
  type: FAQPage
second_title: Aspose.3D Java API
title: Tworzenie ekstruzji 3D z przekrojami – Aspose.3D for Java
url: /pl/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Utwórz ekstruzję 3D z przekrojami – Aspose.3D dla Javy

## Wprowadzenie

Jeśli potrzebujesz **tworzyć ekstruzję 3D** obiekty, które wyglądają gładko i precyzyjnie, kluczowe jest kontrolowanie liczby przekrojów. W tym samouczku przeprowadzimy Cię przez proces określania przekrojów podczas wykonywania liniowej ekstruzji przy użyciu Aspose.3D dla Javy. Zobaczysz, dlaczego liczba przekrojów ma znaczenie, jak ustawić promień zaokrąglenia oraz jak wyeksportować wynik jako plik OBJ, który może być używany w dowolnym potoku 3‑D.

## Szybkie odpowiedzi
- **Co kontrolują „przekroje”?** Liczba pośrednich przekrojów używanych do przybliżania powierzchni ekstruzji.  
- **Która metoda ustawia liczbę przekrojów?** `LinearExtrusion.setSlices(int)`  
- **Czy mogę zmienić promień zaokrąglenia profilu?** Tak, za pomocą `RectangleShape.setRoundingRadius(double)`  
- **Jaki format pliku jest używany w tym przykładzie?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **Czy potrzebna jest licencja do uruchomienia kodu?** Darmowa wersja próbna wystarczy do oceny; licencja komercyjna jest wymagana w produkcji.

`LinearExtrusion.setSlices(int)` ustawia, ile pośrednich przekrojów zostanie wygenerowanych przez ekstruzję.  
`RectangleShape.setRoundingRadius(double)` definiuje promień narożnika prostokątnego profilu.

## Jak utworzyć ekstruzję 3D w Javie z przekrojami?

Wczytaj swój profil 2‑D, wybierz liczbę przekrojów, ustaw promień zaokrąglenia i wywołaj `save` – cały przepływ pracy mieści się w kilku linijkach. Aspose.3D dla Javy obsługuje tworzenie geometrii, interpolację przekrojów i eksport OBJ automatycznie, dzięki czemu możesz skupić się na jakości wizualnej, a nie na niskopoziomowych obliczeniach siatki.

## Czym jest liniowa ekstruzja z przekrojami?

Liniowa ekstruzja z przekrojami przekształca płaską figurę 2‑D w bryłę 3‑D, przesuwając ją wzdłuż prostej linii i generując konfigurowalną liczbę pośrednich przekrojów. Liczba przekrojów bezpośrednio wpływa na to, jak płynnie renderowane są zakrzywione krawędzie, takie jak zaokrąglone narożniki.

## Dlaczego używać Aspose.3D dla Javy do tworzenia ekstruzji 3D?

Aspose.3D zapewnia **pełną kontrolę programistyczną** nad każdym parametrem ekstruzji, obsługuje **ponad 50 formatów wejściowych i wyjściowych** (w tym OBJ, FBX, STL i GLTF) i może przetwarzać **modele o setkach stron** bez ładowania całego pliku do pamięci. Działa na każdej platformie obsługującej Javę, nie wymaga natywnych DLL‑ów i gwarantuje deterministyczne wyniki na Windows, Linux i macOS.

## Prerequisites

1. **Java Development Kit** – zainstalowany JDK 8 lub nowszy.  
2. **Aspose.3D for Java** – Pobierz bibliotekę z oficjalnej strony [tutaj](https://releases.aspose.com/3d/java/).  
3. IDE lub edytor tekstu według własnego wyboru.

## Importowanie pakietów

Dodaj przestrzeń nazw Aspose.3D do swojego projektu, aby mieć dostęp do klas modelowania 3‑D.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Przewodnik krok po kroku

### Krok 1: Konfiguracja sceny i zdefiniowanie profilu

`RectangleShape` to klasa definiująca profil prostokąta 2‑D.  
Najpierw tworzymy `RectangleShape` i nadajemy mu **promień zaokrąglenia**, aby narożniki były gładkie.  
`Scene` jest głównym kontenerem dla wszystkich węzłów i geometrii.  
Następnie inicjalizujemy nową `Scene`, która będzie przechowywać całą geometrię.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Krok 2: Utwórz obiekty węzłów potomnych dla każdej ekstruzji

`Node` reprezentuje element w grafie sceny, który może przechowywać geometrię i transformacje.  
Każdy element geometrii znajduje się pod `Node`. Tutaj generujemy dwa węzły siostrzane – jeden dla ekstruzji z małą liczbą przekrojów i drugi dla ekstruzji z dużą liczbą przekrojów – i przesuwamy lewy węzeł nieco na bok, aby wyniki były łatwe do porównania.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Krok 3: Wykonaj liniową ekstruzję i ustaw przekroje

`LinearExtrusion` to klasa, która tworzy bryłę poprzez liniowe przesuwanie profilu.  
`LinearExtrusion` jest klasą Aspose.3D, która generuje bryłę przez ekstruzję profilu 2‑D wzdłuż prostej linii. Korzystając z **anonimowej klasy wewnętrznej**, wywołujemy `setSlices`, aby kontrolować płynność. Lewy węzeł otrzymuje tylko 2 przekroje (grubo), podczas gdy prawy węzeł otrzymuje 10 przekrojów (gładko).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Krok 4: Eksportuj OBJ – zapisz scenę

Na koniec zapisujemy scenę do pliku Wavefront OBJ, formatu szeroko wspieranego przez edytory 3‑D i silniki gier. To demonstruje możliwość **eksportu OBJ w Javie** w Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Typowe problemy i rozwiązania

| Problem | Dlaczego się pojawia | Rozwiązanie |
|---------|----------------------|-------------|
| **Ekstruzja wygląda płasko** | Liczba przekrojów ustawiona na 1 lub 0 | Upewnij się, że `setSlices` jest wywoływany z wartością ≥ 2. |
| **Zaokrąglone narożniki wyglądają ząbkowanie** | Promień zaokrąglenia zbyt mały w stosunku do liczby przekrojów | Zwiększ promień lub liczbę przekrojów, aby uzyskać płynniejsze krzywe. |
| **Plik nie został znaleziony przy zapisie** | `MyDir` wskazuje na nieistniejący folder | Utwórz katalog wcześniej lub użyj ścieżki bezwzględnej. |

## Najczęściej zadawane pytania

**P: Jak mogę pobrać Aspose.3D dla Javy?**  
Możesz pobrać bibliotekę [tutaj](https://releases.aspose.com/3d/java/).

**P: Gdzie mogę znaleźć dokumentację Aspose.3D?**  
Zapoznaj się z dokumentacją [tutaj](https://reference.aspose.com/3d/java/).

**P: Czy dostępna jest darmowa wersja próbna?**  
Tak, możesz wypróbować darmową wersję próbną [tutaj](https://releases.aspose.com/).

**P: Jak mogę uzyskać wsparcie dla Aspose.3D?**  
Odwiedź forum wsparcia [tutaj](https://forum.aspose.com/c/3d/18).

**P: Czy mogę kupić tymczasową licencję?**  
Tak, tymczasową licencję można uzyskać [tutaj](https://purchase.aspose.com/temporary-license/).

**Ostatnia aktualizacja:** 2026-05-24  
**Testowano z:** Aspose.3D for Java 24.11 (najnowsza w momencie pisania)  
**Autor:** Aspose

## Powiązane samouczki

- [Utwórz ekstruzję 3D w Javie z Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Jak ustawić kierunek w liniowej ekstruzji z Aspose.3D dla Javy](/3d/java/linear-extrusion/setting-direction/)
- [Utwórz scenę 3D z obrotem w liniowej ekstruzji – Aspose.3D dla Javy](/3d/java/linear-extrusion/applying-twist/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}