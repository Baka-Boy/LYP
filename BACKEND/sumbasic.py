from collections import Counter
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

from rouge_score import rouge_scorer
nltk.download('punkt')
def calculate_word_probabilities(document):
    words = word_tokenize(document.lower())
    word_counts = Counter(words)
    total_words = sum(word_counts.values())
    word_probabilities = {word: count / total_words for word, count in word_counts.items()}
    return word_probabilities

def calculate_sentence_scores(document, word_probabilities):
    sentences = sent_tokenize(document)
    sentence_scores = {}

    for sentence in sentences:
        words = word_tokenize(sentence.lower())
        score = sum(word_probabilities.get(word, 0) for word in words) / len(words)
        sentence_scores[sentence] = score

    return sentence_scores

def summarize(document, summary_length):
    word_probabilities = calculate_word_probabilities(document)
    sentences = sent_tokenize(document)
    summary = []

    while len(summary) < summary_length:
        best_sentence = max(sentences, key=lambda x: calculate_sentence_scores(x, word_probabilities).get(x, 0))
        summary.append(best_sentence)
        words = word_tokenize(best_sentence.lower())
        for word in words:
            word_probabilities[word] = 0
        sentences.remove(best_sentence)

    return ' '.join(summary)

def evaluate_rouge(generated_summary, reference_summary):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL', 'rougeLsum'], use_stemmer=True)
    scores = scorer.score(generated_summary, reference_summary)
    return scores

# Usage - ATC 1 - https://www.engadget.com/proposed-class-action-lawsuit-accuses-apple-of-monopolizing-cloud-storage-for-its-devices-190822242.html
text = "Following months of speculation, the European Commission has officially handed down its fine to Apple, and it's much higher than initially expected. Apple is on the hook to pay €1.8 billion ($1.95 billion) for restricting alternative music streaming apps on the App Store — the EU's first fine for Apple and its third-largest ever announced. It follows an investigation initially opened in 2020 following Spotify's filed complaint alleging Apple took steps to suppress the music service due to competition with iTunes and Apple Music. The Commission has announced that Apple bans music streaming app developers from fully informing iOS users about alternative and cheaper music subscription services available outside of the app and from providing any instructions about how to subscribe to such offers. The practice, known as anti-steering, is illegal under EU antitrust laws. The investigation found that Apple banned app developers from telling users the price of any subscriptions on the internet or the difference in price between in-app and outside purchases. The company also prevented developers from including information about or links to alternative subscription purchasing pages on their websites or in emails. Apple has engaged in these practices for nearly 10 years and might have caused iOS users to pay more for music streaming subscriptions than necessary due to the fees it imposes (that developers then factor into their prices). The Commission found Apple's actions also led to non-monetary harm, creating a more frustrating user experience. The news follows February rumors that Apple would be hit with a fine of €500 million ($542.6 million) due to its antitrust App Store policies — less than a third of the final number. The European Commission claims it set the fine at €1.8 billion to be sufficiently deterrent to prevent Apple repeating its actions. However, Apple plans to appeal the decision."
summary = summarize(text, 4)
print(summary)
scores = evaluate_rouge(summary, text)
print(scores)

# Usage - ATC 2 - https://www.globenewswire.com/news-release/2024/03/05/2840707/28124/en/Global-Plug-In-Hybrid-Electric-Vehicle-PHEV-Market-to-Reach-189-47-Billion-by-2030-Comprehensive-Industry-Trends-Market-Shares-Growth-Insights-and-Key-Player-Profiles.html
text = "Global Plug-In Hybrid Electric Vehicle (PHEV) Market to Reach $189.47 Billion by 2030: Comprehensive Industry Trends, Market Shares, Growth Insights, and Key Player Profiles March 05, 2024 11:33 ET | Source: Research and Markets Share Dublin, March 05, 2024 (GLOBE NEWSWIRE) -- The Plug-in Hybrid Electric Vehicle Market, Size, Global Forecast 2024-2030, Industry Trends, Share, Growth, Insight, Impact of Inflation, Company Analysis report has been added to ResearchAndMarkets.com's offering. The Global Plug-In Hybrid Electric Vehicle Market is on a steady course of growth, projected to achieve an estimated value of around US$ 189.47 billion by the year 2030. This report sheds light on the market trends, shares, and growth that illuminate the intersecting paths of traditional automotive engineering and futuristic electric mobility. This market expansion is anticipated to flourish at a CAGR of 10.82% from the year 2024 to 2030, paving the way for sustainable and electrified transportation solutions. Within this burgeoning sector, it is observed that the Asia-Pacific region, fueled by China's extensive market presence and robust governmental support for electric vehicles (EVs), stands as a front-runner. Europe and North America are not far behind, buoyed by established automakers and increasing consumer inclination towards eco-friendly vehicle options. These regions are witnessing a major shift as governments implement policy initiatives and tax incentives to promote EV and PHEV adoption, further contributing to market vitality. Segmented Vehicle Class and Car Type Analysis: Mid-Priced PHEVs and SUVs Lead Market Demand The market is dissected into various segments such as vehicle classes and car types, with mid-priced Plug-in Hybrid Electric Vehicles emerging as the driving force of the market. This segment offers consumers a harmonious blend of affordability and cutting-edge technology. Additionally, the popularity of SUVs as PHEVs manifests a powerful combination of utility and energy efficiency. This segment brings the rugged appeal of SUVs to environmentally conscious buyers, delivering both roomy comfort and sustainable driving options. Among nations, the United States is recognized for its escalating growth and strategic positioning in the global PHEV market. American consumers have shown an increased affinity for PHEVs as a middle ground between traditional automobiles and fully electric vehicles. Enhanced by federal initiatives and a burgeoning charging infrastructure, the U.S. market for PHEVs is surging, denoting a significant geographic region of growth within the global landscape. Key players such as Tesla, Ford, General Motors, and Toyota are actively broadening the PHEV market spectrum with strategic advancements and innovations, as highlighted in the comprehensive analysis. This has led to a diversification of choices for consumers, signaling a transformative phase for the automotive industry. The detailed market analysis is classified based on Vehicle Class into Low Priced, Mid-Priced, and Luxury categories. With respect to Car Type, it is broken down into SUV, MPV & Vans, Midsize & Large Cars, and Small & Compact Cars. Geographically, the study encompasses a thorough breakdown into key regions such as North America, Europe, Asia Pacific, Latin America, Middle East & Africa, and the Rest of the World, presenting a 360-degree view of the PHEV landscape. Companies Mentioned Tesla BMW Group BYD Company Ltd. Mercedes-Benz Group AG Ford Motor Company General Motor Company Nissan Motor Co. Ltd. Toyota Motor Corporation"
summary = summarize(text, 4)
print(summary)
scores = evaluate_rouge(summary, text)
print(scores)

# Usage - ATC 3 - https://www.bbc.com/news/technology-68479242
text = "A far-left activist group has claimed responsibility for a suspected arson attack which saw Tesla halt production at its Berlin car factory on Tuesday. In a letter published online, activists calling themselves the Volcano Group say they sabotaged production. An electricity pylon close to the plant caught fire, causing power outages in the factory and nearby towns. Tesla said workers had been sent home but its building was in a 'safe state'. The fire did not reach the electric car-maker's factory itself but did burn an electricity pylon and high-voltage wires. In its letter claiming responsibility for the attack, the Volcano Group said it sabotaged Tesla because it ate up resources and labour. It also accused Tesla of contaminating groundwater and using huge amounts of drinking water. The BBC has contacted the car firm for its response to the accusations. The Reuters news agency has reported that state police are checking the authenticity of the letter. 'The rule of law will react to such an act of sabotage with the utmost severity,' said Interior Minister for Brandenburg state Michael Stuebgen after the attack took place on Tuesday morning. Controversial expansion Tesla wants to double the size of its Berlin plant - which is its only one in Europe - a plan which some environmentalists object to because it would involve chopping down nearby trees. Around 100 people are camping in a forest near the factory, protesting against its expansion. However those green activists have distanced themselves from what has happened. One group, which calls itself Robin Wood, told the BBC it had 'nothing to do with the fire'. A protestor on a ladder up a tree next to a treehouse IMAGE SOURCE,REUTERS Image caption, Protestors have set up treehouses in the forest near the factory The Tesla factory currently makes around 500,000 cars a year - the Elon Musk-owned company wants to double that. 'We are currently unable to say when production can be expected to resume,' Tesla said in a statement given to the AFP news agency."
summary = summarize(text, 4)
print(summary)
scores = evaluate_rouge(summary, text)
print(scores)

# Usage - ATC 4 - https://techcrunch.com/2024/03/05/discord-is-down-for-some-users/
text = "Discord is back online after an outage this morning, the company confirmed to TechCrunch. The outage came as Meta’s Instagram, Facebook and Threads all went down this morning. YouTube has also confirmed that its service is having issues this morning too, and that it’s working on a fix. “This incident has been resolved,” Discord’s status page reads. “We are reviewing the updated rate limiting that triggered the initial session start issues, as well as the scaling targets for the internal service which limited guild loading during initial recovery.” Discord says it is monitoring the recovery of multiple systems. According to third party monitoring website DownDetector, the issues began at around 10:50 AM ET. Users reported that they were unable to load messages, while others say said they were unable to access the service at all. The outages across the multiple services come on Super Tuesday, a day when people across a number of U.S. states are voting in the primary today. The outages, mainly on Facebook and Instagram, may make it harder for candidates to continue their outreach and remind people to head to the polls on an important day."
summary = summarize(text, 4)
print(summary)
scores = evaluate_rouge(summary, text)
print(scores)

# Usage - ATC 5 - https://www.wsj.com/tech/salesforce-ceo-marc-benioff-makes-150-million-donation-to-hawaii-hospitals-7b09ef59
text = "The $150 million gift by Marc and Lynne Benioff is one of the largest single private donations in Hawai'i's history. Developed through more than a year of collaboration across three different hospitals, it provides $50 million for Hilo Medical Center, on the island of Hawai'i, to build out critical areas of care, including a state-of-the-art family birthing center, intensive care unit, and neurosurgical program as well as behavioral health services. It provides $100 million for Hawai'i Pacific Health, one of the state's largest nonprofit healthcare organizations, to help create a 'healthcare campus of the future' at Honolulu-based Straub Medical Center. And it deepens connections between both Hawai'i hospitals and UCSF Health in San Francisco to provide more specialized care to patients who need it. The gift brings the Benioffs' total philanthropy in Hawai'i to more than $250 million, including recent gifts of 282 acres for affordable housing on the Island of Hawaii and another 158 acres owned by a separate nonprofit entity for charitable use. The gift builds on previous philanthropic efforts by the Benioffs to expand healthcare and emergency services in Hawai'i, including funding for state-of-the-art medical helicopters and fire trucks; support for Hawaii Island Community Health Center, Kona Hospital Foundation; previous contributions for Hilo Medical Center; providing housing for medical staff and other support at Queen's North Hawai'i Community Hospital in Waimea; and a recent $5 million gift to support Hawai'i Gov. Josh Green's HELP program aimed at recruiting and retaining healthcare professionals. In all, the Benioffs' personal philanthropic giving totals more than $1 billion, including $600 million in healthcare donations in Hawaii, San Francisco and across the country. 'Our philosophy has always been to give locally and to give through experts who deeply understand local needs, and we are so pleased to have found that with the wonderful, lifesaving teams at Hilo Medical Center, Hawai'i Pacific Health and UCSF Health,' said Marc and Lynne Benioff. They added: 'We feel fortunate to have been part of the Hawai'i community for many decades and to be able to support our ohana in this way. Nothing is more important than the health of our community, and access to care for all who need it.""Before becoming governor I worked as an ER doctor in these hospitals, so I know what it means to have a true benefactor step up and rescue services,' said Hawai'i Gov. Green. 'This huge donation will support the care for thousands of critically ill people in Hawai'i. This generosity is a game-changer for our state.'The expansion of Hilo Medical Center is a unique public-private partnership, with the $50 million from the Benioffs matching a previous, separate $50 million appropriation from the State of Hawai'i. In addition to building out critical areas of care, the donation will support an expansion of Hilo Medical Center's physician recruitment program. The Benioffs' $100 million gift to Hawai'i Pacific Health will support a visionary renovation project that will triple the size of Straub Medical Center, which includes the state's only Burn Unit, lifesaving services, community outreach and education that furthers local clinical research. 'Hilo Medical Center's mission is to provide the best possible healthcare for our family, friends and neighbors,' says Dan Brinkman, CEO of Hilo Medical Center. 'These new resources present an opportunity to make healthcare better on Hawaii Island for eeryone."
summary = summarize(text, 4)
print(summary)
scores = evaluate_rouge(summary, text)
print(scores)