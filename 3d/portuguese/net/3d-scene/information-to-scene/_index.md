---
date: 2026-03-26
description: Aprenda como adicionar informações do fornecedor a uma cena 3D e como
  salvar arquivos FBX usando Aspose.3D para .NET. Siga este guia passo a passo com
  código pronto para executar.
linktitle: Extracting Information to Scene Assets
second_title: Aspose.3D .NET API
title: Como adicionar informações do fornecedor e salvar a cena FBX usando Aspose.3D
url: /pt/net/3d-scene/information-to-scene/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Como Adicionar Informações do Vendedor e Salvar Cena FBX Usando Aspose.3D

## Introdução

Bem-vindo a este tutorial abrangente que mostra **como adicionar fornecedor** detalhes a uma cena 3D e então **como salvar FBX** arquivos com Aspose.3D para .NET. Seja construindo visualizações arquitetônicas, ativos de jogos ou modelos de engenharia, incorporar metadados de fornecedor e aplicação torna suas cenas mais informativas e mais fáceis de gerenciar posteriormente. Vamos percorrer o processo passo a passo.

## Respostas Rápidas
- **O que significa “add vendor”?** Ele armazena os nomes da aplicação e do fornecedor dentro do bloco AssetInfo da cena.  
- **Qual formato suporta informações de fornecedor?** FBX (ASCII ou binário) mantém os metadados ao ser salvo.  
- **Como salvar FBX?** Use `scene.Save(path, FileFormat.FBX7500ASCII)` ou o equivalente binário.  
- **Preciso de uma licença?** Um teste gratuito funciona para desenvolvimento; uma licença comercial é necessária para produção.  
- **Posso mudar as unidades de medida?** Sim, defina `AssetInfo.UnitName` e `AssetInfo.UnitScaleFactor`.

## O que é “como adicionar fornecedor” em uma cena 3D?
Adicionar informações de fornecedor significa preencher as propriedades `AssetInfo` de um objeto `Scene`. Essas propriedades viajam com o arquivo, permitindo que qualquer consumidor do arquivo FBX veja qual aplicação o criou e quem é o fornecedor.

## Por que adicionar informações de fornecedor?
- **Rastreabilidade:** Identifique rapidamente a origem de um modelo em pipelines extensas.  
- **Conformidade:** Algumas indústrias exigem marcação explícita de fornecedor para gerenciamento de ativos.  
- **Automação:** Scripts podem filtrar ou processar arquivos com base nos metadados do fornecedor.

## Pré-requisitos

- Aspose.3D para .NET instalado. Você pode baixá-lo na [página Aspose.3D para .NET](https://releases.aspose.com/3d/net/).

## Importar Namespaces

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## Como Adicionar Informação de Fornecedor

### Etapa 1: Inicializar uma Cena 3D

```csharp
Scene scene = new Scene();
```

Criar uma nova `Scene` fornece uma tela limpa para trabalhar.

### Etapa 2: Definir Informações da Aplicação e do Fornecedor

```csharp
scene.AssetInfo.ApplicationName = "Egypt";
scene.AssetInfo.ApplicationVendor = "Manualdesk";
```

Aqui demonstramos **como adicionar fornecedor** dados atribuindo strings significativas a `ApplicationName` e `ApplicationVendor`.

### Etapa 3: Definir Unidades de Medida

```csharp
scene.AssetInfo.UnitName = "pole";
scene.AssetInfo.UnitScaleFactor = 0.6;
```

Especificar o sistema de unidades garante que quem abrir o arquivo FBX interprete as dimensões corretamente. Neste exemplo, um “pole” equivale a 60 cm.

## Como Salvar a Cena FBX

### Etapa 4: Salvar a Cena (como salvar fbx)

```csharp
var output = "Your Output Directory" + "InformationToScene.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Esta linha mostra **como salvar fbx** usando a versão ASCII do FBX 7.5.0. Se preferir binário, substitua `FBX7500ASCII` por `FBX7500Binary`.

> **Dica profissional:** Mantenha a extensão do arquivo `.fbx` consistente com o formato escolhido; caso contrário, alguns visualizadores podem interpretar o conteúdo incorretamente.

### Etapa 5: Exibir Mensagem de Sucesso

```csharp
Console.WriteLine("\nAsset information added successfully to Scene.\nFile saved at " + output);
```

Uma mensagem amigável no console confirma que a cena, completa com metadados de fornecedor, foi gravada no disco.

## Problemas Comuns e Soluções

| Problema | Solução |
|----------|---------|
| **Informação do fornecedor não aparece no visualizador** | Certifique-se de que salvou o arquivo como **FBX ASCII** ou **Binary**; alguns visualizadores antigos leem apenas um formato. |
| **Caminho contém espaços** | Envolva o caminho entre aspas ou use `Path.Combine` para construir um caminho de arquivo seguro. |
| **Escala da unidade parece errada** | Verifique novamente `UnitScaleFactor`; é um multiplicador relativo a metros. |
| **Exceção de licença** | Use o teste gratuito para testes; obtenha uma licença completa para builds de produção. |

## Perguntas Frequentes

**Q: Posso usar Aspose.3D para .NET com outras linguagens de programação?**  
A: Aspose.3D suporta principalmente linguagens .NET, mas você pode explorar opções de interoperabilidade para outras linguagens.

**Q: Existe um teste gratuito disponível para Aspose.3D para .NET?**  
A: Sim, você pode acessar o teste gratuito [aqui](https://releases.aspose.com/).

**Q: Como obtenho suporte para dúvidas relacionadas ao Aspose.3D?**  
A: Visite o [fórum Aspose.3D](https://forum.aspose.com/c/3d/18) para comunidade e suporte.

**Q: Posso adquirir uma licença temporária para Aspose.3D para .NET?**  
A: Sim, você pode adquirir uma licença temporária [aqui](https://purchase.aspose.com/temporary-license/).

**Q: Onde posso encontrar documentação detalhada para Aspose.3D para .NET?**  
A: Consulte a [documentação](https://reference.aspose.com/3d/net/) para informações aprofundadas.

---

**Última atualização:** 2026-03-26  
**Testado com:** Aspose.3D 24.11 for .NET  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}