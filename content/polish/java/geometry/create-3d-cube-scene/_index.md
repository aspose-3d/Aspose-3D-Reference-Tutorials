---
title: Utwórz scenę kostki 3D w Javie za pomocą Aspose.3D
linktitle: Utwórz scenę kostki 3D w Javie za pomocą Aspose.3D
second_title: Aspose.3D API Java
description: Odkryj cuda grafiki scen sześcianów 3D dzięki Aspose.3D dla Java. Twórz wspaniałe sceny bez wysiłku.
type: docs
weight: 12
url: /pl/java/geometry/create-3d-cube-scene/
---
## Wstęp

Witamy w fascynującym świecie grafiki 3D w Javie przy użyciu Aspose.3D! W tym samouczku przeprowadzimy Cię przez proces tworzenia oszałamiającej sceny kostki 3D przy użyciu Aspose.3D dla Java. Aspose.3D to potężna biblioteka Java, która zapewnia wszechstronne funkcje do pracy z modelami i scenami 3D.

## Warunki wstępne

Zanim zajmiemy się tworzeniem sceny kostki 3D, upewnij się, że spełnione są następujące wymagania wstępne:

1.  Zestaw Java Development Kit (JDK): Upewnij się, że w systemie jest zainstalowana Java. Najnowszą wersję możesz pobrać ze strony[stronie internetowej Oracle](https://www.oracle.com/java/).

2.  Aspose.3D dla biblioteki Java: Pobierz i zainstaluj bibliotekę Aspose.3D. Możesz znaleźć link do pobrania[Tutaj](https://releases.aspose.com/3d/java/).

## Importuj pakiety

Rozpocznij od zaimportowania niezbędnych pakietów do projektu Java:

```java
import java.io.File;

import com.aspose.threed.Box;
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Mesh;
import com.aspose.threed.Node;
import com.aspose.threed.Scene;
```

Podzielmy teraz proces tworzenia sceny kostki 3D na wiele etapów.

## Krok 1: Zainicjuj scenę

```java
// Zainicjuj obiekt sceny
Scene scene = new Scene();
```

## Krok 2: Zainicjuj węzeł i siatkę

```java
// Zainicjuj obiekt klasy Node
Node cubeNode = new Node("box");

// Wywołaj klasę Common, aby utworzyć siatkę przy użyciu metody konstruktora wielokątów, aby ustawić instancję siatki
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Wskaż węzeł na geometrię siatki
cubeNode.setEntity(mesh);
```

## Krok 3: Dodaj węzeł do sceny

```java
// Dodaj węzeł do sceny
scene.getRootNode().getChildNodes().add(cubeNode);
```

## Krok 4: Zapisz scenę 3D

```java
// Ścieżka do katalogu dokumentów.
String MyDir = "Your Document Directory";
MyDir = MyDir + "CubeScene.fbx";

//Zapisz scenę 3D w obsługiwanych formatach plików
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Krok 5: Wydrukuj wiadomość o powodzeniu

```java
System.out.println("\nCube Scene created successfully.\nFile saved at " + MyDir);
```

## Wniosek

Gratulacje! Pomyślnie utworzyłeś scenę kostki 3D przy użyciu Aspose.3D dla Java. Ten samouczek zapewnia solidną podstawę do odkrywania bardziej zaawansowanych funkcji i uwalniania kreatywności w świecie grafiki 3D.

## Często zadawane pytania

### P1: Czy mogę używać Aspose.3D w projektach komercyjnych?

 A1: Tak, możesz. Sprawdź[strona zakupu](https://purchase.aspose.com/buy) w celu uzyskania szczegółów licencji.

### P2: Jak mogę uzyskać wsparcie dla Aspose.3D?

 A2: Odwiedź[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) za wsparcie społeczne.

### P3: Czy dostępny jest bezpłatny okres próbny?

 A3: Tak, możesz uzyskać bezpłatną wersję próbną[Tutaj](https://releases.aspose.com/).

### P4: Gdzie mogę znaleźć dokumentację dla Aspose.3D?

 A4: Patrz[Dokumentacja Aspose.3D](https://reference.aspose.com/3d/java/) aby uzyskać szczegółowe informacje.

### P5: Jak uzyskać tymczasową licencję na Aspose.3D?

 Odpowiedź 5: Możesz uzyskać licencję tymczasową[Tutaj](https://purchase.aspose.com/temporary-license/).