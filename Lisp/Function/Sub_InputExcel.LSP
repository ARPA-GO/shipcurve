(defun InputExcel()
;서브함수 InputExcel 선언,
;교차점을 구하는 intersect함수에서 구한 값을 엑셀로 보내는 서브함수
  
  (setq xlist blist)
  ;intersect함수를 통해 구한 x좌표 리스트인 blist를 xlist로 저장
  
  (setq colY mm rowX 3)
  ;행의 값을 변수로 두어 station에 따라 지정 셀에 값을 삽입
  
  (mapcar
    '(lambda(val)
       (vlax-put-property Cells 'Item colY rowX val)
       (setq rowX (1+ rowX)))xlist)

  );InputExcel 함수 종료