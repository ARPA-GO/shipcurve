(defun casetwo()
;�����Լ� casetwo ����
;station�� �̷�� ����� ��ü�� 2���� ��� waterline���� station���� �������� ã�� �����Լ�
  
  (setq clist(list ) dlist(list ) blist(list ))
  ;clist�� station�� �̷�� ù��° ����� waterline�� ������ ����Ʈ
  ;dlist�� station�� �̷�� �ι�° ����� waterline�� ������ ����Ʈ
  ;blist�� clist�� ������ ��ҿ� dlist�� ������ ��Ҹ� ���� ���Ͽ�
  ;���������� waterline�� station�� ���������� ����Ʈ
  ;����Ʈ�� ���� ���� ����, 
  
  (setq ni 0 m 0)
  (repeat wllistn
    (setq wl(nth ni wllist))
    (setq obj1(vlax-ename->vla-object wl))
    (setq interpc(vlax-invoke obj1 'intersectwith obj3 0))
    (setq selectxc(car interpc))
    (if (/= selectxc nil)
      (progn
	(setq selectxc(abs selectxc))
	(setq clist(append clist(list selectxc))))
      (setq clist(append clist(list m))))
    (setq ni(+ ni 1)))

  (setq ni 0 m 0)
  (repeat wllistn
    (setq wl(nth ni wllist))
    (setq obj1(vlax-ename->vla-object wl))
    (setq interpd(vlax-invoke obj1 'intersectwith obj4 0))
    (setq selectxd(car interpd))
    (if (/= selectxd nil)
      (progn
	(setq selectxd(abs selectxd))
	(setq dlist(append dlist(list selectxd))))
      (setq dlist(append dlist(list m))))
    (setq ni(+ ni 1)))
; ��������� caseone�� ����.
  
  (setq blist (mapcar '(lambda (x y) (+ x y)) clist dlist))
  ; mapcar : ����Ʈ�� �����Ģ�� �������ش�.
  ; ���� ���, (mapcar '1+(list 10 20 40))�� ����Ʈ(11 21 31)�� ��ȯ�Ѵ�.
  ; lambda : �����Լ��� �����Ѵ�.
  ; �������, (lambda(x)(+ x 2))�� ���ϻ�� Ǯ���غ���
  ; (defun lambda�Լ�(x) (setq result (+ x 2)) )�� ����.
  ; ��, ������ 2�� �����ִ� �Լ��� �����Ѵ�.
  ; ����Ʈ ��ҿ� �����Ģ�� �������ִ� mapcar�Լ��� �����Լ��� �����ϴ� lambda�Լ��� �����
  ; clist�� dlist�� ������ ��Ҹ� ���� ���� �������� blist�� ���Ѵ�.
  );casetwo �Լ� ����