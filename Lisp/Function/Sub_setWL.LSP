(defun setWL()
;�����Լ� setWL����, ���� ��ü���� waterline�� �Ǻ��س��� ����, �������� ����

  (setq wllist(list ) wlnumlist(list ))
  ;wllist�� wlnumlist�� �� ����Ʈ�� ��������
  ;�� ���� �ȿ� ���� body�� ���� ���ϰ� ���� ��� modeNB�� ������ ��� �� �����̹Ƿ�
  ;waterline�� ���� �̸��� �����س��� ����Ʈ�� offset�� �Է��� WL������ ������ ����Ʈ�� �����

  (setq num 0)
  ;���� num �� 0

  (repeat (sslength wlspl)
  ;wlspl�� ����� ��Ʈ�� ������ŭ �ݺ��ض�

    (setq name(ssname wlspl num))
    ;���� name�� wlspl����Ʈ�� num��° ��Ʈ�� ���� �̸��� ������

    (if (and (= "LINE" (cdr(assoc 0 (entget name))))
	     ;��ü�� Line�̿����Ѵٴ� ����
	     ;entget�� �����̸��� name�� ��ü�� entity list ����
	     ;assoc 0 : entget�� ���� ���� entity lsit�� 0��°�� �ش��ϴ� list ����
	     ;cdr : assoc�� ���� ���� ������ ����Ʈ �� ù��° ���� �����ϰ� ����

	     (or (zerop (vla-get-angle (vlax-ename->vla-object name)))
		 ;vlax-ename->vla-object name : name�� ������ �����̸��� ��ü�� �ٲپ��ش�.
		 ;vla-get-angle : ��ü�� ������ ���Ѵ�.
		 ;zerop : ��ü�� ������ 0�̿��� �Ѵٴ� ����

		 (equal (vla-get-angle (vlax-ename->vla-object name)) pi 0.0001)
		 ;��ü�� ����=180�� �̿��� �Ѵٴ� ����

		 );or ����
	     );and ����
      ;waterline�� ����� �����̹Ƿ� ��ü�� ������ 0 �Ǵ� 180 �ΰ��� �����̴�.

      (setq wllist(append wllist (list name)))
      ;���ǹ��� ���ϰ�� ��ü�� �̸��� wllist ����Ʈ�� �߰���

      );If�� ����

    (setq num(+ num 1))
    ;���� num�� num+1������ ������

    );repeat�� ����

  (setq wllist(vl-sort wllist '(lambda (x y)(< (cadr (cdr(assoc 10 (entget x))))
					       (cadr (cdr(assoc 10 (entget y))))))))
  ;wllist ����Ʈ�� ����Ʈ ����� ������ ������ ��ǥ��(y)�������� �����϶�

  (setq wllistn(length wllist))
  ;wllist ����Ʈ�� ���̸� wllistn ������ ����

  (setq wlnum 1)
  ;wlnum ������ 1�� ����

  (repeat (- wllistn 2)
  ;wllistn-2 ��ŭ �ݺ��϶�

    (setq wlnumlist(append wlnumlist(list wlnum)))
    ;wlnum�� wlnumlist ����Ʈ�� �߰��Ѱ��� wlnumlsit ��� ����

    (setq wlnum(+ wlnum 1))
    ;���� wlnum�� num+1������ ����

    );repeat�� ����

  );setWL �Լ� ����