---
date: 2026-02-25
description: Dowiedz się, jak tworzyć trójwymiarowe ekstruzje w Javie przy użyciu
  Aspose.3D i eksportować pliki OBJ w Javie, dostarczając wysokiej jakości modele
  3D w aplikacjach Java.
linktitle: Create 3D Extrusion Java with Aspose.3D
second_title: Aspose.3D Java API
title: Utwórz trójwymiarową ekstruzję w Javie z Aspose.3D
url: /pl/java/linear-extrusion/performing-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Tworzenie 3D Extrusion w Javie z Aspose.3D

## Wprowadzenie

Jeśli potrzebujesz **szybko i niezawodnie stworzyć 3d extrusion java**, trafiłeś na właściwy tutorial. W ciągu kilku minut przeprowadzimy Cię przez generowanie liniowej ekstruzji, dostosowywanie jej geometrii oraz **eksportowanie pliku obj java** przy użyciu biblioteki Aspose.3D. Niezależnie od tego, czy budujesz narzędzie podobne do CAD, pipeline zasobów do gry, czy jakikolwiek inny workflow 3‑D oparty na Javie, ten przewodnik zapewni solidną, gotową do produkcji podstawę.

## Szybkie odpowiedzi
- **Co oznacza „linear extrusion”?** To przemieszczenie profilu 2‑D wzdłuż prostej linii w celu utworzenia bryły 3‑D.  
- **Która biblioteka obsługuje ekstruzję?** Aspose.3D for Java udostępnia wysokopoziomowe API.  
- **Czy mogę wyeksportować wynik jako OBJ?** Tak – tutorial kończy się wywołaniem `scene.save(..., FileFormat.WAVEFRONTOBJ)`.  
- **Czy potrzebna jest licencja do rozwoju?** Darmowa wersja próbna wystarczy do nauki; licencja komercyjna jest wymagana w produkcji.  
- **Jaką wersję Javy obsługuje?** Java 1.6 i nowsze.

## Co to jest Create 3D Extrusion Java?
Tworzenie 3D extrusion w Javie oznacza wzięcie prostego kształtu 2‑D (np. prostokąta) i wydłużenie go w trzecim wymiarze. Powstała siatka może być zapisana w popularnych formatach, takich jak OBJ, które rozumie wiele edytorów 3‑D.

## Dlaczego warto używać Aspose.3D do Linear Extrusion?
- **Czyste API Java** – brak zależności natywnych, idealne dla projektów wieloplatformowych.  
- **Bogate sterowanie geometrią** – zaokrąglanie, skręcanie, podziały i offset są dostępne poprzez proste właściwości.  
- **Bezpośredni eksport** – zapisywanie do OBJ, STL, FBX i innych bez dodatkowych konwerterów.  
- **Wsparcie klasy korporacyjnej** – licencjonowanie, dokumentacja i fora społecznościowe są łatwo dostępne.

## Wymagania wstępne

Zanim rozpoczniesz, upewnij się, że masz:

1. **Środowisko programistyczne Java** – zainstalowany i skonfigurowany JDK 1.6+.  
2. **Bibliotekę Aspose.3D** – pobierz najnowszy plik JAR z oficjalnej strony [tutaj](https://releases.aspose.com/3d/java/).  

## Importowanie pakietów

Dodaj podstawową przestrzeń nazw Aspose.3D do swojego pliku źródłowego Java:

```java
import com.aspose.threed.*;
```

## Krok 1: Ustawienie katalogu dokumentu

Zdefiniuj, gdzie będą zapisywane wygenerowane pliki:

```java
String MyDir = "Your Document Directory";
```

> **Wskazówka:** Użyj ścieżki bezwzględnej lub konfigurowalnej właściwości, aby lokalizacja wyjściowa działała w różnych środowiskach.

## Krok 2: Inicjalizacja podstawowego kształtu

Utwórz prostokąt, który posłuży jako profil ekstruzji. Promień zaokrąglenia wygładza narożniki:

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

Możesz eksperymentować z `setRoundingRadius`, aby uzyskać bardziej okrągły lub ostrzejszy profil.

## Krok 3: Wykonanie liniowej ekstruzji

Teraz przekształcamy prostokąt 2‑D w obiekt 3‑D. Konstruktor przyjmuje profil oraz głębokość ekstruzji (w tym przykładzie 10 jednostek). Dodatkowe właściwości precyzują siatkę:

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

- **Slices** – kontroluje płynność ekstruzji.  
- **Center** – wyrównuje geometrię względem początku układu współrzędnych.  
- **Twist** – obraca profil wzdłuż osi ekstruzji (tutaj pełne 360°).  
- **TwistOffset** – przesuwa punkt obrotu, co pozwala tworzyć spirale.

## Krok 4: Utworzenie sceny 3D

`Scene` jest kontenerem dla wszystkich obiektów 3‑D. Dodanie ekstruzji jako węzła potomnego sprawia, że staje się ona częścią grafu sceny:

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

## Krok 5: Zapis sceny 3D

Na koniec wyeksportuj scenę do pliku Wavefront OBJ – formatu szeroko wspieranego przez edytory 3‑D, silniki gier i pipeline’y druku:

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Po uruchomieniu kodu znajdziesz **LinearExtrusion.obj** w określonym katalogu, gotowy do otwarcia w Blenderze, Mayi lub dowolnym innym przeglądarce OBJ.

## Typowe problemy i rozwiązania

| Objaw | Prawdopodobna przyczyna | Rozwiązanie |
|---------|--------------|-----|
| `FileNotFoundException` przy zapisie | `MyDir` nie istnieje lub brak uprawnień do zapisu | Utwórz folder wcześniej lub użyj ścieżki bezwzględnej z odpowiednimi uprawnieniami. |
| OBJ jest pusty w przeglądarce | Do sceny nie dodano geometrii | Sprawdź, czy obiekt `LinearExtrusion` został poprawnie zainicjowany i podłączony do węzła głównego. |
| Skręt wygląda niepoprawnie | Nieprawidłowe wartości `TwistOffset` | Dostosuj współrzędne `Vector3`; pamiętaj, że offset jest stosowany przed rotacją skrętu. |

## Najczęściej zadawane pytania

### Q1: Czy Aspose.3D jest kompatybilny ze wszystkimi wersjami Javy?
A1: Aspose.3D został zaprojektowany do pracy z Java 1.6 i nowszymi wersjami.

### Q2: Czy mogę używać Aspose.3D w projektach komercyjnych?
A2: Tak, Aspose.3D może być używany zarówno w projektach prywatnych, jak i komercyjnych. Szczegóły licencjonowania znajdziesz [tutaj](https://purchase.aspose.com/buy).

### Q3: Jak mogę uzyskać wsparcie dla Aspose.3D?
A3: Odwiedź [forum Aspose.3D](https://forum.aspose.com/c/3d/18) w celu uzyskania pomocy społeczności lub rozważ zakup [tymczasowej licencji](https://purchase.aspose.com/temporary-license/) dla wsparcia premium.

### Q4: Czy Aspose.3D oferuje inne funkcje modelowania 3D?
A4: Oczywiście! Przeglądaj obszerną dokumentację [tutaj](https://reference.aspose.com/3d/java/) po pełną listę funkcji i przykładów.

### Q5: Czy dostępna jest darmowa wersja próbna Aspose.3D?
A5: Tak, darmową wersję próbną możesz pobrać [tutaj](https://releases.aspose.com/).

## Zakończenie

Teraz wiesz, jak **tworzyć 3d extrusion java** przy użyciu Aspose.3D, dostosowywać jej geometrię oraz **eksportować plik obj java** do dalszego wykorzystania. Eksperymentuj z różnymi profilami, skrętami i formatami eksportu, aby dopasować rozwiązanie do konkretnych potrzeb projektu. Gdy będziesz gotowy, odkryj inne możliwości Aspose.3D, takie jak manipulacja siatką, mapowanie tekstur i animacje, aby jeszcze bardziej wzbogacić swoje aplikacje 3‑D oparte na Javie.

---

**Ostatnia aktualizacja:** 2026-02-25  
**Testowano z:** Aspose.3D 24.12 for Java  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}