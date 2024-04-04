---
title: Exportando cena 3D para formato AMF compactado
linktitle: Exportando cena para AMF compactado
second_title: API Aspose.3D .NET
description: Aprenda como exportar cenas 3D para formato AMF compactado usando Aspose.3D for .NET. Aprimore suas habilidades de desenvolvimento com este guia passo a passo.
type: docs
weight: 11
url: /pt/net/loading-and-saving/amf/export-scene-compressed-amf/
---
## Introdução

No mundo dinâmico da modelagem e renderização 3D, eficiência e flexibilidade são fundamentais. Aspose.3D for .NET capacita os desenvolvedores a exportar perfeitamente cenas 3D para o formato compactado AMF (Additive Manufacturing File), garantindo o tamanho de arquivo ideal sem comprometer a qualidade. Este tutorial irá guiá-lo através do processo passo a passo, tornando mais fácil para iniciantes e desenvolvedores experientes aproveitar os recursos do Aspose.3D para .NET.

## Pré-requisitos

Antes de mergulhar no tutorial, certifique-se de ter os seguintes pré-requisitos:

- Compreensão básica dos conceitos de modelagem 3D
- Visual Studio instalado em sua máquina
-  Biblioteca Aspose.3D para .NET. Você pode baixá-lo[aqui](https://releases.aspose.com/3d/net/)
- Um desejo de aprimorar suas habilidades de desenvolvimento 3D!

## Importar namespaces

Em seu projeto, certifique-se de importar os namespaces necessários para aproveitar a funcionalidade do Aspose.3D for .NET:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Etapa 1: carregar uma cena 3D

Comece carregando uma cena 3D usando Aspose.3D for .NET. Crie um objeto de cena e adicione entidades como caixas a ele:

```csharp
Scene scene = new Scene();
var box = new Box();
var tr = scene.RootNode.CreateChildNode(box).Transform;
tr.Scale = new Vector3(12, 12, 12);
tr.Translation = new Vector3(10, 0, 0);
```

## Etapa 2: transformação de escala

A seguir, aplique uma transformação de escala em outra caixa na cena:

```csharp
tr = scene.RootNode.CreateChildNode(box).Transform;
tr.Scaling = new Vector3(5, 5, 5);
```

## Etapa 3: definir ângulos de Euler

Defina ângulos de Euler para a transformação:

```csharp
tr.EulerAngles = new Vector3(50, 10, 0);
```

## Etapa 4: salvar o arquivo AMF compactado

Finalmente, salve a cena 3D em um arquivo AMF compactado no diretório de saída desejado:

```csharp
scene.Save("Your Output Directory/" + "Aspose.amf", new AmfSaveOptions() { EnableCompression = false });
```

## Conclusão

Parabéns! Você exportou com sucesso uma cena 3D para um formato AMF compactado usando Aspose.3D para .NET. Esta poderosa biblioteca abre um mundo de possibilidades para desenvolvedores 3D, permitindo-lhes criar modelos eficientes e visualmente impressionantes.

## Perguntas frequentes

### Q1: O Aspose.3D é compatível com software de modelagem 3D popular?

A1: Aspose.3D suporta vários formatos de arquivo, tornando-o compatível com ferramentas populares de modelagem 3D.

### P2: Posso ativar a compactação para outros formatos de arquivo além do AMF?

A2: Sim, o Aspose.3D oferece opções para habilitar a compactação para vários formatos de arquivo.

### Q3: O Aspose.3D é adequado para desenvolvedores iniciantes e avançados?

A3: Com certeza! Aspose.3D oferece simplicidade para iniciantes e recursos avançados para desenvolvedores experientes.

### P4: Há alguma limitação quanto ao tamanho das cenas 3D que podem ser exportadas?

A4: Aspose.3D foi projetado para lidar com cenas de complexidade variada e não há limitações estritas de tamanho.

### P5: Onde posso encontrar suporte adicional e discussões na comunidade?

 A5: Visite o[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18) para apoio e discussões.