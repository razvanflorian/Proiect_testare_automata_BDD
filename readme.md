#  Descriere proiect
Acest proiect reprezinta testarea automata a unui site pentru a verifica si rula diferite functionalitati ale acestuiua precum, logare user, eliminare produs din cos, navigare din pagina in pagina, realizarea unui review a unui produs.
Am folosit metodologia BDD(principalele fisere fiind feautures, pages si steps)
Ca si IDE am folosit pycharm si Selenium
In urma rapoartelor, toate testele au trecut

Din punct de vedere structural am folosit BDD

3 tipuri principale de fisiere Directory:

 - features - aici sunt cuprinse toate scenariile cum ar fi:add_to_cart.feature, register.feature, make_a_review.feature, search.feauture sau login.feature, unde am folosit mai multe scenarii, inclusiv Scenario Outline

 - pages - aici am definit , in mare parte, elementele interfetei paginii web(print folosirea selectorilor de diferite tipuri:simpli, selectorii CSS, selectori xpath relativ) si metodele de interactiune cu elementele respective pentru fiecare scenariu realizat
 - steps - In baza acestor fisiere am realizat implementare pasilor de testare, inclusiv organizare si strucurarea pasilor pentru fiecare test.

 Am importat din libraria behave structuri cheie cum ar fi ("given", "then", "and", "when") pentru o definire mai clara a pasilor de testare in cadrul scenariilor scrise in limbajul Gherkin

Am creat fisiere python adiacente precum browser si environment:

 - browser - am folosit metodologia OOP, utilizand o clasa pentru a avea acces facil la interctiunea cu browser-ul in care am realizat testele
 - environment - acest fisier de mediu l-am  folosit   pentru a gestiona  setările de mediu și pentru a stabili contextul necesar pentru testele create. Termenul "context" este  folosit pentru a face referire la starea inițială sau condițiile în care se desfășoară un anumit scenariu din cadrul proiectului. Se poate observa in fisierele de tip steps.


Intr-o ultima perspectiva, acest proiect evidentiaza functionalitatea unor procese principale din cadrul aplicatiei Magento oferind ca si concluzie o buna utilizare si interactiune cu elementele  acesteia.