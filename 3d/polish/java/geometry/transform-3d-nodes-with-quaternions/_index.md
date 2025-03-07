---
title: Przekształcaj węzły 3D za pomocą kwaternionów w Javie przy użyciu Aspose.3D
linktitle: Przekształcaj węzły 3D za pomocą kwaternionów w Javie przy użyciu Aspose.3D
second_title: Aspose.3D API Java
description: Ulepsz swoje aplikacje Java za pomocą Aspose.3D, aby uzyskać potężne transformacje 3D. Z tego przewodnika krok po kroku dowiesz się, jak przekształcać węzły za pomocą kwaternionów.
weight: 20
url: /pl/java/geometry/transform-3d-nodes-with-quaternions/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Przekształcaj węzły 3D za pomocą kwaternionów w Javie przy użyciu Aspose.3D

## Wstęp

Witamy w tym przewodniku krok po kroku dotyczącym przekształcania węzłów 3D za pomocą kwaternionów w Javie przy użyciu Aspose.3D. Jeśli chcesz ulepszyć swoją aplikację Java za pomocą potężnych transformacji 3D, ten samouczek jest dla Ciebie. Aspose.3D dla Java zapewnia solidny zestaw funkcji do pracy z grafiką 3D, a w tym samouczku skupimy się na przekształcaniu węzłów 3D za pomocą kwaternionów.

## Warunki wstępne

Zanim przejdziemy do samouczka, upewnij się, że spełniasz następujące wymagania wstępne:

- Podstawowa znajomość programowania w języku Java.
- Zainstalowano Aspose.3D dla Java. Możesz go pobrać[Tutaj](https://releases.aspose.com/3d/java/).
- Katalog dokumentów skonfigurowany do zapisywania scen 3D.

## Importuj pakiety

W tej sekcji zaimportujemy niezbędne pakiety, aby rozpocząć transformacje 3D przy użyciu Aspose.3D.

```java
import com.aspose.threed.*;
```

## Krok 1: Zainicjuj obiekt sceny

Na początek utwórz obiekt sceny, który będzie służył jako pojemnik na elementy 3D.

```java
Scene scene = new Scene();
```

## Krok 2: Zainicjuj obiekt klasy węzła

Teraz utwórz obiekt klasy węzła, w tym przypadku reprezentujący sześcian.

```java
Node cubeNode = new Node("cube");
```

## Krok 3: Utwórz siatkę za pomocą narzędzia Polygon Builder

Użyj wspólnej klasy, aby utworzyć siatkę za pomocą metody konstruktora wielokątów.

```java
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Krok 4: Ustaw geometrię siatki

Przypisz utworzoną siatkę do węzła sześcianu.

```java
cubeNode.setEntity(mesh);
```

## Krok 5: Ustaw obrót za pomocą kwaternionu

Zastosuj obrót do węzła sześcianu za pomocą kwaternionów.

```java
cubeNode.getTransform().setRotation(Quaternion.fromRotation(new Vector3(0, 1, 0), new Vector3(0.3, 0.5, 0.1)));
```

## Krok 6: Ustaw tłumaczenie

Określ tłumaczenie węzła kostki.

```java
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## Krok 7: Dodaj kostkę do sceny

Dołącz węzeł sześcianu do sceny.

```java
scene.getRootNode().getChildNodes().add(cubeNode);
```

## Krok 8: Zapisz scenę 3D

Zapisz scenę 3D w obsługiwanym formacie pliku, na przykład FBX7500ASCII.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

## Wniosek

Gratulacje! Pomyślnie nauczyłeś się przekształcać węzły 3D przy użyciu kwaternionów w Javie za pomocą Aspose.3D. Eksperymentuj z różnymi transformacjami, aby ożywić swoje aplikacje 3D.

## Często zadawane pytania

### P1: Czy mogę używać Aspose.3D dla Java za darmo?

O1: Aspose.3D dla Java oferuje bezpłatną wersję próbną. Możesz to znaleźć[Tutaj](https://releases.aspose.com/).

### P2: Gdzie mogę znaleźć dokumentację Aspose.3D dla Java?

 Odpowiedź 2: Dokumentacja jest dostępna[Tutaj](https://reference.aspose.com/3d/java/).

### P3: Jak uzyskać wsparcie dla Aspose.3D dla Java?

 A3: Odwiedź[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) dla wsparcia.

### P4: Czy dostępne są licencje tymczasowe?

 A4: Tak, możesz uzyskać licencję tymczasową[Tutaj](https://purchase.aspose.com/temporary-license/).

### P5: Gdzie mogę kupić Aspose.3D dla Java?

 A5: Możesz to kupić[Tutaj](https://purchase.aspose.com/buy).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
