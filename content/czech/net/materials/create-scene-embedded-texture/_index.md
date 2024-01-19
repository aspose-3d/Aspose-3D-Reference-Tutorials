---
title: Vytvoření scény s vloženou texturou
linktitle: Vytvoření scény s vloženou texturou
second_title: Aspose.3D .NET API
description: Vytvářejte fascinující 3D scény s vloženými texturami pomocí Aspose.3D for .NET. Postupujte podle našeho podrobného průvodce pro ohromující výsledky.
type: docs
weight: 10
url: /cs/net/materials/create-scene-embedded-texture/
---
## Úvod
Vítejte ve vzrušujícím světě 3D grafiky s Aspose.3D pro .NET! V tomto komplexním tutoriálu vás provedeme procesem vytváření úžasných 3D scén s vloženými texturami pomocí Aspose.3D, výkonné a všestranné knihovny pro vývojáře .NET.
## Předpoklady
Než se pustíte do výukového programu, ujistěte se, že máte splněny následující předpoklady:
- Základní znalost programování v C# a .NET.
- Visual Studio nainstalované na vašem počítači.
-  Aspose.3D for .NET knihovna, kterou si můžete stáhnout[tady](https://releases.aspose.com/3d/net/).
- Seznámení s koncepty 3D grafiky a tvorby scén.
## Importovat jmenné prostory
Začněte importováním potřebných jmenných prostorů do vašeho projektu. Tyto jmenné prostory vám poskytnou nástroje a funkce potřebné pro manipulaci s 3D grafikou.
```csharp
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
```
## Krok 1: Vytvoření scény
Začněte vytvořením nové 3D scény pomocí Aspose.3D for .NET. To poslouží jako plátno pro vaše 3D mistrovské dílo.
```csharp
// Vytvořte soubor FBX s vloženými texturami
Scene scene = new Scene();
```
## Krok 2: Vytvoření vložené textury
Nyní dodejte vaší scéně vizuální šmrnc vložením textury. Vytvoříme texturu s vlastním obsahem a přiřadíme jí název souboru.
```csharp
// Vytvořte vloženou texturu
Texture tex = new Texture()
{
    Content = CreateTextureContent(),
    // Pokud je použita vložená textura, je vyžadován název souboru.
    FileName = "test.png"
};
tex.SetProperty("TexProp", "value");
```
## Krok 3: Vytvoření materiálu
Dále vytvořte materiál pro své 3D objekty se začleněním dříve vytvořené textury a uživatelských vlastností.
```csharp
// Vytvořte materiál s vlastní vlastností
LambertMaterial mat = new LambertMaterial("my-mat");
mat.SetTexture(Material.MapDiffuse, tex);
mat.SetProperty("MyProp", 1.0);
```
## Krok 4: Vytvoření 3D objektu
Nyní vaši scénu oživíme přidáním 3D objektu. V tomto příkladu použijeme torus a aplikujeme materiál, který jste právě vytvořili.
```csharp
// Vytvořte torus s naneseným dříve vytvořeným materiálem
scene.RootNode.CreateChildNode(new Torus()).Material = mat;
```
## Krok 5: Uložení scény
Nakonec uložte své mistrovské dílo do souboru. V tomto příkladu jej uložíme ve formátu FBX.
```csharp
// Uložte scénu do souboru
scene.Save(RunExamples.GetOutputFilePath(@"test.fbx"), FileFormat.FBX7500ASCII);
```
Gratulujeme! Úspěšně jste vytvořili 3D scénu s vloženými texturami pomocí Aspose.3D for .NET.
## CreateTextureContent Zdrojový kód
```csharp
        private static byte[] CreateTextureContent()
        {
            using (var bitmap = new Bitmap(256, 256))
            {
                using (var g = Graphics.FromImage(bitmap))
                {
                    g.Clear(Color.White);
                    LinearGradientBrush brush = new LinearGradientBrush(new Rectangle(0, 0, 128, 128), Color.Moccasin,
                        Color.ForestGreen, 45);
                    using (var font = new Font(FontFamily.GenericSerif, 40))
                    {
                        g.DrawString("Aspose.3D", font, brush, Point.Empty);
                    }
                }
                using (var ms = new MemoryStream())
                {
                    bitmap.Save(ms, ImageFormat.Png);
                    return ms.ToArray();
                }
            }
        }
```
## Závěr
tomto tutoriálu jsme prozkoumali základy vytváření vizuálně úžasných 3D scén s vloženými texturami pomocí Aspose.3D for .NET. Vyzbrojeni těmito znalostmi můžete popustit uzdu své kreativitě a vytvářet úchvatné 3D aplikace.

## Často kladené otázky

### Otázka: Mohu používat Aspose.3D pro .NET s jinými programovacími jazyky?
Odpověď: Aspose.3D je primárně navržen pro .NET, ale podobné knihovny jsou dostupné i pro jiné jazyky.
### Otázka: Jak mohu použít animace na své 3D scény?
Odpověď: Aspose.3D poskytuje možnosti animace; podrobné pokyny naleznete v dokumentaci.
### Otázka: Je k dispozici zkušební verze pro Aspose.3D pro .NET?
 Odpověď: Ano, můžete si stáhnout zkušební verzi[tady](https://releases.aspose.com/).
### Otázka: Kde najdu další podporu a zdroje?
 A: Navštivte[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) za podporu komunity a diskuze.
### Otázka: Mohu použít Aspose.3D pro komerční projekty?
 Odpověď: Ano, můžete si zakoupit licenci[tady](https://purchase.aspose.com/buy).