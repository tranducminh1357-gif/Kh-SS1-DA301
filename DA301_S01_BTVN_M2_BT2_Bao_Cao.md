# BÁO CÁO PHÂN TÍCH B2A: HIỆU SUẤT NGÀNH HÀNG LAPTOP & PHỤ KIỆN TẠI MWG

**Mã bài tập:** `DA301_S01_BTVN_M2_BT2` | **Công cụ:** Google Antigravity & Python Sandbox (`mwg_btvn_m2_bt2.py`)

> **Ghi chú minh bạch dữ liệu:** Thư mục `datasets/` hiện chưa có tệp `mwg_manual_reporting_workflow.csv` đủ 40 dòng; do đó các phép tính theo `category` dưới đây được thực thi trong Python Sandbox trên **8 bản ghi mẫu (`ST_001`–`ST_008`)** kết hợp **Bảng Control Totals 40 cửa hàng** của đề bài.

---

## 1. Phương pháp Phân rã B2A (4 Bước) & Bảng Số liệu Kiểm chứng Sandbox

### Khung chuyển đổi B2A (Business-to-Analytics)
1. **Bước 1 — Business Question:** *Tại sao ngành hàng Laptop và Phụ kiện tại một số chi nhánh có tỷ lệ hoàn thành doanh thu thấp hơn đáng kể so với mục tiêu tháng?*
2. **Bước 2 — Metrics & Dimensions:**
   - **Metrics:** `target_revenue_mil`, `actual_revenue_mil`, `Gap_mil = actual - target`, `Completion_Pct = (actual / target) × 100`, `units_sold`, `stockout_rate_pct`.
   - **Dimensions:** `category` (trọng tâm `Laptop`, `Phu kien`), `region`, `store_id`.
3. **Bước 3 — Analytical Method:** Tổng hợp (Groupby Aggregation) theo `category`, đối chiếu chênh lệch kế hoạch và kiểm tra mối liên hệ giữa `stockout_rate_pct` với `Gap_mil` trong Python Sandbox (`pandas`), đối soát Control Total.
4. **Bước 4 — Atomic Analytical Tasks (Giao cho AI Agent):**
   - *Task A1:* Kiểm định schema 8 cột, xác nhận không có giá trị Null/lỗi định dạng.
   - *Task A2:* Tính `Gap_mil` và `Completion_Pct` theo từng `category`.
   - *Task A3:* Xếp hạng các ngành hàng thiếu hụt lớn nhất và đối chiếu Control Total (`5.260,0 - 5.090,0 = -170,0` triệu VNĐ trên mẫu 8 CH; `34.300,0 - 33.252,0 = -1.048,0` triệu VNĐ toàn chuỗi 40 CH).

### Bảng so sánh hiệu suất ngành hàng (Mẫu 8 chi nhánh — Python Sandbox)
| Ngành hàng (`category`) | Số CH | Target (mil) | Actual (mil) | Gap (mil) | Hoàn thành (%) | Sản lượng (`units_sold`) | Đứt hàng TB (%) |
| :--- | :---: | ---: | ---: | ---: | :---: | :---: | :---: |
| **Laptop** | 2 | 1.245,0 | 1.136,0 | **-109,0** | **91,24%** | 227 | 6,70% |
| **Phu kien** | 2 | 1.315,0 | 1.244,0 | **-71,0** | **94,60%** | 249 | 7,90% |
| **Dien gia dung** | 2 | 1.385,0 | 1.356,0 | -29,0 | 97,91% | 271 | 9,10% |
| **Dong ho** | 1 | 640,0 | 646,0 | +6,0 | 100,94% | 129 | 7,30% |
| **Dien thoai** | 1 | 675,0 | 708,0 | +33,0 | 104,89% | 141 | 8,50% |

---

## 2. Nhận định Chuyên sâu (Định lượng)

1. **Laptop và Phụ kiện là hai nhóm kéo giảm doanh thu mạnh nhất:** Trong mẫu kiểm chứng, `Laptop` đạt tỷ lệ hoàn thành thấp nhất (**`91,24%`**, hụt **`-109,0` triệu VNĐ**), theo sau là `Phu kien` (**`94,60%`**, hụt **`-71,0` triệu VNĐ**). Riêng 2 ngành hàng này tại Miền Trung (`ST_001`, `ST_006`) và Miền Nam (`ST_002`, `ST_007`) cộng lại đã hụt `-180,0` triệu VNĐ. Trên toàn chuỗi 40 cửa hàng, Miền Trung (`94,85%`, `-349,0` triệu) và Miền Nam (`95,99%`, `-283,0` triệu) cũng là 2 vùng hụt nặng nhất.
2. **Đứt hàng làm trầm trọng hóa thiếu hụt ở nhóm có biên độ dao động cao:** Khi tỷ lệ đứt hàng tăng từ `3,7%` (`ST_001`) lên `9,7%` (`ST_006` - Laptop) và `10,9%` (`ST_007` - Phụ kiện), mức hụt doanh thu tăng vọt lên `-50,0` triệu và `-31,0` triệu. Tuy nhiên, đứt hàng không phải nguyên nhân duy nhất: `ST_001` có đứt hàng thấp (`3,7%`) nhưng vẫn hụt `-59,0` triệu, cho thấy còn yếu tố sức mua hoặc đặt chỉ tiêu (Target) chưa sát thực tế vùng.

---

## 3. Khuyến nghị Hành động cho Ban Quản lý MWG

1. **Thiết lập ngưỡng cảnh báo kép (Stockout > 5% & Completion < 95%) cho Laptop và Phụ kiện:** Triển khai script `mwg_btvn_m2_bt2.py` tự động gắn cờ các chi nhánh Miền Trung (`ST_006`) và Miền Nam (`ST_007`) để ưu tiên bổ sung tồn kho ngay trong ngày.
2. **Rà soát lại cơ cấu chỉ tiêu (Target) và kích cầu tại Miền Trung:** Với các chi nhánh đứt hàng thấp nhưng vẫn hụt chỉ tiêu sâu như `ST_001` (`3,7%` đứt hàng, hụt `-59,0` triệu), cần rà soát lại mức phân bổ Target tháng và áp dụng combo bán kèm Laptop + Phụ kiện để nâng giá trị đơn hàng.

---

### Minh chứng Prompt điều phối AI Agent
```text
Áp dụng khung B2A 4 bước trên dữ liệu MWG (mwg_btvn_m2_bt2.py). Chạy Python Sandbox tính tổng target_revenue_mil, actual_revenue_mil, Gap_mil, Completion_Pct, units_sold và trung bình stockout_rate_pct theo từng category; đối soát Control Total và không tự suy diễn số liệu.
```

