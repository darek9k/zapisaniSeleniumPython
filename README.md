# Testy z zadań ze strony zapisani

Pierwotnie w Cypress, ale dla treningu proszę oto te same testy w Selenium z użyciem Pythona

Smoczek lubi snake_case to duża zmiana dla osoby, która ciśnie Javę od prawie roku :)
Brak miliona nawiasów za to trzeba utrzymywać odpowiednie odstępy od bloków kodu.

Opcje wyciągania count'a z response już odpuściłem - generalizując usłyszałem głos -> YOU AIN’T GONA NEED IT :)

Enjoy!

Utwórz test Cypress, który:

wejdzie na stronę https://testy-zadanie.zapisani.dev/
wypełni poprawnie formularz
zweryfikuje, że po wybraniu "Produkt ze skończoną pulą" po kliknięciu "Uzyskaj dostęp przedpremierowy" - zostanie wyświetlone okienko wyskakujące z komunikatem błędu mówiącym o braku dostępności produktu
Utwórz test Cypress, który:

wejdzie na stronę https://testy-zadanie.zapisani.dev/
wypełni poprawnie formularz
zweryfikuje, że po wybraniu "Produkt z organiczoną pulą" po kliknięciu "Uzyskaj dostęp przedpremierowy" - zostanie przekierowany na stronę płatności.
po wybraniu płatności gotówkowej przejdzie na stronę "sukcesu" z gratulacjami po poprawnym wypełnieniu formularza
sprawdzi, że po ponownym wejściu na formularz, liczba dostępnych produktów będzie o 1 miejsza od liczby produktów dostępnych pierwotnie.
