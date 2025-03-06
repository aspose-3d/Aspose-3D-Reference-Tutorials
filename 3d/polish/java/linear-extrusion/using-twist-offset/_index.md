---
title: Używanie przesunięcia skrętu w wytłaczaniu liniowym z Aspose.3D dla Java
linktitle: Używanie przesunięcia skrętu w wytłaczaniu liniowym z Aspose.3D dla Java
second_title: Aspose.3D API Java
description: Popraw swoje umiejętności modelowania 3D dzięki Aspose.3D dla Java. W tym obszernym samouczku nauczysz się korzystać z przesunięcia skrętu w wytłaczaniu liniowym.

weight: 15
url: /pl/java/linear-extrusion/using-twist-offset/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Używanie przesunięcia skrętu w wytłaczaniu liniowym z Aspose.3D dla Java

## Wstęp

W dynamicznym świecie grafiki 3D opanowanie sztuki wytłaczania liniowego zmienia zasady gry. Dzięki Aspose.3D dla Java możesz podnieść swoje umiejętności modelowania 3D, włączając funkcję Twist Offset do procesu wytłaczania liniowego. Ten samouczek poprowadzi Cię przez etapy wykorzystania przesunięcia skrętu w wytłaczaniu liniowym przy użyciu Aspose.3D dla Java, zapewniając narzędzia do tworzenia wspaniałych scen 3D.

## Warunki wstępne

Zanim przejdziesz do samouczka, upewnij się, że spełniasz następujące wymagania wstępne:

- Środowisko Java: Upewnij się, że w systemie skonfigurowane jest środowisko programistyczne Java.
-  Aspose.3D dla Java: Pobierz i zainstaluj bibliotekę Aspose.3D z[link do pobrania](https://releases.aspose.com/3d/java/).
-  Dokumentacja: Zapoznaj się z[Dokumentacja Aspose.3D dla Java](https://reference.aspose.com/3d/java/).

## Importuj pakiety

W swoim projekcie Java zaimportuj niezbędne pakiety, aby rozpocząć korzystanie z Aspose.3D dla Java. Upewnij się, że dołączono wymagane biblioteki, aby zapewnić bezproblemową integrację.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Krok 1: Skonfiguruj środowisko

Rozpocznij od skonfigurowania środowiska programistycznego Java i upewnienia się, że Aspose.3D for Java jest poprawnie zainstalowany.

## Krok 2: Zainicjuj profil podstawowy

Utwórz profil bazowy do wytłoczenia, w tym przypadku RectangleShape o promieniu zaokrąglenia 0,3.

```java
// Ścieżka do katalogu dokumentów.
String MyDir = "Your Document Directory";
// Zainicjuj profil bazowy, który ma zostać wyciągnięty
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Krok 3: Utwórz scenę 3D

Zbuduj scenę 3D, w której pomieszczą się wytłaczane obiekty.

```java
// Utwórz scenę
Scene scene = new Scene();
```

## Krok 4: Utwórz węzły

Generuj węzły w scenie, aby reprezentować różne elementy.

```java
// Utwórz lewy węzeł
Node left = scene.getRootNode().createChildNode();
// Utwórz prawy węzeł
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Krok 5: Wykonaj wytłaczanie liniowe

Wykorzystaj wytłaczanie liniowe zarówno w lewym, jak i prawym węźle o różnych właściwościach.

```java
// Wykonaj wytłaczanie liniowe na lewym węźle, korzystając z właściwości skrętu i plasterków
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// Wykonaj wytłaczanie liniowe na prawym węźle, używając właściwości skrętu, przesunięcia skrętu i plasterków
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

## Krok 6: Zapisz scenę 3D

Zapisz nowo utworzoną scenę 3D w określonym formacie pliku.

```java
// Zapisz scenę 3D
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Wniosek

Gratulacje! Pomyślnie zaimplementowałeś przesunięcie skrętu w wytłaczaniu liniowym przy użyciu Aspose.3D dla Java. Ta potężna funkcja otwiera świat możliwości w zakresie modelowania 3D, umożliwiając tworzenie skomplikowanych i urzekających scen.

## Często zadawane pytania

### P1: Czy mogę używać Aspose.3D dla Java w projektach niekomercyjnych?

 Odpowiedź 1: Tak, Aspose.3D dla Java może być używany zarówno w projektach komercyjnych, jak i niekomercyjnych. Sprawdź[opcje licencjonowania](https://purchase.aspose.com/buy) po więcej szczegółów.

### P2: Gdzie mogę znaleźć wsparcie dla Aspose.3D dla Java?

 A2: Odwiedź[Forum Aspose.3D dla Java](https://forum.aspose.com/c/3d/18) aby uzyskać pomoc i nawiązać kontakt ze społecznością.

### P3: Czy dostępna jest bezpłatna wersja próbna Aspose.3D dla Java?

 Odpowiedź 3: Tak, możesz skorzystać z bezpłatnej wersji próbnej w witrynie[strona z wydaniami](https://releases.aspose.com/).

### P4: Jak uzyskać tymczasową licencję na Aspose.3D dla Java?

 A4: Uzyskaj tymczasową licencję na swój projekt, odwiedzając stronę[ten link](https://purchase.aspose.com/temporary-license/).

### P5: Czy dostępne są dodatkowe przykłady i samouczki?

 A5: Tak, patrz[dokumentacja](https://reference.aspose.com/3d/java/) aby uzyskać więcej przykładów i szczegółowych samouczków.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
