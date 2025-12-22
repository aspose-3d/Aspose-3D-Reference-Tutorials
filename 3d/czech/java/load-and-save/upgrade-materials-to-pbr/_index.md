---
date: 2025-12-22
description: Naučte se, jak exportovat scénu do glTF v Javě pomocí Aspose.3D a při
  tom upgradovat 3D materiály na PBR pro zvýšený realismus.
linktitle: Export Scene to glTF in Java with Aspose.3D
second_title: Upgrade 3D Materials to PBR
title: Export scény do glTF v Javě s Aspose.3D
url: /cs/java/load-and-save/upgrade-materials-to-pbr/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Export scény do glTF v Javě s Aspose.3D – Upgradovat materiály na PBR

## Úvod

V tomto tutoriálu se naučíte, jak **export scene to glTF** v Javě s Aspose.3D a zároveň upgradovat vaše 3D materiály na Physically‑Based Rendering (PBR). Upgradování na PBR dodá vašim modelům mnohem realističtější vzhled a export do široce podporovaného formátu glTF 2.0 vám umožní sdílet tyto vysoce kvalitní assety napříč enginy, prohlížeči a AR/VR platformami. Provedeme vás předpoklady, naimportujeme potřebné balíčky a podrobně rozebráme každý příklad krok za krokem, abyste mohli tuto techniku použít ve svých projektech.

## Rychlé odpovědi
- **Co znamená „export scene to glTF“?** Převádí scénu Aspose.3D do formátu souboru glTF 2.0 a zachovává geometrii, materiály a hierarchii.  
- **Proč upgradovat materiály na PBR nejdříve?** PBR materiály se přímo mapují na workflow metallic‑roughness glTF, což poskytuje realistické osvětlení bez dalších konverzních kroků.  
- **Potřebuji licenci pro spuštění kódu?** Bezplatná zkušební verze funguje pro vývoj; pro produkci je vyžadována komerční licence.  
- **Které Java IDE jsou podporovány?** Jakékoli IDE, které dokáže kompilovat Javu (Eclipse, IntelliJ IDEA, VS Code atd.).  
- **Mohu exportovat velké scény?** Ano, Aspose.3D streamuje data efektivně; jen zajistěte dostatek heap paměti pro opravdu velké modely.

## Co je „export scene to glTF“?
Export scény do glTF znamená serializaci celé 3D scény — včetně meshí, uzlů, kamer, světel a materiálů — do formátu GL Transmission Format (glTF). glTF je otevřený standard optimalizovaný pro real‑time rendering, což jej činí ideálním pro web, mobilní zařízení a herní enginy.

## Proč upgradovat materiály na PBR před exportem?
PBR (Physically‑Based Rendering) materiály popisují, jak světlo interaguje s povrchy pomocí parametrů jako albedo, metallic a roughness. glTF 2.0 nativně podporuje PBR, takže převod Phong nebo vlastních materiálů na PBR zajišťuje, že barvy, odrazy a stínování budou vypadat správně ve všech glTF‑kompatibilních prohlížečích.

## Předpoklady

1. **Aspose.3D pro Javu** – stáhněte jej ze [stránky vydání](https://releases.aspose.com/3d/java/).  
2. **Java Development Environment** – JDK 8 nebo vyšší a IDE dle vašeho výběru.  
3. **Document Directory** – složka na vašem počítači, kde budete číst/zapisovat 3D soubory.

## Import balíčků

Přidejte hlavní namespace Aspose.3D do svého projektu:

```java
import com.aspose.threed.*;
```

Tento jediný import vám poskytuje přístup k `Scene`, `Box`, `PhongMaterial`, `PbrMaterial`, `GltfSaveOptions` a API pro konverzi materiálů.

## Krok 1: Inicializovat novou 3D scénu

Vytvořte novou scénu, která bude obsahovat vaši geometrii a materiály:

```java
// ExStart:InitializeScene
String MyDir = "Your Document Directory";
Scene s = new Scene();
// ExEnd:InitializeScene
```

> **Pro tip:** Uchovávejte `MyDir` jako absolutní cestu během vývoje, aby nedocházelo k chybám „file‑not‑found“.

## Krok 2: Vytvořit krychli s PhongMaterial

Začneme jednoduchou krychlí, která používá klasický Phong materiál. Ten bude během exportu následně převeden na PBR materiál:

```java
// ExStart:CreateBoxWithMaterial
Box box = new Box();
PhongMaterial mat = new PhongMaterial();
mat.setDiffuseColor(new Vector3(1, 0, 1));
s.getRootNode().createChildNode("box1", box).setMaterial(mat);
// ExEnd:CreateBoxWithMaterial
```

> **Proč Phong?** PhongMaterial je snadno nastavitelný a ukazuje, jak funguje logika konverze.

## Krok 3: Uložit ve formátu GLTF 2.0 (Export scene to glTF)

Nastavte možnosti uložení GLTF tak, aby automaticky konvertovaly jakýkoli `PhongMaterial` na `PbrMaterial`. To je jádro **export scene to glTF**:

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

Když tento kód spustíte, scéna se zapíše do `Non_PBRtoPBRMaterial_Out.gltf`. Vlastní `MaterialConverter` zajistí, že Phong materiál bude převeden na PBR materiál, takže výsledný glTF soubor bude ve všech glTF prohlížečích zobrazovat realistické stínování.

## Časté problémy a řešení

| Problém | Řešení |
|---------|--------|
| **FileNotFoundException** při ukládání | Ověřte, že `MyDir` ukazuje na existující složku a že aplikace má oprávnění k zápisu. |
| **ClassCastException** v konvertoru | Ujistěte se, že materiál předávaný do konvertoru je skutečně `PhongMaterial`. Přidejte kontrolu `instanceof`, pokud kombinujete různé typy materiálů. |
| **Missing textures** po exportu | glTF očekává textury jako samostatné soubory; pokud je potřeba, přidejte do konvertoru zpracování textur. |

## Často kladené otázky

**Q:** Je Aspose.3D kompatibilní s Java vývojovými prostředími jinými než Eclipse?  
**A:** Ano, Aspose.3D funguje s libovolným Java IDE, včetně IntelliJ IDEA, NetBeans a VS Code.

**Q:** Mohu používat Aspose.3D pro komerční projekty?  
**A:** Ano, můžete Aspose.3D používat jak pro osobní, tak pro komerční projekty. Navštivte [stránku nákupu](https://purchase.aspose.com/buy) pro podrobnosti o licencování.

**Q:** Je k dispozici bezplatná zkušební verze?  
**A:** Ano, bezplatnou zkušební verzi získáte [zde](https://releases.aspose.com/).

**Q:** Kde mohu najít podporu pro Aspose.3D?  
**A:** Prozkoumejte [Aspose.3D fórum](https://forum.aspose.com/c/3d/18) pro komunitní podporu.

**Q:** Jak získám dočasnou licenci pro Aspose.3D?  
**A:** Navštivte [tento odkaz](https://purchase.aspose.com/temporary-license/) pro informace o dočasné licenci.

## Závěr

Po absolvování výše uvedených kroků nyní umíte **export scene to glTF** v Javě pomocí Aspose.3D a automaticky upgradovat Phong materiály na PBR. Tento workflow vám umožní vytvářet vysoce kvalitní, fyzikálně založené assety připravené pro moderní renderovací pipeline, webové prohlížeče a AR/VR zážitky. Vyzkoušejte složitější geometrie, textury a osvětlení, abyste plně využili sílu PBR a glTF.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Poslední aktualizace:** 2025-12-22  
**Testováno s:** Aspose.3D 24.12 for Java  
**Autor:** Aspose  

---