---
date: 2026-04-08
description: Dowiedz się, jak stworzyć cylinder z przesuniętą górą w Aspose.3D dla
  Javy, dodać węzeł potomny w Javie, ustawić przesunięcie górnej części, wygenerować
  model 3D i wyeksportować OBJ przy użyciu tymczasowej licencji Aspose.
keywords:
- aspose temporary license
- generate 3d model
- add child node java
- java export obj
- set offset top
linktitle: Licencja tymczasowa Aspose – Utwórz cylinder z przesuniętym górnym końcem
  (Java)
second_title: Aspose.3D Java API
title: Tymczasowa licencja Aspose – Tworzenie walca z przesuniętym górnym końcem (Java)
url: /pl/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Licencja tymczasowa Aspose – Tworzenie walca z przesuniętym wierzchołkiem (Java)

## Wprowadzenie

Jeśli chcesz **tworzyć walec** obiekty z niestandardowym przesunięciem górnej części w scenie 3D opartej na Javie, Aspose.3D upraszcza cały proces. W tym samouczku przeprowadzimy Cię przez każdy krok — od skonfigurowania sceny po wyeksportowanie finalnego modelu jako pliku OBJ — abyś mógł z pewnością integrować walce z przesuniętym wierzchołkiem w swoich aplikacjach. Po zakończeniu przewodnika zrozumiesz także, jak **aspose temporary license** pozwala ocenić te funkcje bez pełnego zakupu.

## Szybkie odpowiedzi
- **Jakiej biblioteki użyto?** Aspose.3D for Java  
- **Czy mogę przesunąć górną część walca?** Yes, using `setOffsetTop`  
- **Jak dodać węzeł potomny w Javie?** Call `createChildNode` on the root node  
- **Do którego formatu mogę eksportować?** Wavefront OBJ (`java export obj`)  
- **Czy potrzebuję licencji do testowania?** An **aspose temporary license** is available for evaluation  

## Co to jest licencja tymczasowa Aspose?

**aspose temporary license** jest krótkoterminowym, bezpłatnym kluczem ewaluacyjnym, który odblokowuje pełny zestaw funkcji Aspose.3D for Java podczas rozwoju i testowania. Usuwa znaki wodne wersji ewaluacyjnej i pozwala generować pliki modeli 3D, takie jak OBJ, STL czy FBX, dokładnie tak jak licencja płatna.

## Dlaczego warto używać Aspose.3D dla Javy?

- **High‑level API:** Nie trzeba zarządzać danymi siatki niskiego poziomu.  
- **Cross‑platform:** Działa w każdym środowisku kompatybilnym z JVM.  
- **Built‑in exporters:** Bezpośrednio zapisuje do OBJ, STL, FBX i innych.  
- **Extensible:** Łatwo dodawać węzły potomne, stosować przekształcenia i integrować z innymi bibliotekami Javy.  

## Wymagania wstępne

- **Java Development Kit (JDK)** – zainstalowana kompatybilna wersja.  
- **Aspose.3D for Java library** – pobierz najnowszy plik JAR ze strony oficjalnej [tutaj](https://releases.aspose.com/3d/java/).  
- IDE według własnego wyboru (Eclipse, IntelliJ IDEA, NetBeans itp.).  

## Importowanie pakietów

Najpierw zaimportuj klasy, które będą potrzebne. Umieść te instrukcje na początku swojego pliku Java:

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Przewodnik krok po kroku

### Krok 1: Utwórz scenę Java 3D

**java 3d scene** pełni rolę kontenera dla wszystkich obiektów 3D.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### Krok 2: Zainicjuj walec z przesuniętym wierzchołkiem

Tutaj odpowiadamy na pytanie, **jak stworzyć walec** z niestandardowym przesunięciem. Konstruktor definiuje promień, wysokość, liczbę segmentów (slices), stosów (stacks) oraz czy walec jest zamknięty. Następnie przesuwamy górę przy użyciu `setOffsetTop`.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### Krok 3: Dodaj węzeł potomny w Javie – Dołącz pierwszy walec

Tworzymy węzeł potomny pod głównym węzłem sceny i przenosimy walec do wybranej lokalizacji.

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### Krok 4: Zainicjuj drugi walec (bez przesunięcia)

Dla porównania dodajemy zwykły walec bez przesunięcia.

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### Krok 5: Dodaj węzeł potomny w Javie – Dołącz drugi walec

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Krok 6: Eksport OBJ w Javie – Zapisz scenę jako OBJ

Na koniec **java export obj** całą scenę (oba walce) jako plik Wavefront OBJ, który jest szeroko wspierany przez narzędzia 3D.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

Po uruchomieniu programu znajdziesz plik `CustomizedOffsetTopCylinder.obj` w określonym katalogu, gotowy do otwarcia w Blenderze, Maya lub dowolnym innym przeglądarce obsługującej OBJ.

## Jak wygenerować model 3D i wyeksportować OBJ w Javie

Połączenie `Scene.save(..., FileFormat.WAVEFRONTOBJ)` oraz **aspose temporary license** pozwala szybko **generate 3d model** pliki, bez konieczności używania zewnętrznych konwerterów. Jest to szczególnie przydatne podczas prototypowania lub udostępniania zasobów projektantom.

## Praktyczne zastosowania

- **Architectural visualisation:** Walce z przesuniętym wierzchołkiem modelują kolumny zwężające się w kierunku sufitu.  
- **Mechanical parts:** Tworzenie tłoków lub obudów kół zębatych, gdzie górna powierzchnia jest celowo przesunięta.  
- **Game assets:** Generowanie różnorodnych kształtów filarów w locie, zmniejszając potrzebę ręcznie tworzonych siatek.

## Typowe problemy i rozwiązania

| Problem | Powód | Rozwiązanie |
|-------|--------|-----|
| **Plik OBJ jest pusty** | Scena nie została poprawnie zapisana lub ścieżka jest nieprawidłowa. | Sprawdź, czy katalog wyjściowy istnieje i masz uprawnienia do zapisu. |
| **Przesunięcie nie zastosowano** | Używana jest starsza wersja Aspose.3D. | Zaktualizuj do najnowszej biblioteki, w której obsługiwane jest `setOffsetTop`. |
| **Węzeł potomny niewidoczny** | Transformacja nie została zastosowana. | Upewnij się, że wywołujesz `getTransform().setTranslation` po utworzeniu węzła potomnego. |

## Najczęściej zadawane pytania

**Q: Czy Aspose.3D jest kompatybilny z różnymi IDE Java?**  
A: Tak, działa bezproblemowo z Eclipse, IntelliJ IDEA, NetBeans i innymi IDE.

**Q: Czy mogę zastosować tekstury do utworzonych obiektów 3D?**  
A: Oczywiście! Użyj klasy `Material`, aby przypisać tekstury i właściwości powierzchni.

**Q: Czy istnieją opcje licencjonowania Aspose.3D?**  
A: Dostępne są różne modele licencjonowania; możesz je przeglądać [tutaj](https://purchase.aspose.com/buy).

**Q: Jak mogę uzyskać pomoc lub podzielić się doświadczeniami?**  
A: Dołącz do forum społeczności Aspose.3D [tutaj](https://forum.aspose.com/c/3d/18), aby uzyskać wsparcie i dyskusję.

**Q: Czy dostępna jest licencja tymczasowa do testów?**  
A: Tak, **aspose temporary license** można uzyskać do oceny [tutaj](https://purchase.aspose.com/temporary-license/).

**Ostatnia aktualizacja:** 2026-04-08  
**Testowano z:** Aspose.3D for Java 24.12 (latest)  
**Autor:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}