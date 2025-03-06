---
title: Przekształcaj węzły 3D za pomocą kątów Eulera w Javie przy użyciu Aspose.3D
linktitle: Przekształcaj węzły 3D za pomocą kątów Eulera w Javie przy użyciu Aspose.3D
second_title: Aspose.3D API Java
description: Poznaj świat transformacji 3D w Javie z Aspose.3D. Postępuj zgodnie z naszym przewodnikiem krok po kroku, aby dodać dynamiczne kąty Eulera do węzłów 3D.
weight: 19
url: /pl/java/geometry/transform-3d-nodes-with-euler-angles/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Przekształcaj węzły 3D za pomocą kątów Eulera w Javie przy użyciu Aspose.3D

## Wstęp

Witamy w tym samouczku krok po kroku dotyczącym przekształcania węzłów 3D za pomocą kątów Eulera w Javie przy użyciu Aspose.3D. W tym przewodniku zagłębimy się w proces dodawania transformacji do węzła 3D przy użyciu kątów Eulera w celu uzyskania dynamicznego pozycjonowania i orientacji.

## Warunki wstępne

Zanim przejdziemy do samouczka, upewnij się, że spełniasz następujące wymagania wstępne:

- Podstawowa znajomość programowania w języku Java.
- Zestaw Java Development Kit (JDK) zainstalowany na komputerze.
-  Biblioteka Aspose.3D, z której można uzyskać[Dokumentacja Java Aspose.3D](https://reference.aspose.com/3d/java/).

## Importuj pakiety

 Rozpocznij od zaimportowania niezbędnych pakietów do projektu Java. Upewnij się, że biblioteka Aspose.3D została poprawnie dodana do ścieżki klas. Jeśli jeszcze go nie pobrałeś, możesz znaleźć link do pobrania[Tutaj](https://releases.aspose.com/3d/java/).

```java
import com.aspose.threed.*;
```

## Krok 1. Zainicjuj scenę i węzeł

```java
// ExStart: Dodaj transformację do węzła według kątów Eulera
// Zainicjuj obiekt sceny
Scene scene = new Scene();

// Zainicjuj obiekt klasy Node
Node cubeNode = new Node("cube");
```

## Krok 2. Utwórz siatkę i ustaw geometrię

```java
// Wywołaj klasę Common, aby utworzyć siatkę przy użyciu metody konstruktora wielokątów, aby ustawić instancję siatki
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Wskaż węzeł na geometrię siatki
cubeNode.setEntity(mesh);
```

## Krok 3. Ustaw kąty Eulera i przesunięcie

```java
// Kąty Eulera
cubeNode.getTransform().setEulerAngles(new Vector3(0.3, 0.1, -0.5));

// Ustaw tłumaczenie
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## Krok 4. Dodaj węzeł do sceny

```java
// Dodaj kostkę do sceny
scene.getRootNode().getChildNodes().add(cubeNode);
```

## Krok 5. Zapisz scenę 3D

```java
// Ścieżka do katalogu dokumentów.
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";

// Zapisz scenę 3D w obsługiwanych formatach plików
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByEulerAngles
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

Pamiętaj, aby zastąpić „Twój katalog dokumentów” odpowiednią ścieżką na swoim komputerze.

## Wniosek

Gratulacje! Pomyślnie przekształciłeś węzły 3D przy użyciu kątów Eulera w Javie za pomocą Aspose.3D. Eksperymentuj z różnymi kątami i tłumaczeniami, aby tworzyć dynamiczne i wciągające sceny 3D.

## Często zadawane pytania

### P1: Czy mogę używać Aspose.3D dla Java w projektach komercyjnych?

 A1: Tak, możesz. Odwiedzić[strona zakupu](https://purchase.aspose.com/buy) w celu uzyskania szczegółów licencji.

### P2: Gdzie mogę znaleźć wsparcie dla Aspose.3D?

 A2:[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) to miejsce, w którym można szukać pomocy i nawiązać kontakt ze społecznością.

### P3: Czy dostępny jest bezpłatny okres próbny?

 A3: Tak, możesz eksplorować[bezpłatna wersja próbna](https://releases.aspose.com/) aby doświadczyć możliwości Aspose.3D.

### P4: Jak mogę uzyskać licencję tymczasową?

 A4: Możesz uzyskać licencję tymczasową[Tutaj](https://purchase.aspose.com/temporary-license/).

### P5: Gdzie mogę znaleźć dokumentację?

 A5:[dokumentacja](https://reference.aspose.com/3d/java/) zapewnia kompleksowe wskazówki dotyczące korzystania z Aspose.3D dla Java.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
