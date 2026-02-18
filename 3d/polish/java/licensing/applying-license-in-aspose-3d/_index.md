---
date: 2026-02-14
description: Dowiedz się, jak ustawić licencję Aspose w Aspose.3D dla Javy, w tym
  jak zastosować licencję z pliku i ustawić klucze publiczne i prywatne.
linktitle: How to Set Aspose License in Aspose.3D for Java
second_title: Aspose.3D Java API
title: Jak ustawić licencję Aspose w Aspose.3D dla Javy
url: /pl/java/licensing/applying-license-in-aspose-3d/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak ustawić licencję Aspose w Aspose.3D dla Java

## Wprowadzenie

W tym obszernej poradniku dowiesz się **jak ustawić licencję Aspose** dla Aspose.3D w środowisku Java. Niezależnie od tego, czy wolisz ładować plik licencji, przesyłać go jako strumień, czy używać licencjonowania metrowego z kluczami publicznym i prywatnym, przeprowadzimy Cię krok po kroku przez każde podejście, abyś mógł szybko i pewnie odblokować pełny zestaw funkcji Aspose.3D.

## Szybkie odpowiedzi
- **Jaki jest podstawowy sposób ustawienia licencji Aspose.3D?** Użyj klasy `License` i wywołaj `setLicense` z ścieżką do pliku lub strumieniem.  
- **Czy mogę załadować licencję ze strumienia?** Tak – opakuj plik `.lic` w `FileInputStream` i przekaż go do `setLicense`.  
- **Co zrobić, jeśli potrzebuję licencji metrowej?** Zainicjalizuj obiekt `Metered` i wywołaj `setMeteredKey` z Twoimi kluczami publicznym i prywatnym.  
- **Czy potrzebuję licencji dla wersji deweloperskich?** Wymagana jest licencja próbna lub tymczasowa dla każdego scenariusza nie‑ewaluacyjnego.  
- **Jakie wersje Java są obsługiwane?** Aspose.3D działa z Java 6 i nowszymi.

## Wymagania wstępne

Zanim zaczniemy, upewnij się, że masz następujące wymagania:

- Podstawowa znajomość programowania w Javie.  
- Zainstalowana biblioteka Aspose.3D. Możesz ją pobrać ze [strony wydania](https://releases.aspose.com/3d/java/).  

## Importowanie pakietów

Aby rozpocząć, zaimportuj niezbędne pakiety do swojego projektu Java. Upewnij się, że Aspose.3D jest dodane do classpath. Oto przykład:

```java
import com.aspose.threed.License;
import com.aspose.threed.Metered;

import java.io.FileInputStream;
import java.io.IOException;
```

## Stosowanie licencji przy użyciu pliku

### Krok 1: Utwórz obiekt License

Najpierw utwórz obiekt `License` w swoim kodzie Java.

```java
License license = new License();
```

### Krok 2: Zastosuj licencję z pliku

Określ ścieżkę do pliku licencji i ustaw licencję przy użyciu poniższego kodu. To pokazuje technikę **zastosowania licencji z pliku**.

```java
license.setLicense("Aspose._3D.lic");
```

## Stosowanie licencji przy użyciu obiektu strumienia

### Krok 1: Utwórz obiekt License

Podobnie, utwórz obiekt `License` w swoim kodzie Java.

```java
License license = new License();
```

### Krok 2: Ustaw licencję z obiektu strumienia

Użyj `FileInputStream`, aby utworzyć strumień i ustawić licencję:

```java
try (FileInputStream myStream = new FileInputStream("Aspose._3D.lic")) {
    license.setLicense(myStream);
}
```

## Używanie kluczy publicznego i prywatnego do licencjonowania metrowego

### Krok 1: Zainicjalizuj obiekt licencji Metered

Zainicjalizuj obiekt licencji `Metered`:

```java
Metered metered = new Metered();
```

### Krok 2: Ustaw klucze publiczny i prywatny

Ustaw swoje klucze publiczny i prywatny, aby włączyć licencjonowanie metrowe. To obejmuje scenariusz **ustawiania kluczy publicznego i prywatnego**.

```java
metered.setMeteredKey("your-public-key", "your-private-key");
```

## Dlaczego ustawienie licencji ma znaczenie

Zastosowanie właściwej licencji usuwa znaki wodne wersji ewaluacyjnej, odblokowuje formaty plików premium i zapewnia zgodność z modelem licencjonowania Aspose. Użycie odpowiedniej metody (plik, strumień lub metrowa) pozwala płynnie zintegrować licencjonowanie z potokami CI/CD, wdrożeniami w chmurze lub aplikacjami desktopowymi.

## Typowe problemy i wskazówki

- **Plik nie znaleziony** – Sprawdź, czy ścieżka do pliku `.lic` jest poprawna względem katalogu roboczego lub użyj ścieżki bezwzględnej.  
- **Strumień zamknięty przedwcześnie** – Podczas używania strumienia, utrzymuj obiekt `License` aktywny przez cały czas działania aplikacji; licencja jest buforowana po pierwszym udanym wywołaniu.  
- **Niezgodność klucza metrowego** – Sprawdź dwukrotnie, czy klucze publiczny i prywatny odpowiadają tej samej licencji metrowej; literówka spowoduje wyjątek w czasie wykonywania.  
- **Porada:** Przechowuj plik licencji w bezpiecznej lokalizacji poza drzewem źródłowym i ładuj go za pomocą zmiennej środowiskowej, aby uniknąć jego zatwierdzania do kontroli wersji.

## Podsumowanie

Gratulacje! Pomyślnie nauczyłeś się **jak ustawić licencję Aspose** w Aspose.3D dla Java, używając różnych metod, w tym stosowania licencji z pliku, przesyłania jej jako strumienia oraz konfigurowania licencjonowania metrowego z kluczami publicznym i prywatnym. Teraz możesz płynnie zintegrować Aspose.3D ze swoimi aplikacjami Java i w pełni wykorzystać jego możliwości przetwarzania 3D.

## Najczęściej zadawane pytania

**P: Czy Aspose.3D jest kompatybilny ze wszystkimi wersjami Java?**  
O: Tak, Aspose.3D jest kompatybilny z Java 6 i nowszymi wersjami.

**P: Gdzie mogę znaleźć dodatkową dokumentację?**  
O: Możesz odwołać się do dokumentacji [tutaj](https://reference.aspose.com/3d/java/).

**P: Czy mogę wypróbować Aspose.3D przed zakupem?**  
O: Tak, możesz wypróbować darmową wersję próbną [tutaj](https://releases.aspose.com/).

**P: Jak mogę uzyskać wsparcie dla Aspose.3D?**  
O: Odwiedź [Forum Aspose.3D](https://forum.aspose.com/c/3d/18), aby uzyskać pomoc.

**P: Czy potrzebuję tymczasowej licencji do testów?**  
O: Tak, uzyskaj tymczasową licencję [tutaj](https://purchase.aspose.com/temporary-license/).

**P: Jaka jest różnica między licencją plikową a licencją metrową?**  
O: Licencja plikowa to statyczny plik `.lic` powiązany z określoną wersją produktu, natomiast licencja metrowa weryfikuje użycie w oparciu o usługę metrowania w chmurze Aspose przy użyciu kluczy publicznego i prywatnego.

**P: Czy mogę osadzić kod ładowania licencji w inicjalizatorze statycznym?**  
O: Oczywiście – umieszczenie inicjalizacji `License` w bloku static zapewnia, że licencja zostanie zastosowana raz, gdy klasa zostanie po raz pierwszy załadowana.

---

**Ostatnia aktualizacja:** 2026-02-14  
**Testowano z:** Aspose.3D 24.11 for Java  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}