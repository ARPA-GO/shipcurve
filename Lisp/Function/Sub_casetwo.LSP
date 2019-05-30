(defun casetwo()
;서브함수 casetwo 선언
;station을 이루는 도면상 객체가 2개인 경우 waterline별로 station과의 교차점을 찾는 서브함수
  
  (setq clist(list ) dlist(list ) blist(list ))
  ;clist는 station을 이루는 첫번째 요소의 waterline별 교차점 리스트
  ;dlist는 station을 이루는 두번째 요소의 waterline별 교차점 리스트
  ;blist는 clist의 각각의 요소와 dlist의 각각의 요소를 서로 더하여
  ;최종적으로 waterline별 station의 교차점들의 리스트
  ;리스트를 비우고 구문 시작, 
  
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
; 여기까지는 caseone과 같다.
  
  (setq blist (mapcar '(lambda (x y) (+ x y)) clist dlist))
  ; mapcar : 리스트에 연산규칙을 적용해준다.
  ; 예를 들어, (mapcar '1+(list 10 20 40))은 리스트(11 21 31)을 반환한다.
  ; lambda : 무영함수를 생성한다.
  ; 예를들어, (lambda(x)(+ x 2))를 유하사게 풀이해보면
  ; (defun lambda함수(x) (setq result (+ x 2)) )와 같다.
  ; 즉, 변수에 2를 더해주는 함수를 생성한다.
  ; 리스트 요소에 연산규칙을 수행해주는 mapcar함수와 무영함수를 생성하는 lambda함수를 사용해
  ; clist와 dlist의 각각의 요소를 서로 더해 최종적인 blist를 구한다.
  );casetwo 함수 종료
