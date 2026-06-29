---
date: 2026-06-29
description: Aprenda como usar uma licença Aspose 3D para criar uma cena 3D com extrusão
  linear de offset de torção em Java e exportá‑la como um arquivo Wavefront OBJ.
keywords:
- aspose 3d license
- wavefront obj export
- linear extrusion twist
- java 3d modeling
linktitle: Usando Offset de Torção em Extrusão Linear com Aspose.3D para Java
schemas:
- author: Aspose
  dateModified: '2026-06-29'
  description: Learn how to use an Aspose 3D license to create a 3D scene with twist
    offset linear extrusion in Java and export it as a Wavefront OBJ file.
  headline: Using Aspose 3D License for Twist Offset Extrusion in Java
  type: TechArticle
- description: Learn how to use an Aspose 3D license to create a 3D scene with twist
    offset linear extrusion in Java and export it as a Wavefront OBJ file.
  name: Using Aspose 3D License for Twist Offset Extrusion in Java
  steps:
  - name: Set Up the Environment
    text: Begin by setting up your Java development environment and ensuring that
      Aspose.3D for Java is correctly installed. This step is essential for any **java
      3d modeling** work.
  - name: Initialize the Base Profile
    text: '`RectangleShape` is a class representing a rectangular 2‑D shape used as
      an extrusion profile. Create a base profile for extrusion, in this case, a `RectangleShape`
      with a rounding radius of 0.3. The profile defines the cross‑section that will
      be swept along the extrusion path.'
  - name: Create a 3D Scene
    text: '`Scene` is the container that holds all nodes, lights, and cameras for
      your model. Building the scene first gives you a place to attach the extruded
      geometry.'
  - name: Create Nodes
    text: Generate nodes within the scene to represent different entities. Here we
      create two sibling nodes—one for a plain extrusion and another that uses a twist
      offset.
  - name: Perform Linear Extrusion with Twist and Twist Offset
    text: Apply linear extrusion on both nodes. The left node demonstrates a basic
      twist, while the right node adds a twist offset to illustrate the extra control
      you get with this feature. `setSlices(int)` sets the number of slices (segments)
      used to approximate the twist, controlling mesh resolution. > **Pr
  - name: Save the 3D Scene (Export 3d scene)
    text: '`save(String, FileFormat)` writes the scene to a file in the specified
      format. Finally, export the assembled scene to an OBJ file so you can view it
      in any standard 3D viewer or import it into other pipelines. CODE_BLOCK_PLACEHOLDER_6_END
      When the code runs successfully, you’ll find `TwistOffsetInLi'
  type: HowTo
- questions:
  - answer: Yes, Aspose.3D for Java can be used in both commercial and non‑commercial
      projects. Check the [licensing options](https://purchase.aspose.com/buy) for
      more details.
    question: Can I use Aspose.3D for Java in non‑commercial projects?
  - answer: Visit the [Aspose.3D for Java forum](https://forum.aspose.com/c/3d/18)
      to get assistance and connect with the community.
    question: Where can I find support for Aspose.3D for Java?
  - answer: Yes, you can explore a free trial version from the [releases page](https://releases.aspose.com/).
    question: Is there a free trial available for Aspose.3D for Java?
  - answer: Get a temporary license for your project by visiting [this link](https://purchase.aspose.com/temporary-license/).
    question: How do I obtain a temporary license for Aspose.3D for Java?
  - answer: Yes, refer to the [documentation](https://reference.aspose.com/3d/java/)
      for more examples and in‑depth tutorials.
    question: Are there additional examples and tutorials available?
  type: FAQPage
second_title: Aspose.3D Java API
title: Usando Licença Aspose 3D para Extrusão com Offset de Torção em Java
url: /pt/java/linear-extrusion/using-twist-offset/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Usando a Licença Aspose 3D para Extrusão com Offset de Torção em Java

## Introdução

Criar uma cena 3D em Java torna‑se muito mais poderoso quando você combina uma **licença Aspose 3D** com recursos de torção de extrusão linear e offset de torção. Este tutorial orienta você em cada passo necessário para **criar cena 3D**, aplicar um offset de torção e, finalmente, **exportar cena 3D** como um arquivo Wavefront OBJ. Com uma versão licenciada, você desbloqueia geração de malha em resolução total, tamanho de arquivo ilimitado e desempenho de nível comercial.

## Respostas Rápidas
- **O que o Twist Offset faz?** Ele desloca o ponto inicial da torção, permitindo que você faça offset da rotação ao longo do caminho de extrusão.  
- **Qual classe realiza a extrusão linear?** `LinearExtrusion` – you can set twist, slices, and twist offset on it.  
- **Posso exportar o resultado?** Sim, chame `scene.save(..., FileFormat.WAVEFRONTOBJ)` para exportar a cena 3D.  
- **Preciso de uma licença Aspose 3D para desenvolvimento?** Uma licença temporária funciona para testes; uma **licença Aspose 3D** completa é necessária para produção e para remover marcas d'água de avaliação.  
- **Qual versão do Java é suportada?** Qualquer runtime Java 8+ funciona com a biblioteca mais recente do Aspose.3D.

## O que é “create 3d scene” no Aspose.3D?

`Scene` é o objeto de nível superior do Aspose.3D que representa um ambiente 3D completo. Criar uma cena 3D no Aspose.3D significa instanciar um objeto `Scene`, adicionar nós filhos que contêm geometria, luzes ou câmeras e, em seguida, salvar a hierarquia em um formato de arquivo como OBJ. O `Scene` serve como o contêiner raiz para todo o conteúdo 3D em sua aplicação Java.

## Por que usar torção de extrusão linear com um offset de torção?

`LinearExtrusion` é a classe do Aspose.3D para varrer um perfil 2‑D ao longo de uma linha reta para gerar geometria 3‑D. Usá‑la com torção adiciona um componente rotacional, e o offset de torção permite que você desloque onde essa rotação começa, proporcionando controle preciso sobre formas espirais como colunas helicoidais, alças decorativas ou molas mecânicas. Esse controle extra é especialmente valioso em **java 3d modeling** para peças mecânicas e designs artísticos.

## Pré-requisitos

- **Java Environment:** Certifique‑se de que você tem um ambiente de desenvolvimento Java configurado em seu sistema.  
- **Aspose.3D for Java:** Baixe e instale a biblioteca Aspose.3D a partir do [download link](https://releases.aspose.com/3d/java/).  
- **Documentation:** Familiarize‑se com a [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/).  

## Importar Pacotes

No seu projeto Java, importe os pacotes necessários para começar a usar o Aspose.3D para Java. Certifique‑se de incluir as bibliotecas requeridas para uma integração perfeita.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Como criar cena 3d – Guia Passo a Passo

Para criar uma cena 3D com extrusão linear de offset de torção em Java, você primeiro configura seu ambiente de desenvolvimento, então define um perfil retangular, instancia um `Scene`, adiciona dois nós filhos, aplica `LinearExtrusion` com e sem offset de torção e, finalmente, salva a cena como um arquivo Wavefront OBJ. Siga as seções passo a passo abaixo para obter os trechos de código exatos.

### Etapa 1: Configurar o Ambiente
Comece configurando seu ambiente de desenvolvimento Java e garantindo que o Aspose.3D para Java esteja corretamente instalado. Esta etapa é essencial para qualquer trabalho de **java 3d modeling**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
// Initialize the base profile to be extruded
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### Etapa 2: Inicializar o Perfil Base
`RectangleShape` é uma classe que representa uma forma retangular 2‑D usada como perfil de extrusão. Crie um perfil base para a extrusão, neste caso, um `RectangleShape` com raio de arredondamento de 0,3. O perfil define a seção transversal que será varrida ao longo do caminho de extrusão.

```java
// Create a scene
Scene scene = new Scene();
```

### Etapa 3: Criar uma Cena 3D
`Scene` é o contêiner que contém todos os nós, luzes e câmeras do seu modelo. Construir a cena primeiro fornece um local para anexar a geometria extrudada.

```java
// Create left node
Node left = scene.getRootNode().createChildNode();
// Create right node
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Etapa 4: Criar Nós
Gere nós dentro da cena para representar diferentes entidades. Aqui criamos dois nós irmãos—um para uma extrusão simples e outro que usa um offset de torção.

```java
// Perform linear extrusion on left node using twist and slices property
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// Perform linear extrusion on right node using twist, twist offset, and slices property
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

### Etapa 5: Executar Extrusão Linear com Torção e Offset de Torção
Aplique extrusão linear em ambos os nós. O nó da esquerda demonstra uma torção básica, enquanto o nó da direita adiciona um offset de torção para ilustrar o controle extra que você obtém com esse recurso. `setSlices(int)` define o número de fatias (segmentos) usados para aproximar a torção, controlando a resolução da malha.

```java
// Save 3D scene
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

> **Dica profissional:** Ajuste `setSlices()` para aumentar a resolução da malha quando precisar de curvatura mais suave.

### Etapa 6: Salvar a Cena 3D (Exportar cena 3d)
`save(String, FileFormat)` grava a cena em um arquivo no formato especificado. Finalmente, exporte a cena montada para um arquivo OBJ para que você possa visualiz‑la em qualquer visualizador 3D padrão ou importá‑la em outros pipelines.

CODE_BLOCK_PLACEHOLDER_6_END

Quando o código for executado com sucesso, você encontrará `TwistOffsetInLinearExtrusion.obj` no diretório especificado, pronto para ser aberto em ferramentas como Blender, MeshLab ou qualquer software CAD.

## Problemas Comuns e Soluções
| Issue | Why it Happens | Fix |
|-------|----------------|-----|
| **Scene salva como arquivo vazio** | O caminho `MyDir` está incorreto ou faltam permissões de gravação. | Verifique se o diretório existe e tem permissão de escrita, ou use um caminho absoluto. |
| **Twist parece plano** | `setSlices()` está muito baixo, resultando em uma malha grosseira. | Aumente a contagem de fatias (por exemplo, 200) para torções mais suaves. |
| **Offset de torção não tem efeito** | O vetor de offset é colinear com a direção da extrusão. | Use um componente X ou Y diferente de zero para ver o deslocamento do offset. |

## Perguntas Frequentes

**Q: Posso usar Aspose.3D para Java em projetos não comerciais?**  
A: Sim, o Aspose.3D para Java pode ser usado tanto em projetos comerciais quanto não comerciais. Consulte as [licensing options](https://purchase.aspose.com/buy) para mais detalhes.

**Q: Onde posso encontrar suporte para Aspose.3D para Java?**  
A: Visite o [Aspose.3D for Java forum](https://forum.aspose.com/c/3d/18) para obter assistência e conectar‑se com a comunidade.

**Q: Existe uma versão de teste gratuita disponível para Aspose.3D para Java?**  
A: Sim, você pode experimentar uma versão de teste gratuita na [releases page](https://releases.aspose.com/).

**Q: Como obtenho uma licença temporária para Aspose.3D para Java?**  
A: Obtenha uma licença temporária para seu projeto visitando [this link](https://purchase.aspose.com/temporary-license/).

**Q: Existem exemplos e tutoriais adicionais disponíveis?**  
A: Sim, consulte a [documentation](https://reference.aspose.com/3d/java/) para mais exemplos e tutoriais aprofundados.

---

**Última atualização:** 2026-06-29  
**Testado com:** Aspose.3D for Java 24.11 (latest)  
**Autor:** Aspose

{{< blocks/products/products-backtop-button >}}

## Tutoriais Relacionados

- [Criar Extrusão 3D Java com Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Criar Cena 3D com Torção em Extrusão Linear – Aspose.3D para Java](/3d/java/linear-extrusion/applying-twist/)
- [Como Definir Direção em Extrusão Linear com Aspose.3D para Java](/3d/java/linear-extrusion/setting-direction/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}