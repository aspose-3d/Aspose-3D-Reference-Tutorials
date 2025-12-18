---
date: 2025-12-18
description: Dowiedz się, jak wyciągać kształt w Javie przy użyciu Aspose.3D, tworzyć
  scenę 3D i łatwo eksportować pliki Wavefront OBJ.
linktitle: How to Extrude Shape in Java with Aspose.3D Linear Extrusion
second_title: Aspose.3D Java API
title: Jak wyciągnąć kształt w Javie przy użyciu Aspose.3D – ekstruzja liniowa
url: /pl/java/linear-extrusion/performing-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Wykonywanie liniowej ekstruzji w Aspose.3D dla Javy

## Introduction

Witamy w tym kompleksowym samouczku dotyczącym **how to extrude shape** w Aspose.3D dla Javy! Jeśli chcesz rozwinąć swoje umiejętności modelowania 3D przy użyciu Javy, jesteś we właściwym miejscu. Przeprowadzimy Cię przez tworzenie sceny 3D, wykonywanie liniowej ekstruzji i eksportowanie wyniku jako plik Wavefront OBJ — wszystko z jasnymi, krok po kroku przykładami kodu.

## Quick Answers
- **What is linear extrusion?** Rozciąganie profilu 2D wzdłuż prostej ścieżki w celu utworzenia bryły 3D.  
- **Which library handles this in Java?** Aspose.3D for Java.  
- **Can I export to OBJ?** Tak, przy użyciu funkcji eksportu Wavefront OBJ.  
- **Do I need a license for development?** Darmowa wersja próbna działa do testów; licencja jest wymagana w produkcji.  
- **What Java version is required?** Java 1.6 lub nowsza.

## What is “how to extrude shape”?

Liniowa ekstruzja jest podstawową techniką w **3d modeling java**, która przekształca płaski profil — na przykład prostokąt — w obiekt objętościowy poprzez przeciągnięcie go na określoną odległość. Metoda ta jest szeroko stosowana do tworzenia części mechanicznych, elementów architektonicznych i modeli dekoracyjnych.

## Why use Aspose.3D for linear extrusion?
- ** control** nad geometrią (przycięcia, skręt, offset).  
- **Seamless integration** z projektami Java — bez zależności natywnych.  
- **Built‑in exporters** dla popularnych formatów, w tym Wavefront OBJ, co ułatwia **generate 3d model** pliki dla dalszych procesów.

## Prerequisites

Zanim zanurzysz się w samouczek, upewnij się, że masz następujące wymagania:

1. **Java Development Environment** – JDK (1.6 lub nowszy) oraz ulubione IDE.  
2. **Aspose.3D Library** – pobierz i zainstaluj bibliotekę ze strony oficjalnej **[here](https://releases.aspose.com/3d/java/)**.

## Importowanie pakietów

Po skonfigurowaniu środowiska programistycznego i zainstalowaniu biblioteki Aspose.3D, zaimportuj niezbędny pakiet:

```java
import com.aspose.threed.*;
```

### Krok 1: Ustaw katalog dokumentu

Zdefiniuj folder, w którym będą zapisywane wygenerowane pliki:

```java
String MyDir = "Your Document Directory";
```

> To zapewnia, że operacja **generate 3d model** zapisuje plik OBJ w znanej lokalizacji.

### Krok 2: Zainicjuj podstawowy kształt

Utwórz prostokąt, który będzie służył jako profil ekstruzji:

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### Krok 3: Wykonaj liniową ekstruzję

Teraz ekstruzujemy prostokąt wzdłuż osi Z, dodajemy przycięcia, włączamy centrowanie i stosujemy skręt z przesunięciem:

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

- **Extrusion length** – `10` jednostek.  
- **Slices** – `100` dla gładkiej geometrii.  
- **Twist** – `360°` tworzy pełny obrót.  
- **Twist offset** – przesuwa początek skrętu do `(10, 0, 0)`.

### Krok 4: Utwórz scenę 3D

Utwórz kontener sceny i dodaj ekstruzję jako węzeł potomny. Ten krok **creates 3d scene** może pomieścić wiele obiektów:

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

### Krok 5: Zapisz scenę 3D

Wyeksportuj scenę do pliku Wavefront OBJ. To demonstruje możliwości **wavefront obj export** i **save 3d obj**:

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Po uruchomieniu kodu znajdziesz `LinearExtrusion.obj` w określonym katalogu, gotowy do otwarcia w dowolnym przeglądarce 3D lub dalszego przetwarzania.

## Typowe problemy i rozwiązania

| Problem | Przyczyna | Rozwiązanie |
|---------|-----------|-------------|
| Plik OBJ jest pusty | Ścieżka katalogu wyjściowego jest niepoprawna lub nie ma uprawnień do zapisu | Sprawdź, czy `MyDir` wskazuje istniejący folder z uprawnieniami do zapisu. |
| Skręt nie został zastosowany | pominięto `setCenter(true)` | Upewnij się, że centrowanie jest włączone lub dostosuj wartości `setTwistOffset`. |
| Błąd kompilacji przy `LinearExtrusion` | Używanie starszej wersji Aspose.3D | Zaktualizuj do najnowszej wersji Aspose.3D. |

## Najczęściej zadawane pytania

**Q: Czy Aspose.3D jest kompatybilny ze wszystkimi wersjami Javy?**  
A: Aspose.3D działa z Java 1.6 i nowszymi.

**Q: Czy mogę używać Aspose.3D w projektach komercyjnych?**  
A: Tak, użycie komercyjne jest dozwolone przy ważnej licencji. Możesz ją uzyskać **[here](https://purchase.aspose.com/buy)**.

**Q: Gdzie mogę uzyskać wsparcie, jeśli napotkam problemy?**  
A: Odwiedź **[Aspose.3D forum](https://forum.aspose.com/c/3d/18)**, aby uzyskać pomoc społeczności lub zakup **[temporary license](https://purchase.aspose.com/temporary-license/)** dla wsparcia premium.

**Q: Jakie inne funkcje modelowania 3D oferuje Aspose.3D?**  
A: Biblioteka zawiera manipulację siatką, operacje boolowskie, mapowanie tekstur i wiele innych. Zobacz pełną listę **[here](https://reference.aspose.com/3d/java/)**.

**Q: Czy dostępna jest darmowa wersja próbna?**  
A: Tak, możesz pobrać wersję próbną **[here](https://releases.aspose.com/)**.

## Zakończenie

Teraz wiesz, jak **how to extrude shape** przy użyciu Aspose.3D dla Javy, stworzyłeś scenę 3D i wyeksportowałeś wynik jako plik Wavefront OBJ. Ta technika otwiera drzwi do szerokiego zakresu projektów **3d modeling java** — od prostych części po złożone zespoły. Zbadaj dodatkowe funkcje, takie jak operacje boolowskie czy mapowanie tekstur, aby jeszcze bardziej wzbogacić swoje modele.

---

**Ostatnia aktualizacja:** 2025-12-18  
**Testowano z:** Aspose.3D 24.11 for Java  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

## SŁOWA KLUCZOWE CELU:

**Primary Keyword (HIGHEST PRIORITY):**
how to extrude shape

**Secondary Keywords (SUPPORTING):**
create 3d scene, 3d modeling java, generate 3d model, wavefront obj export, save 3d obj