---
title: Dodaj właściwości animacji do scen 3D w Javie | Samouczek Aspose.3D
linktitle: Dodaj właściwości animacji do scen 3D w Javie | Samouczek Aspose.3D
second_title: Aspose.3D API Java
description: Ulepsz swoje projekty 3D oparte na Javie za pomocą Aspose.3D. Postępuj zgodnie z naszym samouczkiem, aby bezproblemowo dodawać właściwości animacji.
type: docs
weight: 10
url: /pl/java/animations/add-animation-properties-to-scenes/
---
## Wstęp

Witamy w tym samouczku krok po kroku dotyczącym dodawania właściwości animacji do scen 3D w Javie przy użyciu Aspose.3D. Jeśli chcesz wzbogacić swoje projekty 3D o dynamiczne animacje, jesteś we właściwym miejscu. W tym przewodniku przeprowadzimy Cię przez ten proces, dzieląc każdy krok, aby zapewnić bezproblemową obsługę.

## Warunki wstępne

Zanim przejdziemy do samouczka, upewnij się, że spełniasz następujące wymagania wstępne:

- Podstawowa znajomość programowania w języku Java.
-  Zainstalowana biblioteka Aspose.3D. Jeśli nie, pobierz go z[strona wydania](https://releases.aspose.com/3d/java/).

## Importuj pakiety

W swoim projekcie Java upewnij się, że zaimportowałeś niezbędne pakiety, aby wykorzystać funkcjonalności Aspose.3D:

```java
import com.aspose.threed.*;

import examples.geometry.Common;
```

Przejdźmy teraz do przewodnika krok po kroku.

## Krok 1: Zainicjuj scenę

```java
// Zainicjuj obiekt sceny
Scene scene = new Scene();
```

## Krok 2: Utwórz siatkę za pomocą narzędzia Polygon Builder

```java
// Wywołaj klasę Common, aby utworzyć siatkę przy użyciu metody konstruktora wielokątów, aby ustawić instancję siatki
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Krok 3: Utwórz węzeł kostki z translacją

```java
// Każdy węzeł sześcianu ma swoje własne tłumaczenie
Node cube1 = scene.getRootNode().createChildNode("cube1", mesh);
```

## Krok 4: Znajdź właściwość tłumaczenia

```java
//Znajdź właściwość tłumaczenia w obiekcie transformacji węzła
Property translation = cube1.getTransform().findProperty("Translation");
```

## Krok 5: Utwórz punkt powiązania

```java
// Utwórz punkt powiązania w oparciu o właściwość tłumaczenia
BindPoint bindPoint = new BindPoint(scene, translation);
```

## Krok 6: Utwórz krzywą animacji

```java
// Utwórz krzywą animacji na składniku X skali
KeyframeSequence kfs = new KeyframeSequence();

// Dodaj klatki kluczowe dla komponentu X
kfs.add(0, 10.0f, Interpolation.BEZIER);
kfs.add(3, 20.0f, Interpolation.BEZIER);
kfs.add(5, 30.0f, Interpolation.LINEAR);

// Powiąż sekwencję klatek kluczowych ze składnikiem X
bindPoint.bindKeyframeSequence("X", kfs);
```

## Krok 7: Powtórz dla komponentu Z

```java
// Powtórz ten proces dla komponentu Z
kfs = new KeyframeSequence();
kfs.add(0, 10.0f, Interpolation.BEZIER);
kfs.add(3, -10.0f, Interpolation.BEZIER);
kfs.add(5, 0.0f, Interpolation.LINEAR);

bindPoint.bindKeyframeSequence("Z", kfs);
```

## Krok 8: Zapisz scenę 3D

```java
// Określ katalog do zapisania sceny 3D
String MyDir = "Your Document Directory";
MyDir = MyDir + "PropertyToDocument.fbx";

// Zapisz scenę 3D w obsługiwanych formatach plików
scene.save(MyDir, FileFormat.FBX7500ASCII);
```

## Wniosek

Gratulacje! Pomyślnie dodałeś właściwości animacji do swojej sceny 3D przy użyciu Aspose.3D w Javie. Eksperymentuj z różnymi parametrami, aby uzyskać pożądane animacje w swoich projektach.

## Często zadawane pytania

### P1: Czy mogę używać Aspose.3D w projektach komercyjnych?

 A1: Tak, możesz. Odwiedzić[strona zakupu](https://purchase.aspose.com/buy) w celu uzyskania szczegółów licencji.

### P2: Czy dostępny jest bezpłatny okres próbny?

 A2: Oczywiście! Chwyć swoje[bezpłatna wersja próbna](https://releases.aspose.com/) przed podjęciem decyzji o zakupie.

### P3: Gdzie mogę znaleźć wsparcie dla Aspose.3D?

A3: Dołącz do społeczności pod adresem[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) do pomocy.

### P4: Jak mogę uzyskać licencję tymczasową?

 A4: Uzyskaj[licencja tymczasowa](https://purchase.aspose.com/temporary-license/) na okres próbny.

### P5: Czy dostępnych jest więcej samouczków?

 A5: Poznaj kompleksowość[dokumentacja](https://reference.aspose.com/3d/java/) na dodatkowe tutoriale.