from django.shortcuts import render
import requests
import bs4

def HomeView(request):
    word = request.GET.get('word', None)
    h1_texts = []
    pronunciation_texts = []
    li_texts = []
    strongest_synonyms = []
    strong_synonyms = []
    weak_synonyms = []
    results = {}

    if word:
        # Fetch from Dictionary.com
        response = requests.get(f'https://www.dictionary.com/browse/{word}')
        response2 = requests.get(f'https://www.thesaurus.com/browse/{word}')
        
        if response:
            soup_1 = bs4.BeautifulSoup(response.text, 'lxml')
            sections = soup_1.find_all('section', {'data-type': 'dictionary-headword-module'})
            
            # Extract h1 and pronunciation
            for section in sections:
                h1_tag = section.find('h1')
                if h1_tag:
                    h1_texts.append(h1_tag.get_text(strip=True))

                pronunciation_div = section.find('div', {'data-type': 'pronunciation-toggle'})
                if pronunciation_div:
                    p_tag = pronunciation_div.find('p')
                    if p_tag:
                        pronunciation_texts.append(p_tag.get_text(strip=True))

            # Extract meanings
            meaning = soup_1.find_all('ol', {'data-type': 'definition-content-list'})
            for ol in meaning:
                li_elements = ol.find_all('li', recursive=True)
                for li in li_elements:
                    li_text = li.get_text(strip=True)
                    li_texts.append(li_text)
        
        if response2:
            soup_2 = bs4.BeautifulSoup(response2.text, 'lxml')
            synonym_card = soup_2.find('div', {'data-type': 'synonym-and-antonym-card'})
            
            if synonym_card:
                # Find the sections inside the synonym card
                synonym_sections = synonym_card.find_all('div', recursive=True)

                current_category = None

                for section in synonym_sections:
                    # Check for the heading that indicates the type of match
                    heading_tag = section.find('p')  # Find <p> tag that acts as a heading
                    if heading_tag:
                        heading_text = heading_tag.get_text(strip=True).lower()

                        # Set the category based on the heading text
                        if "strongest matches" in heading_text:
                            current_category = "strongest"
                        elif "strong matches" in heading_text:
                            current_category = "strong"
                        elif "weak matches" in heading_text:
                            current_category = "weak"
                        else:
                            current_category = None

                    # Extract synonyms under the current category
                    if current_category and section.find_all('a'):
                        synonyms = [a.get_text(strip=True) for a in section.find_all('a')]

                        if current_category == "strongest":
                            strongest_synonyms.extend(synonyms)
                        elif current_category == "strong":
                            strong_synonyms.extend(synonyms)
                        elif current_category == "weak":
                            weak_synonyms.extend(synonyms)
        
        strongest_synonyms = list(set(strongest_synonyms))
        check_set = set(strong_synonyms + weak_synonyms)
        strongest_synonyms = [item for item in strongest_synonyms if item not in check_set]

        
        # If no h1_texts, meanings, or synonyms found, return an error
        if not h1_texts and not li_texts and not (strongest_synonyms or strong_synonyms or weak_synonyms):
            results = {
                'error': "There is no result related to your search. Please try again with a different word!"
            }
        else:
            results = {
                'word': word,
                'meanings': li_texts,
                'h1_texts': h1_texts,
                'pronunciation_texts': pronunciation_texts,
                'strongest_synonyms': strongest_synonyms,
                'strong_synonyms': strong_synonyms,
                'weak_synonyms': weak_synonyms,
            }
    
    return render(request, 'dictionary/home.html', {'results': results})
