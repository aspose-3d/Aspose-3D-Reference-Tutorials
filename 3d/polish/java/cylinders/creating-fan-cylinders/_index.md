---
date: 2026-08-02
description: Dowiedz się, jak stworzyć cylinder fan shape w Javie przy użyciu Aspose.3D.
  Ten przewodnik obejmuje modelowanie 3D w Javie oraz techniki zapisywania plików
  OBJ w Javie.
keywords:
- create cylinder fan shape
- save obj file java
- aspose 3d export obj
lastmod: 2026-08-02
linktitle: Jak stworzyć cylinder fan shape przy użyciu Aspose.3D w Javie
og_description: Stwórz cylinder fan shape przy użyciu Aspose.3D w Javie i wyeksportuj
  plik OBJ. Postępuj zgodnie z instrukcjami krok po kroku, aby modelować, dostosowywać
  i zapisywać swój 3D fan cylinder.
og_image_alt: 'Tutorial: create cylinder fan shape in Java with Aspose.3D'
og_title: Stwórz cylinder fan shape przy użyciu Aspose.3D w Javie – Szybki przewodnik
schemas:
- author: Aspose
  dateModified: '2026-08-02'
  description: Learn how to create cylinder fan shape in Java with Aspose.3D. This
    guide covers java 3d modeling and save obj file java techniques.
  headline: How to create cylinder fan shape using Aspose.3D for Java
  type: TechArticle
- questions:
  - answer: Yes, Aspose.3D can coexist with libraries like Java 3D or jMonkeyEngine,
      allowing you to integrate custom geometry into larger pipelines.
    question: Is Aspose.3D compatible with other Java 3D libraries?
  - answer: Absolutely. You can apply materials, textures, and lighting by accessing
      the node’s `Material` and `Light` collections.
    question: Can I further customize the appearance of the fan cylinder?
  - answer: Visit the [Aspose.3D forum](https://forum.aspose.com/c/3d/18) for community
      help and official responses.
    question: Where can I get additional support?
  - answer: Yes, you can explore Aspose.3D with a [free trial](https://releases.aspose.com/)
      before purchasing.
    question: Is there a free trial available?
  - answer: Acquire one [here](https://purchase.aspose.com/temporary-license/) to
      unlock full functionality during development.
    question: How do I obtain a temporary license for testing?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- create cylinder fan shape
- Aspose.3D
- Java 3D modeling
- export OBJ
- 3D geometry
title: Jak stworzyć cylinder fan shape przy użyciu Aspose.3D w Javie
url: /pl/java/cylinders/creating-fan-cylinders/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak stworzyć kształt wentylatora cylindrycznego przy użyciu Aspose.3D dla Javy

## Wprowadzenie

Gotowy, aby opanować **tworzenie kształtu wentylatora cylindrycznego** w środowisku Java? W tym samouczku przeprowadzimy Cię przez każdy krok — od przygotowania sceny po eksport pliku Wavefront OBJ — przy użyciu Aspose.3D. Niezależnie od tego, czy tworzysz zasób do gry, prototyp CAD, czy po prostu eksperymentujesz z geometrią 3D, zobaczysz, jak łatwe może być modelowanie 3D w Javie dzięki tej potężnej bibliotece.

## Szybkie odpowiedzi
- **Jaki jest główny cel?** Utworzyć konfigurowalny cylinder w kształcie wentylatora i zapisać go jako plik OBJ.  
- **Która biblioteka jest używana?** Aspose.3D for Java.  
- **Czy potrzebna jest licencja?** Darmowa wersja próbna wystarcza do rozwoju; licencja komercyjna jest wymagana w produkcji.  
- **Jakie są wymagania wstępne?** Zainstalowany JDK oraz pakiet Aspose.3D Java dodany do projektu.  
- **Czy mogę eksportować inne formaty?** Tak — Aspose.3D obsługuje wiele formatów; w tym przykładzie używany jest Wavefront OBJ.

## Co to jest cylinder‑wentylator?

Cylinder‑wentylator to segment cylindryczny, w którym usunięto część okrągłej podstawy, tworząc otwarty sektor „wentylatora”. Definiowany jest przez promień, wysokość i kąt otwarcia, co czyni go idealnym do wizualizacji wycinków, pulpitów nawigacyjnych lub niestandardowych części mechanicznych.

W praktyce wyobraź sobie zwykły cylinder z wyciętym klinem — idealny do przedstawiania częściowych obrotów lub wizualizacji w stylu wycinków w pulpitach inżynierskich.

## Dlaczego używać Aspose.3D do modelowania 3D w Javie?

Aspose.3D for Java oferuje wysokopoziomowe, obiektowo‑zorientowane API, które ukrywa niskopoziomową matematykę, obsługuje **ponad 50 formatów wejściowych i wyjściowych** i może przetwarzać modele o setkach stron bez ładowania całego pliku do pamięci, umożliwiając szybki rozwój aplikacji 3D. Biblioteka automatycznie obsługuje operacje **eksportu plików OBJ w Javie**, dzięki czemu możesz skupić się na geometrii, a nie na problemach formatów plików.

## Wymagania wstępne

Zanim zaczniemy, upewnij się, że masz:

- **Java Development Kit (JDK)** – pobierz go [tutaj](https://www.oracle.com/java/technologies/javase-downloads.html).  
- **Aspose.3D for Java** – pobierz najnowszy JAR z [linku do pobrania](https://releases.aspose.com/3d/java/).  

Dodaj JAR Aspose.3D do classpathu swojego projektu.

## Importowanie pakietów

Zacznij od zaimportowania niezbędnych klas. Dzięki temu uzyskasz dostęp do sceny 3D, prymitywów geometrycznych i metod pomocniczych.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Krok 1: Utwórz scenę

Klasa `Scene` jest kontenerem Aspose.3D, który przechowuje wszystkie obiekty 3D, światła i kamery. Traktuj ją jak wirtualną scenę, na której umieszczasz każdy element swojego modelu.

```java
// ExStart:2
// Create a Scene
Scene scene = new Scene();
// ExEnd:2
```

## Krok 2: Utwórz cylinder‑wentylator (jak utworzyć cylinder)

Klasa `Cylinder` reprezentuje siatkę cylindryczną, którą można dostosować pod względem promienia, wysokości, teselacji oraz kąta otwarcia wentylatora. Poprzez zmianę `setThetaLength` kontrolujesz, jaka część cylindra zostaje pominięta.

```java
// ExStart:3
// Create a cylinder with fan
Cylinder fan = new Cylinder(2, 2, 10, 20, 1, false);
fan.setGenerateFanCylinder(true);
fan.setThetaLength(MathUtils.toRadian(270.0));
// ExEnd:3
```

> **Wskazówka:** Dostosuj `setThetaLength`, aby zmienić kąt otwarcia. 270° tworzy trójczwartowy wentylator; 180° dałoby półcylindra.

## Krok 3: Pozycjonowanie cylindra‑wentylatora

Klasa `Node` jest elementem grafu sceny, który przechowuje geometrię i jej transformację. Przesuwanie węzła przenosi cylinder‑wentylator do żądanej lokalizacji w układzie współrzędnych (X, Y, Z).

```java
// ExStart:4
// Create ChildNode and set translation
scene.getRootNode().createChildNode(fan).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

## Krok 4: Utwórz cylinder bez wentylatora (porównanie modelowania 3D w Javie)

Aby zilustrować elastyczność Aspose.3D, tworzymy również zwykły cylinder bez otwarcia wentylatora. To porównanie obok siebie pomaga zobaczyć wpływ parametru `ThetaLength`.

```java
// ExStart:5
// Create a cylinder without a fan
Cylinder nonfan = new Cylinder(2, 2, 10, 20, 1, false);
// Create ChildNode
scene.getRootNode().createChildNode(nonfan);
// ExEnd:5
```

## Krok 5: Zapisz scenę (zapis pliku OBJ w Javie)

Metoda `Scene.save` zapisuje całą scenę do pliku. Przekazując `FileFormat.WAVEFRONTOBJ`, Aspose.3D generuje standardowy plik OBJ, który można otworzyć w programach takich jak Blender, Maya, Unity i wielu innych narzędziach 3D.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

> **Uwaga:** Zastąp `"Your Document Directory"` ścieżką absolutną lub względną, w której masz uprawnienia do zapisu.

## Jak zapisać plik OBJ w Javie przy użyciu Aspose 3D

Aby wyeksportować scenę, wywołaj `scene.save("output.obj", FileFormat.WAVEFRONTOBJ);` — Aspose.3D zapisuje geometrię, materiały i odniesienia do tekstur w standardowym pliku Wavefront OBJ, który może otworzyć każdy główny edytor 3D.

## Częste problemy i rozwiązania

| Problem | Powód | Rozwiązanie |
|-------|--------|-----|
| Plik OBJ jest pusty | Scena nie została zapisana lub ścieżka jest nieprawidłowa | Sprawdź, czy katalog wyjściowy istnieje i ma uprawnienia do zapisu. |
| Otwór wentylatora wygląda nieprawidłowo | Nieprawidłowa wartość `ThetaLength` | Użyj `MathUtils.toRadian(degrees)`, aby ustawić dokładny potrzebny kąt. |
| Błędy kompilacji | Brak JAR Aspose.3D w classpathie | Dodaj JAR do folderu `libs` projektu i uwzględnij go w ścieżce budowania. |

## Najczęściej zadawane pytania

**P: Czy Aspose.3D jest kompatybilny z innymi bibliotekami 3D w Javie?**  
O: Tak, Aspose.3D może współistnieć z takimi bibliotekami jak Java 3D czy jMonkeyEngine, umożliwiając integrację niestandardowej geometrii w większych pipeline'ach.

**P: Czy mogę dalej dostosować wygląd cylindra‑wentylatora?**  
O: Oczywiście. Możesz zastosować materiały, tekstury i oświetlenie, uzyskując dostęp do kolekcji `Material` i `Light` węzła.

**P: Gdzie mogę uzyskać dodatkowe wsparcie?**  
O: Odwiedź [forum Aspose.3D](https://forum.aspose.com/c/3d/18), aby uzyskać pomoc społeczności i oficjalne odpowiedzi.

**P: Czy dostępna jest darmowa wersja próbna?**  
O: Tak, możesz wypróbować Aspose.3D w ramach [darmowej wersji próbnej](https://releases.aspose.com/) przed zakupem.

**P: Jak uzyskać tymczasową licencję do testów?**  
O: Uzyskaj ją [tutaj](https://purchase.aspose.com/temporary-license/), aby odblokować pełną funkcjonalność podczas rozwoju.

---

**Ostatnia aktualizacja:** 2026-08-02  
**Testowano z:** Aspose.3D 24.11 for Java  
**Autor:** Aspose

## Powiązane samouczki

- [Jak tworzyć modele cylindrów przy użyciu Aspose.3D dla Javy](/3d/java/cylinders/)
- [Tymczasowa licencja Aspose – Utwórz cylinder z przesuniętym wierzchołkiem (Java)](/3d/java/cylinders/creating-cylinders-with-offset-top/)
- [Jak zmienić orientację płaszczyzny i wyeksportować OBJ w Javie](/3d/java/3d-scenes-and-models/change-plane-orientation/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}