---
date: 2026-05-24
description: Dowiedz się, jak wyciągnąć kształt przy użyciu Aspose.3D for Java. Ten
  samouczek modelowania 3D w Java obejmuje linear extrusion, center control, direction,
  slices, twist i wiele więcej!
keywords:
- how to extrude shape
- java 3d geometry
- create 3d model java
- create solid from 2d
linktitle: Tworzenie modeli 3D przy użyciu Linear Extrusion w Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to extrude shape using Aspose.3D for Java. This java 3d modeling
    tutorial covers linear extrusion, center control, direction, slices, twist and
    more!
  headline: How to Extrude Shape - Creating 3D Models with Linear Extrusion in Java
  type: TechArticle
- description: Learn how to extrude shape using Aspose.3D for Java. This java 3d modeling
    tutorial covers linear extrusion, center control, direction, slices, twist and
    more!
  name: How to Extrude Shape - Creating 3D Models with Linear Extrusion in Java
  steps:
  - name: Define the 2‑D profile
    text: Create a `Polygon` or `Polyline` that represents the shape you want to extrude.
      *A `Polygon` represents a closed shape defined by vertices, while a `Polyline`
      is an open series of line segments.* Ready to get started? [Perform Linear Extrusion
      Now](./performing-linear-extrusion/) For a detailed tuto
  - name: Configure extrusion options
    text: 'Set the center, direction, slices, twist, and twist offset on an `Extrusion`
      object. *The `Extrusion` class encapsulates all parameters needed to generate
      a 3‑D mesh from a 2‑D profile.* Get hands‑on with center control: [Control Center
      in Linear Extrusion](./controlling-center/) Read more about cen'
  - name: Add the extrusion to the scene
    text: 'Instantiate a `Scene`, attach the extrusion mesh, and export to your desired
      format. *`Scene` is the container that holds all 3‑D objects and handles exporting
      to various file formats.* Ready to set the direction? [Explore Now](./setting-direction/)
      Learn more about direction: [Setting Direction in '
  - name: Export or render
    text: 'Use `Scene.save()` to write the model to OBJ, STL, or any supported format.
      *`Scene.save()` writes the entire scene to the specified file format, applying
      any necessary post‑processing.* Start specifying slices: [Learn More](./specifying-slices/)
      Detailed guide: [Specifying Slices in Linear Extrusio'
  type: HowTo
- questions:
  - answer: Yes, a valid Aspose license is required for production use, but a free
      trial is available for evaluation.
    question: Can I use Aspose.3D for Java in a commercial project?
  - answer: The library works with Java 8 and newer runtimes, including Java 11, 17,
      and 21.
    question: Which Java versions are supported?
  - answer: Aspose.3D handles mesh generation efficiently, but you can call `scene.dispose()`
      when you’re done with large scenes to free native resources.
    question: Do I need to manage memory for large extrusions?
  - answer: Absolutely – you can create several extrusion objects, position them independently,
      and add them to the same scene.
    question: Can I combine multiple extrusion operations in one model?
  - answer: Yes, the “Applying Twist” and “Using Twist Offset” tutorials demonstrate
      how to set both properties on the same extrusion object.
    question: Is there sample code for applying twist and twist offset together?
  type: FAQPage
second_title: Aspose.3D Java API
title: Jak wyciągnąć kształt - Tworzenie modeli 3D przy użyciu Linear Extrusion w
  Java
url: /pl/java/linear-extrusion/
weight: 23
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak wyciągnąć kształt – Tworzenie modeli 3D przy użyciu liniowego wyciągania w Javie

## Szybkie odpowiedzi
- **Czym jest liniowe wyciąganie?** Przekształcenie 2‑D szkicu w bryłę 3‑D poprzez wydłużenie wzdłuż kierunku.  
- **Która biblioteka Ci pomaga?** Aspose.3D for Java udostępnia płynne API do zadań wyciągania.  
- **Czy potrzebuję licencji?** Darmowa wersja próbna wystarcza do nauki; licencja komercyjna jest wymagana w produkcji.  
- **Jaka wersja Javy jest wymagana?** Java 8 lub wyższa.  
- **Czy mogę zastosować skręcenia lub przesunięcia?** Tak – API obsługuje kąt skrętu i offset skrętu od razu.  

## Co to jest „jak wyciągnąć kształt” w Javie?
Operacja `Extrusion` jest podstawową funkcją Aspose.3D, która konwertuje płaską konturę na siatkę wolumetryczną. W prostych słowach, podajesz profil 2‑D (na przykład prostokąt lub własny wielokąt), określasz, jak daleko go wyciągnąć, a biblioteka tworzy dla Ciebie geometrię 3‑D.

## Dlaczego warto używać Aspose.3D dla Javy?
Aspose.3D obsługuje **ponad 50 formatów wejściowych i wyjściowych** – w tym OBJ, STL, FBX i GLTF – i może generować siatki z aż **10 000 wierzchołkami na wyciąganie** bez ładowania całej sceny do pamięci. Jego wieloplatformowy silnik działa na Windows, Linux i macOS, dostarczając spójne wyniki zarówno na stacji roboczej, jak i na bezgłowym serwerze CI.

## Wymagania wstępne
- Java 8 lub nowsza zainstalowana na Twoim komputerze deweloperskim.  
- Maven lub Gradle do zarządzania zależnościami.  
- Plik licencji Aspose.3D for Java (opcjonalny w wersji próbnej).  

## Jak działa liniowe wyciąganie?
Liniowe wyciąganie tworzy bryłę 3‑D poprzez przeciągnięcie profilu 2‑D wzdłuż prostej linii. Silnik najpierw trianguluje profil, następnie powiela go w każdym przekroju wzdłuż osi wyciągania, a na końcu łączy przekroje, tworząc szczelną siatkę. Ten proces automatycznie oblicza wektory normalne i współrzędne UV, więc możesz renderować wynik bez dodatkowego przetwarzania geometrii.

## Jakie są kluczowe parametry liniowego wyciągania?
Liniowe wyciąganie można dostosować za pomocą kilku parametrów. **center** określa punkt obrotu profilu przed wyciąganiem. Wektor **direction** ustawia oś wyciągania, domyślnie dodatnią oś Z. **Slices** kontroluje liczbę pośrednich przekrojów, wpływając na płynność przy skręconych lub zwężających się kształtach. **Twist angle** obraca profil stopniowo od początku do końca, natomiast **twist offset** dodaje liniowe przesunięcie wzdłuż osi, umożliwiając formy spiralne.

- **Center** – Punkt obrotu, wokół którego profil jest pozycjonowany przed wyciąganiem.  
- **Direction** – Wektor definiujący oś wyciągania; domyślnie dodatnia oś Z.  
- **Slices** – Liczba pośrednich przekrojów; więcej przekrojów daje płynniejsze przejścia przy skręconych lub zwężających się wyciągnięciach.  
- **Twist Angle** – Całkowity obrót zastosowany do profilu od początku do końca, wyrażony w stopniach.  
- **Twist Offset** – Liniowe przesunięcie, które przemieszcza profil wzdłuż osi wyciągania podczas skręcania, umożliwiając kształty spiralne.

## Wykonywanie liniowego wyciągania w Aspose.3D dla Javy

Załaduj swój profil, skonfiguruj parametry i pozwól API wygenerować siatkę. Poniższe kroki przedstawiają typowy przepływ pracy.

### Krok 1: Zdefiniuj profil 2‑D
Utwórz `Polygon` lub `Polyline`, które reprezentują kształt, który chcesz wyciągnąć.  
*`Polygon` reprezentuje zamknięty kształt zdefiniowany wierzchołkami, natomiast `Polyline` jest otwartą serią odcinków liniowych.*  
Gotowy, aby rozpocząć? [Wykonaj liniowe wyciąganie teraz](./performing-linear-extrusion/)  
Aby uzyskać szczegółowy samouczek, zobacz [Wykonywanie liniowego wyciągania w Aspose.3D dla Javy](./performing-linear-extrusion/).

### Krok 2: Skonfiguruj opcje wyciągania
Ustaw center, direction, slices, twist i twist offset na obiekcie `Extrusion`.  
*Klasa `Extrusion` kapsułkuje wszystkie parametry potrzebne do wygenerowania siatki 3‑D z profilu 2‑D.*  
Praktyczne sterowanie środkiem: [Sterowanie środkiem w liniowym wyciąganiu](./controlling-center/)  
Czytaj więcej o sterowaniu środkiem: [Sterowanie środkiem w liniowym wyciąganiu z Aspose.3D dla Javy](./controlling-center/)

### Krok 3: Dodaj wyciąganie do sceny
Utwórz `Scene`, dołącz siatkę wyciągania i wyeksportuj do wybranego formatu.  
*`Scene` jest kontenerem, który przechowuje wszystkie obiekty 3‑D i obsługuje eksport do różnych formatów plików.*  
Gotowy, aby ustawić kierunek? [Zbadaj teraz](./setting-direction/)  
Dowiedz się więcej o kierunku: [Ustawianie kierunku w liniowym wyciąganiu z Aspose.3D dla Javy](./setting-direction/)

### Krok 4: Eksportuj lub renderuj
Użyj `Scene.save()`, aby zapisać model w formacie OBJ, STL lub innym obsługiwanym formacie.  
*`Scene.save()` zapisuje całą scenę w określonym formacie pliku, stosując niezbędne przetwarzanie końcowe.*  
Rozpocznij określanie przekrojów: [Dowiedz się więcej](./specifying-slices/)  
Szczegółowy przewodnik: [Określanie przekrojów w liniowym wyciąganiu z Aspose.3D dla Javy](./specifying-slices/)

## Jak zastosować skręt do wyciągania?
Zastosuj skręt, ustawiając właściwość `twistAngle` w opcjach wyciągania. Silnik obraca każdy przekrój proporcjonalnie, tworząc efekt helisy. Regulując kąt, możesz uzyskać wszystko, od subtelnego skręcenia po pełne spirale 360°, przydatne w elementach dekoracyjnych lub funkcjonalnych sprężynach.  
Gotowy, aby wprowadzić skręt? [Zastosuj skręt teraz](./applying-twist/)  
Pełny przykład: [Zastosowanie skrętu w liniowym wyciąganiu z Aspose.3D dla Javy](./applying-twist/)

## Jak używać offsetu skrętu dla kształtów spiralnych?
Offset skrętu przesuwa każdy przekrój wzdłuż osi wyciągania podczas obracania, tworząc spiralne schody lub geometrię korkociągu. Połączenie kąta skrętu z dodatnim offsetem daje płynną rampę helisy, natomiast ujemny offset może tworzyć spirale schodzące w dół. Technika ta jest idealna do modelowania gwintów, sprężyn lub artystycznych wstążek.  
Rozwijaj umiejętności: [Poznaj offset skrętu](./using-twist-offset/)  
Kompletny przewodnik: [Używanie offsetu skrętu w liniowym wyciąganiu z Aspose.3D dla Javy](./using-twist-offset/)

## Typowe zastosowania liniowego wyciągania
- **Części mechaniczne** – Szybko generuj śruby, wały i wsporniki z prostych szkiców.  
- **Elementy architektoniczne** – Wyciągaj plany pięter w ściany lub kolumny dla prototypów BIM.  
- **Zasoby gier** – Twórz low‑poly obiekty, takie jak ogrodzenia, rury lub dekoracyjne szyny bezpośrednio z grafiki 2‑D.  
- **Narzędzia edukacyjne** – Wizualizuj powierzchnie matematyczne poprzez wyciąganie krzywych parametrycznych.

## Rozwiązywanie typowych problemów
- **Brakujące powierzchnie** – Upewnij się, że profil jest zamkniętą pętlą; otwarte kontury powodują luki.  
- **Nadmierne zużycie pamięci** – Zmniejsz liczbę `slices` lub włącz `scene.setMemoryOptimization(true)`.  
- **Nieprawidłowy kierunek skrętu** – Pozytywne kąty obracają zgodnie z ruchem wskazówek zegara przy patrzeniu wzdłuż kierunku wyciągania; użyj wartości ujemnych, aby odwrócić.

## Najczęściej zadawane pytania

**Q: Czy mogę używać Aspose.3D for Java w projekcie komercyjnym?**  
A: Tak, wymagana jest ważna licencja Aspose do użytku produkcyjnego, ale dostępna jest darmowa wersja próbna do oceny.

**Q: Jakie wersje Javy są obsługiwane?**  
A: Biblioteka działa z Java 8 i nowszymi środowiskami uruchomieniowymi, w tym Java 11, 17 i 21.

**Q: Czy muszę zarządzać pamięcią przy dużych wyciągnięciach?**  
A: Aspose.3D efektywnie obsługuje generowanie siatek, ale możesz wywołać `scene.dispose()`, gdy skończysz z dużymi scenami, aby zwolnić zasoby natywne.

**Q: Czy mogę połączyć wiele operacji wyciągania w jednym modelu?**  
A: Oczywiście – możesz utworzyć kilka obiektów `Extrusion`, pozycjonować je niezależnie i dodać do tej samej sceny.

**Q: Czy istnieje przykładowy kod do jednoczesnego zastosowania skrętu i offsetu skrętu?**  
A: Tak, samouczki „Applying Twist” i „Using Twist Offset” pokazują, jak ustawić obie właściwości na tym samym obiekcie `Extrusion`.

---

**Ostatnia aktualizacja:** 2026-05-24  
**Testowano z:** Aspose.3D for Java 24.11  
**Autor:** Aspose  

{{< blocks/products/products-backtop-button >}}

## Powiązane samouczki

- [Samouczek Java 3D Graphics – Center w liniowym wyciąganiu](/3d/java/linear-extrusion/controlling-center/)
- [Jak ustawić kierunek w liniowym wyciąganiu z Aspose.3D dla Javy](/3d/java/linear-extrusion/setting-direction/)
- [Tworzenie 3D wyciągania z przekrojami – Aspose.3D dla Javy](/3d/java/linear-extrusion/specifying-slices/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}