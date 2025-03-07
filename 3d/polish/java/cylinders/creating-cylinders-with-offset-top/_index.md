---
title: Tworzenie cylindrów z przesuniętą górą w Aspose.3D dla Java
linktitle: Tworzenie cylindrów z przesuniętą górą w Aspose.3D dla Java
second_title: Aspose.3D API Java
description: Odkryj cuda modelowania 3D w Javie dzięki Aspose.3D. Naucz się bez wysiłku tworzyć urzekające cylindry z przesuniętymi blatami.
weight: 11
url: /pl/java/cylinders/creating-cylinders-with-offset-top/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Tworzenie cylindrów z przesuniętą górą w Aspose.3D dla Java

## Wstęp

dziedzinie modelowania 3D w oparciu o Javę Aspose.3D wyróżnia się jako potężne narzędzie, oferując programistom możliwość łatwego tworzenia skomplikowanych scen 3D. W tym samouczku zagłębimy się w fascynujący świat Aspose.3D dla Java, koncentrując się na konkretnym zadaniu – tworzeniu cylindrów z przesuniętymi wierzchołkami. Pod koniec tego przewodnika będziesz w pełni obeznany z procesem, co umożliwi Ci bezproblemową integrację tej funkcji z projektami 3D.

## Warunki wstępne

Zanim wyruszymy w tę twórczą podróż, upewnij się, że spełniasz następujące wymagania wstępne:

- Zestaw Java Development Kit (JDK): Aspose.3D dla Java wymaga kompatybilnego pakietu JDK zainstalowanego na twoim komputerze.
-  Biblioteka Aspose.3D: Pobierz i zintegruj bibliotekę Aspose.3D ze swoim projektem Java. Można znaleźć bibliotekę i szczegółową dokumentację[Tutaj](https://releases.aspose.com/3d/java/).

## Importuj pakiety

Rozpocznijmy proces od zaimportowania niezbędnych pakietów dla naszego projektu Java. W swoim kodzie umieść następujące informacje:

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Krok 1: Utwórz scenę

Rozpocznij od zainicjowania sceny, w której będziesz aranżować elementy 3D.

```java
// ExStart:1
// Utwórz scenę
Scene scene = new Scene();
// RozwińKoniec:1
```

## Krok 2: Zainicjuj cylinder z przesuniętą górą

Następnie utwórz obiekt cylindryczny z dostosowanym przesuniętym blatem, używając następującego kodu:

```java
// ExStart:2
// Zainicjuj cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Ustaw odsunięcie od góry
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// RozwińKoniec:2
```

## Krok 3: Utwórz węzeł podrzędny

Teraz utwórz węzeł podrzędny na scenie i ustaw tłumaczenie dla pierwszego cylindra:

```java
// ExStart:3
// Utwórz węzeł podrzędny
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// RozwińKoniec:3
```

## Krok 4: Zainicjuj drugi cylinder

Zainicjujmy drugi cylinder bez niestandardowego przesuniętego blatu:

```java
// ExStart:4
// Zainicjuj drugi cylinder bez dostosowanego OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// RozwińKoniec:4
```

## Krok 5: Utwórz węzeł podrzędny dla drugiego cylindra

Utwórz węzeł podrzędny dla drugiego cylindra w scenie:

```java
// ExStart:5
// Utwórz węzeł podrzędny
scene.getRootNode().createChildNode(cylinder2);
// RozwińKoniec:5
```

## Krok 6: Zapisz scenę

Na koniec zapisz scenę z utworzonymi cylindrami jako plik Wavefront OBJ w katalogu dokumentów:

```java
// ExStart:6
//Ratować
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// RozwińKoniec:6
```

Dzięki tym prostym krokom udało Ci się stworzyć cylindry 3D z przesuniętymi wierzchołkami przy użyciu Aspose.3D dla Java!

## Wniosek

Aspose.3D dla Java umożliwia programistom łatwe urzeczywistnianie ich wizji 3D. W tym samouczku skupiliśmy się na tworzeniu cylindrów z przesuniętymi wierzchołkami, prezentując wszechstronność i prostotę Aspose.3D. Teraz, uzbrojony w tę wiedzę, możesz eksplorować i integrować bardziej zaawansowane funkcje ze swoimi projektami 3D opartymi na Javie.

## Często zadawane pytania

### P1: Czy Aspose.3D jest kompatybilny z różnymi środowiskami Java IDE?

O1: Tak, Aspose.3D bezproblemowo integruje się z popularnymi zintegrowanymi środowiskami programistycznymi Java (IDE), takimi jak Eclipse, IntelliJ IDEA i NetBeans.

### P2: Czy mogę zastosować tekstury do utworzonych obiektów 3D?

A2: Absolutnie! Aspose.3D zapewnia szerokie możliwości stosowania tekstur i materiałów w celu zwiększenia atrakcyjności wizualnej modeli 3D.

### P3: Czy dostępne są opcje licencjonowania dla Aspose.3D?

Odpowiedź 3: Tak, możesz sprawdzić i wybrać opcję licencjonowania odpowiadającą Twoim potrzebom[Tutaj](https://purchase.aspose.com/buy).

### P4: Jak mogę szukać pomocy lub podzielić się swoimi doświadczeniami z Aspose.3D?

 A4: Dołącz do forum społeczności Aspose.3D[Tutaj](https://forum.aspose.com/c/3d/18) aby nawiązać kontakt z innymi programistami, szukać wsparcia i dzielić się swoimi spostrzeżeniami.

### P5: Czy istnieje opcja licencji tymczasowej do celów testowych?

 Odpowiedź 5: Tak, możesz uzyskać tymczasową licencję do celów testowania i oceny[Tutaj](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
