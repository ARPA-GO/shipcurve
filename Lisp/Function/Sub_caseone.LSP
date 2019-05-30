(defun caseone()
;서브함수 caseone 선언
;station이 도면상 객체 1개로 그려졌을 경우, waterline과 station의 교차점 찾는 서브함수
  
  (setq blist(list ))
  ;blist를 비워주고 구문 시작
  ;blist는 waterline별 station의 교차점중 x좌표 리스트
  
  (setq ni 0 m 0)
  
  (repeat wllistn
  ;wllistn(waterline개수) 만큼 만복해라
    
    (setq wl(nth ni wllist))
    ;wllist(waterline들의 도면이름 리스트)리스트의 ni번째를 변수 wl로 저장
    
    (setq obj1(vlax-ename->vla-object wl))
    ;도면이름인 wl을 객체로 바꾸어 변수 obj1로 저장
    
    (setq interp(vlax-invoke obj1 'intersectwith obj2 0))
    ;obj1(waterline) 과 obj2(station)의 교차점을 변수 interp에 저장
    ;vlax-invoke 객체1 'intersectwith 객체2 0 :객체1과 객체 2의 교차점을 찾는 함수
    ;0이 아니라 1이면, 두 객체가 교차하지 않으면 연장하여 가상의 교차점을 찾으라는 뜻
    
    (setq selectx(car interp))
    ;교차점의 첫번째 요소(x좌표)를 변수 selectx에 저장
    
    (if (/= selectx nil)
    ;조건 : 교차점이 존재
      
      (progn
      ;조건이 참일경우(교차점이 존재할경우) 실행문 시작
	
	(setq selectx(abs selectx))
	;selectx(교차점의 x좌표)에 절댓값을 씌워 저장
	
	(setq blist(append blist(list selectx)))
	;blist에 selectx를 추가

	);조건이 참일경우 실행문 묶은 progn 종료
	
      (setq blist(append blist(list m)))
      ;조건이 거짓일 경우(교차점이 존재하지 않을경우) blist에 m(0)을 추가

      );교차점 존재여부 조건문 종료
    
    (setq ni(+ ni 1))
    ;ni를 ni+1 값으로 저장

    );repeat문 종료
  
  (if (= (last blist) 0)
  ;조건 : blist의 마지막 요소가 0인 경우
  ;대표적으로 Station No.10 같은 경우 선형상 waterline과의 교차점이 얼마 없다.
  ;즉, 해당 waterline에서 선박의 반폭 길이와 같은 값을 가진다는 뜻이므로 이 조건문을 작성하였다.
    
    (setq blist(subst halfB '0 blist))
    ;blist에 존재하는 0을 halB(초반에 사용자에게 입력받은 반폭)로 대체하라

    );조건문 종료

  );caseone함수 종료