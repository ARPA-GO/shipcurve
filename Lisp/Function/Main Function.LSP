(defun c:ARPAGO (/ oldsnap)
; ���ɾ ARPAGO�� �Լ� ����,�������� oldsnap
  
  (setq oldsnap(getvar "osmode"))
  ;���� ��������带 oldsnap�� ����
  
  (setvar "osmode" 0)
  ;�����Ǿ��մ� ��������带 ��� ��

  (vl-load-com)
  ;���־� ������ ����ϴ� �����̹Ƿ� ���־� ���� Ȯ���ڸ� �ҷ���

  (initget "N U")
  ;get* ���ɵ��� �޾ƿ��� ������ ������ ���� " " �ȿ� �ִ� ���� ����

  (setq mode(getkword "Choodse Mode [ New Body(N) // Update Body(U) ] : "))(terpri)
  ;getkword : initget�� ���� ������ ���Ϲ��ڸ� ����, ����ڰ� �Է��� ���ڸ� mode�� ����
  ;terpri�� ������ָ� ����â �� �ٿ� �� ������ ǥ�õ�

  (if (= mode nil)(setq mode "N"))
  ;mode�� nil���̸� N ���� ������

  (if (= mode "N")
    ;mode�� ���� ���� ���ǹ�,���� :  mode = N
    
    (modeNB)
    ;������ ���ϰ�� modeNB��� �����Լ��� ������
    ;���ο� �����϶� ���� �� �Լ�
    
    (modeUB))
    ;������ �����ϰ�� modeUB��� �����Լ��� ������
    ;���� ������ �������� �� ���� �� �Լ�
  
  (alert "Check Excel ! ")
  ;"Check Excel !" �̶�� ������ �˸�â�� ���, Ȯ�ι�ư�ۿ� ����

  (setvar "osmode" oldsnap)
  ;������ ��带 oldsnap�� �����س��� �ʱ���·� ������

  (princ)
  ;���� ������ �������� ������ָ� �����Ȳ�� ����, ���ۼ��� ����â�� nil�� ǥ�õ�

  )
;ARPAGO �Լ� ����