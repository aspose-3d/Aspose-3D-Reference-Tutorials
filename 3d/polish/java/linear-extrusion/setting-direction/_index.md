---
date: 2025-12-18
description: Dowiedz się, jak stworzyć scenę 3D i zapisać plik OBJ przy użyciu Aspose.3D
  dla Javy. Postępuj zgodnie z naszym przewodnikiem krok po kroku dotyczącym kierunku
  ekstruzji liniowej.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Utwórz scenę 3D – Ustaw kierunek ekstruzji Aspose.3D Java
url: /pl/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Utwórz scenę 3D – Ustaw kierunek ekstruzji Aspose.3D Java

## Wprowadzenie

W tym samouczku nauczysz się **tworzyć obiekty sceny 3d** i kontrolować kierunek ekstruzji przy użyciu Aspose.3D dla Javy. Niezależnie od tego, czy tworzysz wizualizacje architektoniczne, prototypy produktów, czy zasoby do gier, opanowanie liniowej ekstruzji daje elastyczność w szybkim modelowaniu złożonych kształtów. Przejdziemy krok po kroku, od dodawania węzłów w Javie po **eksportowanie modelu 3d do pliku obj**, abyś mógł od razu zobaczyć rezultat.

## Szybkie odpowiedzi
- **Co oznacza „create 3d scene”?** To inicjalizacja obiektu `Scene` Aspose.3D, który będzie przechowywał całą geometrię, światła i kamery.  
- **Jak ustawić kierunek ekstruzji?** Użyj metody `setDirection(Vector3)` na instancji `LinearExtrusion`.  
- **Jaki format wybrać do eksportu?** Format OBJ (`FileFormat.WAVEFRONTOBJ`) jest szeroko wspierany w przepływach pracy 3‑D.  
- **Czy potrzebna jest licencja na Aspose.3D?** Darmowa wersja próbna wystarcza do rozwoju; licencja komercyjna jest wymagana w produkcji.  
- **Czy mogę dodać więcej węzłów w Javie?** Tak — użyj `scene.getRootNode().createChildNode()`, aby dodać dowolną liczbę obiektów.

## Co to jest przepływ pracy „create 3d scene”?

Przepływ pracy **create 3d scene** zaczyna się od pustego obiektu `Scene`, dodaje geometrię (np. ekstruzowane profile), pozycjonuje ją przy pomocy transformacji i na końcu zapisuje scenę do formatu pliku, takiego jak OBJ. Ten schemat jest podstawą większości aplikacji 3‑D tworzonych przy użyciu Aspose.3D.

## Dlaczego ustawiać kierunek ekstruzji?

Ustawienie kierunku ekstruzji pozwala przechylić, obrócić lub pochylić kształt w trakcie ekstruzji, dając kontrolę nad ostateczną geometrią bez dodatkowego post‑processingu. Jest to szczególnie przydatne przy:

- Tworzeniu zwężających się kolumn lub rur o niestandardowych kształtach.  
- Dopasowywaniu ekstruzji do nietypowych osi w częściach mechanicznych.  
- Generowaniu artystycznych kształtów do efektów wizualnych.

## Wymagania wstępne

Zanim zaczniemy, upewnij się, że masz:

- Podstawową znajomość Javy.  
- Zainstalowaną bibliotekę Aspose.3D – pobierz ją [tutaj](https://releases.aspose.com/3d/java/).  
- IDE, takie jak Eclipse lub IntelliJ IDEA.

## Importowanie pakietów

Najpierw zaimportuj wymagane klasy Aspose.3D:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Krok 1: Inicjalizacja profilu bazowego

Utwórz profil 2‑D, który zostanie ekstruzowany. W tym przykładzie używamy zaokrąglonego prostokąta:

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

> **Porada:** Dostosuj promień zaokrąglenia, aby kontrolować, jak ostre lub gładkie będą rogi prostokąta przed ekstruzją.

## Krok 2: Utworzenie sceny

Teraz **create 3d scene**, która będzie hostować nasze obiekty:

```java
Scene scene = new Scene();
```

## Krok 3: Dodawanie węzłów w Javie – Pozycjonowanie obiektów

Dodamy dwa węzły potomne (lewy i prawy) do węzła głównego sceny i przesuniemy lewy nieco na bok:

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Krok 4: Jak ekstruzować – Węzeł lewy (domyślny kierunek)

Ekstruzujemy profil w lewym węźle używając domyślnego kierunku osi Z. Ustawiamy także pełny obrót 360° i zwiększamy liczbę przekrojów dla płynności:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Krok 5: Jak ustawić kierunek – Węzeł prawy

Tutaj **how to set direction** poprzez podanie własnego `Vector3`. Przechylamy ekstruzję w kierunku wektora (0.3, 0.2, 1):

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Krok 6: Zapis pliku OBJ – Eksport modelu 3D

Na koniec **save obj file**, aby zobaczyć rezultat w dowolnym przeglądarce 3‑D:

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Po otwarciu wygenerowanego pliku OBJ zobaczysz dwa wyekstruzowane prostokąty: jeden z domyślnym kierunkiem, a drugi przechylony zgodnie z ustawionym wektorem.

## Typowe problemy i rozwiązania

| Problem | Przyczyna | Rozwiązanie |
|-------|--------|-----|
| Plik OBJ jest pusty | Scena nie została zapisana lub ścieżka jest nieprawidłowa | Sprawdź, czy `MyDir` wskazuje na folder z prawami zapisu i czy nazwa pliku kończy się na `.obj`. |
| Ekstruzja wygląda płasko | `setSlices` jest za niskie | Zwiększ `setSlices` (np. do 200) dla płynniejszej geometrii. |
| Kierunek nie zmienia się | Wektor nie jest znormalizowany | Użyj znormalizowanego `Vector3` lub dostosuj wartości, aby odzwierciedlały pożądany przechył. |

## Najczęściej zadawane pytania

### Q1: Czy mogę używać Aspose.3D w innych językach programowania?
A1: Aspose.3D obsługuje różne języki, w tym .NET i Javę.

### Q2: Czy dostępna jest darmowa wersja próbna Aspose.3D?
A2: Tak, możesz wypróbować funkcje Aspose.3D w darmowej wersji próbnej [tutaj](https://releases.aspose.com/).

### Q3: Gdzie znajdę szczegółową dokumentację Aspose.3D dla Javy?
A3: Kompleksowa dokumentacja jest dostępna [tutaj](https://reference.aspose.com/3d/java/).

### Q4: Jak mogę uzyskać wsparcie dla Aspose.3D?
A4: Odwiedź [forum Aspose.3D](https://forum.aspose.com/c/3d/18) w celu uzyskania pomocy lub zadania pytań.

### Q5: Czy dostępne są tymczasowe licencje na Aspose.3D?
A5: Tak, tymczasową licencję możesz uzyskać [tutaj](https://purchase.aspose.com/temporary-license/).

---

**Ostatnia aktualizacja:** 2025-12-18  
**Testowano z:** Aspose.3D 24.11 dla Javy  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}