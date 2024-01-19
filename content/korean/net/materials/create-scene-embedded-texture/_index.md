---
title: 임베디드 텍스처로 장면 만들기
linktitle: 임베디드 텍스처로 장면 만들기
second_title: Aspose.3D .NET API
description: .NET용 Aspose.3D를 사용하여 내장된 텍스처로 매혹적인 3D 장면을 만드세요. 놀라운 결과를 얻으려면 단계별 가이드를 따르십시오.
type: docs
weight: 10
url: /ko/net/materials/create-scene-embedded-texture/
---
## 소개
.NET용 Aspose.3D를 사용하여 흥미진진한 3D 그래픽 세계에 오신 것을 환영합니다! 이 포괄적인 튜토리얼에서는 .NET 개발자를 위한 강력하고 다재다능한 라이브러리인 Aspose.3D를 사용하여 텍스처가 포함된 멋진 3D 장면을 만드는 과정을 안내합니다.
## 전제 조건
튜토리얼을 시작하기 전에 다음 전제 조건이 충족되었는지 확인하세요.
- C# 및 .NET 프로그래밍에 대한 기본적인 이해.
- 컴퓨터에 Visual Studio가 설치되어 있습니다.
-  다운로드할 수 있는 .NET 라이브러리용 Aspose.3D[여기](https://releases.aspose.com/3d/net/).
- 3D 그래픽 및 장면 생성 개념에 익숙합니다.
## 네임스페이스 가져오기
필요한 네임스페이스를 프로젝트로 가져오는 것부터 시작하세요. 이러한 네임스페이스는 3D 그래픽 조작에 필요한 도구와 기능을 제공합니다.
```csharp
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
```
## 1단계: 장면 만들기
.NET용 Aspose.3D를 사용하여 새로운 3D 장면을 만드는 것부터 시작하세요. 이는 귀하의 3D 걸작을 위한 캔버스 역할을 할 것입니다.
```csharp
// 텍스처가 포함된 FBX 파일 만들기
Scene scene = new Scene();
```
## 2단계: 내장된 텍스처 만들기
이제 텍스처를 삽입하여 장면에 시각적 효과를 추가해 보겠습니다. 사용자 정의 컨텐츠로 텍스처를 생성하고 파일 이름을 지정하겠습니다.
```csharp
// 포함된 텍스처 만들기
Texture tex = new Texture()
{
    Content = CreateTextureContent(),
    // 내장된 텍스처를 사용하는 경우 파일 이름이 필요합니다.
    FileName = "test.png"
};
tex.SetProperty("TexProp", "value");
```
## 3단계: 재료 만들기
다음으로, 이전에 생성된 텍스처와 사용자 정의 속성을 통합하여 3D 객체용 재질을 생성합니다.
```csharp
// 사용자 정의 속성을 사용하여 재료 만들기
LambertMaterial mat = new LambertMaterial("my-mat");
mat.SetTexture(Material.MapDiffuse, tex);
mat.SetProperty("MyProp", 1.0);
```
## 4단계: 3D 개체 만들기
이제 3D 개체를 추가하여 장면에 생기를 불어넣어 보겠습니다. 이 예에서는 토러스를 사용하고 방금 만든 재질을 적용하겠습니다.
```csharp
// 이전에 만든 재질을 적용하여 토러스를 만듭니다.
scene.RootNode.CreateChildNode(new Torus()).Material = mat;
```
## 5단계: 장면 저장
마지막으로 걸작을 파일에 저장하세요. 이 예에서는 FBX 형식으로 저장하겠습니다.
```csharp
// 장면을 파일로 저장
scene.Save(RunExamples.GetOutputFilePath(@"test.fbx"), FileFormat.FBX7500ASCII);
```
축하해요! .NET용 Aspose.3D를 사용하여 텍스처가 포함된 3D 장면을 성공적으로 만들었습니다.
## CreateTextureContent 소스 코드
```csharp
        private static byte[] CreateTextureContent()
        {
            using (var bitmap = new Bitmap(256, 256))
            {
                using (var g = Graphics.FromImage(bitmap))
                {
                    g.Clear(Color.White);
                    LinearGradientBrush brush = new LinearGradientBrush(new Rectangle(0, 0, 128, 128), Color.Moccasin,
                        Color.ForestGreen, 45);
                    using (var font = new Font(FontFamily.GenericSerif, 40))
                    {
                        g.DrawString("Aspose.3D", font, brush, Point.Empty);
                    }
                }
                using (var ms = new MemoryStream())
                {
                    bitmap.Save(ms, ImageFormat.Png);
                    return ms.ToArray();
                }
            }
        }
```
## 결론
이 튜토리얼에서는 .NET용 Aspose.3D를 사용하여 내장된 텍스처로 시각적으로 놀라운 3D 장면을 만드는 기본 사항을 살펴보았습니다. 이러한 지식으로 무장하면 창의력을 발휘하고 매력적인 3D 애플리케이션을 구축할 수 있습니다.

## 자주 묻는 질문

### Q: 다른 프로그래밍 언어와 함께 .NET용 Aspose.3D를 사용할 수 있습니까?
A: Aspose.3D는 기본적으로 .NET용으로 설계되었지만 다른 언어에도 사용할 수 있는 유사한 라이브러리가 있습니다.
### Q: 3D 장면에 애니메이션을 어떻게 적용할 수 있나요?
A: Aspose.3D는 애니메이션 기능을 제공합니다. 자세한 지침은 설명서를 참조하세요.
### Q: .NET용 Aspose.3D에 사용할 수 있는 평가판이 있습니까?
 A: 예, 평가판을 다운로드할 수 있습니다.[여기](https://releases.aspose.com/).
### Q: 추가 지원과 리소스는 어디서 찾을 수 있나요?
 답: 다음을 방문하세요.[Aspose.3D 포럼](https://forum.aspose.com/c/3d/18) 커뮤니티 지원 및 토론을 위해.
### Q: Aspose.3D를 상업용 프로젝트에 사용할 수 있나요?
 A: 예, 라이센스를 구매할 수 있습니다.[여기](https://purchase.aspose.com/buy).