---
title: Sử dụng CancellingToken
linktitle: Sử dụng CancellingToken
second_title: API Aspose.3D .NET
description: Khám phá thế giới liền mạch của mô hình 3D với Aspose.3D cho .NET. Tìm hiểu cách tải và lưu tài liệu 3D một cách hiệu quả bằng cách sử dụng CancellationToken.
type: docs
weight: 10
url: /vi/net/loading-and-saving/cancellation-token/
---
## Giới thiệu

Chào mừng bạn đến với hướng dẫn toàn diện của chúng tôi về cách sử dụng Aspose.3D cho .NET để nâng cao các dự án kết xuất và tạo mô hình 3D của bạn. Aspose.3D là một thư viện mạnh mẽ cho phép các nhà phát triển .NET làm việc liền mạch với các tệp 3D. Trong hướng dẫn này, chúng ta sẽ đi sâu vào các khía cạnh tải và lưu, đặc biệt tập trung vào việc sử dụng CancellationToken để quản lý hiệu quả các tác vụ không đồng bộ.

## Điều kiện tiên quyết

Trước khi chúng ta bắt đầu cuộc hành trình này, hãy đảm bảo bạn có sẵn các điều kiện tiên quyết sau:

-  Aspose.3D for .NET: Tải xuống và cài đặt thư viện từ[đây](https://releases.aspose.com/3d/net/).
- Môi trường .NET: Đảm bảo bạn đã thiết lập môi trường phát triển .NET tương thích.
- Hiểu biết cơ bản về C#: Nên làm quen với ngôn ngữ lập trình C#.

## Nhập không gian tên

Để bắt đầu, hãy đảm bảo bạn đưa các không gian tên cần thiết vào dự án của mình. Các không gian tên này sẽ cung cấp quyền truy cập vào các chức năng cần thiết để thao tác với tệp 3D.

```csharp
using Aspose.ThreeD;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
```

## Đang tải và lưu - Sử dụng CancellationToken

### Bước 1: Tạo CancellationTokenSource

```csharp
// ExStart:CancellationTokenSource

CancellationTokenSource cts = new CancellationTokenSource();
```

Ở đây, chúng tôi khởi tạo CancellationTokenSource, một thành phần quan trọng để quản lý việc hủy trong các hoạt động không đồng bộ.

### Bước 2: Khởi tạo cảnh 3D

```csharp
Scene scene = new Scene();
```

Tạo một thể hiện của lớp Cảnh. Đây sẽ là canvas cho các hoạt động lập mô hình 3D của bạn.

### Bước 3: Đặt thời gian chờ của CancellationToken

```csharp
cts.CancelAfter(1000);
```

 Đặt thời gian chờ hủy bằng cách sử dụng`CancelAfter` phương pháp. Trong ví dụ này, thời gian chờ được đặt thành 1000 mili giây (1 giây).

### Bước 4: Mở tài liệu 3D

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

 Cố gắng mở tài liệu 3D trong khung thời gian đã chỉ định. Các`cts.Token` tham số đảm bảo rằng thao tác có thể bị hủy nếu vượt quá thời gian chờ đã đặt.

### Bước 5: Xử lý ngoại lệ nhập

Trong trường hợp xảy ra ngoại lệ ImportException, hãy xử lý nó một cách khéo léo bằng cách kiểm tra xem liệu nó có phải do OperationCanceledException gây ra hay không.

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

## Phần kết luận

Chúc mừng! Bạn đã điều hướng thành công trong quá trình sử dụng Aspose.3D cho .NET với CancellationToken để quản lý việc tải tài liệu 3D. Kỹ thuật này đảm bảo hoạt động nhập hiệu quả và kịp thời, nâng cao hiệu suất tổng thể của các ứng dụng 3D của bạn.

## Câu hỏi thường gặp

### Câu hỏi 1: Aspose.3D có tương thích với tất cả các định dạng tệp 3D không?

 Câu trả lời 1: Aspose.3D hỗ trợ nhiều định dạng tệp 3D, bao gồm FBX, STL, OBJ, v.v. Tham khảo đến[tài liệu](https://reference.aspose.com/3d/net/) để có danh sách đầy đủ.

### Câu hỏi 2: Làm cách nào tôi có thể nhận được giấy phép tạm thời cho Aspose.3D?

 A2: Lấy giấy phép tạm thời bằng cách truy cập[liên kết này](https://purchase.aspose.com/temporary-license/).

### Câu hỏi 3: Tôi có thể tìm hỗ trợ cho Aspose.3D ở đâu?

 A3: Tham gia thảo luận cộng đồng tại[Diễn đàn Aspose.3D](https://forum.aspose.com/c/3d/18).

### Câu hỏi 4: Tôi có thể dùng thử Aspose.3D miễn phí trước khi mua không?

 Câu trả lời 4: Có, hãy khám phá các tính năng bằng bản dùng thử miễn phí[đây](https://releases.aspose.com/).

### Câu hỏi 5: Phiên bản mới nhất của Aspose.3D dành cho .NET là gì?

 Câu trả lời 5: Luôn cập nhật bằng cách kiểm tra[trang tải xuống](https://releases.aspose.com/3d/net/) cho phiên bản mới nhất.