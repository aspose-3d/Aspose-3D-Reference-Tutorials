---
title: Laddar och sparar - Använder CancellationToken
linktitle: Laddar och sparar - Använder CancellationToken
second_title: Aspose.3D .NET API
description: Utforska den sömlösa världen av 3D-modellering med Aspose.3D för .NET. Lär dig att ladda och spara 3D-dokument effektivt med CancellationToken.
type: docs
weight: 10
url: /sv/net/loading-and-saving/cancellation-token/
---
## Introduktion

Välkommen till vår omfattande guide om hur du använder Aspose.3D för .NET för att förbättra dina 3D-modellerings- och renderingsprojekt. Aspose.3D är ett kraftfullt bibliotek som ger .NET-utvecklare möjlighet att sömlöst arbeta med 3D-filer. I den här handledningen kommer vi att fördjupa oss i laddnings- och sparaspekterna, speciellt med fokus på användningen av CancellationToken för effektiv hantering av asynkrona uppgifter.

## Förutsättningar

Innan vi ger oss ut på denna resa, se till att du har följande förutsättningar på plats:

-  Aspose.3D för .NET: Ladda ner och installera biblioteket från[här](https://releases.aspose.com/3d/net/).
- .NET-miljö: Se till att du har en kompatibel .NET-utvecklingsmiljö inställd.
- Grundläggande förståelse för C#: Bekantskap med programmeringsspråket C# rekommenderas.

## Importera namnområden

För att komma igång, se till att du inkluderar de nödvändiga namnrymden i ditt projekt. Dessa namnutrymmen ger tillgång till de funktioner som behövs för 3D-filmanipulation.

```csharp
using Aspose.ThreeD;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
```

## Laddar och sparar - Använder CancellationToken

### Steg 1: Skapa CancellationTokenSource

```csharp
// ExStart:CancellationTokenSource

CancellationTokenSource cts = new CancellationTokenSource();
```

Här instansierar vi en CancellationTokenSource, en avgörande komponent för att hantera avbokning i asynkrona operationer.

### Steg 2: Initiera 3D-scen

```csharp
Scene scene = new Scene();
```

Skapa en instans av klassen Scene. Detta kommer att vara duken för dina 3D-modelleringsaktiviteter.

### Steg 3: Ställ in CancellationToken Timeout

```csharp
cts.CancelAfter(1000);
```

 Ställ in tidsgränsen för avbokning med hjälp av`CancelAfter` metod. I det här exemplet är timeout satt till 1000 millisekunder (1 sekund).

### Steg 4: Öppna 3D-dokument

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

 Försök att öppna 3D-dokumentet inom den angivna tidsramen. De`cts.Token`parametern säkerställer att operationen kan avbrytas om den överskrider den inställda timeouten.

### Steg 5: Hantera importundantag

I händelse av ett ImportException, hantera det graciöst genom att kontrollera om det orsakades av ett OperationCanceledException.

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

## Slutsats

Grattis! Du har framgångsrikt navigerat genom processen att använda Aspose.3D för .NET med CancellationToken för att hantera inläsningen av 3D-dokument. Denna teknik säkerställer effektiva och snabba importoperationer, vilket förbättrar den övergripande prestandan för dina 3D-applikationer.

## FAQ's

### F1: Är Aspose.3D kompatibel med alla 3D-filformat?

 S1: Aspose.3D stöder ett brett utbud av 3D-filformat, inklusive FBX, STL, OBJ och mer. Referera till[dokumentation](https://reference.aspose.com/3d/net/) för hela listan.

### F2: Hur kan jag få en tillfällig licens för Aspose.3D?

 A2: Skaffa en tillfällig licens genom att besöka[den här länken](https://purchase.aspose.com/temporary-license/).

### F3: Var kan jag hitta support för Aspose.3D?

 S3: Gå med i samhällsdiskussionen på[Aspose.3D-forum](https://forum.aspose.com/c/3d/18).

### F4: Kan jag prova Aspose.3D gratis innan jag köper?

 S4: Ja, utforska funktionerna med en gratis provperiod tillgänglig[här](https://releases.aspose.com/).

### F5: Vilken är den senaste versionen av Aspose.3D för .NET?

 S5: Håll dig uppdaterad genom att kontrollera[nedladdningssida](https://releases.aspose.com/3d/net/) för den senaste utgåvan.