---
date: 2026-02-22
description: Aprenda como definir a direção na extrusão linear e exportar modelo 3D
  OBJ usando Aspose.3D para Java. Siga nosso guia passo a passo.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Como Definir a Direção na Extrusão Linear com Aspose.3D para Java
url: /pt/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Como Definir a Direção na Extrusão Linear com Aspose.3D para Java

## Introdução

Neste tutorial abrangente, você descobrirá **como definir a direção** ao realizar uma extrusão linear com Aspose.3D para Java. Seja construindo uma ferramenta semelhante a CAD ou gerando geometria para um motor de jogo, controlar a direção da extrusão permite criar exatamente a forma que você precisa. Percorreremos cada passo, desde a inicialização de um perfil até a gravação do resultado como um arquivo OBJ, para que você também possa **exportar arquivos de modelo 3d obj** diretamente do Java.

## Respostas Rápidas
- **Qual é a classe principal para extrusão linear?** `LinearExtrusion`
- **Qual método define a direção da extrusão?** `setDirection(Vector3 direction)`
- **Posso exportar o resultado como OBJ?** Sim, usando `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **Preciso de uma licença para desenvolvimento?** Um teste gratuito está disponível; uma licença é necessária para produção.
- **Qual IDE Java funciona melhor?** IntelliJ IDEA ou Eclipse são ambos totalmente suportados.

## O que é Extrusão Linear?

A extrusão linear pega um perfil 2‑D (como um retângulo ou círculo) e o estende ao longo de uma linha reta para criar um sólido 3‑D. Por padrão, a extrusão segue o eixo Z positivo, mas o Aspose.3D permite alterar esse caminho com a propriedade `setDirection`.

## Por que Definir a Direção na Extrusão Linear?

- Alinhar a geometria com objetos existentes em uma cena.
- Criar peças inclinadas ou anguladas sem etapas adicionais de transformação.
- Exportar modelos que precisam corresponder a um sistema de coordenadas específico (por exemplo, para impressão 3‑D ou motores de jogo).

## Pré-requisitos

- Conhecimento básico de Java.
- Biblioteca Aspose.3D instalada. Você pode baixá‑la [aqui](https://releases.aspose.com/3d/java/).
- Uma IDE como Eclipse ou IntelliJ IDEA.

## Importar Pacotes

Primeiro, importe os namespaces que fornecem as classes principais 3‑D e tipos utilitários.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Etapa 1: Inicializar o Perfil Base

Crie a forma que será extrudada. Neste exemplo, usamos um `RectangleShape` com um pequeno raio de arredondamento para dar às bordas um aspecto suave.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Etapa 2: Criar uma Cena

Um objeto `Scene` funciona como um contêiner para todos os nós 3‑D, luzes, câmeras e materiais.

```java
Scene scene = new Scene();
```

## Etapa 3: Criar Nós

Adicione dois nós filhos à raiz da cena — um para a extrusão à esquerda e outro para a extrusão à direita. O nó da direita é transladado para que os dois objetos não se sobreponham.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Etapa 4: Executar a Extrusão Linear no Nó da Esquerda

Extruda o perfil no nó da esquerda usando a direção padrão do eixo Z. Também adicionamos uma torção completa de 360° e aumentamos a contagem de fatias para uma malha mais suave.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Etapa 5: Executar a Extrusão Linear no Nó da Direita com Direção

É aqui que **definimos a direção**. Ao passar um `Vector3` personalizado para `setDirection`, a extrusão segue o vetor (0.3, 0.2, 1), produzindo uma forma inclinada.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Etapa 6: Salvar a Cena 3D

Finalmente, exporte a cena para o formato Wavefront OBJ. Esta etapa demonstra como **salvar arquivos obj java** e facilita a visualização do resultado em qualquer visualizador 3‑D.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Problemas Comuns e Soluções

| Problema | Por que acontece | Correção |
|----------|------------------|----------|
| O arquivo OBJ aparece vazio | O perfil não foi adicionado a um nó | Certifique-se de que `createChildNode` seja chamado em um nó válido |
| A direção parece não ter sido alterada | `setDirection` foi chamado após a extrusão já ter sido construída | Defina a direção dentro do inicializador `LinearExtrusion` conforme mostrado |
| Malha de baixa resolução | O valor de `setSlices` está muito baixo | Aumente a contagem de fatias (por exemplo, 100 ou mais) |

## Conclusão

Agora você sabe **como definir a direção** em uma extrusão linear, como ajustar as configurações de torção e fatias, e como **exportar arquivos de modelo 3d obj** usando Aspose.3D para Java. Essas técnicas fornecem controle detalhado sobre a criação de geometria e facilitam a integração de ativos 3‑D em pipelines maiores.

## Perguntas Frequentes

### Q1: Posso usar o Aspose.3D com outras linguagens de programação?

A1: O Aspose.3D suporta várias linguagens de programação, incluindo .NET e Java.

### Q2. Existe um teste gratuito disponível para o Aspose.3D?

A2: Sim, você pode explorar os recursos do Aspose.3D com um teste gratuito [aqui](https://releases.aspose.com/).

### Q3: Onde posso encontrar documentação detalhada do Aspose.3D para Java?

A3: A documentação completa está disponível [aqui](https://reference.aspose.com/3d/java/).

### Q4: Como posso obter suporte para o Aspose.3D?

A4: Visite o [fórum Aspose.3D](https://forum.aspose.com/c/3d/18) para qualquer assistência ou dúvidas.

### Q5: Licenças temporárias estão disponíveis para o Aspose.3D?

A5: Sim, você pode obter uma licença temporária [aqui](https://purchase.aspose.com/temporary-license/).

---

**Última Atualização:** 2026-02-22  
**Testado com:** Aspose.3D para Java (versão mais recente)  
**Autor:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
