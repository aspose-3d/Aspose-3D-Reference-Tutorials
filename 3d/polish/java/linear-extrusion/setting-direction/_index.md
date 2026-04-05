---
date: 2026-02-22
description: Dowiedz się, jak ustawić kierunek w ekstruzji liniowej i wyeksportować
  model 3D w formacie OBJ przy użyciu Aspose.3D dla Javy. Postępuj zgodnie z naszym
  przewodnikiem krok po kroku.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Jak ustawić kierunek w ekstruzji liniowej przy użyciu Aspose.3D dla Javy
url: /pl/java/linear-extrusion/setting-direction/
weight: 12
---

02-22  
**Tested With:** Aspose.3D for Java (latest release)  
**Author:** Aspose

We can translate "Last Updated" to "Ostatnia aktualizacja", "Tested With" to "Testowano z", "Author" to "Autor". But not required? The instruction says translate all text content. So yes.

Let's translate.

Now produce final output.

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak ustawić kierunek w ekstruzji liniowej przy użyciu Aspose.3D dla Javy

## Wprowadzenie

W tym obszernej tutorialu odkryjesz **jak ustawić kierunek** podczas wykonywania ekstruzji liniowej przy użyciu Aspose.3D dla Javy. Niezależnie od tego, czy tworzysz narzędzie podobne do CAD, czy generujesz geometrie dla silnika gry, kontrolowanie kierunku ekstruzji pozwala stworzyć dokładnie taki kształt, jakiego potrzebujesz. Przejdziemy krok po kroku, od inicjalizacji profilu po zapis wyniku jako pliku OBJ, abyś mógł również **eksportować pliki 3d model obj** bezpośrednio z Javy.

## Szybkie odpowiedzi
- **Jaką klasą główną używa się do ekstruzji liniowej?** `LinearExtrusion`
- **Która metoda definiuje kierunek ekstruzji?** `setDirection(Vector3 direction)`
- **Czy mogę wyeksportować wynik jako OBJ?** Tak, używając `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **Czy potrzebna jest licencja do rozwoju?** Dostępna jest darmowa wersja próbna; licencja jest wymagana w środowisku produkcyjnym.
- **Jakie IDE Java działa najlepiej?** IntelliJ IDEA lub Eclipse są w pełni wspierane.

## Czym jest ekstruzja liniowa?

Ekstruzja liniowa przyjmuje profil 2‑D (np. prostokąt lub koło) i wydłuża go wzdłuż prostej linii, tworząc bryłę 3‑D. Domyślnie ekstruzja podąża wzdłuż dodatniej osi Z, ale Aspose.3D pozwala zmienić tę ścieżkę za pomocą właściwości `setDirection`.

## Dlaczego ustawiać kierunek w ekstruzji liniowej?

Ustawienie własnego kierunku jest przydatne, gdy:
- Dopasowujesz geometrię do istniejących obiektów w scenie.
- Tworzysz pochyłe lub skośne części bez dodatkowych kroków transformacji.
- Eksportujesz modele, które muszą odpowiadać określonemu systemowi współrzędnych (np. do druku 3‑D lub silników gier).

## Wymagania wstępne

Zanim przejdziemy dalej, upewnij się, że masz:

- Podstawową znajomość Javy.
- Zainstalowaną bibliotekę Aspose.3D. Możesz ją pobrać [tutaj](https://releases.aspose.com/3d/java/).
- IDE, takie jak Eclipse lub IntelliJ IDEA.

## Importowanie pakietów

Najpierw zaimportuj przestrzenie nazw, które dostarczają podstawowe klasy 3‑D oraz typy pomocnicze.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Krok 1: Inicjalizacja podstawowego profilu

Utwórz kształt, który zostanie wyekstruzowany. W tym przykładzie używamy `RectangleShape` z małym promieniem zaokrąglenia, aby krawędzie były gładkie.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Krok 2: Utworzenie sceny

Obiekt `Scene` działa jako kontener dla wszystkich węzłów 3‑D, świateł, kamer i materiałów.

```java
Scene scene = new Scene();
```

## Krok 3: Tworzenie węzłów

Dodaj dwa węzły potomne do korzenia sceny — jeden dla ekstruzji po lewej stronie, a drugi dla ekstruzji po prawej stronie. Węzeł prawy jest przesunięty, aby dwa obiekty się nie nakładały.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Krok 4: Wykonanie ekstruzji liniowej na lewym węźle

Ekstruzuj profil w lewym węźle, używając domyślnego kierunku wzdłuż osi Z. Dodajemy także pełny obrót 360° i zwiększamy liczbę przekrojów, aby uzyskać gładszą siatkę.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Krok 5: Wykonanie ekstruzji liniowej na prawym węźle z kierunkiem

Tutaj **ustawiamy kierunek**. Przekazując własny `Vector3` do `setDirection`, ekstruzja podąża wektorem (0.3, 0.2, 1), tworząc pochyły kształt.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Krok 6: Zapis sceny 3D

Na koniec wyeksportuj scenę do formatu Wavefront OBJ. Ten krok pokazuje, jak **zapiswać pliki obj java** i ułatwia podgląd wyniku w dowolnym przeglądarce 3‑D.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Typowe problemy i rozwiązania

| Problem | Dlaczego się pojawia | Rozwiązanie |
|---------|----------------------|-------------|
| Plik OBJ jest pusty | Profil nie został dodany do węzła | Upewnij się, że `createChildNode` jest wywoływane na prawidłowym węźle |
| Kierunek wydaje się niezmieniony | `setDirection` został wywołany po tym, jak ekstruzja już została skonstruowana | Ustaw kierunek wewnątrz inicjalizatora `LinearExtrusion`, jak pokazano |
| Siatka o niskiej rozdzielczości | Wartość `setSlices` jest zbyt niska | Zwiększ liczbę przekrojów (np. 100 lub więcej) |

## Zakończenie

Teraz wiesz **jak ustawić kierunek** w ekstruzji liniowej, jak dostosować ustawienia skrętu i liczby przekrojów oraz jak **eksportować pliki 3d model obj** przy użyciu Aspose.3D dla Javy. Te techniki dają precyzyjną kontrolę nad tworzeniem geometrii i ułatwiają integrację zasobów 3‑D w większych pipeline’ach.

## FAQ

### P1: Czy mogę używać Aspose.3D z innymi językami programowania?

A1: Aspose.3D obsługuje różne języki programowania, w tym .NET i Javę.

### P2. Czy dostępna jest darmowa wersja próbna Aspose.3D?

A2: Tak, możesz wypróbować funkcje Aspose.3D w darmowej wersji próbnej [tutaj](https://releases.aspose.com/).

### P3: Gdzie mogę znaleźć szczegółową dokumentację Aspose.3D dla Javy?

A3: Kompleksowa dokumentacja jest dostępna [tutaj](https://reference.aspose.com/3d/java/).

### P4: Jak mogę uzyskać wsparcie dla Aspose.3D?

A4: Odwiedź [forum Aspose.3D](https://forum.aspose.com/c/3d/18), aby uzyskać pomoc lub zadać pytania.

### P5: Czy dostępne są tymczasowe licencje dla Aspose.3D?

A5: Tak, tymczasową licencję możesz uzyskać [tutaj](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Ostatnia aktualizacja:** 2026-02-22  
**Testowano z:** Aspose.3D for Java (latest release)  
**Autor:** Aspose