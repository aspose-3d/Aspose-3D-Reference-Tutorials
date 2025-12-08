---
date: 2025-12-08
description: Dowiedz się, jak tworzyć sceny 3D w Javie, stosować realistyczne materiały
  PBR przy użyciu Aspose.3D oraz zapisywać model 3D w formacie STL do renderowania
  obiektów 3D w Javie.
language: pl
linktitle: Create 3D Scene Java – Apply PBR Materials with Aspose.3D
second_title: Aspose.3D Java API
title: 'Utwórz scenę 3D w Javie: zastosuj materiały PBR przy użyciu Aspose.3D'
url: /java/geometry/apply-pbr-materials-to-objects/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Utwórz scenę 3D w Javie – zastosuj materiały PBR z Aspose.3D

## Wprowadzenie

W tym praktycznym samouczku nauczysz się **jak utworzyć scenę 3D w Javie** i wzbogacić ją o materiały Physically Based Rendering (PBR) przy użyciu biblioteki Aspose.3D. Po zakończeniu przewodnika będziesz w stanie renderować realistyczne powierzchnie i **zapisać model 3D w formacie STL** do dalszego wykorzystania w dowolnym pipeline 3D.

## Szybkie odpowiedzi
- **Co oznacza „create 3d scene java”?** Jest to proces tworzenia obiektu Scene, który przechowuje geometrie, światła i kamery w aplikacji Java.  
- **Która biblioteka obsługuje materiały PBR?** Aspose.3D udostępnia gotową klasę `PbrMaterial`.  
- **Czy mogę wyeksportować wynik jako STL?** Tak – metoda `Scene.save` obsługuje STL (ASCII i binarny).  
- **Czy potrzebna jest licencja do produkcji?** Stała licencja Aspose.3D jest wymagana do użytku komercyjnego; licencja tymczasowa działa w testach.  
- **Jakiej wersji Java wymaga się?** Obsługiwane jest dowolne środowisko uruchomieniowe Java 8+.

## Czym jest scena 3D w Javie?

*Scena* to kontener, który przechowuje wszystkie obiekty (węzły), ich geometrie, materiały, światła i kamery. Traktuj ją jak wirtualną scenę, na której umieszczasz swoje modele 3D. Klasa `Scene` z Aspose.3D zapewnia czysty, obiektowo‑zorientowany sposób budowania tej sceny programowo.

## Dlaczego używać materiałów PBR do renderowania obiektów 3D w Javie?

PBR (Physically Based Rendering) naśladuje rzeczywistą interakcję światła, używając parametrów takich jak współczynniki metaliczności i szorstkości. Efektem jest bardziej przekonujący wygląd w różnych warunkach oświetleniowych, co jest szczególnie cenne w wizualizacji produktów, grach lub doświadczeniach AR/VR.

## Wymagania wstępne

1. **Środowisko programistyczne Java** – zainstalowany JDK 8 lub nowszy.  
2. **Biblioteka Aspose.3D** – Pobierz najnowszy plik JAR z [linku do pobrania](https://releases.aspose.com/3d/java/).  
3. **Dokumentacja** – Zapoznaj się z API za pośrednictwem oficjalnej [dokumentacji](https://reference.aspose.com/3d/java/).  
4. **Licencja tymczasowa (opcjonalnie)** – Jeśli nie masz stałej licencji, uzyskaj [licencję tymczasową](https://purchase.aspose.com/temporary-license/) do testów.

## Importowanie pakietów

Dodaj przestrzeń nazw Aspose.3D do swojego pliku źródłowego Java:

```java
import com.aspose.threed.*;
```

## Krok 1: Inicjalizacja sceny

Utwórz scenę, która będzie pełnić rolę płótna dla twojej geometrii i materiałów.

```java
// ExStart:InitializeScene
String MyDir = "Your Document Directory";
Scene scene = new Scene();
// ExEnd:InitializeScene
```

> **Wskazówka:** Upewnij się, że `MyDir` wskazuje na folder z prawami zapisu; w przeciwnym razie wywołanie `save` zakończy się niepowodzeniem.

## Krok 2: Inicjalizacja materiału PBR

Skonfiguruj materiał PBR z wartościami metaliczności i szorstkości, które dają wygląd zbliżony do metalu.

```java
// ExStart:InitializePBRMaterial
PbrMaterial mat = new PbrMaterial();
mat.setMetallicFactor(0.9);
mat.setRoughnessFactor(0.9);
// ExEnd:InitializePBRMaterial
```

> **Dlaczego te wartości?** Wysoki współczynnik metaliczności (≈ 0.9) sprawia, że powierzchnia zachowuje się jak metal, natomiast wysoka szorstkość (≈ 0.9) dodaje subtelną dyfuzję, zapobiegając idealnemu lustrzanemu wykończeniu.

## Krok 3: Utworzenie obiektu 3D i zastosowanie materiału

Tutaj generujemy prostą geometrię pudełka, dołączamy ją do węzła głównego sceny i przypisujemy materiał PBR, który właśnie utworzyliśmy.

```java
// ExStart:Create3DObject
Node boxNode = scene.getRootNode().createChildNode("box", new Box());
boxNode.setMaterial(mat);
// ExEnd:Create3DObject
```

> **Typowy błąd:** Zapomnienie o ustawieniu materiału na węźle spowoduje, że obiekt będzie miał domyślny (nie‑PBR) wygląd.

## Krok 4: Zapis sceny 3D (eksport STL)

Wyeksportuj całą scenę — w tym pudełko wzbogacone o PBR — do pliku STL. STL jest powszechnie obsługiwanym formatem do druku 3‑D i szybkich kontroli wizualnych.

```java
// ExStart:Save3DScene
scene.save(MyDir + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
// ExEnd:Save3DScene
```

Możesz również wybrać `FileFormat.STLBINARY`, jeśli wymagany jest mniejszy rozmiar pliku.

## Typowe problemy i rozwiązania

| Problem | Prawdopodobna przyczyna | Rozwiązanie |
|---------|--------------------------|-------------|
| **Plik nie zapisany** | `MyDir` wskazuje na nieistniejący folder lub brakuje uprawnień do zapisu | Sprawdź, czy katalog istnieje i czy proces Java ma dostęp do zapisu |
| **Materiał wygląda płasko** | Wartości Metallic/Roughness ustawione na 0 | Zwiększ `setMetallicFactor` i/lub `setRoughnessFactor` |
| **Plik STL nie może być otwarty** | Nieprawidłowa flaga formatu pliku (ASCII vs Binary) dla przeglądarki | Użyj odpowiedniego enumu `FileFormat` dla docelowego podglądu |

## Najczęściej zadawane pytania

**P: Czy mogę używać Aspose.3D w projektach komercyjnych?**  
O: Tak. Kup licencję komercyjną na [stronie zakupu](https://purchase.aspose.com/buy).

**P: Jak uzyskać wsparcie dla Aspose.3D?**  
O: Dołącz do społeczności na [forum Aspose.3D](https://forum.aspose.com/c/3d/18) aby uzyskać darmową pomoc, lub otwórz zgłoszenie wsparcia posiadając ważną licencję.

**P: Czy dostępna jest darmowa wersja próbna?**  
O: Oczywiście. Pobierz wersję próbną ze [strony darmowej wersji próbnej](https://releases.aspose.com/).

**P: Gdzie mogę znaleźć szczegółową dokumentację Aspose.3D?**  
O: Wszystkie odniesienia API są dostępne w oficjalnej [dokumentacji](https://reference.aspose.com/3d/java/).

**P: Jak uzyskać tymczasową licencję do testów?**  
O: Zamów ją poprzez [link do licencji tymczasowej](https://purchase.aspose.com/temporary-license/).

## Podsumowanie

Utworzyłeś teraz **scenę 3D w Javie**, zastosowałeś realistyczny materiał PBR i wyeksportowałeś wynik jako plik STL przy użyciu Aspose.3D. Ten przepływ pracy zapewnia solidną podstawę do tworzenia bogatszych wizualizacji, przygotowywania zasobów do druku 3‑D lub wprowadzania modeli do silników gier.

---

**Ostatnia aktualizacja:** 2025-12-08  
**Testowano z:** Aspose.3D 24.12 (latest)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}