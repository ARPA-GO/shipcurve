(defun LoadExcel ()
;서브함수 LoadExcel 선언
;Excel과 연결하기 위한 서브함수
  
  (if (and (setq excelPath (vl-registry-read
			     "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\App Paths\\Excel.exe"
			     "Path"))
	   (setq excelPath (strcat excelPath "Excel.exe")))
   ;엑셀의 실행화일 경로를 알아냄
    
    (progn
      (if (not msxl-acos)
	(vlax-import-type-library
	  :tlb-filename excelPath
	  :methods-prefix "msxl-"
	  :properties-prefix "msxl-"
	  :constants-prefix "msxl-"))
      (setq ExcelApp (vlax-get-or-create-object "Excel.Application")))
    ;실행화일 경로를 알아내었으니 엑셀과 연결하여 ExcelApp에 저장
    
  ExcelApp
  ;ExcelApp실행
    
  );LoadExcel 종료