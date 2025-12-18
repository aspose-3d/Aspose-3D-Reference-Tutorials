---
date: 2025-12-18
description: Aprenda como adicionar um plano de base e definir a propriedade center
  na extrusão linear usando Aspose.3D para Java, com exemplos de código passo a passo.
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Como adicionar plano de base e centro de controle em extrusão linear com Aspose.3D
  para Java
url: /pt/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Controle do Centro em Extrusão Linear com Aspose.3D para Java

## Introdução

Ao criar cenas 3D em Java, a capacidade de **add ground plane** enquanto define precisamente a **set center property** em uma extrusão linear pode fazer a diferença entre um protótipo simples e uma visualização polida. Neste tutorial, percorreremos todo o processo de controlar o centro da extrusão e adicionar um plano de base usando Aspose.3D para Java. Você verá por que isso é importante, como configurá‑lo e obterá um exemplo de código pronto‑para‑executar que pode adaptar aos seus próprios projetos.

## Respostas Rápidas
- **O que “add ground plane” faz?** Ele cria uma geometria de referência fina que ajuda a visualizar a posição da extrusão em relação aos eixos do mundo.  
- **Como definir o centro de uma extrusão linear?** Use o método `setCenter(boolean)` no objeto `LinearExtrusion`.  
- **Preciso de uma licença para executar o exemplo?** Uma licença temporária funciona para testes; uma licença completa é necessária para produção.  
- **Qual formato de arquivo é usado para salvar?** O exemplo salva em Wavefront OBJ (`.obj`).  
- **Qual versão do Java é necessária?** Java 8 ou superior é suficiente.

## O que é “add ground plane” em uma cena 3D?

Adicionar um ground plane significa inserir uma geometria retangular fina (geralmente uma caixa com espessura mínima) que fica no plano X‑Z. Ela funciona como um piso visual, facilitando a avaliação da altura e alinhamento de outros objetos, especialmente quando você está experimentando com centros de extrusão.

## Por que definir a propriedade center em uma extrusão linear?

Por padrão, uma extrusão linear inicia a partir da origem do perfil. Definir a propriedade center (`setCenter(true)`) desloca o perfil de modo que a extrusão fique centralizada em torno da origem, o que é útil para designs simétricos ou quando você precisa de alinhamento consistente entre vários objetos.

## Pré‑requisitos

Antes de embarcarmos nesta jornada de tutorial, certifique‑se de que você tem os seguintes pré‑requisitos configurados:

1. **Java Development Environment** – Certifique‑se de que você tem um ambiente de desenvolvimento Java configurado na sua máquina.  
2. **Aspose.3D for Java** – Baixe e instale a biblioteca Aspose.3D. Você pode encontrar a biblioteca e sua documentação [aqui](https://reference.aspose.com/3d/java/).  
3. **Document Directory** – Crie um diretório para armazenar seus documentos Java. Vamos chamá‑lo de “Your Document Directory.”

## Importar Pacotes

No seu ambiente de desenvolvimento Java, importe os pacotes necessários para Aspose.3D. Isso garante que seu código tenha acesso às funcionalidades fornecidas pela biblioteca.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Etapa 1: Configurar o Perfil Base

Inicialize o perfil base a ser extrudado. Neste exemplo, usaremos uma forma retangular com raio de arredondamento de 0,3.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Etapa 2: Criar uma Cena 3D

Construa a base do seu mundo 3D criando uma cena.

```java
Scene scene = new Scene();
```

## Etapa 3: Criar Nós Esquerdo e Direito

Estabeleça nós esquerdo e direito dentro da sua cena. Esses nós servem como tela para seus objetos 3D.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Etapa 4: Extrusão Linear com Propriedade Center (Nó Esquerdo)

Execute a extrusão linear no nó esquerdo **sem centralizar** e defina o número de fatias para 3. Observe a chamada `setCenter(false)` – é aqui que **set center property** é definido como *false*.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## Etapa 5: Adicionar Ground Plane para Referência (Nó Esquerdo)

Melhore a representação visual **adicionando um ground plane** ao nó esquerdo. A caixa fina funciona como um piso para que você possa ver claramente a altura da extrusão.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## Etapa 6: Extrusão Linear com Propriedade Center (Nó Direito)

Agora execute a extrusão linear no nó direito, desta vez **centralizando a extrusão**. A chamada `setCenter(true)` demonstra como **set center property** é definido como *true*.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## Etapa 7: Adicionar Ground Plane para Referência (Nó Direito)

Assim como no lado esquerdo, adicione um ground plane ao nó direito para uma base visual consistente.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## Etapa 8: Salvar a Cena 3D

Salve sua cena 3D no formato Wavefront OBJ para que você possa visualiz‑la em qualquer visualizador 3D padrão.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Problemas Comuns e Soluções

| Problema | Por que acontece | Correção |
|----------|------------------|----------|
| Ground plane não visível | A espessura da caixa é muito pequena para a escala do visualizador. | Aumente a espessura (primeiro parâmetro de `Box`) ou afaste o zoom no visualizador. |
| Extrusão aparece deslocada | Valor de `setCenter` não definido como pretendido. | Verifique novamente o boolean passado para `setCenter`. |
| Arquivo não salvo | Caminho do diretório incorreto ou permissões de gravação ausentes. | Verifique se `MyDir` aponta para uma pasta existente com acesso de gravação. |

## Perguntas Frequentes

**Q1: Posso usar Aspose.3D for Java em projetos comerciais?**  
A1: Sim, Aspose.3D for Java está disponível para uso comercial. Para detalhes de licenciamento, visite [aqui](https://purchase.aspose.com/buy).

**Q2: Existe uma versão de avaliação gratuita?**  
A2: Sim, você pode experimentar uma avaliação gratuita do Aspose.3D for Java [aqui](https://releases.aspose.com/).

**Q3: Onde posso encontrar suporte para Aspose.3D for Java?**  
A3: O fórum da comunidade Aspose.3D é um ótimo lugar para buscar suporte e compartilhar suas experiências. Visite o fórum [aqui](https://forum.aspose.com/c/3d/18).

**Q4: Preciso de uma licença temporária para testes?**4: Sim, se você precisar de uma licença temporária para fins de teste, pode obtê‑la [aqui](https://purchase.aspose.com/temporary-license/).

**Q5: Onde posso encontrar a documentação?**  
A5: A documentação do Aspose.3D for Java está disponível [aqui](https://reference.aspose.com/3d/java/).

## Conclusão

Controlar o centro em extrusão linear **e** aprender a **add ground plane** com Aspose.3D para Java abre possibilidades empolgantes no desenvolvimento de gráficos 3D. Seguindo as etapas acima, você agora tem um padrão reutilizável para criar extrusões centralizadas, planos de referência visual e exportar o resultado para OBJ. Sinta‑se à vontade para experimentar diferentes perfis, contagens de fatias e transformações para atender às necessidades do seu projeto.

---

**Última atualização:** 2025-12-18  
**Testado com:** Aspose.3D 24.11 for Java (latest at time of writing)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}