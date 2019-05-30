(defun separateST()
;�����Լ� separateST����, station�� ���̺�, �����η� ������ ����Ŵ
  
  (setq Astlist(list ) Fstlist(list ) Alaylist(list ) Flaylist(list ))
  ;���� setWL�Լ��� ���������� ����Ʈ ����ְ� ���� ����
  ;Astlist:���̺�station                Fstlist:������station
  ;Alaylist:���̺�station�Ƿ��̾��̸�   Flaylsit:������station�Ƿ��̾��̸�
  
  (setq num 0)
  ;���� num�� 0�� ����
  
  (repeat (sslength wlspl)
  ;wlspl ��Ʈ ����Ʈ ���̸�ŭ �ݺ��ض�
    
    (setq name(ssname wlspl num))
    ;wlspl ��Ʈ ����Ʈ�� num��° ����� �����̸��� ���� name�� ����
    
    (setq layname(cdr (assoc 8 (entget name))))
    ;���̾� �̸��� layname������ ����
    
    (setq objname(vlax-ename->vla-object name))
    ;���� �̸��� ��ü�� �ٲپ� objname ������ ����
    
    (if (= "SPLINE" (cdr(assoc 0 (entget name))))
    ;���� : ����� ���� = SPLINE
      
      (progn
      ;���ǹ� ���� ���๮�� �������ϰ�� �Ѱ��� �����ش�. ��������� spline�ϰ��(������ ���ΰ��) ���๮ ����

	(setq jpoint(car(vlax-curve-getpointatparam objname 0.5)))
	;��� �߰����� ��ǥ�� x��ǥ�� jpoint������ ����
	
	(if (< jpoint 0)
	;���� : jpoint(�߰����� x��ǥ) < 0
	  
	  (progn
	  ;jpoint���ǹ� ���ΰ�� ���๮ ����
	    (setq Astlist(append Astlist(list name)))
	    ;����� ���� �̸��� Astlist ����Ʈ�� ����
	    
	    (if (= (member layname Alaylist) nil)
	    ;���� : Alaylist ����Ʈ�� layname(����� ���̾� �̸�)�� �����������
	      
	      (setq Alaylist(append Alaylist(list layname)))
	      ;������ ���ϰ�� Alaylist�� layname�� �߰��Ѵ�.
	      
	      );Alaylist ���ǹ� ����
	    
	    );jpoint���ǹ� ���ϰ�� ���๮ ���� progn ����
	  
	  (progn
	  ;jpoint���ǹ� ������ ��� ���๮ ����
	    
	    (setq Fstlist(append Fstlist(list name)))
	    ;����� ���� �̸��� Fstlist ����Ʈ�� ����
	    
	    (if (= (member layname Flaylist) nil)
	    ;���� : Flaylist ����Ʈ�� layname(����� ���̾� �̸�)�� ���� �������
	      
	      (setq Flaylist(append Flaylist(list layname)))
	      ;������ ���ϰ�� Flaylist�� layname�� �߰��Ѵ�.

	      );Flaylist ���ǹ� ����

	    );jpoint���ǹ� ������ ��� ���๮ ���� progn ����

	  );jpoint���ǹ� ����

	);��� ������ spline�ϰ�� ���๮ ���� progn ����
      
      (progn
      ;��� ���� ���ǹ��� ������ ��� ���๮ ����
	
	(if (= "ARC" (cdr(assoc 0 (entget name))))
	;���� : ��� ���� = ARC
	  
	  (progn
	  ;�������=ARC �� ��� (������ ���ΰ��) ���๮ ����
	    
	    (setq jpoint(car(vlax-curve-getstartpoint objname)))
	    ;����� �������� x��ǥ�� jpoint�� ����
	    
	    (if (< jpoint 0)
	    ;���ϴ� spline�� ���� ���������� Astlist, Fstlist�Ǻ�
	      
	      (progn
		(setq Astlist(append Astlist(list name)))
		(if (= (member layname Astlist) nil)
		  (setq Alaylist(append Alaylist(list layname)))))
	      
	      );jpoint ���ǹ� ����

	    );��� ���� ARC ���ϰ�� ���๮ ���� progn����

	  );������� ARC ���ǹ� ����

	);������� spline ���ǹ� ������ ��� ���๮ ���� progn ����

      );������� spline ���ǹ� ����
      
    (setq num(+ num 1))
    ;���� num�� num+1�� ����

    );repeat�� ����
  
  (setq Alaylist(vl-sort Alaylist '<))
  ;Alyalist ����Ʈ(���̾� �̸� ����Ʈ)�� ������������ �����϶�
  
  (setq Alaylistn(length Alaylist))
  ;Alaylsit�� ���̸� ���� Alaylistn�� ����
  
  (setq Alastlist(append Alastlist (list (nth (- Alaylistn 1) Alaylist)
					 (nth (- Alaylistn 2) Alaylist)
					 (nth (- Alaylistn 3) Alaylist))))
  ;Alaylist ����Ʈ�� (Alaylistn-1), (Alaylistn-2), (Alaylistn-3)��° ��ҵ��� Alastlist�� �߰�
  
  (setq Alaylist(vl-remove (nth 0 Alastlist) Alaylist))
  (setq Alaylist(vl-remove (nth 1 Alastlist) Alaylist))
  (setq Alaylist(vl-remove (nth 2 Alastlist) Alaylist))
  ;Alaylsit�� 0,1,2 ��° ��Ҹ� Alaylist���� ����
  
  (setq Alaylist(append Alastlist Alaylist))
  ;Alaylist�� Alastlist�� �߰��ϰ� �װ��� Alaylist������ ����

  (setq Flaylist(vl-sort Flaylist '>))
  ;Flaylist ����Ʈ�� ������������ �����϶�
  
  (setq Flaylistn(length Flaylist))
  ;Flaylist ����Ʈ�� ���̸� Flaylistn ������ ����

  )