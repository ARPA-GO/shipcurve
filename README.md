# shipcurve
These are to calculate the ship's hydrostatic curves.

## Overview

There are already many commercial shipping programs such as Foran, Aveva Marine.  
But students and Start-up Company find it difficult to use these programs because of their high prices.  
And also we cannot easily use the program before it is educated.  
To solve this problem, we developed a library.  
**ARPA-GO** is python based ship calculation open source library.   
Ship calculations are divided into various fields.   
Among them, **hydrostatic curve** which is based on all ship calculations was prioritized and also provided ship calculation sheet for additional calculation.

## Getting Start
**Please refer to the manual for details.**  
### Prerequisites  
  Recommend installing anaconda and other necessary libraries.    
### Installing  
1. python  
  User wants to use python, should use editing programs such as jupyter notebook or pycharm.
2. .exe file  
  User wants to use an exe file in the form of a program, can download it from the url below.
  https://drive.google.com/open?id=1QNXKc0-pwct7xsZWkVGubp9pcGPgKCwM  
  Go to this public drive site to download files which are not uploaded in the repository due to large file storage. 
  > It may take a long time. Please understand.
  
## Run Program  
**Please refer to the manual for details.**  
>Let me explain by assuming that you use .exe file  
* User having offset table 
  1. Click ***Input File*** and select offset table
  2. Write ***waterline NO. , Length Between Perpendiculars and Breath***
  3. According to the user's purpose, click ***Calculation Sheet*** or ***Hydrostatic Curve***
  
* User not having offset table
  1. Use ***Lisp*** to create offset table
  > Refer to manual page.(이 부분에 리습 설명서 쪽수 적으면 좋을듯)
  2. As above, Click ***Input File*** and select offset table
  3. Write ***waterline NO. , Length Between Perpendiculars and Breath***
  4. According to the user's purpose, click ***Calculation Sheet*** or ***Hydrostatic Curve***
  
## Participant
* solmi LEE    (Bachelor of Science in Naval Architecture and Ocean Engineering)  
* jungmin KANG (Bachelor of Science in Naval Architecture and Ocean Engineering)  
* eunji KIM    (Bachelor of Science in Naval Architecture and Ocean Engineering)  
* hyunji KIM   (Bachelor of Science in Naval Architecture and Ocean Engineering)  
* huijeong YU  (Bachelor of Science in Naval Architecture and Ocean Engineering)  

## Acknowledgments
Thank you for mentor (sangggho)
