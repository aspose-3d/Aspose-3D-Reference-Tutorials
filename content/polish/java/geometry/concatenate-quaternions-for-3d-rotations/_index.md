---
title: Łączenie kwaternionów dla obrotów 3D w Javie za pomocą Aspose.3D
linktitle: Łączenie kwaternionów dla obrotów 3D w Javie za pomocą Aspose.3D
second_title: Aspose.3D API Java
description: Dowiedz się, jak łączyć kwaterniony dla rotacji 3D w Javie przy użyciu Aspose.3D. Postępuj zgodnie z naszym przewodnikiem krok po kroku, aby uzyskać płynne transformacje animacji.
type: docs
weight: 11
url: /pl/java/geometry/concatenate-quaternions-for-3d-rotations/
---
## Wstęp

Konkatenacja kwaternionów to podstawowa koncepcja grafiki 3D, umożliwiająca płynne łączenie wielu transformacji obrotowych. Aspose.3D upraszcza ten proces w Javie, oferując wydajny i intuicyjny sposób obsługi operacji kwaternionów. W tym samouczku przeprowadzimy Cię przez proces łączenia kwaternionów i stosowania ich do obiektów 3D za pomocą Aspose.3D.

## Warunki wstępne

Przed przystąpieniem do samouczka upewnij się, że spełniasz następujące wymagania wstępne:

- Podstawowa znajomość programowania w języku Java.
-  Zainstalowano Aspose.3D dla Java. Możesz go pobrać[Tutaj](https://releases.aspose.com/3d/java/).

## Importuj pakiety

Pamiętaj, aby zaimportować niezbędne pakiety, aby wykorzystać funkcje Aspose.3D. Dołącz następujące wiersze do swojego kodu Java:

```java
import com.aspose.threed.*;
```

Podzielmy teraz przykładowy kod na wiele kroków, aby utworzyć kompleksowy samouczek:

## Krok 1: Ustaw scenę

```java
Scene scene = new Scene();
```

## Krok 2: Zdefiniuj kwaterniony

```java
Quaternion q1 = Quaternion.fromEulerAngle(Math.PI * 0.5, 0, 0);
Vector3.X_AXIS.x = 3;
Quaternion q2 = Quaternion.fromAngleAxis(-Math.PI * 0.5, Vector3.X_AXIS);
```

## Krok 3: Połącz kwaterniony

```java
Quaternion q3 = q1.concat(q2);
```

## Krok 4: Utwórz 3 cylindry

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

## Krok 5: Zapisz do pliku

```java
MyDir = MyDir + "test_out.fbx";
scene.save(MyDir, FileFormat.FBX7400ASCII);
// ExEnd:ConcatenateQuaternions
```

## Krok 6: Wydrukuj wiadomość o powodzeniu

```java
System.out.println("\nQuaternions concatenated successfully.\nFile saved at " + MyDir);
```

## Wniosek

Wykonując ten samouczek, nauczyłeś się łączyć kwaterniony dla rotacji 3D w Javie przy użyciu Aspose.3D. Eksperymentuj z różnymi kombinacjami kwaternionów, aby uzyskać różnorodne i precyzyjne rotacje w swoich projektach 3D.

## Często zadawane pytania

### P1: Czy mogę używać Aspose.3D dla Java za darmo?

 A1: Aspose.3D oferuje[bezpłatna wersja próbna](https://releases.aspose.com/) abyś mógł poznać jego funkcje. W przypadku długotrwałego użytkowania rozważ zakup:[licencja](https://purchase.aspose.com/buy).

### P2: Gdzie mogę znaleźć obszerną dokumentację dla Aspose.3D?

 A2:[dokumentacja](https://reference.aspose.com/3d/java/) zawiera szczegółowe informacje i przykłady, które pomogą Ci zacząć.

### P3: Jak mogę uzyskać wsparcie dla Aspose.3D?

 A3: Odwiedź[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) aby zadawać pytania, dzielić się doświadczeniami i uzyskać pomoc od społeczności.

### P4: Czy dostępne są licencje tymczasowe dla Aspose.3D?

 A4: Tak, możesz uzyskać[licencja tymczasowa](https://purchase.aspose.com/temporary-license/) do celów testowania i oceny.

### P5: Jakie formaty plików są obsługiwane przy zapisywaniu scen 3D?

O5: Aspose.3D obsługuje różne formaty i możesz zapisywać sceny w formacie FBX, jak pokazano w tym samouczku.