(defun caseone()
;�����Լ� caseone ����
;station�� ����� ��ü 1���� �׷����� ���, waterline�� station�� ������ ã�� �����Լ�
  
  (setq blist(list ))
  ;blist�� ����ְ� ���� ����
  ;blist�� waterline�� station�� �������� x��ǥ ����Ʈ
  
  (setq ni 0 m 0)
  
  (repeat wllistn
  ;wllistn(waterline����) ��ŭ �����ض�
    
    (setq wl(nth ni wllist))
    ;wllist(waterline���� �����̸� ����Ʈ)����Ʈ�� ni��°�� ���� wl�� ����
    
    (setq obj1(vlax-ename->vla-object wl))
    ;�����̸��� wl�� ��ü�� �ٲپ� ���� obj1�� ����
    
    (setq interp(vlax-invoke obj1 'intersectwith obj2 0))
    ;obj1(waterline) �� obj2(station)�� �������� ���� interp�� ����
    ;vlax-invoke ��ü1 'intersectwith ��ü2 0 :��ü1�� ��ü 2�� �������� ã�� �Լ�
    ;0�� �ƴ϶� 1�̸�, �� ��ü�� �������� ������ �����Ͽ� ������ �������� ã����� ��
    
    (setq selectx(car interp))
    ;�������� ù��° ���(x��ǥ)�� ���� selectx�� ����
    
    (if (/= selectx nil)
    ;���� : �������� ����
      
      (progn
      ;������ ���ϰ��(�������� �����Ұ��) ���๮ ����
	
	(setq selectx(abs selectx))
	;selectx(�������� x��ǥ)�� ������ ���� ����
	
	(setq blist(append blist(list selectx)))
	;blist�� selectx�� �߰�

	);������ ���ϰ�� ���๮ ���� progn ����
	
      (setq blist(append blist(list m)))
      ;������ ������ ���(�������� �������� �������) blist�� m(0)�� �߰�

      );������ ���翩�� ���ǹ� ����
    
    (setq ni(+ ni 1))
    ;ni�� ni+1 ������ ����

    );repeat�� ����
  
  (if (= (last blist) 0)
  ;���� : blist�� ������ ��Ұ� 0�� ���
  ;��ǥ������ Station No.10 ���� ��� ������ waterline���� �������� �� ����.
  ;��, �ش� waterline���� ������ ���� ���̿� ���� ���� �����ٴ� ���̹Ƿ� �� ���ǹ��� �ۼ��Ͽ���.
    
    (setq blist(subst halfB '0 blist))
    ;blist�� �����ϴ� 0�� halB(�ʹݿ� ����ڿ��� �Է¹��� ����)�� ��ü�϶�

    );���ǹ� ����

  );caseone�Լ� ����