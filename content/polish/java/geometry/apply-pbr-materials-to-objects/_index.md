---
title: Zastosuj materiały PBR do obiektów 3D w Javie za pomocą Aspose.3D
linktitle: Zastosuj materiały PBR do obiektów 3D w Javie za pomocą Aspose.3D
second_title: Aspose.3D API Java
description: Naucz się stosować realistyczne materiały PBR do obiektów 3D w Javie przy użyciu Aspose.3D. Popraw jakość wizualną dzięki renderowaniu opartemu na fizyce.
type: docs
weight: 10
url: /pl/java/geometry/apply-pbr-materials-to-objects/
---
## Wstęp

Witamy w tym przewodniku krok po kroku dotyczącym stosowania materiałów renderowania opartego na fizyce (PBR) do obiektów 3D w Javie przy użyciu Aspose.3D. Aspose.3D to potężna biblioteka Java, która zapewnia wszechstronną funkcjonalność do pracy z modelami i scenami 3D. W tym samouczku skupimy się na zastosowaniu materiałów PBR, które symulują rzeczywiste oświetlenie i właściwości powierzchni, zwiększając realizm obiektów 3D.

## Warunki wstępne

Zanim przejdziemy do samouczka, upewnij się, że spełniasz następujące wymagania wstępne:

1. Środowisko programistyczne Java: Upewnij się, że masz zainstalowaną Javę w swoim systemie.

2.  Biblioteka Aspose.3D: Pobierz i zainstaluj bibliotekę Aspose.3D z[link do pobrania](https://releases.aspose.com/3d/java/).

3.  Dokumentacja: Patrz[dokumentacja](https://reference.aspose.com/3d/java/) dla Aspose.3D, aby zapoznać się z funkcjami biblioteki.

4.  Licencja tymczasowa (opcjonalnie): Jeśli nie masz licencji, możesz uzyskać[licencja tymczasowa](https://purchase.aspose.com/temporary-license/) dla testów.

## Importuj pakiety

swoim projekcie Java dołącz pakiety niezbędne do korzystania z Aspose.3D. Dodaj następujące instrukcje importu do swojego kodu:

```java
import com.aspose.threed.*;
```

## Krok 1: Zainicjuj scenę

Zacznij od stworzenia sceny 3D za pomocą Aspose.3D. Scena służy jako płótno dla obiektów 3D.

```java
// ExStart: Zainicjuj scenę
String MyDir = "Your Document Directory";
Scene scene = new Scene();
// ExEnd:InitializeScene
```

## Krok 2: Zainicjuj materiał PBR

Utwórz materiał PBR i dostosuj jego właściwości, takie jak współczynniki metaliczne i chropowatość.

```java
// ExStart: Zainicjuj materiał PBR
PbrMaterial mat = new PbrMaterial();
mat.setMetallicFactor(0.9);
mat.setRoughnessFactor(0.9);
// ExEnd:InitializePBRMaterial
```

## Krok 3: Utwórz obiekt 3D

Wygeneruj obiekt 3D (np. pudełko), na który zostanie nałożony materiał PBR.

```java
// ExStart: Utwórz obiekt 3D
Node boxNode = scene.getRootNode().createChildNode("box", new Box());
boxNode.setMaterial(mat);
// Rozwiń: Utwórz obiekt 3D
```

## Krok 4: Zapisz scenę 3D

Zapisz scenę 3D, łącznie z zastosowanym materiałem PBR, w określonym formacie pliku, np. STL.

```java
// ExStart: Zapisz3DScene
scene.save(MyDir + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
// Rozwiń: Zapisz3DScenę
```

Powtórz te kroki dla bardziej złożonych scen lub różnych obiektów.

## Wniosek

Gratulacje! Pomyślnie zastosowałeś materiały PBR do obiektu 3D w Javie przy użyciu Aspose.3D. Zwiększa to atrakcyjność wizualną modeli 3D, czyniąc je bardziej realistycznymi i oszałamiającymi wizualnie.

## Często zadawane pytania

### P1: Czy mogę używać Aspose.3D w projektach komercyjnych?

 A1: Tak, możesz. Odwiedzić[strona zakupu](https://purchase.aspose.com/buy) w celu uzyskania szczegółów licencji.

### P2: Jak uzyskać wsparcie dla Aspose.3D?

 A2: Dołącz do[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) za wsparcie i pomoc społeczną.

### P3: Czy dostępny jest bezpłatny okres próbny?

 A3: Tak, możesz odkryć a[bezpłatna wersja próbna](https://releases.aspose.com/) przed dokonaniem zakupu.

### P4: Gdzie mogę znaleźć szczegółową dokumentację dla Aspose.3D?

 A4: Patrz[dokumentacja](https://reference.aspose.com/3d/java/) w celu uzyskania kompleksowych wskazówek.

### P5: Jak uzyskać tymczasową licencję na testowanie?

 A5: Odwiedź[ten link](https://purchase.aspose.com/temporary-license/) aby uzyskać licencję tymczasową.