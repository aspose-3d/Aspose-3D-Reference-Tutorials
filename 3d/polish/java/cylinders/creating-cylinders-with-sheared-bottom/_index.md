---
title: Tworzenie cylindrów ze ściętym dnem w Aspose.3D dla Java
linktitle: Tworzenie cylindrów ze ściętym dnem w Aspose.3D dla Java
second_title: Aspose.3D API Java
description: Naucz się tworzyć niestandardowe cylindry ze ściętymi spodami przy użyciu Aspose.3D dla Java. Podnieś swoje umiejętności modelowania 3D dzięki temu przewodnikowi krok po kroku.
type: docs
weight: 12
url: /pl/java/cylinders/creating-cylinders-with-sheared-bottom/
---
## Wstęp

Witamy w tym przewodniku krok po kroku dotyczącym tworzenia cylindrów ze ściętymi dnami przy użyciu Aspose.3D dla Java. Aspose.3D to potężna biblioteka Java, która umożliwia bezproblemową pracę z plikami 3D. W tym samouczku zagłębimy się w tworzenie niestandardowych cylindrów ze ściętymi spodami, zapewniając praktyczne doświadczenie w używaniu Aspose.3D w celu udoskonalenia umiejętności modelowania 3D.

## Warunki wstępne

Zanim zaczniemy, upewnij się, że spełnione są następujące wymagania wstępne:
- Zestaw Java Development Kit (JDK) zainstalowany w systemie.
-  Biblioteka Aspose.3D for Java pobrana i dodana do Twojego projektu. Możesz znaleźć link do pobrania[Tutaj](https://releases.aspose.com/3d/java/).

## Importuj pakiety

Aby rozpocząć, zaimportuj pakiety niezbędne do pracy z Aspose.3D w swojej aplikacji Java:
```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Krok 1: Utwórz scenę

Rozpocznij od stworzenia sceny 3D, w której będziesz dodawać cylindry i manipulować nimi:
```java
// ExStart:3
// Utwórz scenę
Scene scene = new Scene();
// RozwińKoniec:3
```

## Krok 2: Utwórz cylinder 1

Teraz utwórzmy pierwszy walec ze ściętym dnem:
```java
// ExStart:4
// Utwórz cylinder 1
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Dostosowane dno ścinane dla cylindra 1
cylinder1.setShearBottom(new Vector2(0, 0.83)); //Ścinanie 47,5 stopnia w płaszczyźnie xy (oś z)
// Dodaj cylinder 1 do sceny
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// RozwińKoniec:4
```

## Krok 3: Utwórz cylinder 2

Następnie dodajmy do sceny drugi cylinder bez ściętego dna:
```java
// ExStart:5
// Utwórz cylinder 2
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// Dodaj do sceny cylinder 2 bez ShearBottom
scene.getRootNode().createChildNode(cylinder2);
// RozwińKoniec:5
```

## Krok 4: Zapisz scenę

Zapisz scenę z dostosowanymi cylindrami w katalogu dokumentów:
```java
// ExStart:6
// Zapisz scenę
scene.save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WAVEFRONTOBJ);
// RozwińKoniec:6
```

Gratulacje! Pomyślnie utworzyłeś cylindry ze ściętymi dnami przy użyciu Aspose.3D dla Java.

## Wniosek

W tym samouczku omówiliśmy, jak wykorzystać Aspose.3D dla Java do ulepszenia projektów modelowania 3D. Tworzenie niestandardowych cylindrów ze ściętymi spodami dodaje niepowtarzalny akcent Twoim projektom, a Aspose.3D upraszcza ten proces.

## Często zadawane pytania

### P1: Czy mogę używać Aspose.3D dla Java z innymi bibliotekami Java 3D?

O1: Aspose.3D dla Java został zaprojektowany do niezależnej pracy. Chociaż można go zintegrować z innymi bibliotekami, jest on wystarczająco wydajny, aby samodzielnie obsługiwać większość zadań związanych z modelowaniem 3D.

### P2: Czy Aspose.3D jest odpowiedni dla początkujących w modelowaniu 3D?

Odpowiedź 2: Tak, Aspose.3D zapewnia przyjazne dla użytkownika API, dzięki czemu jest odpowiednie zarówno dla początkujących, jak i doświadczonych programistów w modelowaniu 3D.

### P3: Gdzie mogę znaleźć dodatkowe wsparcie dla Aspose.3D dla Java?

 A3: Odwiedź[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) za wsparcie społeczności i dyskusje.

### P4: Jak mogę uzyskać tymczasową licencję na Aspose.3D?

 A4: Możesz uzyskać licencję tymczasową[Tutaj](https://purchase.aspose.com/temporary-license/).

### P5: Czy mogę kupić Aspose.3D dla Java?

 Odpowiedź 5: Tak, możesz kupić Aspose.3D dla Java[Tutaj](https://purchase.aspose.com/buy).