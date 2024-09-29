from openai import OpenAI
from . import api_key

CLIENT = OpenAI(api_key=api_key.get_api_key())
MODEL = "gpt-4o"


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
                                                Myśl krok po kroku. Jeśli nie znajdziesz żadnych przykładów, zwróć w odpowiedzi po prostu słowo \"brak\".
                 
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



    def important_fragments_searcher(self, text):
            check_important_fragments = CLIENT.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system",
                     "content": '''Jesteś ekspertem językowym, który analizuje tekst w celu znalezienia i wskazania najważniejszych fragmentów. Twoim zadaniem jest wyodrębnienie kluczowych informacji z tekstu, ograniczając się do maksymalnie 3-4 słów na każdy fragment. Odpowiadasz precyzyjnie i profesjonalnie.'''},
                    {"role": "user", "content": f'''Twoim zadaniem jest analiza treści otrzymanego tekstu i wyodrębnienie najważniejszych fragmentów. Fragmenty te powinny liczyć maksymalnie 3-4 słowa i reprezentować kluczowe informacje lub idee zawarte w tekście. Wypisz każdy fragment w osobnej linii. Jeśli nie znajdziesz żadnych przykładów, zwróć w odpowiedzi po prostu słowo \"brak\".

                                                    <PRZYKŁAD1>
                                                    %%%TEKST%%%
                                                    Podczas spotkania omówiono kwestie związane z wdrożeniem nowego systemu, którego celem jest zwiększenie efektywności pracy zespołów oraz poprawa komunikacji między działami. Podkreślono także znaczenie lepszej koordynacji działań i wykorzystania zasobów.

                                                    %%%ODPOWIEDŹ%%%
                                                    wdrożenie nowego systemu
                                                    zwiększenie efektywności pracy
                                                    poprawa komunikacji
                                                    koordynacja działań
                                                    </PRZYKŁAD1>

                                                    <PRZYKŁAD2>
                                                    %%%TEKST%%%
                                                    Zespół opracował strategię marketingową mającą na celu dotarcie do nowych klientów poprzez kampanie online oraz partnerstwa z innymi firmami technologicznymi. Plan zakłada również rozszerzenie obecności na mediach społecznościowych. 

                                                    %%%ODPOWIEDŹ%%%
                                                    strategia marketingowa
                                                    dotarcie do nowych klientów
                                                    kampanie online
                                                    partnerstwa z firmami
                                                    </PRZYKŁAD2>

                                                    <PRZYKŁAD3>
                                                    %%%TEKST%%%
                                                    Firma ogłosiła wyniki kwartalne, wskazując na wzrost przychodów oraz znaczną redukcję kosztów operacyjnych, co wpłynęło na poprawę marży operacyjnej.

                                                    %%%ODPOWIEDŹ%%%
                                                    wzrost przychodów
                                                    redukcja kosztów operacyjnych
                                                    poprawa marży operacyjnej
                                                    </PRZYKŁAD3>

                                                    %%%TEKST%%%                 
                                                    {text}

                                                    %%%ODPOWIEDŹ%%%'''}
                ]
            )

            answer = check_important_fragments.choices[0].message.content
            return answer

    def jargon_searcher(self, text):

        check_jargon = CLIENT.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system",
                 "content": '''Jesteś ekspertem językowym, który z łatwością identyfikuje słowa należące do żargonu specjalistycznego. Twoim zadaniem jest analiza tekstu w celu znalezienia i wypisania takich słów. Odpowiadasz w sposób jasny i profesjonalny.'''},
                {"role": "user", "content": f'''Twoim zadaniem jest analiza treści otrzymanego tekstu i znalezienie w nim słów należących do żargonu. Mogą to być specjalistyczne terminy techniczne, ekonomiczne, medyczne, prawnicze lub inne charakterystyczne dla danego środowiska.
                                                Odpowiedź powinna zawierać jedno słowo na linię. Jeśli nie znajdziesz żadnych przykładów, zwróć w odpowiedzi po prostu słowo \"brak\".

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
                {"role": "user", "content": f'''Twoim zadaniem jest analiza treści otrzymanego tekstu i znalezienie w nim słów, które są zbyt długie lub zbyt skomplikowane dla przeciętnego odbiorcy. Wybieraj tylko te słowa, które mogą sprawić trudność, a każda odpowiedź powinna zawierać jedno słowo na linię. Jeśli nie znajdziesz żadnych przykładów, zwróć w odpowiedzi po prostu słowo \"brak\".

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
                {"role": "user", "content": f'''Twoim zadaniem jest analiza treści otrzymanego tekstu i znalezienie w nim zdań, które mogą być zbyt długie, skomplikowane lub trudne dla przeciętnego odbiorcy. Zwróć szczególną uwagę na zdania zawierające skomplikowane struktury składniowe lub nadmiarowe informacje. Odpowiedź powinna zawierać jedno zdanie na linię. Jeśli nie znajdziesz żadnych przykładów, zwróć w odpowiedzi po prostu słowo \"brak\".

                                                    <PRZYKŁAD1>
                                                    %%%TEKST%%%
                                                    Implementacja nowego systemu zarządzania zasobami ludzkimi, który ma na celu zautomatyzowanie procesów rekrutacyjnych, a także zwiększenie efektywności administracyjnej poprzez lepszą organizację i integrację istniejących systemów, stanowi kluczowy element strategii rozwoju przedsiębiorstwa. Proces ten wymaga zaangażowania całego zespołu.

                                                    %%%ODPOWIEDŹ%%%
                                                    Implementacja nowego systemu zarządzania zasobami ludzkimi, który ma na celu zautomatyzowanie procesów rekrutacyjnych, a także zwiększenie efektywności administracyjnej poprzez lepszą organizację i integrację istniejących systemów, stanowi kluczowy element strategii rozwoju przedsiębiorstwa.

                                                    <PRZYKŁAD2>
                                                    %%%TEKST%%%
                                                    Zgodnie z raportem, który został opublikowany przez niezależnych ekspertów zajmujących się analizą rynku finansowego, wskaźniki rentowności przedsiębiorstw utrzymują się na stabilnym poziomie. Jednak przewiduje się, że w kolejnych kwartałach mogą one ulec zmianie w wyniku zmieniających się warunków gospodarczych.

                                                    %%%ODPOWIEDŹ%%%
                                                    Zgodnie z raportem, który został opublikowany przez niezależnych ekspertów zajmujących się analizą rynku finansowego, wskaźniki rentowności przedsiębiorstw utrzymują się na stabilnym poziomie, jednak przewiduje się, że w kolejnych kwartałach mogą one ulec zmianie w wyniku zmieniających się warunków gospodarczych.

                                                    <PRZYKŁAD3>
                                                    %%%TEKST%%%
                                                    W związku z wprowadzeniem nowych regulacji prawnych dotyczących ochrony danych osobowych, przedsiębiorstwa będą musiały dostosować swoje wewnętrzne procedury oraz systemy informatyczne. Dzięki temu zapewnią zgodność z przepisami oraz unikną potencjalnych kar finansowych, które mogą być nałożone w przypadku naruszenia obowiązujących regulacji.

                                                    %%%ODPOWIEDŹ%%%
                                                    W związku z wprowadzeniem nowych regulacji prawnych dotyczących ochrony danych osobowych, przedsiębiorstwa będą musiały dostosować swoje wewnętrzne procedury oraz systemy informatyczne, aby zapewnić zgodność z przepisami oraz uniknąć potencjalnych kar finansowych, które mogą być nałożone w przypadku naruszenia obowiązujących regulacji.

                                                    <PRZYKŁAD4>
                                                    %%%TEKST%%%
                                                    Pracownicy spotkali się na krótkiej naradzie, aby omówić postępy projektu.

                                                    %%%ODPOWIEDŹ%%%
                                                    brak

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
                {"role": "user", "content": f'''Twoim zadaniem jest analiza treści otrzymanego tekstu i znalezienie w nim słów, które nie są w języku polskim. Mogą to być wyrazy zapożyczone z innych języków lub wtrącenia. Wypisz każde takie słowo w osobnej linii. Jeśli nie znajdziesz żadnych przykładów, zwróć w odpowiedzi po prostu słowo \"brak\".

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

    def repetition_searcher(self, text):

        check_repetitions = CLIENT.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system",
                 "content": '''Jesteś ekspertem językowym, który z łatwością identyfikuje niepotrzebne powtórzenia w tekście. Twoim zadaniem jest analiza treści w celu znalezienia i wypisania takich powtórzeń, które mogą wpływać na zrozumiałość tekstu. Odpowiadasz profesjonalnie i precyzyjnie.'''},
                {"role": "user", "content": f'''Twoim zadaniem jest analiza otrzymanego tekstu i znalezienie w nim niepotrzebnych powtórzeń. Wypisz każde powtórzone słowo lub frazę w osobnej linii. Jeśli nie znajdziesz żadnych przykładów, zwróć w odpowiedzi po prostu słowo \"brak\".

                                                <PRZYKŁAD1>
                                                %%%TEKST%%%
                                                W czasie spotkania omówiono kwestie związane z wdrażaniem nowego systemu. System ten ma na celu poprawę efektywności procesów oraz zwiększenie bezpieczeństwa danych.

                                                %%%ODPOWIEDŹ%%%
                                                system
                                                </PRZYKŁAD1>

                                                <PRZYKŁAD2>
                                                %%%TEKST%%%
                                                Projekt wymaga współpracy między działami. Współpraca jest kluczowa dla sukcesu tego przedsięwzięcia.

                                                %%%ODPOWIEDŹ%%%
                                                współpraca
                                                </PRZYKŁAD2>

                                                <PRZYKŁAD3>
                                                %%%TEKST%%%
                                                Ustalono, że zespół zrealizuje zadanie w ustalonym czasie, a wszystkie ustalone terminy będą dotrzymane.

                                                %%%ODPOWIEDŹ%%%
                                                ustalone
                                                </PRZYKŁAD3>

                                                %%%TEKST%%%                 
                                                {text}

                                                %%%ODPOWIEDŹ%%%'''}
            ]
        )
        answer = check_repetitions.choices[0].message.content
        return answer

    def non_existent_word_searcher(self, text):

        check_non_existent_words = CLIENT.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system",
                 "content": '''Jesteś ekspertem językowym, który z łatwością identyfikuje słowa, które nie istnieją w języku polskim. Twoim zadaniem jest analiza tekstu w celu znalezienia i wypisania takich słów, które są błędne lub niepoprawne. Odpowiadasz precyzyjnie i profesjonalnie.'''},
                {"role": "user", "content": f'''Twoim zadaniem jest analiza treści otrzymanego tekstu i znalezienie w nim słów, które nie istnieją w języku polskim. Wypisz każde nieistniejące słowo w osobnej linii.

                                                <PRZYKŁAD1>
                                                %%%TEKST%%%
                                                Ostatnio zauważyliśmy wzrost efektywności pracowników, jednak niektóre z nowych rozwiązań są niedopracowalizowane.

                                                %%%ODPOWIEDŹ%%%
                                                niedopracowalizowane
                                                </PRZYKŁAD1>

                                                <PRZYKŁAD2>
                                                %%%TEKST%%%
                                                System zintegrował się z naszymi procesami, ale pojawiły się pewne nieprzewidzalne trudności w procedurze wdrożeniowej.

                                                %%%ODPOWIEDŹ%%%
                                                nieprzewidzalne
                                                </PRZYKŁAD2>

                                                <PRZYKŁAD3>
                                                %%%TEKST%%%
                                                Nowy projekt wymagał dodatkowych zasobów i rewizji pierwotniakowych założeń, jednak nie wszyscy uczestnicy byli w pełni zaangażowani w proces implementacyjny.

                                                %%%ODPOWIEDŹ%%%
                                                pierwotniakowych
                                                </PRZYKŁAD3>

                                                %%%TEKST%%%                 
                                                {text}

                                                %%%ODPOWIEDŹ%%%'''}
            ]
        )

    # def passive_form_verifier_spacy(self, zdanie):
    #     doc = nlp(zdanie)
    #     bierne_czasowniki = []
        
    #     for token in doc:
    #         if token.pos_ == "VERB":
    #             if "Voice=Pass" in token.morph:
    #                 bierne_czasowniki.append(token.text)

    #     if len(bierne_czasowniki) == 0:
    #         return "brak"
    #     else:
    #         return "\n".join(bierne_czasowniki)

    # def number_analysis_spacy(self, zdanie):
    #     doc = nlp(zdanie)
    #     liczby = []

    #     for token in doc:
    #         if token.pos_ == "NUM":
    #             liczby.append(token.text)

    #     if len(zdanie.split()) == 0:
    #         return "brak"

    #     if len(liczby)/len(zdanie.split()) >= 0.1:
    #         return "\n".join(liczby)
    #     else:
    #         return "brak"

    def complex_sentence_searcher_simple(self, text):
        long_sentences = []
        sentences = text.split(".")
        for sentence in sentences:
            if len(sentence.split()) >= 22:
                long_sentences.append(sentence)

        if len(long_sentences) == 0:
            return "brak"
        else:
            return "\n".join(long_sentences)




    # zdanie = "Zostało podjęte działanie, które miało poprawić sytuację. Reformy zostały wdrożone przez ministerstwo."

    # bierne_czasowniki = wykryj_strone_bierna(zdanie)

    # print("Czasowniki w stronie biernej:", bierne_czasowniki)

