---
date: 2025-12-17
description: Tanulja meg, hogyan állíthat be licencet az Aspose.3D Java verziójában,
  és hogyan használhatja a nyilvános és privát kulcsokat a mérő licenceléshez.
linktitle: Applying a License in Aspose.3D for Java
second_title: Aspose.3D Java API
title: Hogyan állítsuk be a licencet az Aspose.3D for Java-ban – Teljes útmutató
url: /hu/java/licensing/applying-license-in-aspose-3d/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hogyan állítsuk be a licencet az Aspose.3D-hez Java-ban

## Bevezetés

Üdvözöljük! Ebben a lépésről‑lépésre útmutatóban **meg fogja tanulni, hogyan állítsuk be a licencet** az Aspose.3D-hez egy Java alkalmazásban, és megtanulja, **hogyan használjunk nyilvános és privát kulcsokat** a mérő licenceléshez. Az Aspose.3D egy erőteljes Java könyvtár, amely egyszerűsíti a 3D fájlformátumokkal való munkát, és egy érvényes licenc feloldja a teljes funkciókészletet. A útmutató végére képes lesz a licencelést zökkenőmentesen integrálni bármely Java projektbe.

## Gyors válaszok
- **Mi a fő módja a licenc beállításának?** Használja a `License` osztályt, és hívja a `setLicense` metódust fájlúttal vagy streammel.  
- **Betölthetem a licencet streamből?** Igen – egy `FileInputStream` tökéletesen működik.  
- **Mire szolgálnak a nyilvános/privát kulcsok?** Lehetővé teszik a mérő licencelést a `Metered` osztályon keresztül.  
- **Szükségem van licencre a fejlesztéshez?** Egy ideiglenes vagy próbaverzió licenc elegendő a teszteléshez; a teljes licenc a termeléshez szükséges.  
- **Mely Java verziók támogatottak?** Az Aspose.3D a Java 6 és újabb verziókkal működik.

## Előfeltételek

Mielőtt elkezdenénk, győződjön meg róla, hogy rendelkezik:

- Alapvető Java programozási ismeretekkel.  
- Az Aspose.3D könyvtár hozzáadva a projekthez. Töltse le a [release page](https://releases.aspose.com/3d/java/) oldalról.  
- Érvényes `.lic` fájl vagy a nyilvános és privát mérő kulcsok.

## Csomagok importálása

Adja hozzá a szükséges importokat a Java forrásfájlhoz. Győződjön meg róla, hogy az Aspose.3D JAR a classpath‑on van.

```java
import com.aspose.threed.License;
import com.aspose.threed.Metered;

import java.io.FileInputStream;
import java.io.IOException;
```

## Hogyan állítsuk be a licencet fájl használatával

### 1. lépés: Licenc objektum létrehozása

Példányosítsa a `License` osztályt – ez az objektum fogja tárolni a licencinformációkat.

```java
License license = new License();
```

### 2. lépés: Licenc beállítása fájlból

Adja meg a relatív vagy abszolút útvonalat a `.lic` fájlhoz, és alkalmazza.

```java
license.setLicense("Aspose._3D.lic");
```

> **Pro tip:** Tartsa a licencfájlt a forrás‑vezérlés könyvtárán kívül, hogy elkerülje a véletlen kiadását.

## Hogyan állítsuk be a licencet stream használatával

### 1. lépés: Licenc objektum létrehozása

Mint korábban, kezdjen egy új `License` példánnyal.

```java
License license = new License();
```

### 2. lépés: Licenc beállítása streamből

Olvassa be a licencfájlt egy `FileInputStream`‑be, és adja át a streamet a `setLicense`‑nek. A try‑with‑resources blokk biztosítja, hogy a stream automatikusan bezáródjon.

```java
try (FileInputStream myStream = new FileInputStream("Aspose._3D.lic")) {
    license.setLicense(myStream);
}
```

## Hogyan használjuk a nyilvános és privát kulcsokat a mérő licenceléshez

### 1. lépés: Metered licenc objektum inicializálása

Hozzon létre egy `Metered` osztály példányt, amely a mérő (pay‑as‑you‑go) licencelést kezeli.

```java
Metered metered = new Metered();
```

### 2. lépés: Nyilvános és privát kulcsok beállítása

Adja meg az Aspose‑tól kapott kulcsokat. Ezek a kulcsok lehetővé teszik a könyvtár számára, hogy jelentse a használatot a licenc szervernek.

```java
metered.setMeteredKey("your-public-key", "your-private-key");
```

> **Warning:** Soha ne kódolja be a privát kulcsát egy nyilvánosan terjesztett JAR‑ba. Fontolja meg, hogy biztonságos helyről vagy környezeti változóból töltse be.

## Általános felhasználási esetek

- **Vállalati 3D renderelési csővezetékek** – a licenc beállítása után feloldja a nagy teljesítményű API‑kat.  
- **Automatizált tesztkörnyezetek** – használjon ideiglenes licencet (lásd a GYIK‑ot) a funkciók ellenőrzéséhez anélkül, hogy teljes licencet vásárolna.  
- **Mérő SaaS megoldások** – integrálja a nyilvános/privát kulcsokat, hogy a tényleges használat alapján számlázzon ügyfeleket.

## Összegzés

Gratulálunk! Most már tudja, **hogyan állítsuk be a licencet** az Aspose.3D-hez Java-ban fájl vagy stream használatával, és **hogyan használjunk nyilvános és privát kulcsokat** a mérő licenceléshez. Ezekkel a lépésekkel magabiztosan integrálhatja az Aspose.3D-t bármely Java alkalmazásba, és teljes mértékben kihasználhatja a 3D feldolgozási képességeit.

## Gyakran Ismételt Kérdések

**Q1: Az Aspose.3D kompatibilis minden Java verzióval?**  
A1: Igen, az Aspose.3D a Java 6 és újabb verziókkal működik.

**Q2: Hol találok további dokumentációt?**  
A2: A dokumentációra [itt](https://reference.aspose.com/3d/java/) hivatkozhat.

**Q3: Kipróbálhatom az Aspose.3D-t vásárlás előtt?**  
A3: Igen, egy ingyenes próbaverziót [itt](https://releases.aspose.com/) tekinthet meg.

**Q4: Hogyan kaphatok támogatást az Aspose.3D-hez?**  
A4: Látogassa meg az [Aspose.3D Fórumot](https://forum.aspose.com/c/3d/18) a közösségi és hivatalos támogatásért.

**Q5: Szükségem van ideiglenes licencre a teszteléshez?**  
A5: Igen, ideiglenes licencet szerezhet [itt](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}
{{< blocks/products/products-backtop-button >}}

---

**Utoljára frissítve:** 2025-12-17  
**Tesztelve a következővel:** Aspose.3D 24.11 for Java  
**Szerző:** Aspose