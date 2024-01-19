---
title: Carregando e salvando - usando CancellationToken
linktitle: Carregando e salvando - usando CancellationToken
second_title: API Aspose.3D .NET
description: Explore o mundo contínuo da modelagem 3D com Aspose.3D para .NET. Aprenda a carregar e salvar documentos 3D de forma eficiente usando CancellationToken.
type: docs
weight: 10
url: /pt/net/loading-and-saving/cancellation-token/
---
## Introdução

Bem-vindo ao nosso guia completo sobre a utilização do Aspose.3D for .NET para aprimorar seus projetos de modelagem e renderização 3D. Aspose.3D é uma biblioteca poderosa que permite aos desenvolvedores .NET trabalhar perfeitamente com arquivos 3D. Neste tutorial, nos aprofundaremos nos aspectos de carregamento e salvamento, focando especificamente no uso de CancellationToken para gerenciamento eficiente de tarefas assíncronas.

## Pré-requisitos

Antes de embarcarmos nesta jornada, certifique-se de ter os seguintes pré-requisitos em vigor:

-  Aspose.3D para .NET: Baixe e instale a biblioteca de[aqui](https://releases.aspose.com/3d/net/).
- Ambiente .NET: certifique-se de ter um ambiente de desenvolvimento .NET compatível configurado.
- Compreensão básica de C#: Recomenda-se familiaridade com a linguagem de programação C#.

## Importar namespaces

Para começar, certifique-se de incluir os namespaces necessários em seu projeto. Esses namespaces fornecerão acesso às funcionalidades necessárias para a manipulação de arquivos 3D.

```csharp
using Aspose.ThreeD;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
```

## Carregando e salvando - usando CancellationToken

### Etapa 1: Criar CancellationTokenSource

```csharp
// ExStart:CancellationTokenSource

CancellationTokenSource cts = new CancellationTokenSource();
```

Aqui, instanciamos um CancellationTokenSource, um componente crucial para gerenciar o cancelamento em operações assíncronas.

### Etapa 2: inicializar a cena 3D

```csharp
Scene scene = new Scene();
```

Crie uma instância da classe Scene. Esta será a tela para suas atividades de modelagem 3D.

### Etapa 3: definir o tempo limite do CancellationToken

```csharp
cts.CancelAfter(1000);
```

 Defina o tempo limite de cancelamento usando o`CancelAfter` método. Neste exemplo, o tempo limite é definido como 1.000 milissegundos (1 segundo).

### Passo 4: Abra o Documento 3D

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

 Tente abrir o documento 3D dentro do prazo especificado. O`cts.Token`parâmetro garante que a operação possa ser cancelada se exceder o tempo limite definido.

### Etapa 5: lidar com exceção de importação

No caso de uma ImportException, trate-a normalmente, verificando se ela foi causada por uma OperationCanceledException.

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

## Conclusão

Parabéns! Você navegou com sucesso pelo processo de uso do Aspose.3D for .NET com CancellationToken para gerenciar o carregamento de documentos 3D. Esta técnica garante operações de importação eficientes e oportunas, melhorando o desempenho geral dos seus aplicativos 3D.

## Perguntas frequentes

### Q1: O Aspose.3D é compatível com todos os formatos de arquivo 3D?

 A1: Aspose.3D suporta uma ampla variedade de formatos de arquivo 3D, incluindo FBX, STL, OBJ e muito mais. Consulte o[documentação](https://reference.aspose.com/3d/net/) para a lista completa.

### Q2: Como posso obter uma licença temporária para Aspose.3D?

 A2: Obtenha uma licença temporária visitando[esse link](https://purchase.aspose.com/temporary-license/).

### Q3: Onde posso encontrar suporte para Aspose.3D?

 A3: Participe da discussão da comunidade no[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18).

### Q4: Posso experimentar o Aspose.3D gratuitamente antes de comprar?

 A4: Sim, explore os recursos com uma avaliação gratuita disponível[aqui](https://releases.aspose.com/).

### Q5: Qual é a versão mais recente do Aspose.3D para .NET?

 A5: Mantenha-se atualizado verificando o[página de download](https://releases.aspose.com/3d/net/) para o último lançamento.