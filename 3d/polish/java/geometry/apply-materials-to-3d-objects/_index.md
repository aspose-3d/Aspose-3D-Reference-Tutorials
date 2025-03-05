---
title: Zastosuj materiały do obiektów 3D w Javie za pomocą Aspose.3D
linktitle: Zastosuj materiały do obiektów 3D w Javie za pomocą Aspose.3D
second_title: Aspose.3D API Java
description: Poznaj świat grafiki 3D dzięki Aspose.3D dla Java. Dowiedz się, jak płynnie nakładać materiały na obiekty 3D. Podnieś poziom swoich projektów dzięki realistycznym efektom wizualnym.
type: docs
weight: 14
url: /pl/java/geometry/apply-materials-to-3d-objects/
---
## Wstęp

W dynamicznym świecie grafiki 3D Aspose.3D for Java wyróżnia się jako potężne narzędzie ożywiające Twoje projekty. Dodawanie materiałów do obiektów 3D zwiększa atrakcyjność wizualną, czyniąc je bardziej realistycznymi. W tym samouczku przeprowadzimy Cię przez proces nakładania materiałów na kostkę 3D przy użyciu Aspose.3D dla Java.

## Warunki wstępne

Zanim przejdziesz do samouczka, upewnij się, że spełniasz następujące wymagania wstępne:

- Zestaw Java Development Kit (JDK) zainstalowany w systemie.
- Biblioteka Aspose.3D for Java pobrana i dodana do Twojego projektu.
- Znajomość podstawowych koncepcji programowania w języku Java.

## Importuj pakiety

Aby rozpocząć, zaimportuj niezbędne pakiety do swojego projektu Java. Dodaj następujące wiersze na początku kodu:

```java
import com.aspose.threed.*;


import java.nio.file.Files;
import java.nio.file.Paths;
```

## Krok 1: Zainicjuj obiekt sceny

```java
// Zainicjuj obiekt sceny
Scene scene = new Scene();
```

## Krok 2: Zainicjuj obiekt węzła kostki

```java
// Zainicjuj obiekt węzła kostki
Node cubeNode = new Node("cube");
```

## Krok 3: Utwórz siatkę za pomocą narzędzia Polygon Builder

```java
// Wywołaj klasę Common, aby utworzyć siatkę przy użyciu metody konstruktora wielokątów, aby ustawić instancję siatki
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Krok 4: Skieruj węzeł na siatkę

```java
// Wskaż węzeł na siatkę
cubeNode.setEntity(mesh);
```

## Krok 5: Dodaj kostkę do sceny

```java
// Dodaj kostkę do sceny
scene.getRootNode().addChildNode(cubeNode);
```

## Krok 6: Zainicjuj obiekt PhongMaterial

```java
// Zainicjuj obiekt PhongMaterial
PhongMaterial mat = new PhongMaterial();
```

## Krok 7: Zainicjuj obiekt tekstury

```java
// Zainicjuj obiekt tekstury
Texture diffuse = new Texture();
```

## Krok 8: Ustaw lokalną ścieżkę pliku tekstury

```java
// Ścieżka do katalogu dokumentów.
String MyDir = "Your Document Directory";
```

## Krok 9: Ustaw lokalną ścieżkę pliku dla osadzonej tekstury

```java
// Ustaw lokalną ścieżkę pliku dla osadzonej tekstury
diffuse.setFileName(MyDir + "surface.dds");
```

## Krok 10: Ustaw teksturę materiału

```java
// Ustaw teksturę materiału
mat.setTexture(Material.MAP_DIFFUSE, diffuse);
```

## Krok 11: Osadź surowe dane treści w FBX (opcjonalnie)

```java
// Ustaw nazwę pliku dla osadzonej tekstury
diffuse.setFileName("embedded-texture.png");
// Ustaw zawartość binarną
diffuse.setContent(Files.readAllBytes(Paths.get(MyDir, "aspose-logo.jpg")));
```

## Krok 12: Ustaw kolor lustrzany

```java
// Ustaw kolor lustrzany
mat.setSpecularColor(new Vector3(1, 0, 0));
```

## Krok 13: Ustaw jasność

```java
// Ustaw jasność
mat.setShininess(100);
```

## Krok 14: Ustaw właściwości materiału obiektu kostki

```java
// Ustaw właściwość materiału obiektu kostki
cubeNode.setMaterial(mat);
```

## Krok 15: Zapisz scenę 3D

```java
// Ustaw nazwę pliku
MyDir = MyDir + "MaterialToCube.fbx";
// Zapisz scenę 3D w obsługiwanych formatach plików
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Wniosek

Gratulacje! Pomyślnie zastosowałeś materiały do kostki 3D przy użyciu Aspose.3D dla Java. Ta prosta, ale potężna technika może wynieść Twoje projekty 3D na nowy poziom, zapewniając realistyczne i oszałamiające wizualnie wrażenia.

## Często zadawane pytania

### P1: Czy mogę zastosować wiele materiałów do jednego obiektu 3D?

Odpowiedź 1: Tak, Aspose.3D pozwala na zastosowanie wielu materiałów do różnych części obiektu 3D w celu lepszego dostosowania.

### P2: Jakie formaty plików obsługuje Aspose.3D do zapisywania scen?

 O2: Aspose.3D obsługuje różne formaty plików, w tym FBX, STL i 3DS. Patrz[dokumentacja](https://reference.aspose.com/3d/java/) dla pełnej listy.

### P3: Czy dostępna jest tymczasowa licencja na Aspose.3D dla Java?

 A3: Tak, możesz uzyskać[licencja tymczasowa](https://purchase.aspose.com/temporary-license/) w celach ewaluacyjnych.

### P4: Gdzie mogę znaleźć wsparcie dla Aspose.3D?

 A4: Odwiedź[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) za wsparcie społeczności i dyskusje.

### P5: Czy mogę pobrać bibliotekę Aspose.3D z określonego łącza?

 O5: Tak, użyj[link do pobrania](https://releases.aspose.com/3d/java/) aby uzyskać dostęp do najnowszej wersji Aspose.3D dla Java.