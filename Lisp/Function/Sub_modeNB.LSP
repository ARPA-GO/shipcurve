(defun modeNB (/ wlspl num ni m objname jpoint Astlist Fstlist Alaylist Flaylist Alaylistn Alastlist Flastlist sta stb stc std ste stf stg sth sti stj stk stl stm stn sto stnn stmm stll stkk stjj stii sthh stgg stff stee stdd stcc stbb staa mm interp interpc interpd selectx selectxc selectxd blist clist dlist xlist obj1 obj2 obj3 obj4 excelPath ExcelApp workbooks currentwbook sheets acsheet cells borders font interior bordersB bordersH bordersV bordersR ran val )
;�����Լ� modeNB ����,modeNB�� ���ο� �����϶� ������ ����, �������� ����

  (setq halfB(getreal "Breadth/2 : "))(terpri)
  ;getreal : ����ڷκ��� �Ǽ����� �Է¹޴� �Է��Լ�," " ���� ������ ����â�� ǥ�õ�, ���� ������ �Է¹���
  ;�Է¹��� ���� ������ halfB��� ������ ����

  (STapart)
  ;�����Լ� STapart����, ��ü�� �κк� station������ �Է¹���

  (setq wlspl(ssget '((0 . "LINE,SPLINE,ARC"))))
  ;ssget : ���� ��ü�� ���� �� ���� ���� ��Ʈ���� ����Ʈ ���·� �޾ƿ�
  ;'((0 . "LINE,SPLINE,ARC")))) : ����ڰ� ������ ��ü�� LINE,SPLINE,ARC �� �ڵ����� �Ǻ��ؼ� �޵�����
  ;���� ��ü���� wlspl�������� ����

  (setWL)
  ;�����Լ� setWL ����, ������ ��ü���� waterline�� �����س�

  (setST)
  ;�����Լ� setST ����, ������ ��ü���� Station�� �����س�

  (offsetNB)
  ;�����Լ� offsetNB ����, ������ ��Ÿ�� offsetǥ�� ���� ����

  (Xposition)
  ;�����Լ� Xposition ����, ���� �������� �Է¹��� station���ݵ��� �̿��� station�� ���� x��ǥ�� ������ �Է���

  (intersect)
  ;�����Լ� intersect ����, waterline�� station�� �������� ã�� ������ �Է���

  )
;modeNB �Լ� ����