(defun c:ARPAGO (/ oldsnap)
; 명령어가 ARPAGO인 함수 정의,지역변수 oldsnap
  
  (setq oldsnap(getvar "osmode"))
  ;현재 오스냅모드를 oldsnap에 저장
  
  (setvar "osmode" 0)
  ;설정되어잇던 오스냅모드를 모두 끔

  (vl-load-com)
  ;비주얼 리습을 사용하는 구문이므로 비주얼 리습 확장자를 불러줌

  (initget "N U")
  ;get* 명령들이 받아오는 조건의 힘력을 방지 " " 안에 있는 값만 받음

  (setq mode(getkword "Choodse Mode [ New Body(N) // Update Body(U) ] : "))(terpri)
  ;getkword : initget에 의해 지정된 단일문자만 받음, 사용자가 입력한 문자를 mode에 저장
  ;terpri를 사용해주면 명령창 한 줄에 이 구문만 표시됨

  (if (= mode nil)(setq mode "N"))
  ;mode가 nil값이면 N 으로 설정함

  (if (= mode "N")
    ;mode의 값에 따른 조건문,조건 :  mode = N
    
    (modeNB)
    ;조건이 참일경우 modeNB라는 서브함수를 수행함
    ;새로운 선형일때 수행 할 함수
    
    (modeUB))
    ;조건이 거짓일경우 modeUB라는 서브함수를 수행함
    ;기존 선형을 수정했을 때 수행 할 함수
  
  (alert "Check Excel ! ")
  ;"Check Excel !" 이라는 내용의 알림창을 띄움, 확인버튼밖에 없음

  (setvar "osmode" oldsnap)
  ;오스냅 모드를 oldsnap에 저장해놓은 초기상태로 설정함

  (princ)
  ;보통 구문의 마지막에 사용해주며 진행상황을 숨김, 미작성시 명령창에 nil이 표시됨

  )
;ARPAGO 함수 종료