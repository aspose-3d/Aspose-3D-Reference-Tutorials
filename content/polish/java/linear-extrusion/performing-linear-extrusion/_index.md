---
title: Wykonywanie wytłaczania liniowego w Aspose.3D dla Java
linktitle: Wykonywanie wytłaczania liniowego w Aspose.3D dla Java
second_title: Aspose.3D API Java
description: Poznaj świat modelowania 3D z Aspose.3D dla Java. Naucz się bez wysiłku wykonywać wytłaczanie liniowe.
type: docs
weight: 10
url: /pl/java/linear-extrusion/performing-linear-extrusion/
---
## Wstęp

Witamy w tym kompleksowym samouczku na temat wykonywania wytłaczania liniowego w Aspose.3D dla Java! Jeśli chcesz udoskonalić swoje umiejętności modelowania 3D przy użyciu języka Java, jesteś we właściwym miejscu. W tym samouczku przeprowadzimy Cię przez proces wykonywania wytłaczania liniowego przy użyciu Aspose.3D, potężnej biblioteki Java do modelowania 3D.

## Warunki wstępne

Zanim przejdziesz do samouczka, upewnij się, że spełniasz następujące wymagania wstępne:

1. Środowisko programistyczne Java: Upewnij się, że na komputerze skonfigurowano środowisko programistyczne Java.

2.  Biblioteka Aspose.3D: Pobierz i zainstaluj bibliotekę Aspose.3D. Możesz znaleźć drogę do biblioteki[Tutaj](https://releases.aspose.com/3d/java/).

## Importuj pakiety

Po skonfigurowaniu środowiska programistycznego i zainstalowaniu biblioteki Aspose.3D nadszedł czas na zaimportowanie niezbędnych pakietów. W kodzie Java umieść następujące elementy:

```java
import com.aspose.threed.*;
```

Rozłóżmy każdy krok, aby zapewnić jasne zrozumienie.

## Krok 1: Ustaw katalog dokumentów

Zdefiniuj ścieżkę do katalogu dokumentów:

```java
String MyDir = "Your Document Directory";
```

Dzięki temu wygenerowany model 3D zostanie zapisany w określonym katalogu.

## Krok 2: Zainicjuj kształt podstawowy

Utwórz kształt prostokąta jako profil bazowy do wytłaczania:

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

W razie potrzeby dostosuj promień zaokrąglenia, aby dostosować kształt.

## Krok 3: Wykonaj wytłaczanie liniowe

Wykonaj wytłaczanie liniowe na profilu bazowym:

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

Tutaj wyciągamy kształt o 10 jednostek, ustawiamy liczbę plasterków, umożliwiamy centrowanie i stosujemy przesunięcie skrętu i skrętu.

## Krok 4: Utwórz scenę 3D

Utwórz scenę 3D i dodaj tłoczenie jako węzeł podrzędny:

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

## Krok 5: Zapisz scenę 3D

Zapisz wygenerowaną scenę 3D jako plik Wavefront OBJ:

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Teraz pomyślnie wykonałeś wytłaczanie liniowe przy użyciu Aspose.3D dla Java!

## Wniosek

Gratulacje! Nauczyłeś się, jak wykorzystywać Aspose.3D dla Java do wykonywania wytłaczania liniowego. Ta potężna biblioteka otwiera świat możliwości dla Twoich projektów modelowania 3D.

## Często zadawane pytania

### P1: Czy Aspose.3D jest kompatybilny ze wszystkimi wersjami Java?

O1: Aspose.3D jest zaprojektowany do współpracy z Java 1.6 i nowszymi wersjami.

### P2: Czy mogę używać Aspose.3D w projektach komercyjnych?

Odpowiedź 2: Tak, Aspose.3D może być używany zarówno do projektów osobistych, jak i komercyjnych. Sprawdź szczegóły licencji[Tutaj](https://purchase.aspose.com/buy).

### P3: Jak mogę uzyskać wsparcie dla Aspose.3D?

 A3: Odwiedź[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) uzyskać wsparcie społeczności lub rozważyć zakup a[licencja tymczasowa](https://purchase.aspose.com/temporary-license/) za wsparcie premium.

### P4: Czy w Aspose.3D dostępne są inne funkcje modelowania 3D?

 A4: Absolutnie! Zapoznaj się z obszerną dokumentacją[Tutaj](https://reference.aspose.com/3d/java/) aby uzyskać obszerną listę funkcji i przykładów.

### P5: Czy dostępna jest bezpłatna wersja próbna Aspose.3D?

 Odpowiedź 5: Tak, możesz uzyskać dostęp do bezpłatnego okresu próbnego[Tutaj](https://releases.aspose.com/).