(defun Xposition()
;서브함수 Xposition 선언,
;서브함수 STapart를 통해 입력받은 station간격들을 이용해 station별 실제 x좌표를 엑셀에 입력하는 서브함수
;선박의 각 부분별 station개수를 고려하여 위치를 계산해 엑셀에 입력해준다.  

  (setq colY 2 rowX 2)
  (setq val (- 0 (* 2 stern)))
  ;station transom의 x값이므로 stern부분 간격에 2배하여 0에서 빼줌
  ;이하 동일
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

  );Xposition함수 종료
