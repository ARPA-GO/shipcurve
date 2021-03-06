(defun setFST()
;서브함수 setFST 정의
;선미부 station 레이어 이름을 저장해놓은 Flaylist를 이용해 선미부station 구분하는 함수
;이하 setAST와 동일
  
  (if (= Flaylistn 14)
    (progn
      (setq nn 0)
      (repeat (length Fstlist)
	(cond
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 0 Flaylist)) (setq staa(append staa (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 1 Flaylist)) (setq stbb(append stbb (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 2 Flaylist)) (setq stcc(append stcc (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 3 Flaylist)) (setq stdd(append stdd (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 4 Flaylist)) (setq stee(append stee (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 5 Flaylist)) (setq stff(append stff (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 6 Flaylist)) (setq stgg(append stgg (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 7 Flaylist)) (setq sthh(append sthh (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 8 Flaylist)) (setq stii(append stii (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 9 Flaylist)) (setq stjj(append stjj (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 10 Flaylist)) (setq stkk(append stkk (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 11 Flaylist)) (setq stll(append stll (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 12 Flaylist)) (setq stmm(append stmm (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 13 Flaylist)) (setq stnn(append stnn (list (nth nn Fstlist))))))
	(setq nn(+ nn 1)))))

  (if (= Flaylistn 13)
    (progn
      (setq nn 0)
      (repeat (length Fstlist)
	(cond
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 0 Flaylist)) (setq staa(append staa (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 1 Flaylist)) (setq stbb(append stbb (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 2 Flaylist)) (setq stcc(append stcc (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 3 Flaylist)) (setq stdd(append stdd (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 4 Flaylist)) (setq stee(append stee (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 5 Flaylist)) (setq stff(append stff (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 6 Flaylist)) (setq stgg(append stgg (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 7 Flaylist)) (setq sthh(append sthh (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 8 Flaylist)) (setq stii(append stii (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 9 Flaylist)) (setq stjj(append stjj (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 10 Flaylist)) (setq stkk(append stkk (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 11 Flaylist)) (setq stll(append stll (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 12 Flaylist))
	   (setq stmm(append stmm (list (nth nn Fstlist))) stnn(append stnn (list (nth nn Fstlist))))))
	(setq nn(+ nn 1)))))

  (if (= Flaylistn 12)
    (progn
      (setq nn 0)
      (repeat (length Fstlist)
	(cond
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 0 Flaylist)) (setq staa(append staa (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 1 Flaylist)) (setq stbb(append stbb (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 2 Flaylist)) (setq stcc(append stcc (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 3 Flaylist)) (setq stdd(append stdd (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 4 Flaylist)) (setq stee(append stee (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 5 Flaylist)) (setq stff(append stff (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 6 Flaylist)) (setq stgg(append stgg (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 7 Flaylist)) (setq sthh(append sthh (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 8 Flaylist)) (setq stii(append stii (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 9 Flaylist)) (setq stjj(append stjj (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 10 Flaylist)) (setq stkk(append stkk (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 11 Flaylist))
	   (setq stll(append stll (list (nth nn Fstlist))) stmm(append stmm (list (nth nn Fstlist)))
		 stnn(append stnn (list (nth nn Fstlist))))))
	(setq nn(+ nn 1)))))

  (if (= Flaylistn 11)
    (progn
      (setq nn 0)
      (repeat (length Fstlist)
	(cond
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 0 Flaylist)) (setq staa(append staa (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 1 Flaylist)) (setq stbb(append stbb (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 2 Flaylist)) (setq stcc(append stcc (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 3 Flaylist)) (setq stdd(append stdd (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 4 Flaylist)) (setq stee(append stee (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 5 Flaylist)) (setq stff(append stff (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 6 Flaylist)) (setq stgg(append stgg (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 7 Flaylist)) (setq sthh(append sthh (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 8 Flaylist)) (setq stii(append stii (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 9 Flaylist)) (setq stjj(append stjj (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 10 Flaylist))
	   (setq stkk(append stkk (list (nth nn Fstlist))) stll(append stll (list (nth nn Fstlist)))
		 stmm(append stmm (list (nth nn Fstlist))) stnn(append stnn (list (nth nn Fstlist))))))
	(setq nn(+ nn 1)))))

  (if (= Flaylistn 10)
    (progn
      (setq nn 0)
      (repeat (length Fstlist)
	(cond
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 0 Flaylist)) (setq staa(append staa (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 1 Flaylist)) (setq stbb(append stbb (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 2 Flaylist)) (setq stcc(append stcc (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 3 Flaylist)) (setq stdd(append stdd (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 4 Flaylist)) (setq stee(append stee (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 5 Flaylist)) (setq stff(append stff (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 6 Flaylist)) (setq stgg(append stgg (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 7 Flaylist)) (setq sthh(append sthh (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 8 Flaylist)) (setq stii(append stii (list (nth nn Fstlist)))))
	  ((= (cdr(assoc 8 (entget(nth nn Fstlist)))) (nth 9 Flaylist))
	   (setq stjj(append stjj (list (nth nn Fstlist))) stkk(append stkk (list (nth nn Fstlist)))
		 stll(append stll (list (nth nn Fstlist))) stmm(append stmm (list (nth nn Fstlist)))
		 stnn(append stnn (list (nth nn Fstlist))))))
	(setq nn(+ nn 1)))))

  (setq #staa staa #stbb stbb #stcc stcc #stdd stdd #stee stee #stff stff #stgg stgg
	#sthh sthh #stii stii #stjj stjj #stkk stkk #stll stll #stmm stmm #stnn stnn)

  )
