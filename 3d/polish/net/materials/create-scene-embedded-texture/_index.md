---
title: Tworzenie sceny z osadzoną teksturą
linktitle: Tworzenie sceny z osadzoną teksturą
second_title: Aspose.3D API .NET
description: Twórz hipnotyzujące sceny 3D z osadzonymi teksturami za pomocą Aspose.3D dla .NET. Postępuj zgodnie z naszym przewodnikiem krok po kroku, aby uzyskać oszałamiające rezultaty.
weight: 10
url: /pl/net/materials/create-scene-embedded-texture/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Tworzenie sceny z osadzoną teksturą

## Wstęp
Witamy w ekscytującym świecie grafiki 3D z Aspose.3D dla .NET! W tym kompleksowym samouczku poprowadzimy Cię przez proces tworzenia oszałamiających scen 3D z osadzonymi teksturami przy użyciu Aspose.3D, potężnej i wszechstronnej biblioteki dla programistów .NET.
## Warunki wstępne
Zanim przejdziesz do samouczka, upewnij się, że spełniasz następujące wymagania wstępne:
- Podstawowa znajomość programowania w C# i .NET.
- Program Visual Studio zainstalowany na Twoim komputerze.
- Biblioteka Aspose.3D dla .NET, którą możesz pobrać[Tutaj](https://releases.aspose.com/3d/net/).
- Znajomość koncepcji grafiki 3D i tworzenia scen.
## Importuj przestrzenie nazw
Zacznij od zaimportowania niezbędnych przestrzeni nazw do swojego projektu. Te przestrzenie nazw zapewnią Ci narzędzia i funkcjonalności wymagane do manipulacji grafiką 3D.
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
## Krok 1: Tworzenie sceny
Rozpocznij od utworzenia nowej sceny 3D przy użyciu Aspose.3D dla .NET. Będzie to służyć jako płótno dla Twojego arcydzieła 3D.
```csharp
// Utwórz plik FBX z osadzonymi teksturami
Scene scene = new Scene();
```
## Krok 2: Tworzenie osadzonej tekstury
Teraz dodajmy trochę wizualnego akcentu do Twojej sceny, osadzając teksturę. Stworzymy teksturę z niestandardową zawartością i przypiszemy jej nazwę pliku.
```csharp
// Utwórz osadzoną teksturę
Texture tex = new Texture()
{
    Content = CreateTextureContent(),
    //Nazwa pliku jest wymagana, jeśli używana jest osadzona tekstura.
    FileName = "test.png"
};
tex.SetProperty("TexProp", "value");
```
## Krok 3: Tworzenie materiału
Następnie utwórz materiał dla swoich obiektów 3D, wykorzystując wcześniej utworzoną teksturę i niestandardowe właściwości.
```csharp
// Utwórz materiał z niestandardowymi właściwościami
LambertMaterial mat = new LambertMaterial("my-mat");
mat.SetTexture(Material.MapDiffuse, tex);
mat.SetProperty("MyProp", 1.0);
```
## Krok 4: Tworzenie obiektu 3D
Teraz ożywimy Twoją scenę, dodając obiekt 3D. W tym przykładzie użyjemy torusa i zastosujemy właśnie utworzony materiał.
```csharp
// Utwórz torus z zastosowanym wcześniej utworzonym materiałem
scene.RootNode.CreateChildNode(new Torus()).Material = mat;
```
## Krok 5: Zapisywanie sceny
Na koniec zapisz swoje arcydzieło w pliku. W tym przykładzie zapiszemy go w formacie FBX.
```csharp
// Zapisz scenę do pliku
scene.Save(RunExamples.GetOutputFilePath(@"test.fbx"), FileFormat.FBX7500ASCII);
```
Gratulacje! Pomyślnie utworzyłeś scenę 3D z osadzonymi teksturami przy użyciu Aspose.3D dla .NET.
## Kod źródłowy CreateTextureContent
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
## Wniosek
tym samouczku omówiliśmy podstawy tworzenia oszałamiających wizualnie scen 3D z osadzonymi teksturami przy użyciu Aspose.3D dla .NET. Uzbrojeni w tę wiedzę możesz uwolnić swoją kreatywność i tworzyć wciągające aplikacje 3D.

## Często Zadawane Pytania

### P: Czy mogę używać Aspose.3D dla .NET z innymi językami programowania?
Odp.: Aspose.3D jest przeznaczony głównie dla .NET, ale dostępne są podobne biblioteki dla innych języków.
### P: Jak mogę zastosować animacje do scen 3D?
Odp.: Aspose.3D zapewnia możliwości animacji; szczegółowe instrukcje można znaleźć w dokumentacji.
### P: Czy dostępna jest wersja próbna Aspose.3D dla .NET?
 Odp.: Tak, możesz pobrać wersję próbną[Tutaj](https://releases.aspose.com/).
### P: Gdzie mogę znaleźć dodatkowe wsparcie i zasoby?
 O: Odwiedź[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) za wsparcie społeczności i dyskusje.
### P: Czy mogę używać Aspose.3D w projektach komercyjnych?
 Odpowiedź: Tak, możesz kupić licencję[Tutaj](https://purchase.aspose.com/buy).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
