---
date: 2026-11-17
description: Como reduzir o tamanho de modelo 3D gerando uma malha de esfera em Java
  e comprimindo-a com Google Draco via Aspose.3D. Aprenda todo o fluxo de trabalho
  em minutos.
images:
- /java/3d-mesh-data/compress-meshes-google-draco/og-image.png
keywords:
- create sphere mesh
- how to compress 3d
- reduce 3d model size
- aspose 3d java
- compress 3d mesh
lastmod: 2026-11-17
linktitle: Como Reduzir o Tamanho de Modelo 3D – Criar Malha de Esfera em Java Usando
  Google Draco
og_description: Criar malha de esfera e comprimir modelo 3D com Java usando Aspose.3D
  e Google Draco. Este tutorial mostra como gerar uma esfera, exportar para .drc e
  alcançar até 95% de redução de tamanho em minutos.
og_image_alt: 'Developer guide: Reduce 3d model size with Java sphere mesh and Draco
  compression'
og_title: Criar malha de esfera e comprimir modelo 3D com Java e Draco
schemas:
- author: Aspose
  dateModified: '2026-11-17'
  description: How to reduce 3d model size by generating a sphere mesh in Java and
    compressing it with Google Draco via Aspose.3D. Learn the full workflow in minutes.
  headline: How to reduce 3d model size with a Java sphere mesh and Draco
  type: TechArticle
- description: How to reduce 3d model size by generating a sphere mesh in Java and
    compressing it with Google Draco via Aspose.3D. Learn the full workflow in minutes.
  name: How to reduce 3d model size with a Java sphere mesh and Draco
  steps:
  - name: set up the project
    text: Create a new Java project (any IDE works) and add all Aspose.3D JARs to
      the classpath. Keep your source files in a package such as `com.example.draco`
      for clarity.
  - name: how to create sphere mesh in Java
    text: 'The `Sphere` class is Aspose.3D''s built‑in geometry generator that produces
      a triangulated mesh with a configurable radius and tessellation. > **Pro tip:**
      The `Sphere` class generates a triangulated mesh with a default radius of 1.0.
      You can pass custom radius, tessellation, or material parameters '
  - name: export the mesh to Draco format
    text: After the sphere is added to a `Scene` object, call `scene.save("sphere.drc",
      SaveFormat.Draco)`. Aspose.3D automatically selects optimal compression settings,
      but you can fine‑tune them by adjusting `DracoCompressionOptions` if you need
      the smallest possible file. `DracoCompressionOptions` lets you
  - name: verify the output
    text: Open the generated `.drc` file with a Draco viewer (e.g., three.js `DRACOLoader`)
      to ensure the geometry renders correctly. You’ll notice a dramatic reduction
      in file size—often a factor of ten or more.
  type: HowTo
- questions:
  - answer: Yes, Aspose.3D supports OBJ, FBX, STL, GLTF, and many others, making it
      a versatile choice for **Aspose 3d export** pipelines.
    question: Is Aspose.3D compatible with different 3d file formats?
  - answer: Absolutely. Draco offers native libraries for C++, Python, and JavaScript.
      This tutorial focuses on Java, but the concepts apply across languages.
    question: Can I use Google Draco for compression in other programming languages?
  - answer: Visit the **[Aspose.3D Java documentation](https://reference.aspose.com/3d/java/)**
      for full API references and more examples.
    question: Where can I find additional Aspose.3D documentation?
  - answer: Explore temporary licensing options on the **[Aspose temporary license
      page](https://purchase.aspose.com/temporary-license/)**.
    question: How do I obtain a temporary license for Aspose.3D?
  - answer: Yes, join the discussion at the **[Aspose.3D Forum](https://forum.aspose.com/c/3d/18)**.
    question: Is there a community forum for Aspose.3D support?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- reduce 3d model size
- Aspose.3D
- Java 3D compression
- Google Draco
- sphere mesh
title: Como reduzir o tamanho de modelo 3D com uma malha de esfera em Java e Draco
url: /pt/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Como reduzir o tamanho de modelo 3d com uma malha de esfera Java e Draco

## Introdução

Aspose.3D for Java é uma biblioteca que permite a criação, manipulação e conversão de modelos 3‑D diretamente a partir de código Java. Se você está procurando uma maneira rápida de **reduzir o tamanho de modelo 3d** enquanto ainda entrega geometria de alta qualidade, você chegou ao lugar certo. Neste tutorial, vamos percorrer a geração de uma malha de esfera com **Aspose.3D for Java** e então comprimir essa malha usando **Google Draco**. Ao final, você terá um arquivo `.drc` pronto para uso que é dramaticamente menor que o original, tornando-o perfeito para visualizadores baseados na web, jogos móveis ou qualquer aplicação Java com largura de banda limitada.

## Respostas rápidas
- **O que este tutorial cobre?** Criação de uma malha de esfera em Java e compressão com Google Draco via Aspose.3D.  
- **Biblioteca principal?** Aspose.3D for Java (usada tanto para criação da malha quanto para exportação Draco).  
- **Tempo típico de implementação?** Cerca de 10‑15 minutos para uma esfera básica.  
- **Pré-requisito chave?** Um ambiente de desenvolvimento Java com os JARs do Aspose.3D no classpath.  
- **Resultado?** Um arquivo `.drc` que **reduz o tamanho do modelo 3d** em até 95 % comparado a uma malha não comprimida.

## Como reduzir o tamanho de modelo 3d?

Carregue sua esfera e comprima‑a em duas etapas simples. Primeiro, você **cria a malha da esfera** com `new Sphere(1.0, 32, 32)`. Em seguida, exporta a cena diretamente para Draco usando `scene.save("sphere.drc", SaveFormat.Draco)`. Aspose.3D lida com quantização de geometria e deduplicação de vértices automaticamente, entregando arquivos que são tipicamente 80‑95 % menores enquanto preservam a fidelidade visual.

A classe `Sphere` é o gerador de geometria embutido do Aspose.3D que cria uma malha de esfera triangulada. Ela aceita um raio e parâmetros de tesselação, permitindo que você controle o nível de detalhe antes da compressão.

## O que significa “reduzir o tamanho de modelo 3d” no contexto do desenvolvimento 3d?

**Reduzir o tamanho de modelo 3d** significa diminuir a quantidade de dados de geometria que precisam ser transferidos ou armazenados, sem degradar perceptivelmente a qualidade visual. Draco consegue isso codificando posições de vértices, normais e outros atributos em um formato binário altamente compacto. Quando combinado com Aspose.3D, todo o fluxo de trabalho permanece dentro do Java, de modo que você não precisa lidar com binários nativos.

## Por que usar compressão de malha Google Draco com Aspose.3D?

Google Draco combinado com Aspose.3D fornece um pipeline eficiente que reduz drasticamente os arquivos de malha enquanto os mantém fáceis de integrar em projetos Java. A biblioteca lida com toda a codificação de baixo nível, permitindo que os desenvolvedores se concentrem na criação de geometria sem lidar com binários nativos do Draco, resultando em desenvolvimento mais rápido e ativos menores para web e dispositivos móveis.

- **Redução massiva de tamanho:** Draco pode reduzir os dados da malha em até 95 % para modelos típicos, transformando um OBJ de 5 MB em um `.drc` de 0.3 MB.  
- **Decodificação rápida em tempo de execução:** Engines como Unity, Unreal e three.js decodificam Draco nativamente, levando a tempos de carregamento mais rápidos.  
- **Integração Java perfeita:** Aspose.3D abstrai a biblioteca nativa Draco, permitindo que você permaneça no ecossistema Java.  
- **Exportação única Aspose 3D:** A mesma API que você usa para criar geometria também lida com a exportação, simplificando o pipeline.  

Aspose.3D suporta **mais de 50 formatos de entrada e saída** — incluindo OBJ, FBX, STL, GLTF e muitos outros — e pode processar modelos de centenas de páginas sem carregar o arquivo inteiro na memória.

## Pré-requisitos

- **Java Development Kit (JDK)** – versão 8 ou superior.  
- **Aspose.3D for Java** – faça download dos JARs mais recentes na **[página de lançamentos Aspose 3D Java](https://releases.aspose.com/3d/java/)**.  
- **Familiaridade básica com Google Draco** – você usará o wrapper do Aspose.3D, portanto não é necessário configurar o Draco nativo.

## Importar pacotes

```java
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Sphere;


import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

## Guia passo a passo

### Passo 1: configurar o projeto

Crie um novo projeto Java (qualquer IDE funciona) e adicione todos os JARs do Aspose.3D ao classpath. Mantenha seus arquivos fonte em um pacote como `com.example.draco` para clareza.

### Passo 2: como criar uma malha de esfera em Java

A classe `Sphere` é o gerador de geometria embutido do Aspose.3D que cria uma malha de esfera triangulada.  

```java
import java.nio.file.Files;
import java.nio.file.Paths;
import com.aspose.threed.Sphere;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.FileFormat;

// ExStart:Encode3DMeshinGoogleDraco
// The path to the documents directory.
String MyDir = "Your Document Directory";

// Create a sphere
Sphere sphere = new Sphere();

// Encode the sphere to Google Draco raw data using optimal compression level.
DracoSaveOptions opt = new DracoSaveOptions();
opt.setCompressionLevel(DracoCompressionLevel.OPTIMAL);
byte[] b = FileFormat.DRACO.encode(sphere.toMesh(), opt);

// Save the raw bytes to file
Files.write(Paths.get(MyDir, "SphereMeshtoDRC_Out.drc"), b);
// ExEnd:Encode3DMeshinGoogleDraco
```

> **Dica profissional:** A classe `Sphere` gera uma malha triangulada com raio padrão de 1.0. Você pode passar um raio personalizado, tesselação ou parâmetros de material se precisar de um nível de detalhe diferente antes da compressão.

### Passo 3: exportar a malha para o formato Draco

A classe `Scene` representa uma cena 3‑D completa que pode conter malhas, luzes e câmeras. A classe `DracoCompressionOptions` permite personalizar as configurações de compressão Draco, como quantização e nível de compressão. Após a esfera ser adicionada a um objeto `Scene`, chame `scene.save("sphere.drc", SaveFormat.Draco)`. Aspose.3D seleciona automaticamente as configurações de compressão ideais, mas você pode ajustá-las finamente modificando `DracoCompressionOptions` se precisar do arquivo o menor possível. `DracoCompressionOptions` permite

### Passo 4: verificar a saída

O `DRACOLoader` é uma utilidade do three.js que carrega arquivos `.drc` comprimidos com Draco e os converte em geometria compatível com WebGL. Abra o arquivo `.drc` gerado com um visualizador Draco (por exemplo, o `DRACOLoader` do three.js) para garantir que a geometria seja renderizada corretamente. Você notará uma redução dramática no tamanho do arquivo — frequentemente um fator de dez ou mais.

## Casos de uso comuns

| Cenário | Por que reduzir o tamanho do modelo? | Como este tutorial ajuda |
|----------|-----------------------|--------------------------|
| Configuradores de produtos baseados na web | Carregamento de página mais rápido em conexões lentas | Arquivos `.drc` comprimidos com Draco carregam em segundos |
| Aplicativos móveis de AR/VR | Menor consumo de memória nos dispositivos | Malhas menores mantêm o aplicativo responsivo |
| Cenas renderizadas na nuvem | Reduzir custos de largura de banda | Exportação com um clique do Aspose.3D para Draco |

## Problemas comuns e soluções

| Problema | Razão | Correção |
|-------|--------|-----|
| **`NoClassDefFoundError` for Draco classes** | JARs do Aspose.3D não estão no classpath | Verifique que *todos* os arquivos JAR do Aspose.3D estejam incluídos e que a versão corresponda à documentação. |
| **Output file is empty** | `MyDir` aponta para uma pasta inexistente | Crie o diretório programaticamente (`Files.createDirectories(Paths.get(MyDir))`) antes de gravar o arquivo. |
| **Compressed mesh looks distorted** | Uso de nível de compressão baixo ou tesselação insuficiente | Altere para `DracoCompressionLevel.OPTIMAL` e aumente a tesselação da esfera (por exemplo, `new Sphere(1.0, 64, 64)`). `DracoCompressionLevel.OPTIMAL` seleciona a maior qualidade de compressão para a saída Draco. |

## Perguntas frequentes

**Q: O Aspose.3D é compatível com diferentes formatos de arquivo 3d?**  
A: Sim, o Aspose.3D suporta OBJ, FBX, STL, GLTF e muitos outros, tornando‑o uma escolha versátil para pipelines de **exportação Aspose 3d**.

**Q: Posso usar o Google Draco para compressão em outras linguagens de programação?**  
A: Absolutamente. Draco oferece bibliotecas nativas para C++, Python e JavaScript. Este tutorial foca em Java, mas os conceitos se aplicam a várias linguagens.

**Q: Onde posso encontrar documentação adicional do Aspose.3D?**  
A: Visite a **[documentação Aspose.3D Java](https://reference.aspose.com/3d/java/)** para referências completas da API e mais exemplos.

**Q: Como obtenho uma licença temporária para o Aspose.3D?**  
A: Explore as opções de licenciamento temporário na **[página de licença temporária da Aspose](https://purchase.aspose.com/temporary-license/)**.

**Q: Existe um fórum da comunidade para suporte ao Aspose.3D?**  
A: Sim, participe da discussão no **[Fórum Aspose.3D](https://forum.aspose.com/c/3d/18)**.

## Conclusão

Neste guia demonstramos como **reduzir o tamanho de modelo 3d** criando uma malha de esfera em Java e, em seguida, comprimindo‑a com Google Draco através do Aspose.3D. Seguindo estes passos concisos, você pode reduzir drasticamente os arquivos de malha, melhorar os tempos de carregamento e manter suas aplicações 3d baseadas em Java responsivas e econômicas em largura de banda.

---

**Última atualização:** 2026-11-17  
**Testado com:** Aspose.3D for Java 24.12 (latest)  
**Autor:** Aspose

## Tutoriais relacionados

- [Reduzir tamanho de arquivo 3D – Comprimir cenas com Aspose.3D para Java](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [Gerar uma nuvem de pontos Draco a partir de esferas usando Aspose.3D para Java](/3d/java/point-clouds/generate-point-clouds-spheres-java/)
- [Aprenda a triangular malhas para renderização otimizada em Java usando Aspose.3D](/3d/java/geometry/triangulate-meshes-for-optimized-rendering/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}