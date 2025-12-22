---
date: 2025-12-22
description: Dowiedz się, jak wyeksportować scenę do formatu glTF w Javie przy użyciu
  Aspose.3D, jednocześnie aktualizując materiały 3D do PBR, aby uzyskać większy realizm.
linktitle: Export Scene to glTF in Java with Aspose.3D
second_title: Upgrade 3D Materials to PBR
title: Eksportuj scenę do glTF w Javie z Aspose.3D
url: /pl/java/load-and-save/upgrade-materials-to-pbr/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Eksportuj scenę do glTF w Javie z Aspose.3D – Ulepsz materiały do PBR

## Wprowadzenie

W tym samouczku nauczysz się, jak **eksportować scenę do glTF** w Javie z Aspose.3D, jednocześnie ulepszając swoje materiały 3D do Physically‑Based Rendering (PBR). Ulepszenie do PBR nadaje Twoim modelom znacznie bardziej realistyczny wygląd, a eksport do szeroko wspieranego formatu glTF 2.0 pozwala udostępniać te wysokiej jakości zasoby w różnych silnikach, przeglądarkach i platformach AR/VR. Przejdziemy przez wymagania wstępne, zaimportujemy niezbędne pakiety i rozłożymy każdy przykład krok po kroku, abyś mógł zastosować tę technikę w własnych projektach.

## Szybkie odpowiedzi
- **Co oznacza „export scene to glTF”?** Konwertuje scenę Aspose.3D do formatu pliku glTF 2.0, zachowując geometrię, materiały i hierarchię.  
- **Dlaczego najpierw ulepszyć materiały do PBR?** Materiały PBR mapują się bezpośrednio na workflow metaliczno‑szorstkości glTF, zapewniając realistyczne oświetlenie bez dodatkowych kroków konwersji.  
- **Czy potrzebna jest licencja do uruchomienia kodu?** Darmowa wersja próbna wystarcza do rozwoju; licencja komercyjna jest wymagana w produkcji.  
- **Jakie IDE Java są obsługiwane?** Każde IDE, które potrafi kompilować Javę (Eclipse, IntelliJ IDEA, VS Code, itp.).  
- **Czy mogę eksportować duże sceny?** Tak, Aspose.3D strumieniuje dane efektywnie; wystarczy zapewnić wystarczającą pamięć heap dla bardzo dużych modeli.

## Co to jest „export scene to glTF”?

Eksportowanie sceny do glTF oznacza serializację całej sceny 3D — w tym siatek, węzłów, kamer, świateł i materiałów — do formatu GL Transmission Format (glTF). glTF jest otwartym standardem zoptymalizowanym pod renderowanie w czasie rzeczywistym, co czyni go idealnym do użycia w sieci, na urządzeniach mobilnych i w silnikach gier.

## Dlaczego przed eksportem ulepszyć materiały do PBR?

Materiały PBR (Physically‑Based Rendering) opisują, jak światło oddziałuje z powierzchniami przy użyciu parametrów takich jak albedo, metaliczność i szorstkość. glTF 2.0 natywnie obsługuje PBR, więc konwersja materiałów Phong lub własnych do PBR zapewnia, że kolory, odbicia i cieniowanie będą wyglądały poprawnie po załadowaniu modelu w dowolnym przeglądarce kompatybilnej z glTF.

## Wymagania wstępne

1. **Aspose.3D for Java** – pobierz go ze [strony wydania](https://releases.aspose.com/3d/java/).  
2. **Środowisko programistyczne Java** – JDK 8 lub wyższy oraz wybrane IDE.  
3. **Katalog dokumentów** – folder na twoim komputerze, w którym będziesz odczytywać/zapisywać pliki 3D.

## Importowanie pakietów

Add the core Aspose.3D namespace to your project:

```java
import com.aspose.threed.*;
```

Ten pojedynczy import daje dostęp do `Scene`, `Box`, `PhongMaterial`, `PbrMaterial`, `GltfSaveOptions` oraz API konwersji materiałów.

## Krok 1: Inicjalizacja nowej sceny 3D

Create a fresh scene that will hold your geometry and materials:

```java
// ExStart:InitializeScene
String MyDir = "Your Document Directory";
Scene s = new Scene();
// ExEnd:InitializeScene
```

> **Wskazówka:** Trzymaj `MyDir` jako ścieżkę bezwzględną podczas rozwoju, aby uniknąć błędów „plik nie znaleziony”.

## Krok 2: Utwórz sześcian z PhongMaterial

We’ll start with a simple box that uses a classic Phong material. This will later be converted to a PBR material during export:

```java
// ExStart:CreateBoxWithMaterial
Box box = new Box();
PhongMaterial mat = new PhongMaterial();
mat.setDiffuseColor(new Vector3(1, 0, 1));
s.getRootNode().createChildNode("box1", box).setMaterial(mat);
// ExEnd:CreateBoxWithMaterial
```

> **Dlaczego Phong?** PhongMaterial jest łatwy do skonfigurowania i demonstruje, jak działa logika konwersji.

## Krok 3: Zapisz w formacie GLTF 2.0 (Export Scene to glTF)

Configure the GLTF save options to automatically convert any `PhongMaterial` to a `PbrMaterial`. This is the core of **export scene to glTF**:

```java
// ExStart:SaveInGLTF
GltfSaveOptions opt = new GltfSaveOptions(FileFormat.GLTF2);
opt.setMaterialConverter(new MaterialConverter() {
    @Override
    public Material call(Material material) {
        PhongMaterial m = (PhongMaterial) material;
        PbrMaterial ret = new PbrMaterial();
        ret.setAlbedo(m.getDiffuseColor());
        return ret;
    }
});
s.save(MyDir + "Non_PBRtoPBRMaterial_Out.gltf", opt);
// ExEnd:SaveInGLTF
```

Gdy ten kod zostanie uruchomiony, scena zostanie zapisana do `Non_PBRtoPBRMaterial_Out.gltf`. Niestandardowy `MaterialConverter` zapewnia, że materiał Phong zostaje przekształcony w materiał PBR, dzięki czemu powstały plik glTF wyświetla się z realistycznym cieniowaniem w dowolnej przeglądarce glTF.

## Typowe problemy i rozwiązania

| Problem | Rozwiązanie |
|-------|----------|
| **FileNotFoundException** podczas zapisu | Sprawdź, czy `MyDir` wskazuje istniejący folder i czy aplikacja ma uprawnienia do zapisu. |
| **ClassCastException** w konwerterze | Upewnij się, że materiał przekazywany do konwertera jest rzeczywiście `PhongMaterial`. Dodaj sprawdzenie `instanceof`, jeśli mieszane są typy materiałów. |
| **Missing textures** po eksporcie | glTF oczekuje, że tekstury będą dostarczone osobno; dodaj obsługę tekstur w konwerterze w razie potrzeby. |

## Najczęściej zadawane pytania

**Q:** Czy Aspose.3D jest kompatybilny z innymi środowiskami programistycznymi Java niż Eclipse?  
**A:** Tak, Aspose.3D działa z dowolnym IDE Java, w tym IntelliJ IDEA, NetBeans i VS Code.

**Q:** Czy mogę używać Aspose.3D w projektach komercyjnych?  
**A:** Tak, możesz używać Aspose.3D zarówno w projektach prywatnych, jak i komercyjnych. Odwiedź [stronę zakupu](https://purchase.aspose.com/buy) po szczegóły licencjonowania.

**Q:** Czy dostępna jest darmowa wersja próbna?  
**A:** Tak, darmową wersję próbną możesz uzyskać [tutaj](https://releases.aspose.com/).

**Q:** Gdzie mogę znaleźć wsparcie dla Aspose.3D?  
**A:** Przeglądaj [forum Aspose.3D](https://forum.aspose.com/c/3d/18) w celu uzyskania wsparcia społeczności.

**Q:** Jak uzyskać tymczasową licencję na Aspose.3D?  
**A:** Odwiedź [ten link](https://purchase.aspose.com/temporary-license/) po informacje o tymczasowej licencji.

## Podsumowanie

Postępując zgodnie z powyższymi krokami, teraz wiesz, jak **eksportować scenę do glTF** w Javie przy użyciu Aspose.3D, automatycznie ulepszając materiały Phong do PBR. Ten przepływ pracy pozwala tworzyć wysokiej jakości, fizycznie oparte zasoby gotowe do nowoczesnych pipeline'ów renderingu, przeglądarek internetowych oraz doświadczeń AR/VR. Eksperymentuj z bardziej złożonymi geometriami, teksturami i oświetleniem, aby w pełni wykorzystać moc PBR i glTF.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2025-12-22  
**Tested With:** Aspose.3D 24.12 for Java  
**Author:** Aspose  

---