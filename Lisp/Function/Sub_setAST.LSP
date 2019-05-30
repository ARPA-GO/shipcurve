(defun setAST()
;서브함수 setAST 선언
;선수부station 레이어 이름을 저장해놓은 Alaylist를 이용해 선수부 station 구분하는 함수

  (if (= Alaylistn 15)
  ;조건 : Alaylistn(선수부 레이어이름 리스트 길이) = 15
    
    (progn
      (setq nn 0)
      (repeat (length Astlist)
      ;Astlist(선수부 station) 길이만큼 반복하라
	
	(cond
	;조건문이지만 if 처럼 거짓일 경우 실행문이 따로 없고 다음으로 넘어간다.
	  
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 0 Alaylist)) (setq sta (append sta (list (nth nn Astlist)))))
	  ;조건 : Astlist의 nn번째 요소의 레이어 이름 = Alaylist 의 0번째 요소
	  ;참일경우 : Astlist의 nn번째 요소(도면이름)를 sta리스트에 추가하라, sta리스트는 station transom을 이루는 객체들로 지정
	  ;거짓일경우 : 다음줄로 넘어감
	  
	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 1 Alaylist)) (setq stb (append stb (list (nth nn Astlist)))))

	  ((= (cdr(assoc 8 (entget(nth nn Astlist)))) (nth 2 Alaylist)) (setq stc (append stc (list (nth nn Astlist)))))
	  ;조건 : Astlist의 nn번째 요소의 레이어 이름 = Alaylist의 2번째 요소
	  ;참일경우 : Astlist의 nn번째 요소(도면이름)를 stc리스트에 추가하라, stc리스트는 station A.P를 이루는 객체들로 지정
	  ;거짓일 경우 : 다음줄로 넘어감
	  ;이하 동일
	  
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
  ;sta stb stc...는 다른 서브함수에서도 사용되어 값을 유지하여야하지만
  ;리스트에 append로 요소를 추가받는 리스트 형태이므로 지역변수로 선언해주어야
  ;함수 재 사용시 리스트 요소가 누적되지 않는다.

  )
