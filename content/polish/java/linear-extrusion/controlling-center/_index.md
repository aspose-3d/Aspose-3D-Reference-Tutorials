---
title: Centrum sterowania w wytłaczaniu liniowym z Aspose.3D dla Java
linktitle: Centrum sterowania w wytłaczaniu liniowym z Aspose.3D dla Java
second_title: Aspose.3D API Java
description: Poznaj świat grafiki 3D w Javie dzięki Aspose.3D. Kontroluj środek w wytłaczaniu liniowym bez wysiłku.
type: docs
weight: 11
url: /pl/java/linear-extrusion/controlling-center/
---
## Wstęp

świecie grafiki 3D i programowania w Java, sterowanie środkiem w wyciskaniu liniowym odgrywa kluczową rolę w uzyskaniu pożądanych efektów w Twoich projektach. Aspose.3D dla Java zapewnia potężny zestaw narzędzi do płynnej obsługi takich zadań. W tym samouczku zagłębimy się w proces kontrolowania środka w wytłaczaniu liniowym przy użyciu Aspose.3D dla Java, dzieląc każdy krok, aby zapewnić płynne i wszechstronne zrozumienie.

## Warunki wstępne

Zanim wyruszymy w tę podróż samouczka, upewnij się, że spełniasz następujące wymagania wstępne:

1. Środowisko programistyczne Java: Upewnij się, że na komputerze skonfigurowano środowisko programistyczne Java.

2.  Aspose.3D dla Java: Pobierz i zainstaluj bibliotekę Aspose.3D. Możesz znaleźć bibliotekę i jej dokumentację[Tutaj](https://reference.aspose.com/3d/java/).

3. Katalog dokumentów: Utwórz katalog do przechowywania dokumentów Java. Nazwijmy to „Twoim katalogiem dokumentów”.

## Importuj pakiety

środowisku programistycznym Java zaimportuj niezbędne pakiety dla Aspose.3D. Dzięki temu Twój kod będzie miał dostęp do funkcjonalności udostępnianych przez bibliotekę.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Krok 1: Skonfiguruj profil podstawowy

Zainicjuj profil bazowy, który ma zostać wyciągnięty. W tym przykładzie użyjemy kształtu prostokąta o promieniu zaokrąglenia 0,3.

```java
// Ścieżka do katalogu dokumentów.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Krok 2: Utwórz scenę 3D

Zbuduj fundament swojego świata 3D, tworząc scenę.

```java
Scene scene = new Scene();
```

## Krok 3: Utwórz lewy i prawy węzeł

Utwórz lewy i prawy węzeł w swojej scenie. Węzły te służą jako płótno dla obiektów 3D.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Krok 4: Wytłaczanie liniowe z właściwością środkową

Wykonaj wytłaczanie liniowe na lewym węźle bez centrowania i ustaw liczbę plasterków na 3.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## Krok 5: Ustaw płaszczyznę podłoża jako odniesienie

Popraw reprezentację wizualną, dodając płaszczyznę podstawy do lewego węzła.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## Krok 6: Wyciągnięcie liniowe z właściwością środka (prawy węzeł)

Wykonaj wytłaczanie liniowe na prawym węźle, tym razem centrując wytłaczanie i ponownie ustaw liczbę plasterków na 3.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## Krok 7: Ustaw płaszczyznę podłoża jako odniesienie (prawy węzeł)

Podobnie jak w przypadku lewego węzła, dodaj płaszczyznę podłoża do prawego węzła w celach informacyjnych.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## Krok 8: Zapisz scenę 3D

Zapisz swoją scenę 3D w formacie Wavefront OBJ.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Wniosek

Sterowanie środkiem w wytłaczaniu liniowym za pomocą Aspose.3D dla Java otwiera ekscytujące możliwości w rozwoju grafiki 3D. Postępując zgodnie z tym przewodnikiem krok po kroku, nauczyłeś się manipulować właściwością center, co pozwala uzyskać pożądane efekty wizualne w projektach Java.

## Często zadawane pytania

### P1: Czy mogę używać Aspose.3D dla Java w projektach komercyjnych?

 O1: Tak, Aspose.3D dla Java jest dostępny do użytku komercyjnego. Aby uzyskać szczegółowe informacje na temat licencji, odwiedź stronę[Tutaj](https://purchase.aspose.com/buy).

### P2: Czy dostępny jest bezpłatny okres próbny?

 Odpowiedź 2: Tak, możesz skorzystać z bezpłatnej wersji próbnej Aspose.3D dla Java[Tutaj](https://releases.aspose.com/).

### P3: Gdzie mogę znaleźć wsparcie dla Aspose.3D dla Java?

 Odpowiedź 3: Forum społeczności Aspose.3D jest doskonałym miejscem do szukania wsparcia i dzielenia się swoimi doświadczeniami. Odwiedź forum[Tutaj](https://forum.aspose.com/c/3d/18).

### P4: Czy potrzebuję tymczasowej licencji do testowania?

Odpowiedź 4: Tak, jeśli potrzebujesz tymczasowej licencji do celów testowych, możesz ją uzyskać[Tutaj](https://purchase.aspose.com/temporary-license/).

### P5: Gdzie mogę znaleźć dokumentację?

 O5: Dostępna jest dokumentacja Aspose.3D dla Java[Tutaj](https://reference.aspose.com/3d/java/).