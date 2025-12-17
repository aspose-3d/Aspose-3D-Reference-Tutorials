---
date: 2025-12-09
description: Aprenda a usar o Aspose para criar cilindros personalizados com bases
  chanfradas em Java, ideal para modelagem 3D em Java e para salvar cenas como OBJ.
language: pt
linktitle: 'How to Use Aspose: Create Cylinders with Sheared Bottom in Java'
second_title: Aspose.3D Java API
title: 'Como usar o Aspose: criar cilindros com base chanfrada em Java'
url: /java/cylinders/creating-cylinders-with-sheared-bottom/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Como Usar Aspose: Criar Cilindros com Base Cisalhada em Java

## Introdução

Neste tutorial prático você descobrirá **como usar Aspose** para construir um cilindro cuja base é cisalhada — uma técnica frequentemente necessária em projetos de *modelagem 3d java*. Percorreremos cada passo, desde a configuração da cena até a gravação do modelo final como um arquivo OBJ. Ao final, você terá um trecho de código reutilizável que pode ser inserido em qualquer aplicação 3D baseada em Java.

## Respostas Rápidas
- **O que significa “shear bottom”?** Inclina a base do cilindro por um ângulo especificado no plano XY.  
- **Qual biblioteca cuida da matemática 3D?** Aspose.3D for Java fornece as classes `Cylinder` e `Vector2`.  
- **Preciso de licença para executar o exemplo?** Uma licença temporária funciona para avaliação; uma licença completa é necessária para produção.  
- **Posso exportar o modelo para outros formatos?** Sim — use `scene.save(..., FileFormat.WAVEFRONTOBJ)` para obter um arquivo OBJ.  
- **Qual versão do Java é necessária?** JDK 8 ou superior é suficiente.

## O que significa “how to use aspose” no contexto de modelagem 3D?

Aspose.3D for Java é uma API de alto nível que abstrai as complexidades da geometria 3D, formatos de arquivo e transformações. Em vez de lidar com buffers de vértices de baixo nível, você chama métodos intuitivos como `new Cylinder(...)` e deixa o Aspose fazer o trabalho pesado.

## Por que usar Aspose para Modelagem 3D em Java?

- **Desenvolvimento rápido:** Crie formas complexas com poucas linhas de código.  
- **Amplo suporte a formatos:** Exporte para OBJ, STL, FBX e muito mais.  
- **Multiplataforma:** Funciona em qualquer SO que suporte Java.  
- **API consistente:** O mesmo código funciona em desktop, servidor ou ambientes Android.

## Pré‑requisitos

Antes de começar, certifique‑se de que você tem:

- **Java Development Kit (JDK) 8+** instalado e configurado no seu IDE.  
- **Biblioteca Aspose.3D for Java** adicionada ao classpath do seu projeto. Você pode baixá‑la no site oficial [aqui](https://releases.aspose.com/3d/java/).  
- **Uma licença temporária ou completa** (opcional para execuções de teste).

## Importar Pacotes

Para iniciar, importe as classes essenciais do Aspose.3D e utilitários Java:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Etapa 1: Criar uma Cena

Uma *cena* é o contêiner que contém todos os objetos 3D, luzes e câmeras. Pense nela como o palco onde você colocará seus cilindros.

```java
// ExStart:3
// Create a scene
Scene scene = new Scene();
// ExEnd:3
```

## Etapa 2: Criar Cilindro 1 (Base Cisalhada)

Agora criaremos o primeiro cilindro e aplicaremos uma transformação de cisalhamento à sua base. O método `setShearBottom` recebe um `Vector2` onde o componente X representa o fator de cisalhamento ao longo do eixo X e o componente Y ao longo do eixo Y.

```java
// ExStart:4
// Create cylinder 1
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Customized shear bottom for cylinder 1
cylinder1.setShearBottom(new Vector2(0, 0.83)); // Shear 47.5deg in the xy plane (z-axis)
// Add cylinder 1 to the scene
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

> **Dica profissional:** O fator de cisalhamento `0.83` corresponde a aproximadamente 47,5°; ajuste esse valor para obter o ângulo exato que você precisa.

## Etapa 3: Criar Cilindro 2 (Padrão)

Para comparação, adicionaremos um segundo cilindro sem nenhum cisalhamento. Isso ajuda a visualizar a diferença diretamente no arquivo OBJ exportado.

```java
// ExStart:5
// Create cylinder 2
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// Add cylinder 2 without a ShearBottom to the scene
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

## Etapa 4: Salvar a Cena (Como Salvar a Cena como OBJ)

Por fim, persistimos a cena no disco. A constante `FileFormat.WAVEFRONTOBJ` indica ao Aspose que deve escrever um arquivo OBJ, amplamente suportado por editores 3D como Blender e Maya.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

> **Observação:** Substitua `"Your Document Directory"` por um caminho absoluto ou relativo adequado ao seu ambiente.

## Problemas Comuns e Soluções

| Problema | Causa | Solução |
|----------|-------|----------|
| **Cilindro aparece plano** | Fator de cisalhamento incorreto (fora do intervalo 0‑1) | Use um valor entre 0 e 1; ajuste gradualmente enquanto visualiza. |
| **Arquivo OBJ não carrega no visualizador** | Definições de material ausentes | Adicione um material simples a cada nó ou exporte como STL para teste apenas de geometria. |
| **LicenseException em tempo de execução** | Arquivo de licença inválido ou ausente | Coloque `Aspose.3D.lic` na raiz do projeto ou use a classe `License` para carregá‑lo programaticamente. |

## Perguntas Frequentes

### Q1: Posso usar Aspose.3D for Java com outras bibliotecas 3D Java?
**A:** Aspose.3D for Java foi projetado para funcionar de forma independente. Embora você possa integrá‑lo a outras bibliotecas, ele fornece um conjunto completo de recursos para a maioria das tarefas de modelagem 3D por conta própria.

### Q2: Aspose.3D é adequado para iniciantes em modelagem 3D?
**A:** Sim, Aspose.3D oferece uma API amigável que abstrai detalhes de baixo nível, tornando‑a acessível tanto para iniciantes quanto para desenvolvedores experientes.

### Q3: Onde posso encontrar suporte adicional para Aspose.3D for Java?
**A:** Visite o [fórum Aspose.3D](https://forum.aspose.com/c/3d/18) para suporte da comunidade, tutoriais e discussões.

### Q4: Como obter uma licença temporária para Aspose.3D?
**A:** Você pode obter uma licença temporária [aqui](https://purchase.aspose.com/temporary-license/).

### Q5 Posso comprar Aspose.3D for Java?
**A:** Sim, você pode adquirir Aspose.3D for Java [aqui](https://purchase.aspose.com/buy).

## Conclusão

Percorremos **como usar Aspose** para criar dois cilindros — um com base cisalhada e outro padrão — e, em seguida, salvamos o resultado como um arquivo OBJ. Essa técnica serve como bloco de construção para modelos 3D mais sofisticados, como peças personalizadas, elementos arquitetônicos ou ativos de jogos. Sinta‑se à vontade para experimentar diferentes valores de cisalhamento, raios e alturas para atender às necessidades do seu projeto.

---

**Última atualização:** 2025-12-09  
**Testado com:** Aspose.3D for Java 24.11 (mais recente na data de escrita)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}