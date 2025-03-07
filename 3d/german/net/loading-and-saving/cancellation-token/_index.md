---
title: Verwenden von CancellationToken
linktitle: Verwenden von CancellationToken
second_title: Aspose.3D .NET API
description: Entdecken Sie die nahtlose Welt der 3D-Modellierung mit Aspose.3D für .NET. Erfahren Sie, wie Sie 3D-Dokumente mit CancellationToken effizient laden und speichern.
weight: 10
url: /de/net/loading-and-saving/cancellation-token/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Verwenden von CancellationToken

## Einführung

Willkommen zu unserem umfassenden Leitfaden zur Verwendung von Aspose.3D für .NET zur Verbesserung Ihrer 3D-Modellierungs- und Rendering-Projekte. Aspose.3D ist eine leistungsstarke Bibliothek, die .NET-Entwicklern die nahtlose Arbeit mit 3D-Dateien ermöglicht. In diesem Tutorial befassen wir uns mit den Lade- und Speicheraspekten und konzentrieren uns dabei insbesondere auf die Verwendung von CancellationToken für die effiziente Verwaltung asynchroner Aufgaben.

## Voraussetzungen

Bevor wir uns auf diese Reise begeben, stellen Sie sicher, dass Sie über die folgenden Voraussetzungen verfügen:

-  Aspose.3D für .NET: Laden Sie die Bibliothek herunter und installieren Sie sie[Hier](https://releases.aspose.com/3d/net/).
- .NET-Umgebung: Stellen Sie sicher, dass Sie eine kompatible .NET-Entwicklungsumgebung eingerichtet haben.
- Grundkenntnisse von C#: Vertrautheit mit der Programmiersprache C# wird empfohlen.

## Namespaces importieren

Stellen Sie zunächst sicher, dass Sie die erforderlichen Namespaces in Ihr Projekt aufnehmen. Diese Namespaces bieten Zugriff auf die für die 3D-Dateibearbeitung erforderlichen Funktionen.

```csharp
using Aspose.ThreeD;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
```

## Laden und Speichern – Verwenden von CancellationToken

### Schritt 1: Erstellen Sie eine CancellationTokenSource

```csharp
// ExStart:CancellationTokenSource

CancellationTokenSource cts = new CancellationTokenSource();
```

Hier instanziieren wir eine CancellationTokenSource, eine entscheidende Komponente für die Verwaltung des Abbruchs bei asynchronen Vorgängen.

### Schritt 2: 3D-Szene initialisieren

```csharp
Scene scene = new Scene();
```

Erstellen Sie eine Instanz der Scene-Klasse. Dies wird die Leinwand für Ihre 3D-Modellierungsaktivitäten sein.

### Schritt 3: Legen Sie das CancellationToken-Timeout fest

```csharp
cts.CancelAfter(1000);
```

 Legen Sie das Abbruch-Timeout mit fest`CancelAfter` Methode. In diesem Beispiel ist das Timeout auf 1000 Millisekunden (1 Sekunde) eingestellt.

### Schritt 4: Öffnen Sie das 3D-Dokument

```csharp
try
{
    scene.Open("Your Output Directory" + "document.fbx", cts.Token);
    Console.WriteLine("Import is done within 1000ms");
}
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
```

 Versuchen Sie, das 3D-Dokument innerhalb des angegebenen Zeitrahmens zu öffnen. Der`cts.Token` Der Parameter stellt sicher, dass der Vorgang abgebrochen werden kann, wenn er das eingestellte Timeout überschreitet.

### Schritt 5: Importausnahme behandeln

Behandeln Sie eine ImportException ordnungsgemäß, indem Sie prüfen, ob sie durch eine OperationCanceledException verursacht wurde.

```csharp
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
// ExEnd:CancellationTokenSource
```

## Abschluss

Glückwunsch! Sie haben den Prozess der Verwendung von Aspose.3D für .NET mit CancellationToken zum Verwalten des Ladens von 3D-Dokumenten erfolgreich durchlaufen. Diese Technik gewährleistet effiziente und zeitnahe Importvorgänge und verbessert die Gesamtleistung Ihrer 3D-Anwendungen.

## FAQs

### F1: Ist Aspose.3D mit allen 3D-Dateiformaten kompatibel?

 A1: Aspose.3D unterstützt eine Vielzahl von 3D-Dateiformaten, darunter FBX, STL, OBJ und mehr. Siehe die[Dokumentation](https://reference.aspose.com/3d/net/) für die vollständige Liste.

### F2: Wie kann ich eine temporäre Lizenz für Aspose.3D erhalten?

 A2: Besorgen Sie sich durch einen Besuch eine temporäre Lizenz[dieser Link](https://purchase.aspose.com/temporary-license/).

### F3: Wo finde ich Unterstützung für Aspose.3D?

 A3: Beteiligen Sie sich an der Community-Diskussion im[Aspose.3D-Forum](https://forum.aspose.com/c/3d/18).

### F4: Kann ich Aspose.3D vor dem Kauf kostenlos testen?

 A4: Ja, entdecken Sie die Funktionen mit einer kostenlosen Testversion[Hier](https://releases.aspose.com/).

### F5: Was ist die neueste Version von Aspose.3D für .NET?

 A5: Bleiben Sie auf dem Laufenden, indem Sie die überprüfen[Download-Seite](https://releases.aspose.com/3d/net/) für die neueste Version.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
