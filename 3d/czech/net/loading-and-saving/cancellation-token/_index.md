---
title: Použití CancellationToken
linktitle: Použití CancellationToken
second_title: Aspose.3D .NET API
description: Prozkoumejte bezproblémový svět 3D modelování s Aspose.3D pro .NET. Naučte se efektivně načítat a ukládat 3D dokumenty pomocí CancellationToken.
weight: 10
url: /cs/net/loading-and-saving/cancellation-token/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Použití CancellationToken

## Úvod

Vítejte v našem komplexním průvodci o využití Aspose.3D pro .NET k vylepšení vašich projektů 3D modelování a vykreslování. Aspose.3D je výkonná knihovna, která umožňuje vývojářům .NET bezproblémově pracovat s 3D soubory. V tomto tutoriálu se ponoříme do aspektů načítání a ukládání, konkrétně se zaměříme na použití CancellationToken pro efektivní správu asynchronních úloh.

## Předpoklady

Než se vydáme na tuto cestu, ujistěte se, že máte splněny následující předpoklady:

-  Aspose.3D for .NET: Stáhněte a nainstalujte knihovnu z[tady](https://releases.aspose.com/3d/net/).
- Prostředí .NET: Ujistěte se, že máte nastaveno kompatibilní vývojové prostředí .NET.
- Základní znalost C#: Doporučuje se znalost programovacího jazyka C#.

## Importovat jmenné prostory

Chcete-li začít, ujistěte se, že jste do projektu zahrnuli potřebné jmenné prostory. Tyto jmenné prostory budou poskytovat přístup k funkcím potřebným pro 3D manipulaci se soubory.

```csharp
using Aspose.ThreeD;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
```

## Načítání a ukládání – pomocí CancellationToken

### Krok 1: Vytvořte CancellationTokenSource

```csharp
// ExStart:CancellationTokenSource

CancellationTokenSource cts = new CancellationTokenSource();
```

Zde vytvoříme instanci CancellationTokenSource, klíčovou komponentu pro správu zrušení v asynchronních operacích.

### Krok 2: Inicializujte 3D scénu

```csharp
Scene scene = new Scene();
```

Vytvořte instanci třídy Scene. Toto bude plátno pro vaše aktivity 3D modelování.

### Krok 3: Nastavte časový limit CancellationToken

```csharp
cts.CancelAfter(1000);
```

 Nastavte časový limit zrušení pomocí`CancelAfter` metoda. V tomto příkladu je časový limit nastaven na 1000 milisekund (1 sekunda).

### Krok 4: Otevřete 3D dokument

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

 Pokuste se otevřít 3D dokument v určeném časovém rámci. The`cts.Token` Parametr zajišťuje, že operaci lze zrušit, pokud překročí nastavený časový limit.

### Krok 5: Ošetřete výjimku importu

V případě výjimky ImportException ji zpracujte elegantně kontrolou, zda byla způsobena výjimkou OperationCanceledException.

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

## Závěr

Gratulujeme! Úspěšně jste prošli procesem používání Aspose.3D for .NET s CancellationToken ke správě načítání 3D dokumentů. Tato technika zajišťuje efektivní a včasné operace importu a zvyšuje celkový výkon vašich 3D aplikací.

## FAQ

### Q1: Je Aspose.3D kompatibilní se všemi 3D formáty souborů?

 Odpověď 1: Aspose.3D podporuje širokou škálu formátů 3D souborů, včetně FBX, STL, OBJ a dalších. Odkazovat na[dokumentace](https://reference.aspose.com/3d/net/) pro úplný seznam.

### Q2: Jak mohu získat dočasnou licenci pro Aspose.3D?

 A2: Získejte dočasnou licenci návštěvou[tento odkaz](https://purchase.aspose.com/temporary-license/).

### Q3: Kde najdu podporu pro Aspose.3D?

 A3: Připojte se k diskuzi komunity na[Aspose.3D fórum](https://forum.aspose.com/c/3d/18).

### Q4: Mohu vyzkoušet Aspose.3D zdarma před nákupem?

 A4: Ano, prozkoumejte funkce pomocí bezplatné zkušební verze[tady](https://releases.aspose.com/).

### Q5: Jaká je nejnovější verze Aspose.3D pro .NET?

 A5: Zůstaňte v aktuálním stavu kontrolou[stránka ke stažení](https://releases.aspose.com/3d/net/) pro nejnovější vydání.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
