---
date: 2025-12-06
description: Aprenda como salvar arquivos FBX e recuperar informações da cena usando
  Aspose.3D para Java. Este guia passo a passo aborda a definição do nome do aplicativo,
  a definição das unidades de medida e a exportação da cena para FBX.
language: pt
linktitle: How to Save FBX and Retrieve 3D Scene Info in Java
second_title: Aspose.3D Java API
title: Como salvar FBX e recuperar informações da cena 3D em Java
url: /java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Como Salvar FBX e Recuperar Informações da Cena 3D em Java

## Introdução

Se você está procurando um guia claro e prático sobre **como salvar arquivos fbx** enquanto extrai metadados úteis das suas cenas 3D, chegou ao lugar certo. Neste tutorial vamos percorrer cada etapa usando a biblioteca **Aspose.3D Java**: desde a criação de uma cena, **definição do nome da aplicação**, **especificação das unidades de medida**, até a **exportação da cena para FBX**. Ao final, você terá um arquivo FBX pronto para uso que contém as informações de ativos necessárias para pipelines posteriores.

## Respostas Rápidas
- **Qual é o objetivo principal?** Salvar um arquivo FBX que contenha informações personalizadas de ativos.  
- **Qual biblioteca é usada?** Aspose.3D para Java.  
- **Preciso de licença?** Uma avaliação gratuita funciona para desenvolvimento; uma licença comercial é necessária para produção.  
- **Posso mudar as unidades de medida?** Sim – use `setUnitName` e `setUnitScaleFactor`.  
- **Onde o output é salvo?** No caminho que você especificar em `scene.save(...)`.

## Pré‑requisitos

Antes de começar, certifique‑se de que você tem:

- Um bom domínio da sintaxe básica de Java.  
- **Aspose.3D para Java** baixado e adicionado ao seu projeto (você pode obtê‑lo na página oficial de download da) [Aspose 3D](https://releases.aspose.com/3d/java/).  
- Seu IDE Java favorito (IntelliJ IDEA, Eclipse, NetBeans, etc.) devidamente configurado.

## Importar Pacotes

No seu arquivo fonte Java, importe as classes Aspose.3D que fornecem manipulação de cena e suporte a formatos de arquivo.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Dica profissional:** Mantenha a lista de imports mínima para evitar dependências desnecessárias e melhorar o tempo de compilação.

## Qual é o processo para salvar um arquivo FBX?

A seguir, um passo a passo conciso que mostra **como adicionar informações de ativos** a uma cena e então **exportar a cena para FBX**.

### Etapa 1: Inicializar uma Cena 3D

Primeiro, crie um objeto `Scene` vazio. Ele será o contêiner para toda a geometria, luzes, câmeras e metadados de ativos.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Etapa 2: Definir Informações da Aplicação e do Fornecedor

Adicionar metadados personalizados ajuda ferramentas posteriores a identificar a origem do arquivo. Aqui nós **definimos o nome da aplicação** e do fornecedor usando o objeto `AssetInfo`.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Por que isso importa:** Muitos pipelines filtram ou etiquetam ativos com base na aplicação de origem, tornando esta etapa essencial para projetos de grande escala.

### Etapa 3: Definir Unidades de Medida

Aspose.3D permite especificar o sistema de unidades que sua cena utiliza. Neste exemplo usamos uma unidade egípcia antiga chamada “pole” com um fator de escala personalizado.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Dica:** Ajuste `unitScaleFactor` para corresponder ao tamanho real dos seus modelos; 1.0 representa um mapeamento 1‑para‑1 com a unidade escolhida.

### Etapa 4: Exportar Cena para FBX

Agora que as informações de ativos estão anexadas, salvamos a cena como um arquivo FBX. A opção `FileFormat.FBX7500ASCII` produz um FBX ASCII legível por humanos, útil para depuração.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddAssetInformationToScene
```

> **Lembre‑se:** Substitua `"Your Document Directory"` por um caminho absoluto ou relativo ao diretório de trabalho do seu projeto.

### Etapa 5: Imprimir Mensagem de Sucesso

Uma simples saída no console confirma que a operação foi bem‑sucedida e indica onde o arquivo foi gravado.

```java
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
```

## Casos de Uso Comuns

- **Pipelines de ativos para jogos** – incorporar informações do criador diretamente nos arquivos FBX para rastreamento de versões.  
- **Visualização arquitetônica** – armazenar unidades específicas do projeto para evitar erros de escala ao importar em motores de renderização.  
- **Relatórios automatizados** – gerar arquivos FBX sob demanda com metadados que ferramentas de análise posteriores podem ler.

## Solução de Problemas & Dicas

| Problema | Solução |
|----------|---------|
| **Arquivo não encontrado após salvar** | Verifique se `MyDir` aponta para uma pasta existente e se sua aplicação tem permissão de escrita. |
| **Unidades aparecem incorretas em visualizador externo** | Revise `unitScaleFactor`; alguns visualizadores esperam metros como unidade base. |
| **Metadados de ativos ausentes** | Certifique‑se de chamar `scene.getAssetInfo()` **antes** de salvar; alterações feitas após `save()` não serão persistidas. |

## Perguntas Frequentes

### Q1: O Aspose.3D é compatível com todos os IDEs Java?

A1: Sim, o Aspose.3D foi projetado para funcionar perfeitamente com todos os principais IDEs Java.

### Q2: Posso usar o Aspose.3D em projetos comerciais?

A2: Absolutamente. O Aspose.3D oferece licenças comerciais para desenvolvedores, garantindo conformidade com os requisitos de licenciamento.

### Q3: Onde posso encontrar suporte adicional para o Aspose.3D?

A3: Para dúvidas ou assistência, visite o [fórum Aspose.3D](https://forum.aspose.com/c/3d/18).

### Q4: Existe uma avaliação gratuita disponível para o Aspose.3D?

A4: Sim, você pode explorar os recursos com uma avaliação gratuita disponível [aqui](https://releases.aspose.com/).

### Q5: Como obter uma licença temporária para o Aspose.3D?

A5: Obtenha uma licença temporária para testes [aqui](https://purchase.aspose.com/temporary-license/).

## Perguntas Frequentes (FAQ)

**Q: Como mudar o formato de saída para FBX binário?**  
A: Substitua `FileFormat.FBX7500ASCII` por `FileFormat.FBX7500` ao chamar `scene.save(...)`.

**Q: Posso adicionar metadados definidos pelo usuário além dos campos de ativo incorporados?**  
A: Sim, use `scene.getUserData().add("Key", "Value")` para inserir pares chave‑valor adicionais.

**Q: O Aspose.3D suporta outros formatos de exportação como OBJ ou GLTF?**  
A: Sim. Basta mudar o enum `FileFormat` para `OBJ` ou `GLTF2`, conforme necessário.

**Q: Qual versão do Java é necessária?**  
A: O Aspose.3D para Java suporta Java 8 ou superior.

**Q: É possível carregar um FBX existente, modificar suas informações de ativo e salvar novamente?**  
A: Absolutamente. Carregue o arquivo com `new Scene("input.fbx")`, modifique `scene.getAssetInfo()`, então salve.

---

**Última atualização:** 2025-12-06  
**Testado com:** Aspose.3D for Java 24.11  
**Autor:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
