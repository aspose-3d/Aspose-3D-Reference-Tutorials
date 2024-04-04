---
title: Criando uma cena com textura incorporada
linktitle: Criando uma cena com textura incorporada
second_title: API Aspose.3D .NET
description: Crie cenas 3D fascinantes com texturas incorporadas usando Aspose.3D para .NET. Siga nosso guia passo a passo para obter resultados impressionantes.
type: docs
weight: 10
url: /pt/net/materials/create-scene-embedded-texture/
---
## Introdução
Bem-vindo ao emocionante mundo dos gráficos 3D com Aspose.3D for .NET! Neste tutorial abrangente, iremos guiá-lo através do processo de criação de cenas 3D impressionantes com texturas incorporadas usando Aspose.3D, uma biblioteca poderosa e versátil para desenvolvedores .NET.
## Pré-requisitos
Antes de mergulhar no tutorial, certifique-se de ter os seguintes pré-requisitos em vigor:
- Uma compreensão básica de programação C# e .NET.
- Visual Studio instalado em sua máquina.
- Biblioteca Aspose.3D para .NET, que você pode baixar[aqui](https://releases.aspose.com/3d/net/).
- Familiaridade com os conceitos de gráficos 3D e criação de cenas.
## Importar namespaces
Comece importando os namespaces necessários para o seu projeto. Esses namespaces fornecerão as ferramentas e funcionalidades necessárias para a manipulação de gráficos 3D.
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
## Passo 1: Criando uma Cena
Comece criando uma nova cena 3D usando Aspose.3D for .NET. Isso servirá como tela para sua obra-prima 3D.
```csharp
// Crie um arquivo FBX com texturas incorporadas
Scene scene = new Scene();
```
## Passo 2: Criando uma Textura Incorporada
Agora, vamos adicionar um toque visual à sua cena incorporando uma textura. Criaremos uma textura com conteúdo personalizado e atribuiremos um nome de arquivo a ela.
```csharp
// Crie uma textura incorporada
Texture tex = new Texture()
{
    Content = CreateTextureContent(),
    // nome do arquivo é necessário se a textura incorporada for usada.
    FileName = "test.png"
};
tex.SetProperty("TexProp", "value");
```
## Etapa 3: Criando um Material
Em seguida, crie um material para seus objetos 3D, incorporando a textura criada anteriormente e as propriedades personalizadas.
```csharp
// Crie um material com propriedade personalizada
LambertMaterial mat = new LambertMaterial("my-mat");
mat.SetTexture(Material.MapDiffuse, tex);
mat.SetProperty("MyProp", 1.0);
```
## Passo 4: Criando um Objeto 3D
Agora, vamos dar vida à sua cena adicionando um objeto 3D. Neste exemplo, usaremos um toro e aplicaremos o material que você acabou de criar.
```csharp
// Crie um toro com o material criado anteriormente aplicado
scene.RootNode.CreateChildNode(new Torus()).Material = mat;
```
## Etapa 5: salvando a cena
Finalmente, salve sua obra-prima em um arquivo. Neste exemplo, salvaremos no formato FBX.
```csharp
// Salve a cena em um arquivo
scene.Save(RunExamples.GetOutputFilePath(@"test.fbx"), FileFormat.FBX7500ASCII);
```
Parabéns! Você criou com sucesso uma cena 3D com texturas incorporadas usando Aspose.3D para .NET.
## Código-fonte CreateTextureContent
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
## Conclusão
Neste tutorial, exploramos os fundamentos da criação de cenas 3D visualmente impressionantes com texturas incorporadas usando Aspose.3D para .NET. Armado com esse conhecimento, você pode liberar sua criatividade e criar aplicativos 3D cativantes.

## perguntas frequentes

### P: Posso usar o Aspose.3D for .NET com outras linguagens de programação?
R: Aspose.3D foi projetado principalmente para .NET, mas existem bibliotecas semelhantes disponíveis para outras linguagens.
### P: Como posso aplicar animações às minhas cenas 3D?
R: Aspose.3D fornece recursos de animação; consulte a documentação para obter instruções detalhadas.
### P: Existe uma versão de teste disponível para Aspose.3D for .NET?
 R: Sim, você pode baixar a versão de teste[aqui](https://releases.aspose.com/).
### P: Onde posso encontrar suporte e recursos adicionais?
 R: Visite o[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18) para apoio e discussões da comunidade.
### P: Posso usar o Aspose.3D para projetos comerciais?
 R: Sim, você pode comprar uma licença[aqui](https://purchase.aspose.com/buy).