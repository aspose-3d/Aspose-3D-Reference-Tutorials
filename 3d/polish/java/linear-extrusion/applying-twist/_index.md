---
title: Stosowanie skrętu w wytłaczaniu liniowym za pomocą Aspose.3D dla Java
linktitle: Stosowanie skrętu w wytłaczaniu liniowym za pomocą Aspose.3D dla Java
second_title: Aspose.3D API Java
description: Dowiedz się, jak dodać zwrot akcji do swoich modeli 3D za pomocą Aspose.3D dla Java. Postępuj zgodnie z naszym przewodnikiem krok po kroku, aby uzyskać ulepszone efekty wytłaczania liniowego.
weight: 14
url: /pl/java/linear-extrusion/applying-twist/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Stosowanie skrętu w wytłaczaniu liniowym za pomocą Aspose.3D dla Java

## Wstęp

Witamy w tym samouczku krok po kroku dotyczącym zastosowania skrętu w wytłaczaniu liniowym przy użyciu Aspose.3D dla Java. Aspose.3D to potężna biblioteka Java, która umożliwia programistom pracę z formatami plików 3D, oferując solidną funkcjonalność do tworzenia, manipulowania i renderowania scen 3D. W tym samouczku dowiemy się, jak zastosować efekt skrętu podczas procesu wytłaczania liniowego, aby ulepszyć modele 3D.

## Warunki wstępne

Zanim przejdziesz do samouczka, upewnij się, że spełniasz następujące wymagania wstępne:

- Środowisko programistyczne Java: Upewnij się, że masz zainstalowaną Javę w swoim systemie.
-  Biblioteka Aspose.3D: Pobierz i zainstaluj bibliotekę Aspose.3D dla Java z[link do pobrania](https://releases.aspose.com/3d/java/).
-  Dokumentacja: Patrz[Dokumentacja Aspose.3D](https://reference.aspose.com/3d/java/) w celu uzyskania kompleksowych wskazówek.

## Importuj pakiety

Przed rozpoczęciem procesu kodowania zaimportuj niezbędne pakiety do swojego projektu Java. Oto przykład, jak to zrobić:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Krok 1: Ustaw katalog dokumentów

Rozpocznij od ustawienia katalogu dokumentów, w którym zostanie zapisana scena 3D.

```java
// ExStart:Ustaw katalog dokumentów
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## Krok 2: Zainicjuj profil podstawowy

Zainicjuj profil bazowy, który ma zostać wyciągnięty. W tym przykładzie używamy kształtu prostokąta z promieniem zaokrąglenia.

```java
// ExStart:InitializeBaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:InitializeBaseProfile
```

## Krok 3: Utwórz scenę

Utwórz scenę 3D, w której będą znajdować się wyciągnięte węzły.

```java
// ExStart: Utwórz scenę
Scene scene = new Scene();
// Rozwiń: Utwórz scenę
```

## Krok 4: Utwórz węzły

Utwórz lewy i prawy węzeł w scenie. Dostosuj tłumaczenie lewego węzła.

```java
// ExStart: Utwórz węzły
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:Utwórz węzły
```

## Krok 5: Wykonaj wytłaczanie liniowe za pomocą skrętu

Wykonaj wytłaczanie liniowe zarówno w lewym, jak i prawym węźle, stosując właściwości skrętu i plasterków.

```java
// ExStart: Wyciągnięcie liniowe ze skrętem
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// Zakończenie: Wyciągnięcie liniowe ze skrętem
```

## Krok 6: Zapisz scenę 3D

Zapisz scenę 3D w formacie pliku Wavefront OBJ.

```java
// ExStart: Zapisz3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
//Rozwiń: Zapisz3DScenę
```

## Wniosek

Gratulacje! Pomyślnie zastosowałeś skręt w wytłaczaniu liniowym przy użyciu Aspose.3D dla Java. Ten samouczek zawiera szczegółowy przewodnik krok po kroku, który pomoże Ci ulepszyć możliwości modelowania 3D.

## Często zadawane pytania

### P1: Czy mogę używać Aspose.3D dla Java do pracy z innymi formatami plików 3D?

Odpowiedź 1: Tak, Aspose.3D obsługuje różne formaty plików 3D, umożliwiając importowanie, eksportowanie i manipulowanie różnymi typami plików.

### P2: Gdzie mogę znaleźć wsparcie dla Aspose.3D dla Java?

 A2: Odwiedź[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) za wsparcie społeczności i dyskusje.

### P3: Czy dostępna jest bezpłatna wersja próbna Aspose.3D dla Java?

 Odpowiedź 3: Tak, możesz uzyskać dostęp do bezpłatnej wersji próbnej z[Tutaj](https://releases.aspose.com/).

### P4: Jak mogę uzyskać tymczasową licencję na Aspose.3D dla Java?

 A4: Zdobądź tymczasową licencję od[strona licencji tymczasowej](https://purchase.aspose.com/temporary-license/).

### P5: Gdzie mogę kupić Aspose.3D dla Java?

 A5: Kup Aspose.3D dla Java w sklepie[strona zakupowa](https://purchase.aspose.com/buy).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
