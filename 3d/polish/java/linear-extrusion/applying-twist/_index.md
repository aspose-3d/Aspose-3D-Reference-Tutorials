---
date: 2025-12-17
description: Dowiedz się, jak stworzyć skręcony model 3D przy użyciu Aspose.3D dla
  Javy z liniową ekstruzją skrętu i wyeksportować plik OBJ w Javie. Postępuj zgodnie
  z naszym przewodnikiem krok po kroku.
linktitle: Applying Twist in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Tworzenie skręconego modelu 3D – zastosowanie skrętu w liniowej ekstruzji przy
  użyciu Aspose.3D dla Javy
url: /pl/java/linear-extrusion/applying-twist/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Zastosowanie skrętu w ekstruzji liniowej z Aspose.3D dla Javy

## Wprowadzenie

Witamy w tym samouczku krok po kroku, jak **utworzyć skręcony model 3D** poprzez zastosowanie skrętu podczas ekstruzji liniowej przy użyciu Aspose.3D dla Javy. Niezależnie od tego, czy tworzysz wizualizacje architektoniczne, zasoby do gier, czy prototypy inżynieryjne, dodanie skrętu może nadać Twojej geometrii dynamiczny, spiralny wygląd przy zaledwie kilku linijkach kodu.

## Szybkie odpowiedzi
- **Co oznacza „skręt” w ekstruzji?** Obraca profil wokół osi ekstruzji w miarę wydłużania kształtu.  
- **Która klasa API obsługuje skręt?** `LinearExtrusion` udostępnia metodę `setTwist`.  
- **Czy potrzebna jest licencja do uruchomienia przykładu?** Darmowa wersja próbna działa w celach ewaluacyjnych; licencja komercyjna jest wymagana w produkcji.  
- **Czy mogę wyeksportować wynik jako OBJ?** Tak, użyj `scene.save(..., FileFormat.WAVEFRONTOBJ)`.  
- **Jaka wersja Javy jest wymagana?** Java 8 lub nowsza jest w pełni wspierana.

## Wymagania wstępne

Przed przystąpieniem do samouczka upewnij się, że spełniasz następujące wymagania:

- Środowisko programistyczne Java: Upewnij się, że Java jest zainstalowana w Twoim systemie.  
- Biblioteka Aspose.3D: Pobierz i zainstaluj bibliotekę Aspose.3D dla Javy z [linku do pobrania](https://releases.aspose.com/3d/java/).  
- Dokumentacja: Odwołaj się do [dokumentacji Aspose.3D](https://reference.aspose.com/3d/java/) w celu uzyskania szczegółowych wskazówek.

## Importowanie pakietów

Zanim rozpoczniesz proces kodowania, zaimportuj niezbędne pakiety do swojego projektu Java. Oto przykład, jak to zrobić:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Ustawienie katalogu dokumentu

Najpierw określ, gdzie zostanie zapisany wygenerowany plik 3D.

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## Inicjalizacja podstawowego profilu

Następnie utwórz kształt, który zostanie wyekstruzowany. W tym przykładzie używamy prostokąta z małym promieniem zaokrąglenia.

```java
// ExStart:InitializeBaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:InitializeBaseProfile
```

## Tworzenie sceny

Obiekt `Scene` działa jako kontener dla wszystkich węzłów 3D.

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
```

## Tworzenie węzłów

Dodaj dwa węzły potomne do sceny – jeden pozostanie prosty, drugi otrzyma skręt.

```java
// ExStart:CreateNodes
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CreateNodes
```

## Skręt w ekstruzji liniowej

Teraz wykonujemy **skręt w ekstruzji liniowej** na obu węzłach. Lewy węzeł otrzymuje skręt 0° (prosty), natomiast prawy węzeł otrzymuje skręt 90°, tworząc spiralny kształt. Ustawiamy także liczbę przekrojów, aby zapewnić płynną geometrię.

```java
// ExStart:LinearExtrusionWithTwist
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd:LinearExtrusionWithTwist
```

## Eksport pliku OBJ w Javie

Na koniec zapisz scenę w szeroko wspieranym formacie OBJ. Demonstracja **eksportu pliku OBJ w Javie** pokazuje możliwości Aspose.3D.

```java
// ExStart:Save3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:Save3DScene
```

## Dlaczego to ma znaczenie

Utworzenie skręconego modelu 3D daje potężny efekt wizualny bez konieczności korzystania z zewnętrznych narzędzi modelujących. Jest to szczególnie przydatne dla:

- **Części mechanicznych**, które wymagają cech spiralnych (np. sprężyny, śruby).  
- **Projektów artystycznych**, gdzie subtelna spirala dodaje waloru wizualnego.  
- **Zasobów do gier**, które korzystają z niskopoligonowej, proceduralnie generowanej geometrii.

## Typowe problemy i wskazówki

| Problem | Rozwiązanie |
|-------|----------|
| Skręt wygląda płasko lub nie występuje | Upewnij się, że `setSlices` jest ustawione na wystarczająco wysoką wartość (np. 100), aby zapewnić płynną rotację. |
| Plik OBJ nie otwiera się w przeglądarce | Zweryfikuj, czy ścieżka wyjściowa (`MyDir`) jest prawidłowa i czy plik ma odpowiednie uprawnienia do zapisu. |
| Nieoczekiwane skalowanie | Sprawdź system jednostek swojego profilu źródłowego; Aspose.3D domyślnie pracuje w metrach. |

## Najczęściej zadawane pytania

**Q: Czy mogę używać Aspose.3D dla Javy do pracy z innymi formatami plików 3D?**  
A: Tak, Aspose.3D obsługuje szeroką gamę formatów, takich jak FBX, STL, 3MF i inne.

**Q: Gdzie mogę znaleźć wsparcie dla Aspose.3D dla Javy?**  
A: Odwiedź [forum Aspose.3D](https://forum.aspose.com/c/3d/18) w celu uzyskania pomocy społeczności i oficjalnego wsparcia.

**Q: Czy dostępna jest darmowa wersja próbna?**  
A: Tak, wersję próbną można pobrać [tutaj](https://releases.aspose.com/).

**Q: Jak uzyskać tymczasową licencję do testów?**  
A: Tymczasową licencję można pobrać ze [strony tymczasowej licencji](https://purchase.aspose.com/temporary-license/).

**Q: Gdzie mogę kupić pełną licencję?**  
A: Pełną licencję Aspose.3D dla Javy można nabyć na [stronie zakupu](https://purchase.aspose.com/buy).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Ostatnia aktualizacja:** 2025-12-17  
**Testowano z:** Aspose.3D 24.11 for Java  
**Autor:** Aspose  

---