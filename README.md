# Analyse_Laptop_feature
Crawl Data &amp; Analyse 
## 1. Thư mục `Crawler` chứa sourcecode
## 2. File `data.csv` là dữ liệu chưa qua xử lý (raw data)
**Nguồn dữ liệu về laptop thu thập được từ 3 trang web:**
    + https://fptshop.com.vn/
    + https://www.dienmayxanh.com/
    + https://phongvu.vn/
## 3. File `laptop_clean.csv`gồm:
**17 trường dữ liệu:**
    + **id**: ID laptop
    + **brand**: Thương hiệu của laptop
    + **cpu**: Bộ xử lý trung tâm. 
    >CPU đóng vai trò như não bộ của một chiếc Laptop, tại đó mọi thông tin, thao tác, dữ liệu sẽ được tính toán kỹ lưỡng và đưa ra lệnh điều khiển mọi hoạt động của Laptop.
    + **cpu_GHz**: Tốc độ xử lý CPU hay tần số tính toán và làm việc của nó được đo bằng đơn vị GHz hoặc MHz
    > Nếu cùng một dòng chip ví dụ như Core i3 thì xung nhịp cao hơn đồng nghĩa với tốc độ xử lý nhanh hơn, khả năng làm việc tốt hơn. Tuy nhiên, nếu giữa 2 dòng chip khác nhau như Core i3 hai nhân xung nhịp 2.2GHz và Intel Pentium Dual core 2.3GHz thì không thể so sánh ngay được bởi vì tốc độ xử lý của Laptop còn phụ thuộc rất nhiều yếu tố khác
    + **cpu_brand**: Hãng sản xuất CPU
    + **ram**: Bộ nhớ tạm (đơn vị GB)
    > RAM là bộ nhớ tạm của máy giúp lưu trữ thông tin hiện hành để CPU có thể truy xuất và xử lý.
    + **scrsize**: Kích thước màn hình laptop (đơn vị inch)
    + **gpu**: đơn vị xử lý đồ họa chuyên dụng, nhiệm vụ chính là tăng tốc, xử lý đồ họa cho bộ xử lý của CPU
    > Ngoài tác vụ đồ họa, GPU còn xử lý thông tin đa luồng, song song và bộ nhớ ở tốc độ cao.
    + **gpu_brand**: Hãng sản xuất GPU
    + **memory**: Dung lượng lưu trữ (đơn vị GB)
    + **drive_type**: Loại ổ đĩa
    + **opersystem**: Hệ điều hành
    + **since**: Năm sản xuất
    + **shop**: Cửa hàng phân phối
    + **price**: Giá sản phẩm
    + **url**: Đường dẫn đến sản phẩm