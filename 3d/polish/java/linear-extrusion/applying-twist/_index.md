---
date: 2026-02-20
description: Dowiedz się, jak stworzyć scenę 3D i zastosować liniowy skręt ekstruzji
  przy użyciu Aspose.3D for Java. Eksportuj pliki OBJ dzięki prostym, krok po kroku
  instrukcjom.
linktitle: Create 3D Scene with Twist in Linear Extrusion – Aspose.3D for Java
second_title: Aspose.3D Java API
title: Utwórz scenę 3D z obrotem w ekstruzji liniowej – Aspose.3D dla Javy
url: /pl/java/linear-extrusion/applying-twist/
weight: 14
---

/products/products-backtop-button >}}

Check that we kept all shortcodes and code block placeholders. Yes.

Make sure we didn't translate any URLs. They remain unchanged.

All headings preserved.

Now output only the translated content.{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Utwórz scenę 3D z obrotem w liniowej ekstruzji – Aspose.3D for Java

## Wprowadzenie

W tym praktycznym **java 3d tutorial** nauczysz się **tworzyć scenę 3d**, stosować *obrotową liniową ekstruzję* oraz w końcu **eksportować pliki obj java** przy użyciu Aspose.3D for Java. Niezależnie od tego, czy tworzysz zasób do gry, prototyp CAD, czy efekt wizualny, dodanie obrotu podczas ekstruzji nadaje Twoim modelom dynamiczny, spiralny wygląd, którego trudno osiągnąć przy zwykłej ekstruzji.

## Szybkie odpowiedzi
- **Co oznacza „twist” w ekstruzji?** Obraca profil stopniowo wzdłuż ścieżki ekstruzji.  
- **Która biblioteka udostępnia funkcję twist?** Aspose.3D for Java.  
- **Czy mogę wyeksportować wynik jako OBJ?** Tak – użyj `FileFormat.WAVEFRONTOBJ`.  
- **Czy potrzebna jest licencja do tego tutorialu?** Wymagana jest tymczasowa lub pełna licencja do użytku produkcyjnego.  
- **Jakiej wersji Javy potrzebuję?** Java 8 lub nowsza.

## Co to jest „twist” w liniowej ekstruzji?

Twist to przekształcenie, które obraca każdy przekrój ekstruzowanego kształtu o określony kąt. Kontrolując kąt, możesz tworzyć spirale, śruby lub subtelne skręty, które dodają wizualnego zainteresowania płaskim ekstruzjom.

## Dlaczego warto używać Aspose.3D for Java?

- **Obsługa wielu formatów:** Import i eksport dziesiątek formatów 3D, w tym OBJ, FBX i STL.  
- **Czyste API Java:** Brak zależności natywnych, co ułatwia integrację w każdym projekcie Java.  
- **Wysokowydajny silnik geometryczny:** Obsługuje złożone operacje, takie jak twist, bez utraty szybkości.

## Wymagania wstępne

- **Java Development Kit (JDK) 8+** zainstalowany na komputerze.  
- **Aspose.3D for Java** – pobierz z [download link](https://releases.aspose.com/3d/java/).  
- Znajomość podstawowej składni Javy i koncepcji 3‑D.  
- Dostęp do oficjalnej [dokumentacji Aspose.3D](https://reference.aspose.com/3d/java/) w celu odniesienia.

## Importowanie pakietów

Najpierw wprowadź wymagane klasy Aspose.3D do swojego projektu.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Krok 1: Ustaw katalog dokumentu

Zdefiniuj, gdzie zostanie zapisany wygenerowany plik OBJ. Zastąp symboliczny placeholder rzeczywistą ścieżką folderu w swoim systemie.

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## Krok 2: Zainicjuj profil bazowy

Utwórz kształt, który będzie ekstruzowany. Tutaj używamy prostokąta z małym promieniem zaokrąglenia, aby krawędzie były łagodniejsze.

```java
// ExStart:InitializeBaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:InitializeBaseProfile
```

## Krok 3: Utwórz scenę, w której będą przechowywane węzły

Obiekt `Scene` jest kontenerem dla wszystkich jednostek 3‑D (siatek, świateł, kamer itp.).  

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
```

## Krok 4: Dodaj węzły lewy i prawy

Utworzymy dwa węzły rodzeństwa: jeden bez twistu (do porównania) i jeden z 90‑stopniowym twistem.

```java
// ExStart:CreateNodes
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CreateNodes
```

## Krok 5: Wykonaj liniową ekstruzję z twistem

Konstruktor `LinearExtrusion` przyjmuje profil i długość ekstruzji.  
- `setTwist(0)` → brak rotacji (prosta ekstruzja).  
- `setTwist(90)` → pełny obrót o 90° wzdłuż długości.  
Oba węzły używają 100 przekrojów dla płynnej geometrii.

```java
// ExStart:LinearExtrusionWithTwist
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd:LinearExtrusionWithTwist
```

## Krok 6: Zapisz scenę 3D jako OBJ

Na koniec zapisz scenę do pliku OBJ, aby móc ją otworzyć w dowolnym standardowym przeglądarce 3‑D.

```java
// ExStart:Save3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:Save3DScene
```

## Typowe problemy i wskazówki

- **Błędy ścieżki pliku:** Upewnij się, że `MyDir` kończy się separatorem ścieżki (`/` lub `\\`) odpowiednim dla Twojego systemu.  
- **Zbyt duży kąt twistu:** Kąty powyżej 360° mogą powodować nakładanie się geometrii; trzymaj się zakresu 0‑360° dla przewidywalnych rezultatów.  
- **Wydajność:** Zwiększenie `setSlices` poprawia gładkość, ale może wpływać na pamięć; 100 przekrojów to dobry kompromis w większości przypadków.

## Najczęściej zadawane pytania (Original)

### Q1: Czy mogę używać Aspose.3D for Java do pracy z innymi formatami plików 3D?

A1: Tak, Aspose.3D obsługuje różne formaty plików 3D, umożliwiając import, eksport i manipulację różnorodnymi typami plików.

### Q2: Gdzie mogę znaleźć wsparcie dla Aspose.3D for Java?

A2: Odwiedź [forum Aspose.3D](https://forum.aspose.com/c/3d/18) w celu uzyskania pomocy społeczności i dyskusji.

### Q3: Czy dostępna jest darmowa wersja próbna Aspose.3D for Java?

A3: Tak, wersję próbną można pobrać [tutaj](https://releases.aspose.com/).

### Q4: Jak mogę uzyskać tymczasową licencję dla Aspose.3D for Java?

A4: Uzyskaj tymczasową licencję na [stronie tymczasowej licencji](https://purchase.aspose.com/temporary-license/).

### Q5: Gdzie mogę kupić Aspose.3D for Java?

A5: Zakup Aspose.3D for Java można dokonać na [stronie zakupu](https://purchase.aspose.com/buy).

## Dodatkowe FAQ (AI‑Optimized)

**Q: Czy mogę zmienić kierunek twistu?**  
A: Tak – użyj ujemnego kąta w `setTwist()`, aby obrócić w przeciwnym kierunku.

**Q: Czy można zastosować różne wartości twistu wzdłuż ekstruzji?**  
A: Aspose.3D obecnie stosuje jednolity twist; aby uzyskać zmienny twist, trzeba ręcznie generować wiele segmentów.

**Q: Jak wyświetlić wyeksportowany plik OBJ?**  
A: Każdy standardowy przeglądarka 3‑D (np. Blender, MeshLab) może otworzyć pliki OBJ.

**Q: Czy biblioteka obsługuje mapowanie tekstur na skręconych ekstruzjach?**  
A: Tak – po ekstruzji możesz przypisać materiały lub współrzędne UV do siatki węzła.

## Podsumowanie

Udało Ci się **utworzyć scenę 3D**, zastosować **obrotową liniową ekstruzję** oraz wyeksportować wynik jako plik OBJ przy użyciu Aspose.3D for Java. Eksperymentuj z różnymi profilami, kątami twistu i liczbą przekrojów, aby tworzyć unikalne geometrie dla gier, symulacji lub druku 3‑D.

---

**Ostatnia aktualizacja:** 2026-02-20  
**Testowano z:** Aspose.3D for Java 24.11  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}