---
date: 2025-12-05
description: Aprenda a criar modelos de cilindro com topos deslocados no Aspose.3D
  para Java, adicione etapas de nó filho em Java e exporte arquivos OBJ de modelos
  3D facilmente.
linktitle: How to Create Cylinder with Offset Top in Aspose.3D for Java
second_title: Aspose.3D Java API
title: Como criar um cilindro com topo deslocado no Aspose.3D para Java
url: /pt/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Como Criar Cilindro com Topo Deslocado no Aspose.3D para Java

## Introdução

Se você está procurando **how to create cylinder** objetos com um topo deslocado personalizado em uma cena 3D baseada em Java, o Aspose.3D torna o processo simples. Neste tutorial, percorreremos cada passo — desde a configuração da cena até a exportação do modelo final como um arquivo OBJ — para que você possa integrar cilindros com topo deslocado em suas aplicações com confiança.

## Respostas Rápidas
- **Qual biblioteca é usada?** Aspose.3D for Java  
- **Posso deslocar o topo de um cilindro?** Sim, usando `setOffsetTop`  
- **Como adiciono um nó filho em Java?** Chame `createChildNode` no nó raiz  
- **Para qual formato posso exportar?** Wavefront OBJ (`export 3d model obj`)  
- **Preciso de licença para testes?** Uma licença temporária está disponível para avaliação  

## O que é “how to create cylinder” com um topo deslocado?

Criar um cilindro com um topo deslocado significa que a face circular superior é deslocada em relação à base, permitindo modelar formas cônicas ou assimétricas sem manipulação manual de vértices. O Aspose.3D fornece um construtor dedicado e uma propriedade `OffsetTop` para alcançar isso em apenas algumas linhas de código.

## Por que usar Aspose.3D para Java?

- **API de alto nível:** Não é necessário gerenciar dados de malha de baixo nível.  
- **Multiplataforma:** Funciona em qualquer ambiente compatível com JVM.  
- **Exportadores integrados:** Salve diretamente em OBJ, STL, FBX e mais.  
- **Extensível:** Adicione facilmente nós filhos, aplique transformações e integre com outras bibliotecas Java.

## Pré‑requisitos

Antes de começar, certifique‑se de que você tem:

- **Java Development Kit (JDK)** – uma versão compatível instalada.  
- **Aspose.3D for Java library** – faça download do JAR mais recente no site oficial [aqui](https://releases.aspose.com/3d/java/).  
- Uma IDE de sua escolha (Eclipse, IntelliJ IDEA, NetBeans, etc.).

## Importar Pacotes

Primeiro, importe as classes que iremos precisar. Coloque estas instruções no topo do seu arquivo Java:

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Guia Passo a Passo

### Etapa 1: Criar uma Cena

Uma cena funciona como o contêiner para todos os objetos 3D.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### Etapa 2: Inicializar Cilindro com Topo Deslocado

Aqui respondemos **how to create cylinder** com um deslocamento personalizado. O construtor define raio, altura, fatias, pilhas e se o cilindro está fechado. Em seguida, deslocamos o topo usando `setOffsetTop`.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### Etapa 3: Como **add child node Java** – Anexar o Primeiro Cilindro

Criamos um nó filho sob o nó raiz da cena e movemos o cilindro para a localização desejada.

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### Etapa 4: Inicializar um Segundo Cilindro (Sem Deslocamento)

Para comparação, adicionamos um cilindro regular sem deslocamento.

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### Etapa 5: Como **add child node Java** – Anexar o Segundo Cilindro

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Etapa 6: Como **export 3d model OBJ** – Salvar a Cena

Finalmente, exportamos toda a cena (ambos os cilindros) como um arquivo Wavefront OBJ, amplamente suportado por ferramentas 3D.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

Ao executar o programa, você encontrará `CustomizedOffsetTopCylinder.obj` no diretório especificado, pronto para ser aberto no Blender, Maya ou qualquer outro visualizador compatível com OBJ.

## Problemas Comuns e Soluções

| Problema | Motivo | Solução |
|----------|--------|---------|
| **Arquivo OBJ está vazio** | Cena não salva corretamente ou caminho errado. | Verifique se o diretório de saída existe e se você tem permissão de gravação. |
| **Deslocamento não aplicado** | Uso de uma versão antiga do Aspose.3D. | Atualize para a biblioteca mais recente onde `setOffsetTop` é suportado. |
| **Nó filho não visível** | Transformação não aplicada. | Certifique‑se de chamar `getTransform().setTranslation` após criar o nó filho. |

## Perguntas Frequentes

**Q: O Aspose.3D é compatível com diferentes IDEs Java?**  
A: Sim, funciona perfeitamente com Eclipse, IntelliJ IDEA, NetBeans e outras IDEs.

**Q: Posso aplicar texturas aos objetos 3D criados?**  
A: Absolutamente! Use a classe `Material` para atribuir texturas e propriedades de superfície.

**Q: Existem opções de licenciamento para o Aspose.3D?**  
A: Diversos modelos de licenciamento estão disponíveis; você pode explorá‑los [aqui](https://purchase.aspose.com/buy).

**Q: Como posso obter ajuda ou compartilhar experiências?**  
A: Participe do fórum da comunidade Aspose.3D [aqui](https://forum.aspose.com/c/3d/18) para suporte e discussões.

**Q: Uma licença temporária está disponível para testes?**  
A: Sim, uma licença temporária pode ser obtida para avaliação [aqui](https://purchase.aspose.com/temporary-license/).

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---
**Última Atualização:** 2025-12-05  
**Testado Com:** Aspose.3D for Java 24.12 (latest)  
**Autor:** Aspose