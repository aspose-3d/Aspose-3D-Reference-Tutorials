---
title: Ladda och spara - Skapa ett tomt 3D-dokument
linktitle: Ladda och spara - Skapa ett tomt 3D-dokument
second_title: Aspose.3D .NET API
description: Utforska världen av 3D-dokumentskapande med Aspose.3D för .NET. Skapa, redigera och spara fantastiska 3D-scener utan ansträngning.
type: docs
weight: 11
url: /sv/net/loading-and-saving/create-empty-3d-document/
---
## Introduktion

Välkommen till en värld av 3D-dokumentskapande med Aspose.3D för .NET! I den här handledningen kommer vi att utforska grunderna för att ladda och spara 3D-dokument. Aspose.3D för .NET tillhandahåller en kraftfull uppsättning verktyg för att arbeta med 3D-scener, och vi guidar dig genom varje steg för att hjälpa dig komma igång smidigt.

## Förutsättningar

Innan vi dyker in i handledningen, se till att du har följande förutsättningar på plats:

-  Aspose.3D för .NET: Se till att du har biblioteket installerat. Du kan ladda ner den från[här](https://releases.aspose.com/3d/net/).

## Importera namnområden

Börja med att importera de nödvändiga namnrymden i ditt .NET-projekt:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## Ladda och spara - Skapa ett tomt 3D-dokument

### Steg 1: Konfigurera din utdatakatalog

```csharp
// Sökvägen till dokumentkatalogen.
var output = "Your Output Directory" + "document.fbx";
```

### Steg 2: Skapa ett tomt 3D-dokument

```csharp
// ExStart:CreateEmpty3DDocument

// Skapa ett objekt av klassen Scene
Scene scene = new Scene();

// Spara 3D-scendokumentet i FBX-format
scene.Save(output, FileFormat.FBX7500ASCII);

// ExEnd:CreateEmpty3DDocument
```

### Steg 3: Visa resultatet

```csharp
Console.WriteLine("\nAn empty 3D document created successfully.\nFile saved at " + output);
```

Grattis! Du har precis skapat ditt första tomma 3D-dokument med Aspose.3D för .NET. Utforska gärna fler funktioner och funktioner för att frigöra den fulla potentialen i detta bibliotek.

## Slutsats

 I den här handledningen täckte vi grunderna för att skapa ett tomt 3D-dokument med Aspose.3D för .NET. När du fortsätter din resa med 3D-utveckling, se[dokumentation](https://reference.aspose.com/3d/net/) för djupgående insikter och avancerade funktioner.

## FAQ's

### F1: Är Aspose.3D för .NET lämplig för nybörjare?

S1: Ja, Aspose.3D för .NET tillhandahåller ett användarvänligt gränssnitt, vilket gör det tillgängligt för både nybörjare och erfarna utvecklare.

### F2: Kan jag prova Aspose.3D för .NET innan jag köper?

 A2: Absolut! Du kan få tillgång till en gratis provperiod[här](https://releases.aspose.com/).

### F3: Hur kan jag få support för Aspose.3D för .NET?

 A3: Besök[Aspose.3D-forum](https://forum.aspose.com/c/3d/18) att söka hjälp och få kontakt med samhället.

### F4: Finns tillfälliga licenser tillgängliga för Aspose.3D för .NET?

 A4: Ja, du kan få en tillfällig licens[här](https://purchase.aspose.com/temporary-license/).

### F5: Var kan jag köpa Aspose.3D för .NET?

 A5: Du kan köpa biblioteket[här](https://purchase.aspose.com/buy).