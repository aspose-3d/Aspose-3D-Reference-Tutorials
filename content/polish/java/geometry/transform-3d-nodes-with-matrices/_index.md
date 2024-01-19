---
title: Przekształcaj węzły 3D za pomocą macierzy transformacji przy użyciu Aspose.3D
linktitle: Przekształcaj węzły 3D za pomocą macierzy transformacji w Javie przy użyciu Aspose.3D
second_title: Aspose.3D API Java
description: Poznaj świat grafiki 3D w Javie dzięki Aspose.3D. Naucz się bez wysiłku przekształcać węzły za pomocą macierzy transformacji.
type: docs
weight: 21
url: /pl/java/geometry/transform-3d-nodes-with-matrices/
---
## Wstęp

Witamy w tym przewodniku krok po kroku dotyczącym przekształcania węzłów 3D za pomocą macierzy transformacji w Javie przy użyciu Aspose.3D. Jeśli jesteś programistą Java i chcesz udoskonalić swoje umiejętności w zakresie grafiki 3D i modelowania, jesteś we właściwym miejscu. W tym samouczku zagłębimy się w proces stosowania transformacji do węzłów 3D w środowisku Aspose.3D.

## Warunki wstępne

Zanim zaczniemy, upewnij się, że spełniasz następujące wymagania wstępne:

- Podstawowa znajomość programowania w języku Java.
-  Zainstalowana biblioteka Aspose.3D. Można go pobrać z[Tutaj](https://releases.aspose.com/3d/java/).
- Działające zintegrowane środowisko programistyczne (IDE) do programowania w języku Java.

## Importuj pakiety

W swoim projekcie Java zaimportuj niezbędne pakiety z Aspose.3D. Upewnij się, że Twój projekt jest poprawnie skonfigurowany do korzystania z biblioteki Aspose.3D. Oto przykładowa instrukcja importu:

```java
import com.aspose.threed.*;

```

## Przekształcanie węzłów 3D

### Krok 1: Zainicjuj obiekt sceny

Rozpocznij od zainicjowania obiektu sceny, który służy jako pojemnik na elementy 3D.

```java
Scene scene = new Scene();
```

### Krok 2: Zainicjuj obiekt klasy węzła

Utwórz obiekt klasy Node, taki jak kostka, który zostanie poddany transformacji.

```java
Node cubeNode = new Node("cube");
```

### Krok 3: Utwórz siatkę za pomocą narzędzia Polygon Builder

Użyj klasy Common, aby utworzyć siatkę za pomocą metody konstruktora wielokątów. Spowoduje to ustawienie instancji siatki dla sześcianu.

```java
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

### Krok 4: Wskaż węzeł na geometrię siatki

Przypisz utworzoną siatkę do węzła sześcianu.

```java
cubeNode.setEntity(mesh);
```

### Krok 5: Ustaw niestandardową macierz tłumaczeń

Zastosuj niestandardową macierz translacji do węzła kostki. W tym przykładzie ustawiana jest macierz transformacji do translacji.

```java
cubeNode.getTransform().setTransformMatrix(new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
));
```

### Krok 6: Dodaj kostkę do sceny

Dołącz węzeł kostki do węzła głównego sceny.

```java
scene.getRootNode().addChildNode(cubeNode);
```

### Krok 7: Zapisz scenę 3D

Określ katalog i nazwę pliku do zapisania sceny 3D w obsługiwanych formatach plików, takich jak FBX.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

## Wniosek

Gratulacje! Pomyślnie nauczyłeś się przekształcać węzły 3D przy użyciu Aspose.3D w Javie. Eksperymentuj z różnymi matrycami i odkrywaj nieskończone możliwości grafiki 3D.

## Często zadawane pytania

### P1: Czy mogę zastosować wiele transformacji do pojedynczego węzła 3D?

O1: Tak, możesz łączyć wiele macierzy transformacji w celu uzyskania złożonych transformacji.

### P2: Jak mogę obrócić obiekt 3D w Aspose.3D?

A2: Użyj odpowiedniej macierzy rotacji w macierzy transformacji dla pożądanej rotacji.

### P3: Czy istnieje ograniczenie rozmiaru scen 3D, które mogę utworzyć?

O3: Rozmiar scen 3D może być ograniczony przez zasoby systemowe, ale Aspose.3D został zaprojektowany pod kątem wydajności.

### P4: Gdzie mogę znaleźć dodatkowe przykłady i dokumentację?

 A4: Odwiedź[Dokumentacja Aspose.3D](https://reference.aspose.com/3d/java/) aby uzyskać więcej przykładów i szczegółów.

### P5: Jak uzyskać tymczasową licencję na Aspose.3D?

 Odpowiedź 5: Możesz uzyskać licencję tymczasową[Tutaj](https://purchase.aspose.com/temporary-license/).