---
title: Criando cilindro de ventilador
linktitle: Criando cilindro de ventilador
second_title: API Aspose.3D .NET
description: Desbloqueie o mundo do design 3D com Aspose.3D para .NET! Crie cilindros impressionantes com e sem ventilador sem esforço. Baixe seu teste agora.
type: docs
weight: 10
url: /pt/net/working-with-cylinder/create-fan-cylinder/
---
## Introdução
Bem-vindo ao mundo da modelagem e visualização 3D com Aspose.3D for .NET! Neste guia passo a passo, exploraremos como criar um cilindro de ventilador cativante usando Aspose.3D para .NET. Aspose.3D é uma biblioteca poderosa que oferece amplos recursos para trabalhar com conteúdo 3D em aplicativos .NET.
## Pré-requisitos
Antes de mergulharmos no emocionante mundo da modelagem 3D, certifique-se de ter os seguintes pré-requisitos:
- Uma compreensão básica da programação .NET.
- Visual Studio instalado em sua máquina.
-  Biblioteca Aspose.3D para .NET, que você pode baixar[aqui](https://releases.aspose.com/3d/net/).
- Um interesse genuíno em liberar sua criatividade através do design 3D.
## Importar namespaces
Vamos começar importando os namespaces necessários para disponibilizar a funcionalidade Aspose.3D em seu projeto .NET.
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
// Importar namespaces Aspose.3D
```
Agora que estamos todos configurados, vamos dividir o processo de criação de um cilindro de ventilador em etapas gerenciáveis.
## Etapa 1: crie uma cena
```csharp
// Crie uma cena
Scene scene = new Scene();
```
Comece inicializando uma nova cena 3D. Isso serve como tela onde nosso cilindro de ventilador ganhará vida.
## Etapa 2: crie um cilindro de ventilador
```csharp
// Crie um cilindro
var fan = new Cylinder(2, 2, 10, 20, 1, false);
```
Defina as características do cilindro do seu ventilador, especificando parâmetros como raio, altura e resolução.
## Etapa 3: personalizar as propriedades do cilindro do ventilador
```csharp
// Defina GenerateFanCylinder como verdadeiro
fan.GenerateFanCylinder = true;
// Definir comprimento Theta
fan.ThetaLength = MathUtils.ToRadian(270);
```
Personalize o cilindro do seu ventilador permitindo a geração da peça do ventilador e ajustando a varredura angular usando ThetaLength.
## Etapa 4: posicione o cilindro do ventilador na cena
```csharp
// Criar ChildNode
scene.RootNode.CreateChildNode(fan).Transform.Translation = new Vector3(10, 0, 0);
```
Adicione o cilindro do ventilador como um nó filho ao nó raiz da cena e posicione-o no espaço 3D.
## Etapa 5: Crie um cilindro sem ventilador
```csharp
// Crie um cilindro sem ventilador
var nonfan = new Cylinder(2, 2, 10, 20, 1, false);
```
Explore a flexibilidade do Aspose.3D criando um cilindro sem a parte do ventilador.
## Etapa 6: personalizar as propriedades do cilindro sem ventilador
```csharp
// Defina GenerateFanCylinder como falso
nonfan.GenerateFanCylinder = false;
// Definir comprimento Theta
nonfan.ThetaLength = MathUtils.ToRadian(270);
```
Distinga o cilindro sem ventilador desativando a geração da peça do ventilador.
## Etapa 7: posicione o cilindro sem ventilador na cena
```csharp
// Criar ChildNode
scene.RootNode.CreateChildNode(nonfan);
```
Da mesma forma, adicione o cilindro sem ventilador como um nó filho ao nó raiz da cena.
## Etapa 8: salve a cena
```csharp
// Salvar cena
scene.Save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WavefrontOBJ);
```
Salve sua obra-prima no formato e local desejado. Agora, você criou com sucesso um cilindro com e sem ventilador usando Aspose.3D para .NET!
## Conclusão
Parabéns por concluir este guia prático para modelagem 3D com Aspose.3D for .NET! Você liberou sua criatividade no mundo digital, criando cilindros com e sem ventilador com facilidade.
## perguntas frequentes
### Posso usar o Aspose.3D for .NET com outras estruturas .NET?
Sim, o Aspose.3D é compatível com diversos frameworks .NET, proporcionando versatilidade em seus projetos de desenvolvimento.
### Existe uma avaliação gratuita disponível para Aspose.3D for .NET?
 Sim, você pode explorar uma avaliação gratuita[aqui](https://releases.aspose.com/).
### Onde posso encontrar documentação detalhada para Aspose.3D for .NET?
 A documentação está disponível[aqui](https://reference.aspose.com/3d/net/).
### Como posso obter suporte para Aspose.3D para .NET?
 Visite o fórum de suporte[aqui](https://forum.aspose.com/c/3d/18)pela assistência da comunidade e dos especialistas da Aspose.
### As licenças temporárias estão disponíveis para Aspose.3D for .NET?
 Sim, licenças temporárias podem ser obtidas[aqui](https://purchase.aspose.com/temporary-license/).