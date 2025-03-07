---
title: Dividindo todas as malhas da cena por material
linktitle: Dividindo todas as malhas da cena por material
second_title: API Aspose.3D .NET
description: Aprenda como dividir malhas 3D por material usando Aspose.3D for .NET. Siga nosso guia passo a passo para organização e gerenciamento eficiente de modelos 3D.
weight: 21
url: /pt/net/meshes/split-all-meshes-by-material/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Dividindo todas as malhas da cena por material

## Introdução
Bem-vindo a este guia passo a passo sobre como dividir todas as malhas de uma cena 3D por material usando Aspose.3D para .NET. Se você trabalha com modelos 3D e deseja organizar suas malhas de maneira eficiente com base em materiais, este tutorial é para você. Aspose.3D é uma biblioteca .NET poderosa que oferece uma variedade de recursos para trabalhar com arquivos 3D, tornando-a uma excelente escolha para desenvolvedores.
## Pré-requisitos
Antes de mergulhar no tutorial, certifique-se de ter os seguintes pré-requisitos:
- Compreensão básica da linguagem de programação C#.
- Visual Studio instalado em sua máquina.
-  Biblioteca Aspose.3D para .NET. Você pode baixá-lo em[aqui](https://releases.aspose.com/3d/net/).
- Um arquivo 3D de entrada (por exemplo, "test.fbx") que você deseja dividir.
## Importar namespaces
Comece importando os namespaces necessários em seu projeto C#:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```
## Etapa 1: carregar o arquivo 3D
```csharp
// O caminho para o diretório de documentos.
string input = RunExamples.GetDataFilePath("test.fbx");
// Carregar um arquivo 3D
Scene scene = new Scene(input);
```
 Nesta etapa, carregamos o arquivo 3D usando Aspose.3D's`Scene` aula.
## Etapa 2: dividir todas as malhas
```csharp
// Dividir todas as malhas
PolygonModifier.SplitMesh(scene, SplitMeshPolicy.CloneData);
```
 Aqui, usamos o`SplitMesh` método do`PolygonModifier` classe para dividir todas as malhas com base no material.
## Etapa 3: salve a cena dividida
```csharp
// Salvar Arquivo
var output = "Your Output Directory" + "test-splitted.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```
Salve a cena modificada em um novo arquivo para manter as alterações.
## Etapa 4: exibir mensagem de sucesso
```csharp
// Exibir mensagem de sucesso
Console.WriteLine("\nSplitting all meshes of a scene per material successfully.\nFile saved at " + output);
```
Imprima uma mensagem de sucesso indicando que a operação foi concluída com sucesso.
## Conclusão
Parabéns! Você aprendeu com sucesso como dividir todas as malhas de uma cena 3D por material usando Aspose.3D for .NET. Esta pode ser uma técnica valiosa para organizar e gerenciar modelos 3D complexos.
## Perguntas frequentes
### 1. Posso usar Aspose.3D for .NET com outras linguagens de programação?
Aspose.3D foi projetado principalmente para .NET, mas fornece interoperabilidade com outras linguagens por meio de ligações de linguagem .NET.
### 2. Existe uma versão de teste disponível?
 Sim, você pode acessar a versão de avaliação gratuita[aqui](https://releases.aspose.com/).
### 3. Onde posso encontrar mais exemplos e documentação?
 Explore a documentação abrangente em[Documentação Aspose.3D](https://reference.aspose.com/3d/net/).
### 4. Como posso obter suporte para Aspose.3D?
 Visite a[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18) para apoio e discussões da comunidade.
### 5. Posso obter uma licença temporária?
 Sim, você pode obter uma licença temporária[aqui](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
