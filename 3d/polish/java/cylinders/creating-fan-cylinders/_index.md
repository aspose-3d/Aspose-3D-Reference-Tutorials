---
date: 2026-04-03
description: Dowiedz się, jak stworzyć kształt wentylatora cylindrycznego w Javie
  przy użyciu Aspose.3D. Ten przewodnik obejmuje modelowanie 3D w Javie oraz techniki
  zapisywania plików OBJ w Javie.
keywords:
- create cylinder fan shape
- save obj file java
- aspose 3d export obj
linktitle: Jak utworzyć kształt wentylatora cylindrycznego przy użyciu Aspose.3D dla
  Javy
second_title: Aspose.3D Java API
title: Jak utworzyć kształt wentylatora cylindrycznego przy użyciu Aspose.3D dla Javy
url: /pl/java/cylinders/creating-fan-cylinders/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak stworzyć kształt wentylatora cylindrycznego przy użyciu Aspose.3D dla Javy

## Wprowadzenie

Gotowy, aby opanować **tworzenie kształtu wentylatora cylindrycznego** w środowisku Java? W tym samouczku przeprowadzimy Cię przez każdy krok — od ustawienia sceny po eksportowanie pliku Wavefront OBJ — używając Aspose.3D. Niezależnie od tego, czy tworzysz zasób do gry, prototyp CAD, czy po prostu eksperymentujesz z geometrią 3D, zobaczysz, jak łatwe może być modelowanie 3D w Javie dzięki tej potężnej bibliotece.

## Szybkie odpowiedzi
- **Jaki jest główny cel?** Utworzyć konfigurowalny cylinder w kształcie wentylatora i zapisać go jako plik OBJ.  
- **Która biblioteka jest używana?** Aspose.3D dla Javy.  
- **Czy potrzebna jest licencja?** Darmowa wersja próbna działa w fazie rozwoju; licencja komercyjna jest wymagana w produkcji.  
- **Jakie są wymagania wstępne?** Zainstalowany JDK oraz dodany pakiet Aspose.3D Java do projektu.  
- **Czy mogę eksportować inne formaty?** Tak — Aspose.3D obsługuje wiele formatów; w tym przykładzie używamy Wavefront OBJ.

## Co to jest cylinder wentylatorowy?

Cylinder wentylatorowy to cylinder o częściowej powierzchni, w którym wycięto sektor okrągłej podstawy, tworząc otwór w kształcie „wentylatora”. Ta geometria jest przydatna do wizualizacji przekrojów, paneli kontrolnych lub niestandardowych części mechanicznych.

## Dlaczego używać Aspose.3D do modelowania 3D w Javie?

Aspose.3D oferuje czyste, obiektowo‑zorientowane API, które abstrahuje niskopoziomową matematykę grafiki 3D. Możesz skupić się na projektowaniu, a nie na dziwactwach formatów plików, a biblioteka automatycznie obsługuje operacje **save obj file java**.

## Wymagania wstępne

Zanim zaczniemy, upewnij się, że masz:

- **Java Development Kit (JDK)** – pobierz go [tutaj](https://www.oracle.com/java/technologies/javase-downloads.html).  
- **Aspose.3D for Java** – pobierz najnowszy plik JAR z [linku do pobrania](https://releases.aspose.com/3d/java/).  

Dodaj plik JAR Aspose.3D do classpathu swojego projektu.

## Importowanie pakietów

Zacznij od zaimportowania niezbędnych klas. Dzięki temu uzyskasz dostęp do sceny 3D, prymitywów geometrycznych oraz metod pomocniczych.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Krok 1: Utworzenie sceny

Najpierw tworzymy nową instancję `Scene`. Traktuj scenę jako kontener, który przechowuje wszystkie Twoje obiekty 3D, światła i kamery.

```java
// ExStart:2
// Create a Scene
Scene scene = new Scene();
// ExEnd:2
```

## Krok 2: Utworzenie cylindra wentylatora (jak stworzyć cylinder)

Teraz budujemy sam cylinder wentylatorowy. Parametry konstruktora określają promień, wysokość, tessellację oraz to, czy geometria jest generowana jako wentylator.

```java
// ExStart:3
// Create a cylinder with fan
Cylinder fan = new Cylinder(2, 2, 10, 20, 1, false);
fan.setGenerateFanCylinder(true);
fan.setThetaLength(MathUtils.toRadian(270.0));
// ExEnd:3
```

> **Pro tip:** Dostosuj `setThetaLength`, aby zmienić kąt otwarcia. 270° tworzy wentylator trzech czwartej; 180° dałoby półcylindr.

## Krok 3: Pozycjonowanie cylindra wentylatora

Następnie dodajemy cylinder wentylatorowy do sceny i przenosimy go w wygodne miejsce. Współrzędne translacji podawane są w kolejności (X, Y, Z).

```java
// ExStart:4
// Create ChildNode and set translation
scene.getRootNode().createChildNode(fan).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

## Krok 4: Utworzenie cylindra bez wentylatora (porównanie modelowania 3D w Javie)

Aby zilustrować elastyczność Aspose.3D, tworzymy również zwykły cylinder bez otworu wentylatora.

```java
// ExStart:5
// Create a cylinder without a fan
Cylinder nonfan = new Cylinder(2, 2, 10, 20, 1, false);
// Create ChildNode
scene.getRootNode().createChildNode(nonfan);
// ExEnd:5
```

## Krok 5: Zapisanie sceny (zapis pliku OBJ w Javie)

Na koniec eksportujemy całą scenę do pliku Wavefront OBJ. Ten format jest szeroko wspierany przez większość edytorów 3D i silników gier.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

> **Uwaga:** Zastąp `"Your Document Directory"` ścieżką absolutną lub względną, w której masz uprawnienia do zapisu.

## Jak zapisać plik OBJ w Javie przy użyciu Aspose 3D

Metoda `Scene.save` z Aspose.3D automatycznie obsługuje proces **aspose 3d export obj**. Wystarczy podać nazwę docelowego pliku oraz wartość wyliczenia `FileFormat.WAVEFRONTOBJ`, jak pokazano w poprzednim kroku.

## Typowe problemy i rozwiązania

| Problem | Przyczyna | Rozwiązanie |
|---------|-----------|-------------|
| Plik OBJ jest pusty | Scena nie została zapisana lub ścieżka jest nieprawidłowa | Sprawdź, czy katalog wyjściowy istnieje i ma uprawnienia do zapisu. |
| Otwór wentylatora wygląda nieprawidłowo | Nieprawidłowa wartość `ThetaLength` | Użyj `MathUtils.toRadian(degrees)`, aby ustawić dokładny potrzebny kąt. |
| Błędy kompilacji | Brak pliku JAR Aspose.3D w classpath | Dodaj JAR do folderu `libs` projektu i uwzględnij go w ścieżce budowania. |

## Najczęściej zadawane pytania

**Q: Czy Aspose.3D jest kompatybilny z innymi bibliotekami 3D w Javie?**  
A: Tak, Aspose.3D może współistnieć z takimi bibliotekami jak Java 3D czy jMonkeyEngine, umożliwiając integrację własnej geometrii w większych pipeline'ach.

**Q: Czy mogę dalej dostosować wygląd cylindra wentylatora?**  
A: Oczywiście. Możesz zastosować materiały, tekstury i oświetlenie, uzyskując dostęp do kolekcji `Material` i `Light` węzła.

**Q: Gdzie mogę uzyskać dodatkowe wsparcie?**  
A: Odwiedź [forum Aspose.3D](https://forum.aspose.com/c/3d/18), aby uzyskać pomoc społeczności i oficjalne odpowiedzi.

**Q: Czy dostępna jest darmowa wersja próbna?**  
A: Tak, możesz wypróbować Aspose.3D za pomocą [darmowej wersji próbnej](https://releases.aspose.com/) przed zakupem.

**Q: Jak uzyskać tymczasową licencję do testów?**  
A: Pobierz ją [tutaj](https://purchase.aspose.com/temporary-license/), aby odblokować pełną funkcjonalność podczas rozwoju.

---

**Ostatnia aktualizacja:** 2026-04-03  
**Testowano z:** Aspose.3D 24.11 dla Javy  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}