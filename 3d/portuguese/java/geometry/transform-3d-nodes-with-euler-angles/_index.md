---
date: 2025-12-13
description: Aprenda a usar o Aspose 3D Java para transformar nós 3D. Este guia mostra
  como usar ângulos de Euler, adicionar rotação 3D e definir a translação em Java.
linktitle: Aspose 3D Java – Transform 3D Nodes with Euler Angles
second_title: Aspose.3D Java API
title: Aspose 3D Java – Transformar nós 3D com ângulos de Euler
url: /pt/java/geometry/transform-3d-nodes-with-euler-angles/
weight: 19
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Transformar nós 3D com ângulos de Euler em Java usando Aspose.3D

## Introdução

Neste tutorial você descobrirá **como usar aspose 3d java** para transformar nós 3D aplicando ângulos de Euler. Ao final do guia você será capaz de adicionar rotação 3d, definir tradução java e criar cenas dinâmicas que reagem a dados em tempo real.

## Respostas rápidas
- **Qual biblioteca lida com transformações 3D em Java?** Aspose 3D for Java.  
- **Qual método define rotação usando ângulos de Euler?** `setEulerAngles()` na transformação do nó.  
- **Como mover um nó no espaço?** Use `setTranslation()` com um `Vector3`.  
- **Preciso de licença para produção?** Sim, é necessária uma licença comercial do Aspose 3D.  
- **Posso exportar para FBX?** Absolutamente – `scene.save(..., FileFormat.FBX7500ASCII)` funciona imediatamente.

## Pré-requisitos

Antes de mergulharmos no tutorial, certifique‑se de que você tem os seguintes pré-requisitos configurados:

- Conhecimento básico de programação Java.  
- Java Development Kit (JDK) instalado na sua máquina.  
- Biblioteca Aspose.3D, que você pode obter em [Aspose.3D Java Documentation](https://reference.aspose.com/3d/java/).

## Importar Pacotes

Comece importando os pacotes necessários para o seu projeto Java. Certifique‑se de que a biblioteca Aspose.3D esteja corretamente adicionada ao seu classpath. Se ainda não a baixou, você pode encontrar o link de download [aqui](https://releases.aspose.com/3d/java/).

```java
import com.aspose.threed.*;
```

## aspose 3d java – Trabalhando com Ângulos de Euler

### Passo 1. Inicializar Cena e Nó

Primeiro, crie uma cena e um nó que conterá a geometria que você deseja transformar.

```java
// ExStart:AddTransformationToNodeByEulerAngles
// Initialize scene object
Scene scene = new Scene();

// Initialize Node class object
Node cubeNode = new Node("cube");
```

### Passo 2. Criar Malha e Definir Geometria

Em seguida, gere uma malha simples (um cubo neste caso) e anexe‑a ao nó.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Point node to the Mesh geometry
cubeNode.setEntity(mesh);
```

## Adicionar Rotação 3D a um Nó

### Passo 3. Definir Ângulos de Euler e Translação

Agora aplicamos a rotação usando ângulos de Euler e também movemos o nó para uma posição visível.

```java
// Euler angles
cubeNode.getTransform().setEulerAngles(new Vector3(0.3, 0.1, -0.5));

// Set translation
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## Definir Translação Java – Posicionando o Nó

A etapa de translação acima demonstra **set translation java** na prática: o nó é deslocado 20 unidades ao longo do eixo Z para que você possa vê‑lo após a renderização.

## Passo 4. Adicionar Nó à Cena

Anexe o nó transformado ao nó raiz da cena.

```java
// Add cube to the scene
scene.getRootNode().getChildNodes().add(cubeNode);
```

## Passo 5. Salvar Cena 3D

Finalmente, exporte a cena para um arquivo FBX (ou qualquer outro formato suportado).

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByEulerAngles
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

Certifique‑se de substituir `"Your Document Directory"` pelo caminho apropriado na sua máquina.

## Conclusão

Parabéns! Você transformou nós 3D com sucesso usando ângulos de Euler em Java com **aspose 3d java**. Experimente diferentes ângulos e translações para criar cenas 3D dinâmicas e envolventes.

## Perguntas Frequentes

### Q1: Posso usar Aspose.3D para Java em projetos comerciais?

A1: Sim, você pode. Visite a [página de compra](https://purchase.aspose.com/buy) para detalhes de licenciamento.

### Q2: Onde posso encontrar suporte para Aspose.3D?

A2: O [fórum Aspose.3D](https://forum.aspose.com/c/3d/18) é o local para buscar assistência e conectar‑se com a comunidade.

### Q3: Existe uma versão de avaliação gratuita disponível?

A3: Sim, você pode explorar o [teste gratuito](https://releases.aspose.com/) para experimentar as capacidades do Aspose.3D.

### Q4: Como posso obter uma licença temporária?

A4: Você pode obter uma licença temporária [aqui](https://purchase.aspose.com/temporary-license/).

### Q5: Onde posso encontrar a documentação?

A5: A [documentação](https://reference.aspose.com/3d/java/) fornece orientações abrangentes sobre o uso do Aspose.3D para Java.

## Perguntas Frequentes

**Q: Qual é a diferença entre ângulos de Euler e rotação por quaternion?**  
**A:** Ângulos de Euler são intuitivos (pitch, yaw, roll), mas podem sofrer de gimbal lock, enquanto quaternions evitam esse problema e são melhores para interpolações suaves.

**Q: Posso encadear múltiplas transformações no mesmo nó?**  
**A:** Sim. Chame `setEulerAngles`, `setTranslation` e `setScale` em qualquer ordem; a biblioteca as compõe em uma única matriz de transformação.

**Q: É possível exportar para outros formatos como OBJ ou STL?**  
**A:** Absolutamente. Substitua `FileFormat.FBX7500ASCII` por `FileFormat.OBJ` ou `FileFormat.STL` na chamada `scene.save`.

**Q: Como aplicar a mesma rotação a vários nós ao mesmo tempo?**  
**A:** Crie um nó pai, aplique a rotação ao pai e adicione nós filhos sob ele. Todos os filhos herdam a transformação.

**Q: Preciso chamar algum método de limpeza após salvar?**  
**A:** O coletor de lixo do Java lida com a maioria dos recursos, mas você pode chamar explicitamente `scene.dispose()` se trabalhar com cenas grandes em uma aplicação de longa duração.

---

**Última atualização:** 2025-12-13  
**Testado com:** Aspose.3D 23.12 for Java  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}