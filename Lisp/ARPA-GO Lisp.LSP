;Main Function----------------------------------------------------------------------------------------------------------------------------------------------
(defun c:ARPAGO (/ oldsnap)
  
  (setq oldsnap(getvar "osmode"))
  (setvar "osmode" 0)

  (vl-load-com)

  (initget "N U")
  (setq mode(getkword "Choose Mode [ New Body(N) // Update Body(U) ]  :  "))(terpri)
  
  (if (= mode nil)(setq mode "N"))
  
  (if (= mode "N")
    (modeNB)
    (modeUB))

  (alert "Excel을 확인해주세요 !")

  (setvar "osmode" oldsnap)
  (princ)
  )

;Sub Function_modeNB-------------------
(defun modeNB (/ wlspl num ni m objname jpoint Astlist Fstlist Alaylist Flaylist Alaylistn Alastlist Flastlist sta stb stc std ste stf stg sth sti stj stk stl stm stn sto stnn stmm stll stkk stjj stii sthh stgg stff stee stdd stcc stbb staa mm interp interpc interpd selectx selectxc selectxd blist clist dlist xlist obj1 obj2 obj3 obj4 excelPath ExcelApp workbooks currentwbook sheets acsheet cells borders font interior bordersB bordersH bordersV bordersR ran val )

  (setq halfB(getreal "Breadth/2 : "))(terpri)
  (STapart)
  (setq wlspl(ssget '((0 . "LINE,SPLINE,ARC"))))
  (setWL)
  (setST)
  (offsetNB)
  (Xposition)
  (intersect)

  )

;Sub Function_modeUB-------------------
(defun modeUB()

  (offsetUB)
  (Xposition)
  (intersect)

  )

;Sub Function_STapart-----------------------------
(defun STapart()

  (setq stern(getreal "Stern Station Apart :  "))(terpri)
  (setq square(getreal "Square Station Apart  :  "))(terpri)
  (setq Bow(getreal "Bow Station Apart  : "))(terpri)
  
  )

;Sub Function_setWL--------------------------------
(defun setWL()

  (setq wllist(list ) wlnumlist(list ))

  (setq num 0)
  (repeat (sslength wlspl)
    (setq name(ssname wlspl num))
    (if (and (= "LINE" (cdr(assoc 0 (entget name))))
	     (or (zerop (vla-get-angle (vlax-ename->vla-object name)))
		 (equal (vla-get-angle (vlax-ename->vla-object name)) pi 0.0001)))
      (setq wllist(append wllist (list name))))
    (setq num(+ num 1)))

  (setq wllist(vl-sort wllist '(lambda (x y)(< (cadr (cdr(assoc 10 (entget x))))
					       (cadr (cdr(assoc 10 (entget y))))))))

  (setq wllistn(length wllist))
  
  (setq wlnum 1)
  (repeat (- wllistn 2)
    (setq wlnumlist(append wlnumlist(list wlnum)))
    (setq wlnum(+ wlnum 1)))
  
  )

;Sub Function_separateST---------------------------
(defun separateST()

  (setq Astlist(list ) Fstlist(list ) Alaylist(list ) Flaylist(list ))
  
  (setq num 0)
  (repeat (sslength wlspl)
    (setq name(ssname wlspl num))
    (setq layname(cdr (assoc 8 (entget name))))
    (setq objname(vlax-ename->vla-object name))
    (if (= "SPLINE" (cdr(assoc 0 (entget name))))
      (progn
	(setq jpoint(car(vlax-curve-getpointatparam objname 0.5)))
	(if (< jpoint 0)
	  (progn
	    (setq Astlist(append Astlist(list name)))
	    (if (= (member layname Alaylist) nil)
	      (setq Alaylist(append Alaylist(list layname)))))
	  (progn
	    (setq Fstlist(append Fstlist(list name)))
	    (if (= (member layname Flaylist) nil)
	      (setq Flaylist(append Flaylist(list layname)))))))
      (progn
	(if (= "ARC" (cdr(assoc 0 (entget name))))
	  (progn
	    (setq jpoint(car(vlax-curve-getstartpoint objname)))
	    (if (< jpoint 0)
	      (progn
		(setq Astlist(append Astlist(list name)))
		(if (= (member layname Astlist) nil)
		  (setq Alaylist(append Alaylist(list layname))))))))))
    (setq num(+ num 1)))

  (setq Alaylist(vl-sort Alaylist '<))
  (setq Alaylistn(length Alaylist))
  (setq Alastlist(append Alastlist (list (nth (- Alaylistn 1) Alaylist)
					 (nth (- Alaylistn 2) Alaylist)
					 (nth (- Alaylistn 3) Alaylist))))
  (setq Alaylist(vl-remove (nth 0 Alastlist) Alaylist))
  (setq Alaylist(vl-remove (nth 1 Alastlist) Alaylist))
  (setq Alaylist(vl-remove (nth 2 Alastlist) Alaylist))
  (setq Alaylist(append Alastlist Alaylist))

  (setq Flaylist(vl-sort Flaylist '>))
  (setq Flaylistn(length Flaylist))

  )

;Sub Function_setAST----------------------------
(defun setAST()

  (if (= Alaylistn 15)
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

  )

;Sub Function_setFST-------------------------------
(defun setFST()

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

;Sub Function_intersect-----------------
(defun intersect()

  (if (= (length #sta) 1)
    (progn
      (setq obj2(vlax-ename->vla-object (nth 0 #sta)))
      (caseone)
      (setq mm 2)
      (inputExcel))
    (progn
      (setq obj3(vlax-ename->vla-object (nth 0 #sta)))
      (setq obj4(vlax-ename->vla-object (nth 1 #sta)))
      (casetwo)
      (setq mm 2)
      (inputExcel)))

  (if (= (length #stb) 1)
    (progn
      (setq obj2(vlax-ename->vla-object (nth 0 #stb)))
      (caseone)
      (setq mm 3)
      (inputExcel))
    (progn
      (setq obj3(vlax-ename->vla-object (nth 0 #stb)))
      (setq obj4(vlax-ename->vla-object (nth 1 #stb)))
      (casetwo)
      (setq mm 3)
      (inputExcel)))

  (if (= (length #stc) 1)
    (progn
      (setq obj2(vlax-ename->vla-object (nth 0 #stc)))
      (caseone)
      (setq mm 4)
      (inputExcel))
    (progn
      (setq obj3(vlax-ename->vla-object (nth 0 #stc)))
      (setq obj4(vlax-ename->vla-object (nth 1 #stc)))
      (casetwo)
      (setq mm 4)
      (inputExcel)))

  (if (= (length #std) 1)
    (progn
      (setq obj2(vlax-ename->vla-object (nth 0 #std)))
      (caseone)
      (setq mm 5)
      (inputExcel))
    (progn
      (setq obj3(vlax-ename->vla-object (nth 0 #std)))
      (setq obj4(vlax-ename->vla-object (nth 1 #std)))
      (casetwo)
      (setq mm 5)
      (inputExcel)))

  (if (= (length #ste) 1)
    (progn
      (setq obj2(vlax-ename->vla-object (nth 0 #ste)))
      (caseone)
      (setq mm 6)
      (inputExcel))
    (progn
      (setq obj3(vlax-ename->vla-object (nth 0 #ste)))
      (setq obj4(vlax-ename->vla-object (nth 1 #ste)))
      (casetwo)
      (setq mm 6)
      (inputExcel)))

  (if (= (length #stf) 1)
    (progn
      (setq obj2(vlax-ename->vla-object (nth 0 #stf)))
      (caseone)
      (setq mm 7)
      (inputExcel))
    (progn
      (setq obj3(vlax-ename->vla-object (nth 0 #stf)))
      (setq obj4(vlax-ename->vla-object (nth 1 #stf)))
      (casetwo)
      (setq mm 7)
      (inputExcel)))

  (if (= (length #stg) 1)
    (progn
      (setq obj2(vlax-ename->vla-object (nth 0 #stg)))
      (caseone)
      (setq mm 8)
      (inputExcel))
    (progn
      (setq obj3(vlax-ename->vla-object (nth 0 #stg)))
      (setq obj4(vlax-ename->vla-object (nth 1 #stg)))
      (casetwo)
      (setq mm 8)
      (inputExcel)))

  (if (= (length #sth) 1)
    (progn
      (setq obj2(vlax-ename->vla-object (nth 0 #sth)))
      (caseone)
      (setq mm 9)
      (inputExcel))
    (progn
      (setq obj3(vlax-ename->vla-object (nth 0 #sth)))
      (setq obj4(vlax-ename->vla-object (nth 1 #sth)))
      (casetwo)
      (setq mm 9)
      (inputExcel)))

  (if (= (length #sti) 1)
    (progn
      (setq obj2(vlax-ename->vla-object (nth 0 #sti)))
      (caseone)
      (setq mm 10)
      (inputExcel))
    (progn
      (setq obj3(vlax-ename->vla-object (nth 0 #sti)))
      (setq obj4(vlax-ename->vla-object (nth 1 #sti)))
      (casetwo)
      (setq mm 10)
      (inputExcel)))

  (if (= (length #stj) 1)
    (progn
      (setq obj2(vlax-ename->vla-object (nth 0 #stj)))
      (caseone)
      (setq mm 11)
      (inputExcel))
    (progn
      (setq obj3(vlax-ename->vla-object (nth 0 #stj)))
      (setq obj4(vlax-ename->vla-object (nth 1 #stj)))
      (casetwo)
      (setq mm 11)
      (inputExcel)))

  (if (= (length #stk) 1)
    (progn
      (setq obj2(vlax-ename->vla-object (nth 0 #stk)))
      (caseone)
      (setq mm 12)
      (inputExcel))
    (progn
      (setq obj3(vlax-ename->vla-object (nth 0 #stk)))
      (setq obj4(vlax-ename->vla-object (nth 1 #stk)))
      (casetwo)
      (setq mm 12)
      (inputExcel)))

  (if (= (length #stl) 1)
    (progn
      (setq obj2(vlax-ename->vla-object (nth 0 #stl)))
      (caseone)
      (setq mm 13)
      (inputExcel))
    (progn
      (setq obj3(vlax-ename->vla-object (nth 0 #stl)))
      (setq obj4(vlax-ename->vla-object (nth 1 #stl)))
      (casetwo)
      (setq mm 13)
      (inputExcel)))

  (if (= (length #stm) 1)
    (progn
      (setq obj2(vlax-ename->vla-object (nth 0 #stm)))
      (caseone)
      (setq mm 14)
      (inputExcel))
    (progn
      (setq obj3(vlax-ename->vla-object (nth 0 #stm)))
      (setq obj4(vlax-ename->vla-object (nth 1 #stm)))
      (casetwo)
      (setq mm 14)
      (inputExcel)))

  (if (= (length #stn) 1)
    (progn
      (setq obj2(vlax-ename->vla-object (nth 0 #stn)))
      (caseone)
      (setq mm 15)
      (inputExcel))
    (progn
      (setq obj3(vlax-ename->vla-object (nth 0 #stn)))
      (setq obj4(vlax-ename->vla-object (nth 1 #stn)))
      (casetwo)
      (setq mm 15)
      (inputExcel)))

  (if (= (length #sto) 1)
    (progn
      (setq obj2(vlax-ename->vla-object (nth 0 #sto)))
      (caseone)
      (setq mm 16)
      (inputExcel))
    (progn
      (setq obj3(vlax-ename->vla-object (nth 0 #sto)))
      (setq obj4(vlax-ename->vla-object (nth 1 #sto)))
      (casetwo)
      (setq mm 16)
      (inputExcel)))

  (if (= (length #stnn) 1)
    (progn
      (setq obj2(vlax-ename->vla-object (nth 0 #stn)))
      (caseone)
      (setq mm 17)
      (inputExcel))
    (progn
      (setq obj3(vlax-ename->vla-object (nth 0 #stnn)))
      (setq obj4(vlax-ename->vla-object (nth 1 #stnn)))
      (casetwo)
      (setq mm 17)
      (inputExcel)))

  (if (= (length #stmm) 1)
    (progn
      (setq obj2(vlax-ename->vla-object (nth 0 #stmm)))
      (caseone)
      (setq mm 18)
      (inputExcel))
    (progn
      (setq obj3(vlax-ename->vla-object (nth 0 #stmm)))
      (setq obj4(vlax-ename->vla-object (nth 1 #stmm)))
      (casetwo)
      (setq mm 18)
      (inputExcel)))
  
  (if (= (length #stll) 1)
    (progn
      (setq obj2(vlax-ename->vla-object (nth 0 #stll)))
      (caseone)
      (setq mm 19)
      (inputExcel))
    (progn
      (setq obj3(vlax-ename->vla-object (nth 0 #stll)))
      (setq obj4(vlax-ename->vla-object (nth 1 #stll)))
      (casetwo)
      (setq mm 19)
      (inputExcel)))

  (if (= (length #stkk) 1)
    (progn
      (setq obj2(vlax-ename->vla-object (nth 0 #stkk)))
      (caseone)
      (setq mm 20)
      (inputExcel))
    (progn
      (setq obj3(vlax-ename->vla-object (nth 0 #stkk)))
      (setq obj4(vlax-ename->vla-object (nth 1 #stkk)))
      (casetwo)
      (setq mm 20)
      (inputExcel)))

  (if (= (length #stjj) 1)
    (progn
      (setq obj2(vlax-ename->vla-object (nth 0 #stjj)))
      (caseone)
      (setq mm 21)
      (inputExcel))
    (progn
      (setq obj3(vlax-ename->vla-object (nth 0 #stjj)))
      (setq obj4(vlax-ename->vla-object (nth 1 #stjj)))
      (casetwo)
      (setq mm 21)
      (inputExcel)))

  (if (= (length #stii) 1)
    (progn
      (setq obj2(vlax-ename->vla-object (nth 0 #stii)))
      (caseone)
      (setq mm 22)
      (inputExcel))
    (progn
      (setq obj3(vlax-ename->vla-object (nth 0 #stii)))
      (setq obj4(vlax-ename->vla-object (nth 1 #stii)))
      (casetwo)
      (setq mm 22)
      (inputExcel)))

  (if (= (length #sthh) 1)
    (progn
      (setq obj2(vlax-ename->vla-object (nth 0 #sthh)))
      (caseone)
      (setq mm 23)
      (inputExcel))
    (progn
      (setq obj3(vlax-ename->vla-object (nth 0 #sthh)))
      (setq obj4(vlax-ename->vla-object (nth 1 #sthh)))
      (casetwo)
      (setq mm 23)
      (inputExcel)))

  (if (= (length #stgg) 1)
    (progn
      (setq obj2(vlax-ename->vla-object (nth 0 #stgg)))
      (caseone)
      (setq mm 24)
      (inputExcel))
    (progn
      (setq obj3(vlax-ename->vla-object (nth 0 #stgg)))
      (setq obj4(vlax-ename->vla-object (nth 1 #stgg)))
      (casetwo)
      (setq mm 24)
      (inputExcel)))

  (if (= (length #stff) 1)
    (progn
      (setq obj2(vlax-ename->vla-object (nth 0 #stff)))
      (caseone)
      (setq mm 25)
      (inputExcel))
    (progn
      (setq obj3(vlax-ename->vla-object (nth 0 #stff)))
      (setq obj4(vlax-ename->vla-object (nth 1 #stff)))
      (casetwo)
      (setq mm 25)
      (inputExcel)))

  (if (= (length #stee) 1)
    (progn
      (setq obj2(vlax-ename->vla-object (nth 0 #stee)))
      (caseone)
      (setq mm 26)
      (inputExcel))
    (progn
      (setq obj3(vlax-ename->vla-object (nth 0 #stee)))
      (setq obj4(vlax-ename->vla-object (nth 1 #stee)))
      (casetwo)
      (setq mm 26)
      (inputExcel)))

  (if (= (length #stdd) 1)
    (progn
      (setq obj2(vlax-ename->vla-object (nth 0 #stdd)))
      (caseone)
      (setq mm 27)
      (inputExcel))
    (progn
      (setq obj3(vlax-ename->vla-object (nth 0 #stdd)))
      (setq obj4(vlax-ename->vla-object (nth 1 #stdd)))
      (casetwo)
      (setq mm 27)
      (inputExcel)))

  (if (= (length #stcc) 1)
    (progn
      (setq obj2(vlax-ename->vla-object (nth 0 #stcc)))
      (caseone)
      (setq mm 28)
      (inputExcel))
    (progn
      (setq obj3(vlax-ename->vla-object (nth 0 #stcc)))
      (setq obj4(vlax-ename->vla-object (nth 1 #stcc)))
      (casetwo)
      (setq mm 28)
      (inputExcel)))

  (if (= (length #stbb) 1)
    (progn
      (setq obj2(vlax-ename->vla-object (nth 0 #stbb)))
      (caseone)
      (setq mm 29)
      (inputExcel))
    (progn
      (setq obj3(vlax-ename->vla-object (nth 0 #stbb)))
      (setq obj4(vlax-ename->vla-object (nth 1 #stbb)))
      (casetwo)
      (setq mm 29)
      (inputExcel)))

  (if (= (length #staa) 1)
    (progn
      (setq obj2(vlax-ename->vla-object (nth 0 #staa)))
      (caseone)
      (setq mm 30)
      (inputExcel))
    (progn
      (setq obj3(vlax-ename->vla-object (nth 0 #staa)))
      (setq obj4(vlax-ename->vla-object (nth 1 #staa)))
      (casetwo)
      (setq mm 30)
      (inputExcel)))

  )

;Sub Function_intersect_caseone----------
(defun caseone()

  (setq blist(list ))
  (setq ni 0 m 0)
  (repeat wllistn
    (setq wl(nth ni wllist))
    (setq obj1(vlax-ename->vla-object wl))
    (setq interp(vlax-invoke obj1 'intersectwith obj2 0))
    (setq selectx(car interp))
    (if (/= selectx nil)
      (progn
	(setq selectx(abs selectx))
	(setq blist(append blist(list selectx))))
      (setq blist(append blist(list m))))
    (setq ni(+ ni 1)))
  
  (if (= (last blist) 0)
    (setq blist(subst halfB '0 blist)))

  )

;Sub Function_intersect_casetwo-----------
(defun casetwo()

  (setq clist(list ) dlist(list ) blist(list ))
  
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

  (setq blist (mapcar '(lambda (x y) (+ x y)) clist dlist))

  )

;Sub Function_LoadExcel---------------------------
(defun LoadExcel ()

  (if
    (and
      (setq excelPath
	     (vl-registry-read
	       "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\App Paths\\Excel.exe"
	       "Path"))
      (setq excelPath (strcat excelPath "Excel.exe")))
    (progn
      (if (not msxl-acos)
	(vlax-import-type-library
	  :tlb-filename excelPath
	  :methods-prefix "msxl-"
	  :properties-prefix "msxl-"
	  :constants-prefix "msxl-"))
      (setq ExcelApp (vlax-get-or-create-object "Excel.Application"))))
  
  ExcelApp
  
  )

;Sub Function_offsetNB------------------
(defun offsetNB()

  (setq ExcelApp (LoadExcel))
  (vlax-put Excelapp "visible" :vlax-false)
  (setq Workbooks (vlax-get-property ExcelApp 'Workbooks))
  (setq CurrentWBook (vlax-invoke-method Workbooks 'Add))
  (setq Sheets (vlax-get-property ExcelApp 'Sheets))
  (setq AcSheet (vlax-get-property ExcelApp 'ActiveSheet))
  (setq Cells (vlax-get-property AcSheet 'Cells))
  

  ;offset form---
  (setq Ran (vlax-get-property Excelapp 'Range "B2:Z100"))
  (vlax-put-property Ran 'Numberformat "0.000")


  ;WL Number-----
  (setq colY 1 rowX 3)
  (setq val "BOTTOM")
  (vlax-put-property Cells 'Item colY rowX val)

  (setq colY 1 rowX 4)
  (setq val "0.5 WL")
  (vlax-put-property Cells 'Item colY rowX val)
  
  (setq colY 1 rowX 5)
  (setq wlnumlist(mapcar '(lambda(x)(strcat (itoa x) " W.L"))wlnumlist))
  (mapcar
    '(lambda (val)
       (vlax-put-property Cells 'Item colY rowX val)
       (setq rowX(1+ rowX)))wlnumlist)

  (setq wx 3)
  (repeat wllistn
    (setq colY 1 rowX wx)
    (setq cel(vlax-variant-value(vlax-get-property Cells 'Item colY rowX)))
    (setq int(vlax-get-property cel 'Interior))
    (setq Font(vlax-get-property cel 'Font))
    (setq borders(vlax-get-property cel 'Borders))
    (setq bordersB(vlax-get-property borders 'Item 9))
    (setq bordersR(vlax-get-property borders 'Item 10))
    (vlax-put-property cel 'HorizontalAlignment -4108)
    (vlax-put-property int 'Color 14599344)
    (vlax-put-property Font 'Bold "true")
    (vlax-put-property bordersB 'Weight 4)
    (vlax-put-property bordersB 'LineStyle 1)
    (vlax-put-property bordersR 'Weight 2)
    (vlax-put-property bordersR 'LineStyle 1)
    (setq wx(+ wx 1)))
  

  ;ST Number-----
  (setq colY 1 rowX 1)
  (setq backlist (list "NO. Station" "T2" "T1" "A.P." "S.T 0.5" "S.T 1" "S.T 1.5"))
  (mapcar
    '(lambda(val)
       (vlax-put-property Cells 'Item colY rowX val)
       (setq colY (1+ colY)))backlist)
  
  (setq colY 8 rowX 1)
  (setq stnumlist(list 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18))
  (setq stnumlist(mapcar '(lambda(x)(strcat "S.T " (itoa x) ))stnumlist))
  (mapcar
    '(lambda (val)
       (vlax-put-property Cells 'Item colY rowX val)
       (setq colY (1+ colY)))stnumlist)

  (setq colY 25 rowX 1)
  (setq frontlist (list "S.T 18.5" "S.T 19" "S.T 19.5" "F.P." "F1" "F2"))
  (mapcar
    '(lambda(val)
       (vlax-put-property Cells 'Item colY rowX val)
       (setq colY (1+ colY)))frontlist)

  (setq Ran(vlax-get-property Excelapp 'Range "A1:B1"))
  (setq Font(vlax-get-property Ran 'Font))
  (setq borders(vlax-get-property Ran 'Borders))
  (setq bordersB(vlax-get-property borders 'Item 9))
  (setq bordersR(vlax-get-property borders 'Item 10))
  (vlax-put-property Ran 'MergeCells "true")
  (vlax-put-property Ran 'HorizontalAlignment -4108)
  (vlax-put-property Font 'Bold "true")
  (vlax-put-property bordersB 'Weight 4)
  (vlax-put-property bordersR 'Weight 4)
  (vlax-put-property bordersB 'LineStyle 1)
  (vlax-put-property bordersR 'LineStyle 1)
  
  (setq Ran(vlax-get-property Excelapp 'Range "A2:A30"))
  (setq int(vlax-get-property Ran 'Interior))
  (setq Font(vlax-get-property Ran 'Font))
  (vlax-put-property int 'Color 14599344) 
  (vlax-put-property Font 'Bold "true")
  (vlax-put-property Ran 'HorizontalAlignment -4108)

  (setq Ran(vlax-get-property Excelapp 'Range "A2:B30"))
  (setq borders(vlax-get-property Ran 'Borders))
  (setq bordersR(vlax-get-property borders 'Item 10))
  (setq bordersV(vlax-get-property borders 'Item 11))
  (setq bordersH(vlax-get-property borders 'Item 12))
  (vlax-put-property bordersR 'Weight 4)
  (vlax-put-property bordersV 'Weight 2)
  (vlax-put-property bordersH 'Weight 2)
  (vlax-put-property bordersR 'LineStyle 1)
  (vlax-put-property bordersV 'LineStyle 1)
  (vlax-put-property bordersH 'LineStyle 1)

  )

;Sub Function_offsetUB--------------------------
(defun offsetUB()

  (setq ExcelApp (LoadExcel))
  (vlax-put Excelapp "visible" :vlax-false)
  (setq Workbooks (vlax-get-property ExcelApp 'Workbooks))
  (setq CurrentWBook (vlax-invoke-method Workbooks 'Add))
  (setq Sheets (vlax-get-property ExcelApp 'Sheets))
  (setq AcSheet (vlax-get-property ExcelApp 'ActiveSheet))
  (setq Cells (vlax-get-property AcSheet 'Cells))
  

  ;offset form---------------------
  (setq Ran (vlax-get-property Excelapp 'Range "B2:Z100"))
  (vlax-put-property Ran 'Numberformat "0.000")


  ;;WL Number----------
  (setq colY 1 rowX 3)
  (setq val "BOTTOM")
  (vlax-put-property Cells 'Item colY rowX val)

  (setq colY 1 rowX 4)
  (setq val "0.5 WL")
  (vlax-put-property Cells 'Item colY rowX val)
  
  (setq colY 1 rowX 5)
  (mapcar
    '(lambda (val)
       (vlax-put-property Cells 'Item colY rowX val)
       (setq rowX(1+ rowX)))wlnumlist)

  (setq wx 3)
  (repeat wllistn
    (setq colY 1 rowX wx)
    (setq cel(vlax-variant-value(vlax-get-property Cells 'Item colY rowX)))
    (setq int(vlax-get-property cel 'Interior))
    (setq Font(vlax-get-property cel 'Font))
    (setq borders(vlax-get-property cel 'Borders))
    (setq bordersB(vlax-get-property borders 'Item 9))
    (setq bordersR(vlax-get-property borders 'Item 10))
    (vlax-put-property cel 'HorizontalAlignment -4108)
    (vlax-put-property int 'Color 14599344)
    (vlax-put-property Font 'Bold "true")
    (vlax-put-property bordersB 'Weight 4)
    (vlax-put-property bordersB 'LineStyle 1)
    (vlax-put-property bordersR 'Weight 2)
    (vlax-put-property bordersR 'LineStyle 1)
    (setq wx(+ wx 1)))

  ;;ST Number----------
  (setq colY 1 rowX 1)
  (mapcar
    '(lambda(val)
       (vlax-put-property Cells 'Item colY rowX val)
       (setq colY (1+ colY)))backlist)
  
  (setq colY 8 rowX 1)
  (mapcar
    '(lambda (val)
       (vlax-put-property Cells 'Item colY rowX val)
       (setq colY (1+ colY)))stnumlist)

  (setq colY 25 rowX 1)
  (mapcar
    '(lambda(val)
       (vlax-put-property Cells 'Item colY rowX val)
       (setq colY (1+ colY)))frontlist)

  
  (setq Ran(vlax-get-property Excelapp 'Range "A1:B1"))
  (setq Font(vlax-get-property Ran 'Font))
  (setq borders(vlax-get-property Ran 'Borders))
  (setq bordersB(vlax-get-property borders 'Item 9))
  (setq bordersR(vlax-get-property borders 'Item 10))
  (vlax-put-property Ran 'MergeCells "true")
  (vlax-put-property Ran 'HorizontalAlignment -4108)
  (vlax-put-property Font 'Bold "true")
  (vlax-put-property bordersB 'Weight 4)
  (vlax-put-property bordersR 'Weight 4)
  (vlax-put-property bordersB 'LineStyle 1)
  (vlax-put-property bordersR 'LineStyle 1)
  
  (setq Ran(vlax-get-property Excelapp 'Range "A2:A30"))
  (setq int(vlax-get-property Ran 'Interior))
  (setq Font(vlax-get-property Ran 'Font))
  (vlax-put-property int 'Color 14599344) 
  (vlax-put-property Font 'Bold "true")
  (vlax-put-property Ran 'HorizontalAlignment -4108)

  (setq Ran(vlax-get-property Excelapp 'Range "A2:B30"))
  (setq borders(vlax-get-property Ran 'Borders))
  (setq bordersR(vlax-get-property borders 'Item 10))
  (setq bordersV(vlax-get-property borders 'Item 11))
  (setq bordersH(vlax-get-property borders 'Item 12))
  (vlax-put-property bordersR 'Weight 4)
  (vlax-put-property bordersV 'Weight 2)
  (vlax-put-property bordersH 'Weight 2)
  (vlax-put-property bordersR 'LineStyle 1)
  (vlax-put-property bordersV 'LineStyle 1)
  (vlax-put-property bordersH 'LineStyle 1)

  )

;Sub Function_InputExcel---------------------------
(defun InputExcel()

  (setq xlist blist)
  (setq colY mm rowX 3)
  (mapcar
    '(lambda(val)
       (vlax-put-property Cells 'Item colY rowX val)
       (setq rowX (1+ rowX)))xlist)

  )

;Sub Function_Xposition-------------------------------    
(defun Xposition()

  (setq colY 2 rowX 2)
  (setq val (- 0 (* 2 stern)))
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

  )

;End Function------------------------------------------------
(defun setST()
  
  (separateST)
  (setAST)
  (setFST)
	
  )