---
date: 2025-12-01
description: Naucz się zmieniać kolor tekstury, uzyskiwać dostęp do właściwości materiału,
  ustawiać wartości Vector3 oraz pobierać właściwości po nazwie w scenach Java z Aspose.3D
  – kompletny samouczek Aspose 3D.
language: pl
linktitle: Change texture color and manage 3D properties in Java scenes using Aspose.3D
second_title: Aspose.3D Java API
title: Zmieniaj kolor tekstury i zarządzaj właściwościami 3D w scenach Java przy użyciu
  Aspose.3D
url: /java/3d-scenes-and-models/managing-3d-properties-scenes/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Zmieniaj kolor tekstury i zarządzaj właściwościami 3D w scenach Java przy użyciu Aspose.3D

## Wprowadzenie

W tym **samouczku Aspose 3D** odkryjesz, jak **zmienić kolor tekstury** oraz pracować z właściwościami 3D i danymi niestandardowymi w scenach Java. Niezależnie od tego, czy tworzysz grę, wizualizator produktów, czy przeglądarkę naukową, możliwość modyfikacji atrybutów materiału w czasie rzeczywistym daje pełną kontrolę artystyczną. Przejdźmy krok po kroku od załadowania sceny po dostosowanie koloru *Diffuse* przy użyciu wartości `Vector3`.

## Szybkie odpowiedzi
- **Co mogę modyfikować?** Możesz zmienić kolor tekstury, przezroczystość, połysk oraz dowolną własną właściwość przypisaną do materiału.  
- **Która klasa przechowuje dane?** `Material` oraz jego `PropertyCollection`.  
- **Jak ustawić nowy kolor?** Użyj `props.set("Diffuse", new Vector3(r, g, b))`.  
- **Czy potrzebna jest licencja?** Licencja tymczasowa działa w trybie ewaluacyjnym; pełna licencja jest wymagana w produkcji.  
- **Obsługiwane formaty?** FBX, OBJ, STL, GLTF i wiele innych.

## Wymagania wstępne

- Zainstalowany Java Development Kit (JDK) 8 lub nowszy.  
- Biblioteka Aspose.3D for Java (pobierz z [strony Aspose](https://releases.aspose.com/3d/java/)).  
- Podstawowa znajomość składni Java oraz koncepcji programowania obiektowego.

## Importowanie pakietów

Zanim napiszesz jakąkolwiek logikę, zaimportuj klasy, które dają dostęp do właściwości materiału i manipulacji wektorami.

```java
import java.io.IOException;

import com.aspose.threed.Material;
import com.aspose.threed.Property;
import com.aspose.threed.PropertyCollection;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;
```

### Dlaczego importować te klasy?

- `Scene` ładuje i reprezentuje plik 3D.  
- `Material` definiuje powierzchnię (tekstury, kolory itp.).  
- `PropertyCollection` jest kontenerem podobnym do słownika, który pozwala **dostępować do właściwości materiału** po nazwie.  
- `Vector3` jest typem danych używanym dla kolorów i innych wektorów trzy‑składowych.

## Krok 1: Inicjalizacja sceny

```java
String dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
```

Tworzymy obiekt `Scene`, ładując plik FBX, który już zawiera teksturę. To jest płótno, na którym **zmienimy kolor tekstury**.

## Krok 2: Dostęp do właściwości materiału

```java
Material material = scene.getRootNode().getChildNodes().get(0).getMaterial();
PropertyCollection props = material.getProperties();
```

Tutaj **dostęp do właściwości materiału** pierwszej siatki w scenie. Obiekt `Material` zawiera `PropertyCollection`, który przechowuje każdy konfigurowalny atrybut, taki jak *Diffuse*, *Specular* oraz dane użytkownika.

## Krok 3: Wyświetlenie wszystkich właściwości

```java
for (Property prop : props) {
    System.out.println("Name" + prop.getName() + " Value = " + prop.getValue());
}
```

Iterowanie po `props` wypisuje każdą nazwę właściwości i jej bieżącą wartość. Ten szybki inwentarz pomaga odkryć, które klucze można później modyfikować, np. `"Diffuse"` dla podstawowego koloru.

## Krok 4: Ustawienie wartości Vector3 w celu zmiany koloru tekstury

```java
props.set("Diffuse", new Vector3(1, 0, 1));
```

**Pro tip:** Konstruktor `Vector3` przyjmuje trzy liczby zmiennoprzecinkowe reprezentujące **czerwony, zielony i niebieski** (zakres 0‑1). Ustawienie `(1, 0, 1)` zmienia podstawowy kolor tekstury na magentę, skutecznie **zmieniając kolor tekstury** modelu.

## Krok 5: Pobranie właściwości po nazwie

```java
Object diffuse = (Vector3) props.get("Diffuse");
System.out.println(diffuse);
```

To pokazuje **pobranie właściwości po nazwie**. Rzutujemy zwrócony `Object` na `Vector3`, aby programowo pracować z kolorem.

## Krok 6: Dostęp do instancji właściwości

```java
Property pdiffuse = props.findProperty("Diffuse");
System.out.println(pdiffuse);
```

`findProperty` zwraca pełny obiekt `Property`, dając dostęp do metadanych, takich jak typ właściwości, etykieta i wszelkie dołączone dane niestandardowe.

## Krok 7: Przeglądanie pod‑właściwości właściwości

```java
for (Property pp : pdiffuse.getProperties()) {
    System.out.println("Diffuse. " + pp.getName() + " = " + pp.getValue());
}
```

Niektóre właściwości są hierarchiczne. Przeglądanie `pdiffuse.getProperties()` pokazuje wszelkie zagnieżdżone atrybuty (np. współrzędne tekstury, klucze animacji), które należą do wpisu *Diffuse*.

## Typowe problemy i rozwiązania

| Problem | Dlaczego występuje | Rozwiązanie |
|-------|----------------|-----|
| **`NullPointerException` on `material`** | Węzeł może nie mieć przypisanego materiału. | Wywołaj `node.setMaterial(new Material())` przed dostępem do właściwości. |
| **Color does not change** | Model używa tekstury, która nadpisuje kolor *Diffuse*. | Wyłącz teksturę lub zmodyfikuj bezpośrednio obraz tekstury. |
| **`ClassCastException` when retrieving** | Próba rzutowania właściwości, która nie jest typu Vector3. | Zweryfikuj typ właściwości przy pomocy `pdiffuse.getValue().getClass()` przed rzutowaniem. |

## Najczęściej zadawane pytania

**Q: Jak mogę zainstalować bibliotekę Aspose.3D w moim projekcie Java?**  
A: Pobierz plik JAR z [strony Aspose](https://releases.aspose.com/3d/java/) i dodaj go do classpath projektu lub zależności Maven/Gradle.

**Q: Czy dostępne są darmowe wersje próbne Aspose.3D?**  
A: Tak, w pełni funkcjonalna 30‑dniowa wersja próbna jest dostępna na [stronie darmowej wersji próbnej Aspose](https://releases.aspose.com/).

**Q: Gdzie znajdę szczegółową dokumentację Aspose.3D dla Java?**  
A: Oficjalna referencja API znajduje się pod adresem [Aspose.3D documentation](https://reference.aspose.com/3d/java/).

**Q: Czy istnieje forum wsparcia dla Aspose.3D, gdzie mogę zadawać pytania?**  
A: Oczywiście — odwiedź [forum wsparcia Aspose.3D](https://forum.aspose.com/c/3d/18), aby połączyć się ze społecznością i ekspertami.

**Q: Jak mogę uzyskać tymczasową licencję dla Aspose.3D?**  
A: Poproś o nią na [stronie tymczasowej licencji](https://purchase.aspose.com/temporary-license/) na witrynie Aspose.

**Q: Czy mogę zmieniać inne atrybuty materiału oprócz koloru?**  
A: Tak, właściwości takie jak `Specular`, `Opacity` oraz dane użytkownika można modyfikować przy użyciu tego samego wzorca `props.set`.

## Zakończenie

Nauczyłeś się teraz, jak **zmienić kolor tekstury**, **dostępować do właściwości materiału**, **ustawić wartość Vector3** oraz **pobrać właściwość po nazwie** w scenie Java przy użyciu Aspose.3D. Te techniki dają precyzyjną kontrolę nad dowolnym zasobem 3D, umożliwiając dynamiczne efekty wizualne i dostosowanie w czasie działania aplikacji.

---

**Last Updated:** 2025-12-01  
**Tested With:** Aspose.3D for Java 24.11  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}