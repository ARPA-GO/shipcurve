(defun STapart()
;서브함수 STapart 선언, 선체의 각 부분별 station간격을 받는 구문

  (setq stern(getreal "Stern Station Apart : "))(terpri)
  ;사용자로부터 입력받은 선미부의 station간격을 stern변수에 저장

  (setq square(getreal "Square Station Apart : "))(terpri)
  ;사용자로부터 입력받은 주요부의 station간격을 square변수에 저장

  (setq Bow(getreal "Bow Station Apart : "))(terpri)
  ;사용자로부터 입력받은 선수부의 station간격을 Bow변수에 저장

  )
;STapart함수 종료