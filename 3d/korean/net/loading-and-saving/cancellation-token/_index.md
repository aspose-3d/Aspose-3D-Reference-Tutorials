---
title: CancellationToken 사용
linktitle: CancellationToken 사용
second_title: Aspose.3D .NET API
description: .NET용 Aspose.3D를 사용하여 원활한 3D 모델링 세계를 탐색해 보세요. CancellationToken을 사용하여 3D 문서를 효율적으로 로드하고 저장하는 방법을 알아보세요.
weight: 10
url: /ko/net/loading-and-saving/cancellation-token/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# CancellationToken 사용

## 소개

.NET용 Aspose.3D를 활용하여 3D 모델링 및 렌더링 프로젝트를 향상시키는 방법에 대한 포괄적인 가이드에 오신 것을 환영합니다. Aspose.3D는 .NET 개발자가 3D 파일을 원활하게 사용할 수 있도록 지원하는 강력한 라이브러리입니다. 이 튜토리얼에서는 로딩 및 저장 측면을 자세히 살펴보겠습니다. 특히 비동기 작업의 효율적인 관리를 위한 CancellationToken 사용에 중점을 둡니다.

## 전제 조건

이 여정을 시작하기 전에 다음과 같은 전제 조건이 갖추어져 있는지 확인하세요.

-  .NET용 Aspose.3D: 다음에서 라이브러리를 다운로드하고 설치하세요.[여기](https://releases.aspose.com/3d/net/).
- .NET 환경: 호환 가능한 .NET 개발 환경이 설정되어 있는지 확인하세요.
- C#에 대한 기본 이해: C# 프로그래밍 언어에 익숙한 것이 좋습니다.

## 네임스페이스 가져오기

시작하려면 프로젝트에 필요한 네임스페이스를 포함했는지 확인하세요. 이러한 네임스페이스는 3D 파일 조작에 필요한 기능에 대한 액세스를 제공합니다.

```csharp
using Aspose.ThreeD;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
```

## 로드 및 저장 - CancellationToken 사용

### 1단계: CancellationTokenSource 생성

```csharp
// ExStart:CancellationTokenSource

CancellationTokenSource cts = new CancellationTokenSource();
```

여기서는 비동기 작업에서 취소를 관리하는 데 중요한 구성 요소인 CancellationTokenSource를 인스턴스화합니다.

### 2단계: 3D 장면 초기화

```csharp
Scene scene = new Scene();
```

Scene 클래스의 인스턴스를 만듭니다. 이는 3D 모델링 활동을 위한 캔버스가 됩니다.

### 3단계: CancellationToken 시간 초과 설정

```csharp
cts.CancelAfter(1000);
```

 다음을 사용하여 취소 시간 초과를 설정합니다.`CancelAfter` 방법. 이 예에서는 시간 제한이 1000밀리초(1초)로 설정되어 있습니다.

### 4단계: 3D 문서 열기

```csharp
try
{
    scene.Open("Your Output Directory" + "document.fbx", cts.Token);
    Console.WriteLine("Import is done within 1000ms");
}
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
```

 지정된 시간 내에 3D 문서를 열려고 시도합니다. 그만큼`cts.Token` 매개변수는 설정된 제한 시간을 초과하는 경우 작업이 취소될 수 있도록 보장합니다.

### 5단계: 가져오기 예외 처리

ImportException이 발생한 경우 OperationCanceledException으로 인해 발생했는지 확인하여 정상적으로 처리합니다.

```csharp
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
// ExEnd:CancellationTokenSource
```

## 결론

축하해요! CancellationToken과 함께 .NET용 Aspose.3D를 사용하여 3D 문서 로드를 관리하는 프로세스를 성공적으로 탐색했습니다. 이 기술은 효율적이고 시기적절한 가져오기 작업을 보장하여 3D 애플리케이션의 전반적인 성능을 향상시킵니다.

## FAQ

### Q1: Aspose.3D는 모든 3D 파일 형식과 호환됩니까?

 A1: Aspose.3D는 FBX, STL, OBJ 등을 포함한 광범위한 3D 파일 형식을 지원합니다. 다음을 참조하세요.[선적 서류 비치](https://reference.aspose.com/3d/net/) 전체 목록을 보려면.

### Q2: Aspose.3D의 임시 라이선스를 어떻게 얻을 수 있나요?

 A2: 방문하여 임시 면허를 취득하세요.[이 링크](https://purchase.aspose.com/temporary-license/).

### Q3: Aspose.3D에 대한 지원은 어디서 찾을 수 있나요?

 A3: 커뮤니티 토론에 참여하세요.[Aspose.3D 포럼](https://forum.aspose.com/c/3d/18).

### Q4: 구매하기 전에 Aspose.3D를 무료로 사용해 볼 수 있나요?

 A4: 예, 무료 평가판을 통해 기능을 살펴보세요.[여기](https://releases.aspose.com/).

### Q5: .NET용 Aspose.3D의 최신 버전은 무엇입니까?

 A5: 최신 정보를 확인하여 최신 상태를 유지하세요.[다운로드 페이지](https://releases.aspose.com/3d/net/) 최신 릴리스의 경우.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
