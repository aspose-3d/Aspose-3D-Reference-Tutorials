---
date: 2025-12-17
description: Aprenda a criar um modelo 3D torcido usando Aspose.3D para Java com torção
  de extrusão linear e exportar o arquivo OBJ em Java. Siga nosso guia passo a passo.
linktitle: Applying Twist in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Criar Modelo 3D Torcido – Aplicando Torção na Extrusão Linear com Aspose.3D
  para Java
url: /pt/java/linear-extrusion/applying-twist/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aplicando Torção na Extrusão Linear com Aspose.3D para Java

## Introdução

Bem‑vindo a este tutorial passo a passo sobre **como criar um modelo 3D torcido** aplicando uma torção durante a extrusão linear usando Aspose.3D para Java. Seja construindo visualizações arquitetônicas, ativos de jogos ou protótipos de engenharia, adicionar uma torção pode dar à sua geometria um aspecto dinâmico e espiralado com apenas algumas linhas de código.

## Respostas Rápidas
- **O que significa “torção” na extrusão?** Ela rotaciona o perfil ao redor do eixo de extrusão à medida que a forma é estendida.  
- **Qual classe da API lida com a torção?** `LinearExtrusion` fornece o método `setTwist`.  
- **Preciso de uma licença para executar o exemplo?** Uma avaliação gratuita funciona para avaliação; uma licença comercial é necessária para produção.  
- **Posso exportar o resultado como OBJ?** Sim, use `scene.save(..., FileFormat.WAVEFRONTOBJ)`.  
- **Qual versão do Java é necessária?** Java 8 ou posterior é totalmente suportado.

## Pré‑requisitos

Antes de mergulhar no tutorial, certifique‑se de que você tem os seguintes pré‑requisitos em vigor:

- **Ambiente de Desenvolvimento Java:** Certifique‑se de que o Java está instalado em seu sistema.  
- **Biblioteca Aspose.3D:** Baixe e instale a biblioteca Aspose.3D para Java a partir do [link de download](https://releases.aspose.com/3d/java/).  
- **Documentação:** Consulte a [documentação do Aspose.3D](https://reference.aspose.com/3d/java/) para orientação abrangente.

## Importar Pacotes

Antes de iniciar o processo de codificação, importe os pacotes necessários para o seu projeto Java. Aqui está um exemplo de como fazer isso:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Definir Diretório do Documento

Primeiro, defina onde o arquivo 3D gerado será salvo.

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## Inicializar Perfil Base

Em seguida, crie a forma que será extrudada. Neste exemplo usamos um retângulo com um pequeno raio de arredondamento.

```java
// ExStart:InitializeBaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:InitializeBaseProfile
```

## Criar uma Cena

Um objeto `Scene` atua como o contêiner para todos os nós 3D.

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
```

## Criar Nós

Adicione dois nós filhos à cena – um permanecerá reto, o outro receberá a torção.

```java
// ExStart:CreateNodes
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CreateNodes
```

## Torção na Extrusão Linear

Agora realizamos **torção na extrusão linear** em ambos os nós. O nó da esquerda recebe uma torção de 0° (reto), enquanto o nó da direita recebe uma torção de 90°, criando uma forma espiralada. Também definimos o número de fatias para garantir geometria suave.

```java
// ExStart:LinearExtrusionWithTwist
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd:LinearExtrusionWithTwist
```

## Exportar Arquivo OBJ Java

Finalmente, salve a cena no formato OBJ amplamente suportado. Isso demonstra a capacidade de **exportar arquivo OBJ Java** do Aspose.3D.

```java
// ExStart:Save3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:Save3DScene
```

## Por Que Isso É Importante

Criar um modelo 3D torcido oferece um efeito visual poderoso sem a necessidade de ferramentas de modelagem externas. É especialmente útil para:

- **Peças mecânicas** que requerem recursos helicoidais (por exemplo, molas, parafusos).  
- **Designs artísticos** onde uma espiral sutil adiciona interesse visual.  
- **Ativos de jogos** que se beneficiam de geometria de baixa polígonos, gerada proceduralmente.

## Problemas Comuns & Dicas

| Problema | Solução |
|----------|---------|
| A torção aparece plana ou ausente | Certifique‑se de que `setSlices` esteja alto o suficiente (por exemplo, 100) para rotação suave. |
| O arquivo OBJ não abre no visualizador | Verifique se o caminho de saída (`MyDir`) está correto e se o arquivo tem permissões de gravação. |
| Escala inesperada | Verifique o sistema de unidades do seu perfil de origem; Aspose.3D trabalha em metros por padrão. |

## Perguntas Frequentes

**P: Posso usar Aspose.3D para Java para trabalhar com outros formatos de arquivo 3D?**  
R: Sim, Aspose.3D suporta uma ampla gama de formatos como FBX, STL, 3MF e mais.

**P: Onde posso encontrar suporte para Aspose.3D para Java?**  
R: Visite o [forum Aspose.3D](https://forum.aspose.com/c/3d/18) para ajuda da comunidade e assistência oficial.

**P: Existe uma versão de avaliação gratuita disponível?**  
R: Sim, você pode baixar uma versão de avaliação a partir de [aqui](https://releases.aspose.com/).

**P: Como obtenho uma licença temporária para testes?**  
R: Obtenha uma licença temporária na [página de licença temporária](https://purchase.aspose.com/temporary-license/).

**P: Onde posso comprar uma licença completa?**  
R: Compre Aspose.3D para Java na [página de compra](https://purchase.aspose.com/buy).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Última atualização:** 2025-12-17  
**Testado com:** Aspose.3D 24.11 for Java  
**Autor:** Aspose  

---