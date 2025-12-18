---
date: 2025-12-18
description: Aprenda a extrudar formas em Java usando Aspose.3D, criar cenas 3D e
  exportar arquivos Wavefront OBJ sem esforço.
linktitle: How to Extrude Shape in Java with Aspose.3D Linear Extrusion
second_title: Aspose.3D Java API
title: Como extrudar forma em Java com Aspose.3D Extrusão Linear
url: /pt/java/linear-extrusion/performing-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Realizando Extrusão Linear no Aspose.3D para Java

## Introdução

Welcome to this comprehensive tutorial on **how to extrude shape** in Aspose.3D for Java! If you're looking to enhance your 3D modeling skills using Java, you're in the right place. We'll walk you through creating a 3D scene, performing linear extrusion, and exporting the result as a Wavefront OBJ file—all with clear, step‑by‑step code examples.

## Respostas Rápidas
- **O que é extrusão linear?** Extending a 2D profile along a straight path to create a 3D solid.  
- **Qual biblioteca lida com isso em Java?** Aspose.3D for Java.  
- **Posso exportar para OBJ?** Sim, usando o recurso de exportação Wavefront OBJ.  
- **Preciso de licença para desenvolvimento?** Uma versão de avaliação gratuita funciona para testes; uma licença é necessária para produção.  
- **Qual versão do Java é necessária?** Java 1.6 ou posterior.

## O que é “how to extrude shape”?
Linear extrusion is a fundamental technique in **3d modeling java** that turns a flat profile—like a rectangle—into a volumetric object by pulling it along a defined distance. This method is widely used for creating mechanical parts, architectural elements, and decorative models.

## Por que usar Aspose.3D para extrusão linear?
- **Full control** sobre a geometria (slices, twist, offset).  
- **Seamless integration** com projetos Java—sem dependências nativas.  
- **Built‑in exporters** para formatos populares, incluindo Wavefront OBJ, facilitando a **generate 3d model** de arquivos para pipelines posteriores.

## Pré-requisitos

Before diving into the tutorial, make sure you have the following prerequisites in place:

1. **Java Development Environment** – um JDK (1.6 or newer) and your favorite IDE.  
2. **Aspose.3D Library** – download and install the library from the official site **[here](https://releases.aspose.com/3d/java/)**.

## Importar Pacotes

Once you've set up your development environment and installed the Aspose.3D library, import the necessary package:

```java
import com.aspose.threed.*;
```

### Passo 1: Definir Diretório do Documento

Define the folder where the generated files will be saved:

```java
String MyDir = "Your Document Directory";
```

> This ensures that the **generate 3d model** operation writes the OBJ file to a known location.

### Passo 2: Inicializar Forma Base

Create a rectangle that will serve as the extrusion profile:

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

Você pode ajustar o raio de arredondamento para obter cantos arredondados ou defini-lo como `0` para um retângulo perfeito.

### Passo 3: Executar Extrusão Linear

Now we extrude the rectangle along the Z‑axis, add slices, enable centering, and apply a twist with an offset:

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

- **Extrusion length** – `10` unidades.  
- **Slices** – `100` para geometria suave.  
- **Twist** – `360°` cria uma rotação completa.  
- **Twist offset** – move a origem da torção para `(10, 0, 0)`.

### Passo 4: Criar Cena 3D

Create a scene container and add the extrusion as a child node. This step **creates 3d scene** that can hold multiple objects:

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

### Passo 5: Salvar Cena 3D

Export the scene to a Wavefront OBJ file. This demonstrates **wavefront obj export** and **save 3d obj** capabilities:

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

After running the code, you’ll find `LinearExtrusion.obj` in the directory you specified, ready to be opened in any 3D viewer or further processed.

## Problemas Comuns e Soluções

| Problema | Motivo | Solução |
|----------|--------|---------|
| OBJ file is empty | O caminho do diretório de saída está incorreto ou não gravável | Verifique se `MyDir` aponta para uma pasta existente com permissões de gravação. |
| Twist not applied | `setCenter(true)` omitido | Certifique-se de que o centramento está habilitado ou ajuste os valores de `setTwistOffset`. |
| Compilation error on `LinearExtrusion` | Usando uma versão mais antiga do Aspose.3D | Atualize para a versão mais recente do Aspose.3D. |

## Perguntas Frequentes

**Q: O Aspose.3D é compatível com todas as versões do Java?**  
A: Aspose.3D funciona com Java 1.6 e posteriores.

**Q: Posso usar o Aspose.3D em projetos comerciais?**  
A: Sim, o uso comercial é permitido com uma licença válida. Você pode obter uma **[here](https://purchase.aspose.com/buy)**.

**Q: Onde posso obter suporte se encontrar problemas?**  
A: Visite o **[Aspose.3D forum](https://forum.aspose.com/c/3d/18)** para ajuda da comunidade ou adquira uma **[temporary license](https://purchase.aspose.com/temporary-license/)** para suporte premium.

**Q: Quais outras funcionalidades de modelagem 3D o Aspose.3D oferece?**  
A: A biblioteca inclui manipulação de malhas, operações booleanas, mapeamento de texturas e muito mais. Veja a lista completa **[here](https://reference.aspose.com/3d/java/)**.

**Q: Existe uma versão de avaliação gratuita?**  
A: Sim, você pode baixar uma versão de avaliação **[here](https://releases.aspose.com/)**.

## Conclusão

You’ve now learned **how to extrude shape** using Aspose.3D for Java, created a 3D scene, and exported the result as a Wavefront OBJ file. This technique opens the door to a wide range of **3d modeling java** projects—from simple parts to complex assemblies. Explore additional features like Boolean operations or texture mapping to further enrich your models.

---

**Última atualização:** 2025-12-18  
**Testado com:** Aspose.3D 24.11 for Java  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

## PALAVRAS‑CHAVE‑ALVO:

**Palavra‑chave Primária (MAIOR PRIORIDADE):**  
how to extrude shape

**Palavras‑chave Secundárias (SUPORTE):**  
create 3d scene, 3d modeling java, generate 3d model, wavefront obj export, save 3d obj