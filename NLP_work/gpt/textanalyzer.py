from openai import OpenAI
import api_key
from prompts import *

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
        print(answer)
        return answer



    def passive_form_verifier_spacy(zdanie):
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