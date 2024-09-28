from openai import OpenAI
from . import api_key

CLIENT = OpenAI(api_key=api_key.get_api_key())
MODEL = "gpt-4o"

import spacy
nlp = spacy.load("pl_core_news_sm")



class TextAnalyzer:

    def __init__(self):
        self.model = MODEL

    def passive_form_verifier(self, text):

        ckeck_if_passive_voice = CLIENT.chat.completions.create(
            model = self.model,
            messages=[
                {"role": "system", "content": '''Jesteś pomocnym specjalistą języka polskiego i z łatwością określasz formy gramatyczne zastosowane w tekście. Pracujesz przy analizie tekstu, która polega wskazywaniu fragmentów, w których została używa strona bierna. Odpowiadasz szczerze, w oficjalnym i przyjaznym dla użytkownika stylu.'''},
                {"role": "user", "content": f'''Twoim zadaniem jest analiza treści otrzymanego tekstu i wykrycie, czy użyto w nich fomę bezosobową bierną. 
                                                Forma bierna rozumiana jest jako .... 
                                                Uważnie przeanalizuj poniższe przykłady. Przyswój logikę rozumowania i zwróć odpowiedź.
                                                Myśl krok po kroku.
                 
                                                <PRZYKŁAD1>
                                                %%%TEKST%%%
                                                Podczas spotkania omówiono szereg rozwiązań, w tym tych wdrażanych w innych krajach, które mogłyby przyczynić się do poprawy nadzoru nad sektorem zdrowia publicznego. Podkreślono, że zwiększenie kontroli nad wydatkowaniem środków oraz skuteczniejsza współpraca instytucji państwowych powinny być priorytetem dla całego sektora. Zwrócono również uwagę na istotny aspekt ochrony zdrowia obywateli. W trakcie dyskusji poruszono także inne bieżące kwestie związane z finansowaniem systemu ochrony zdrowia i jego efektywnością.

                                                %%%ODPOWIEDŹ%%%
                                                Tekst zawiera stronę bierną. Znajdują się w nim słoczasowniki wa takie jak "omówiono", "podkreślono", czy "zwrócono".
                                                </PRZYKŁAD1>

                                                <PRZYKŁAD2>
                                                %%%TEKST%%%
                                                Podczas spotkania ministerialnego omówiono szereg działań, które zostaną podjęte w celu poprawy funkcjonowania sektora edukacji. Zostały przedstawione plany reform, które mają na celu dostosowanie systemu nauczania do wymogów współczesnego rynku pracy. Ministrowie wskazali, że kluczowe będzie zwiększenie środków na rozwój cyfrowej infrastruktury edukacyjnej. Ministrowie wskazali, że kluczowe będzie zwiększenie środków na rozwój cyfrowej infrastruktury edukacyjnej.
                                                
                                                %%%ODPOWIEDŹ%%%
                                                Tekst częściowo zawiera stronę bierną. Znajdują się w nim słowa takie jak "omówiono", ale w ostatnim zdaniu forma czasowników jest inna, przykładem jest "zostały".
                                                </PRZYKŁAD2>

                                                <PRZYKŁAD3>
                                                %%%TEKST%%%
                                                Ministerstwo Zdrowia wprowadza nowy program profilaktyki zdrowotnej, który ma na celu poprawę jakości życia obywateli. Eksperci opracowują szczegółowe wytyczne dotyczące zdrowego stylu życia, a także rekomendacje dla placówek medycznych.
                                                
                                                %%%ODPOWIEDŹ%%%
                                                W tekście nie zastosowano strony biernej. Czasowniki takie jak "wprowadza", "opracowują" są w formie czynnej.

                                                </PRZYKŁAD3>

                                                %%%TEKST%%%                 
                                                {text}

                                                %%%ODPOWIEDŹ%%%'''}
            ]
        )

        # FUNCTION CALLING --> PYDANTIC

        answer = ckeck_if_passive_voice.choices[0].message.content
        return answer

    def important_phrases_searcher(self, text):

        check_important_phrases = CLIENT.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system",
                 "content": '''Jesteś pomocnym specjalistą języka polskiego i z łatwością określasz istotne frazy w tekście. Pracujesz przy analizie tekstu, która polega na wskazywaniu najbardziej istotnych miejsc w tekście. Odpowiadasz szczerze, w oficjalnym i przyjaznym dla użytkownika stylu.'''},
                {"role": "user", "content": f'''Twoim zadaniem jest analiza treści otrzymanego tekstu i znalezienie w nim najważniejszych cytatów. Cytatów może być kilka, ale staraj się, by nie były dłuższe niż 2-3 słowa.
                                                Myśl krok po kroku. Twoja odpowiedź powinna składać się tylko z istotnych cytatów, jeden na linię.

                                                <PRZYKŁAD1>
                                                %%%TEKST%%%
                                                Podczas spotkania omówiono szereg rozwiązań, w tym tych wdrażanych w innych krajach, które mogłyby przyczynić się do poprawy nadzoru nad sektorem zdrowia publicznego. Podkreślono, że zwiększenie kontroli nad wydatkowaniem środków oraz skuteczniejsza współpraca instytucji państwowych powinny być priorytetem dla całego sektora. Zwrócono również uwagę na istotny aspekt ochrony zdrowia obywateli. W trakcie dyskusji poruszono także inne bieżące kwestie związane z finansowaniem systemu ochrony zdrowia i jego efektywnością.

                                                %%%ODPOWIEDŹ%%%
                                                ochrony zdrowia obywateli
                                                sektorem zdrowia publicznego
                                                ochrona zdrowia obywateli
                                                </PRZYKŁAD1>

                                                <PRZYKŁAD2>
                                                %%%TEKST%%%
                                                Audytem objęliśmy 96 podmiotów, a łączna kwota badanych środków publicznych to około 100 miliardów złotych. W toku działań stwierdziliśmy m.in. niegospodarne i niecelowe wydatkowanie środków publicznych, udzielenie dotacji podmiotów, które nie spełniały kryteriów konkursowych.

                                                %%%ODPOWIEDŹ%%%
                                                96 podmiotów
                                                100 miliardów złotych
                                                </PRZYKŁAD2>

                                                <PRZYKŁAD3>
                                                %%%TEKST%%%
                                                Ministerstwo Zdrowia wprowadza nowy program profilaktyki zdrowotnej, który ma na celu poprawę jakości życia obywateli. Eksperci opracowują szczegółowe wytyczne dotyczące zdrowego stylu życia, a także rekomendacje dla placówek medycznych.

                                                %%%ODPOWIEDŹ%%%
                                                program profilaktyki zdrowotnej
                                                poprawę jakości życia

                                                </PRZYKŁAD3>

                                                %%%TEKST%%%                 
                                                {text}

                                                %%%ODPOWIEDŹ%%%'''}
            ]
        )

        # FUNCTION CALLING --> PYDANTIC

        answer = check_important_phrases.choices[0].message.content
        return answer

    def jargon_searcher(self, text):

        check_jargon = CLIENT.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system",
                 "content": '''Jesteś ekspertem językowym, który z łatwością identyfikuje słowa należące do żargonu specjalistycznego. Twoim zadaniem jest analiza tekstu w celu znalezienia i wypisania takich słów. Odpowiadasz w sposób jasny i profesjonalny.'''},
                {"role": "user", "content": f'''Twoim zadaniem jest analiza treści otrzymanego tekstu i znalezienie w nim słów należących do żargonu. Mogą to być specjalistyczne terminy techniczne, ekonomiczne, medyczne, prawnicze lub inne charakterystyczne dla danego środowiska.
                                                Odpowiedź powinna zawierać jedno słowo na linię.

                                                <PRZYKŁAD1>
                                                %%%TEKST%%%
                                                W nowym systemie CRM wdrożono mechanizmy automatyzacji procesów sprzedażowych, które integrują się z API zewnętrznych platform handlowych.

                                                %%%ODPOWIEDŹ%%%
                                                CRM
                                                automatyzacja
                                                API
                                                platform handlowych
                                                </PRZYKŁAD1>

                                                <PRZYKŁAD2>
                                                %%%TEKST%%%
                                                W związku z rosnącym zapotrzebowaniem na usługi telemedyczne, konieczne jest zwiększenie interoperacyjności systemów informatycznych oraz poprawa przepływu danych między jednostkami ochrony zdrowia.

                                                %%%ODPOWIEDŹ%%%
                                                telemedyczne
                                                interoperacyjności
                                                systemów informatycznych
                                                </PRZYKŁAD2>

                                                <PRZYKŁAD3>
                                                %%%TEKST%%%
                                                Audytorzy finansowi wskazali na potrzebę wzmocnienia kontroli nad wykorzystaniem zasobów kapitałowych w spółkach giełdowych.

                                                %%%ODPOWIEDŹ%%%
                                                Audytorzy finansowi
                                                zasobów kapitałowych
                                                spółkach giełdowych
                                                </PRZYKŁAD3>

                                                %%%TEKST%%%                 
                                                {text}

                                                %%%ODPOWIEDŹ%%%'''}
            ]
        )
        answer = check_jargon.choices[0].message.content
        return answer

    def complex_word_searcher(self, text):

        check_complex_words = CLIENT.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system",
                 "content": '''Jesteś ekspertem językowym, który analizuje tekst pod kątem prostoty języka. Twoim zadaniem jest znalezienie słów, które mogą być zbyt długie, skomplikowane lub trudne do zrozumienia dla przeciętnego odbiorcy. Twoje odpowiedzi powinny być profesjonalne i precyzyjne.'''},
                {"role": "user", "content": f'''Twoim zadaniem jest analiza treści otrzymanego tekstu i znalezienie w nim słów, które są zbyt długie lub zbyt skomplikowane dla przeciętnego odbiorcy. Wybieraj tylko te słowa, które mogą sprawić trudność, a każda odpowiedź powinna zawierać jedno słowo na linię.

                                                <PRZYKŁAD1>
                                                %%%TEKST%%%
                                                Podjęcie decyzji o implementacji innowacyjnych rozwiązań w dziedzinie infrastruktury technologicznej wymaga zaangażowania wieloletnich ekspertów oraz ścisłej współpracy z zewnętrznymi konsultantami.

                                                %%%ODPOWIEDŹ%%%
                                                implementacji
                                                innowacyjnych
                                                infrastruktury
                                                konsultantami
                                                </PRZYKŁAD1>

                                                <PRZYKŁAD2>
                                                %%%TEKST%%%
                                                Rozwój działalności gospodarczej w kontekście regulacji prawnych oraz zawiłości rynkowych stawia przed przedsiębiorcami wiele wyzwań związanych z optymalizacją strategii rozwoju.

                                                %%%ODPOWIEDŹ%%%
                                                działalności gospodarczej
                                                zawiłości
                                                optymalizacją
                                                </PRZYKŁAD2>

                                                <PRZYKŁAD3>
                                                %%%TEKST%%%
                                                Przeprowadzenie szczegółowej analizy operacyjnej wymaga zastosowania skomplikowanych narzędzi statystycznych oraz zaawansowanych technik obliczeniowych.

                                                %%%ODPOWIEDŹ%%%
                                                szczegółowej
                                                operacyjnej
                                                statystycznych
                                                zaawansowanych
                                                </PRZYKŁAD3>

                                                %%%TEKST%%%                 
                                                {text}

                                                %%%ODPOWIEDŹ%%%'''}
            ]
        )
        answer = check_complex_words.choices[0].message.content
        return answer

    def complex_sentence_searcher(self, text):

        check_complex_sentences = CLIENT.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system",
                 "content": '''Jesteś ekspertem językowym, który analizuje tekst pod kątem jego czytelności. Twoim zadaniem jest znalezienie zdań, które są zbyt długie, złożone i trudne do zrozumienia dla przeciętnego odbiorcy. Twoje odpowiedzi powinny być profesjonalne i precyzyjne.'''},
                {"role": "user", "content": f'''Twoim zadaniem jest analiza treści otrzymanego tekstu i znalezienie w nim zdań, które mogą być zbyt długie, skomplikowane lub trudne dla przeciętnego odbiorcy. Zwróć szczególną uwagę na zdania zawierające skomplikowane struktury składniowe lub nadmiarowe informacje. Odpowiedź powinna zawierać jedno zdanie na linię.

                                                <PRZYKŁAD1>
                                                %%%TEKST%%%
                                                Implementacja nowego systemu zarządzania zasobami ludzkimi, który ma na celu zautomatyzowanie procesów rekrutacyjnych, a także zwiększenie efektywności administracyjnej poprzez lepszą organizację i integrację istniejących systemów, stanowi kluczowy element strategii rozwoju przedsiębiorstwa.

                                                %%%ODPOWIEDŹ%%%
                                                Implementacja nowego systemu zarządzania zasobami ludzkimi, który ma na celu zautomatyzowanie procesów rekrutacyjnych, a także zwiększenie efektywności administracyjnej poprzez lepszą organizację i integrację istniejących systemów, stanowi kluczowy element strategii rozwoju przedsiębiorstwa.
                                                </PRZYKŁAD1>

                                                <PRZYKŁAD2>
                                                %%%TEKST%%%
                                                Zgodnie z raportem, który został opublikowany przez niezależnych ekspertów zajmujących się analizą rynku finansowego, wskaźniki rentowności przedsiębiorstw utrzymują się na stabilnym poziomie, jednak przewiduje się, że w kolejnych kwartałach mogą one ulec zmianie w wyniku zmieniających się warunków gospodarczych.

                                                %%%ODPOWIEDŹ%%%
                                                Zgodnie z raportem, który został opublikowany przez niezależnych ekspertów zajmujących się analizą rynku finansowego, wskaźniki rentowności przedsiębiorstw utrzymują się na stabilnym poziomie, jednak przewiduje się, że w kolejnych kwartałach mogą one ulec zmianie w wyniku zmieniających się warunków gospodarczych.
                                                </PRZYKŁAD2>

                                                <PRZYKŁAD3>
                                                %%%TEKST%%%
                                                W związku z wprowadzeniem nowych regulacji prawnych dotyczących ochrony danych osobowych, przedsiębiorstwa będą musiały dostosować swoje wewnętrzne procedury oraz systemy informatyczne, aby zapewnić zgodność z przepisami oraz uniknąć potencjalnych kar finansowych, które mogą być nałożone w przypadku naruszenia obowiązujących regulacji.

                                                %%%ODPOWIEDŹ%%%
                                                W związku z wprowadzeniem nowych regulacji prawnych dotyczących ochrony danych osobowych, przedsiębiorstwa będą musiały dostosować swoje wewnętrzne procedury oraz systemy informatyczne, aby zapewnić zgodność z przepisami oraz uniknąć potencjalnych kar finansowych, które mogą być nałożone w przypadku naruszenia obowiązujących regulacji.
                                                </PRZYKŁAD3>

                                                %%%TEKST%%%                 
                                                {text}

                                                %%%ODPOWIEDŹ%%%'''}
            ]
        )
        answer = check_complex_sentences.choices[0].message.content
        return answer

    def foreign_word_searcher(self, text):

        check_foreign_words = CLIENT.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system",
                 "content": '''Jesteś ekspertem językowym, który z łatwością identyfikuje słowa, które nie są w języku polskim. Twoim zadaniem jest analiza tekstu w celu znalezienia i wypisania takich słów. Odpowiadasz precyzyjnie i profesjonalnie.'''},
                {"role": "user", "content": f'''Twoim zadaniem jest analiza treści otrzymanego tekstu i znalezienie w nim słów, które nie są w języku polskim. Mogą to być wyrazy zapożyczone z innych języków lub wtrącenia. Wypisz każde takie słowo w osobnej linii.

                                                <PRZYKŁAD1>
                                                %%%TEKST%%%
                                                W nowym systemie CRM wdrożono mechanizmy automatyzacji, które integrują się z API zewnętrznych platform e-commerce, co ma na celu zwiększenie user experience.

                                                %%%ODPOWIEDŹ%%%
                                                CRM
                                                API
                                                e-commerce
                                                user experience
                                                </PRZYKŁAD1>

                                                <PRZYKŁAD2>
                                                %%%TEKST%%%
                                                Nowy raport zawiera insighty, które mogą pomóc w poprawie customer journey, w oparciu o case studies z rynku fintech.

                                                %%%ODPOWIEDŹ%%%
                                                insighty
                                                customer journey
                                                case studies
                                                fintech
                                                </PRZYKŁAD2>

                                                <PRZYKŁAD3>
                                                %%%TEKST%%%
                                                Organizacja zorganizowała event na dużą skalę, aby promować partnershipy z liderami branży IT, którzy dostarczają cutting-edge solutions.

                                                %%%ODPOWIEDŹ%%%
                                                event
                                                partnershipy
                                                cutting-edge
                                                solutions
                                                </PRZYKŁAD3>

                                                %%%TEKST%%%                 
                                                {text}

                                                %%%ODPOWIEDŹ%%%'''}
            ]
        )
        answer = check_foreign_words.choices[0].message.content
        return answer

    def passive_form_verifier_spacy(self, zdanie):
        doc = nlp(zdanie)
        bierne_czasowniki = []
        
        for token in doc:
            if token.pos_ == "VERB":
                if "Voice=Pass" in token.morph:
                    bierne_czasowniki.append(token.text)
        
        return bierne_czasowniki



    # zdanie = "Zostało podjęte działanie, które miało poprawić sytuację. Reformy zostały wdrożone przez ministerstwo."

    # bierne_czasowniki = wykryj_strone_bierna(zdanie)

    # print("Czasowniki w stronie biernej:", bierne_czasowniki)