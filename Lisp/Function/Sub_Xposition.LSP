(defun Xposition()
;�����Լ� Xposition ����,
;�����Լ� STapart�� ���� �Է¹��� station���ݵ��� �̿��� station�� ���� x��ǥ�� ������ �Է��ϴ� �����Լ�
;������ �� �κк� station������ �����Ͽ� ��ġ�� ����� ������ �Է����ش�.  

  (setq colY 2 rowX 2)
  (setq val (- 0 (* 2 stern)))
  ;station transom�� x���̹Ƿ� stern�κ� ���ݿ� 2���Ͽ� 0���� ����
  ;���� ����
  (vlax-put-property Cells 'Item colY rowX val)

  (setq colY 3 rowX 2)
  (setq val (- 0 stern))
  (vlax-put-property Cells 'Item colY rowX val)

  (setq colY 4 rowX 2)
  (setq val 0)
  (vlax-put-property Cells 'Item colY rowX val)

  (setq colY 5 rowX 2)
  (setq slist(list 0.5 1 1.5 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 18.5 19 19.5 20))
  (setq slist(mapcar '(lambda(x)(* x square))slist))
    (mapcar
    '(lambda (val)
       (vlax-put-property Cells 'Item colY rowX val)
       (setq colY (1+ colY)))slist)

  (setq colY 29 rowX 2)
  (setq val (+ bow (* square 20)))
  (vlax-put-property Cells 'Item ColY rowX val)

  (setq colY 30 rowX 2)
  (setq val (+ bow (+ bow (* square 20))))
  (vlax-put-property Cells 'Item ColY rowX val)

  );Xposition�Լ� ����