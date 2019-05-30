(defun intersect()
;서브함수 intersect 선언
;waterline의 station별 교차점을 찾아 엑셀로 좌표를 추출하는 함수

  (if (= (length #sta) 1)
  ;조건 : #sta(station transom을 이루는 객체들의 도면이름 리스트)의 길이 = 1
    
    (progn
    ;조건이 참일경우 실행문 시작(station transom이 도면상에 한개의 객체로 그려졌을경우)
      
      (setq obj2(vlax-ename->vla-object (nth 0 #sta)))
      ;#sta의 0번째 요소(도면이름)를 객체로 바꾸어 obj2변수에 저장
      
      (caseone)
      ;서브함수 caseone 실행, (1개의 객체로 이루어졌을경우 교차점 찾는 서브함수)
      
      (setq mm 2)
      
      (inputExcel)
      ;서브함수 inputExcel 실행, (교차점의 좌표값을 엑셀로 보내는 서브함수)

      );조건이 참일경우 실행문 묶은 progn 종료
    
    (progn
    ;조건이 거짓일 경우 실행문 시작,(station transom이 도면상에 두개의 객체로 그려졌을 경우)
      
      (setq obj3(vlax-ename->vla-object (nth 0 #sta)))
      ;#sta의 0번째 요소(도면이름)를 객체로 바꾸어 obj3변수에 저장
      
      (setq obj4(vlax-ename->vla-object (nth 1 #sta)))
      ;#sta의 1번째 요소(도면이름)를 객체로 바꾸어 obj4변수에 저장
      
      (casetwo)
      ;서브함수 casetwo 실행,(2개의 객체로 이루어졌을경우 교차점 찾는 서브함수)
      
      (setq mm 2)
      
      (inputExcel)
      ;서브함수 inputExcel 실행

      );조건이 거짓일 경우 실행문 묶은 progn 종료

    );#sta(station transom) 조건문 종료

;이하 동일
  
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

  );intersect 함수 종료
