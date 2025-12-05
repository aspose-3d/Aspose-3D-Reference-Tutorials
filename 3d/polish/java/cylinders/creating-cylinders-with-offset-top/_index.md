---
date: 2025-12-05
description: Dowiedz się, jak tworzyć modele cylindrów z przesuniętymi górnymi częściami
  w Aspose.3D dla Javy, dodawać kroki węzła potomnego w Javie i łatwo eksportować
  pliki OBJ modeli 3D.
language: pl
linktitle: How to Create Cylinder with Offset Top in Aspose.3D for Java
second_title: Aspose.3D Java API
title: Jak stworzyć cylinder z przesuniętym górnym końcem w Aspose.3D dla Javy
url: /java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak utworzyć cylinder z przesuniętym wierzchołkiem w Aspose.3D dla Javy

## Wprowadzenie

Jeśli chcesz **jak utworzyć cylinder** z niestandardowym przesunięciem wierzchołka w scenie 3D opartej na Javie, Aspose.3D upraszcza cały proces. W tym samouczku przeprowadzimy Cię przez każdy krok — od konfiguracji sceny po eksport gotowego modelu jako pliku OBJ — abyś mógł z pewnością integrować cylindry z przesuniętym wierzchołkiem w swoich aplikacjach.

## Szybkie odpowiedzi
- **Jakiej biblioteki używać?** Aspose.3D dla Javy  
- **Czy mogę przesunąć wierzchołek cylindra?** Tak, przy użyciu `setOffsetTop`  
- **Jak dodać węzeł potomny w Javie?** Wywołaj `createChildNode` na węźle głównym  
- **Do jakiego formatu mogę eksportować?** Wavefront OBJ (`export 3d model obj`)  
- **Czy potrzebna jest licencja do testów?** Dostępna jest tymczasowa licencja do oceny  

## Co to jest „jak utworzyć cylinder” z przesuniętym wierzchołkiem?

Utworzenie cylindra z przesuniętym wierzchołkiem oznacza, że górna okrągła powierzchnia jest przesunięta względem podstawy, co pozwala modelować stożkowe lub asymetryczne kształty bez ręcznej manipulacji wierzchołkami. Aspose.3D udostępnia dedykowany konstruktor oraz właściwość `OffsetTop`, aby osiągnąć to w kilku linijkach kodu.

## Dlaczego warto używać Aspose.3D dla Javy?

- **Wysokopoziomowe API:** Nie musisz zarządzać niskopoziomowymi danymi siatki.  
- **Cross‑platform:** Działa w każdym środowisku kompatybilnym z JVM.  
- **Wbudowane eksportery:** Bezpośrednio zapisuj do OBJ, STL, FBX i innych.  
- **Rozszerzalność:** Łatwo dodawaj węzły potomne, stosuj transformacje i integruj z innymi bibliotekami Javy.

## Wymagania wstępne

Zanim przejdziesz do kodu, upewnij się, że masz:

- **Java Development Kit (JDK)** – zainstalowaną kompatybilną wersję.  
- **Aspose.3D dla Javy** – pobierz najnowszy plik JAR z oficjalnej strony [tutaj](https://releases.aspose.com/3d/java/).  
- IDE według własnego wyboru (Eclipse, IntelliJ IDEA, NetBeans itp.).

## Importowanie pakietów

Najpierw zaimportuj klasy, które będą potrzebne. Umieść te instrukcje na początku pliku Java:

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Przewodnik krok po kroku

### Krok 1: Utwórz scenę

Scena działa jako kontener dla wszystkich obiektów 3D.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### Krok 2: Zainicjalizuj cylinder z przesuniętym wierzchołkiem

Tutaj odpowiadamy na pytanie **jak utworzyć cylinder** z niestandardowym przesunięciem. Konstruktor określa promień, wysokość, liczbę segmentów (slices), stosów (stacks) oraz czy cylinder jest zamknięty. Następnie przesuwamy górę przy użyciu `setOffsetTop`.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### Krok 3: Jak **dodać węzeł potomny w Javie** – dołącz pierwszy cylinder

Tworzymy węzeł potomny pod węzłem głównym sceny i przesuwamy cylinder do żądanej lokalizacji.

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### Krok 4: Zainicjalizuj drugi cylinder (bez przesunięcia)

Dla porównania dodajemy zwykły cylinder bez przesunięcia.

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### Krok 5: Jak **dodać węzeł potomny w Javie** – dołącz drugi cylinder

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Krok 6: Jak **wyeksportować model 3D OBJ** – zapisz scenę

Na koniec eksportujemy całą scenę (oba cylindry) jako plik Wavefront OBJ, który jest szeroko wspierany przez narzędzia 3D.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

Po uruchomieniu programu znajdziesz plik `CustomizedOffsetTopCylinder.obj` w określonym katalogu, gotowy do otwarcia w Blenderze, Maya lub innym przeglądarce obsługującej OBJ.

## Typowe problemy i rozwiązania

| Problem | Przyczyna | Rozwiązanie |
|---------|-----------|-------------|
| **Plik OBJ jest pusty** | Scena nie została poprawnie zapisana lub podano złą ścieżkę. | Sprawdź, czy katalog wyjściowy istnieje i masz uprawnienia do zapisu. |
| **Przesunięcie nie zostało zastosowane** | Używana starsza wersja Aspose.3D. | Zaktualizuj do najnowszej biblioteki, w której obsługiwane jest `setOffsetTop`. |
| **Węzeł potomny nie jest widoczny** | Transformacja nie została zastosowana. | Upewnij się, że po utworzeniu węzła wywołujesz `getTransform().setTranslation`. |

## Najczęściej zadawane pytania

**P: Czy Aspose.3D jest kompatybilny z różnymi IDE Javy?**  
O: Tak, działa bezproblemowo w Eclipse, IntelliJ IDEA, NetBeans i innych IDE.

**P: Czy mogę zastosować tekstury do utworzonych obiektów 3D?**  
O: Oczywiście! Użyj klasy `Material`, aby przypisać tekstury i właściwości powierzchni.

**P: Jakie są opcje licencjonowania Aspose.3D?**  
O: Dostępne są różne modele licencjonowania; możesz je poznać [tutaj](https://purchase.aspose.com/buy).

**P: Gdzie mogę uzyskać pomoc lub podzielić się doświadczeniami?**  
O: Dołącz do forum społeczności Aspose.3D [tutaj](https://forum.aspose.com/c/3d/18) w celu uzyskania wsparcia i dyskusji.

**P: Czy dostępna jest tymczasowa licencja do testów?**  
O: Tak, tymczasową licencję można uzyskać do oceny [tutaj](https://purchase.aspose.com/temporary-license/).

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---
**Ostatnia aktualizacja:** 2025-12-05  
**Testowano z:** Aspose.3D dla Javy 24.12 (najnowsza)  
**Autor:** Aspose