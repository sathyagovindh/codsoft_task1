# import re module for pattern matching
import re
# import random module for pick random values
import random


# creating class
class chatbot:
    def __init__(self):
        self.greeting = "\nBOT: Hello there!👋 Welcome ! May I know your name please\nUSER:"
        self.negative_response = ["no", "not", "quite", "end", "stop", "conclude", "wrap-up", "thanks", "thankyou",
                                  "thank-you"]
        self.question = {'What is your favorite book?': r'.*(best|favorite|favourite).*(book|books).*',
                    'Can you recommend a good mystery novel?': r'.*mystery?.*(novel|novels).*',
                    'How do you find new books to read?': r'.*find?.*new.*books.*read.*',
                    'Suggest best fiction and non-fiction movies?': r'.*best?.*(fiction|fictional)?.*non[-]?(fiction|fictional)?.*movies?',
                    'Can you explain the plot of a book you recently read?': r'.*recently.*read.*book.*',
                    'How do you borrow books from a library?': r'.*borrow.*books.*library.*',
                    'What is your favorite genre of literature?': r'.*(favorite|favourite)?.*genre.*(book|literature).*',
                    'Can you recommend a classic novel?': r'.*classic.*novel.*',
                    'How do you organize your bookshelf?': r'.*(organize|organise).*bookshelf.*',
                    'What are some benefits of reading?': r'.*benefits.*reading.*books?.*',
                    'Can you describe the main characters in a book you enjoyed?': r'.*main?.*characters.*book.*enjoyed.*',
                    'How do you write a book review?': r'.*write.*book.*review.*',
                    'What is your opinion on e-books versus physical books?': r'.*e[-]?(book|books).*physical.*book.*',
                    'Can you recommend a good fantasy series for young readers?': r'.*fantasy.*(book|books|series).*',
                    'How do you find time to read with a busy schedule?': r'.*find?.*time.*read.*(busy schedule)?.*',
                    'What is the importance of symbolism in literature?': r'.*importance?.*symbolism.*(literature|books).*',
                    'How do you choose a book for a book club?': r'.*choose.*(book|books).*book club.*',
                    'Can you recommend a biography of a famous person?': r'.*biography.*famous.*(person|author).*',
                    'What are some common themes in literature?': r'.*common?.*themes.*(literature|books).*',
                    'How do you support local bookstores?': r'.*support.*local.*(library|libraries|bookstores|bookstalls).*'
                         }

    def greet(self):

        name = input(self.greeting)
        reply = input(
            f"\nBOT: Hi {name} !I'm here to assist you with any questions about \" Books and Literature\". Feel free to ask anything or let me know how I can help you today!\nUSER:").lower()

        while reply not in self.negative_response:
            reply = input(self.find_match(reply)).lower()

        else:
            print(
                "\nNo problem! If you have any questions or need assistance in the future, feel free to reach out. Have a great day!")

    def find_match(self, reply):
        global found_match
        for key,value in self.question.items():
            found_match = re.search(value, reply)
            if found_match and key == "What is your favorite book?":
                return self.favorite_book()
            elif found_match and key == "Can you recommend a good mystery novel?":
                return self.mystery_novel()
            elif found_match and key == "How do you find new books to read?":
                return self.new_books()
            elif found_match and key == "Suggest best fiction and non-fiction movies?":
                return self.fic_nonfic()
            elif found_match and key == "Can you explain the plot of a book you recently read?":
                return self.recently_read()
            elif found_match and key == "How do you borrow books from a library?":
                return self.borrow_books()
            elif found_match and key == 'What is your favorite genre of literature?':
                return self.genre()
            elif found_match and key == 'Can you recommend a classic novel?':
                return self.novel()
            elif found_match and key == 'How do you organize your bookshelf?':
                return self.bookshelf()
            elif found_match and key == 'What are some benefits of reading?':
                return self.benefits()
            elif found_match and key == 'Can you describe the main characters in a book you enjoyed?':
                return self.characters()
            elif found_match and key == 'How do you write a book review?':
                return self.write_review()
            elif found_match and key == 'What is your opinion on e-books versus physical books?':
                return self.difference()
            elif found_match and key == 'Can you recommend a good fantasy series for young readers?':
                return self.fantasy()
            elif found_match and key == 'How do you find time to read with a busy schedule?':
                return self.time_to_read()
            elif found_match and key == 'What is the importance of symbolism in literature?':
                return self.symbolism()
            elif found_match and key == 'How do you choose a book for a book club?':
                return self.book_club()
            elif found_match and key == 'Can you recommend a biography of a famous person?':
                return self.biography()
            elif found_match and key == 'What are some common themes in literature?':
                return self.themes()
            elif found_match and key == 'How do you support local bookstores?':
                return self.local_stores()

        if found_match==None:
           return self.no_match_found()
    def favorite_book(self):
        responses = (
            "\nBOT: As an AI, I don't have personal preferences like humans do, so I don't have a favorite book. However, I can recommend books based on various criteria or preferences you might have! Let me know if you're interested in any recommendations.\nUSER:",
            "\nBOT:  As an AI, I don't have personal preferences like humans do, but I can suggest few books like \"Harry Potter\",\"The Lord of the Rings\",\"To Kill a Mockingbird\",\"The Great Gatsby\",\"Pride and Prejudice\" etc..\nUSER:")
        return random.choice(responses)

    def mystery_novel(self):
        responses = (
            "\"The Girl with the Dragon Tattoo\" by Stieg Larsson - This international bestseller follows journalist Mikael Blomkvist and hacker Lisbeth Salander as they investigate a decades-old disappearance in a wealthy Swedish family.\nUSER:",
            "\"The Da Vinci Code\" by Dan Brown - A gripping thriller that follows symbologist Robert Langdon and cryptologist Sophie Neveu as they unravel a complex mystery involving secret societies, hidden messages, and religious symbolism.\nUSER:",
            "\"And Then There Were None\" by Agatha Christie - A classic whodunit where ten strangers are lured to a remote island and are mysteriously killed one by one, forcing them to confront their past sins.\nUSER:")
        return random.choice(responses)

    def new_books(self):
        responses = (
            "Recommendations from Friends and Family: Many people find new books to read based on recommendations from friends, family members, or colleagues whose tastes they trust.\nUSER:",
            "Book Clubs: Joining a book club can be a great way to discover new books, as members often suggest and discuss different titles.\nUSER:",
            "Bestseller Lists: Checking bestseller lists from reputable sources like The New York Times, Amazon, or Publishers Weekly can help you discover popular and trending books.\nUSER:",
            "Online Communities and Forums: Platforms like Goodreads, Reddit's r/books, and various book-related groups on social media are excellent places to find recommendations from fellow book enthusiasts.\nUSER:")
        return random.choice(responses)

    def fic_nonfic(self):
        responses = (
            "Fiction and non-fiction books represent two distinct categories of literature, each with its own unique characteristics and purposes. Fiction books are imaginative works of literature that transport readers into fictional worlds created by the author\'s imagination.\n On the other hand, non-fiction books are factual works of literature that are grounded in reality, based on real events, experiences, or information. These books aim to inform, educate, or persuade readers about various topics, subjects, and issues.\nSome of fiction and non-fiction books include\nFiction Books:\n1.\"Harry Potter and the Sorcerer's Stone\" by J.K. Rowling\n2.\"The Great Gatsby\" by F. Scott Fitzgerald\n3.\"To Kill a Mockingbird\" by Harper Lee\nNon-Fiction Books:\n1.\"Sapiens: A Brief History of Humankind\" by Yuval Noah Harari\n2.\"The Immortal Life of Henrietta Lacks\" by Rebecca Skloot\n3.\"Educated\" by Tara Westover.\nUSER:")
        return random.choice(responses)

    def recently_read(self):
        responses = (
            "As an AI, I don't have the capability to read books or have personal experiences, so I can't provide information about a book I've recently read. However, I can provide a summary of a popular book if you'd like! Just let me know the title, and I'll be happy to give you a brief overview of its plot.\nLet's consider \"1984\" by George Orwell, a classic dystopian novel.\nThe story is set in a totalitarian society ruled by the Party led by Big Brother. The protagonist, Winston Smith, works for the Party's Ministry of Truth, altering historical records to fit the Party's propaganda. However, Winston secretly harbors rebellious thoughts against the oppressive regime.\nUSER:",
            "As an AI language model, I don't have access to real-time data or individual browsing histories, so I can't provide information on what most people have recently read. Reading habits can vary widely among individuals and depend on factors such as personal interests, current events, popular trends, and cultural influences. Some people may be reading bestsellers, while others may be delving into classic literature, non-fiction, or academic texts.\nUSER:")
        return random.choice(responses)

    def borrow_books(self):
        responses = (
            "Borrowing books from a library typically involves the following steps:\nGet a library card: The first step is to sign up for a library card at your local library. \nBrowse the collection: Once you have your library card, you can browse the library's collection to find books you want to borrow.\nReturn the books: Most libraries have a specific loan period, typically ranging from a few weeks to a month, during which you can keep the book. Once you've finished reading, return the book to the library by the due date.\nRenew or request: If you need more time with a book, you may be able to renew it for an extended loan period, either online, by phone, or in person.\nUSER:")
        return responses

    def genre(self):
        responses = (
            "Sure! Here are a few popular genres of literature that you might enjoy exploring:\nMystery/Thriller: If you enjoy suspenseful plots, intricate mysteries, and unexpected twists, then the mystery and thriller genre might be perfect for you. Authors like Agatha Christie, Lee Child, and Gillian Flynn are well-known for their thrilling stories.\nFantasy: Fantasy literature transports readers to magical realms filled with mythical creatures, epic quests, and fantastical adventures\nRomance: Romance novels focus on the development of romantic relationships between characters, often set against the backdrop of compelling storylines and emotional journeys. \nHistorical Fiction: Historical fiction brings the past to life through captivating narratives set in specific time periods or historical events.\nUSER:")
        return responses

    def novel(self):
        responses = (
            "Of course! One classic novel that I highly recommend is \"Pride and Prejudice\" by Jane Austen. First published in 1813, this beloved novel follows the story of Elizabeth Bennet, a witty and independent young woman, as she navigates the challenges of love, marriage, and societal expectations in early 19th-century England.\nUSER:")
        return responses

    def bookshelf(self):
        responses = (
            "Organizing a bookshelf can be a personal preference, and different people may choose to organize their books in various ways based on factors like genre, author, color, or size. Here are some common methods for organizing a bookshelf:\n Alphabetically by Author: Arrange your books in alphabetical order by the author's last name. This method makes it easy to locate books by specific authors.\nGenre or Category: Group books together based on their genre or category, such as fiction, non-fiction, mystery, fantasy, science fiction, biography, etc\nChronological Order: Arrange your books chronologically based on publication date or the time period in which they were written.\nPriority or Frequency of Use: Place books you frequently use or want to read soon in a prominent and easily accessible location on the shelf.\nUSER:")
        return responses

    def benefits(self):
        responses = (
            "Reading offers numerous benefits, both intellectual and emotional. Here are some of the key advantages of reading:\nKnowledge Acquisition: Reading exposes you to new ideas, information, and perspectives, allowing you to expand your knowledge base on various topics.\nVocabulary Expansion: Reading regularly exposes you to a wide range of vocabulary, helping you improve your language skills and communication abilities.\nStress Reduction: Immersing yourself in a good book can be a form of relaxation and escapism, helping to reduce stress levels and promote mental well-being.\nUSER:")
        return responses

    def characters(self):
        responses = (
            "Sure, here's a description of the main characters in \"To Kill a Mockingbird\" by Harper Lee, a book that many people have enjoyed:\nScout Finch: The protagonist and narrator of the story, Scout is a young girl growing up in the racially segregated town of Maycomb, Alabama, during the 1930s. \nAtticus Finch: Scout's father, Atticus Finch, is a respected lawyer known for his integrity, compassion, and unwavering commitment to justice. \nJem Finch: Scout's older brother, Jem Finch, is mature, responsible, and protective of his sister. He idolizes their father, Atticus, and shares his commitment to fairness and equality.\nUSER: ")
        return responses

    def write_review(self):
        responses = (
            "Writing a book review can be an enjoyable and rewarding process. Here are some steps to guide you through writing a thoughtful and engaging book review:\nRead the book thoroughly: Before you can write a review, it's essential to read the book carefully from beginning to end.\nSummarize the plot: Give a brief overview of the book's plot without giving away any major spoilers. \nProvide some background information: Start your review by providing some context about the book, such as the author's name, the title of the book, the genre, and any relevant information about the author or the book's publication.\nEvaluate the writing style: Assess the author's writing style, including their use of language, dialogue, pacing, and descriptive imagery.\nUSER:")
        return responses

    def difference(self):
        responses = (
            "The debate between e-books and physical books is a matter of personal preference, and both formats have their own advantages and disadvantages.\nE-books:\nPortability: E-books allow readers to carry multiple books in a single device, making them convenient for travel and commuting.\nAccessibility: E-books can be downloaded instantly from online stores, allowing readers to access a wide range of titles without leaving their homes.\nAdjustable text size and font: E-books offer customization options for text size, font, and background color, making them accessible to readers with visual impairments.\nSearchability and annotation: E-books enable readers to search for specific keywords or phrases, as well as highlight and annotate text for later reference.\nPhysical books:\nTangibility and aesthetics: Physical books provide a tactile reading experience that some readers find more enjoyable and satisfying. They also offer the aesthetic appeal of cover art, typography, and paper quality.\nSense of ownership: Owning physical books allows readers to display them on bookshelves, lend them to friends, and create a personal library collection.\nReduced screen time: Reading physical books can help reduce exposure to screens and alleviate eye strain associated with prolonged digital device use.\nUSER:")
        return responses

    def fantasy(self):
        responses = (
            "Certainly! One popular fantasy series for young readers is \"Percy Jackson & the Olympians\" by Rick Riordan. This series follows the adventures of Percy Jackson, a young demigod who discovers that he is the son of Poseidon, the Greek god of the sea. Throughout the series, Percy navigates the challenges of being a demigod while attending Camp Half-Blood and embarking on quests to save the world from various mythological threats.\nAnother excellent choice is \"Harry Potter\" series by J.K. Rowling. This beloved series follows the journey of Harry Potter, a young wizard who learns on his eleventh birthday that he is a wizard and has been accepted to attend Hogwarts School of Witchcraft and Wizardry.\nUSER:")
        return responses

    def time_to_read(self):
        responses = (
            "Finding time to read can be challenging with a busy schedule, but with some planning and prioritization, it's definitely possible. Here are some tips to help you carve out time for reading:\nSet aside dedicated time: Schedule specific times during your day when you can devote to reading.\nMake it a habit: Incorporate reading into your daily routine by making it a habit. \nLimit screen time: Reduce the time spent on activities like watching TV, scrolling through social media, or playing video games, and replace it with reading instead.\nUSER:")
        return responses

    def symbolism(self):
        responses = (
            "Symbolism in literature holds significant importance as it enriches texts by adding depth, complexity, and layers of meaning. By representing abstract ideas or values through concrete symbols, authors enhance the themes of their works, inviting readers to explore complex concepts in a nuanced manner. Symbols evoke emotions, stimulate imagination, and facilitate critical analysis, allowing readers to uncover hidden meanings and interpret the text on multiple levels. Moreover, symbols provide unity and coherence to the narrative, connecting disparate elements and fostering thematic cohesion.\nUSER: ")
        return responses

    def book_club(self):
        responses = (
            "Choosing a book for a book club involves thoughtful consideration of members' interests, diversity, discussion potential, and consensus. By surveying club members for recommendations and preferences, prioritizing diversity in genre, authorship, and themes, and selecting books with rich character development and open-ended interpretations, clubs can ensure engaging discussions. Additionally, rotating the responsibility of selecting books among members and reaching a consensus through discussion or voting allows everyone to have a say in the process. Ultimately, the goal is to choose books that resonate with the group, stimulate meaningful conversations, and enrich the book club experience for all members.\nUSER:")
        return responses

    def biography(self):
        responses = (
            "Certainly! One highly recommended biography is \"Steve Jobs\" by Walter Isaacson. This comprehensive biography delves into the life of the iconic co-founder of Apple Inc., providing insights into his visionary leadership, innovative mindset, and complex personality. Isaacson's thorough research and engaging narrative style offer readers a captivating exploration of Jobs' life, from his early days in Silicon Valley to his revolutionary impact on technology and culture. Whether you're intrigued by entrepreneurship, technology, or simply fascinated by extraordinary individuals, \"Steve Jobs\" offers a compelling portrait of one of the most influential figures of the modern era.\nUSER:")
        return responses

    def themes(self):
        responses = (
            "Common themes in literature encompass a wide array of human experiences and emotions that resonate across cultures and time periods. These themes serve as the foundation upon which stories are built, providing depth and meaning to narrative exploration. Love and relationships often take center stage, with authors delving into the complexities of romantic entanglements, familial bonds, friendships, and other interpersonal connections. Alongside this, the journey of self-discovery and identity formation is a recurring motif, as characters grapple with questions of self-worth, belonging, and personal growth. Coming-of-age narratives follow individuals as they navigate the challenges of adolescence, transitioning into adulthood while seeking their place in the world.\nUSER:")
        return responses

    def local_stores(self):
        responses = ("Supporting local bookstores is essential for fostering a thriving literary community and preserving cultural diversity. These independent establishments play a vital role in promoting literature, providing a platform for local authors, and offering unique reading experiences. By purchasing books from local bookstores instead of online retailers or chain stores, you directly contribute to the local economy and help sustain the livelihoods of bookstore owners and staff. Additionally, attending events hosted by local bookstores, such as author readings, book signings, and book clubs, not only enriches your reading experience but also creates opportunities for meaningful engagement with fellow book lovers and authors. Furthermore, spreading the word about your favorite local bookstore through word-of-mouth recommendations, social media shares, and online reviews can help attract new customers and increase visibility. Volunteering your time, joining loyalty programs, and providing feedback are other ways to support local bookstores and ensure their continued success. By actively participating in and advocating for your local bookstore, you contribute to the vibrancy and resilience of your community's literary ecosystem.\nUSER:")
        return responses

    def no_match_found(self):
        responses = ("I'm sorry, I couldn't find a suitable response based on the input provided. It seems that the question or request may be outside the scope of my current capabilities.Please reassure the spelling/word that used. Is there anything else I can assist you with?\nUSER:")
        return responses


chat = chatbot()
chat.greet()
