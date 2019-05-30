(defun separateST()
;서브함수 separateST선언, station을 선미부, 선수부로 나누어 기억시킴
  
  (setq Astlist(list ) Fstlist(list ) Alaylist(list ) Flaylist(list ))
  ;앞의 setWL함수와 마찬가지로 리스트 비워주고 구문 시작
  ;Astlist:선미부station                Fstlist:선수부station
  ;Alaylist:선미부station의레이어이름   Flaylsit:선수부station의레이어이름
  
  (setq num 0)
  ;변수 num에 0을 저장
  
  (repeat (sslength wlspl)
  ;wlspl 세트 리스트 길이만큼 반복해라
    
    (setq name(ssname wlspl num))
    ;wlspl 세트 리스트의 num번째 요소의 도면이름을 변수 name에 저장
    
    (setq layname(cdr (assoc 8 (entget name))))
    ;레이어 이름을 layname변수에 저장
    
    (setq objname(vlax-ename->vla-object name))
    ;도면 이름을 객체로 바꾸어 objname 변수로 저장
    
    (if (= "SPLINE" (cdr(assoc 0 (entget name))))
    ;조건 : 요소의 종류 = SPLINE
      
      (progn
      ;조건문 내에 실행문이 여래개일경우 한개로 묶어준다. 요소종류가 spline일경우(조건이 참인경우) 실행문 시작

	(setq jpoint(car(vlax-curve-getpointatparam objname 0.5)))
	;곡선의 중간점의 좌표중 x좌표를 jpoint변수에 저장
	
	(if (< jpoint 0)
	;조건 : jpoint(중간점의 x좌표) < 0
	  
	  (progn
	  ;jpoint조건문 참인경우 실행문 시작
	    (setq Astlist(append Astlist(list name)))
	    ;요소의 도면 이름을 Astlist 리스트에 저장
	    
	    (if (= (member layname Alaylist) nil)
	    ;조건 : Alaylist 리스트에 layname(요소의 레이어 이름)이 있지않을경우
	      
	      (setq Alaylist(append Alaylist(list layname)))
	      ;조건이 참일경우 Alaylist에 layname을 추가한다.
	      
	      );Alaylist 조건문 종료
	    
	    );jpoint조건문 참일경우 실행문 묶은 progn 종료
	  
	  (progn
	  ;jpoint조건문 거짓일 경우 실행문 시작
	    
	    (setq Fstlist(append Fstlist(list name)))
	    ;요소의 도면 이름을 Fstlist 리스트에 저장
	    
	    (if (= (member layname Flaylist) nil)
	    ;조건 : Flaylist 리스트에 layname(요소의 레이어 이름)이 있지 않을경우
	      
	      (setq Flaylist(append Flaylist(list layname)))
	      ;조건이 참일경우 Flaylist에 layname을 추가한다.

	      );Flaylist 조건문 종료

	    );jpoint조건문 거짓일 경우 실행문 묶은 progn 종료

	  );jpoint조건문 종료

	);요소 종류가 spline일경우 실행문 묶은 progn 종료
      
      (progn
      ;요소 종류 조건문이 거짓일 경우 실행문 시작
	
	(if (= "ARC" (cdr(assoc 0 (entget name))))
	;조건 : 요소 종류 = ARC
	  
	  (progn
	  ;요소종류=ARC 인 경우 (조건이 참인경우) 실행문 시작
	    
	    (setq jpoint(car(vlax-curve-getstartpoint objname)))
	    ;요소의 시작점의 x좌표를 jpoint에 저장
	    
	    (if (< jpoint 0)
	    ;이하는 spline인 경우와 마찬가지로 Astlist, Fstlist판별
	      
	      (progn
		(setq Astlist(append Astlist(list name)))
		(if (= (member layname Astlist) nil)
		  (setq Alaylist(append Alaylist(list layname)))))
	      
	      );jpoint 조건문 종료

	    );요소 종류 ARC 참일경우 실행문 묶은 progn종료

	  );요소종류 ARC 조건문 종료

	);요소종류 spline 조건문 거짓일 경우 실행문 묶은 progn 종료

      );요소종류 spline 조건문 종료
      
    (setq num(+ num 1))
    ;변수 num을 num+1로 저장

    );repeat문 종료
  
  (setq Alaylist(vl-sort Alaylist '<))
  ;Alyalist 리스트(레이어 이름 리스트)를 오름차순으로 정렬하라
  
  (setq Alaylistn(length Alaylist))
  ;Alaylsit의 길이를 변수 Alaylistn에 저장
  
  (setq Alastlist(append Alastlist (list (nth (- Alaylistn 1) Alaylist)
					 (nth (- Alaylistn 2) Alaylist)
					 (nth (- Alaylistn 3) Alaylist))))
  ;Alaylist 리스트의 (Alaylistn-1), (Alaylistn-2), (Alaylistn-3)번째 요소들을 Alastlist에 추가
  
  (setq Alaylist(vl-remove (nth 0 Alastlist) Alaylist))
  (setq Alaylist(vl-remove (nth 1 Alastlist) Alaylist))
  (setq Alaylist(vl-remove (nth 2 Alastlist) Alaylist))
  ;Alaylsit의 0,1,2 번째 요소를 Alaylist에서 지움
  
  (setq Alaylist(append Alastlist Alaylist))
  ;Alaylist를 Alastlist에 추가하고 그것을 Alaylist변수에 저장

  (setq Flaylist(vl-sort Flaylist '>))
  ;Flaylist 리스트를 내림차순으로 정렬하라
  
  (setq Flaylistn(length Flaylist))
  ;Flaylist 리스트의 길이를 Flaylistn 변수에 저장

  )