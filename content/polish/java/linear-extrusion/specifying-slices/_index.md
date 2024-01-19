---
title: Określanie plasterków w wytłaczaniu liniowym za pomocą Aspose.3D dla Java
linktitle: Określanie plasterków w wytłaczaniu liniowym za pomocą Aspose.3D dla Java
second_title: Aspose.3D API Java
description: Naucz się określać plasterki w wyciskaniu liniowym przy użyciu Aspose.3D dla Java. Podnieś swoje umiejętności modelowania 3D dzięki temu przewodnikowi krok po kroku.
type: docs
weight: 13
url: /pl/java/linear-extrusion/specifying-slices/
---
## Wstęp

Tworzenie skomplikowanych modeli 3D często wymaga czegoś więcej niż tylko kreatywności; wymaga to dokładnego zrozumienia narzędzi, którymi dysponujesz. Aspose.3D dla Java zmienia zasady gry pod tym względem. W tym samouczku skupimy się na konkretnym aspekcie - określeniu przekrojów w wyciskaniu liniowym.

## Warunki wstępne

Zanim przejdziesz do samouczka, upewnij się, że spełniasz następujące wymagania wstępne:

1. Środowisko Java: Upewnij się, że w systemie skonfigurowane jest środowisko programistyczne Java.
2.  Aspose.3D dla Java: Pobierz i zainstaluj bibliotekę Aspose.3D. Możesz znaleźć potrzebne pakiety[Tutaj](https://releases.aspose.com/3d/java/).

## Importuj pakiety

W projekcie Java zaimportuj bibliotekę Aspose.3D. Jest to kluczowe dla uzyskania dostępu do funkcjonalności, z którymi będziemy pracować. Dodaj następującą instrukcję importu do swojego kodu:

```java
import com.aspose.threed.*;

import java.io.IOException;
```

Podzielmy teraz przykład na wiele kroków.

## Krok 1: Ustaw scenę

Zainicjuj profil bazowy, który ma zostać wyciągnięty, w tym przypadku a`RectangleShape` z określonym promieniem zaokrąglenia. Utwórz scenę 3D, w której będziesz pracować.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

## Krok 2: Utwórz węzły

Wygeneruj lewy i prawy węzeł w scenie. Dostosuj tłumaczenie lewego węzła pod kątem zmienności przestrzennej.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Krok 3: Wytłaczanie liniowe z plasterkami

Wykonaj wyciskanie liniowe na obu węzłach, określając liczbę wycinków dla każdego. To tutaj dzieje się magia.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

## Krok 4: Zapisz scenę

Zapisz scenę 3D w żądanym formacie, w tym przypadku w pliku Wavefront OBJ.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Wniosek

Gratulacje! Pomyślnie nauczyłeś się określać plasterki w wyciskaniu liniowym przy użyciu Aspose.3D dla Java. Ta umiejętność otwiera nowe możliwości w procesie modelowania 3D.

## Często zadawane pytania

### P1: Jak mogę pobrać Aspose.3D dla Java?

 Odpowiedź 1: Możesz pobrać bibliotekę[Tutaj](https://releases.aspose.com/3d/java/).

### P2: Gdzie mogę znaleźć dokumentację dla Aspose.3D?

 Odpowiedź 2: Zapoznaj się z dokumentacją[Tutaj](https://reference.aspose.com/3d/java/).

### P3: Czy dostępny jest bezpłatny okres próbny?

 Odpowiedź 3: Tak, możesz skorzystać z bezpłatnego okresu próbnego[Tutaj](https://releases.aspose.com/).

### P4: Jak mogę uzyskać wsparcie dla Aspose.3D?

 Odpowiedź 4: Odwiedź forum pomocy technicznej[Tutaj](https://forum.aspose.com/c/3d/18).

### P5: Czy mogę kupić licencję tymczasową?

 Odpowiedź 5: Tak, można uzyskać licencję tymczasową[Tutaj](https://purchase.aspose.com/temporary-license/).