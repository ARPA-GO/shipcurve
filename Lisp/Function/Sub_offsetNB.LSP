(defun offsetNB()
;�����Լ� offsetNB ����
;modeNB�϶� ������ ��Ÿ�� offsetǥ�� ������ �����ϱ����� �����Լ�
  
  (setq ExcelApp (LoadExcel))
  ;�����Լ� LoadExcel�� �ε��Ѵ�
  
  (vlax-put Excelapp "visible" :vlax-false)
  ;vlax-true�� ���, ������ �����Ų��. �̴� ����ڸ� �����ϰ� �� �� �����Ƿ� �����Ͽ���.
  
  (setq Workbooks (vlax-get-property ExcelApp 'Workbooks))
  ;�����ִ� ���������� Workbooks������ ����
  
  (setq CurrentWBook (vlax-invoke-method Workbooks 'Add))
  ;��ǥ�� ������ ������ �����͸� ����ϴ°��̹Ƿ� ���ο� ���������� ����
  
  (setq Sheets (vlax-get-property ExcelApp 'Sheets))
  ;���� ��Ʈ���� Shetts������ ����
  
  (setq AcSheet (vlax-get-property ExcelApp 'ActiveSheet))
  ;���� Ȱ��ȭ�� ��Ʈ�� AcSheet������ ����
  
  (setq Cells (vlax-get-property AcSheet 'Cells))
  ;Ȱ��ȭ�� ��Ʈ�� ������ Cells������ ����
  

  ;offset form---
  ;offsetǥ�� ���� �Ҽ��� 4°�ڸ����� �ݿø��ϹǷ� ������ ������ ��������
  
  (setq Ran (vlax-get-property Excelapp 'Range "B2:Z100"))
  ;B2���� ������ property�� Ran�� ����
  
  (vlax-put-property Ran 'Numberformat "0.000")
  ;Ran�� property�� ���������Ƿ� ���������� �������ִ� Numberformat�� �̿��� ���� ����

  ;WL Number-----
  ;WaterLine Number�� ǥ���ϴ� �κ��� ���� ����
  
  (setq colY 1 rowX 3)
  ;1�� 3��(C1)�� ����
  
  (setq val "BOTTOM")
  ;BOTTOM �̶�� ���� val������ ����
  
  (vlax-put-property Cells 'Item colY rowX val)
  ;C1�� val���� �־��

  (setq colY 1 rowX 4)
  ;1�� 4��(D1)�� ����
  
  (setq val "0.5 WL")
  ;0.5 W.L �̶�� ���� val������ ����
  
  (vlax-put-property Cells 'Item colY rowX val)
  ;D1�� val���� �־��
  
  (setq colY 1 rowX 5)
  ;E1
  
  (setq wlnumlist(mapcar '(lambda(x)(strcat (itoa x) " W.L"))wlnumlist))
  ;�����Լ� setWL���� ������ wlnumlist ����Ʈ ��ҵ鿡 "W.L"�� �߰�
  
  (mapcar
    '(lambda (val)
       (vlax-put-property Cells 'Item colY rowX val)
       (setq rowX(1+ rowX)))wlnumlist)
  ;���η� ���������� ����Ʈ��(wlnumlist)�� ����


  ;�� Ư�� ����
  (setq wx 3)
  ;C1���� �����ϱ����� ���� �ʱⰪ�� 3���� ����
  
  (repeat wllistn
  ;waterline ������ŭ �ݺ�
    
    (setq colY 1 rowX wx)
    ;C1���� ������
    
    (setq cel(vlax-variant-value(vlax-get-property Cells 'Item colY rowX)))
    ;���� �ٽ� ��ü�� ����
    
    (setq int(vlax-get-property cel 'Interior))
    ;������ �ٲٱ� ���� Interior�Ӽ��� ���� int������ ����
    
    (setq Font(vlax-get-property cel 'Font))
    ;�۲��� �β��� �ٲٱ� ���� Font �Ӽ��� ���� Font������ ����
    
    (setq borders(vlax-get-property cel 'Borders))
    ;�׵θ� ���� ������ ���� Borders�Ӽ��� ���� borders������ ����

    (setq bordersB(vlax-get-property borders 'Item 9))
    ;�׵θ��� �Ʒ��κ��� �Ӽ��� ���� bordersB������ ����
    
    (setq bordersR(vlax-get-property borders 'Item 10))
    ;�׵θ��� �����ʺκ��� �Ӽ��� ���� bordersR������ ����
    
    (vlax-put-property cel 'HorizontalAlignment -4108)
    ;���� �Էµ� ���� ���������� ���������
    
    (vlax-put-property int 'Color 14599344)
    ;���� ���� ����
    
    (vlax-put-property Font 'Bold "true")
    ;���� �۲� �β� ���� ����
    
    (vlax-put-property bordersB 'Weight 4)
    ;�Ʒ��� �׵θ� �β� ���� ����
    
    (vlax-put-property bordersB 'LineStyle 1)
    ;�Ʒ��� �׵θ� ��Ÿ�� ������ �Ǽ� ����
    
    (vlax-put-property bordersR 'Weight 2)
    ;������ �׵θ� �β� ��� ����
    
    (vlax-put-property bordersR 'LineStyle 1)
    ;������ �׵θ� ��Ÿ�� ������ �Ǽ� ����
    
    (setq wx(+ wx 1))
    );repeat�� ����
  

  ;ST Number-----
  ;Station Number�� ǥ���ϴ� �κ��� ���� ����
  ;WL Number�� ���κ� ����
  
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
  ;Ran���� ������ ������ ������ ������
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
  ;�Ѱ��� ���� �ƴ� ������ ������ ���̹Ƿ� ���� �׵θ��� ���� �׵θ��� �Ӽ��� ���� bordersV������ ����
  (setq bordersH(vlax-get-property borders 'Item 12))
  ;���� �׵θ��� �Ӽ��� ���� vordersH������ ����
  (vlax-put-property bordersR 'Weight 4)
  (vlax-put-property bordersV 'Weight 2)
  (vlax-put-property bordersH 'Weight 2)
  (vlax-put-property bordersR 'LineStyle 1)
  (vlax-put-property bordersV 'LineStyle 1)
  (vlax-put-property bordersH 'LineStyle 1)

  );offsetNB �Լ� ����