---
date: 2026-02-02
description: Dowiedz się, jak tworzyć kształty wentylatora cylindrycznego w Javie
  przy użyciu Aspose.3D. Ten przewodnik obejmuje modelowanie 3D w Javie oraz techniki
  zapisywania plików OBJ w Javie.
linktitle: How to Create Cylinder Fan Shapes Using Aspose.3D for Java
second_title: Aspose.3D Java API
title: Jak tworzyć kształty wentylatora cylindrycznego przy użyciu Aspose.3D dla Javy
url: /pl/java/cylinders/creating-fan-cylinders/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak tworzyć kształty wentylatora cylindrycznego przy użyciu Aspose.3D dla Javy

## Wprowadzenie

ów‑wentylatorów** w środowisku Java? W tym samouczku przejdziemy przez każdy krok — od konfiguracji sceny po eksport pliku Wavefront OBJ — używając Aspose.3D. Niezależnie od tego, czy tworzysz zasób do gry, prototyp CAD, czy po prostu eksperymentujesz z geometrią 3D, zobaczysz, jak proste może być modelowanie 3D w Javie dzięki tej potężnej bibliotece.

## Szybkie odpowiedzi
- **Jaki jest główny cel?** Utworzyć konfigurowalny cylinder‑wentylator i zapisać go jako plik OBJ.  
- **Jakiej biblioteki używamy?** Aspose.3D dla Javy.  
- **Czy potrzebna jest licencja?** Darmowa wersja próbna wystarczy do rozwoju; licencja komercyjna jest wymagana w produkcji.  
- **Jakie są wymagania wstęp JDK oraz pakiet Aspose.3D Java dodany do projektu.  
- **Czy mogę eksportować inne formaty?** Tak — Aspose.3D obsługuje wiele formatów; w tym przykładzie używamy Wavefront OBJ.

## Co to jest cylinder‑wentylator?

Cylinder‑wentylator to cylinder o częściowo usuniętej powierzchni, w którym odcinek kołowej podstawy jest pominięty, tworząc otwarcie w kształcie „wentylatora”. Geometria ta jest przydatna do wizualizacji przekrojów, paneli kontrolnych lub niestandardowych części mechanicznych.

## Dlaczego warto używać Aspose.3D do modelAspose.3D oferuje czyste, obiektowo‑zorientowane API,ć się na projektowaniu, a nie na szczegółach formatów plików, a biblioteka automatycznie obsługuje operacje **java save obj file**.

## Wymagania wstępne

Zanim zaczniemy, upewnij się, że masz:

- **Java Development Kit (JDK)** — pobierz go [tutaj](https://www.oracle.com/java/technologies/javase-downloads.html).  
- **Aspose.3D dla Javy** — pobierz najnowszy plik JAR z [linku do pobrania](https://releases.aspose.com/3d/java/).  

Dodaj plik JAR Aspose.3D do ścieżki klas swojego projektu.

## Importowanie pakietów

Rozpocznij od zaimportowania niezbędnych klas. Dzięki temu uzyskasz dostęp do sceny 3D, prymitywów geometrycznych i metod pomocniczych.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Krok 1: Utworzenie sceny

Najpierw tworzymy nową instancję `Scene`. Scena jest kontenerem, w którym znajdują się wszystkie obiekty 3D, światła i kamery.

```java
// ExStart:2
// Create a Scene
Scene scene = new Scene();
// ExEnd:2
```

## Krok 2: Utworzenie cylindra‑wentylatora (jak utworzyć cylinder)

Teraz budujemy sam cylinder‑wentylator. Parametry konstruktora określają promień, wysokość, tessellację oraz to, czy geometria ma być generowana jako wentylator.

```java
// ExStart:3
// Create a cylinder with fan
Cylinder fan = new Cylinder(2, 2, 10, 20, 1, false);
fan.setGenerateFanCylinder(true);
fan.setThetaLength(MathUtils.toRadian(270.0));
// ExEnd:3
```

> **Porada:** Dostosuj `setThetaLength`, aby zmienić kąt otwarcia. 270° tworzy wentylator o trzech czwartych; 180° dałoby półcylindra.

## Krok 3: Pozycjonowanie cylindra‑wentylatora

Następnie dodajemy cylinder‑wentylator do sceny miejsce. Współrzędne translacji podawane są w kolejności (X, Y, Z).

```java
// ExStart:4
// Create ChildNode and set translation
scene.getRootNode().createChildNode(fan).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

## Krok 4: Utworzenie cylindra bez wentylatora (porównanie modelowania 3D w Javie)

Aby pokazać elastyczność Aspose.3D, tworzymy również zwykły cylinder bez otwarcia wentylatora.

```java
// ExStart:5
// Create a cylinder without a fan
Cylinder nonfan = new Cylinder(2, 2, 10, 20, 1, false);
// Create ChildNode
scene.getRootNode().createChildNode(nonfan);
// ExEnd:5
```

## Krok 5: Zapis sceny (java save obj file)

Na koniec eksportujemy całą scenę do pliku Wavefront OBJ. Format ten jest szeroko wspierany przez większość edytorów 3D i silników gier.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

> **Uwaga:** Zastąp `"Your Document Directory"` ścieżką absolutną lub względną, w której masz uprawnienia do zapisu.

## Typowe problemy i rozwiązania

| Problem | Powód | Rozwiązanie |
|-------|--------|-----|
| Plik OBJ jest pusty | Scena nie została zapisana lub ścieżka jest niepoprawna | Sprawdź, czy katalog wyjściowy istnieje i ma prawa zapisu. |
| Otwarcie wentylatora wygląda niepoprawnie | Nieprawidłowa wartość `ThetaLength` | Użyj `MathUtils.toRadian(degrees)`, aby ustawić dokładny kąt. |
| Błędy kompilacji | Brak pliku JAR Aspose.3D w classpath | Dodaj JAR do folderu `libs` projektu Najczęściej zadawane pytania

**P:: Tak, Aspose.3D może współistnieć z takimi bibliotekami jak Java zych pipeline’ach.

**P: Czy mogę dalej dostosowywać wygląd cylindra‑wentylatora?**  
O: Oczywiście. Możesz stosować materiały, tekstury i oświetlenie, uzyskując dostęp do kolekcji `Material` i `Light` węzła.

**P: Gdzie mogę uzyskać dodatkowe wsparcie?**  
O: Odwiedź [forum Aspose.3D](https://forum.aspose.com/c/3d/18) po pomoc społeczności i oficjalne odpowiedzi.

**P: Czy dostępna jest Aspose.3D za pomocą [darmowej wersji próbnej](https://releases.aspose.com/) przed zakupem.

**P: Jak uzyskać tymczasową licencję do testów?**  
O: Pobierz ją [tutaj](https://purchase.aspose.com/temporary-license/), aby odblokować pełną funkcjonalność podczas rozwoju.

---

**Ostatnia aktualizacja:** 202avy  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}