import streamlit as st
import json

st.set_page_config(page_title="Ôn Tập Tiếng Anh EHOU", page_icon="📚", layout="centered")

# Dữ liệu ngân hàng (218 câu hỏi)
QUIZ_DATA = [
    {
        "category": "Từ Vựng - Tiền Tố",
        "question": "Choose the correct prefix for 'formal':",
        "options": [
            "un-",
            "in-",
            "dis-",
            "im-"
        ],
        "answer": 1
    },
    {
        "category": "Từ Vựng - Tiền Tố",
        "question": "Choose the correct prefix for 'satisfied':",
        "options": [
            "un-",
            "in-",
            "dis-",
            "im-"
        ],
        "answer": 2
    },
    {
        "category": "Từ Vựng - Tiền Tố",
        "question": "Choose the correct prefix for 'honest':",
        "options": [
            "un-",
            "in-",
            "dis-",
            "im-"
        ],
        "answer": 2
    },
    {
        "category": "Từ Vựng - Tiền Tố",
        "question": "Choose the correct prefix for 'polite':",
        "options": [
            "un-",
            "in-",
            "dis-",
            "im-"
        ],
        "answer": 3
    },
    {
        "category": "Từ Vựng - Tiền Tố",
        "question": "Choose the correct prefix for 'practical':",
        "options": [
            "un-",
            "in-",
            "dis-",
            "im-"
        ],
        "answer": 3
    },
    {
        "category": "Từ Vựng - Tiền Tố",
        "question": "Choose the correct prefix for 'considerate':",
        "options": [
            "un-",
            "in-",
            "dis-",
            "im-"
        ],
        "answer": 1
    },
    {
        "category": "Từ Vựng - Tiền Tố",
        "question": "Choose the correct prefix for 'friendly':",
        "options": [
            "un-",
            "in-",
            "dis-",
            "im-"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Tiền Tố",
        "question": "Choose the correct prefix for 'efficient':",
        "options": [
            "un-",
            "in-",
            "dis-",
            "im-"
        ],
        "answer": 1
    },
    {
        "category": "Từ Vựng - Tiền Tố",
        "question": "Choose the correct prefix for 'important':",
        "options": [
            "un-",
            "in-",
            "dis-",
            "im-"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Tiền Tố",
        "question": "Choose the correct prefix for 'respectful':",
        "options": [
            "un-",
            "in-",
            "dis-",
            "im-"
        ],
        "answer": 2
    },
    {
        "category": "Từ Vựng - Tiền Tố",
        "question": "Choose the correct prefix for 'patient':",
        "options": [
            "un-",
            "in-",
            "dis-",
            "im-"
        ],
        "answer": 3
    },
    {
        "category": "Từ Vựng - Tiền Tố",
        "question": "Choose the correct prefix for 'appropriate':",
        "options": [
            "un-",
            "in-",
            "dis-",
            "im-"
        ],
        "answer": 1
    },
    {
        "category": "Ngữ Pháp - Từ Loại",
        "question": "He took up that sport for its _______",
        "options": [
            "Popular",
            "Unpopular",
            "Popularize",
            "Popularity"
        ],
        "answer": 3
    },
    {
        "category": "Ngữ Pháp - Từ Loại",
        "question": "The _______ system in this country is rather complex.",
        "options": [
            "Education",
            "Educated",
            "Educating",
            "Educate"
        ],
        "answer": 0
    },
    {
        "category": "Ngữ Pháp - Từ Loại",
        "question": "A _______ diet is one that helps maintain general health.",
        "options": [
            "Health",
            "Unhealthy",
            "Healthy",
            "Healthily"
        ],
        "answer": 2
    },
    {
        "category": "Ngữ Pháp - Từ Loại",
        "question": "_______ is necessary after hard work.",
        "options": [
            "Relaxed",
            "Relaxing",
            "Relaxation",
            "Relax"
        ],
        "answer": 2
    },
    {
        "category": "Ngữ Pháp - Từ Loại",
        "question": "He _______ in at the university.",
        "options": [
            "Specialty",
            "Specializes",
            "Special",
            "Specially"
        ],
        "answer": 1
    },
    {
        "category": "Ngữ Pháp - Từ Loại",
        "question": "NUS is the _______ university of Singapore.",
        "options": [
            "Nation",
            "Nationality",
            "National",
            "Nationally"
        ],
        "answer": 2
    },
    {
        "category": "Ngữ Pháp - Từ Loại",
        "question": "He has a big stamp _______",
        "options": [
            "Collection",
            "Collector",
            "Collect",
            "Collective"
        ],
        "answer": 0
    },
    {
        "category": "Ngữ Pháp - Từ Loại",
        "question": "The patient comes to the hospital in the _______ that he will be cured.",
        "options": [
            "Believe",
            "Belief",
            "Unbelievable",
            "Believable"
        ],
        "answer": 1
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "JUNGLE CAFÉ\nSORRY!\nTables at the front of the café are reserved for a birthday party.",
        "question": "What does it say?",
        "options": [
            "Don't sit at the front of the café unless you're attending the party.",
            "If you're coming to the party you shouldn't use the tables at the front.",
            "The café says 'sorry' because of closing today.",
            "Only people invited to the party can come into the café."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "STUDENTS!\nYOUR $6 DEPOSIT FOR LOCKER KEYS WON'T BE REFUNDED IF KEYS ARE LOST.",
        "question": "What does it say?",
        "options": [
            "Lost locker keys can be replaced for a charge of $6",
            "We cannot return your $6 deposit if you lose your locker key.",
            "You will receive $6 if your locker key is lost",
            "You cannot collect your locker key until you have paid a $6 deposit."
        ],
        "answer": 1
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "Becky,\nDon't forget your Aunt Jane's coming to stay tonight, so can you make sure the house is neat when you go out this afternoon?\nMum",
        "question": "Why is mum writing this note?",
        "options": [
            "To ask Becky to tidy the house before she leaves",
            "To remind Becky to go to her aunt's house",
            "To tell Becky to go out with her aunt Jane",
            "To tell Becky to stay at home to see aunt"
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "Frank, Rabbit Records phoned. The CD you ordered arrived today, but someone sold it. They're really sorry! They've reordered available next Monday at the latest.",
        "question": "Why did the record shop phone?",
        "options": [
            "To apologise for a mistake with Frank's order.",
            "To say that Frank's CD is ready for collection.",
            "The earliest Frank can get his CD is next Monday.",
            "To suggest Frank comes in later this week."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "Market vehicles unload here 07.00-10.00 daily\nCustomer parking allowed at other times.",
        "question": "What does it say?",
        "options": [
            "Customers may park here at times when vehicles are not unloading.",
            "Customers are allowed to park here from 07.00-10.00.",
            "You may unload your vehicle here at any time.",
            "Customers may park outside the market for up to three hours."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "What a fantastic city. We found the restaurant you recommended but it was shut! Menu looks good value, so we'll definitely go before we leave.",
        "question": "What does it say?",
        "options": [
            "Elena and Tim think the restaurant's prices are reasonable.",
            "Elena and Tim have already tried the restaurant.",
            "Elena and Tim have discovered another good restaurant.",
            "Elena and Tim will have to try the restaurant on their next visit."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "To: Sally | From: Kim\nFeeling any better? When you're back at college, remember to register for the films course. Email me if you want any information.",
        "question": "Why has Kim emailed Sally?",
        "options": [
            "To remind her to do something.",
            "To borrow a film from her.",
            "To give her some details.",
            "To let her know that he's ill."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "Mustafa, your brother phones. He's emailed you something to read before you write that letter to the hotel. I said you'd call his mobile number today.\nJean",
        "question": "How should Mustafa reply to his brother?",
        "options": [
            "By phone",
            "By email",
            "By meeting",
            "By letter"
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "HOSPITAL WAITING ROOM\nPLEASE PUT ALL CHILDREN'S TOYS BACK IN THIS ROOM BEFORE YOU LEAVE.",
        "question": "What does it say?",
        "options": [
            "Please don't leave any toys outside this room when you go.",
            "Don't forget to pay for the toys before you leave.",
            "Remember to take your children's toys with you when you leave.",
            "We leave some toys at the back of this room for children."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "Do not use this medicine for more than seven days without your doctor's advice.",
        "question": "What does it say?",
        "options": [
            "Contact your doctor if you wish to continue using this medicine after one week.",
            "You cannot keep this medicine for more than seven days.",
            "Doctors can only supply enough medicine for one week at a time.",
            "You can use this medicine for more than a week."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "SPORTS HALL\nFinal five minutes of bookings must be used to put equipment away.",
        "question": "What does it say?",
        "options": [
            "All the equipments must be put away after booking time (in the final 5 mins).",
            "You have five minutes after bookings have finished to return any sports equipment used.",
            "Bookings now include an extra five minutes for equipment to be put away.",
            "The hall must be cleared of equipment in the five minutes after bookings end."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "NO DIVING ALLOWED EXCEPT AT THE DEEP END OF THE SWIMMING POOL",
        "question": "What does it say?",
        "options": [
            "You must not dive into the pool where the water is shallow.",
            "The water is not deep enough in this poor for you to dive.",
            "Swimming is not permitted where people are diving.",
            "The swimming pool is too deep to swim."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "Patients with appointments ring once and enter. Those with enquiries ring twice and enter.",
        "question": "What does it say?",
        "options": [
            "Ring once if you have an appointment and twice if you don't.",
            "You should ring twice and enter unless you have an enquiry.",
            "If you have an appointment, you don't have to ring.",
            "To make an appointment, ring once and enter."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "CYCLISTS\nWhen this entrance is locked use side gate.",
        "question": "What does it say?",
        "options": [
            "Cyclists should use a different entrance when this one is locked.",
            "The only entrance is the side gate.",
            "If the side gate is locked, go through cycle entrance.",
            "Lock your cycle near this gate before entering."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "Please don't park within 3 metres of this vehicle - space needed for unloading.",
        "question": "What does it say?",
        "options": [
            "You are requested not to park any closer than 3 metres to this vehicle.",
            "This parking space is reserved for the vehicle's owner.",
            "If you want to load things, park beyond 3 metres.",
            "You should not park near here because it is an exit for vehicles."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "$25 RESERVES ANY PICTURES IN THE GALLERY",
        "question": "What does it say?",
        "options": [
            "We will keep any picture for you if you give us $25.",
            "It costs $25 to show your picture in the gallery.",
            "Some of the pictures in the gallery are reserved.",
            "A picture in the gallery costs $25."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "ROOM TO RENT\nUNEXPECTEDLY AVAILABLE so only $250 per month including fuel bills",
        "question": "What does it say?",
        "options": [
            "This rent includes all bills.",
            "The rent for this room is reduced to $250 plus bills.",
            "People renting this room should expect to pay extra for gas and electricity.",
            "This room is cheap to rent as it was not expected to be empty."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "WANTED: KITCHEN ASSISTANTS\nEvening or weekends. Free meals. Full training provided. Apply inside",
        "question": "What does it say?",
        "options": [
            "There are part-time opportunities for people without experience of working in a kitchen.",
            "Only people who are trained in kitchen work should apply for these part-time jobs.",
            "The kitchen assistant will be offered three free meals a day.",
            "We offer cheap meals to people who work part-time in our kitchen."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "BASKETBALL TRAINING\nProfessional coach available for pre-booked groups - 48 hours' notice required.",
        "question": "What does it say?",
        "options": [
            "A basketball coach is available if a booking is made far enough in advance.",
            "Those who want to attend the training group must book in 4 days.",
            "Basketball players are only allowed to practice here if accompanied by a professional coach.",
            "Basketball training for groups is cancelled until further notice."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "This medicine is taken between meals at six-hourly intervals, up to three times daily.",
        "question": "What does it say?",
        "options": [
            "It is essential to wait six hours before having more of this medicine.",
            "It is essential to take this medicine before each meal.",
            "It is essential to take this medicine straight after meals.",
            "It is essential to use this medicine more than three times a day."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "From: Roberto | To: Sam\nSorry I missed you yesterday. I'm not in all next week, but the following Thursday's fine. Why not see if Sven's free as well?",
        "question": "What does it say?",
        "options": [
            "Roberto is suggesting that Sam should invite Sven to their next meeting.",
            "Roberto is suggesting that He will join Sam in a meeting next Thursday.",
            "Roberto will be free the whole next week.",
            "Roberto is suggesting that Sven is unavailable for a meeting next week."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "Once opened, remove any unused soup from the tin and place in the refrigerator.",
        "question": "What does it say?",
        "options": [
            "This label gives advice on how to store the product.",
            "This label gives information on the ingredients of the product.",
            "This label gives advice on how to use the product.",
            "This label gives advice on how to open the product."
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "Nowadays people are more aware that wildlife all over the world is in danger...",
        "question": "Many species of animals could easily become __ if we do not make an effort...",
        "options": [
            "disappeared",
            "lost",
            "extinct",
            "empty"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "Nowadays people are more aware that wildlife all over the world is in danger...",
        "question": "Some birds, __ as parrots are caught alive...",
        "options": [
            "like",
            "such",
            "and",
            "or"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "Nowadays people are more aware that wildlife all over the world is in danger...",
        "question": "More __ is used for farms, for houses or industry...",
        "options": [
            "soil",
            "area",
            "earth",
            "land"
        ],
        "answer": 3
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "Nowadays people are more aware that wildlife all over the world is in danger...",
        "question": "These chemicals pollute __ environment...",
        "options": [
            "a",
            "that",
            "an",
            "the"
        ],
        "answer": 3
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "Nowadays people are more aware that wildlife all over the world is in danger...",
        "question": "Human beings will soon be the only ones left, __ we can solve this problem.",
        "options": [
            "unless",
            "if",
            "however",
            "because"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "In most countries, almost all schools (1)__ private until the early 1800's. At that time, many government leaders...",
        "question": "almost all schools (1)__ private until the early 1800's",
        "options": [
            "have",
            "had",
            "are",
            "were"
        ],
        "answer": 3
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "In most countries, almost all schools (1)__ private until the early 1800's. At that time, many government leaders...",
        "question": "promote national progress by (2)__ education widely available",
        "options": [
            "make",
            "made",
            "making",
            "to make"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "In most countries, almost all schools (1)__ private until the early 1800's. At that time, many government leaders...",
        "question": "differs (3)__ one country to another",
        "options": [
            "about",
            "from",
            "with",
            "at"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "In most countries, almost all schools (1)__ private until the early 1800's. At that time, many government leaders...",
        "question": "a general focus on (4)__ for college",
        "options": [
            "chance",
            "attention",
            "participation",
            "preparation"
        ],
        "answer": 3
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "In most countries, almost all schools (1)__ private until the early 1800's. At that time, many government leaders...",
        "question": "one of the (5)__ sponsors of private schools",
        "options": [
            "largest",
            "much",
            "more",
            "larger"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "If you are invited to someone's house for dinner in the United States, you should (1)__ a gift...",
        "question": "you should (1)__ a gift",
        "options": [
            "take",
            "bring",
            "give",
            "make"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "If you are invited to someone's house for dinner in the United States, you should (1)__ a gift...",
        "question": "shows that the host is excited (2)__ receiving the gift",
        "options": [
            "about",
            "for",
            "with",
            "of"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "If you are invited to someone's house for dinner in the United States, you should (1)__ a gift...",
        "question": "tell a (3)__ lie",
        "options": [
            "white",
            "deliberate",
            "great",
            "obvious"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "If you are invited to someone's house for dinner in the United States, you should (1)__ a gift...",
        "question": "you should not arrive (4)__ on time",
        "options": [
            "slowly",
            "recently",
            "exactly",
            "perfectly"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "If you are invited to someone's house for dinner in the United States, you should (1)__ a gift...",
        "question": "the host may not (5)__ ready.",
        "options": [
            "been",
            "be",
            "being",
            "to be"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "The village of Jukkasjarvi is in Swedish Lapland... In this hotel, you eat, drink and sleep in rooms...",
        "question": "sleep in rooms made (2)__ ice",
        "options": [
            "by",
            "of",
            "within",
            "for"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "The village of Jukkasjarvi is in Swedish Lapland... In this hotel, you eat, drink and sleep in rooms...",
        "question": "you can (3)__ get married in one",
        "options": [
            "even",
            "however",
            "already",
            "yet"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "The village of Jukkasjarvi is in Swedish Lapland... In this hotel, you eat, drink and sleep in rooms...",
        "question": "putting hot drinks on it is obviously not (4)__",
        "options": [
            "supported",
            "recognized",
            "recommended",
            "agreed"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "The village of Jukkasjarvi is in Swedish Lapland... In this hotel, you eat, drink and sleep in rooms...",
        "question": "fortunately guests are (5)__ with special sleeping bags",
        "options": [
            "given",
            "offered",
            "provided",
            "supplied"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "The village of Jukkasjarvi is in Swedish Lapland... In this hotel, you eat, drink and sleep in rooms...",
        "question": "that will keep (6)__ warm",
        "options": [
            "these",
            "those",
            "they",
            "them"
        ],
        "answer": 3
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "The village of Jukkasjarvi is in Swedish Lapland... In this hotel, you eat, drink and sleep in rooms...",
        "question": "(7)__ outdoor clothes can be supplied",
        "options": [
            "suitable",
            "convenient",
            "acceptable",
            "satisfactory"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "The village of Jukkasjarvi is in Swedish Lapland... In this hotel, you eat, drink and sleep in rooms...",
        "question": "six months old (8)__ it melts",
        "options": [
            "although",
            "because",
            "so",
            "while"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "The village of Jukkasjarvi is in Swedish Lapland... In this hotel, you eat, drink and sleep in rooms...",
        "question": "and (9)__ winter it is rebuilt",
        "options": [
            "other",
            "any",
            "each",
            "another"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "The village of Jukkasjarvi is in Swedish Lapland... In this hotel, you eat, drink and sleep in rooms...",
        "question": "Creating the hotel (10)__ 10,000 tons of ice",
        "options": [
            "brings",
            "puts",
            "fetches",
            "takes"
        ],
        "answer": 3
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "Henry Ford was born on a farm in Michigan in 1863 but he did not like farming...",
        "question": "After he (1)__ driven it 1,500 kilometers",
        "options": [
            "is",
            "was",
            "had",
            "has"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "Henry Ford was born on a farm in Michigan in 1863 but he did not like farming...",
        "question": "in 1903, he (2)__ the Ford Motor Company.",
        "options": [
            "raised",
            "started",
            "led",
            "appeared"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "Henry Ford was born on a farm in Michigan in 1863 but he did not like farming...",
        "question": "By (3)__ strong but light steel",
        "options": [
            "putting",
            "operating",
            "using",
            "managing"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "Henry Ford was born on a farm in Michigan in 1863 but he did not like farming...",
        "question": "built cheap cars for (4)__ people to buy.",
        "options": [
            "usual",
            "ordinary",
            "general",
            "typical"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "Henry Ford was born on a farm in Michigan in 1863 but he did not like farming...",
        "question": "built the first Ford Model 'T', (5)__ sold for $825.",
        "options": [
            "where",
            "which",
            "who",
            "what"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "Henry Ford was born on a farm in Michigan in 1863 but he did not like farming...",
        "question": "He was soon selling 100 cars (6)__ day.",
        "options": [
            "a",
            "some",
            "the",
            "one"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "Henry Ford was born on a farm in Michigan in 1863 but he did not like farming...",
        "question": "the Ford Motor Company was (7)__ $700 million.",
        "options": [
            "rich",
            "worth",
            "expensive",
            "dear"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "Henry Ford was born on a farm in Michigan in 1863 but he did not like farming...",
        "question": "but (8)__ things simple",
        "options": [
            "remaining",
            "staying",
            "keeping",
            "holding"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "Henry Ford was born on a farm in Michigan in 1863 but he did not like farming...",
        "question": "sometimes (9)__ less choice.",
        "options": [
            "meant",
            "decided",
            "planned",
            "intended"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "Henry Ford was born on a farm in Michigan in 1863 but he did not like farming...",
        "question": "'You (10)__ have any color you like,' said Henry Ford",
        "options": [
            "will",
            "ought",
            "need",
            "can"
        ],
        "answer": 3
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Two years ago, our 14-year-old son, Ben, asked us for a set of drums for his birthday. At first, we were very much against the idea because of the noise...",
        "question": "Ben asked his parents for a drum when he was:",
        "options": [
            "14 years old",
            "12 years old",
            "2 years old",
            "16 years old"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Two years ago, our 14-year-old son, Ben, asked us for a set of drums for his birthday. At first, we were very much against the idea because of the noise...",
        "question": "His parents disagreed at first because:",
        "options": [
            "it was expensive",
            "it was noisy",
            "they prefer computer",
            "it was dangerous"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Two years ago, our 14-year-old son, Ben, asked us for a set of drums for his birthday. At first, we were very much against the idea because of the noise...",
        "question": "Ben started playing music with:",
        "options": [
            "his friends/band members",
            "himself",
            "his neighbors",
            "his parents"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Two years ago, our 14-year-old son, Ben, asked us for a set of drums for his birthday. At first, we were very much against the idea because of the noise...",
        "question": "They play / practice at:",
        "options": [
            "outside",
            "at Ben's house",
            "at Ben's friends' house",
            "at the park"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Two years ago, our 14-year-old son, Ben, asked us for a set of drums for his birthday. At first, we were very much against the idea because of the noise...",
        "question": "When the band starts practicing, Ben's parents:",
        "options": [
            "go for a long walk",
            "go to sleep",
            "go shopping",
            "stay and listen"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Two years ago, our 14-year-old son, Ben, asked us for a set of drums for his birthday. At first, we were very much against the idea because of the noise...",
        "question": "Ben's parents think his friends are:",
        "options": [
            "rude",
            "stubborn",
            "well-behaved (friendly and polite)",
            "annoying"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Two years ago, our 14-year-old son, Ben, asked us for a set of drums for his birthday. At first, we were very much against the idea because of the noise...",
        "question": "The writer is worried because:",
        "options": [
            "the children may quit school",
            "the children won't spend enough time on school work",
            "the children are bored",
            "they make too much noise"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Two years ago, our 14-year-old son, Ben, asked us for a set of drums for his birthday. At first, we were very much against the idea because of the noise...",
        "question": "The writer thinks that:",
        "options": [
            "Ben should not have joined the band",
            "Ben's decision to play music has kept him out of trouble",
            "Ben should study more",
            "Ben should sell the drums"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Two years ago, our 14-year-old son, Ben, asked us for a set of drums for his birthday. At first, we were very much against the idea because of the noise...",
        "question": "What is the writer trying to do in this text?",
        "options": [
            "describe her son's hobby",
            "give advice to teenagers",
            "complain about her son's friends",
            "compare herself with her parents"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Student Volunteers Needed! On Saturday, December 12th, from 10 A.M. until 4 P.M., Carverton Middle School will be holding a music festival...",
        "question": "What time will the festival begin?",
        "options": [
            "10 A.M.",
            "11 A.M.",
            "1 P.M.",
            "2 P.M."
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Student Volunteers Needed! On Saturday, December 12th, from 10 A.M. until 4 P.M., Carverton Middle School will be holding a music festival...",
        "question": "The word 'feature' is closest in meaning to",
        "options": [
            "look",
            "keep",
            "include",
            "entertain"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Student Volunteers Needed! On Saturday, December 12th, from 10 A.M. until 4 P.M., Carverton Middle School will be holding a music festival...",
        "question": "What job will be done the day before the festival begins?",
        "options": [
            "Making posters",
            "Setting up the gym",
            "Cleaning up the gym",
            "Helping the performers"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Student Volunteers Needed! On Saturday, December 12th, from 10 A.M. until 4 P.M., Carverton Middle School will be holding a music festival...",
        "question": "Who is told to talk to Ms. Braxton?",
        "options": [
            "Parents",
            "Students",
            "Teachers",
            "Performers"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "When the spring semester began, students at Eastern High School were met by a new science teacher. Her name is Elaine Burgess...",
        "question": "Which headline best summarizes the article?",
        "options": [
            "Science Classes to Features Hands-on Learning",
            "A Chat with the New Science Teacher",
            "The Education of Elaine Burgess",
            "Science Class: Does Anyone Enjoy it?"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "When the spring semester began, students at Eastern High School were met by a new science teacher. Her name is Elaine Burgess...",
        "question": "Based on the article, what is The Quill and Paper?",
        "options": [
            "It is read by every student.",
            "It is a new textbook.",
            "It was written by Ms. Burgess.",
            "It is the name of a newspaper."
        ],
        "answer": 3
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "When the spring semester began, students at Eastern High School were met by a new science teacher. Her name is Elaine Burgess...",
        "question": "Which statement does paragraph 2 support?",
        "options": [
            "This is the second teaching job for Ms. Burgess.",
            "Ms. Burgess has been a teacher for six months.",
            "Ms. Burgess was a professor at Sanderson University.",
            "Ms. Burgess focused on science as an undergraduate."
        ],
        "answer": 3
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "When the spring semester began, students at Eastern High School were met by a new science teacher. Her name is Elaine Burgess...",
        "question": "What does the author point out regarding Ms. Burgess's hope of sparking students' interest?",
        "options": [
            "Too many students have little scientific knowledge.",
            "She wants students to be curious about science.",
            "Science is one of the hardest subjects to learn.",
            "Some experiments can be dangerous for students to do."
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "When the spring semester began, students at Eastern High School were met by a new science teacher. Her name is Elaine Burgess...",
        "question": "What can be inferred about Ms. Burgess?",
        "options": [
            "Some of her students know more about science than her.",
            "Her grades in graduate school were high.",
            "She expects her students to speak in class.",
            "The subject she knows the least is biology."
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Kal Kaur Rai has always been interested in fashion and has just won the title of Young Achiever of the Year...",
        "question": "What is the writer trying to do in the text?",
        "options": [
            "encourage fashion designers to make better business plans",
            "compare a job in fashion with other choices of career",
            "give details of recent changes in the fashion industry",
            "explain how a woman set up a fashion business"
        ],
        "answer": 3
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Kal Kaur Rai has always been interested in fashion and has just won the title of Young Achiever of the Year...",
        "question": "What does the reader learn about Kal's parents?",
        "options": [
            "They wanted Kal to help them run the family business.",
            "They did not realise that Kal wanted to work in fashion.",
            "They insisted Kal should continue with her job in advertising.",
            "They did not think Kal worked hard enough at university."
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Kal Kaur Rai has always been interested in fashion and has just won the title of Young Achiever of the Year...",
        "question": "Kal decided to borrow £20,000 when",
        "options": [
            "all her clothes in the London shop were sold.",
            "her friends asked her to make clothes for them.",
            "she lost her job at the advertising agency.",
            "the fashion industry was in a period of growth."
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Kal Kaur Rai has always been interested in fashion and has just won the title of Young Achiever of the Year...",
        "question": "What does Kal say about her career?",
        "options": [
            "She plans to open more stores.",
            "She believes that she deserves her success.",
            "She particularly enjoys designing for famous people.",
            "She expects more people to buy her clothes after the award."
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Dear Students, I invite you to explore Philips Exeter Academy through this website...",
        "question": "What is the purpose of the letter?",
        "options": [
            "To introduce the school website",
            "To explain Harkness learning fashion",
            "To list all the courses offered",
            "To show the colorful student life"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Dear Students, I invite you to explore Philips Exeter Academy through this website...",
        "question": "The word 'involved' is closest in meaning to",
        "options": [
            "Busy",
            "Diligent",
            "Relevant",
            "Serious"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Dear Students, I invite you to explore Philips Exeter Academy through this website...",
        "question": "What can NOT be inferred about the Harkness tables?",
        "options": [
            "They are located at the center of every class.",
            "They are not real tables, but just a figurative expression.",
            "The Harkness tables are oval and can seat more than 10 people.",
            "Students and teachers can talk and discuss at the Harkness tables."
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Dear Students, I invite you to explore Philips Exeter Academy through this website...",
        "question": "Which of the following items is NOT for the new or prospective students?",
        "options": [
            "Admissions",
            "Academics",
            "Student life",
            "Parent 'gateway'"
        ],
        "answer": 3
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Dear Students, I invite you to explore Philips Exeter Academy through this website...",
        "question": "What can be inferred about the Parent 'gateway'?",
        "options": [
            "New or prospective students can check information under this item.",
            "It is located at the top of the website page.",
            "It provides parents with detail information about the school.",
            "It will not be updated until the parents have new questions."
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "At 32, I have just finished my first year at university. As well as attending lectures regularly...",
        "question": "What is the writer trying to do in the text?",
        "options": [
            "help lecturers understand older students",
            "explain her reasons for returning to study",
            "suggest some good methods for studying",
            "complain about the attitude of young students"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "At 32, I have just finished my first year at university. As well as attending lectures regularly...",
        "question": "What can a reader find out about the writer from this text?",
        "options": [
            "when she left school",
            "how long her university course is",
            "where she will work in future",
            "what subject she is studying"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "At 32, I have just finished my first year at university. As well as attending lectures regularly...",
        "question": "How did the writer feel about her job as a secretary?",
        "options": [
            "Her salary wasn't good enough.",
            "It gave her the opportunity to study.",
            "It didn't make use of her brain.",
            "Her colleagues made her depressed."
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "At 32, I have just finished my first year at university. As well as attending lectures regularly...",
        "question": "In her spare time, the writer likes to",
        "options": [
            "go out to parties.",
            "earn some money.",
            "travel a lot.",
            "do extra study."
        ],
        "answer": 3
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "At 32, I have just finished my first year at university. As well as attending lectures regularly...",
        "question": "Which of these sentences describes the writer?",
        "options": [
            "She realizes the value of a university degree.",
            "She gets on well with the other students.",
            "She is confident about the future.",
            "She finds university life easier than she expected."
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Dear students: This year, we plan to take at least two field trips per semester. Please be aware of the following...",
        "question": "What is the purpose of the notice?",
        "options": [
            "To inform the students about an upcoming field trip",
            "To let the students know about some forms they must submit",
            "To advise students on some punishments they may receive",
            "To ask for the students' opinions on where to take field trips"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Dear students: This year, we plan to take at least two field trips per semester. Please be aware of the following...",
        "question": "The word 'consents' is closest in meaning to",
        "options": [
            "Responds",
            "Agrees",
            "Stresses",
            "Obtains"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Dear students: This year, we plan to take at least two field trips per semester. Please be aware of the following...",
        "question": "The word 'it' refers to",
        "options": [
            "Injury",
            "A field trip",
            "This proof",
            "The front office"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Dear students: This year, we plan to take at least two field trips per semester. Please be aware of the following...",
        "question": "What will happens to students who misbehave while on field trips?",
        "options": [
            "They will not be allowed to go on future trips",
            "They will be punished in some way",
            "They will have to apologize to the teacher",
            "They will be forced to pay a fine"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "One day I hopped in a taxi and we took off for the airport... The driver of the black car whipped his head around and started yelling...",
        "question": "Which title best expresses the main idea of the story?",
        "options": [
            "A weird taxi driver",
            "The law of the garbage truck",
            "A trip to the airport",
            "Waving to people friendly"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "One day I hopped in a taxi and we took off for the airport... The driver of the black car whipped his head around and started yelling...",
        "question": "The word 'hopped' is closest in meaning to",
        "options": [
            "Jumped",
            "Flied",
            "Walked",
            "Lingered"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "One day I hopped in a taxi and we took off for the airport... The driver of the black car whipped his head around and started yelling...",
        "question": "According to the author, what is NOT in the garbage truck?",
        "options": [
            "Happiness",
            "Anger",
            "Frustration",
            "Disappointment"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "One day I hopped in a taxi and we took off for the airport... The driver of the black car whipped his head around and started yelling...",
        "question": "What does the author suggest by telling the story?",
        "options": [
            "We shouldn't take a taxi to the airport",
            "It is not right to whip one's head around and yell at others",
            "We should not pile up too much garbage in our truck",
            "We should love the people who treat us right and pray for the ones who don't"
        ],
        "answer": 3
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "One day I hopped in a taxi and we took off for the airport... The driver of the black car whipped his head around and started yelling...",
        "question": "The word 'They' refers to",
        "options": [
            "Taxis",
            "Taxi drivers",
            "Many people",
            "The taxi driver and I"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Please read the following carefully as it describes my expectations of your during this class...",
        "question": "What is the note mainly about?",
        "options": [
            "The teacher's expectations for the students in class",
            "How the students can get a high grade from the teacher",
            "The type of homework the students will have to do",
            "What the teacher's grading style for the class is"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Please read the following carefully as it describes my expectations of your during this class...",
        "question": "Which of the following is NOT mentioned in the note about something that the students will be graded on?",
        "options": [
            "Homework assignments",
            "Attendance",
            "Tests",
            "Class participation"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Please read the following carefully as it describes my expectations of your during this class...",
        "question": "The word 'inquiries' is closest in meaning to",
        "options": [
            "Investigations",
            "Demands",
            "Examinations",
            "Questions"
        ],
        "answer": 3
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Please read the following carefully as it describes my expectations of your during this class...",
        "question": "The word 'confess' is closest in meaning to",
        "options": [
            "Blame",
            "Admit",
            "Decide",
            "Falsify"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Mankind has used flags for over 4,000 years. The first flags were simply wooden poles...",
        "question": "According to the passage, when did the flag have its current appearance?",
        "options": [
            "Over 4,000 years ago",
            "About 2,000 years ago",
            "When Russia had its flag",
            "When Yugoslavia had its flag"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Mankind has used flags for over 4,000 years. The first flags were simply wooden poles...",
        "question": "What fact does the author say about the first known flag?",
        "options": [
            "They were originated in Russia",
            "They existed over 4,000 years ago.",
            "They were a symbol of courage.",
            "They were completed with a pole and fabric."
        ],
        "answer": 3
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Mankind has used flags for over 4,000 years. The first flags were simply wooden poles...",
        "question": "According to the passage, what is the color of the top stripe on the flag of Yugoslavia?",
        "options": [
            "White",
            "Red",
            "Blue",
            "Green"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Mankind has used flags for over 4,000 years. The first flags were simply wooden poles...",
        "question": "According to the passage, what does the color red symbolize?",
        "options": [
            "Death",
            "Power",
            "Peace",
            "Courage"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Mankind has used flags for over 4,000 years. The first flags were simply wooden poles...",
        "question": "According to the passage, what color is NOT often used on flags of countries?",
        "options": [
            "Black",
            "Green",
            "Pink",
            "Orange"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Rebecca Stevens was the first woman to climb Mount Everest...",
        "question": "Before Rebecca climbed Everest, she worked for",
        "options": [
            "A bookshop",
            "A newspaper (journalist)",
            "A travel agent"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Rebecca Stevens was the first woman to climb Mount Everest...",
        "question": "Rebecca went to Everest",
        "options": [
            "With her family",
            "With a climbing group",
            "Without anyone"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Rebecca Stevens was the first woman to climb Mount Everest...",
        "question": "Rebecca didn't take much luggage because she",
        "options": [
            "Didn't have many things",
            "Had a bad back",
            "Had to carry it herself"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Rebecca Stevens was the first woman to climb Mount Everest...",
        "question": "Rebecca didn't wash on Everest because",
        "options": [
            "It was too cold.",
            "There was not enough water.",
            "She is a dirty person."
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Rebecca Stevens was the first woman to climb Mount Everest...",
        "question": "Rebecca carried water for",
        "options": [
            "Drinking",
            "Cooking",
            "Cleaning her teeth"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Rebecca Stevens was the first woman to climb Mount Everest...",
        "question": "Rebecca became famous when she",
        "options": [
            "Got to the highest place in the world.",
            "Wrote a book about her trip.",
            "Was on a television program."
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Rebecca Stevens was the first woman to climb Mount Everest...",
        "question": "After her trip, Rebecca",
        "options": [
            "Earned the same money.",
            "Stayed in the same flat",
            "Did the same job"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Orbis is an organization which helps blind people everywhere...",
        "question": "What is the writer's main purpose in writing this text?",
        "options": [
            "to describe a dangerous trip.",
            "to report a patient's cure.",
            "to explain how sight can be lost.",
            "to warn against playing with sticks."
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Orbis is an organization which helps blind people everywhere...",
        "question": "What can a reader learn about in this text?",
        "options": [
            "the life of schoolchildren in Mongolia.",
            "the difficulties for blind travelers.",
            "the international work of some eye doctors.",
            "the best way of studying medicine."
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Orbis is an organization which helps blind people everywhere...",
        "question": "After meeting Eukhtuul, Samantha felt",
        "options": [
            "grateful for her own sight.",
            "proud of the doctor's skill.",
            "surprised by Eukhtuul's courage.",
            "angry about Eukhtuul's experience."
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Orbis is an organization which helps blind people everywhere...",
        "question": "What is the result of Eukhtuul's operation?",
        "options": [
            "She can already see perfectly again.",
            "After some time she will see as well as before.",
            "She can see better but will never have normal eyes.",
            "Before she recovers, she will need another operation."
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Orbis is an organization which helps blind people everywhere...",
        "question": "Which is the postcard Samantha wrote to an English friend?",
        "options": [
            "I've visited a Mongolian hospital...",
            "You may have to fly a long way...",
            "I'm staying with my friend Eukhtuul...",
            "Make sure you take care of your eyes because they're more valuable than you realize!"
        ],
        "answer": 3
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "In 2006, Ravi Patra started working for a music company...",
        "question": "What was the first job Ravi wanted to have when he was younger?",
        "options": [
            "Footballer",
            "Pilot",
            "Singer"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "In 2006, Ravi Patra started working for a music company...",
        "question": "What did Ravi's boss at Rock TV say about him?",
        "options": [
            "Ravi asked for a job at Rock TV more than once.",
            "There were other people better than Ravi.",
            "Ravi showed him how much he wanted the job."
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "In 2006, Ravi Patra started working for a music company...",
        "question": "How has Ravi's work changed?",
        "options": [
            "He no longer begins very early.",
            "He is busier than before.",
            "He doesn't stay late at the office."
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "In 2006, Ravi Patra started working for a music company...",
        "question": "In the morning, Ravi often",
        "options": [
            "Works on Rock TV advertisements.",
            "Meets important people at his office.",
            "Decides what to say on his program (writes his words)."
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "In 2006, Ravi Patra started working for a music company...",
        "question": "What does Ravi think is the most important thing about the show?",
        "options": [
            "It has lots of interesting stars.",
            "There is great music.",
            "His is popular with the guests."
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "In 2006, Ravi Patra started working for a music company...",
        "question": "What problem does Ravi sometimes have on the Rock TV show?",
        "options": [
            "He forgets people's names.",
            "He cannot stop laughing.",
            "His questions make people angry."
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "In 2006, Ravi Patra started working for a music company...",
        "question": "Ravi would like to spend more time",
        "options": [
            "In the mountains.",
            "With his friends",
            "Listening to music"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "She was still at primary school when she decided she wanted to travel. So when she was eleven...",
        "question": "What did she want to do when she was a pupil?",
        "options": [
            "Travel",
            "Become a singer",
            "Become an artist"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "She was still at primary school when she decided she wanted to travel. So when she was eleven...",
        "question": "What did she decide to do at the age of 11?",
        "options": [
            "Cycle",
            "Ride a motorbike",
            "Swim"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "She was still at primary school when she decided she wanted to travel. So when she was eleven...",
        "question": "What did she like best when she was at secondary school?",
        "options": [
            "Cycling to school",
            "Learning math",
            "Playing on the school ground"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "She was still at primary school when she decided she wanted to travel. So when she was eleven...",
        "question": "When did she finish secondary school?",
        "options": [
            "At the age of 10",
            "At the age of 11",
            "At the age of 16"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "She was still at primary school when she decided she wanted to travel. So when she was eleven...",
        "question": "Why did she start a business?",
        "options": [
            "Because she liked money.",
            "Because she hated studying",
            "Because she loved cooking"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "She was still at primary school when she decided she wanted to travel. So when she was eleven...",
        "question": "How many courses were there in her meal at first?",
        "options": [
            "2",
            "3",
            "4"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "She was still at primary school when she decided she wanted to travel. So when she was eleven...",
        "question": "Why did she have so many interesting experiences?",
        "options": [
            "Because she travelled a lot",
            "Because she read a lot",
            "Because she usually watched TV"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "She was still at primary school when she decided she wanted to travel. So when she was eleven...",
        "question": "What desert has she been to?",
        "options": [
            "Himalayan",
            "Nepal",
            "Moroccan"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "She was still at primary school when she decided she wanted to travel. So when she was eleven...",
        "question": "Why didn't she go to Egypt?",
        "options": [
            "Because a war started when she was in Turkey.",
            "Because she was sick.",
            "Because she didn't have time."
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "She was still at primary school when she decided she wanted to travel. So when she was eleven...",
        "question": "Who did she travel with?",
        "options": [
            "Her mother",
            "Her friends",
            "all of the above"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "She was still at primary school when she decided she wanted to travel. So when she was eleven...",
        "question": "What problem did she have in 1997?",
        "options": [
            "She had pain in her knee",
            "She had pain in her back",
            "She had pain in her legs"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "She was still at primary school when she decided she wanted to travel. So when she was eleven...",
        "question": "How many books has he written?",
        "options": [
            "2",
            "4",
            "5"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "She was still at primary school when she decided she wanted to travel. So when she was eleven...",
        "question": "How is she going to travel in New Zealand?",
        "options": [
            "by motorbike",
            "by car",
            "by bike"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "While Western medicine is common throughout the world, it is not the only type of medicine that people practice...",
        "question": "What is the best title for the passage?",
        "options": [
            "A New Type of Medicine",
            "All about Acupuncture",
            "Western Medicine vs. Acupuncture",
            "Acupuncture: Does It Work?"
        ],
        "answer": 3
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "While Western medicine is common throughout the world, it is not the only type of medicine that people practice...",
        "question": "What does the author imply about acupuncture?",
        "options": [
            "Its origins are not precisely known.",
            "Some Western doctors use it.",
            "It costs less than Western medicine.",
            "The needles used vary in size."
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "While Western medicine is common throughout the world, it is not the only type of medicine that people practice...",
        "question": "Which of the following statements does paragraph 1 support?",
        "options": [
            "The needles used can sometimes hurt the patients.",
            "Most of the needles are inserted in the patient's back.",
            "Acupuncturists use more than one needle at one time.",
            "Most acupuncture is used to treat fatal diseases."
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "While Western medicine is common throughout the world, it is not the only type of medicine that people practice...",
        "question": "Where is acupuncture becoming practiced more often?",
        "options": [
            "In Asia",
            "In Australia",
            "In Africa",
            "In Europe (and North America)"
        ],
        "answer": 3
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "While Western medicine is common throughout the world, it is not the only type of medicine that people practice...",
        "question": "The word 'ineffective' is closest in meaning to",
        "options": [
            "Useless",
            "Doubtful",
            "Abnormal",
            "Fraudulent"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Dear Thomas, I am curious as to whether or not you are still planning to go on that skiing trip...",
        "question": "Why did the author write this letter?",
        "options": [
            "To describe her winter plans",
            "To describe an upcoming art exhibit",
            "To recommend a special program",
            "To compliment the local college"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Dear Thomas, I am curious as to whether or not you are still planning to go on that skiing trip...",
        "question": "What does the author indicate about Thomas' plans for winter vacation?",
        "options": [
            "He's going to take some art classes.",
            "He will go on a trip with his family.",
            "He will learn how to ski at a resort.",
            "He is going to travel abroad somewhere."
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Dear Thomas, I am curious as to whether or not you are still planning to go on that skiing trip...",
        "question": "What can be inferred from the letter about Westfield State University?",
        "options": [
            "It is one of the top schools in the state.",
            "It is located near the home of the author.",
            "It offers several programs during winter.",
            "High school students can take regular classes there."
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Dear Thomas, I am curious as to whether or not you are still planning to go on that skiing trip...",
        "question": "Which of the following is NOT mentioned about the seminar?",
        "options": [
            "Where it is going to be",
            "How long it is going to last",
            "How many students may take it",
            "What is going to be taught"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "Dear Thomas, I am curious as to whether or not you are still planning to go on that skiing trip...",
        "question": "According to the letter, how can a student get into the seminar?",
        "options": [
            "By applying online",
            "By getting recommended by a teacher",
            "By sending in a work of art",
            "By paying an entrance fee"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "The dogsled race was about to begin. Julie's team of dogs was lined up...",
        "question": "The author wrote the story in order to",
        "options": [
            "Describe how dogs stay warm in cold weather",
            "Tell a story about a dogsled race",
            "Explain how cold it can be in winter",
            "Entertain the reader with funny stories about dogs"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "The dogsled race was about to begin. Julie's team of dogs was lined up...",
        "question": "Where does the dogsled race take place?",
        "options": [
            "In Antarctica",
            "On a track",
            "In Alaska",
            "In a field"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "The dogsled race was about to begin. Julie's team of dogs was lined up...",
        "question": "What is the word 'yelled' in paragraph 1 closest in meaning to?",
        "options": [
            "Shouted",
            "Said",
            "Told",
            "whispered"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "The dogsled race was about to begin. Julie's team of dogs was lined up...",
        "question": "What happened before the gods began running?",
        "options": [
            "The dogs pulled the sled slowly.",
            "Julie and the dogs were lined up at the starting gate.",
            "A runner on Julie's sled broke.",
            "The dogs pulled the sled over hills and into valleys."
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "The dogsled race was about to begin. Julie's team of dogs was lined up...",
        "question": "What does the word 'team' in paragraph 1 refer to?",
        "options": [
            "Friends and family",
            "To join together",
            "Many dogs",
            "A group working together"
        ],
        "answer": 3
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "The dogsled race was about to begin. Julie's team of dogs was lined up...",
        "question": "Why did the dogs wear special booties?",
        "options": [
            "To be well recognized",
            "Because the booties fit their feet",
            "To protect their feet from ice",
            "To keep their feet warm"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "The dogsled race was about to begin. Julie's team of dogs was lined up...",
        "question": "Why don't the dogs freeze in the cold weather?",
        "options": [
            "Julie puts special booties on their feet.",
            "They sleep by the fire at night.",
            "Their thick fur coats keep them warm.",
            "It doesn't get very cold in Alaska."
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "The dogsled race was about to begin. Julie's team of dogs was lined up...",
        "question": "What does the word 'they' in paragraph 3 refer to?",
        "options": [
            "The dogs",
            "The other racers",
            "Runners",
            "Julie and her team"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "The dogsled race was about to begin. Julie's team of dogs was lined up...",
        "question": "The word 'thick' in paragraph 3 is closest in meaning to",
        "options": [
            "Fat",
            "Fat",
            "Thin",
            "Skinny"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "The dogsled race was about to begin. Julie's team of dogs was lined up...",
        "question": "What kind of person is Julie?",
        "options": [
            "Brave and determined",
            "Timid and hesitant",
            "Interesting and careful",
            "Boring and careless"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "It's that time of the year for school to start again. So that means you need to start stocking up on the supplies...",
        "question": "Which headline best summarizes the advertisement?",
        "options": [
            "Big Sale at Carter's Department Store",
            "Are You Ready for School?",
            "Lets Go Shopping at Carter's",
            "Carter's: the Newest Store in Town"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "It's that time of the year for school to start again. So that means you need to start stocking up on the supplies...",
        "question": "The phrase 'stocking up on' is closest in meaning to",
        "options": [
            "Utilizing",
            "Considering",
            "Purchasing",
            "Saving"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "It's that time of the year for school to start again. So that means you need to start stocking up on the supplies...",
        "question": "The author uses paint, paintbrushes and easels as exam",
        "options": [
            "Supplies that all students need",
            "Items selling for more than half off",
            "Some of the store's newest items",
            "Art supplies available at the store"
        ],
        "answer": 3
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "It's that time of the year for school to start again. So that means you need to start stocking up on the supplies...",
        "question": "What is the discount on a notebook computer?",
        "options": [
            "20%",
            "30%",
            "40%",
            "60%"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "It's that time of the year for school to start again. So that means you need to start stocking up on the supplies...",
        "question": "The word 'whopping' is closest in meaning to",
        "options": [
            "Surprising",
            "Unlikely",
            "Reduced",
            "enormous"
        ],
        "answer": 3
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "Jann Mardenborough has loved cars since he was given a toy one as a baby...",
        "question": "When he was a child, workers at the kart centre said Jann was a good driver.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "Jann Mardenborough has loved cars since he was given a toy one as a baby...",
        "question": "Jann stopped racing karts because he became bored with it.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "Jann Mardenborough has loved cars since he was given a toy one as a baby...",
        "question": "Jann was good at computer racing games immediately.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "Jann Mardenborough has loved cars since he was given a toy one as a baby...",
        "question": "Jann played computer racing games with school friends.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "Jann Mardenborough has loved cars since he was given a toy one as a baby...",
        "question": "Jann told his parents about the computer competition after it ended.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "Jann Mardenborough has loved cars since he was given a toy one as a baby...",
        "question": "The people Jann raced against were from different countries.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "Jann Mardenborough has loved cars since he was given a toy one as a baby...",
        "question": "Jann's parents had to pay for his driving course.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "Every year, thousands of people come to Edinburgh, the capital city of Scotland, to be part of the Edinburgh Festival...",
        "question": "The Edinburgh Festival Is a month long.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "Every year, thousands of people come to Edinburgh, the capital city of Scotland, to be part of the Edinburgh Festival...",
        "question": "Edinburgh Festival is in October.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "Every year, thousands of people come to Edinburgh, the capital city of Scotland, to be part of the Edinburgh Festival...",
        "question": "Actors come to the Edinburgh Festival from lots of different countries.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "Every year, thousands of people come to Edinburgh, the capital city of Scotland, to be part of the Edinburgh Festival...",
        "question": "You can hear music all day.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "Every year, thousands of people come to Edinburgh, the capital city of Scotland, to be part of the Edinburgh Festival...",
        "question": "More than ten thousand students come to the Edinburgh Festival every year.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "Every year, thousands of people come to Edinburgh, the capital city of Scotland, to be part of the Edinburgh Festival...",
        "question": "It is expensive to go to the theatre in Edinburgh.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "Every year, thousands of people come to Edinburgh, the capital city of Scotland, to be part of the Edinburgh Festival...",
        "question": "It is usually more difficult to see famous actors in London than in Edinburgh.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "Most house burglaries happen between 2 p.m. and 6 p.m., say the police...",
        "question": "The number of house burglaries is the same as last year.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "Most house burglaries happen between 2 p.m. and 6 p.m., say the police...",
        "question": "Most burglars are men.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "Most house burglaries happen between 2 p.m. and 6 p.m., say the police...",
        "question": "People sometimes make things easy for burglars.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "Most house burglaries happen between 2 p.m. and 6 p.m., say the police...",
        "question": "The summer is more difficult for burglars.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "Most house burglaries happen between 2 p.m. and 6 p.m., say the police...",
        "question": "Burglars don't usually go to houses with lights on.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "Most house burglaries happen between 2 p.m. and 6 p.m., say the police...",
        "question": "Burglars usually drive cars.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "Most house burglaries happen between 2 p.m. and 6 p.m., say the police...",
        "question": "You have to pay for information from the police.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "Nick Barlow loves his work. He's a British actor and he travels around the world making TV programmes...",
        "question": "Nick says that people in the places he visits are very friendly.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "Nick Barlow loves his work. He's a British actor and he travels around the world making TV programmes...",
        "question": "Nick buys something to take home from every country he visits.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "Nick Barlow loves his work. He's a British actor and he travels around the world making TV programmes...",
        "question": "On some trips, Nick travels alone.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "Nick Barlow loves his work. He's a British actor and he travels around the world making TV programmes...",
        "question": "There are often problems with the television cameras.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "Nick Barlow loves his work. He's a British actor and he travels around the world making TV programmes...",
        "question": "Every time Nick goes away, he packs something to read.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "Nick Barlow loves his work. He's a British actor and he travels around the world making TV programmes...",
        "question": "Helen is unhappy when he's away from home.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "Nick Barlow loves his work. He's a British actor and he travels around the world making TV programmes...",
        "question": "When Helen was sick, Nick returned home.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "David Johnson has loved swimming all his life...",
        "question": "David Johnson had problems during a swimming competition in the USA.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "David Johnson has loved swimming all his life...",
        "question": "After 1983, many people swam between Santa Cruz Island and the Californian coast.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "David Johnson has loved swimming all his life...",
        "question": "In January 2004, David was the first person of his age to swim across the Cook Strait.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "David Johnson has loved swimming all his life...",
        "question": "David practiced for more than a year to swim across the Cook Strait.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "David Johnson has loved swimming all his life...",
        "question": "David was in New Zealand for a long time before he swam across the Cook Strait.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "David Johnson has loved swimming all his life...",
        "question": "David's wife was in the boat beside him when he swam the Cook Strait.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (T/F/DS)",
        "passage": "David Johnson has loved swimming all his life...",
        "question": "David had to stop for a short time while swimming the Cook Strait.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 1
    }
]

# Danh sách các thể loại
categories = ["Tất cả"] + list(dict.fromkeys([q["category"] for q in QUIZ_DATA]))

# Giao diện Sidebar để lọc
st.sidebar.title("⚙️ Cài đặt ôn tập")
selected_category = st.sidebar.selectbox("Chọn thể loại bài tập:", categories)

# Quản lý Session State
if "selected_category" not in st.session_state:
    st.session_state.selected_category = "Tất cả"
if "current_idx" not in st.session_state:
    st.session_state.current_idx = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}

# Reset tiến trình nếu người dùng đổi thể loại bài tập
if selected_category != st.session_state.selected_category:
    st.session_state.selected_category = selected_category
    st.session_state.current_idx = 0
    st.session_state.score = 0
    st.session_state.user_answers = {}
    st.rerun()

# Lọc câu hỏi theo thể loại
if st.session_state.selected_category == "Tất cả":
    current_quiz_data = QUIZ_DATA
else:
    current_quiz_data = [q for q in QUIZ_DATA if q["category"] == st.session_state.selected_category]


st.title("📚 Ôn Tập Tiếng Anh EHOU")
st.caption(f"Ngân hàng {len(QUIZ_DATA)} câu hỏi tổng hợp từ 13 tệp (Đã bổ sung 30 bài Đọc Hiểu)")

total_q = len(current_quiz_data)

# Kiểm tra nếu có dữ liệu
if total_q == 0:
    st.warning("Không có câu hỏi nào trong chuyên mục này.")
# Màn hình làm bài
elif st.session_state.current_idx < total_q:
    idx = st.session_state.current_idx
    q_data = current_quiz_data[idx]

    # Thanh tiến trình
    st.progress((idx) / total_q)
    st.markdown(f"**Câu {idx + 1} / {total_q}** | *Chuyên mục: {q_data['category']}*")

    # Đoạn văn / Đoạn trích (nếu có)
    if "passage" in q_data and q_data["passage"]:
        st.info(f"**Đoạn văn / Thông báo:**\n\n{q_data['passage']}")

    # Câu hỏi
    st.subheader(q_data["question"])

    # Danh sách đáp án chọn
    choice = st.radio(
        "Chọn đáp án đúng:",
        q_data["options"],
        key=f"q_{idx}"
    )

    col1, col2 = st.columns([1, 4])
    with col1:
        submit = st.button("Kiểm tra")

    if submit:
        selected_idx = q_data["options"].index(choice)
        st.session_state.user_answers[idx] = selected_idx
        
        if selected_idx == q_data["answer"]:
            st.success("🎉 Chính xác!")
        else:
            correct_opt = q_data["options"][q_data["answer"]]
            st.error(f"❌ Sai rồi! Đáp án đúng là: **{correct_opt}**")

    # Nút sang câu tiếp theo
    if idx in st.session_state.user_answers:
        if st.button("Câu tiếp theo ➡️"):
            if st.session_state.user_answers[idx] == q_data["answer"]:
                st.session_state.score += 1
            st.session_state.current_idx += 1
            st.rerun()

# Màn hình kết quả
else:
    st.progress(1.0)
    st.balloons()
    st.header("🏁 Bạn đã hoàn thành phần ôn tập này!")
    
    final_score = st.session_state.score
    accuracy = round((final_score / total_q) * 100, 1) if total_q > 0 else 0
    
    st.metric(label="Tổng số câu đúng", value=f"{final_score} / {total_q}", delta=f"{accuracy}%")
    
    if st.button("🔄 Thi lại phần này"):
        st.session_state.current_idx = 0
        st.session_state.score = 0
        st.session_state.user_answers = {}
        st.rerun()
