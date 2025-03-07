---
title: A CancellationToken használata
linktitle: A CancellationToken használata
second_title: Aspose.3D .NET API
description: Fedezze fel a 3D modellezés zökkenőmentes világát az Aspose.3D for .NET segítségével. Tanuljon meg hatékonyan betölteni és elmenteni 3D dokumentumokat a CancellationToken használatával.
weight: 10
url: /hu/net/loading-and-saving/cancellation-token/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# A CancellationToken használata

## Bevezetés

Üdvözöljük átfogó útmutatónkban az Aspose.3D for .NET használatáról a 3D modellezési és renderelési projektek javítása érdekében. Az Aspose.3D egy hatékony könyvtár, amely lehetővé teszi a .NET fejlesztők számára, hogy zökkenőmentesen dolgozzanak a 3D fájlokkal. Ebben az oktatóanyagban a betöltési és mentési szempontokat vizsgáljuk meg, különös tekintettel a CancellationToken használatára az aszinkron feladatok hatékony kezeléséhez.

## Előfeltételek

Mielőtt nekivágnánk ennek az útnak, győződjön meg arról, hogy a következő előfeltételeket teljesíti:

-  Aspose.3D for .NET: Töltse le és telepítse a könyvtárat innen[itt](https://releases.aspose.com/3d/net/).
- .NET-környezet: Győződjön meg arról, hogy kompatibilis .NET-fejlesztői környezetet állított be.
- A C# alapszintű ismerete: A C# programozási nyelv ismerete ajánlott.

## Névterek importálása

A kezdéshez feltétlenül vegye fel a szükséges névtereket a projektbe. Ezek a névterek hozzáférést biztosítanak a 3D fájlkezeléshez szükséges funkciókhoz.

```csharp
using Aspose.ThreeD;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
```

## Betöltés és mentés – CancellationToken használata

### 1. lépés: A CancellationTokenSource létrehozása

```csharp
// ExStart:CancellationTokenSource

CancellationTokenSource cts = new CancellationTokenSource();
```

Itt példányosítunk egy CancellationTokenSource-t, amely az aszinkron műveletek törlésének kezelésének kulcsfontosságú összetevője.

### 2. lépés: Inicializálja a 3D jelenetet

```csharp
Scene scene = new Scene();
```

Hozzon létre egy példányt a Scene osztályból. Ez lesz a vászon a 3D modellezési tevékenységeihez.

### 3. lépés: Állítsa be a CancellationToken időtúllépését

```csharp
cts.CancelAfter(1000);
```

 Állítsa be a törlési időt a gombbal`CancelAfter` módszer. Ebben a példában az időtúllépés 1000 ezredmásodpercre (1 másodperc) van beállítva.

### 4. lépés: Nyissa meg a 3D dokumentumot

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

 Próbálja meg megnyitni a 3D dokumentumot a megadott időkereten belül. A`cts.Token` paraméter biztosítja, hogy a művelet megszakítható legyen, ha túllépi a beállított időt.

### 5. lépés: Az importálási kivétel kezelése

ImportException kivétel esetén kezelje kecsesen, ellenőrizve, hogy azt OperationCanceledException okozta-e.

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

## Következtetés

Gratulálunk! Sikeresen navigált az Aspose.3D for .NET CancellationToken használatával a 3D dokumentumok betöltésének kezeléséhez. Ez a technika biztosítja a hatékony és időszerű importálási műveleteket, javítva a 3D-s alkalmazások általános teljesítményét.

## GYIK

### 1. kérdés: Az Aspose.3D kompatibilis az összes 3D fájlformátummal?

 1. válasz: Az Aspose.3D a 3D fájlformátumok széles skáláját támogatja, beleértve az FBX, STL, OBJ és még sok mást. Utal[dokumentáció](https://reference.aspose.com/3d/net/) a teljes listához.

### 2. kérdés: Hogyan szerezhetek ideiglenes licencet az Aspose.3D-hez?

 V2: Szerezzen ideiglenes engedélyt a látogatással[ez a link](https://purchase.aspose.com/temporary-license/).

### 3. kérdés: Hol találok támogatást az Aspose.3D-hez?

 3. válasz: Csatlakozzon a közösségi vitához a[Aspose.3D fórum](https://forum.aspose.com/c/3d/18).

### 4. kérdés: Kipróbálhatom ingyenesen az Aspose.3D-t a vásárlás előtt?

 4. válasz: Igen, fedezze fel a funkciókat ingyenes próbaverzióval[itt](https://releases.aspose.com/).

### 5. kérdés: Mi az Aspose.3D legújabb verziója .NET-hez?

 5. válasz: Maradjon naprakész a[letöltési oldal](https://releases.aspose.com/3d/net/) a legújabb kiadáshoz.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
