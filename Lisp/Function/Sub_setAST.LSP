(defun setAST()
;�����Լ� setAST ����
;������station ���̾� �̸��� �����س��� Alaylist�� �̿��� ������ station �����ϴ� �Լ�

  (if (= Alaylistn 15)
  ;���� : Alaylistn(������ ���̾��̸� ����Ʈ ����) = 15
    
    (progn
      (setq nn 0)
      (repeat (length Astlist)
      ;Astlist(������ station) ���̸�ŭ �ݺ��϶�
	
	(cond
	;���ǹ������� if ó�� ������ ��� ���๮�� ���� ���� �������� �Ѿ��.
	  
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 0 Alaylist)) (setq sta (append sta (list (nth nn Astlist)))))
	  ;���� : Astlist�� nn��° ����� ���̾� �̸� = Alaylist �� 0��° ���
	  ;���ϰ�� : Astlist�� nn��° ���(�����̸�)�� sta����Ʈ�� �߰��϶�, sta����Ʈ�� station transom�� �̷�� ��ü��� ����
	  ;�����ϰ�� : �����ٷ� �Ѿ
	  
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 1 Alaylist)) (setq stb (append stb (list (nth nn Astlist)))))

	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 2 Alaylist)) (setq stc (append stc (list (nth nn Astlist)))))
	  ;���� : Astlist�� nn��° ����� ���̾� �̸� = Alaylist�� 2��° ���
	  ;���ϰ�� : Astlist�� nn��° ���(�����̸�)�� stc����Ʈ�� �߰��϶�, stc����Ʈ�� station A.P�� �̷�� ��ü��� ����
	  ;������ ��� : �����ٷ� �Ѿ
	  ;���� ����
	  
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 3 Alaylist)) (setq std (append std (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 4 Alaylist)) (setq ste (append ste (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 5 Alaylist)) (setq stf (append stf (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 6 Alaylist)) (setq stg (append stg (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 7 Alaylist)) (setq sth (append sth (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 8 Alaylist)) (setq sti (append sti (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 9 Alaylist)) (setq stj (append stj (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 10 Alaylist)) (setq stk (append stk (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 11 Alaylist)) (setq stl (append stl (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 12 Alaylist)) (setq stm (append stm (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 13 Alaylist)) (setq stn (append stn (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 14 Alaylist)) (setq sto (append sto (list (nth nn Astlist))))))
	(setq nn(+ nn 1)))))	
  
  (if (= Alaylistn 14)
    (progn
      (setq nn 0)
      (repeat (length Astlist)
	(cond
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 0 Alaylist)) (setq sta (append sta (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 1 Alaylist)) (setq stb (append stb (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 2 Alaylist)) (setq stc (append stc (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 3 Alaylist)) (setq std (append std (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 4 Alaylist)) (setq ste (append ste (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 5 Alaylist)) (setq stf (append stf (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 6 Alaylist)) (setq stg (append stg (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 7 Alaylist)) (setq sth (append sth (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 8 Alaylist)) (setq sti (append sti (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 9 Alaylist)) (setq stj (append stj (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 10 Alaylist)) (setq stk (append stk (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 11 Alaylist)) (setq stl (append stl (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 12 Alaylist)) (setq stm (append stm (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 13 Alaylist))
	   (setq stn (append stn (list (nth nn Astlist))) sto (append sto (list (nth nn Astlist))))))
	(setq nn(+ nn 1)))))

  (if (= Alaylistn 13)
    (progn
      (setq nn 0)
      (repeat (length Astlist)
	(cond
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 0 Alaylist)) (setq sta (append sta (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 1 Alaylist)) (setq stb (append stb (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 2 Alaylist)) (setq stc (append stc (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 3 Alaylist)) (setq std (append std (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 4 Alaylist)) (setq ste (append ste (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 5 Alaylist)) (setq stf (append stf (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 6 Alaylist)) (setq stg (append stg (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 7 Alaylist)) (setq sth (append sth (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 8 Alaylist)) (setq sti (append sti (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 9 Alaylist)) (setq stj (append stj (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 10 Alaylist)) (setq stk (append stk (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 11 Alaylist)) (setq stl (append stl (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 12 Alaylist))
	   (setq stm (append stm (list (nth nn Astlist))) stn (append stn (list (nth nn Astlist)))
		 sto (append sto (list (nth nn Astlist)))))
	  (setq nn(+ nn 1))))))

  (if (= Alaylistn 12)
    (progn
      (setq nn 0)
      (repeat (length Astlist)
	(cond
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 0 Alaylist)) (setq sta (append sta (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 1 Alaylist)) (setq stb (append stb (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 2 Alaylist)) (setq stc (append stc (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 3 Alaylist)) (setq std (append std (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 4 Alaylist)) (setq ste (append ste (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 5 Alaylist)) (setq stf (append stf (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 6 Alaylist)) (setq stg (append stg (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 7 Alaylist)) (setq sth (append sth (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 8 Alaylist)) (setq sti (append sti (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 9 Alaylist)) (setq stj (append stj (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 10 Alaylist)) (setq stk (append stk (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 11 Alaylist))
	   (setq stl (append stl (list (nth nn Astlist))) stm (append stm (list (nth nn Astlist)))
		 stn (append stn (list (nth nn Astlist))) sto (append sto (list (nth nn Astlist))))))
	(setq nn(+ nn 1)))))

  (if (= Alaylistn 11)
    (progn
      (setq nn 0)
      (repeat (length Astlist)
	(cond
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 0 Alaylist)) (setq sta (append sta (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 1 Alaylist)) (setq stb (append stb (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 2 Alaylist)) (setq stc (append stc (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 3 Alaylist)) (setq std (append std (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 4 Alaylist)) (setq ste (append ste (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 5 Alaylist)) (setq stf (append stf (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 6 Alaylist)) (setq stg (append stg (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 7 Alaylist)) (setq sth (append sth (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 8 Alaylist)) (setq sti (append sti (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 9 Alaylist)) (setq stj (append stj (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 10 Alaylist))
	   (setq stk (append stk (list (nth nn Astlist))) stl (append stl(list (nth nn Astlist)))
		 stm (append stm (list (nth nn Astlist))) stn (append stn(list (nth nn Astlist)))
		 sto (append sto (list (nth nn Astlist))))))
	(setq nn(+ nn 1)))))

  (if (= Alaylistn 10)
    (progn
      (setq nn 0)
      (repeat (length Astlist)
	(cond
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 0 Alaylist)) (setq sta (append sta (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 1 Alaylist)) (setq stb (append stb (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 2 Alaylist)) (setq stc (append stc (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 3 Alaylist)) (setq std (append std (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 4 Alaylist)) (setq ste (append ste (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 5 Alaylist)) (setq stf (append stf (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 6 Alaylist)) (setq stg (append stg (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 7 Alaylist)) (setq sth (append sth (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 8 Alaylist)) (setq sti (append sti (list (nth nn Astlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 9 Alaylist))
	   (setq stj (append stj (list (nth nn Astlist))) stk (append stk (list (nth nn Astlist)))
		 stl (append stl (list (nth nn Astlist))) stm (append stm (list (nth nn Astlist)))
		 stn (append stn (list (nth nn Astlist))) sto (append sto (list (nth nn Astlist))))))
	(setq nn(+ nn 1)))))

  (setq #sta sta #stb stb #stc stc #std std #ste ste #stf stf #stg stg
	#sth sth #sti sti #stj stj #stk stk #stl stl #stm stm #stn stn #sto sto)
  ;sta stb stc...�� �ٸ� �����Լ������� ���Ǿ� ���� �����Ͽ���������
  ;����Ʈ�� append�� ��Ҹ� �߰��޴� ����Ʈ �����̹Ƿ� ���������� �������־��
  ;�Լ� �� ���� ����Ʈ ��Ұ� �������� �ʴ´�.

  )