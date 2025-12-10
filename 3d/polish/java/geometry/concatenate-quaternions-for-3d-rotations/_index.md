---
date: 2025-12-10
description: Dowiedz się, jak stworzyć obrót 3‑dowego walca, łącząc kwaterniony dla
  obrotów 3D w Javie przy użyciu Aspose.3D. Ten przewodnik pokazuje, jak łączyć wiele
  obrotów i konwertować kwaterniony na kąty Eulera.
linktitle: Create 3D Cylinder Rotation by Concatenating Quaternions in Java with Aspise.3D
second_title: Aspose.3D Java API
title: Tworzenie obrotu 3D walca przez łączenie kwaternionów w Javie z Aspise.3D
url: /pl/java/geometry/concatenate-quaternions-for-3d-rotations/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Utwórz obrót walca 3D poprzez łączenie kwaternionów w Javie z Aspose.3D

## Wprowadzenie

Łączenie kwaternionów to podstawowa technika, gdy potrzebujesz **utworzyć obrót walca 3d** w scenie 3‑D. Łącząc obroty, unikasz blokady gimbal i zapewniasz płynność transformacji. W tym samouczku pokażemy, jak **połączyć wiele obrotów** przy użyciu API Java Aspose.3D oraz omówimy, jak **przekształcić kąty eulera kwaternionu**, gdy zajdzie taka potrzeba.

## Szybkie odpowiedzi
- **Co oznacza „łączenie kwaternionów”?** Oznacza to mnożenie dwóch obrotów kwaternionowych w celu uzyskania jednego, połączonego obrotu.  
- **Dlaczego używać kwaternionów do obrotu walca?** Zapewniają płynne interpolacje i unikają blokady gimbal w porównaniu z kątami Eulera.  
- **Czy potrzebna jest licencja do uruchomienia przykładu?** Darmowa wersja próbna wystarcza do rozwoju; licencja płatna jest wymagana w środowisku produkcyjnym.  
- **Jakiego formatu pliku użyto w przykładzie?** Scena jest zapisywana jako plik FBX (wersja ASCII).  
- **Czy mogę zmienić oś obrotu?** Tak – wystarczy zmodyfikować wektor osi przekazywany do `Quaternion.fromAngleAxis`.

## Dlaczego używać łączenia kwaternionów do tworzenia obrotu walca 3d?
Kwaterniony pozwalają na nakładanie obrotów bez martwienia się o kolejność osi. Jest to szczególnie przydatne przy animacji obiektów, takich jak walce, które muszą obracać się wokół wielu osi kolejno. Rezultatem jest czysta, przewidywalna transformacja, która idealnie integruje się z grafem sceny Aspose.3D.

## Wymagania wstępne

Zanim przejdziesz do samouczka, upewnij się, że spełniasz następujące wymagania:

- Podstawowa znajomość programowania w języku Java.  
- Zainstalowany Aspose.3D dla Javy. Możesz go pobrać [tutaj](https://releases.aspose.com/3d/java/).

## Importowanie pakietów

Upewnij się, że zaimportowałeś niezbędne pakiety, aby wykorzystać funkcje Aspose.3D. Dodaj następujące linie do swojego kodu Java:

```java
import com.aspose.threed.*;
```

Teraz rozbijmy przykładowy kod na kilka kroków, aby stworzyć kompleksowy samouczek:

## Krok 1: Konfiguracja sceny

```java
Scene scene = new Scene();
```

## Krok 2: Definicja kwaternionów

```java
Quaternion q1 = Quaternion.fromEulerAngle(Math.PI * 0.5, 0, 0);
Vector3.X_AXIS.x = 3;
Quaternion q2 = Quaternion.fromAngleAxis(-Math.PI * 0.5, Vector3.X_AXIS);
```

## Krok 3: Łączenie kwaternionów

```java
Quaternion q3 = q1.concat(q2);
```

## Krok 4: Tworzenie 3 walców

```java
Node cylinder = scene.getRootNode().createChildNode("cylinder-q1", new Cylinder(0.1, 1, 2));
cylinder.getTransform().setRotation(q1);
cylinder.getTransform().setTranslation(new Vector3(-5, 2, 0));
```

```java
cylinder = scene.getRootNode().createChildNode("cylinder-q2", new Cylinder(0.1, 1, 2));
cylinder.getTransform().setRotation(q2);
cylinder.getTransform().setTranslation(new Vector3(0, 2, 0));
```

```java
cylinder = scene.getRootNode().createChildNode("cylinder-q3", new Cylinder(0.1, 1, 2));
cylinder.getTransform().setRotation(q3);
cylinder.getTransform().setTranslation(new Vector3(5, 2, 0));
```

## Krok 5: Zapis do pliku

```java
MyDir = MyDir + "test_out.fbx";
scene.save(MyDir, FileFormat.FBX7400ASCII);
// ExEnd:ConcatenateQuaternions
```

## Krok 6: Wyświetlenie komunikatu sukcesu

```java
System.out.println("\nQuaternions concatenated successfully.\nFile saved at " + MyDir);
```

## Zakończenie

Postępując zgodnie z tym samouczkiem, nauczyłeś się **tworzyć obrót walca 3d** poprzez łączenie kwaternionów dla obrotów 3D w Javie przy użyciu Aspose.3D. Eksperymentuj z różnymi kombinacjami kwaternionów, aby uzyskać różnorodne i precyzyjne obroty w swoich projektach 3D.

## Najczęściej zadawane pytania

### Q1: Czy mogę używać Aspose.3D dla Javy za darmo?

A1: Aspose.3D oferuje [bezpłatną wersję próbną](https://releases.aspose.com/) do zapoznania się z funkcjami. W przypadku dłuższego użytkowania rozważ zakup [licencji](https://purchase.aspose.com/buy).

### Q2: Gdzie mogę znaleźć pełną dokumentację Aspose.3D?

A2: [Dokumentacja](https://reference.aspose.com/3d/java/) zawiera szczegółowe informacje i przykłady, które pomogą Ci rozpocząć pracę.

### Q3: Jak mogę uzyskać wsparcie techniczne dla Aspose.3D?

A3: Odwiedź [forum Aspose.3D](https://forum.aspose.com/c/3d/18), aby zadawać pytania, dzielić się doświadczeniami i uzyskać pomoc od społeczności.

### Q4: Czy dostępne są tymczasowe licencje dla Aspose.3D?

A4: Tak, możesz uzyskać [tymczasową licencję](https://purchase.aspose.com/temporary-license/) do testów i oceny.

### Q5: Jakie formaty plików są obsługiwane przy zapisie scen 3D?

A5: Aspose.3D obsługuje różne formaty; sceny można zapisywać w formacie FBX, jak pokazano w tym samouczku.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Ostatnia aktualizacja:** 2025-12-10  
**Testowano z:** Aspose.3D 24.11 dla Javy (najnowsza)  
**Autor:** Aspose  

---