---
date: 2025-12-19
description: Dowiedz się, jak stworzyć scenę 3D i wyeksportować obiekt 3D w formacie
  OBJ, używając odchylenia skrętu w ekstruzji liniowej z Aspose.3D dla Javy.
linktitle: Create 3d scene with Twist Offset – Aspose.3D Java
second_title: Aspose.3D Java API
title: Utwórz scenę 3D z offsetem skrętu – Aspose.3D Java
url: /pl/java/linear-extrusion/using-twist-offset/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Utwórz scenę 3d z Twist Offset – Aspose.3D for Java

## Wprowadzenie

W dynamicznym świecie grafiki 3D, nauka **tworzenia sceny 3d** przy użyciu ekstruzji liniowej to przełom. Dzięki Aspose.3D for Java możesz podnieść swoje umiejętności modelowania 3D, wprowadzając funkcję Twist Offset do procesu ekstruzji liniowej. Ten samouczek poprowadzi Cię przez kroki wykorzystania Twist Offset w ekstruzji liniowej przy użyciu Aspose.3D for Java, dostarczając narzędzia do tworzenia zachwycających scen 3D.

## Szybkie odpowiedzi
- **Co robi Twist Offset?** Przesuwa początek skrętu wzdłuż ścieżki ekstruzji, dając większą kontrolę nad geometrią.  
- **Jaki format pliku jest używany do eksportu?** Przykład zapisuje model jako Wavefront OBJ (`.obj`).  
- **Czy potrzebna jest licencja do rozwoju?** Darmowa wersja próbna działa do testów; licencja komercyjna jest wymagana w produkcji.  
- **Jaka wersja Javy jest wymagana?** Java 8 lub nowsza.  
- **Czy mogę zmienić liczbę podziałów?** Tak – metoda `setSlices` definiuje płynność skrętu.

## Wymagania wstępne

Zanim zagłębisz się w samouczek, upewnij się, że spełniasz następujące wymagania:

- Środowisko Java: Upewnij się, że masz skonfigurowane środowisko programistyczne Java na swoim systemie.  
- Aspose.3D for Java: Pobierz i zainstaluj bibliotekę Aspose.3D z [linku do pobrania](https://releases.aspose.com/3d/java/).  
- Dokumentacja: Zapoznaj się z [dokumentacją Aspose.3D for Java](https://reference.aspose.com/3d/java/).  

## Importowanie pakietów

W swoim projekcie Java zaimportuj niezbędne pakiety, aby rozpocząć korzystanie z Aspose.3D for Java. Upewnij się, że dołączasz wymagane biblioteki dla płynnej integracji.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Krok 1: Przygotuj środowisko

Rozpocznij od skonfigurowania środowiska programistycznego Java i upewnienia się, że Aspose.3D for Java jest poprawnie zainstalowane.

## Krok 2: Zainicjuj profil bazowy

Utwórz profil bazowy do ekstruzji, w tym przypadku `RectangleShape` z promieniem zaokrąglenia 0,3.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
// Initialize the base profile to be extruded
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Krok 3: Utwórz scenę 3D

Zbuduj scenę 3D, aby pomieścić wyekstruzowane obiekty.

```java
// Create a scene
Scene scene = new Scene();
```

## Krok 4: Utwórz węzły

Wygeneruj węzły w scenie, aby reprezentować różne podmioty.

```java
// Create left node
Node left = scene.getRootNode().createChildNode();
// Create right node
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Krok 5: Wykonaj ekstruzję liniową

Zastosuj ekstruzję liniową na lewym i prawym węźle z różnymi właściwościami.

```java
// Perform linear extrusion on left node using twist and slices property
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// Perform linear extrusion on right node using twist, twist offset, and slices property
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

## Krok 6: Zapisz scenę 3D

Zapisz nowo utworzoną scenę 3D w określonym formacie pliku.

```java
// Save 3D scene
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Jak zapisać model 3d i wyeksportować 3d obj

Wywołanie `scene.save` w poprzednim kroku **zapisuje model 3d** jako plik OBJ, który jest powszechnie obsługiwanym formatem **export 3d obj**. Możesz zmienić nazwę pliku lub wybrać inny obsługiwany format (np. STL, FBX), modyfikując enum `FileFormat`.

## Podsumowanie

Gratulacje! Pomyślnie zaimplementowałeś Twist Offset w ekstruzji liniowej przy użyciu Aspose.3D for Java. Ta potężna funkcja otwiera przed Tobą świat możliwości w modelowaniu 3D, umożliwiając **tworzenie sceny 3d** z zawiłymi skrętami i offsetami, a następnie **zapisanie modelu 3d** w formacie gotowym do dalszych etapów.

## FAQ

### Q1: Czy mogę używać Aspose.3D for Java w projektach niekomercyjnych?

A1: Tak, Aspose.3D for Java może być używany zarówno w projektach komercyjnych, jak i niekomercyjnych. Sprawdź [opcje licencjonowania](https://purchase.aspose.com/buy) po więcej szczegółów.

### Q2: Gdzie mogę znaleźć wsparcie dla Aspose.3D for Java?

A2: Odwiedź [forum Aspose.3D for Java](https://forum.aspose.com/c/3d/18), aby uzyskać pomoc i połączyć się ze społecznością.

### Q3: Czy dostępna jest darmowa wersja próbna Aspose.3D for Java?

A3: Tak, możesz wypróbować darmową wersję próbną ze [strony wydań](https://releases.aspose.com/).

### Q4: Jak uzyskać tymczasową licencję dla Aspose.3D for Java?

A4: Uzyskaj tymczasową licencję do swojego projektu, odwiedzając [ten link](https://purchase.aspose.com/temporary-license/).

### Q5: Czy dostępne są dodatkowe przykłady i samouczki?

A5: Tak, odwołaj się do [dokumentacji](https://reference.aspose.com/3d/java/), aby uzyskać więcej przykładów i szczegółowych samouczków.

## Najczęściej zadawane pytania

**P: Czy ten samouczek jest częścią serii samouczków Aspose 3d?**  
O: Tak – jest to oficjalny **aspose 3d tutorial**, który demonstruje konkretną funkcję biblioteki.

**P: Czy mogę użyć innego kształtu zamiast prostokąta?**  
O: Oczywiście. Każda implementacja `IProfile` (np. `CircleShape`, własny `PolygonShape`) może być ekstruzowana.

**P: Co się stanie, jeśli pominę `setTwistOffset`?**  
O: Ekstruzja rozpocznie skręt od początku profilu, co skutkuje symetrycznym skrętem.

**P: Jak zwiększyć płynność skrętu?**  
O: Zwiększ wartość przekazywaną do `setSlices`; większa liczba podziałów daje gładszą geometrię.

**P: Jakie inne formaty plików mogę eksportować oprócz OBJ?**  
O: Aspose.3D obsługuje STL, FBX, GLTF, 3MF i kilka innych poprzez enum `FileFormat`.

---

**Ostatnia aktualizacja:** 2025-12-19  
**Testowano z:** Aspose.3D 24.11 for Java  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

## SŁOWA KLUCZOWE DO CELE:

**Główne słowo kluczowe (NAJWYŻSZY PRIORYTET):**  
create 3d scene  

**Drugorzędne słowa kluczowe (WSPARCIE):**  
save 3d model, export 3d obj, aspose 3d tutorial