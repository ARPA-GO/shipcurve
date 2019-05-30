(defun LoadExcel ()
;�����Լ� LoadExcel ����
;Excel�� �����ϱ� ���� �����Լ�
  
  (if (and (setq excelPath (vl-registry-read
			     "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\App Paths\\Excel.exe"
			     "Path"))
	   (setq excelPath (strcat excelPath "Excel.exe")))
   ;������ ����ȭ�� ��θ� �˾Ƴ�
    
    (progn
      (if (not msxl-acos)
	(vlax-import-type-library
	  :tlb-filename excelPath
	  :methods-prefix "msxl-"
	  :properties-prefix "msxl-"
	  :constants-prefix "msxl-"))
      (setq ExcelApp (vlax-get-or-create-object "Excel.Application")))
    ;����ȭ�� ��θ� �˾Ƴ������� ������ �����Ͽ� ExcelApp�� ����
    
  ExcelApp
  ;ExcelApp����
    
  );LoadExcel ����