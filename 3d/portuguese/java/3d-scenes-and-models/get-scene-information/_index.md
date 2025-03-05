---
title: Recuperar informações de cenas 3D em aplicativos Java
linktitle: Recuperar informações de cenas 3D em aplicativos Java
second_title: API Java Aspose.3D
description: Explore o mundo da manipulação de cenas 3D em Java com Aspose.3D. Este tutorial orienta você na recuperação de informações passo a passo.
type: docs
weight: 12
url: /pt/java/3d-scenes-and-models/get-scene-information/
---
## Introdução

Bem-vindo a este guia completo sobre como recuperar informações de cenas 3D em aplicativos Java usando Aspose.3D. Se você é um desenvolvedor Java que deseja aprimorar os recursos do seu aplicativo com manipulação de cenas 3D, você está no lugar certo. Este tutorial irá guiá-lo através do processo passo a passo, garantindo que você compreenda cada conceito completamente.

## Pré-requisitos

Antes de mergulharmos no tutorial, certifique-se de ter o seguinte em vigor:

- Compreensão básica de programação Java.
-  Biblioteca Aspose.3D instalada. Se não, baixe-o[aqui](https://releases.aspose.com/3d/java/).
- Java IDE (Integrated Development Environment) instalado e configurado.

## Importar pacotes

Em seu projeto Java, importe os pacotes necessários para aproveitar as funcionalidades do Aspose.3D. Adicione as seguintes linhas ao seu código:

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

## Etapa 1: inicializar uma cena 3D

```java
// ExStart: AddAssetInformationToScene
Scene scene = new Scene();
```

 Comece criando uma nova cena 3D usando Aspose.3D`Scene` aula.

## Etapa 2: definir informações do aplicativo e do fornecedor

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

Especifique o nome do aplicativo e do fornecedor associado à sua cena 3D.

## Passo 3: Definir Unidades de Medida

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

Defina as unidades de medida para sua cena 3D. Neste exemplo, usamos unidades egípcias antigas.

## Etapa 4: salvar cena em arquivo

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddAssetInformationToScene
```

Especifique o diretório e o nome do arquivo para salvar a cena 3D. O exemplo salva a cena no formato FBX com codificação ASCII.

## Etapa 5: Imprimir mensagem de sucesso

```java
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
```

Exiba uma mensagem de sucesso indicando que as informações do ativo foram adicionadas com sucesso à cena.

## Conclusão

Parabéns! Você aprendeu com sucesso como recuperar informações de cenas 3D em aplicativos Java usando Aspose.3D. Esta poderosa biblioteca abre possibilidades infinitas para aprimorar seus projetos Java com conteúdo 3D envolvente.

## Perguntas frequentes

### Q1: O Aspose.3D é compatível com todos os IDEs Java?

A1: Sim, o Aspose.3D foi projetado para funcionar perfeitamente com todos os principais IDEs Java.

### Q2: Posso usar Aspose.3D para projetos comerciais?

A2: Absolutamente. Aspose.3D oferece licenças comerciais para desenvolvedores, garantindo o cumprimento dos requisitos de licenciamento.

### Q3: Onde posso encontrar suporte adicional para Aspose.3D?

 A3: Para qualquer dúvida ou assistência, visite o[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18).

### Q4: Existe uma avaliação gratuita disponível para Aspose.3D?

 A4: Sim, você pode explorar os recursos com uma avaliação gratuita disponível[aqui](https://releases.aspose.com/).

### Q5: Como posso obter uma licença temporária para Aspose.3D?

 A5: Obtenha uma licença temporária para fins de teste[aqui](https://purchase.aspose.com/temporary-license/).