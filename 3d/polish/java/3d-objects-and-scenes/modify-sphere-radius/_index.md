---
date: 2026-03-31
description: Dowiedz się, jak konwertować 3D do formatu OBJ, dodając kulę do sceny,
  modyfikując jej promień i eksportując plik OBJ w Javie przy użyciu Aspose.3D.
linktitle: 'Convert 3D to OBJ: Add Sphere & Modify Radius in Java'
second_title: Aspose.3D Java API
title: 'Konwertuj 3D do OBJ: Dodaj sferę i zmodyfikuj promień w Javie'
url: /pl/java/3d-objects-and-scenes/modify-sphere-radius/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Konwertuj 3D do OBJ: Dodaj sferę i zmodyfikuj promień w Javie

## Wprowadzenie

Jeśli potrzebujesz **konwertować 3D do OBJ** szybko i programowo, ten przewodnik pokaże Ci dokładnie, jak dodać sferę do sceny, zmienić jej promień i zapisać powstały plik OBJ przy użyciu **biblioteki Aspose.3D Java**. Przejdziemy przez każdy wiersz kodu, wyjaśnimy, dlaczego każdy krok ma znaczenie, i podpowiemy, jak unikać typowych pułapek — abyś mógł z pewnością zintegrować ten proces w grach, narzędziach CAD lub wizualizacjach naukowych.

## Szybkie odpowiedzi
- **Jaki jest główny cel tego samouczka?** Aby pokazać, jak konwertować 3D do OBJ poprzez stworzenie sfery, dostosowanie jej promienia i wyeksportowanie modelu w Javie.  
- **Która biblioteka zapewnia funkcjonalność 3D?** Aspose.3D, pełnoprawny **samouczek biblioteki java 3d**.  
- **Jak zmienić rozmiar sfery?** Wywołaj `sphere.setRadius(double)` na instancji `Sphere`.  
- **Czy mogę zapisać plik OBJ bezpośrednio z Javy?** Tak — użyj `scene.save("file.obj", FileFormat.WAVEFRONTOBJ)`.  
- **Czy potrzebuję licencji do produkcji?** Darmowa wersja próbna wystarczy do rozwoju; stała licencja jest wymagana do użytku komercyjnego.

## Jak konwertować 3D do OBJ przy użyciu Aspose.3D

### Co to jest Aspose.3D dla Javy?

Aspose.3D to **biblioteka java 3d**, która pozwala programistom tworzyć, edytować i konwertować pliki 3D bez żadnych zewnętrznych zależności. Obsługuje popularne formaty, takie jak OBJ, FBX, STL i inne, co czyni ją idealną dla gier, narzędzi CAD i wizualizacji naukowych.

### Dlaczego konwertować 3D do OBJ?

- **Uniwersalna kompatybilność** – OBJ jest obsługiwany praktycznie przez każdy przeglądarka 3D, silnik gier i oprogramowanie do modelowania.  
- **Lekkie eksportowanie** – OBJ przechowuje geometrię w formacie zwykłego tekstu, co ułatwia inspekcję i debugowanie.  
- **Elastyczność przepływu pracy** – Możesz generować pliki OBJ w locie z kodu Java po stronie serwera, umożliwiając automatyzowane pipeline’y tworzenia zasobów.

## Wymagania wstępne

- Podstawowa znajomość programowania w Javie.  
- Zainstalowana biblioteka Aspose.3D – pobierz ją z [dokumentacji Aspose.3D dla Javy](https://reference.aspose.com/3d/java/).  
- Zainstalowany JDK 8 lub nowszy na Twoim komputerze deweloperskim.

## Importowanie pakietów

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Sphere;

import java.io.IOException;
```

## Przewodnik krok po kroku

### Krok 1: Inicjalizacja sceny

```java
// ExStart:WorkingWithSphereRadius

// initialize a scene
Scene scene = new Scene();
```

Utworzenie `Scene` zapewnia kontener dla całej geometrii, świateł i kamer. To miejsce, w którym później **dodamy sferę do sceny**.

### Krok 2: Inicjalizacja sfery

```java
// initialize a Sphere
Sphere sphere = new Sphere();
```

Obiekt `Sphere` rozpoczyna się z domyślnym promieniem 1.0. Traktuj go jako czyste płótno dla kształtu, który chcesz wyeksportować.

### Krok 3: Ustaw pożądany promień

```java
// set radius
sphere.setRadius(10);
```

Tutaj **piszemy kod w stylu java dla pliku obj**, który ustawia dokładny promień. Zastąp `10` dowolną wartością `double`, która odpowiada Twoim wymaganiom projektowym.

### Krok 4: Dodaj sferę do sceny

```java
// add sphere to the scene
scene.getRootNode().createChildNode(sphere);
```

Ten wiersz **dodaje sferę do sceny** poprzez utworzenie węzła potomnego pod węzłem głównym. To moment, w którym geometria staje się częścią grafu sceny.

### Krok 5: Eksportuj model jako OBJ

```java
// save scene
scene.save("sphere.obj", FileFormat.WAVEFRONTOBJ);
```

Wywołanie `scene.save` **eksportuje plik obj w stylu java**, skutecznie **zapisując scenę jako obj**. Wygenerowany `sphere.obj` może być otwarty w dowolnym standardowym przeglądarce 3D.

## Częste problemy i rozwiązania

| Problem | Rozwiązanie |
|-------|----------|
| **Sfera wydaje się za mała w przeglądarce** | Sprawdź, czy wartość promienia jest ustawiona prawidłowo; pamiętaj, że jednostki są arbitralne, chyba że zastosujesz transformację skalowania. |
| **Wyeksportowany OBJ nie ma materiału** | Aspose.3D zapisuje tylko geometrię; dodaj materiał do sfery, jeśli potrzebujesz tekstur (`sphere.setMaterial(...)`). |
| **Wyjątek licencyjny w czasie wykonywania** | Upewnij się, że przed utworzeniem `Scene` załadowany jest plik licencji tymczasowej lub stałej. |

## Najczęściej zadawane pytania

### P: Gdzie mogę znaleźć dokumentację Aspose.3D dla Javy?

A: Możesz odnieść się do [dokumentacji Aspose.3D dla Javy](https://reference.aspose.com/3d/java/) po kompleksowe wskazówki.

### P: Jak pobrać Aspose.3D dla Javy?

A: Pobierz bibliotekę ze strony wydań: [Download Aspose.3D for Java](https://releases.aspose.com/3d/java/).

### P: Czy dostępna jest darmowa wersja próbna Aspose.3D dla Javy?

A: Tak, wypróbuj funkcje w darmowej wersji próbnej, odwiedzając [Aspose.3D Free Trial](https://releases.aspose.com/).

### P: Gdzie mogę uzyskać wsparcie dla Aspose.3D dla Javy?

A: Dołącz do społeczności Aspose na [Aspose.3D Support Forum](https://forum.aspose.com/c/3d/18), aby uzyskać pomoc i dyskusje.

### P: Jak mogę uzyskać tymczasową licencję dla Aspose.3D?

A: Uzyskaj tymczasową licencję, odwiedzając [Temporary License](https://purchase.aspose.com/temporary-license/).

### P: Czy mogę używać tego kodu z innymi formatami 3D, takimi jak STL?

A: Oczywiście — wystarczy zmienić enum `FileFormat` przy wywołaniu `scene.save`, np. `FileFormat.STL`.

## Zakończenie

Teraz wiesz, jak **konwertować 3D do OBJ** poprzez dodanie sfery, dostosowanie jej promienia i wyeksportowanie wyniku przy użyciu Aspose.3D w Javie. Eksperymentuj z innymi prymitywami, stosuj materiały lub łącz wiele transformacji, aby tworzyć bardziej złożone modele. Kiedykolwiek będziesz potrzebował **zapisz scenę jako obj** lub **napisz plik obj w java**, obowiązuje ten sam schemat.

---

**Ostatnia aktualizacja:** 2026-03-31  
**Testowano z:** Aspose.3D for Java 24.11  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}