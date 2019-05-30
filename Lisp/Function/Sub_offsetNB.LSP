(defun offsetNB()
;서브함수 offsetNB 선언
;modeNB일때 엑셀로 나타낼 offset표의 형식을 지정하기위한 서브함수
  
  (setq ExcelApp (LoadExcel))
  ;서브함수 LoadExcel을 로딩한다
  
  (vlax-put Excelapp "visible" :vlax-false)
  ;vlax-true일 경우, 엑셀을 실행시킨다. 이는 사용자를 불편하게 할 수 있으므로 생략하였다.
  
  (setq Workbooks (vlax-get-property ExcelApp 'Workbooks))
  ;열려있는 엑셀파일을 Workbooks변수에 저장
  
  (setq CurrentWBook (vlax-invoke-method Workbooks 'Add))
  ;좌표를 추출해 엑셀에 데이터를 기록하는것이므로 새로운 엑셀파일을 생성
  
  (setq Sheets (vlax-get-property ExcelApp 'Sheets))
  ;현재 시트들을 Shetts변수에 저장
  
  (setq AcSheet (vlax-get-property ExcelApp 'ActiveSheet))
  ;현재 활성화된 시트를 AcSheet변수에 저장
  
  (setq Cells (vlax-get-property AcSheet 'Cells))
  ;활성화된 시트의 셀들을 Cells변수에 저장
  

  ;offset form---
  ;offset표의 값은 소숫점 4째자리에서 반올림하므로 숫자의 형식을 지정해줌
  
  (setq Ran (vlax-get-property Excelapp 'Range "B2:Z100"))
  ;B2이후 셀들의 property를 Ran에 저장
  
  (vlax-put-property Ran 'Numberformat "0.000")
  ;Ran의 property를 얻어왔으으므로 숫자형식을 지정해주는 Numberformat을 이용해 형식 지정

  ;WL Number-----
  ;WaterLine Number를 표시하는 부분의 형식 지정
  
  (setq colY 1 rowX 3)
  ;1행 3열(C1)을 뜻함
  
  (setq val "BOTTOM")
  ;BOTTOM 이라는 값을 val변수에 저장
  
  (vlax-put-property Cells 'Item colY rowX val)
  ;C1에 val값을 넣어라

  (setq colY 1 rowX 4)
  ;1행 4열(D1)을 뜻함
  
  (setq val "0.5 WL")
  ;0.5 W.L 이라는 값을 val변수에 저장
  
  (vlax-put-property Cells 'Item colY rowX val)
  ;D1에 val값을 넣어라
  
  (setq colY 1 rowX 5)
  ;E1
  
  (setq wlnumlist(mapcar '(lambda(x)(strcat (itoa x) " W.L"))wlnumlist))
  ;서브함수 setWL에서 생성한 wlnumlist 리스트 요소들에 "W.L"을 추가
  
  (mapcar
    '(lambda (val)
       (vlax-put-property Cells 'Item colY rowX val)
       (setq rowX(1+ rowX)))wlnumlist)
  ;가로로 연속적으로 리스트값(wlnumlist)을 넣음


  ;셀 특성 변경
  (setq wx 3)
  ;C1부터 시작하기위해 변수 초기값을 3으로 선언
  
  (repeat wllistn
  ;waterline 개수만큼 반복
    
    (setq colY 1 rowX wx)
    ;C1부터 시작함
    
    (setq cel(vlax-variant-value(vlax-get-property Cells 'Item colY rowX)))
    ;셀을 다시 객체로 잡음
    
    (setq int(vlax-get-property cel 'Interior))
    ;배경색을 바꾸기 위해 Interior속성을 얻어와 int변수에 저장
    
    (setq Font(vlax-get-property cel 'Font))
    ;글꼴의 두께를 바꾸기 위해 Font 속성을 얻어와 Font변수에 저장
    
    (setq borders(vlax-get-property cel 'Borders))
    ;테두리 형식 지정을 위해 Borders속성을 얻어와 borders변수에 저장

    (setq bordersB(vlax-get-property borders 'Item 9))
    ;테두리중 아래부분의 속성을 얻어와 bordersB변수에 저장
    
    (setq bordersR(vlax-get-property borders 'Item 10))
    ;테두리중 오른쪽부분의 속성을 얻어와 bordersR변수에 저장
    
    (vlax-put-property cel 'HorizontalAlignment -4108)
    ;셀에 입력된 값의 수평정렬을 가운데정렬함
    
    (vlax-put-property int 'Color 14599344)
    ;셀의 배경색 변경
    
    (vlax-put-property Font 'Bold "true")
    ;셀의 글꼴 두께 굵게 변경
    
    (vlax-put-property bordersB 'Weight 4)
    ;아래쪽 테두리 두께 굵게 설정
    
    (vlax-put-property bordersB 'LineStyle 1)
    ;아래쪽 테두리 스타일 연속적 실선 설정
    
    (vlax-put-property bordersR 'Weight 2)
    ;오른쪽 테두리 두께 얇게 설정
    
    (vlax-put-property bordersR 'LineStyle 1)
    ;오른쪽 테두리 스타일 연속적 실선 설정
    
    (setq wx(+ wx 1))
    );repeat문 종료
  

  ;ST Number-----
  ;Station Number를 표시하는 부분의 형식 지정
  ;WL Number와 상당부분 동일
  
  (setq colY 1 rowX 1)
  (setq backlist (list "NO. Station" "T2" "T1" "A.P." "S.T 0.5" "S.T 1" "S.T 1.5"))
  (mapcar
    '(lambda(val)
       (vlax-put-property Cells 'Item colY rowX val)
       (setq colY (1+ colY)))backlist)
  
  
  (setq colY 8 rowX 1)
  (setq stnumlist(list 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18))
  (setq stnumlist(mapcar '(lambda(x)(strcat "S.T " (itoa x) ))stnumlist))
  (mapcar
    '(lambda (val)
       (vlax-put-property Cells 'Item colY rowX val)
       (setq colY (1+ colY)))stnumlist)

  (setq colY 25 rowX 1)
  (setq frontlist (list "S.T 18.5" "S.T 19" "S.T 19.5" "F.P." "F1" "F2"))
  (mapcar
    '(lambda(val)
       (vlax-put-property Cells 'Item colY rowX val)
       (setq colY (1+ colY)))frontlist)

  (setq Ran(vlax-get-property Excelapp 'Range "A1:B1"))
  (setq Font(vlax-get-property Ran 'Font))
  (setq borders(vlax-get-property Ran 'Borders))
  (setq bordersB(vlax-get-property borders 'Item 9))
  (setq bordersR(vlax-get-property borders 'Item 10))
  (vlax-put-property Ran 'MergeCells "true")
  ;Ran으로 지정한 범위의 셀들을 병합함
  (vlax-put-property Ran 'HorizontalAlignment -4108)
  (vlax-put-property Font 'Bold "true")
  (vlax-put-property bordersB 'Weight 4)
  (vlax-put-property bordersR 'Weight 4)
  (vlax-put-property bordersB 'LineStyle 1)
  (vlax-put-property bordersR 'LineStyle 1)
  
  (setq Ran(vlax-get-property Excelapp 'Range "A2:A30"))
  (setq int(vlax-get-property Ran 'Interior))
  (setq Font(vlax-get-property Ran 'Font))
  (vlax-put-property int 'Color 14599344) 
  (vlax-put-property Font 'Bold "true")
  (vlax-put-property Ran 'HorizontalAlignment -4108)

  (setq Ran(vlax-get-property Excelapp 'Range "A2:B30"))
  (setq borders(vlax-get-property Ran 'Borders))
  (setq bordersR(vlax-get-property borders 'Item 10))
  (setq bordersV(vlax-get-property borders 'Item 11))
  ;한개의 셀이 아닌 범위로 지정된 셀이므로 내부 테두리중 수직 테두리의 속성을 얻어와 bordersV변수에 저장
  (setq bordersH(vlax-get-property borders 'Item 12))
  ;수평 테두리의 속성을 얻어와 vordersH변수에 저장
  (vlax-put-property bordersR 'Weight 4)
  (vlax-put-property bordersV 'Weight 2)
  (vlax-put-property bordersH 'Weight 2)
  (vlax-put-property bordersR 'LineStyle 1)
  (vlax-put-property bordersV 'LineStyle 1)
  (vlax-put-property bordersH 'LineStyle 1)

  );offsetNB 함수 종료
