---
date: 2026-04-08
description: Aprenda como criar um cilindro com topo deslocado no Aspose.3D para Java,
  adicionar nó filho Java, definir o topo deslocado, gerar o modelo 3D e exportar
  OBJ usando uma licença temporária da Aspose.
keywords:
- aspose temporary license
- generate 3d model
- add child node java
- java export obj
- set offset top
linktitle: Licença Temporária Aspose – Criar Cilindro com Topo Deslocado (Java)
second_title: Aspose.3D Java API
title: Licença Temporária Aspose – Criar Cilindro com Topo Deslocado (Java)
url: /pt/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Licença Temporária Aspose – Criar Cilindro com Topo Deslocado (Java)

## Introdução

Se você está procurando **criar cilindro** objetos com um topo deslocado personalizado em uma cena 3D baseada em Java, o Aspose.3D torna o processo simples. Neste tutorial, percorreremos cada passo — desde a configuração da cena até a exportação do modelo final como um arquivo OBJ — para que você possa integrar cilindros com topo deslocado em suas aplicações com confiança. Ao final do guia, você também entenderá como uma **aspose temporary license** permite avaliar esses recursos sem uma compra completa.

## Respostas Rápidas
- **Qual biblioteca é usada?** Aspose.3D for Java  
- **Posso deslocar o topo de um cilindro?** Sim, usando `setOffsetTop`  
- **Como adiciono um nó filho em Java?** Chame `createChildNode` no nó raiz  
- **Para qual formato posso exportar?** Wavefront OBJ (`java export obj`)  
- **Preciso de uma licença para testes?** Uma **aspose temporary license** está disponível para avaliação  

## O que é Licença Temporária Aspose?

Uma **aspose temporary license** é uma chave de avaliação de curto prazo e gratuita que desbloqueia o conjunto completo de recursos do Aspose.3D for Java durante o desenvolvimento e testes. Ela remove marcas d'água de avaliação e permite gerar arquivos de modelo 3D, como OBJ, STL ou FBX, exatamente como faria uma licença paga.

## Por que usar Aspose.3D para Java?

- **API de alto nível:** Não é necessário gerenciar dados de malha de baixo nível.  
- **Multiplataforma:** Funciona em qualquer ambiente compatível com JVM.  
- **Exportadores integrados:** Salve diretamente em OBJ, STL, FBX e mais.  
- **Extensível:** Adicione facilmente nós filhos, aplique transformações e integre com outras bibliotecas Java.  

## Pré-requisitos

- **Java Development Kit (JDK)** – uma versão compatível instalada.  
- **Aspose.3D for Java library** – faça o download do JAR mais recente no site oficial [aqui](https://releases.aspose.com/3d/java/).  
- Uma IDE de sua escolha (Eclipse, IntelliJ IDEA, NetBeans, etc.).  

## Importar Pacotes

First, import the classes we’ll need. Place these statements at the top of your Java file:

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Guia Passo a Passo

### Passo 1: Criar uma Cena 3D Java

Uma **java 3d scene** atua como o contêiner para todos os objetos 3D.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### Passo 2: Inicializar Cilindro com Topo Deslocado

Aqui respondemos **como criar cilindro** com um deslocamento personalizado. O construtor define raio, altura, fatias, pilhas e se o cilindro está fechado. Depois disso, deslocamos o topo usando `setOffsetTop`.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### Passo 3: Adicionar Nó Filho Java – Anexar o Primeiro Cilindro

Criamos um nó filho sob o nó raiz da cena e movemos o cilindro para a localização desejada.

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### Passo 4: Inicializar um Segundo Cilindro (Sem Deslocamento)

Para comparação, adicionamos um cilindro regular sem deslocamento.

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### Passo 5: Adicionar Nó Filho Java – Anexar o Segundo Cilindro

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Passo 6: Exportar OBJ em Java – Salvar a Cena como OBJ

Finalmente, nós **java export obj** a cena inteira (ambos os cilindros) como um arquivo Wavefront OBJ, amplamente suportado por ferramentas 3D.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

Ao executar o programa, você encontrará `CustomizedOffsetTopCylinder.obj` no diretório especificado, pronto para ser aberto no Blender, Maya ou qualquer outro visualizador compatível com OBJ.

## Como Gerar Modelo 3D e Exportar OBJ em Java

A combinação de `Scene.save(..., FileFormat.WAVEFRONTOBJ)` e a **aspose temporary license** permite que você **generate 3d model** arquivos rapidamente, sem necessidade de conversores externos. Isso é especialmente útil durante a prototipagem ou ao compartilhar ativos com designers.

## Casos de Uso no Mundo Real

- **Visualização arquitetônica:** Cilindros com topo deslocado modelam colunas que afinam em direção ao teto.  
- **Peças mecânicas:** Crie pistões ou carcaças de engrenagens onde a superfície superior é intencionalmente deslocada.  
- **Recursos de jogos:** Produza formas variadas de pilares em tempo real, reduzindo a necessidade de malhas feitas à mão.  

## Problemas Comuns e Soluções

| Problema | Razão | Solução |
|----------|-------|---------|
| **OBJ file is empty** | Cena não salva corretamente ou caminho errado. | Verifique se o diretório de saída existe e se você tem permissões de gravação. |
| **Offset not applied** | Uso de uma versão mais antiga do Aspose.3D. | Atualize para a biblioteca mais recente onde `setOffsetTop` é suportado. |
| **Child node not visible** | Transformação não aplicada. | Certifique‑se de chamar `getTransform().setTranslation` após criar o nó filho. |

## Perguntas Frequentes

**Q: O Aspose.3D é compatível com diferentes IDEs Java?**  
A: Sim, funciona perfeitamente com Eclipse, IntelliJ IDEA, NetBeans e outras IDEs.

**Q: Posso aplicar texturas aos objetos 3D criados?**  
A: Absolutamente! Use a classe `Material` para atribuir texturas e propriedades de superfície.

**Q: Existem opções de licenciamento para Aspose.3D?**  
A: Vários modelos de licenciamento estão disponíveis; você pode explorá‑los [aqui](https://purchase.aspose.com/buy).

**Q: Como posso obter ajuda ou compartilhar experiências?**  
A: Participe do fórum da comunidade Aspose.3D [aqui](https://forum.aspose.com/c/3d/18) para suporte e discussão.

**Q: Uma licença temporária está disponível para testes?**  
A: Sim, uma **aspose temporary license** pode ser obtida para avaliação [aqui](https://purchase.aspose.com/temporary-license/).

**Última atualização:** 2026-04-08  
**Testado com:** Aspose.3D for Java 24.12 (latest)  
**Autor:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}