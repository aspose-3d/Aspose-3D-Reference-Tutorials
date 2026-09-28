---
date: 2026-09-28
description: Dowiedz się, jak animować sceny 3D w Javie przy użyciu Aspose.3D, dodawać
  właściwości animacji, tworzyć klatki kluczowe oraz eksportować animowane pliki FBX
  z użyciem technik interpolacji liniowej 3D.
keywords:
- how to animate 3d
- linear interpolation 3d
- export animated fbx
- create keyframe animation
- add animation properties
lastmod: 2026-09-28
linktitle: Jak animować sceny 3D w Javie przy użyciu Aspose.3D
og_description: Dowiedz się, jak animować sceny 3D w Javie przy użyciu Aspose.3D.
  Ten przewodnik krok po kroku pokazuje, jak dodawać właściwości animacji, tworzyć
  klatki kluczowe i eksportować animowane pliki FBX.
og_image_alt: Developer guide showing how to animate 3D scenes in Java with Aspose.3D
og_title: Jak animować sceny 3D w Javie – przewodnik Aspose.3D
schemas:
- author: Aspose
  dateModified: '2026-09-28'
  description: Learn how to animate 3D scenes in Java using Aspose.3D, add animation
    properties, create keyframes, and export animated FBX files with linear interpolation
    3d techniques.
  headline: How to animate 3D scenes in Java with Aspose.3D
  type: TechArticle
- questions:
  - answer: Yes. Purchase a commercial license on the [Aspose purchase page](https://purchase.aspose.com/buy).
    question: Can I use Aspose.3D for commercial projects?
  - answer: Absolutely. Download a trial from the [Aspose releases page](https://releases.aspose.com/).
    question: Is a free trial available?
  - answer: Join the community at the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18)
      for help from staff and other developers.
    question: Where can I get support?
  - answer: Request a [temporary license](https://purchase.aspose.com/temporary-license/)
      to remove runtime restrictions during testing.
    question: How do I obtain a temporary evaluation license?
  - answer: Yes—explore the full [Aspose.3D documentation](https://reference.aspose.com/3d/java/)
      for advanced scenarios such as skeletal animation, morph targets, and custom
      shaders.
    question: Are there more tutorials?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- animate 3d java
- Aspose.3D
- linear interpolation
- FBX export
- Java animation tutorial
title: Jak animować sceny 3D w Javie przy użyciu Aspose.3D
url: /pl/java/animations/add-animation-properties-to-scenes/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak animować sceny 3D w Javie z Aspose.3D

## Wprowadzenie

W tym tutorialu nauczysz się **animować obiekty 3D** w aplikacji Java przy użyciu Aspose.3D. Zacznijemy od stworzenia sceny, zbudujemy prostą siatkę, powiążemy właściwości animacji, zdefiniujemy klatki kluczowe z interpolacją liniową i w końcu wyeksportujemy wynik jako animowany plik FBX. Po zakończeniu będziesz mieć gotowy do użycia plik FBX, który działa w Unity, Blenderze lub dowolnym nowoczesnym przeglądarce 3‑D.

## Szybkie odpowiedzi
- **Jaka biblioteka napędza animację?** Aspose.3D for Java, czysto‑Java silnik 3‑D.  
- **Czy mogę wyeksportować wynik jako FBX?** Tak – przykład zapisuje plik `FBX7500ASCII`, który zachowuje wszystkie klatki kluczowe.  
- **Czy potrzebna jest płatna licencja, aby to wypróbować?** Darmowa wersja próbna działa w fazie rozwoju; licencja komercyjna jest wymagana w produkcji.  
- **Jakiej wersji Javy wymaga?** Java 8 lub nowsza.  
- **Czy interpolacja jest liniowa czy krzywoliniowa?** Obie są obsługiwane; możesz wybrać `Interpolation.LINEAR` dla ruchu prostoliniowego lub `Interpolation.BEZIER` dla płynnych krzywych.

## Czym jest liniowa interpolacja 3D?

Liniowa interpolacja 3D to obliczanie pośrednich wartości transformacji pomiędzy dwoma klatkami kluczowymi przy użyciu prostoliniowego wzoru. W Aspose.3D wybierasz `Interpolation.LINEAR` przy dodawaniu klatki kluczowej, a silnik automatycznie generuje ruch o stałej prędkości między klatkami.

## Dlaczego dodawać właściwości animacji do sceny?

Dodanie właściwości animacji zamienia statyczną geometrię w dynamiczną treść, którą można ponownie wykorzystać w grach, symulacjach lub wizualizacjach produktów. Dzięki Aspose.3D możesz animować wiele węzłów niezależnie, eksportować w pełni animowane pliki FBX i utrzymać cały proces w czystej Javie bez natywnych bibliotek DLL.

## Dlaczego używać Aspose.3D do animacji?

Aspose.3D obsługuje **ponad 12** formatów eksportu — w tym FBX, OBJ, 3MF, STL i GLTF — więc możesz celować w dowolny pipeline. Biblioteka działa wyłącznie na JVM, eliminując zależności natywne. Oferuje także trzy tryby interpolacji (BEZIER, LINEAR, STEP) oraz kompletny interfejs API grafu scen, który pozwala manipulować węzłami, siatkami, materiałami i animacjami przy użyciu jednolitego modelu obiektowego.

## Wymagania wstępne

- Podstawowa znajomość programowania w Javie.  
- Aspose.3D for Java zainstalowane – pobierz go ze [strona wydania](https://releases.aspose.com/3d/java/).  
- Maven lub Gradle skonfigurowane do kompilacji przykładowego projektu.  

## Importowanie pakietów

W swoim pliku źródłowym Java zaimportuj podstawowe przestrzenie nazw Aspose.3D oraz pomocniczą klasę `Common`, która buduje prostą siatkę sześcianu. Klasa `Common` udostępnia statyczne metody generujące podstawową geometrię, taką jak sześcian jednostkowy.

```java
import com.aspose.threed.*;
```

Teraz, gdy przestrzenie nazw są gotowe, rozpocznijmy budowanie sceny.

## Krok 1: inicjalizacja sceny

Klasa `Scene` jest kontenerem najwyższego poziomu Aspose.3D, który przechowuje wszystkie węzły, siatki, światła i dane animacji.

```java
// Initialize scene object
Scene scene = new Scene();
```

## Krok 2: tworzenie siatki przy użyciu konstruktora wielokątów

Klasa `Mesh` reprezentuje zbiór wierzchołków, ścian i normalnych definiujących obiekt 3‑D. W tym kroku pomocnik buduje podstawową siatkę sześcianu, którą później animujemy.

```java
Mesh mesh = new Mesh();
```

## Krok 3: tworzenie węzła sześcianu z translacją

`Node` jest elementem grafu sceny, który może przechowywać siatkę oraz jej właściwości transformacji (translacja, rotacja, skalowanie). Tutaj dołączamy siatkę sześcianu do nowego węzła i pozycjonujemy go w punkcie zerowym.

```java
// Each cube node has its own translation
Node cube1 = scene.getRootNode().createChildNode("cube1", mesh);
```

## Krok 4: znajdowanie właściwości translacji

**Punkt wiązania** łączy określoną właściwość — taką jak translacja — z krzywą animacji. Lokalizując punkt wiązania translacji, umożliwiasz silnikowi modyfikowanie pozycji węzła w czasie.

```java
// Find translation property on node's transform object
Property translation = cube1.getTransform().findProperty("Translation");
```

## Krok 5: tworzenie krzywej animacji dla osi X

Krzywa animacji przechowuje serię klatek kluczowych dla jednego komponentu (X, Y lub Z). Poniższa krzywa definiuje trzy klatki kluczowe w 0 s, 3 s i 5 s. Pierwsze dwie używają BEZIER dla płynnego wygładzania, a ostatnia klatka używa LINEAR, aby pokazać liniową interpolację 3d.

```java
// Create an animation node for the scene
AnimationNode animNode = new AnimationNode("TranslationAnimation");

// Create a bind point for the translation property on the cube's transform
BindPoint bp = animNode.createBindPoint(cube1.getTransform(), "Translation");

// Create the animation curve on the X component of the translation
KeyframeSequence kfsX = new KeyframeSequence();

// Add keyframes for X component
kfsX.add(0, 10.0f, Interpolation.BEZIER);
kfsX.add(3, 20.0f, Interpolation.BEZIER);
kfsX.add(5, 30.0f, Interpolation.LINEAR);

// Bind the keyframe sequence to the X channel of the bind point
bp.bindKeyframeSequence("X", kfsX);
```

## Krok 6: powtórz dla komponentu Z

Animowanie osi Z dodaje głębi ruchowi sześcianu, tworząc bardziej dynamiczną ścieżkę 3‑D. Ta sama logika punktu wiązania i krzywej ma zastosowanie, ale z wartościami przesuwającymi sześcian do przodu i do tyłu.

```java
// Repeat the process for the Z component
KeyframeSequence kfsZ = new KeyframeSequence();
kfsZ.add(0, 10.0f, Interpolation.BEZIER);
kfsZ.add(3, -10.0f, Interpolation.BEZIER);
kfsZ.add(5, 0.0f, Interpolation.LINEAR);

// Bind the keyframe sequence to the Z channel of the same bind point
bp.bindKeyframeSequence("Z", kfsZ);
```

## Jak wyeksportować animowany FBX

Wywołanie `scene.save(...)` z `FileFormat.FBX7500ASCII` zapisuje wszystkie krzywe animacji, punkty wiązania i klatki kluczowe w jednym kontenerze FBX. `FileFormat` jest wyliczeniem definiującym obsługiwane formaty wyjściowe, w tym `FBX7500ASCII`. Upewnij się, że docelowy katalog istnieje i masz uprawnienia zapisu; w przeciwnym razie operacja zapisu zgłosi wyjątek.

```java
// Specify the directory for saving the 3D scene
String MyDir = "Your Document Directory";
MyDir = MyDir + "PropertyToDocument.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7500ASCII);
```

Wygenerowany plik można otworzyć w Blenderze, Unity, Autodesk Maya lub dowolnym przeglądarce obsługującej format FBX, co pozwala natychmiast podglądnąć animację.

## Typowe problemy i rozwiązania

| Objaw | Prawdopodobna przyczyna | Rozwiązanie |
|---------|--------------|-----|
| Brak widocznego ruchu | Kluczowe klatki dodane do niewłaściwego komponentu (np. „Y” zamiast „X”) | Sprawdź nazwę komponentu w `bindKeyframeSequence`. |
| Animacja przeskakuje | Nieprawidłowe mieszanie BEZIER i LINEAR | Utrzymuj spójną interpolację dla płynniejszego ruchu lub ręcznie dostosuj styki. |
| Plik nie został zapisany | Nieprawidłowa ścieżka katalogu | Upewnij się, że `MyDir` wskazuje istniejący folder z prawami zapisu i kończy się na `.fbx`. |

## Najczęściej zadawane pytania

**Q: Czy mogę używać Aspose.3D w projektach komercyjnych?**  
A: Tak. Kup licencję komercyjną na [stronie zakupu Aspose](https://purchase.aspose.com/buy).

**Q: Czy dostępna jest darmowa wersja próbna?**  
A: Absolutnie. Pobierz wersję próbną ze [strony wydania Aspose](https://releases.aspose.com/).

**Q: Gdzie mogę uzyskać wsparcie?**  
A: Dołącz do społeczności na [forum Aspose.3D](https://forum.aspose.com/c/3d/18), aby uzyskać pomoc od zespołu i innych programistów.

**Q: Jak uzyskać tymczasową licencję ewaluacyjną?**  
A: Zamów [tymczasową licencję](https://purchase.aspose.com/temporary-license/), aby usunąć ograniczenia w czasie działania podczas testów.

**Q: Czy jest więcej tutoriali?**  
A: Tak — przeglądaj pełną [dokumentację Aspose.3D](https://reference.aspose.com/3d/java/) w poszukiwaniu zaawansowanych scenariuszy, takich jak animacja szkieletowa, cele morfowania i własne shadery.

## Podsumowanie

Teraz wiesz **jak animować obiekty 3D** w Javie z Aspose.3D: twórz scenę, wiąż właściwości translacji, definiuj sekwencje klatek kluczowych z interpolacją liniową i eksportuj animowany plik FBX. Eksperymentuj z rotacją, skalowaniem lub wieloma węzłami, aby tworzyć bogatsze animacje dla gier, symulacji lub wizualizacji produktów.

---

**Ostatnia aktualizacja:** 2026-09-28  
**Testowano z:** Aspose.3D for Java 24.12 (latest)  
**Autor:** Aspose

## Powiązane tutoriale

- [Utwórz plik FBX przy użyciu Aspose.3D dla Java – Tutorial grafiki 3D](/3d/java/load-and-save/create-empty-3d-document/)
- [Zapisz sceny 3D w Javie z Aspose.3D – Efektywna konwersja plików 3D](/3d/java/load-and-save/save-3d-scenes/)
- [Eksportuj model do FBX z kwaternionami w Javie przy użyciu Aspose.3D](/3d/java/geometry/transform-3d-nodes-with-quaternions/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}