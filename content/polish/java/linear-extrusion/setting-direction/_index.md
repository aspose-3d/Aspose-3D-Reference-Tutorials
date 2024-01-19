---
title: Ustawianie kierunku w wytłaczaniu liniowym za pomocą Aspose.3D dla Java
linktitle: Ustawianie kierunku w wytłaczaniu liniowym za pomocą Aspose.3D dla Java
second_title: Aspose.3D API Java
description: Opanuj wytłaczanie liniowe z Aspose.3D dla Java! Postępuj zgodnie z naszym przewodnikiem, aby uzyskać płynne programowanie 3D. Pobierz teraz i ciesz się wciągającymi wrażeniami.
type: docs
weight: 12
url: /pl/java/linear-extrusion/setting-direction/
---
## Wstęp

Witamy w naszym przewodniku krok po kroku dotyczącym ustawiania kierunku wytłaczania liniowego przy użyciu Aspose.3D dla Java. Aspose.3D to potężna biblioteka Java, która umożliwia programistom bezproblemową pracę z plikami i scenami 3D. W tym samouczku skupimy się na konkretnym zadaniu, jakim jest ustawienie kierunku wytłaczania liniowego, zwiększając Twoją biegłość w programowaniu 3D.

## Warunki wstępne

Zanim przejdziemy do samouczka, upewnij się, że spełniasz następujące wymagania wstępne:

- Podstawowa znajomość języka programowania Java.
-  Zainstalowana biblioteka Aspose.3D. Można go pobrać z[Tutaj](https://releases.aspose.com/3d/java/).
- Zintegrowane środowisko programistyczne (IDE) dla języka Java, takie jak Eclipse lub IntelliJ.

## Importuj pakiety

Upewnij się, że zaimportowałeś niezbędne pakiety, aby rozpocząć projekt:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Krok 1: Zainicjuj profil podstawowy

 Rozpocznij od zainicjowania profilu bazowego, który ma zostać wyciągnięty. W tym przykładzie używamy a`RectangleShape` z promieniem zaokrąglenia 0,3:

```java
// Ścieżka do katalogu dokumentów.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Krok 2: Utwórz scenę

Następnie utwórz scenę 3D zawierającą wyciągnięte obiekty:

```java
Scene scene = new Scene();
```

## Krok 3: Utwórz węzły

Utwórz lewy i prawy węzeł w scenie:

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Krok 4: Wykonaj wytłaczanie liniowe na lewym węźle

 Wykonaj wytłaczanie liniowe w lewym węźle za pomocą`LinearExtrusion`klasa z określonymi parametrami, takimi jak skręt i plasterki:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Krok 5: Wykonaj wytłaczanie liniowe na prawym węźle z kierunkiem

 Wykonaj wytłaczanie liniowe na prawym węźle, wprowadzając`setDirection` właściwość określająca kierunek wytłoczenia:

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Krok 6: Zapisz scenę 3D

Zapisz scenę 3D w żądanym formacie pliku. W tym przykładzie zapisujemy go jako plik Wavefront OBJ:

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Wniosek

Gratulacje! Pomyślnie nauczyłeś się wyznaczać kierunek w wyciskaniu liniowym przy użyciu Aspose.3D dla Java. Ten samouczek rozwinie Twoje umiejętności programowania 3D i otworzy nowe możliwości dla kreatywnych projektów.

## Często zadawane pytania

### P1: Czy mogę używać Aspose.3D z innymi językami programowania?

O1: Aspose.3D obsługuje różne języki programowania, w tym .NET i Java.

### Pytanie 2. Czy dostępna jest bezpłatna wersja próbna Aspose.3D?

 Odpowiedź 2: Tak, możesz poznać funkcje Aspose.3D w ramach bezpłatnej wersji próbnej[Tutaj](https://releases.aspose.com/).

### P3: Gdzie mogę znaleźć szczegółową dokumentację Aspose.3D dla Java?

 A3: Dostępna jest obszerna dokumentacja[Tutaj](https://reference.aspose.com/3d/java/).

### P4: Jak mogę uzyskać wsparcie dla Aspose.3D?

 A4: Odwiedź[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) celu uzyskania pomocy lub pytań.

### P5: Czy dostępne są tymczasowe licencje dla Aspose.3D?

 Odpowiedź 5: Tak, możesz uzyskać licencję tymczasową[Tutaj](https://purchase.aspose.com/temporary-license/).