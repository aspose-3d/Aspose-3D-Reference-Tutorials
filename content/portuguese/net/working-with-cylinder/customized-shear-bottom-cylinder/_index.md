---
title: Cilindro inferior de cisalhamento personalizado
linktitle: Cilindro inferior de cisalhamento personalizado
second_title: API Aspose.3D .NET
description: Aprenda a criar cilindros de fundo de cisalhamento personalizados usando Aspose.3D for .NET com nosso guia passo a passo detalhado. Eleve suas habilidades de modelagem 3D hoje!
type: docs
weight: 12
url: /pt/net/working-with-cylinder/customized-shear-bottom-cylinder/
---
## Introdução
Bem-vindo ao nosso guia completo sobre como criar um cilindro de fundo de cisalhamento personalizado usando Aspose.3D para .NET. Se você deseja aprimorar suas habilidades de modelagem 3D e adicionar recursos exclusivos aos seus projetos, você está no lugar certo. Neste tutorial, orientaremos você no processo passo a passo, usando explicações claras e trechos de código.
## Pré-requisitos
Antes de mergulharmos no tutorial, certifique-se de ter o seguinte:
- Compreensão básica de programação C# e .NET.
-  Biblioteca Aspose.3D para .NET instalada. Você pode baixá-lo[aqui](https://releases.aspose.com/3d/net/).
- Um ambiente de desenvolvimento configurado para programação .NET.
## Importar namespaces
No seu código C#, comece importando os namespaces necessários:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```
## Etapa 1: crie uma cena
Comece criando uma cena 3D usando Aspose.3D:
```csharp
Scene scene = new Scene();
```
## Etapa 2: Criar o Cilindro 1
Gere o primeiro cilindro e defina suas propriedades:
```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
## Etapa 3: Personalizar o fundo de cisalhamento para o cilindro 1
Aplique um fundo de cisalhamento personalizado ao primeiro cilindro:
```csharp
cylinder1.ShearBottom = new Vector2(0, 0.83); // Cisalhamento 47,5 graus no plano xy (eixo z)
```
## Etapa 4: adicionar o cilindro 1 à cena
Adicione o primeiro cilindro à cena e defina sua translação:
```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
## Etapa 5: Crie o Cilindro 2
Gere um segundo cilindro com propriedades semelhantes:
```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
## Etapa 6: adicionar o cilindro 2 à cena
Adicione o segundo cilindro à cena sem fundo de cisalhamento:
```csharp
scene.RootNode.CreateChildNode(cylinder2);
```
## Etapa 7: salve a cena
Salve a cena como um arquivo Wavefront OBJ em seu diretório de documentos:
```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```
## Conclusão
Parabéns! Você criou com sucesso um cilindro de fundo de cisalhamento personalizado usando Aspose.3D para .NET. Este tutorial teve como objetivo fornecer um guia passo a passo para usuários com diversos níveis de conhecimento em modelagem e programação 3D.
## perguntas frequentes
### O Aspose.3D for .NET é adequado para iniciantes?
Absolutamente! Aspose.3D for .NET oferece uma interface amigável, tornando-o acessível tanto para iniciantes quanto para desenvolvedores experientes.
### Posso aplicar diferentes ângulos de cisalhamento aos cilindros?
Sim, você pode personalizar o fundo de cisalhamento para cada cilindro individualmente, permitindo obter efeitos únicos.
### Existe uma versão de teste disponível?
 Sim, você pode explorar a versão de avaliação gratuita[aqui](https://releases.aspose.com/).
### Onde posso encontrar suporte adicional?
 Visite a[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18) para apoio e discussões da comunidade.
### Como posso obter uma licença temporária?
 Obtenha sua licença temporária[aqui](https://purchase.aspose.com/temporary-license/).