---
title: Cilindro superior offset personalizado
linktitle: Cilindro superior offset personalizado
second_title: API Aspose.3D .NET
description: Explore as maravilhas dos gráficos 3D com Aspose.3D para .NET. Aprenda a criar cilindros superiores offset personalizados sem esforço. Eleve sua experiência de codificação agora!
type: docs
weight: 11
url: /pt/net/working-with-cylinder/customized-offset-top-cylinder/
---
## Introdução
Bem-vindo ao mundo da manipulação de gráficos 3D com Aspose.3D for .NET! Neste tutorial, orientaremos você no processo de criação de um cilindro superior offset personalizado usando Aspose.3D, uma biblioteca poderosa para trabalhar com cenas, objetos e formatos 3D em aplicativos .NET.
## Pré-requisitos
Antes de mergulharmos no tutorial, certifique-se de ter os seguintes pré-requisitos:
- Conhecimento básico da linguagem de programação C#.
- Visual Studio instalado em sua máquina.
- Biblioteca Aspose.3D para .NET baixada e referenciada em seu projeto.
Agora, vamos começar com o guia passo a passo!
## Importar namespaces
Em primeiro lugar, certifique-se de importar os namespaces necessários em seu código C#:
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
```csharp
// Crie uma cena
Scene scene = new Scene();
```
Isso inicializa uma nova cena 3D usando Aspose.3D.
## Etapa 2: inicializar o cilindro
```csharp
// Inicializar cilindro
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
Aqui, criamos um cilindro com parâmetros específicos como raio, altura e fatias.
## Etapa 3: definir OffsetTop para o primeiro cilindro
```csharp
// Definir deslocamento superior
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```
Isso define um deslocamento superior personalizado para o primeiro cilindro.
## Etapa 4: Criar ChildNode para o primeiro cilindro
```csharp
// Criar ChildNode
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
Adicionamos o primeiro cilindro como nó filho à cena, ajustando sua posição.
## Etapa 5: inicializar o segundo cilindro
```csharp
//Inicialize o segundo cilindro sem OffsetTop personalizado
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
Um segundo cilindro é inicializado sem um topo de deslocamento personalizado.
## Etapa 6: Criar ChildNode para o segundo cilindro
```csharp
// Criar ChildNode
scene.RootNode.CreateChildNode(cylinder2);
```
Adicionamos o segundo cilindro como nó filho à cena.
## Etapa 7: salve a cena
```csharp
// Salvar
scene.Save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WavefrontOBJ);
```
Isso salva a cena 3D, incluindo o cilindro superior deslocado personalizado, no formato Wavefront OBJ.
Agora você criou com sucesso um cilindro superior deslocado personalizado usando Aspose.3D para .NET!
## Conclusão
Neste tutorial, exploramos os fundamentos do trabalho com Aspose.3D for .NET para criar um cilindro superior de deslocamento personalizado. Esta biblioteca abre possibilidades infinitas para manipulação de gráficos 3D em seus aplicativos .NET.
## Perguntas frequentes
### P: Onde posso encontrar a documentação do Aspose.3D for .NET?
 R: A documentação está disponível[aqui](https://reference.aspose.com/3d/net/).
### P: Como posso baixar o Aspose.3D para .NET?
 R: Você pode baixá-lo[aqui](https://releases.aspose.com/3d/net/).
### P: Existe uma avaliação gratuita disponível para Aspose.3D for .NET?
 R: Sim, você pode obter um teste gratuito[aqui](https://releases.aspose.com/).
### P: Onde posso obter suporte para Aspose.3D for .NET?
 R: Visite o[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18) para suporte.
### P: Posso obter uma licença temporária do Aspose.3D for .NET?
 R: Sim, você pode obter uma licença temporária[aqui](https://purchase.aspose.com/temporary-license/).