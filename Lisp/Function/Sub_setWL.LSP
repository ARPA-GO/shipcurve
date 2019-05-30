(defun setWL()
;서브함수 setWL선언, 여러 객체들중 waterline을 판별해내는 구문, 지역변수 없음

  (setq wllist(list ) wlnumlist(list ))
  ;wllist와 wlnumlist를 빈 리스트로 선언해줌
  ;한 파일 안에 여러 body를 놓고 비교하고 싶을 경우 modeNB를 여러번 사용 할 경우것이므로
  ;waterline별 도면 이름을 저장해놓은 리스트와 offset에 입력할 WL형식을 저장한 리스트를 비워줌

  (setq num 0)
  ;변수 num 은 0

  (repeat (sslength wlspl)
  ;wlspl에 저장된 세트의 개수만큼 반복해라

    (setq name(ssname wlspl num))
    ;변수 name에 wlspl리스트중 num번째 세트의 도면 이름을 저장함

    (if (and (= "LINE" (cdr(assoc 0 (entget name))))
	     ;객체가 Line이여야한다는 조건
	     ;entget은 도면이름이 name인 객체의 entity list 얻음
	     ;assoc 0 : entget을 통해 얻은 entity lsit의 0번째에 해당하는 list 받음
	     ;cdr : assoc을 통해 받은 정보의 리스트 중 첫번째 값을 제외하고 받음

	     (or (zerop (vla-get-angle (vlax-ename->vla-object name)))
		 ;vlax-ename->vla-object name : name에 설정된 도면이름을 객체로 바꾸어준다.
		 ;vla-get-angle : 객체의 각도를 구한다.
		 ;zerop : 객체의 각도가 0이여야 한다는 조건

		 (equal (vla-get-angle (vlax-ename->vla-object name)) pi 0.0001)
		 ;객체의 각도=180도 이여야 한다는 조건

		 );or 종료
	     );and 종료
      ;waterline은 도면상 수평선이므로 객체의 각도가 0 또는 180 인것이 조건이다.

      (setq wllist(append wllist (list name)))
      ;조건문이 참일경우 객체의 이름을 wllist 리스트에 추가함

      );If문 종료

    (setq num(+ num 1))
    ;변수 num을 num+1값으로 저장함

    );repeat문 종료

  (setq wllist(vl-sort wllist '(lambda (x y)(< (cadr (cdr(assoc 10 (entget x))))
					       (cadr (cdr(assoc 10 (entget y))))))))
  ;wllist 리스트를 리스트 요소인 라인의 시작점 좌표로(y)오름차준 정렬하라

  (setq wllistn(length wllist))
  ;wllist 리스트의 길이를 wllistn 변수에 저장

  (setq wlnum 1)
  ;wlnum 변수에 1을 선언

  (repeat (- wllistn 2)
  ;wllistn-2 만큼 반복하라

    (setq wlnumlist(append wlnumlist(list wlnum)))
    ;wlnum을 wlnumlist 리스트에 추가한것을 wlnumlsit 라고 선언

    (setq wlnum(+ wlnum 1))
    ;변수 wlnum을 num+1값으로 저장

    );repeat문 종료

  );setWL 함수 종료