(defun modeNB (/ wlspl num ni m objname jpoint Astlist Fstlist Alaylist Flaylist Alaylistn Alastlist Flastlist sta stb stc std ste stf stg sth sti stj stk stl stm stn sto stnn stmm stll stkk stjj stii sthh stgg stff stee stdd stcc stbb staa mm interp interpc interpd selectx selectxc selectxd blist clist dlist xlist obj1 obj2 obj3 obj4 excelPath ExcelApp workbooks currentwbook sheets acsheet cells borders font interior bordersB bordersH bordersV bordersR ran val )
;서브함수 modeNB 선언,modeNB는 새로운 선형일때 수행할 구문, 지역변수 선언

  (setq halfB(getreal "Breadth/2 : "))(terpri)
  ;getreal : 사용자로부터 실수값을 입력받는 입력함수," " 안의 내용이 명령창에 표시됨, 배의 반폭을 입력받음
  ;입력받은 배의 반폭을 halfB라는 변수에 저장

  (STapart)
  ;서브함수 STapart실행, 선체의 부분별 station간격을 입력받음

  (setq wlspl(ssget '((0 . "LINE,SPLINE,ARC"))))
  ;ssget : 여러 객체를 받을 수 있음 선택 세트들을 리스트 형태로 받아옴
  ;'((0 . "LINE,SPLINE,ARC")))) : 사용자가 선택한 객체중 LINE,SPLINE,ARC 만 자동으로 판별해서 받도록함
  ;받은 객체들을 wlspl변수에에 저장

  (setWL)
  ;서브함수 setWL 실행, 선택한 객체들중 waterline만 구분해냄

  (setST)
  ;서브함수 setST 실행, 선택한 객체들중 Station만 구분해냄

  (offsetNB)
  ;서브함수 offsetNB 실행, 엑셀로 나타낼 offset표의 형식 지정

  (Xposition)
  ;서브함수 Xposition 실행, 앞의 구문에서 입력받은 station간격들을 이용해 station별 실제 x좌표를 엑셀에 입력함

  (intersect)
  ;서브함수 intersect 실행, waterline과 station의 교차점을 찾아 엑셀에 입력함

  )
;modeNB 함수 종료