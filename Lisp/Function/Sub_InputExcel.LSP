(defun InputExcel()
;�����Լ� InputExcel ����,
;�������� ���ϴ� intersect�Լ����� ���� ���� ������ ������ �����Լ�
  
  (setq xlist blist)
  ;intersect�Լ��� ���� ���� x��ǥ ����Ʈ�� blist�� xlist�� ����
  
  (setq colY mm rowX 3)
  ;���� ���� ������ �ξ� station�� ���� ���� ���� ���� ����
  
  (mapcar
    '(lambda(val)
       (vlax-put-property Cells 'Item colY rowX val)
       (setq rowX (1+ rowX)))xlist)

  );InputExcel �Լ� ����