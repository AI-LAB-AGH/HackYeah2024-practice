
def filler_word_prompt(transcript):
    return ("Transcript which I provide at the end of this prompt may contain some filler words. The definition of filler"
                       "word is: "
                       "'Filler words are words such as \"um,\" \"ah,\" \"hmm,\" \"like,\" \"you know,\" and \"alright\" "
                       "that are used to give the speaker time to think, express uncertainty or make something awkward feel less awkward, "
                       "or as a verbal tick. Filler words are also known as vocal disfluencies or hesitations.' "
                       "You have to find these filler words in the transcript. In your response, write only these filler words, one per line."
                       "If there aren't any issues like that, return only word  \"brak\" ."
                       "Jeśli nie ma takich fragmentów tekstu, zwróć tylko słowo  \"brak\" ."
                       f"Here is the transcript: <TEXT> {transcript} <\\TEXT>")

def filler_word_prompt_pl(transcript):
    return ("Transkrypcja, którą podaję na końcu tego polecenia, może zawierać niektóre słowa wypełniacze. Definicja słowa wypełniacza"
                       " to: "
                       "'Słowa wypełniacze to takie wyrazy jak „yyy”, „hmm”, „eee”, „no”, „tak”, które są używane, aby dać mówiącemu czas na zastanowienie,"
                       "wyrażenie niepewności lub sprawienie, by coś niezręcznego było mniej niezręczne, albo jako werbalny tik. "
                       "Słowa wypełniacze są również znane jako werbalne zacięcia lub wahania.' "
                       "Musisz znaleźć te słowa wypełniacze w transkrypcji. W odpowiedzi napisz tylko te słowa wypełniacze, jedno na linię."
                       "Jeśli nie ma takich fragmentów tekstu, zwróć tylko słowo  \"brak\" ."
                       f"Oto transkrypcja: <TEXT> {transcript} <\\TEXT>")

def repetitions_prompt(transcript):
    return ("The transcript which I provide at the end of this prompt may contain some repeated words or phrases. "
                         "Repetition can occur when the speaker says the same word or phrase multiple times consecutively or at close intervals. "
                         "You have to find these repeated words or phrases in the transcript. In your response, write only the repeated words or phrases, one per line. "
                         "If there aren't any issues like that, return only word  \"brak\" ."
                         f"Here is the transcript: <TEXT> {transcript} <\\TEXT>")

def repetitions_prompt_pl(transcript):
    return ("Transkrypcja, którą podaję na końcu tego polecenia, może zawierać powtórzone słowa lub frazy. "
                         "Powtórzenie może wystąpić, gdy mówca mówi to samo słowo lub frazę wielokrotnie, bezpośrednio po sobie lub w krótkich odstępach czasu. "
                         "Musisz znaleźć te powtórzone słowa lub frazy w transkrypcji. W odpowiedzi napisz tylko te powtórzone słowa lub frazy, jedno na linię. "
                         "Jeśli nie ma takich fragmentów tekstu, zwróć tylko słowo  \"brak\" ."
                         f"Oto transkrypcja: <TEKST> {transcript} <\\TEKST>")

#POMYŚLEĆ NAD PRZYKŁADAMI
def complex_words_prompt(transcript):
    return ("The transcript which I provide at the end of this prompt may contain some very complicated or complex words. "
            "These words might be uncommon, highly technical, or difficult for casual viewers to understand. "
            "For example: 'antidisestablishmentarianism', 'quintessential', 'juxtaposition'. "
            "Your task is to identify such words in the transcript. In your response, write only the complicated words, one per line. "
            "If there aren't any issues like that, return only word  \"brak\" ."
            f"Here is the transcript: <TEXT> {transcript} <\\TEXT>")

def complex_words_prompt_pl(transcript):
    return ("Transkrypcja, którą podaję na końcu tego polecenia, może zawierać bardzo skomplikowane lub trudne słowa. "
            "Są to słowa rzadko używane, specjalistyczne lub trudne do zrozumienia dla przeciętnego odbiorcy. "
            "Na przykład: 'antyestablishmentaryzm', 'kwintesencja', 'transcendencja'. "
            "Twoim zadaniem jest zidentyfikowanie takich słów w transkrypcji. W odpowiedzi wypisz tylko trudne słowa, każde w nowej linii. "
            "Jeśli nie ma takich fragmentów tekstu, zwróć tylko słowo  \"brak\" ."
            f"Oto transkrypcja: <TEXT> {transcript} <\\TEXT>")

def jargon_words_prompt(transcript):
    return ("The transcript which I provide at the end of this prompt may contain some jargon or specialized terms. "
            "These are words or phrases used in specific professions, fields, or industries, which may not be easily understood by a general audience. "
            "For example: 'synergy', 'blockchain', 'quantum entanglement'. "
            "Your task is to identify such jargon words in the transcript. In your response, write only the jargon words, one per line. "
            "If there aren't any issues like that, return only word  \"brak\" ."
            f"Here is the transcript: <TEXT> {transcript} <\\TEXT>")

def jargon_words_prompt_pl(transcript):
    return ("Transkrypcja, którą podaję na końcu tego polecenia, może zawierać żargonowe lub specjalistyczne terminy. "
            "Są to słowa lub frazy używane w określonych zawodach, dziedzinach lub branżach, które mogą być trudne do zrozumienia dla ogólnej publiczności. "
            "Na przykład: 'synergia', 'blockchain', 'splątanie kwantowe'. "
            "Twoim zadaniem jest zidentyfikowanie takich żargonowych słów w transkrypcji. W odpowiedzi wypisz tylko słowa żargonowe, każde w nowej linii. "
            "Jeśli nie ma takich fragmentów tekstu, zwróć tylko słowo  \"brak\" ."
            f"Oto transkrypcja: <TEXT> {transcript} <\\TEXT>")

def non_polish_words_prompt(transcript):
    return ("The transcript which I provide at the end of this prompt may contain words in languages other than Polish. "
            "Your task is to identify such words that are not in Polish. "
            "For example: 'business', 'feedback', 'artificial intelligence'. "
            "In your response, write only these non-Polish words, one per line. "
            "If there aren't any issues like that, return only word  \"brak\" ."
            f"Here is the transcript: <TEXT> {transcript} <\\TEXT>")

def non_polish_words_prompt_pl(transcript):
    return ("Transkrypcja, którą podaję na końcu tego polecenia, może zawierać słowa w językach innych niż polski. "
            "Twoim zadaniem jest zidentyfikowanie takich słów, które nie są w języku polskim. "
            "Na przykład: 'business', 'feedback', 'artificial intelligence'. "
            "W odpowiedzi wypisz tylko te niepolskie słowa, każde w nowej linii. "
            "Jeśli nie ma takich fragmentów tekstu, zwróć tylko słowo  \"brak\" ."
            f"Oto transkrypcja: <TEXT> {transcript} <\\TEXT>")

def non_existing_words_prompt(transcript):
    return ("The transcript which I provide at the end of this prompt may contain non-existing or made-up words. "
            "These are words that do not appear in standard dictionaries or are not recognized as legitimate words. "
            "For example: 'flibbertigibbet', 'snollygoster', 'glabberflabber'. "
            "Your task is to identify such non-existing words in the transcript. In your response, write only the non-existing words, one per line. "
            "If there aren't any issues like that, return only word  \"brak\" ."
            f"Here is the transcript: <TEXT> {transcript} <\\TEXT>")

def non_existing_words_prompt_pl(transcript):
    return ("Transkrypcja, którą podaję na końcu tego polecenia, może zawierać nieistniejące lub wymyślone słowa. "
            "Są to słowa, które nie występują w standardowych słownikach lub nie są uznawane za prawidłowe słowa. "
            "Na przykład: 'flibbertigibbet', 'snollygoster', 'glabberflabber'. "
            "Twoim zadaniem jest zidentyfikowanie takich nieistniejących słów w transkrypcji. W odpowiedzi wypisz tylko nieistniejące słowa, każde w nowej linii. "
            "Jeśli nie ma takich fragmentów tekstu, zwróć tylko słowo  \"brak\" ."
            f"Oto transkrypcja: <TEXT> {transcript} <\\TEXT>")

def passive_voice_prompt_pl(transcript):
    return ("Transkrypcja, którą podaję na końcu tego polecenia, może zawierać zdania w stronie biernej. "
            "Strona bierna występuje, gdy wykonawca czynności jest nieokreślony lub nieistotny, a skupiamy się na odbiorcy czynności. "
            "Na przykład: 'Zadanie zostało wykonane', 'Książka została przeczytana przez ucznia'. "
            "Twoim zadaniem jest zidentyfikowanie takich zdań w transkrypcji. W odpowiedzi wypisz tylko zdania w stronie biernej, każde w nowej linii. "
            "Jeśli nie ma takich fragmentów tekstu, zwróć tylko słowo  \"brak\" ."
            f"Oto transkrypcja: <TEXT> {transcript} <\\TEXT>")

def unexpected_topic_change_prompt(transcript):
    return ("The transcript which I provide at the end of this prompt may contain unexpected changes in topic. "
            "An unexpected topic change occurs when the speaker shifts to a new subject that is unrelated to the previous one. "
            "Your task is to identify the first word of every new topic in the transcript. "
            "In your response, write only the first words of each new topic, one per line. "
            "If there aren't any issues like that, return only word \"brak\" ."
            f"Here is the transcript: <TEXT> {transcript} <\\TEXT>")

def unexpected_topic_change_prompt_pl(transcript):
    return ("Transkrypcja, którą podaję na końcu tego polecenia, może zawierać nieoczekiwane zmiany tematu. "
            "Nieoczekiwana zmiana tematu występuje, gdy mówca przechodzi do nowego zagadnienia, które jest niepowiązane z poprzednim. "
            "Twoim zadaniem jest zidentyfikowanie pierwszego słowa każdego nowego tematu w transkrypcji. "
            "W odpowiedzi wypisz tylko pierwsze słowa każdego nowego tematu, każde w nowej linii. "
            "Jeśli nie ma takich fragmentów tekstu, zwróć tylko słowo  \"brak\" ."
            f"Oto transkrypcja: <TEXT> {transcript} <\\TEXT>")

def unusual_numbers_prompt(statement):
    return ("The statement I provide at the end of this prompt may contain an unusual or excessive amount of numbers. "
            "An unusual number of figures can include statistical data, percentages, or any numerical information that may confuse or overwhelm the viewer. "
            "Your task is to identify and list the numbers present in the statement. "
            "In your response, write only the numbers, one per line. "
            "If there aren't any issues like that, return only word  \"brak\" ."
            f"Here is the statement: <TEXT> {statement} <\\TEXT>")

def unusual_numbers_prompt_pl(statement):
    return ("Oświadczenie, które podaję na końcu tego polecenia, może zawierać nietypową lub nadmierną ilość liczb. "
            "Nadmiar liczb może obejmować dane statystyczne, procenty lub jakiekolwiek informacje numeryczne, które mogą zmylić lub przytłoczyć widza. "
            "Twoim zadaniem jest zidentyfikowanie i wypisanie liczb obecnych w oświadczeniu. "
            "W odpowiedzi wypisz tylko liczby, każda w nowej linii. "
            "Jeśli nie ma takich fragmentów tekstu, zwróć tylko słowo  \"brak\" ."
            f"Oto oświadczenie: <TEXT> {statement} <\\TEXT>")

def target_group_prompt(statement):
    return ("The statement I provide at the end of this prompt may be aimed at a specific target group of people. "
            "Based on the content, tone, language, and any implicit or explicit information within the statement, "
            "your task is to describe the likely target audience. Consider factors such as age, profession, interests, education level, or any other relevant characteristics. "
            "In your response, provide a clear description of the target group. Write it in polish."
            f"Here is the statement: <TEXT> {statement} <\\TEXT>")

def valid_questions_prompt(statement):
    return ("The statement I provide at the end of this prompt may contain various details, claims, or pieces of information. "
            "Your task is to generate 10 valid and relevant questions about the statement. These questions should explore its content, context, assumptions, and implications. "
            "Consider aspects like the clarity, purpose, evidence, or any potential gaps in the statement. "
            "In your response, provide 10 distinct questions that could be asked about the statement. Write it in polish."
            "There should be one question per line, line by line."
            f"Here is the statement: <TEXT> {statement} <\\TEXT>")

def important_phrases_prompt(statement):
    return ("The statement I provide at the end of this prompt contains several key ideas or important phrases. "
            "Your task is to identify and cite the most significant phrases within the statement. "
            "These phrases should reflect the main points, arguments, or themes presented. "
            "In your response, list the important phrases along with their context in the statement. Write it in polish."
            "There should be one citation per line, line by line. "
            f"Here is the statement: <TEXT> {statement} <\\TEXT>")