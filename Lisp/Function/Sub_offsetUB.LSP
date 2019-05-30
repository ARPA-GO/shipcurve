(defun offsetUB()
;�����Լ� offsetUB����,
;modeUB�϶� ������ ��Ÿ�� offsetǥ�� ������ �����ϱ� ���� �����Լ�
;��κ� offsetNB�Լ��� �����ϳ� wlnumlist, backlist���� ����Ʈ����
;�ٽ� �������� �ʰ�, ������ ���� �̿�

  (setq ExcelApp (LoadExcel))
  (vlax-put Excelapp "visible" :vlax-false)
  (setq Workbooks (vlax-get-property ExcelApp 'Workbooks))
  (setq CurrentWBook (vlax-invoke-method Workbooks 'Add))
  (setq Sheets (vlax-get-property ExcelApp 'Sheets))
  (setq AcSheet (vlax-get-property ExcelApp 'ActiveSheet))
  (setq Cells (vlax-get-property AcSheet 'Cells))
  

  ;offset form---------------------
  (setq Ran (vlax-get-property Excelapp 'Range "B2:Z100"))
  (vlax-put-property Ran 'Numberformat "0.000")


  ;;WL Number----------
  (setq colY 1 rowX 3)
  (setq val "BOTTOM")
  (vlax-put-property Cells 'Item colY rowX val)

  (setq colY 1 rowX 4)
  (setq val "0.5 WL")
  (vlax-put-property Cells 'Item colY rowX val)
  
  (setq colY 1 rowX 5)
  (mapcar
    '(lambda (val)
       (vlax-put-property Cells 'Item colY rowX val)
       (setq rowX(1+ rowX)))wlnumlist)

  (setq wx 3)
  (repeat wllistn
    (setq colY 1 rowX wx)
    (setq cel(vlax-variant-value(vlax-get-property Cells 'Item colY rowX)))
    (setq int(vlax-get-property cel 'Interior))
    (setq Font(vlax-get-property cel 'Font))
    (setq borders(vlax-get-property cel 'Borders))
    (setq bordersB(vlax-get-property borders 'Item 9))
    (setq bordersR(vlax-get-property borders 'Item 10))
    (vlax-put-property cel 'HorizontalAlignment -4108)
    (vlax-put-property int 'Color 14599344)
    (vlax-put-property Font 'Bold "true")
    (vlax-put-property bordersB 'Weight 4)
    (vlax-put-property bordersB 'LineStyle 1)
    (vlax-put-property bordersR 'Weight 2)
    (vlax-put-property bordersR 'LineStyle 1)
    (setq wx(+ wx 1)))

  ;;ST Number----------
  (setq colY 1 rowX 1)
  (mapcar
    '(lambda(val)
       (vlax-put-property Cells 'Item colY rowX val)
       (setq colY (1+ colY)))backlist)
  
  (setq colY 8 rowX 1)
  (mapcar
    '(lambda (val)
       (vlax-put-property Cells 'Item colY rowX val)
       (setq colY (1+ colY)))stnumlist)

  (setq colY 25 rowX 1)
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
  (setq bordersH(vlax-get-property borders 'Item 12))
  (vlax-put-property bordersR 'Weight 4)
  (vlax-put-property bordersV 'Weight 2)
  (vlax-put-property bordersH 'Weight 2)
  (vlax-put-property bordersR 'LineStyle 1)
  (vlax-put-property bordersV 'LineStyle 1)
  (vlax-put-property bordersH 'LineStyle 1)

  );offsetUB�Լ� ����