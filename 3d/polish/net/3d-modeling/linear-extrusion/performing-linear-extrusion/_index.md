---
date: 2026-01-07
description: Naucz się, jak wykonać liniową ekstruzję 2‑wymiarowego profilu i wyeksportować
  model 3D w formacie OBJ przy użyciu Aspose.3D dla .NET. Ten poradnik dotyczący liniowej
  ekstruzji prowadzi Cię krok po kroku.
linktitle: Performing Linear Extrusion
second_title: Aspose.3D .NET API
title: Jak wykonać ekstruzję liniową w Aspose.3D dla .NET
url: /pl/net/3d-modeling/linear-extrusion/performing-linear-extrusion/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak wykonać Linear Extrude przy użyciu Aspose.3D dla .NET

## Wprowadzenie

Witamy w naszym **samouczku linear extrusion**! W tym przewodniku odkryjesz **how to linear extrude** profil 2‑D i przekształcisz go w w pełni rozwinięty obiekt 3‑D przy użyciu Aspose.3D dla .NET. Niezależnie od tego, czy tworzysz aplikację w stylu CAD, czy po prostu potrzebujesz **export 3d model obj** plików do dalszego przetwarzania, ten krok‑po‑kroku przewodnik da Ci pewność, aby dodać potężne tworzenie geometrii do swoich projektów.

## Szybkie odpowiedzi
- **What is linear extrusion?** Rozciąganie kształtu 2‑D wzdłuż prostej ścieżki w celu utworzenia bryły 3‑D.  
- **Which library do we use?** Aspose.3D for .NET.  
- **Do I need a license?** Tymczasowa licencja działa w testach; pełna licencja jest wymagana w produkcji.  
- **Can I export to OBJ?** Tak – końcowa scena jest zapisywana jako plik Wavefront OBJ.  
- **How many lines of code?** Mniej niż 30 linii C# plus komentarze wyjaśniające.

## Co to jest Linear Extrusion?

Linear extrusion pobiera płaski profil (np. prostokąt lub koło) i przemieszcza go wzdłuż prostej linii, opcjonalnie dodając skręty, skalowanie lub przesunięcia. Wynikiem jest bryła, którą można renderować, edytować lub eksportować do użycia w innych narzędziach 3‑D.

## Dlaczego używać Aspose.3D do Linear Extrusion?

* **Zero‑dependency:** Brak potrzeby zewnętrznych jąder CAD.  
* **Full .NET support:** Działa z .NET Framework, .NET Core oraz .NET 5/6+.  
* **Export flexibility:** Bezpośrednio zapisuje do OBJ, STL, FBX i wielu innych formatów.  
* **Rich API:** Kontroluj warstwy, skręt i przesunięcia przy użyciu kilku właściwości.

## Wymagania wstępne

1. **Aspose.3D installed** – pobierz go z [here](https://releases.aspose.com/3d/net/).  
2. **Documentation access** – postępuj zgodnie z przewodnikiem instalacji [here](https://reference.aspose.com/3d/net/).  
3. Środowisko programistyczne .NET (Visual Studio, VS Code lub Rider) z odwołanymi wymaganymi przestrzeniami nazw.

## Importowanie przestrzeni nazw

Dołącz niezbędne przestrzenie nazw, aby odblokować funkcjonalność Aspose.3D:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Te przestrzenie nazw dają dostęp do `Scene`, `LinearExtrusion`, `RectangleShape` oraz klas pomocniczych, takich jak `Vector3`.

## Wykonywanie Linear Extrusion

Poniżej znajduje się pełny przepływ pracy. Każdy krok jest wyjaśniony prostym językiem przed odpowiednim blokiem kodu, abyś mógł podążać bez zgadywania, co robi kod.

### Krok 1: Inicjalizacja profilu bazowego

Najpierw utwórz kształt 2‑D, który zostanie wyekstruzowany. W tym przykładzie używamy prostokąta z małym promieniem zaokrąglenia.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

*Dlaczego to ważne:* Profil definiuje przekrój końcowego obiektu 3‑D. Dostosuj `RoundingRadius`, szerokość lub wysokość, aby uzyskać różne sylwetki.

### Krok 2: Zastosowanie Linear Extrusion

Teraz przesuń profil o 10 jednostek wzdłuż osi Z, dodając 100 warstw dla płynności, wyśrodkowując geometrię i stosując pełny obrót 360° z przesunięciem.

```csharp
var extrusion = new LinearExtrusion(profile, 10) { Slices = 100, Center = true, Twist = 360, TwistOffset = new Vector3(10, 0, 0) };
```

*Pro tip:* Eksperymentuj z `Slices`, aby zrównoważyć wydajność i jakość wizualną, oraz testuj `Twist` dla efektów spirali.

### Krok 3: Utworzenie sceny

`Scene` działa jako kontener dla wszystkich elementów 3‑D — myśl o nim jak o płótnie.

```csharp
Scene scene = new Scene();
```

### Krok 4: Dodanie ekstruzji do sceny

Dołącz wyekstruzowaną geometrię do węzła głównego sceny, aby stała się częścią hierarchii renderowalnej.

```csharp
scene.RootNode.CreateChildNode(extrusion);
```

### Krok 5: Zapisz model 3‑D

Na koniec wyeksportuj scenę do powszechnie obsługiwanego pliku OBJ. To demonstruje możliwość **export 3d model obj** w Aspose.3D.

```csharp
scene.Save(RunExamples.GetOutputFilePath("LinearExtrusion.obj"), FileFormat.WavefrontOBJ);
```

Gdy otworzysz powstały plik `LinearExtrusion.obj` w dowolnym przeglądarce 3‑D, zobaczysz skręcony prostokątny pryzmat — dokładnie to, co opisuje kod.

## Typowe pułapki i wskazówki

| Problem | Dlaczego się pojawia | Jak naprawić |
|---------|----------------------|--------------|
| **Profil niewidoczny** | Zapomniano dodać ekstruzję do sceny. | Upewnij się, że wywołano `CreateChildNode`. |
| **Skręt wygląda płasko** | `Slices` jest za niskie, co powoduje grubą geometrię. | Zwiększ `Slices` (np. 200), aby uzyskać płynniejszy skręt. |
| **Eksport nie powodzi się** | Folder wyjściowy nie istnieje lub brakuje uprawnień do zapisu. | Użyj `RunExamples.GetOutputFilePath` lub utwórz katalog ręcznie. |
| **Nieoczekiwane skalowanie** | `Center` ustawione na `false` przesuwa geometrię. | Ustaw `Center = true`, chyba że potrzebny jest offset. |

## Najczęściej zadawane pytania

### Q1: Czy Aspose.3D jest odpowiedni dla początkujących?

A1: Zdecydowanie! Aspose.3D oferuje przyjazne dla użytkownika API, a ten samouczek prowadzi Cię przez podstawy linear extrusion.

### Q2: Czy mogę używać Aspose.3D w projektach komercyjnych?

A2: Tak, Aspose.3D posiada opcje licencjonowania zarówno dla użytku prywatnego, jak i komercyjnego. Sprawdź [here](https://purchase.aspose.com/buy) po szczegóły.

### Q3: Jak mogę uzyskać tymczasowe licencje do testów?

A3: Odwiedź [this link](https://purchase.aspose.com/temporary-license/) aby uzyskać tymczasowe licencje do celów testowych.

### Q4: Gdzie mogę znaleźć wsparcie społeczności?

A4: Dołącz do [Aspose.3D Forum](https://forum.aspose.com/c/3d/18), aby połączyć się z aktywną społecznością i uzyskać pomoc.

### Q5: Czy dostępna jest darmowa wersja próbna?

A5: Oczywiście! Pobierz darmową wersję próbną [here](https://releases.aspose.com/), aby osobiście doświadczyć możliwości Aspose.3D.

---

**Last Updated:** 2026-01-07  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

## CELE SŁÓW KLUCZOWYCH:

**Główne słowo kluczowe (NAJWYŻSZY PRIORYTET):**
how to linear extrude

**Drugie słowa kluczowe (WSPARCIU):**
export 3d model obj, linear extrusion tutorial

**Strategia integracji słów kluczowych:**
1. Główne słowo kluczowe: użyj 3‑5 razy (tytuł, meta, pierwszy akapit, nagłówek H2, treść)
2. Drugie słowa kluczowe: użyj 1‑2 razy każde (nagłówki, treść)
3. Wszystkie słowa kluczowe muszą być wprowadzane naturalnie – priorytetem jest czytelność, nie liczba słów kluczowych
4. Jeśli słowo kluczowe nie pasuje naturalnie, użyj semantycznej wariacji lub pomiń je