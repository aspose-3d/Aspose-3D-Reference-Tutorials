---
date: 2026-02-20
description: Aprenda um tutorial de gráficos 3D em Java sobre o controle do centro
  na extrusão linear com Aspose.3D, incluindo como definir o raio de arredondamento
  e salvar o arquivo OBJ em Java.
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Tutorial de Gráficos 3D em Java – Centro na Extrusão Linear
url: /pt/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Tutorial de Gráficos 3D em Java – Centro na Extrusão Linear

## Introdução

Se você está criando visualizações 3D em Java, dominar técnicas de extrusão é essencial. Este **java 3d graphics tutorial** orienta você a controlar o centro de uma extrusão linear usando Aspose.3D for Java, permitindo criar modelos precisos e simétricos sem cálculos adicionais. Ao final deste guia você entenderá por que a propriedade `center` é importante, como **definir o raio de arredondamento** e como **salvar OBJ file java**‑compatible.

## Respostas Rápidas
- **O que a propriedade center faz?** Determina se a extrusão é simétrica em torno da origem do perfil.  
- **Preciso de licença para executar o código?** Uma licença temporária funciona para testes; uma licença completa é necessária para produção.  
- **Qual formato de arquivo é usado para o resultado?** A cena é salva como um arquivo Wavefront OBJ.  
- **Posso alterar o número de fatias?** Sim, use `setSlices(int)` no objeto `LinearExtrusion`.  
- **Aspose.3D é compatível com Java 8+?** Absolutamente – suporta todas as versões modernas do Java.

## O que é um java 3d graphics tutorial?

Um **java 3d graphics tutorial** explica passo a passo como usar bibliotecas Java para criar, manipular e renderizar objetos tridimensionais. Neste caso, focamos na API de extrusão da Aspose.3D, que transforma perfis 2‑D em malhas 3‑D completas.

## Por que usar Aspose.3D para Java?

- **API de alto nível** – Não é necessário escrever cálculos de malha de baixo nível.  
- **Suporte a múltiplos formatos** – Exporta para OBJ, FBX, STL e mais.  
- **Desempenho otimizado** – Lida com cenas grandes de forma eficiente.  
- **Documentação rica** – Inclui exemplos como o abaixo.

## Pré‑requisitos

Antes de começar, certifique‑se de que você tem:

1. **Ambiente de Desenvolvimento Java** – JDK 8 ou superior instalado.  
2. **Aspose.3D for Java** – Baixe a biblioteca e a documentação [aqui](https://reference.aspose.com/3d/java/).  
3. **Diretório de Documentos** – Crie uma pasta na sua máquina para armazenar os arquivos gerados; a chamaremos de **“Your Document Directory.”**

## Importar Pacotes

No seu IDE Java, importe as classes da Aspose.3D que você precisará. Isso fornece ao compilador acesso aos recursos de extrusão e construção de cena.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Guia Passo a Passo

### Passo 1: Configurar o Perfil Base

Primeiro, crie a forma 2‑D que será extrudada. Aqui usamos um retângulo e **definimos o raio de arredondamento** para 0.3, o que suaviza os cantos.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### Passo 2: Criar uma Cena 3D

Um objeto `Scene` atua como contêiner para todos os nós 3‑D, luzes e câmeras.

```java
Scene scene = new Scene();
```

### Passo 3: Adicionar Nós Esquerdo e Direito

Colocaremos dois nós separados lado a lado para que você possa comparar a extrusão com e sem centralização.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Passo 4: Extrusão Linear – Sem Centro (Nó Esquerdo)

Crie a extrusão no nó esquerdo, desative a centralização e limite a malha a três fatias para uma visualização low‑poly.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

### Passo 5: Adicionar um Plano de Chão de Referência (Nó Esquerdo)

Uma caixa fina funciona como um piso visual, ajudando a ver a orientação da extrusão.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

### Passo 6: Extrusão Linear – Centralizada (Nó Direito)

Agora repita a extrusão, desta vez habilitando `center`. A geometria será simétrica em torno da origem do perfil.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

### Passo 7: Adicionar um Plano de Chão de Referência (Nó Direito)

Mesmo plano de chão para o lado direito, tornando a comparação clara.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

### Passo 8: Salvar a Cena 3D

Por fim, exporte a cena completa para um arquivo Wavefront OBJ – um formato prontamente utilizável na maioria dos editores 3‑D.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Problemas Comuns e Soluções

| Problema | Por que acontece | Solução |
|----------|------------------|---------|
| **A extrusão aparece deslocada** | `setCenter(false)` deixa o perfil ancorado em seu canto. | Use `setCenter(true)` para resultados simétricos. |
| **Arquivo OBJ está vazio** | O caminho do diretório de saída está incorreto ou faltam permissões de gravação. | Verifique se `MyDir` aponta para uma pasta existente e se a aplicação tem acesso de escrita. |
| **Cantos arredondados parecem afiados** | O raio de arredondamento é muito pequeno em relação ao tamanho do retângulo. | Aumente o valor do raio (ex.: `setRoundingRadius(0.5)`). |

## Perguntas Frequentes

### Q1: Posso usar Aspose.3D para Java em projetos comerciais?

A1: Sim, Aspose.3D for Java está disponível para uso comercial. Para detalhes de licenciamento, visite [aqui](https://purchase.aspose.com/buy).

### Q2: Existe uma versão de avaliação gratuita?

A2: Sim, você pode experimentar uma avaliação gratuita de Aspose.3D for Java [aqui](https://releases.aspose.com/).

### Q3: Onde posso encontrar suporte para Aspose.3D for Java?

A3: O fórum da comunidade Aspose.3D é um ótimo lugar para buscar suporte e compartilhar experiências. Visite o fórum [aqui](https://forum.aspose.com/c/3d/18).

### Q4: Preciso de uma licença temporária para testes?

A4: Sim, se você precisar de uma licença temporária para fins de teste, pode obtê‑la [aqui](https://purchase.aspose.com/temporary-license/).

### Q5: Onde encontro a documentação?

A5: A documentação para Aspose.3D for Java está disponível [aqui](https://reference.aspose.com/3d/java/).

## Conclusão

Ao concluir este **java 3d graphics tutorial**, você agora sabe como controlar o centro de uma extrusão linear, ajustar o raio de arredondamento e **salvar OBJ file java** usando Aspose.3D. Essas técnicas dão controle fino sobre a simetria da malha, essencial para ativos de jogos, protótipos CAD e visualizações científicas. Sinta‑se à vontade para experimentar diferentes perfis, contagens de fatias e formatos de exportação para expandir sua caixa de ferramentas 3‑D.

---

**Última atualização:** 2026-02-20  
**Testado com:** Aspose.3D for Java 24.11  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}