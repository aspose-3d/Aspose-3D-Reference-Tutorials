---
date: 2026-09-08
description: Aprenda a definir unidades e exportar uma cena para FBX em Java usando
  Aspose.3D. Este guia passo a passo mostra como definir o nome do aplicativo, as
  unidades de medida e recuperar informações da cena 3D.
keywords:
- how to define units
- export scene to fbx
- how to set application name
- define measurement units
lastmod: 2026-09-08
linktitle: Como salvar FBX e recuperar informações da cena 3D em Java
og_description: Aprenda a definir unidades e exportar uma cena para FBX em Java com
  Aspose.3D. O guia aborda a definição do nome do aplicativo, unidades de medida e
  a recuperação de informações da cena 3D em poucos passos.
og_image_alt: Guide showing how to define units and export a 3D scene to FBX using
  Aspose.3D Java
og_title: Como definir unidades e exportar cena para FBX em Java
schemas:
- author: Aspose
  dateModified: '2026-09-08'
  description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  headline: How to define units and export scene to FBX in Java
  type: TechArticle
- description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  name: How to define units and export scene to FBX in Java
  steps:
  - name: initialize a 3D scene
    text: The `Scene` class is Aspose.3D's top‑level container that represents an
      entire 3D scene, including geometry, lights, cameras, and metadata. First, create
      an empty `Scene` object. This will be the container for all geometry, lights,
      cameras, and asset metadata.
  - name: define measurement units
    text: The unit system determines the real‑world scale of the scene; Aspose.3D
      lets you specify a unit name and a scale factor relative to meters. In this
      example we use an ancient Egyptian unit called “pole” with a custom scale factor.
      > **Tip:** Adjust `unitScaleFactor` to match the real‑world size of yo
  - name: export scene to FBX
    text: Now that the asset information is attached, we save the scene as an FBX
      file. The `FileFormat.FBX7500ASCII` option produces a human‑readable ASCII FBX,
      which is handy for debugging. > **Remember:** Replace `"Your Document Directory"`
      with an absolute path or a path relative to your project's working
  type: HowTo
- questions:
  - answer: Replace `FileFormat.FBX7500ASCII` with `FileFormat.FBX7500` when calling
      `scene.save(...)`.
    question: How do I change the output format to binary FBX?
  - answer: Yes, use `scene.getUserData().add("Key", "Value")` to embed additional
      key‑value pairs.
    question: Can I add custom user‑defined metadata beyond the built‑in asset fields?
  - answer: It does. Simply change the `FileFormat` enum to `OBJ` or `GLTF2` as needed.
    question: Does Aspose.3D support other export formats like OBJ or GLTF?
  - answer: Aspose.3D for Java supports Java 8 and later.
    question: What version of Java is required?
  - answer: Absolutely. Load the file with `new Scene("input.fbx")`, modify `scene.getAssetInfo()`,
      then save.
    question: Is it possible to load an existing FBX, modify its asset info, and resave?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- export scene to fbx
- Aspose.3D
- Java 3D
- define units
- 3D asset metadata
title: Como definir unidades e exportar cena para FBX em Java
url: /pt/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Como definir unidades e exportar cena para FBX em Java

## Introdução

Se você está procurando um guia claro e prático sobre **como definir unidades** e **exportar uma cena para FBX** enquanto extrai metadados úteis de suas cenas 3D, você chegou ao lugar certo. Neste tutorial percorreremos cada passo usando a biblioteca **Aspose.3D for Java**: desde a criação de uma cena, **definir o nome da aplicação**, **definir unidades de medida**, até finalmente **exportar a cena para FBX**. Ao final, você terá um arquivo FBX pronto para uso que carrega as informações de ativos necessárias para pipelines downstream.

## Respostas rápidas
- **Qual é o objetivo principal?** Exportar uma cena para FBX que contém informações de ativos personalizadas.  
- **Qual biblioteca é usada?** Aspose.3D for Java.  
- **Preciso de uma licença?** Uma versão de avaliação gratuita funciona para desenvolvimento; uma licença comercial é necessária para produção.  
- **Posso mudar as unidades de medida?** Sim – use `setUnitName` e `setUnitScaleFactor`.  
- **Onde a saída é salva?** No caminho que você especificar em `scene.save(...)`.  

## Pré-requisitos

Antes de começar, certifique‑se de que você tem:

- Um bom domínio da sintaxe básica de Java.  
- **Aspose.3D for Java** baixado e adicionado ao seu projeto (você pode obtê‑lo na página oficial) [Aspose 3D download page](https://releases.aspose.com/3d/java/).  
- Seu IDE Java favorito (IntelliJ IDEA, Eclipse, NetBeans, etc.) devidamente configurado.

## Importar pacotes

No seu arquivo fonte Java, importe as classes Aspose.3D que fornecem suporte a manipulação de cenas e formatos de arquivo.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Dica profissional:** Mantenha a lista de importação mínima para evitar dependências desnecessárias e melhorar o tempo de compilação.

## Qual é o processo para salvar um arquivo FBX?

Para salvar uma cena como um arquivo FBX, você cria um `Scene`, define quaisquer metadados de ativos desejados, especifica a unidade de medida e então chama `scene.save(path, FileFormat.FBX7500ASCII)`. Essa sequência grava geometria, materiais e metadados em um FBX ASCII que pode ser inspecionado ou importado por ferramentas downstream.

### Passo 1: inicializar uma cena 3D

A classe `Scene` é o contêiner de nível superior do Aspose.3D que representa uma cena 3D completa, incluindo geometria, luzes, câmeras e metadados. Primeiro, crie um objeto `Scene` vazio. Este será o contêiner para toda a geometria, luzes, câmeras e metadados de ativos.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Como definir o nome da aplicação em Java

O objeto `AssetInfo` armazena metadados como nome da aplicação, fornecedor e versão da cena. Adicionar metadados personalizados ajuda ferramentas downstream a identificar a origem do arquivo. Use o objeto `AssetInfo` para **definir o nome da aplicação** (e fornecedor) antes de salvar o arquivo.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Por que isso importa:** Muitos pipelines filtram ou etiquetam ativos com base na aplicação de origem, tornando este passo essencial para projetos grandes.

### Passo 3: definir unidades de medida

O sistema de unidades determina a escala do mundo real da cena; o Aspose.3D permite especificar um nome de unidade e um fator de escala relativo a metros. Neste exemplo usamos uma unidade egípcia antiga chamada “pole” com um fator de escala personalizado.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Dica:** Ajuste `unitScaleFactor` para corresponder ao tamanho real dos seus modelos; 1.0 representa um mapeamento 1‑para‑1 com a unidade escolhida.

### Passo 4: exportar cena para FBX

Agora que as informações de ativos estão anexadas, salvamos a cena como um arquivo FBX. A opção `FileFormat.FBX7500ASCII` produz um FBX ASCII legível por humanos, o que é útil para depuração.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
// ExEnd:AddAssetInformationToScene
```

> **Lembre‑se:** Substitua `"Your Document Directory"` por um caminho absoluto ou um caminho relativo ao diretório de trabalho do seu projeto.

## Por que exportar cena para FBX com Aspose.3D?

Aspose.3D suporta **mais de 50 formatos de entrada e saída** e pode processar cenas com centenas de páginas sem carregar o arquivo inteiro na memória, dando a você controle total sobre o arquivo exportado — metadados, unidades e geometria — sem precisar de um aplicativo de autoria 3D pesado. Isso torna a geração automatizada de ativos, o processamento em lote e as conversões server‑side rápidas e confiáveis.

## Casos de uso comuns

- **Pipelines de ativos de jogos** – incorporar informações do criador diretamente em arquivos FBX para rastreamento de versão.  
- **Visualização arquitetônica** – armazenar unidades específicas do projeto para evitar erros de escala ao importar em motores de renderização.  
- **Relatórios automatizados** – gerar arquivos FBX sob demanda com metadados que ferramentas de análise downstream podem ler.  
- **Serviços 3D baseados em nuvem** – criar e exportar cenas programaticamente sem GUI, perfeito para plataformas SaaS.

## Solução de problemas e dicas

| Problema | Solução |
|----------|----------|
| **Arquivo não encontrado após salvar** | Verifique se `MyDir` aponta para uma pasta existente e se sua aplicação tem permissões de escrita. |
| **Unidades aparecem incorretas no visualizador externo** | Verifique novamente `unitScaleFactor`; alguns visualizadores esperam metros como unidade base. |
| **Metadados do ativo ausentes** | Certifique-se de chamar `scene.getAssetInfo()` **antes** de salvar; alterações feitas após `save()` não serão persistidas. |
| **Gargalo de desempenho em cenas grandes** | Use `scene.optimize()` antes de salvar para reduzir o uso de memória. |
| **FBX ASCII é muito grande** | Mude para FBX binário usando `FileFormat.FBX7500` (veja FAQ). |

## Perguntas frequentes

**Q: Como altero o formato de saída para FBX binário?**  
A: Substitua `FileFormat.FBX7500ASCII` por `FileFormat.FBX7500` ao chamar `scene.save(...)`.

**Q: Posso adicionar metadados definidos pelo usuário além dos campos de ativo incorporados?**  
A: Sim, use `scene.getUserData().add("Key", "Value")` para incorporar pares chave‑valor adicionais.

**Q: O Aspose.3D suporta outros formatos de exportação como OBJ ou GLTF?**  
A: Sim. Basta mudar o enum `FileFormat` para `OBJ` ou `GLTF2`, conforme necessário.

**Q: Qual versão do Java é necessária?**  
A: Aspose.3D for Java suporta Java 8 e posteriores.

**Q: É possível carregar um FBX existente, modificar suas informações de ativo e salvar novamente?**  
A: Absolutamente. Carregue o arquivo com `new Scene("input.fbx")`, modifique `scene.getAssetInfo()`, então salve.

---

**Última atualização:** 2026-09-08  
**Testado com:** Aspose.3D for Java 24.11  
**Autor:** Aspose

## Tutoriais Relacionados

- [Reduzir tamanho de arquivo 3D – Compactar cenas com Aspose.3D for Java](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [Como definir cor vector3 java: Alterar cor difusa e gerenciar propriedades 3D em cenas Java usando Aspose.3D](/3d/java/3d-scenes-and-models/managing-3d-properties-scenes/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}