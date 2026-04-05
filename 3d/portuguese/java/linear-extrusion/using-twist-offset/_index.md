---
date: 2026-02-22
description: Aprenda a criar e exportar cenas 3D usando Aspose.3D para Java com extrusão
  linear, torção e deslocamento de torção.
linktitle: Using Twist Offset in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Como criar uma cena 3D com deslocamento de torção em extrusão linear usando
  Aspose.3D para Java
url: /pt/java/linear-extrusion/using-twist-offset/
weight: 15
---

 markdown formatting.

Now produce final content.{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Usando Twist Offset em Extrusão Linear com Aspose.3D para Java

## Introdução

No mundo dinâmico dos gráficos 3D, dominar a arte de **create 3d scene** é um divisor de águas para qualquer projeto de modelagem 3D em Java. Com Aspose.3D para Java você pode não apenas extrudar formas linearmente, mas também adicionar um twist offset para produzir geometria intrincada e torcida. Este tutorial orienta você em cada passo necessário para **create 3d scene**, aplicar um twist de extrusão linear e, finalmente, **export 3d scene** para um arquivo OBJ comum.

## Respostas Rápidas
- **O que o Twist Offset faz?** Ele desloca o ponto inicial do twist, permitindo que você compense a rotação ao longo do caminho de extrusão.  
- **Qual classe realiza a extrusão linear?** `LinearExtrusion` – você pode definir twist, slices e twist offset nela.  
- **Posso exportar o resultado?** Sim, chame `scene.save(..., FileFormat.WAVEFRONTOBJ)` para exportar a cena 3D.  
- **Preciso de licença para desenvolvimento?** Uma licença temporária funciona para testes; uma licença completa é necessária para produção.  
- **Qual versão do Java é suportada?** Qualquer runtime Java 8+ funciona com a biblioteca mais recente do Aspose.3D.

## O que é “create 3d scene” no Aspose.3D?
Criar uma cena 3D significa instanciar um objeto `Scene`, adicionar nós (objetos) à sua hierarquia e, finalmente, salvar a cena em um formato de arquivo de sua escolha. Isso é a base para qualquer fluxo de trabalho de modelagem 3D em Java.

## Por que usar twist de extrusão linear com um twist offset?
Adicionar um twist durante a extrusão fornece formas espirais, como colunas helicoidais ou alças decorativas. O twist offset permite iniciar o twist em uma posição personalizada, oferecendo controle mais fino sobre a forma final — perfeito para peças mecânicas, modelos artísticos ou detalhes arquitetônicos.

## Pré-requisitos

Antes de mergulhar no tutorial, certifique‑se de que você tem os seguintes pré‑requisitos em vigor:

- **Ambiente Java:** Certifique‑se de que você tem um ambiente de desenvolvimento Java configurado em seu sistema.  
- **Aspose.3D para Java:** Baixe e instale a biblioteca Aspose.3D a partir do [download link](https://releases.aspose.com/3d/java/).  
- **Documentação:** Familiarize‑se com a [documentação do Aspose.3D para Java](https://reference.aspose.com/3d/java/).

## Importar Pacotes

Em seu projeto Java, importe os pacotes necessários para começar a usar Aspose.3D para Java. Certifique‑se de incluir as bibliotecas exigidas para uma integração perfeita.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Como criar 3d scene – Guia Passo a Passo

### Passo 1: Configurar o Ambiente
Comece configurando seu ambiente de desenvolvimento Java e garantindo que o Aspose.3D para Java esteja corretamente instalado. Esta etapa é essencial para qualquer trabalho de **java 3d modeling**.

### Passo 2: Inicializar o Perfil Base
Crie um perfil base para extrusão, neste caso, um `RectangleShape` com raio de arredondamento de 0.3. O perfil define a seção transversal que será varrida ao longo do caminho de extrusão.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
// Initialize the base profile to be extruded
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### Passo 3: Criar uma Cena 3D
Construa uma cena 3D para abrigar seus objetos extrudados. É aqui que você **create child node** elementos que representam cada peça de geometria.

```java
// Create a scene
Scene scene = new Scene();
```

### Passo 4: Criar Nós
Gere nós dentro da cena para representar diferentes entidades. Aqui criamos dois nós irmãos — um para uma extrusão simples e outro que usa um twist offset.

```java
// Create left node
Node left = scene.getRootNode().createChildNode();
// Create right node
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Passo 5: Executar Extrusão Linear com Twist e Twist Offset
Aplique extrusão linear em ambos os nós. O nó da esquerda demonstra um twist básico, enquanto o nó da direita adiciona um twist offset para ilustrar o controle extra que você obtém com esse recurso.

```java
// Perform linear extrusion on left node using twist and slices property
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// Perform linear extrusion on right node using twist, twist offset, and slices property
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

> **Dica profissional:** Ajuste `setSlices()` para aumentar a resolução da malha quando precisar de curvatura mais suave.

### Passo 6: Salvar a Cena 3D (Exportar 3d scene)
Finalmente, exporte a cena montada para um arquivo OBJ para que você possa visualizá‑la em qualquer visualizador 3D padrão ou importá‑la em outros pipelines.

```java
// Save 3D scene
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Quando o código for executado com sucesso, você encontrará `TwistOffsetInLinearExtrusion.obj` no diretório especificado, pronto para ser aberto em ferramentas como Blender, MeshLab ou qualquer software CAD.

## Problemas Comuns e Soluções
| Problema | Por que acontece | Solução |
|----------|------------------|---------|
| **A cena salva como arquivo vazio** | O caminho `MyDir` está incorreto ou faltam permissões de gravação. | Verifique se o diretório existe e tem permissão de escrita, ou use um caminho absoluto. |
| **O twist parece plano** | `setSlices()` está muito baixo, resultando em uma malha grosseira. | Aumente a contagem de slices (ex.: 200) para twists mais suaves. |
| **O twist offset não tem efeito** | O vetor de offset é colinear com a direção da extrusão. | Use um componente X ou Y diferente de zero para ver o deslocamento do offset. |

## Perguntas Frequentes

### Q1: Posso usar Aspose.3D para Java em projetos não comerciais?
**A1:** Sim, o Aspose.3D para Java pode ser usado tanto em projetos comerciais quanto não comerciais. Verifique as [opções de licenciamento](https://purchase.aspose.com/buy) para mais detalhes.

### Q2: Onde posso encontrar suporte para Aspose.3D para Java?
**A2:** Visite o [fórum Aspose.3D para Java](https://forum.aspose.com/c/3d/18) para obter assistência e conectar‑se com a comunidade.

### Q3: Existe uma versão de teste gratuita disponível para Aspose.3D para Java?
**A3:** Sim, você pode experimentar uma versão de teste gratuita na [página de releases](https://releases.aspose.com/).

### Q4: Como obtenho uma licença temporária para Aspose.3D para Java?
**A4:** Obtenha uma licença temporária para seu projeto visitando [este link](https://purchase.aspose.com/temporary-license/).

### Q5: Existem exemplos e tutoriais adicionais disponíveis?
**A5:** Sim, consulte a [documentação](https://reference.aspose.com/3d/java/) para mais exemplos e tutoriais detalhados.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Última atualização:** 2026-02-22  
**Testado com:** Aspose.3D for Java 24.11 (latest)  
**Autor:** Aspose