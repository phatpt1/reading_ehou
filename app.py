import streamlit as st
import json
import os
st.set_page_config(page_title="Ôn Tập Tiếng Anh EHOU", page_icon="📚", layout="centered")
PROGRESS_FILE = "progress.json"
# Dữ liệu 313 câu hỏi
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
        "category": "Từ Vựng - Ghép Nghĩa",
        "passage": "Match each expression to its meaning.",
        "question": "What is the meaning of the expression 'waste time'?",
        "options": [
            "use time badly",
            "last too long",
            "use more time",
            "punctual"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Ghép Nghĩa",
        "passage": "Match each expression to its meaning.",
        "question": "What is the meaning of 'take a long time'?",
        "options": [
            "last too long",
            "use time badly",
            "use more time",
            "don't have the time you need"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Ghép Nghĩa",
        "passage": "Match each expression to its meaning.",
        "question": "What is the meaning of 'spend more time'?",
        "options": [
            "use more time",
            "punctual",
            "last too long",
            "use time badly"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Ghép Nghĩa",
        "passage": "Match each expression to its meaning.",
        "question": "What is the meaning of 'on time'?",
        "options": [
            "punctual",
            "use time badly",
            "last too long",
            "use more time"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Ghép Nghĩa",
        "passage": "Match each expression to its meaning.",
        "question": "What is the meaning of 'don't have enough time'?",
        "options": [
            "don't have the time you need",
            "last too long",
            "punctual",
            "use more time"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Trái Nghĩa",
        "passage": "The Royal Family:\nReplace the bold words by the opposite word.",
        "question": "What is the opposite of 'Princess'?",
        "options": [
            "Prince",
            "King",
            "Queen",
            "Duke"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Trái Nghĩa",
        "passage": "The Royal Family:\nReplace the bold words by the opposite word.",
        "question": "What is the opposite of 'granddaughter'?",
        "options": [
            "son",
            "grandson",
            "brother",
            "nephew"
        ],
        "answer": 1
    },
    {
        "category": "Từ Vựng - Trái Nghĩa",
        "passage": "The Royal Family:\nReplace the bold words by the opposite word.",
        "question": "What is the opposite of 'King'?",
        "options": [
            "Prince",
            "Princess",
            "Queen",
            "Duchess"
        ],
        "answer": 2
    },
    {
        "category": "Từ Vựng - Trái Nghĩa",
        "passage": "The Royal Family:\nReplace the bold words by the opposite word.",
        "question": "What is the opposite of 'daughter'?",
        "options": [
            "brother",
            "son",
            "father",
            "nephew"
        ],
        "answer": 1
    },
    {
        "category": "Từ Vựng - Trái Nghĩa",
        "passage": "The Royal Family:\nReplace the bold words by the opposite word.",
        "question": "What is the opposite of 'sister'?",
        "options": [
            "brother",
            "son",
            "uncle",
            "father"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Trái Nghĩa",
        "passage": "The Royal Family:\nReplace the bold words by the opposite word.",
        "question": "What is the opposite of 'father'?",
        "options": [
            "sister",
            "daughter",
            "mother",
            "aunt"
        ],
        "answer": 2
    },
    {
        "category": "Từ Vựng - Trái Nghĩa",
        "passage": "The Royal Family:\nReplace the bold words by the opposite word.",
        "question": "What is the opposite of 'stepfather'?",
        "options": [
            "mother",
            "stepmother",
            "stepbrother",
            "aunt"
        ],
        "answer": 1
    },
    {
        "category": "Từ Vựng - Trái Nghĩa",
        "passage": "The Royal Family:\nReplace the bold words by the opposite word.",
        "question": "What is the opposite of 'husband'?",
        "options": [
            "daughter",
            "sister",
            "wife",
            "mother"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (Short)",
        "passage": "First of all, we need money to repair old roads and build new roads. We also need more to pay teachers' salaries and to pay for services such as trash collection. Finally, more tax money is needed to give financial help to the poor citizens of the city. It is clear that the city will have serious problems if taxes are not raised soon.",
        "question": "What is the main idea?",
        "options": [
            "We should raise city taxes.",
            "City taxes are too high.",
            "City taxes pay for new roads."
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Short)",
        "passage": "One thing you must consider is the quality of the university's educational program. You also need to think about the school's size and location. Finally, you must be sure to consider the university's tuition to make sure you can afford to go to school there.",
        "question": "What is the main idea?",
        "options": [
            "There are several factors to consider when you choose a university to attend.",
            "You should consider getting a good education.",
            "It is expensive to attend a university in the United States."
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Short)",
        "passage": "Color Matters for What You Wear\nClothes are like a second skin. Most likely you feel good when you wear your favorite color...",
        "question": "Circle the best title for the reading text.",
        "options": [
            "Colors and what you wear.",
            "Colors and kids.",
            "Colors and your personality."
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Short)",
        "passage": "Office workers 'admit being rude'\nMost office workers say they are rude or bad-mannered at work...",
        "question": "The author wants to:",
        "options": [
            "give advice on how to behave politely at work",
            "give specific figures of bad manners at work",
            "give specific examples of bad manners at work"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Short)",
        "passage": "Office workers 'admit being rude'\nMost office workers say they are rude or bad-mannered at work...",
        "question": "The aim of the texts is to:",
        "options": [
            "reflect the fact of officer's bad manners at work with illustrations",
            "encourage officer's bad manners at work",
            "reflect the fact of officer's good manners at work with illustrations"
        ],
        "answer": 0
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
        "category": "Biển Báo & Thông Báo",
        "passage": "UNIVERSITY HOLIDAYS\nFrom next Friday, the library will be closed during weekends and evenings.",
        "question": "What will the library do?",
        "options": [
            "Change its opening hours next Friday.",
            "Close for a long time.",
            "Open again to students next Friday.",
            "Have shorter opening hours until next Friday."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "TRIP TO NEW YORK\nApplication forms will be available from the school office from 1st November.",
        "question": "What does it say?",
        "options": [
            "The earliest that students can pick up their application forms is 1st November.",
            "Students should give in their application forms on 1st November.",
            "Application forms will be given on 1st November.",
            "Application forms are unavailable after 1st November."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "Mark,\nWe went on a bus sightseeing tour of the city yesterday. We didn't stop anywhere but saw more than you would on foot.\nJo",
        "question": "What does it say?",
        "options": [
            "Jo is pleased with the number of things she saw from the bus.",
            "Jo went sightseeing on foot yesterday.",
            "Jo thinks there are better sightseeing tours than the one she took.",
            "Jo regrets not having walked around the city to look at the sights."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "Having a great holiday!\nWent windsurfing today after playing beach volleyball.\nStopped for a barbecue on the way to the funfair yesterday.\nSee you soon! Louis",
        "question": "What does it say?",
        "options": [
            "Louis played beach volleyball before he went windsurfing.",
            "Louis went windsurfing after he went to the funfair yesterday.",
            "Louis went to the funfair before he had lunch.",
            "Louis had a barbecue before playing beach volleyball."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "From: Marie | To: Sylviane\nThanks for lending me that biology book - I'm glad you got it back OK. You can borrow my chemistry one and return it next week if you want.",
        "question": "What does it say?",
        "options": [
            "Marie is offering to lend Sylviane a book.",
            "Marie is asking Sylviane to give back a book she had borrowed.",
            "Marie is glad to lend Sylviane a book.",
            "Marie wants to return one of Sylviane's books to her."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "Janine my birthday meal's booked for 6.30 Saturday at Luigi's restaurant. I know there are things you can't eat, so I've attached a menu. Tell me if it's OK.\nSarah",
        "question": "What does Sarah need to know?",
        "options": [
            "If the food at the restaurant will be all right for Janine.",
            "If Janine wants to see the restaurant menu before Saturday.",
            "If Janine's birthday meal will start at 6.30 Saturday.",
            "If Janine will be available to go to the restaurant."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "MATHS HOMEWORK\nSome of you have told me the homework is a bit difficult. So if you haven't finished it by Friday, you can hand it in on Monday.\nMr Peters",
        "question": "What does it say?",
        "options": [
            "Anyone having problems with their homework may have extra time to complete it.",
            "Students who wish to hand in their homework on Monday should tell Mr Peters.",
            "The maths homework must be handed in on Friday.",
            "The homework given out on Friday must be returned by Monday."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "ONLY BOOKS ALREADY PAID FOR CAN BE TAKEN INTO THE BOOKSHOP CAFÉ.",
        "question": "What does it say?",
        "options": [
            "Do not take books which you haven't bought yet into the café.",
            "Do not read our books while you are eating in the café.",
            "Pay in the café for any books that you want to buy.",
            "Don't take books into the café."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "Mr Wright's English lesson today will be in Room 24D beside the language laboratory. He's off sick, so use the lesson to revise for the test.",
        "question": "What does it say?",
        "options": [
            "The usual English teacher cannot attend today's lesson.",
            "Today's English lesson will be beside the laboratory because the teacher is sick.",
            "The room for English lessons is changing because of the test.",
            "The English class must take their workbooks to the language laboratory."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "Class 5 Garden Party\nBecause of bad weather, tomorrow's party will now be in the School Hall.",
        "question": "What has changed about Class 5's party?",
        "options": [
            "The place",
            "The time",
            "The weather",
            "The refreshments"
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "Dan,\nDon't forget to put your football shirt in the washing machine as soon as you get home from the match.\nMum",
        "question": "What does Dan have to do?",
        "options": [
            "Remember to wash his football shirt after the match.",
            "Dan's mum asked him not to put his shirt in the washing machine.",
            "Remember to make sure his football shirt is clean in time for the match.",
            "Remember where he put the football shirt that he needs for the match."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "COLLEGE STAFF/STUDENT BUS\nStudents cannot get on the bus without ID cards",
        "question": "What does it say?",
        "options": [
            "Students are not allowed on the bus unless they have ID cards.",
            "This bus service cannot be used by college staff unless they show ID cards.",
            "This bus is for students only.",
            "Students can get their ID cards on the bus."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "Jennie,\nThe garage rang - your new tyres have arrived. They can't fit them until next week. Please let them know today which day will be convenient.",
        "question": "What does Jennie have to do?",
        "options": [
            "Arrange a time for the garage to fit the new tyres.",
            "Ask another garage to fit her tyres.",
            "The garage can't fix Jennie's car next week.",
            "Collect the new tyres from the garage."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "We're staying at the Plaza hotel. It's not the hotel we wanted but it doesn't matter because this one is nearer the beach and I'm spending all my time there.",
        "question": "How does Sabrina feel about the Plaza hotel?",
        "options": [
            "She thinks it has an advantage.",
            "She wishes it was nearer the beach.",
            "She didn't want to stay there.",
            "She's disappointed with it."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "WARNING TO MOTORISTS\nRepairs to bridge start on 30/11/06\nDelays likely for four weeks",
        "question": "What does it say?",
        "options": [
            "Bridge repairs may make your journey longer from the end of November.",
            "Repairs will finish on 30/11/06.",
            "Repair work on this bridge will finish in November.",
            "The bridge cannot be used until the end of November."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "CITY BUSES\nPlease have ready the exact fare for your journey.",
        "question": "What does it say?",
        "options": [
            "You need to have the correct money when you board the bus.",
            "You must keep your ticket ready for checking.",
            "All City Bus journeys cost exactly the same.",
            "You need to change your money before getting on the bus."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "FOR SALE\nGremlins Computer Game (ages 8 and above)\nUnwanted gift - box unopened",
        "question": "What does it say?",
        "options": [
            "The owner of the computer game that is for sale has never used it.",
            "The game is for children only.",
            "The person selling the computer game no longer wants to play with it.",
            "The computer game is for sale because the owner is too old for it."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "COLLEGE OFFICE\nStudent identity cards will be available for collection from 14 January.",
        "question": "What does it say?",
        "options": [
            "The earliest students can pick up their identity cards is 14 January.",
            "The latest students can get their identity cards is 14 January.",
            "Students should bring in their identity cards on 14 January.",
            "Student identity cards are unavailable after 14 January."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "Would anyone who knows anything about the damaged window in the school library please report to my office before the end of the day.\nMrs Swan",
        "question": "What does Mrs Swan want to do today?",
        "options": [
            "Discover how a window got broken.",
            "Know what was wrong with the library.",
            "Find out who uses the library.",
            "Repair damage done to the library."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "Guess who I met on this mountain! My tennis hero! I was breathless because of the climb, so unfortunately couldn't speak to ask him for a photo of us together.",
        "question": "What is Amanda sorry about?",
        "options": [
            "That she didn't have her photograph taken with her tennis hero.",
            "That she didn't recognize her tennis hero from his photo.",
            "That she couldn't climb high enough to photograph her tennis hero.",
            "That she didn't climb the mountain."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "EVENING PERFORMANCE\nRefreshements are served only during the interval.",
        "question": "What does it say?",
        "options": [
            "You can have a drink during the break.",
            "You can drink after the performance.",
            "Help yourself to drinks after the performance.",
            "Snacks are available before the performance."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "UNIVERSITY LIBRARY\nPlease wait here while we check your books.",
        "question": "What does it say?",
        "options": [
            "Do not go away until we have checked your books.",
            "Come here if you want your books to be checked.",
            "Do not leave books here for checks without telling us.",
            "Check you have all your books before you leave the library."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "DO NOT CLIMB CASTLE WALLS - DANGER OF FALLING STONES.",
        "question": "What does it say?",
        "options": [
            "Do not climb the walls as they are dangerous.",
            "There is a danger of falling on to the stones.",
            "You should be careful with the stones when climbing.",
            "Check for loose stones before you climb."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "Passengers unable to show a ticket must pay an immediate fine of $10.",
        "question": "What does it say?",
        "options": [
            "You are fined $10 at once if you can't show us your ticket.",
            "You can't enter the show without a ticket.",
            "A $10 fine will be payable later if you travel without a ticket.",
            "If you lose your ticket, a new one will cost you $10."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "INTERNATIONAL STUDENTS' CLUB\nNext Saturday's coach trip is cancelled because of lack of interest.",
        "question": "What does it say?",
        "options": [
            "We are cancelling the trip on Saturday as numbers are too low.",
            "To avoid us cancelling another Saturday trip, tell us what your interests are.",
            "Noboday is interested in the coach trip.",
            "Saturday's coach trip is cancelled because there are transport problems."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "Hi Abdul,\nI won't be in college as I'm not well. Please call round on your way in to pick up my homework-it's due in today. Thanks, Aziz.",
        "question": "What does Aziz want Abdul to do?",
        "options": [
            "Take his homework to college for him. (Do his homework for him)",
            "Call their college to say that he is not well.",
            "Take his homework to college for him.",
            "Pick up any new homework given out at college today."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "Tony\nMaria's sorry but she's going to be late this evening. The train is delayed again! Don't forget you're meeting her at the station. She should be there at 7.15.\nAnita",
        "question": "What is Anita doing?",
        "options": [
            "Explaining that she will be late",
            "Asking Tony to meet her at the station.",
            "Reminding somebody of an arrangement",
            "Apologizing for missing the meeting."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "Casali Restaurant\nWe are open downstairs while improvements are made to this area.",
        "question": "What does it say?",
        "options": [
            "You can only eat in one part of the restaurant at the moment.",
            "Please come downstairs and try our recently improved restaurant.",
            "The restaurant will not be open due to repairs.",
            "The restaurant will reopen when the improvements are finished."
        ],
        "answer": 0
    },
    {
        "category": "Biển Báo & Thông Báo",
        "passage": "IF YOUR SHOES ARE DIRTY, PLEASE REMOVE THEM BEFORE ENTERING THIS CHANGING ROOM.",
        "question": "What does it say?",
        "options": [
            "Clean your shoes at the entrance to the changing room before you come in.",
            "You can keep your shoes on in the changing room unless they are dirty.",
            "All shoes must be taken off and left at the changing room entrance.",
            "Please take off your shoes if possible."
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Điền Từ",
        "passage": "A recruitment firm gives this advice to new workers: It is important to (1)___ time in your relationships with others at (2)___. Get to know the people who work near you: (3)___ yourself to them and tell them something about yourself. If people ask for your help, always (4)___ positively. Don't (5)___ emails or phone calls just because you are busy. If you make a mistake, it is better to (6)___ it and then apologise. When things go wrong, stay calm and (7)___ shouting and using bad language. Remember good (8)___ help to (9)___ your working (10)___ and you will find you can enjoy your work more.",
        "question": "(1) It is important to ___ time in your relationships...",
        "options": [
            "invest",
            "Work",
            "introduce",
            "Respond"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Điền Từ",
        "passage": "A recruitment firm gives this advice to new workers: It is important to (1)___ time in your relationships with others at (2)___. Get to know the people who work near you: (3)___ yourself to them and tell them something about yourself. If people ask for your help, always (4)___ positively. Don't (5)___ emails or phone calls just because you are busy. If you make a mistake, it is better to (6)___ it and then apologise. When things go wrong, stay calm and (7)___ shouting and using bad language. Remember good (8)___ help to (9)___ your working (10)___ and you will find you can enjoy your work more.",
        "question": "(2) ...with others at ___.",
        "options": [
            "Work",
            "Manners",
            "Admit",
            "Avoid"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Điền Từ",
        "passage": "A recruitment firm gives this advice to new workers: It is important to (1)___ time in your relationships with others at (2)___. Get to know the people who work near you: (3)___ yourself to them and tell them something about yourself. If people ask for your help, always (4)___ positively. Don't (5)___ emails or phone calls just because you are busy. If you make a mistake, it is better to (6)___ it and then apologise. When things go wrong, stay calm and (7)___ shouting and using bad language. Remember good (8)___ help to (9)___ your working (10)___ and you will find you can enjoy your work more.",
        "question": "(3) ... ___ yourself to them and tell them something about yourself.",
        "options": [
            "introduce",
            "ignore",
            "improve",
            "Environment"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Điền Từ",
        "passage": "A recruitment firm gives this advice to new workers: It is important to (1)___ time in your relationships with others at (2)___. Get to know the people who work near you: (3)___ yourself to them and tell them something about yourself. If people ask for your help, always (4)___ positively. Don't (5)___ emails or phone calls just because you are busy. If you make a mistake, it is better to (6)___ it and then apologise. When things go wrong, stay calm and (7)___ shouting and using bad language. Remember good (8)___ help to (9)___ your working (10)___ and you will find you can enjoy your work more.",
        "question": "(4) If people ask for your help, always ___ positively.",
        "options": [
            "Respond",
            "invest",
            "Admit",
            "Work"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Điền Từ",
        "passage": "A recruitment firm gives this advice to new workers: It is important to (1)___ time in your relationships with others at (2)___. Get to know the people who work near you: (3)___ yourself to them and tell them something about yourself. If people ask for your help, always (4)___ positively. Don't (5)___ emails or phone calls just because you are busy. If you make a mistake, it is better to (6)___ it and then apologise. When things go wrong, stay calm and (7)___ shouting and using bad language. Remember good (8)___ help to (9)___ your working (10)___ and you will find you can enjoy your work more.",
        "question": "(5) Don't ___ emails or phone calls just because you are busy.",
        "options": [
            "ignore",
            "Avoid",
            "Manners",
            "introduce"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Điền Từ",
        "passage": "A recruitment firm gives this advice to new workers: It is important to (1)___ time in your relationships with others at (2)___. Get to know the people who work near you: (3)___ yourself to them and tell them something about yourself. If people ask for your help, always (4)___ positively. Don't (5)___ emails or phone calls just because you are busy. If you make a mistake, it is better to (6)___ it and then apologise. When things go wrong, stay calm and (7)___ shouting and using bad language. Remember good (8)___ help to (9)___ your working (10)___ and you will find you can enjoy your work more.",
        "question": "(6) If you make a mistake, it is better to ___ it and then apologise.",
        "options": [
            "Admit",
            "improve",
            "invest",
            "Work"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Điền Từ",
        "passage": "A recruitment firm gives this advice to new workers: It is important to (1)___ time in your relationships with others at (2)___. Get to know the people who work near you: (3)___ yourself to them and tell them something about yourself. If people ask for your help, always (4)___ positively. Don't (5)___ emails or phone calls just because you are busy. If you make a mistake, it is better to (6)___ it and then apologise. When things go wrong, stay calm and (7)___ shouting and using bad language. Remember good (8)___ help to (9)___ your working (10)___ and you will find you can enjoy your work more.",
        "question": "(7) When things go wrong, stay calm and ___ shouting and using bad language.",
        "options": [
            "Avoid",
            "Respond",
            "introduce",
            "ignore"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Điền Từ",
        "passage": "A recruitment firm gives this advice to new workers: It is important to (1)___ time in your relationships with others at (2)___. Get to know the people who work near you: (3)___ yourself to them and tell them something about yourself. If people ask for your help, always (4)___ positively. Don't (5)___ emails or phone calls just because you are busy. If you make a mistake, it is better to (6)___ it and then apologise. When things go wrong, stay calm and (7)___ shouting and using bad language. Remember good (8)___ help to (9)___ your working (10)___ and you will find you can enjoy your work more.",
        "question": "(8) Remember good ___ help to improve your working Environment...",
        "options": [
            "Manners",
            "Work",
            "Admit",
            "invest"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Điền Từ",
        "passage": "A recruitment firm gives this advice to new workers: It is important to (1)___ time in your relationships with others at (2)___. Get to know the people who work near you: (3)___ yourself to them and tell them something about yourself. If people ask for your help, always (4)___ positively. Don't (5)___ emails or phone calls just because you are busy. If you make a mistake, it is better to (6)___ it and then apologise. When things go wrong, stay calm and (7)___ shouting and using bad language. Remember good (8)___ help to (9)___ your working (10)___ and you will find you can enjoy your work more.",
        "question": "(9) Remember good Manners help to ___ your working Environment...",
        "options": [
            "improve",
            "ignore",
            "Avoid",
            "introduce"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Điền Từ",
        "passage": "A recruitment firm gives this advice to new workers: It is important to (1)___ time in your relationships with others at (2)___. Get to know the people who work near you: (3)___ yourself to them and tell them something about yourself. If people ask for your help, always (4)___ positively. Don't (5)___ emails or phone calls just because you are busy. If you make a mistake, it is better to (6)___ it and then apologise. When things go wrong, stay calm and (7)___ shouting and using bad language. Remember good (8)___ help to (9)___ your working (10)___ and you will find you can enjoy your work more.",
        "question": "(10) ...help to improve your working ___",
        "options": [
            "Environment",
            "Manners",
            "Work",
            "Admit"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Điền Từ",
        "passage": "A: Did you read the article on Erik Weihenmayer? Isn't he a fascinating person?\nB: Yes, he really is! Imagine being blind and (1)___ a mountain!\nA: Even for people who can see, climbing a mountain is very difficult.\nB: You know, I was really surprised to learn that he is also a teacher and a (2)___ athlete.\nA: People like Erik really (3)___ people all around the world. Did you know that he is not the only person with a disability who has done amazing things?\nB: Yes! I read about Helen Keller in school. She was blind, deaf, and could not speak. Helen Keller became famous because of all the (4)___ she had in her lifetime.\nA: Right! But people who have disabilities are not the only people who face (5)___. We all have difficulties in our lives. We face challenges at home, at work, at school, and in relationships.\nB: I agree. Do you think challenges are good for us?\nA: Yes, I do. I think if a person is not (6)___ and has (7)___, then he or she can overcome most of life's challenges. I believe that challenges make us stronger.\nB: You are right! I think that people like Erik Weihenmayer and Helen Keller really (8)___ others to be brave and face life's challenges and never give up.",
        "question": "(1) Imagine being blind and ___ a mountain!",
        "options": [
            "climbing",
            "afraid",
            "professional",
            "inspire"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Điền Từ",
        "passage": "A: Did you read the article on Erik Weihenmayer? Isn't he a fascinating person?\nB: Yes, he really is! Imagine being blind and (1)___ a mountain!\nA: Even for people who can see, climbing a mountain is very difficult.\nB: You know, I was really surprised to learn that he is also a teacher and a (2)___ athlete.\nA: People like Erik really (3)___ people all around the world. Did you know that he is not the only person with a disability who has done amazing things?\nB: Yes! I read about Helen Keller in school. She was blind, deaf, and could not speak. Helen Keller became famous because of all the (4)___ she had in her lifetime.\nA: Right! But people who have disabilities are not the only people who face (5)___. We all have difficulties in our lives. We face challenges at home, at work, at school, and in relationships.\nB: I agree. Do you think challenges are good for us?\nA: Yes, I do. I think if a person is not (6)___ and has (7)___, then he or she can overcome most of life's challenges. I believe that challenges make us stronger.\nB: You are right! I think that people like Erik Weihenmayer and Helen Keller really (8)___ others to be brave and face life's challenges and never give up.",
        "question": "(2) I was really surprised to learn that he is also a teacher and a ___ athlete.",
        "options": [
            "professional",
            "ambition",
            "accomplishments",
            "encourage"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Điền Từ",
        "passage": "A: Did you read the article on Erik Weihenmayer? Isn't he a fascinating person?\nB: Yes, he really is! Imagine being blind and (1)___ a mountain!\nA: Even for people who can see, climbing a mountain is very difficult.\nB: You know, I was really surprised to learn that he is also a teacher and a (2)___ athlete.\nA: People like Erik really (3)___ people all around the world. Did you know that he is not the only person with a disability who has done amazing things?\nB: Yes! I read about Helen Keller in school. She was blind, deaf, and could not speak. Helen Keller became famous because of all the (4)___ she had in her lifetime.\nA: Right! But people who have disabilities are not the only people who face (5)___. We all have difficulties in our lives. We face challenges at home, at work, at school, and in relationships.\nB: I agree. Do you think challenges are good for us?\nA: Yes, I do. I think if a person is not (6)___ and has (7)___, then he or she can overcome most of life's challenges. I believe that challenges make us stronger.\nB: You are right! I think that people like Erik Weihenmayer and Helen Keller really (8)___ others to be brave and face life's challenges and never give up.",
        "question": "(3) People like Erik really ___ people all around the world.",
        "options": [
            "inspire",
            "afraid",
            "challenges",
            "climbing"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Điền Từ",
        "passage": "A: Did you read the article on Erik Weihenmayer? Isn't he a fascinating person?\nB: Yes, he really is! Imagine being blind and (1)___ a mountain!\nA: Even for people who can see, climbing a mountain is very difficult.\nB: You know, I was really surprised to learn that he is also a teacher and a (2)___ athlete.\nA: People like Erik really (3)___ people all around the world. Did you know that he is not the only person with a disability who has done amazing things?\nB: Yes! I read about Helen Keller in school. She was blind, deaf, and could not speak. Helen Keller became famous because of all the (4)___ she had in her lifetime.\nA: Right! But people who have disabilities are not the only people who face (5)___. We all have difficulties in our lives. We face challenges at home, at work, at school, and in relationships.\nB: I agree. Do you think challenges are good for us?\nA: Yes, I do. I think if a person is not (6)___ and has (7)___, then he or she can overcome most of life's challenges. I believe that challenges make us stronger.\nB: You are right! I think that people like Erik Weihenmayer and Helen Keller really (8)___ others to be brave and face life's challenges and never give up.",
        "question": "(4) Helen Keller became famous because of all the ___ she had in her lifetime.",
        "options": [
            "accomplishments",
            "ambition",
            "professional",
            "encourage"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Điền Từ",
        "passage": "A: Did you read the article on Erik Weihenmayer? Isn't he a fascinating person?\nB: Yes, he really is! Imagine being blind and (1)___ a mountain!\nA: Even for people who can see, climbing a mountain is very difficult.\nB: You know, I was really surprised to learn that he is also a teacher and a (2)___ athlete.\nA: People like Erik really (3)___ people all around the world. Did you know that he is not the only person with a disability who has done amazing things?\nB: Yes! I read about Helen Keller in school. She was blind, deaf, and could not speak. Helen Keller became famous because of all the (4)___ she had in her lifetime.\nA: Right! But people who have disabilities are not the only people who face (5)___. We all have difficulties in our lives. We face challenges at home, at work, at school, and in relationships.\nB: I agree. Do you think challenges are good for us?\nA: Yes, I do. I think if a person is not (6)___ and has (7)___, then he or she can overcome most of life's challenges. I believe that challenges make us stronger.\nB: You are right! I think that people like Erik Weihenmayer and Helen Keller really (8)___ others to be brave and face life's challenges and never give up.",
        "question": "(5) ...people who have disabilities are not the only people who face ___.",
        "options": [
            "challenges",
            "inspire",
            "climbing",
            "afraid"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Điền Từ",
        "passage": "A: Did you read the article on Erik Weihenmayer? Isn't he a fascinating person?\nB: Yes, he really is! Imagine being blind and (1)___ a mountain!\nA: Even for people who can see, climbing a mountain is very difficult.\nB: You know, I was really surprised to learn that he is also a teacher and a (2)___ athlete.\nA: People like Erik really (3)___ people all around the world. Did you know that he is not the only person with a disability who has done amazing things?\nB: Yes! I read about Helen Keller in school. She was blind, deaf, and could not speak. Helen Keller became famous because of all the (4)___ she had in her lifetime.\nA: Right! But people who have disabilities are not the only people who face (5)___. We all have difficulties in our lives. We face challenges at home, at work, at school, and in relationships.\nB: I agree. Do you think challenges are good for us?\nA: Yes, I do. I think if a person is not (6)___ and has (7)___, then he or she can overcome most of life's challenges. I believe that challenges make us stronger.\nB: You are right! I think that people like Erik Weihenmayer and Helen Keller really (8)___ others to be brave and face life's challenges and never give up.",
        "question": "(6) I think if a person is not ___ and has ambition...",
        "options": [
            "afraid",
            "professional",
            "encourage",
            "accomplishments"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Điền Từ",
        "passage": "A: Did you read the article on Erik Weihenmayer? Isn't he a fascinating person?\nB: Yes, he really is! Imagine being blind and (1)___ a mountain!\nA: Even for people who can see, climbing a mountain is very difficult.\nB: You know, I was really surprised to learn that he is also a teacher and a (2)___ athlete.\nA: People like Erik really (3)___ people all around the world. Did you know that he is not the only person with a disability who has done amazing things?\nB: Yes! I read about Helen Keller in school. She was blind, deaf, and could not speak. Helen Keller became famous because of all the (4)___ she had in her lifetime.\nA: Right! But people who have disabilities are not the only people who face (5)___. We all have difficulties in our lives. We face challenges at home, at work, at school, and in relationships.\nB: I agree. Do you think challenges are good for us?\nA: Yes, I do. I think if a person is not (6)___ and has (7)___, then he or she can overcome most of life's challenges. I believe that challenges make us stronger.\nB: You are right! I think that people like Erik Weihenmayer and Helen Keller really (8)___ others to be brave and face life's challenges and never give up.",
        "question": "(7) ...if a person is not afraid and has ___...",
        "options": [
            "ambition",
            "inspire",
            "challenges",
            "climbing"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Điền Từ",
        "passage": "A: Did you read the article on Erik Weihenmayer? Isn't he a fascinating person?\nB: Yes, he really is! Imagine being blind and (1)___ a mountain!\nA: Even for people who can see, climbing a mountain is very difficult.\nB: You know, I was really surprised to learn that he is also a teacher and a (2)___ athlete.\nA: People like Erik really (3)___ people all around the world. Did you know that he is not the only person with a disability who has done amazing things?\nB: Yes! I read about Helen Keller in school. She was blind, deaf, and could not speak. Helen Keller became famous because of all the (4)___ she had in her lifetime.\nA: Right! But people who have disabilities are not the only people who face (5)___. We all have difficulties in our lives. We face challenges at home, at work, at school, and in relationships.\nB: I agree. Do you think challenges are good for us?\nA: Yes, I do. I think if a person is not (6)___ and has (7)___, then he or she can overcome most of life's challenges. I believe that challenges make us stronger.\nB: You are right! I think that people like Erik Weihenmayer and Helen Keller really (8)___ others to be brave and face life's challenges and never give up.",
        "question": "(8) I think that people like Erik Weihenmayer and Helen Keller really ___ others to be brave...",
        "options": [
            "encourage",
            "afraid",
            "professional",
            "ambition"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Điền Từ",
        "passage": "The Royal Family:\nComplete the sentences using the appropriate phrases.",
        "question": "In other ways, their lives are very _______ their friends' lives.",
        "options": [
            "different from",
            "delighted with",
            "in line to",
            "under police escort"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Điền Từ",
        "passage": "The Royal Family:\nComplete the sentences using the appropriate phrases.",
        "question": "The Duchess of Cornwall and Prince Harry... are _______ the news.",
        "options": [
            "delighted with",
            "in due course",
            "admitted to",
            "spent time with"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Điền Từ",
        "passage": "The Royal Family:\nComplete the sentences using the appropriate phrases.",
        "question": "The baby will be third _______ the throne.",
        "options": [
            "in line to",
            "different from",
            "admitted to",
            "under police escort"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Điền Từ",
        "passage": "The Royal Family:\nComplete the sentences using the appropriate phrases.",
        "question": "A spokesman said the duchess has been _______ King Edward VII Hospital...",
        "options": [
            "admitted to",
            "gave birth to",
            "spent time with",
            "in due course"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Điền Từ",
        "passage": "The Royal Family:\nComplete the sentences using the appropriate phrases.",
        "question": "...after the duchess _______ a baby boy.",
        "options": [
            "gave birth to",
            "spent time with",
            "delighted with",
            "admitted to"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Điền Từ",
        "passage": "The Royal Family:\nComplete the sentences using the appropriate phrases.",
        "question": "The young parents _______ their son before telling the news...",
        "options": [
            "spent time with",
            "different from",
            "gave birth to",
            "under police escort"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Điền Từ",
        "passage": "The Royal Family:\nComplete the sentences using the appropriate phrases.",
        "question": "A bulletin signed by him was taken... to the palace _______",
        "options": [
            "under police escort",
            "in line to",
            "in due course",
            "different from"
        ],
        "answer": 0
    },
    {
        "category": "Từ Vựng - Điền Từ",
        "passage": "The Royal Family:\nComplete the sentences using the appropriate phrases.",
        "question": "A Palace spokesman said the names of the baby would be announced _______",
        "options": [
            "in due course",
            "under police escort",
            "delighted with",
            "admitted to"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "The village of Jukkasjarvi is in Swedish Lapland, and winter temperatures there can reach -40C. But 6,000 holidaymakers (1).............go there annually, to visit what is probably Europe's most unusual accommodation. In this hotel, you eat, drink and sleep in rooms made (2)...............ice. If you want, you can (3)...............get married in one. The bar is ice too, and putting hot drinks on it is obviously not (4)..............! The bedrooms are around -4C, but fortunately guests are (5)..............with special sleeping bags that will keep (6)..............warm in the coldest of temperatures. (7)..............outdoor clothes can be supplied too, if needed.\nThe hotel is never more than six months old (8)..............it melts in summer, and (9).............winter it is rebuilt. Creating the hotel (10).............. 10,000 tons of ice, plus 30,000 tons of snow.",
        "question": "6,000 holidaymakers (1).............go there annually",
        "options": [
            "therefore",
            "ever",
            "also",
            "still"
        ],
        "answer": 2
    },
    {
        "category": "Đọc Hiểu (T/F)",
        "passage": "The Olympic Games\nDuring the Olympic Games, people from all over the world come together in the peace and friendship. Some of these people complete for medals. Several million people attend the games, and millions of other people watch them on television.\n\nWhy do we have the Olympic Games? How did they begin? The first Olympic Games that we have records of were in Greece in 776 B.C. The games lasted one day. The only event in the first thirteen Olympic Games was a race. Men ran the length or the stadium (about 192 meters). Then, longer running races were added. Through the years, a few other kinds of events, like the long jump, were also added. During this time, the games were for men only, and women could not even watch them. In the year 393, a Roman emperor ended the Olympic Game because the quality of the games became very low. The Olympics did not take place again for 1500 years!\n\nIn 1984, Pierre de Coubertin of France helped from the International Olympic Committee, and the modern Olympic Games began. In 1896, the games were held again in Athens, Greece. The Greeks built a new stadium for the competition. Three hundred and eleven athletes from thirteen countries competed in many events. The winners became national heroes.\n\nAfter 1896, the games were held every four years during the summer in different cities around the world. In 1900, the Olympics were in Paris, France, and women competed for the first time. In 1908, in London, England, the first gold medals were given to winning athletes. Before that time, the winners received only silver and bronze medals. The Olympic flag was first introduced in 1920 in Antwerp, Belgium. The flag has five rings on it. The rings represent the continents of Africa, Asia, Australia, Europe, and North and South American. Each ring is a different color blue, yellow, black, green, or red because the flag of each of the countries that compete in the games has at least one of these colors in it.\n\nThe Olympic Winter games began in 1924 in Chamonix, France. Athletes competed in winter events such as skiing, ice skating, and ice hockey. Today, the Winter Games take places every four years. The Summer Games also take place every four years, but not in the same year as the winter events. Both the Summer Games and the Winter Games must have at least fifteen events, and they cannot last more than sixteen days.\n\nUntil recently. Olympic competitors could not be professional athletes. All of the athletes in the Olympic Games were amateurs. Today, however, many of the Olympic athletes are professional who play their sports for money during the year. Some people disagree with this idea. They believe that the Olympic game are for amateur athletes, not paid professionals. Other people think that any one can play in the Olympic Games. No matter who the athletes are, millions of people throughout the world enjoy watching the greatest athletic competitions, the Summer Game and the Winter Games of the Olympics.",
        "question": "The first Olympic competitors ran the length of the stadium.",
        "options": [
            "TRUE",
            "FALSE"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (T/F)",
        "passage": "The Olympic Games\nDuring the Olympic Games, people from all over the world come together in the peace and friendship. Some of these people complete for medals. Several million people attend the games, and millions of other people watch them on television.\n\nWhy do we have the Olympic Games? How did they begin? The first Olympic Games that we have records of were in Greece in 776 B.C. The games lasted one day. The only event in the first thirteen Olympic Games was a race. Men ran the length or the stadium (about 192 meters). Then, longer running races were added. Through the years, a few other kinds of events, like the long jump, were also added. During this time, the games were for men only, and women could not even watch them. In the year 393, a Roman emperor ended the Olympic Game because the quality of the games became very low. The Olympics did not take place again for 1500 years!\n\nIn 1984, Pierre de Coubertin of France helped from the International Olympic Committee, and the modern Olympic Games began. In 1896, the games were held again in Athens, Greece. The Greeks built a new stadium for the competition. Three hundred and eleven athletes from thirteen countries competed in many events. The winners became national heroes.\n\nAfter 1896, the games were held every four years during the summer in different cities around the world. In 1900, the Olympics were in Paris, France, and women competed for the first time. In 1908, in London, England, the first gold medals were given to winning athletes. Before that time, the winners received only silver and bronze medals. The Olympic flag was first introduced in 1920 in Antwerp, Belgium. The flag has five rings on it. The rings represent the continents of Africa, Asia, Australia, Europe, and North and South American. Each ring is a different color blue, yellow, black, green, or red because the flag of each of the countries that compete in the games has at least one of these colors in it.\n\nThe Olympic Winter games began in 1924 in Chamonix, France. Athletes competed in winter events such as skiing, ice skating, and ice hockey. Today, the Winter Games take places every four years. The Summer Games also take place every four years, but not in the same year as the winter events. Both the Summer Games and the Winter Games must have at least fifteen events, and they cannot last more than sixteen days.\n\nUntil recently. Olympic competitors could not be professional athletes. All of the athletes in the Olympic Games were amateurs. Today, however, many of the Olympic athletes are professional who play their sports for money during the year. Some people disagree with this idea. They believe that the Olympic game are for amateur athletes, not paid professionals. Other people think that any one can play in the Olympic Games. No matter who the athletes are, millions of people throughout the world enjoy watching the greatest athletic competitions, the Summer Game and the Winter Games of the Olympics.",
        "question": "Pierre de Coubertin was an athlete in the first modern games.",
        "options": [
            "TRUE",
            "FALSE"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (T/F)",
        "passage": "The Olympic Games\nDuring the Olympic Games, people from all over the world come together in the peace and friendship. Some of these people complete for medals. Several million people attend the games, and millions of other people watch them on television.\n\nWhy do we have the Olympic Games? How did they begin? The first Olympic Games that we have records of were in Greece in 776 B.C. The games lasted one day. The only event in the first thirteen Olympic Games was a race. Men ran the length or the stadium (about 192 meters). Then, longer running races were added. Through the years, a few other kinds of events, like the long jump, were also added. During this time, the games were for men only, and women could not even watch them. In the year 393, a Roman emperor ended the Olympic Game because the quality of the games became very low. The Olympics did not take place again for 1500 years!\n\nIn 1984, Pierre de Coubertin of France helped from the International Olympic Committee, and the modern Olympic Games began. In 1896, the games were held again in Athens, Greece. The Greeks built a new stadium for the competition. Three hundred and eleven athletes from thirteen countries competed in many events. The winners became national heroes.\n\nAfter 1896, the games were held every four years during the summer in different cities around the world. In 1900, the Olympics were in Paris, France, and women competed for the first time. In 1908, in London, England, the first gold medals were given to winning athletes. Before that time, the winners received only silver and bronze medals. The Olympic flag was first introduced in 1920 in Antwerp, Belgium. The flag has five rings on it. The rings represent the continents of Africa, Asia, Australia, Europe, and North and South American. Each ring is a different color blue, yellow, black, green, or red because the flag of each of the countries that compete in the games has at least one of these colors in it.\n\nThe Olympic Winter games began in 1924 in Chamonix, France. Athletes competed in winter events such as skiing, ice skating, and ice hockey. Today, the Winter Games take places every four years. The Summer Games also take place every four years, but not in the same year as the winter events. Both the Summer Games and the Winter Games must have at least fifteen events, and they cannot last more than sixteen days.\n\nUntil recently. Olympic competitors could not be professional athletes. All of the athletes in the Olympic Games were amateurs. Today, however, many of the Olympic athletes are professional who play their sports for money during the year. Some people disagree with this idea. They believe that the Olympic game are for amateur athletes, not paid professionals. Other people think that any one can play in the Olympic Games. No matter who the athletes are, millions of people throughout the world enjoy watching the greatest athletic competitions, the Summer Game and the Winter Games of the Olympics.",
        "question": "Winners have always received gold medals.",
        "options": [
            "TRUE",
            "FALSE"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (T/F)",
        "passage": "The Olympic Games\nDuring the Olympic Games, people from all over the world come together in the peace and friendship. Some of these people complete for medals. Several million people attend the games, and millions of other people watch them on television.\n\nWhy do we have the Olympic Games? How did they begin? The first Olympic Games that we have records of were in Greece in 776 B.C. The games lasted one day. The only event in the first thirteen Olympic Games was a race. Men ran the length or the stadium (about 192 meters). Then, longer running races were added. Through the years, a few other kinds of events, like the long jump, were also added. During this time, the games were for men only, and women could not even watch them. In the year 393, a Roman emperor ended the Olympic Game because the quality of the games became very low. The Olympics did not take place again for 1500 years!\n\nIn 1984, Pierre de Coubertin of France helped from the International Olympic Committee, and the modern Olympic Games began. In 1896, the games were held again in Athens, Greece. The Greeks built a new stadium for the competition. Three hundred and eleven athletes from thirteen countries competed in many events. The winners became national heroes.\n\nAfter 1896, the games were held every four years during the summer in different cities around the world. In 1900, the Olympics were in Paris, France, and women competed for the first time. In 1908, in London, England, the first gold medals were given to winning athletes. Before that time, the winners received only silver and bronze medals. The Olympic flag was first introduced in 1920 in Antwerp, Belgium. The flag has five rings on it. The rings represent the continents of Africa, Asia, Australia, Europe, and North and South American. Each ring is a different color blue, yellow, black, green, or red because the flag of each of the countries that compete in the games has at least one of these colors in it.\n\nThe Olympic Winter games began in 1924 in Chamonix, France. Athletes competed in winter events such as skiing, ice skating, and ice hockey. Today, the Winter Games take places every four years. The Summer Games also take place every four years, but not in the same year as the winter events. Both the Summer Games and the Winter Games must have at least fifteen events, and they cannot last more than sixteen days.\n\nUntil recently. Olympic competitors could not be professional athletes. All of the athletes in the Olympic Games were amateurs. Today, however, many of the Olympic athletes are professional who play their sports for money during the year. Some people disagree with this idea. They believe that the Olympic game are for amateur athletes, not paid professionals. Other people think that any one can play in the Olympic Games. No matter who the athletes are, millions of people throughout the world enjoy watching the greatest athletic competitions, the Summer Game and the Winter Games of the Olympics.",
        "question": "The Olympic flag has six colored rings on it.",
        "options": [
            "TRUE",
            "FALSE"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (T/F)",
        "passage": "The Olympic Games\nDuring the Olympic Games, people from all over the world come together in the peace and friendship. Some of these people complete for medals. Several million people attend the games, and millions of other people watch them on television.\n\nWhy do we have the Olympic Games? How did they begin? The first Olympic Games that we have records of were in Greece in 776 B.C. The games lasted one day. The only event in the first thirteen Olympic Games was a race. Men ran the length or the stadium (about 192 meters). Then, longer running races were added. Through the years, a few other kinds of events, like the long jump, were also added. During this time, the games were for men only, and women could not even watch them. In the year 393, a Roman emperor ended the Olympic Game because the quality of the games became very low. The Olympics did not take place again for 1500 years!\n\nIn 1984, Pierre de Coubertin of France helped from the International Olympic Committee, and the modern Olympic Games began. In 1896, the games were held again in Athens, Greece. The Greeks built a new stadium for the competition. Three hundred and eleven athletes from thirteen countries competed in many events. The winners became national heroes.\n\nAfter 1896, the games were held every four years during the summer in different cities around the world. In 1900, the Olympics were in Paris, France, and women competed for the first time. In 1908, in London, England, the first gold medals were given to winning athletes. Before that time, the winners received only silver and bronze medals. The Olympic flag was first introduced in 1920 in Antwerp, Belgium. The flag has five rings on it. The rings represent the continents of Africa, Asia, Australia, Europe, and North and South American. Each ring is a different color blue, yellow, black, green, or red because the flag of each of the countries that compete in the games has at least one of these colors in it.\n\nThe Olympic Winter games began in 1924 in Chamonix, France. Athletes competed in winter events such as skiing, ice skating, and ice hockey. Today, the Winter Games take places every four years. The Summer Games also take place every four years, but not in the same year as the winter events. Both the Summer Games and the Winter Games must have at least fifteen events, and they cannot last more than sixteen days.\n\nUntil recently. Olympic competitors could not be professional athletes. All of the athletes in the Olympic Games were amateurs. Today, however, many of the Olympic athletes are professional who play their sports for money during the year. Some people disagree with this idea. They believe that the Olympic game are for amateur athletes, not paid professionals. Other people think that any one can play in the Olympic Games. No matter who the athletes are, millions of people throughout the world enjoy watching the greatest athletic competitions, the Summer Game and the Winter Games of the Olympics.",
        "question": "The summer and winter games take place in the same year.",
        "options": [
            "TRUE",
            "FALSE"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (T/F)",
        "passage": "The Olympic Games\nDuring the Olympic Games, people from all over the world come together in the peace and friendship. Some of these people complete for medals. Several million people attend the games, and millions of other people watch them on television.\n\nWhy do we have the Olympic Games? How did they begin? The first Olympic Games that we have records of were in Greece in 776 B.C. The games lasted one day. The only event in the first thirteen Olympic Games was a race. Men ran the length or the stadium (about 192 meters). Then, longer running races were added. Through the years, a few other kinds of events, like the long jump, were also added. During this time, the games were for men only, and women could not even watch them. In the year 393, a Roman emperor ended the Olympic Game because the quality of the games became very low. The Olympics did not take place again for 1500 years!\n\nIn 1984, Pierre de Coubertin of France helped from the International Olympic Committee, and the modern Olympic Games began. In 1896, the games were held again in Athens, Greece. The Greeks built a new stadium for the competition. Three hundred and eleven athletes from thirteen countries competed in many events. The winners became national heroes.\n\nAfter 1896, the games were held every four years during the summer in different cities around the world. In 1900, the Olympics were in Paris, France, and women competed for the first time. In 1908, in London, England, the first gold medals were given to winning athletes. Before that time, the winners received only silver and bronze medals. The Olympic flag was first introduced in 1920 in Antwerp, Belgium. The flag has five rings on it. The rings represent the continents of Africa, Asia, Australia, Europe, and North and South American. Each ring is a different color blue, yellow, black, green, or red because the flag of each of the countries that compete in the games has at least one of these colors in it.\n\nThe Olympic Winter games began in 1924 in Chamonix, France. Athletes competed in winter events such as skiing, ice skating, and ice hockey. Today, the Winter Games take places every four years. The Summer Games also take place every four years, but not in the same year as the winter events. Both the Summer Games and the Winter Games must have at least fifteen events, and they cannot last more than sixteen days.\n\nUntil recently. Olympic competitors could not be professional athletes. All of the athletes in the Olympic Games were amateurs. Today, however, many of the Olympic athletes are professional who play their sports for money during the year. Some people disagree with this idea. They believe that the Olympic game are for amateur athletes, not paid professionals. Other people think that any one can play in the Olympic Games. No matter who the athletes are, millions of people throughout the world enjoy watching the greatest athletic competitions, the Summer Game and the Winter Games of the Olympics.",
        "question": "Today both men and women compete in the Olympics.",
        "options": [
            "TRUE",
            "FALSE"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Gap Fill)",
        "passage": "Nowadays people are more aware that wildlife all over the world is in danger. Many species of animals are threatened, and could easily become _(1)_ if we do not make an effort to protect them. There are many reasons for this. In some cases, animals are hunted for their fur or for other valuable parts of their bodies. Some birds, _(2)_ as parrots are caught alive and sold as pets. For many animals and birds, the problem is that their habitat-the place where they live-is disappearing. More_ _(3)_ is used for farms, for houses or industry, and there are fewer open spaces than there once were. Farmers use powerful chemicals to help them grow better crops, but these chemicals pollute _(4)_ environment and harm wildlife. The most successful animal on earth-human beings-will soon be the only ones left, _(5)_ we can solve this problem.",
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
        "passage": "Nowadays people are more aware that wildlife all over the world is in danger. Many species of animals are threatened, and could easily become _(1)_ if we do not make an effort to protect them. There are many reasons for this. In some cases, animals are hunted for their fur or for other valuable parts of their bodies. Some birds, _(2)_ as parrots are caught alive and sold as pets. For many animals and birds, the problem is that their habitat-the place where they live-is disappearing. More_ _(3)_ is used for farms, for houses or industry, and there are fewer open spaces than there once were. Farmers use powerful chemicals to help them grow better crops, but these chemicals pollute _(4)_ environment and harm wildlife. The most successful animal on earth-human beings-will soon be the only ones left, _(5)_ we can solve this problem.",
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
        "passage": "Nowadays people are more aware that wildlife all over the world is in danger. Many species of animals are threatened, and could easily become _(1)_ if we do not make an effort to protect them. There are many reasons for this. In some cases, animals are hunted for their fur or for other valuable parts of their bodies. Some birds, _(2)_ as parrots are caught alive and sold as pets. For many animals and birds, the problem is that their habitat-the place where they live-is disappearing. More_ _(3)_ is used for farms, for houses or industry, and there are fewer open spaces than there once were. Farmers use powerful chemicals to help them grow better crops, but these chemicals pollute _(4)_ environment and harm wildlife. The most successful animal on earth-human beings-will soon be the only ones left, _(5)_ we can solve this problem.",
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
        "passage": "Nowadays people are more aware that wildlife all over the world is in danger. Many species of animals are threatened, and could easily become _(1)_ if we do not make an effort to protect them. There are many reasons for this. In some cases, animals are hunted for their fur or for other valuable parts of their bodies. Some birds, _(2)_ as parrots are caught alive and sold as pets. For many animals and birds, the problem is that their habitat-the place where they live-is disappearing. More_ _(3)_ is used for farms, for houses or industry, and there are fewer open spaces than there once were. Farmers use powerful chemicals to help them grow better crops, but these chemicals pollute _(4)_ environment and harm wildlife. The most successful animal on earth-human beings-will soon be the only ones left, _(5)_ we can solve this problem.",
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
        "passage": "Nowadays people are more aware that wildlife all over the world is in danger. Many species of animals are threatened, and could easily become _(1)_ if we do not make an effort to protect them. There are many reasons for this. In some cases, animals are hunted for their fur or for other valuable parts of their bodies. Some birds, _(2)_ as parrots are caught alive and sold as pets. For many animals and birds, the problem is that their habitat-the place where they live-is disappearing. More_ _(3)_ is used for farms, for houses or industry, and there are fewer open spaces than there once were. Farmers use powerful chemicals to help them grow better crops, but these chemicals pollute _(4)_ environment and harm wildlife. The most successful animal on earth-human beings-will soon be the only ones left, _(5)_ we can solve this problem.",
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
        "passage": "In most countries, almost all schools (1)__ private until the early 1800's. At that time, many government leaders began to encourage development of public schools to promote national progress by_(2)_ education widely available to citizens. Today, the number of public and private schools differs _ (3)__ one country to another. In many developed countries, private schools offer a general focus on __ (4)__ for college; a special focus on science, music or other subject areas; and religious instructions. The Roman Catholic Church is one of the __(5)__ sponsors of private schools throughout the world.",
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
        "passage": "In most countries, almost all schools (1)__ private until the early 1800's. At that time, many government leaders began to encourage development of public schools to promote national progress by_(2)_ education widely available to citizens. Today, the number of public and private schools differs _ (3)__ one country to another. In many developed countries, private schools offer a general focus on __ (4)__ for college; a special focus on science, music or other subject areas; and religious instructions. The Roman Catholic Church is one of the __(5)__ sponsors of private schools throughout the world.",
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
        "passage": "In most countries, almost all schools (1)__ private until the early 1800's. At that time, many government leaders began to encourage development of public schools to promote national progress by_(2)_ education widely available to citizens. Today, the number of public and private schools differs _ (3)__ one country to another. In many developed countries, private schools offer a general focus on __ (4)__ for college; a special focus on science, music or other subject areas; and religious instructions. The Roman Catholic Church is one of the __(5)__ sponsors of private schools throughout the world.",
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
        "passage": "In most countries, almost all schools (1)__ private until the early 1800's. At that time, many government leaders began to encourage development of public schools to promote national progress by_(2)_ education widely available to citizens. Today, the number of public and private schools differs _ (3)__ one country to another. In many developed countries, private schools offer a general focus on __ (4)__ for college; a special focus on science, music or other subject areas; and religious instructions. The Roman Catholic Church is one of the __(5)__ sponsors of private schools throughout the world.",
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
        "passage": "In most countries, almost all schools (1)__ private until the early 1800's. At that time, many government leaders began to encourage development of public schools to promote national progress by_(2)_ education widely available to citizens. Today, the number of public and private schools differs _ (3)__ one country to another. In many developed countries, private schools offer a general focus on __ (4)__ for college; a special focus on science, music or other subject areas; and religious instructions. The Roman Catholic Church is one of the __(5)__ sponsors of private schools throughout the world.",
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
        "passage": "If you are invited to someone's house for dinner in the United States, you should _ (1) _ a gift, such as a bunch of flowers or a box of chocolates. If you give your host a wrapped gift, he/she may open it in front of you. Opening a present in front of the gift-giver is considered polite. It shows that the host is excited _ (2) _ receiving the gift and wants to show his/her appreciation to you immediately. Even if the host doesn't like it, he/ she will tell a \"_(3)_ lie\" and say how much they like the gift to prevent the guest from feeling bad. If your host asks you to arrive at a particular time, you should not arrive _ (4) _ on time or earlier than the expected time, because this is considered to be potentially inconvenient and therefore rude, as the host may not _ (5) _ ready.",
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
        "passage": "If you are invited to someone's house for dinner in the United States, you should _ (1) _ a gift, such as a bunch of flowers or a box of chocolates. If you give your host a wrapped gift, he/she may open it in front of you. Opening a present in front of the gift-giver is considered polite. It shows that the host is excited _ (2) _ receiving the gift and wants to show his/her appreciation to you immediately. Even if the host doesn't like it, he/ she will tell a \"_(3)_ lie\" and say how much they like the gift to prevent the guest from feeling bad. If your host asks you to arrive at a particular time, you should not arrive _ (4) _ on time or earlier than the expected time, because this is considered to be potentially inconvenient and therefore rude, as the host may not _ (5) _ ready.",
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
        "passage": "If you are invited to someone's house for dinner in the United States, you should _ (1) _ a gift, such as a bunch of flowers or a box of chocolates. If you give your host a wrapped gift, he/she may open it in front of you. Opening a present in front of the gift-giver is considered polite. It shows that the host is excited _ (2) _ receiving the gift and wants to show his/her appreciation to you immediately. Even if the host doesn't like it, he/ she will tell a \"_(3)_ lie\" and say how much they like the gift to prevent the guest from feeling bad. If your host asks you to arrive at a particular time, you should not arrive _ (4) _ on time or earlier than the expected time, because this is considered to be potentially inconvenient and therefore rude, as the host may not _ (5) _ ready.",
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
        "passage": "If you are invited to someone's house for dinner in the United States, you should _ (1) _ a gift, such as a bunch of flowers or a box of chocolates. If you give your host a wrapped gift, he/she may open it in front of you. Opening a present in front of the gift-giver is considered polite. It shows that the host is excited _ (2) _ receiving the gift and wants to show his/her appreciation to you immediately. Even if the host doesn't like it, he/ she will tell a \"_(3)_ lie\" and say how much they like the gift to prevent the guest from feeling bad. If your host asks you to arrive at a particular time, you should not arrive _ (4) _ on time or earlier than the expected time, because this is considered to be potentially inconvenient and therefore rude, as the host may not _ (5) _ ready.",
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
        "passage": "If you are invited to someone's house for dinner in the United States, you should _ (1) _ a gift, such as a bunch of flowers or a box of chocolates. If you give your host a wrapped gift, he/she may open it in front of you. Opening a present in front of the gift-giver is considered polite. It shows that the host is excited _ (2) _ receiving the gift and wants to show his/her appreciation to you immediately. Even if the host doesn't like it, he/ she will tell a \"_(3)_ lie\" and say how much they like the gift to prevent the guest from feeling bad. If your host asks you to arrive at a particular time, you should not arrive _ (4) _ on time or earlier than the expected time, because this is considered to be potentially inconvenient and therefore rude, as the host may not _ (5) _ ready.",
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
        "passage": "The village of Jukkasjarvi is in Swedish Lapland, and winter temperatures there can reach -40C. But 6,000 holidaymakers (1).............go there annually, to visit what is probably Europe's most unusual accommodation. In this hotel, you eat, drink and sleep in rooms made (2)...............ice. If you want, you can (3)...............get married in one. The bar is ice too, and putting hot drinks on it is obviously not (4)..............! The bedrooms are around -4C, but fortunately guests are (5)..............with special sleeping bags that will keep (6)..............warm in the coldest of temperatures. (7)..............outdoor clothes can be supplied too, if needed.\nThe hotel is never more than six months old (8)..............it melts in summer, and (9).............winter it is rebuilt. Creating the hotel (10).............. 10,000 tons of ice, plus 30,000 tons of snow.",
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
        "passage": "The village of Jukkasjarvi is in Swedish Lapland, and winter temperatures there can reach -40C. But 6,000 holidaymakers (1).............go there annually, to visit what is probably Europe's most unusual accommodation. In this hotel, you eat, drink and sleep in rooms made (2)...............ice. If you want, you can (3)...............get married in one. The bar is ice too, and putting hot drinks on it is obviously not (4)..............! The bedrooms are around -4C, but fortunately guests are (5)..............with special sleeping bags that will keep (6)..............warm in the coldest of temperatures. (7)..............outdoor clothes can be supplied too, if needed.\nThe hotel is never more than six months old (8)..............it melts in summer, and (9).............winter it is rebuilt. Creating the hotel (10).............. 10,000 tons of ice, plus 30,000 tons of snow.",
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
        "passage": "The village of Jukkasjarvi is in Swedish Lapland, and winter temperatures there can reach -40C. But 6,000 holidaymakers (1).............go there annually, to visit what is probably Europe's most unusual accommodation. In this hotel, you eat, drink and sleep in rooms made (2)...............ice. If you want, you can (3)...............get married in one. The bar is ice too, and putting hot drinks on it is obviously not (4)..............! The bedrooms are around -4C, but fortunately guests are (5)..............with special sleeping bags that will keep (6)..............warm in the coldest of temperatures. (7)..............outdoor clothes can be supplied too, if needed.\nThe hotel is never more than six months old (8)..............it melts in summer, and (9).............winter it is rebuilt. Creating the hotel (10).............. 10,000 tons of ice, plus 30,000 tons of snow.",
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
        "passage": "The village of Jukkasjarvi is in Swedish Lapland, and winter temperatures there can reach -40C. But 6,000 holidaymakers (1).............go there annually, to visit what is probably Europe's most unusual accommodation. In this hotel, you eat, drink and sleep in rooms made (2)...............ice. If you want, you can (3)...............get married in one. The bar is ice too, and putting hot drinks on it is obviously not (4)..............! The bedrooms are around -4C, but fortunately guests are (5)..............with special sleeping bags that will keep (6)..............warm in the coldest of temperatures. (7)..............outdoor clothes can be supplied too, if needed.\nThe hotel is never more than six months old (8)..............it melts in summer, and (9).............winter it is rebuilt. Creating the hotel (10).............. 10,000 tons of ice, plus 30,000 tons of snow.",
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
        "passage": "The village of Jukkasjarvi is in Swedish Lapland, and winter temperatures there can reach -40C. But 6,000 holidaymakers (1).............go there annually, to visit what is probably Europe's most unusual accommodation. In this hotel, you eat, drink and sleep in rooms made (2)...............ice. If you want, you can (3)...............get married in one. The bar is ice too, and putting hot drinks on it is obviously not (4)..............! The bedrooms are around -4C, but fortunately guests are (5)..............with special sleeping bags that will keep (6)..............warm in the coldest of temperatures. (7)..............outdoor clothes can be supplied too, if needed.\nThe hotel is never more than six months old (8)..............it melts in summer, and (9).............winter it is rebuilt. Creating the hotel (10).............. 10,000 tons of ice, plus 30,000 tons of snow.",
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
        "passage": "The village of Jukkasjarvi is in Swedish Lapland, and winter temperatures there can reach -40C. But 6,000 holidaymakers (1).............go there annually, to visit what is probably Europe's most unusual accommodation. In this hotel, you eat, drink and sleep in rooms made (2)...............ice. If you want, you can (3)...............get married in one. The bar is ice too, and putting hot drinks on it is obviously not (4)..............! The bedrooms are around -4C, but fortunately guests are (5)..............with special sleeping bags that will keep (6)..............warm in the coldest of temperatures. (7)..............outdoor clothes can be supplied too, if needed.\nThe hotel is never more than six months old (8)..............it melts in summer, and (9).............winter it is rebuilt. Creating the hotel (10).............. 10,000 tons of ice, plus 30,000 tons of snow.",
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
        "passage": "The village of Jukkasjarvi is in Swedish Lapland, and winter temperatures there can reach -40C. But 6,000 holidaymakers (1).............go there annually, to visit what is probably Europe's most unusual accommodation. In this hotel, you eat, drink and sleep in rooms made (2)...............ice. If you want, you can (3)...............get married in one. The bar is ice too, and putting hot drinks on it is obviously not (4)..............! The bedrooms are around -4C, but fortunately guests are (5)..............with special sleeping bags that will keep (6)..............warm in the coldest of temperatures. (7)..............outdoor clothes can be supplied too, if needed.\nThe hotel is never more than six months old (8)..............it melts in summer, and (9).............winter it is rebuilt. Creating the hotel (10).............. 10,000 tons of ice, plus 30,000 tons of snow.",
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
        "passage": "The village of Jukkasjarvi is in Swedish Lapland, and winter temperatures there can reach -40C. But 6,000 holidaymakers (1).............go there annually, to visit what is probably Europe's most unusual accommodation. In this hotel, you eat, drink and sleep in rooms made (2)...............ice. If you want, you can (3)...............get married in one. The bar is ice too, and putting hot drinks on it is obviously not (4)..............! The bedrooms are around -4C, but fortunately guests are (5)..............with special sleeping bags that will keep (6)..............warm in the coldest of temperatures. (7)..............outdoor clothes can be supplied too, if needed.\nThe hotel is never more than six months old (8)..............it melts in summer, and (9).............winter it is rebuilt. Creating the hotel (10).............. 10,000 tons of ice, plus 30,000 tons of snow.",
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
        "passage": "The village of Jukkasjarvi is in Swedish Lapland, and winter temperatures there can reach -40C. But 6,000 holidaymakers (1).............go there annually, to visit what is probably Europe's most unusual accommodation. In this hotel, you eat, drink and sleep in rooms made (2)...............ice. If you want, you can (3)...............get married in one. The bar is ice too, and putting hot drinks on it is obviously not (4)..............! The bedrooms are around -4C, but fortunately guests are (5)..............with special sleeping bags that will keep (6)..............warm in the coldest of temperatures. (7)..............outdoor clothes can be supplied too, if needed.\nThe hotel is never more than six months old (8)..............it melts in summer, and (9).............winter it is rebuilt. Creating the hotel (10).............. 10,000 tons of ice, plus 30,000 tons of snow.",
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
        "passage": "Henry Ford was born on a farm in Michigan in 1863 but he did not like farming. When he was fifteen he began work as a mechanic and in 1893 he built his first car. After he (1)..........driven it 1,500 kilometers, he sold it and built two bigger cars. Then, in 1903, he (2)................the Ford Motor Company. By (3)..............strong but light steel, he built cheap cars for (4)..............people to buy.\nIn 1908, he built the first Ford Model 'T', (5)..............sold for $825. He was soon selling 100 cars (6)................day. By 1927, the Ford Motor Company was (7).............$700 million. Early Ford cars were simple and cheap, but (8)...........things simple sometimes (9)..............less choice.\n'You (10)..............have any color you like,' said Henry Ford of the Model T, 'as long as it's black'.",
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
        "passage": "Henry Ford was born on a farm in Michigan in 1863 but he did not like farming. When he was fifteen he began work as a mechanic and in 1893 he built his first car. After he (1)..........driven it 1,500 kilometers, he sold it and built two bigger cars. Then, in 1903, he (2)................the Ford Motor Company. By (3)..............strong but light steel, he built cheap cars for (4)..............people to buy.\nIn 1908, he built the first Ford Model 'T', (5)..............sold for $825. He was soon selling 100 cars (6)................day. By 1927, the Ford Motor Company was (7).............$700 million. Early Ford cars were simple and cheap, but (8)...........things simple sometimes (9)..............less choice.\n'You (10)..............have any color you like,' said Henry Ford of the Model T, 'as long as it's black'.",
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
        "passage": "Henry Ford was born on a farm in Michigan in 1863 but he did not like farming. When he was fifteen he began work as a mechanic and in 1893 he built his first car. After he (1)..........driven it 1,500 kilometers, he sold it and built two bigger cars. Then, in 1903, he (2)................the Ford Motor Company. By (3)..............strong but light steel, he built cheap cars for (4)..............people to buy.\nIn 1908, he built the first Ford Model 'T', (5)..............sold for $825. He was soon selling 100 cars (6)................day. By 1927, the Ford Motor Company was (7).............$700 million. Early Ford cars were simple and cheap, but (8)...........things simple sometimes (9)..............less choice.\n'You (10)..............have any color you like,' said Henry Ford of the Model T, 'as long as it's black'.",
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
        "passage": "Henry Ford was born on a farm in Michigan in 1863 but he did not like farming. When he was fifteen he began work as a mechanic and in 1893 he built his first car. After he (1)..........driven it 1,500 kilometers, he sold it and built two bigger cars. Then, in 1903, he (2)................the Ford Motor Company. By (3)..............strong but light steel, he built cheap cars for (4)..............people to buy.\nIn 1908, he built the first Ford Model 'T', (5)..............sold for $825. He was soon selling 100 cars (6)................day. By 1927, the Ford Motor Company was (7).............$700 million. Early Ford cars were simple and cheap, but (8)...........things simple sometimes (9)..............less choice.\n'You (10)..............have any color you like,' said Henry Ford of the Model T, 'as long as it's black'.",
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
        "passage": "Henry Ford was born on a farm in Michigan in 1863 but he did not like farming. When he was fifteen he began work as a mechanic and in 1893 he built his first car. After he (1)..........driven it 1,500 kilometers, he sold it and built two bigger cars. Then, in 1903, he (2)................the Ford Motor Company. By (3)..............strong but light steel, he built cheap cars for (4)..............people to buy.\nIn 1908, he built the first Ford Model 'T', (5)..............sold for $825. He was soon selling 100 cars (6)................day. By 1927, the Ford Motor Company was (7).............$700 million. Early Ford cars were simple and cheap, but (8)...........things simple sometimes (9)..............less choice.\n'You (10)..............have any color you like,' said Henry Ford of the Model T, 'as long as it's black'.",
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
        "passage": "Henry Ford was born on a farm in Michigan in 1863 but he did not like farming. When he was fifteen he began work as a mechanic and in 1893 he built his first car. After he (1)..........driven it 1,500 kilometers, he sold it and built two bigger cars. Then, in 1903, he (2)................the Ford Motor Company. By (3)..............strong but light steel, he built cheap cars for (4)..............people to buy.\nIn 1908, he built the first Ford Model 'T', (5)..............sold for $825. He was soon selling 100 cars (6)................day. By 1927, the Ford Motor Company was (7).............$700 million. Early Ford cars were simple and cheap, but (8)...........things simple sometimes (9)..............less choice.\n'You (10)..............have any color you like,' said Henry Ford of the Model T, 'as long as it's black'.",
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
        "passage": "Henry Ford was born on a farm in Michigan in 1863 but he did not like farming. When he was fifteen he began work as a mechanic and in 1893 he built his first car. After he (1)..........driven it 1,500 kilometers, he sold it and built two bigger cars. Then, in 1903, he (2)................the Ford Motor Company. By (3)..............strong but light steel, he built cheap cars for (4)..............people to buy.\nIn 1908, he built the first Ford Model 'T', (5)..............sold for $825. He was soon selling 100 cars (6)................day. By 1927, the Ford Motor Company was (7).............$700 million. Early Ford cars were simple and cheap, but (8)...........things simple sometimes (9)..............less choice.\n'You (10)..............have any color you like,' said Henry Ford of the Model T, 'as long as it's black'.",
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
        "passage": "Henry Ford was born on a farm in Michigan in 1863 but he did not like farming. When he was fifteen he began work as a mechanic and in 1893 he built his first car. After he (1)..........driven it 1,500 kilometers, he sold it and built two bigger cars. Then, in 1903, he (2)................the Ford Motor Company. By (3)..............strong but light steel, he built cheap cars for (4)..............people to buy.\nIn 1908, he built the first Ford Model 'T', (5)..............sold for $825. He was soon selling 100 cars (6)................day. By 1927, the Ford Motor Company was (7).............$700 million. Early Ford cars were simple and cheap, but (8)...........things simple sometimes (9)..............less choice.\n'You (10)..............have any color you like,' said Henry Ford of the Model T, 'as long as it's black'.",
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
        "passage": "Henry Ford was born on a farm in Michigan in 1863 but he did not like farming. When he was fifteen he began work as a mechanic and in 1893 he built his first car. After he (1)..........driven it 1,500 kilometers, he sold it and built two bigger cars. Then, in 1903, he (2)................the Ford Motor Company. By (3)..............strong but light steel, he built cheap cars for (4)..............people to buy.\nIn 1908, he built the first Ford Model 'T', (5)..............sold for $825. He was soon selling 100 cars (6)................day. By 1927, the Ford Motor Company was (7).............$700 million. Early Ford cars were simple and cheap, but (8)...........things simple sometimes (9)..............less choice.\n'You (10)..............have any color you like,' said Henry Ford of the Model T, 'as long as it's black'.",
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
        "passage": "Henry Ford was born on a farm in Michigan in 1863 but he did not like farming. When he was fifteen he began work as a mechanic and in 1893 he built his first car. After he (1)..........driven it 1,500 kilometers, he sold it and built two bigger cars. Then, in 1903, he (2)................the Ford Motor Company. By (3)..............strong but light steel, he built cheap cars for (4)..............people to buy.\nIn 1908, he built the first Ford Model 'T', (5)..............sold for $825. He was soon selling 100 cars (6)................day. By 1927, the Ford Motor Company was (7).............$700 million. Early Ford cars were simple and cheap, but (8)...........things simple sometimes (9)..............less choice.\n'You (10)..............have any color you like,' said Henry Ford of the Model T, 'as long as it's black'.",
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
        "passage": "Two years ago, our 14-year-old son, Ben, asked us for a set of drums for his birthday. At first, we were very much against the idea because of the noise. 'It's better than watching television or playing computer games in my free time,' Ben argued, 'and it'll keep me out of trouble.' In the end we gave in. 'All right,' we said, 'but you must consider the rest of the family and the neighbors when you play.'\n\nThat was just the beginning. Because drums are not the easiest instruments to transport, the other members of Bens band started appearing at our home with their guitars and other electrical equipment. And so, for several hours a week, the house shakes to the noise of their instruments and their teenage singing.\n\nAt least Ben's hobby has been good for our health: whenever the band start practicing, my husband and I go out for a long walk. And I must admit that, although their music may sound a little strange, they are a friendly and polite group of young men. I cannot judge their musical Skill after all I didn't expect my parents' generation to like the same music as I did when I was a teenager - but they do play regularly in local clubs for young people.\n\nOur main worry is that they won't spend enough time on their school work because of their musical activities, though this hasn't happened yet. I am always stressing to Ben how important his studies are. But one thing is certain Ben was right: it has kept him out of trouble and he is never bored.",
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
        "passage": "Two years ago, our 14-year-old son, Ben, asked us for a set of drums for his birthday. At first, we were very much against the idea because of the noise. 'It's better than watching television or playing computer games in my free time,' Ben argued, 'and it'll keep me out of trouble.' In the end we gave in. 'All right,' we said, 'but you must consider the rest of the family and the neighbors when you play.'\n\nThat was just the beginning. Because drums are not the easiest instruments to transport, the other members of Bens band started appearing at our home with their guitars and other electrical equipment. And so, for several hours a week, the house shakes to the noise of their instruments and their teenage singing.\n\nAt least Ben's hobby has been good for our health: whenever the band start practicing, my husband and I go out for a long walk. And I must admit that, although their music may sound a little strange, they are a friendly and polite group of young men. I cannot judge their musical Skill after all I didn't expect my parents' generation to like the same music as I did when I was a teenager - but they do play regularly in local clubs for young people.\n\nOur main worry is that they won't spend enough time on their school work because of their musical activities, though this hasn't happened yet. I am always stressing to Ben how important his studies are. But one thing is certain Ben was right: it has kept him out of trouble and he is never bored.",
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
        "passage": "Two years ago, our 14-year-old son, Ben, asked us for a set of drums for his birthday. At first, we were very much against the idea because of the noise. 'It's better than watching television or playing computer games in my free time,' Ben argued, 'and it'll keep me out of trouble.' In the end we gave in. 'All right,' we said, 'but you must consider the rest of the family and the neighbors when you play.'\n\nThat was just the beginning. Because drums are not the easiest instruments to transport, the other members of Bens band started appearing at our home with their guitars and other electrical equipment. And so, for several hours a week, the house shakes to the noise of their instruments and their teenage singing.\n\nAt least Ben's hobby has been good for our health: whenever the band start practicing, my husband and I go out for a long walk. And I must admit that, although their music may sound a little strange, they are a friendly and polite group of young men. I cannot judge their musical Skill after all I didn't expect my parents' generation to like the same music as I did when I was a teenager - but they do play regularly in local clubs for young people.\n\nOur main worry is that they won't spend enough time on their school work because of their musical activities, though this hasn't happened yet. I am always stressing to Ben how important his studies are. But one thing is certain Ben was right: it has kept him out of trouble and he is never bored.",
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
        "passage": "Two years ago, our 14-year-old son, Ben, asked us for a set of drums for his birthday. At first, we were very much against the idea because of the noise. 'It's better than watching television or playing computer games in my free time,' Ben argued, 'and it'll keep me out of trouble.' In the end we gave in. 'All right,' we said, 'but you must consider the rest of the family and the neighbors when you play.'\n\nThat was just the beginning. Because drums are not the easiest instruments to transport, the other members of Bens band started appearing at our home with their guitars and other electrical equipment. And so, for several hours a week, the house shakes to the noise of their instruments and their teenage singing.\n\nAt least Ben's hobby has been good for our health: whenever the band start practicing, my husband and I go out for a long walk. And I must admit that, although their music may sound a little strange, they are a friendly and polite group of young men. I cannot judge their musical Skill after all I didn't expect my parents' generation to like the same music as I did when I was a teenager - but they do play regularly in local clubs for young people.\n\nOur main worry is that they won't spend enough time on their school work because of their musical activities, though this hasn't happened yet. I am always stressing to Ben how important his studies are. But one thing is certain Ben was right: it has kept him out of trouble and he is never bored.",
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
        "passage": "Two years ago, our 14-year-old son, Ben, asked us for a set of drums for his birthday. At first, we were very much against the idea because of the noise. 'It's better than watching television or playing computer games in my free time,' Ben argued, 'and it'll keep me out of trouble.' In the end we gave in. 'All right,' we said, 'but you must consider the rest of the family and the neighbors when you play.'\n\nThat was just the beginning. Because drums are not the easiest instruments to transport, the other members of Bens band started appearing at our home with their guitars and other electrical equipment. And so, for several hours a week, the house shakes to the noise of their instruments and their teenage singing.\n\nAt least Ben's hobby has been good for our health: whenever the band start practicing, my husband and I go out for a long walk. And I must admit that, although their music may sound a little strange, they are a friendly and polite group of young men. I cannot judge their musical Skill after all I didn't expect my parents' generation to like the same music as I did when I was a teenager - but they do play regularly in local clubs for young people.\n\nOur main worry is that they won't spend enough time on their school work because of their musical activities, though this hasn't happened yet. I am always stressing to Ben how important his studies are. But one thing is certain Ben was right: it has kept him out of trouble and he is never bored.",
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
        "passage": "Two years ago, our 14-year-old son, Ben, asked us for a set of drums for his birthday. At first, we were very much against the idea because of the noise. 'It's better than watching television or playing computer games in my free time,' Ben argued, 'and it'll keep me out of trouble.' In the end we gave in. 'All right,' we said, 'but you must consider the rest of the family and the neighbors when you play.'\n\nThat was just the beginning. Because drums are not the easiest instruments to transport, the other members of Bens band started appearing at our home with their guitars and other electrical equipment. And so, for several hours a week, the house shakes to the noise of their instruments and their teenage singing.\n\nAt least Ben's hobby has been good for our health: whenever the band start practicing, my husband and I go out for a long walk. And I must admit that, although their music may sound a little strange, they are a friendly and polite group of young men. I cannot judge their musical Skill after all I didn't expect my parents' generation to like the same music as I did when I was a teenager - but they do play regularly in local clubs for young people.\n\nOur main worry is that they won't spend enough time on their school work because of their musical activities, though this hasn't happened yet. I am always stressing to Ben how important his studies are. But one thing is certain Ben was right: it has kept him out of trouble and he is never bored.",
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
        "passage": "Two years ago, our 14-year-old son, Ben, asked us for a set of drums for his birthday. At first, we were very much against the idea because of the noise. 'It's better than watching television or playing computer games in my free time,' Ben argued, 'and it'll keep me out of trouble.' In the end we gave in. 'All right,' we said, 'but you must consider the rest of the family and the neighbors when you play.'\n\nThat was just the beginning. Because drums are not the easiest instruments to transport, the other members of Bens band started appearing at our home with their guitars and other electrical equipment. And so, for several hours a week, the house shakes to the noise of their instruments and their teenage singing.\n\nAt least Ben's hobby has been good for our health: whenever the band start practicing, my husband and I go out for a long walk. And I must admit that, although their music may sound a little strange, they are a friendly and polite group of young men. I cannot judge their musical Skill after all I didn't expect my parents' generation to like the same music as I did when I was a teenager - but they do play regularly in local clubs for young people.\n\nOur main worry is that they won't spend enough time on their school work because of their musical activities, though this hasn't happened yet. I am always stressing to Ben how important his studies are. But one thing is certain Ben was right: it has kept him out of trouble and he is never bored.",
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
        "passage": "Two years ago, our 14-year-old son, Ben, asked us for a set of drums for his birthday. At first, we were very much against the idea because of the noise. 'It's better than watching television or playing computer games in my free time,' Ben argued, 'and it'll keep me out of trouble.' In the end we gave in. 'All right,' we said, 'but you must consider the rest of the family and the neighbors when you play.'\n\nThat was just the beginning. Because drums are not the easiest instruments to transport, the other members of Bens band started appearing at our home with their guitars and other electrical equipment. And so, for several hours a week, the house shakes to the noise of their instruments and their teenage singing.\n\nAt least Ben's hobby has been good for our health: whenever the band start practicing, my husband and I go out for a long walk. And I must admit that, although their music may sound a little strange, they are a friendly and polite group of young men. I cannot judge their musical Skill after all I didn't expect my parents' generation to like the same music as I did when I was a teenager - but they do play regularly in local clubs for young people.\n\nOur main worry is that they won't spend enough time on their school work because of their musical activities, though this hasn't happened yet. I am always stressing to Ben how important his studies are. But one thing is certain Ben was right: it has kept him out of trouble and he is never bored.",
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
        "passage": "Two years ago, our 14-year-old son, Ben, asked us for a set of drums for his birthday. At first, we were very much against the idea because of the noise. 'It's better than watching television or playing computer games in my free time,' Ben argued, 'and it'll keep me out of trouble.' In the end we gave in. 'All right,' we said, 'but you must consider the rest of the family and the neighbors when you play.'\n\nThat was just the beginning. Because drums are not the easiest instruments to transport, the other members of Bens band started appearing at our home with their guitars and other electrical equipment. And so, for several hours a week, the house shakes to the noise of their instruments and their teenage singing.\n\nAt least Ben's hobby has been good for our health: whenever the band start practicing, my husband and I go out for a long walk. And I must admit that, although their music may sound a little strange, they are a friendly and polite group of young men. I cannot judge their musical Skill after all I didn't expect my parents' generation to like the same music as I did when I was a teenager - but they do play regularly in local clubs for young people.\n\nOur main worry is that they won't spend enough time on their school work because of their musical activities, though this hasn't happened yet. I am always stressing to Ben how important his studies are. But one thing is certain Ben was right: it has kept him out of trouble and he is never bored.",
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
        "passage": "Student Volunteers Needed!\nOn Saturday, December 12th, from 10 A.M. until 4 P.M., Carverton Middle School will be holding a music festival in the school gymnasium. The special event will feature a variety of professional musicians and singers.\n\nTask | Time | Date\nMake posters | 1 P.M.-4 P.M. | December 5th\nSet up gym | 11 A.M.-4 P.M. | December 11th\nHelp performers | 9 A.M.-4 P.M. | December 12th\nWelcome guests | 10 A.M.-2 P.M. | December 12th\nClean up gym | 4 P.M.-7 P.M. | December 12th\n\nInterested students should speak with Ms. Braxton, the music teacher. Students who would like to help at the festival must have written permission from a parent or guardian.",
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
        "passage": "Student Volunteers Needed!\nOn Saturday, December 12th, from 10 A.M. until 4 P.M., Carverton Middle School will be holding a music festival in the school gymnasium. The special event will feature a variety of professional musicians and singers.\n\nTask | Time | Date\nMake posters | 1 P.M.-4 P.M. | December 5th\nSet up gym | 11 A.M.-4 P.M. | December 11th\nHelp performers | 9 A.M.-4 P.M. | December 12th\nWelcome guests | 10 A.M.-2 P.M. | December 12th\nClean up gym | 4 P.M.-7 P.M. | December 12th\n\nInterested students should speak with Ms. Braxton, the music teacher. Students who would like to help at the festival must have written permission from a parent or guardian.",
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
        "passage": "Student Volunteers Needed!\nOn Saturday, December 12th, from 10 A.M. until 4 P.M., Carverton Middle School will be holding a music festival in the school gymnasium. The special event will feature a variety of professional musicians and singers.\n\nTask | Time | Date\nMake posters | 1 P.M.-4 P.M. | December 5th\nSet up gym | 11 A.M.-4 P.M. | December 11th\nHelp performers | 9 A.M.-4 P.M. | December 12th\nWelcome guests | 10 A.M.-2 P.M. | December 12th\nClean up gym | 4 P.M.-7 P.M. | December 12th\n\nInterested students should speak with Ms. Braxton, the music teacher. Students who would like to help at the festival must have written permission from a parent or guardian.",
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
        "passage": "Student Volunteers Needed!\nOn Saturday, December 12th, from 10 A.M. until 4 P.M., Carverton Middle School will be holding a music festival in the school gymnasium. The special event will feature a variety of professional musicians and singers.\n\nTask | Time | Date\nMake posters | 1 P.M.-4 P.M. | December 5th\nSet up gym | 11 A.M.-4 P.M. | December 11th\nHelp performers | 9 A.M.-4 P.M. | December 12th\nWelcome guests | 10 A.M.-2 P.M. | December 12th\nClean up gym | 4 P.M.-7 P.M. | December 12th\n\nInterested students should speak with Ms. Braxton, the music teacher. Students who would like to help at the festival must have written permission from a parent or guardian.",
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
        "passage": "When the spring semester began, students at Eastern High School were met by a new science teacher. Her name is Elaine Burgess, and she has replaced Donald Young, who retired to spend time with his grandchildren.\n\nSince Ms. Burgess has just started here, many students are curious about her background. She was kind enough to sit down for an interview with The Quill and Paper. According to Ms. Burgess, she received her master's degree from nearby Sanderson University only six months ago. Her M.A. is in chemistry, but she double majored in chemistry and biology as an undergraduate while simultaneously getting a minor in physics.\n\n'I love all aspects of science', she said. 'And I'm looking forward to teaching students the things I know'. Ms. Burgess further declared that she prefers a hands-on approach to teaching science. So she expects to conduct numerous experiments in the hope of sparking students' interest in science.\n\nFinally, Ms. Burgess added that she welcomes student participation in her classes. 'Not only can students learn from their teachers, but I believe that teachers can also learn from their students. I hope that, by working together, we can all increase our knowledge of science.'",
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
        "passage": "When the spring semester began, students at Eastern High School were met by a new science teacher. Her name is Elaine Burgess, and she has replaced Donald Young, who retired to spend time with his grandchildren.\n\nSince Ms. Burgess has just started here, many students are curious about her background. She was kind enough to sit down for an interview with The Quill and Paper. According to Ms. Burgess, she received her master's degree from nearby Sanderson University only six months ago. Her M.A. is in chemistry, but she double majored in chemistry and biology as an undergraduate while simultaneously getting a minor in physics.\n\n'I love all aspects of science', she said. 'And I'm looking forward to teaching students the things I know'. Ms. Burgess further declared that she prefers a hands-on approach to teaching science. So she expects to conduct numerous experiments in the hope of sparking students' interest in science.\n\nFinally, Ms. Burgess added that she welcomes student participation in her classes. 'Not only can students learn from their teachers, but I believe that teachers can also learn from their students. I hope that, by working together, we can all increase our knowledge of science.'",
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
        "passage": "When the spring semester began, students at Eastern High School were met by a new science teacher. Her name is Elaine Burgess, and she has replaced Donald Young, who retired to spend time with his grandchildren.\n\nSince Ms. Burgess has just started here, many students are curious about her background. She was kind enough to sit down for an interview with The Quill and Paper. According to Ms. Burgess, she received her master's degree from nearby Sanderson University only six months ago. Her M.A. is in chemistry, but she double majored in chemistry and biology as an undergraduate while simultaneously getting a minor in physics.\n\n'I love all aspects of science', she said. 'And I'm looking forward to teaching students the things I know'. Ms. Burgess further declared that she prefers a hands-on approach to teaching science. So she expects to conduct numerous experiments in the hope of sparking students' interest in science.\n\nFinally, Ms. Burgess added that she welcomes student participation in her classes. 'Not only can students learn from their teachers, but I believe that teachers can also learn from their students. I hope that, by working together, we can all increase our knowledge of science.'",
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
        "passage": "When the spring semester began, students at Eastern High School were met by a new science teacher. Her name is Elaine Burgess, and she has replaced Donald Young, who retired to spend time with his grandchildren.\n\nSince Ms. Burgess has just started here, many students are curious about her background. She was kind enough to sit down for an interview with The Quill and Paper. According to Ms. Burgess, she received her master's degree from nearby Sanderson University only six months ago. Her M.A. is in chemistry, but she double majored in chemistry and biology as an undergraduate while simultaneously getting a minor in physics.\n\n'I love all aspects of science', she said. 'And I'm looking forward to teaching students the things I know'. Ms. Burgess further declared that she prefers a hands-on approach to teaching science. So she expects to conduct numerous experiments in the hope of sparking students' interest in science.\n\nFinally, Ms. Burgess added that she welcomes student participation in her classes. 'Not only can students learn from their teachers, but I believe that teachers can also learn from their students. I hope that, by working together, we can all increase our knowledge of science.'",
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
        "passage": "When the spring semester began, students at Eastern High School were met by a new science teacher. Her name is Elaine Burgess, and she has replaced Donald Young, who retired to spend time with his grandchildren.\n\nSince Ms. Burgess has just started here, many students are curious about her background. She was kind enough to sit down for an interview with The Quill and Paper. According to Ms. Burgess, she received her master's degree from nearby Sanderson University only six months ago. Her M.A. is in chemistry, but she double majored in chemistry and biology as an undergraduate while simultaneously getting a minor in physics.\n\n'I love all aspects of science', she said. 'And I'm looking forward to teaching students the things I know'. Ms. Burgess further declared that she prefers a hands-on approach to teaching science. So she expects to conduct numerous experiments in the hope of sparking students' interest in science.\n\nFinally, Ms. Burgess added that she welcomes student participation in her classes. 'Not only can students learn from their teachers, but I believe that teachers can also learn from their students. I hope that, by working together, we can all increase our knowledge of science.'",
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
        "passage": "Kal Kaur Rai has always been interested in fashion and has just won the title of Young Achiever of the Year at the Asian Business Awards. Ever since she was a child, she has drawn clothes and designed patterns. She never told her hard-working parents, who own a supermarket, that she wanted to turn her hobby into a career. She thought they expected her to go into a more established business, so she went to university to do a management degree.\n\nAfter university, she moved to London and worked in an advertising agency. She had to attend industry events but couldn't afford the designer clothes she liked. She started making skirts and tops for herself. When her friends saw her clothes, they asked her to make things for them. She then found a small shop in London willing to take her designs on a sale-or- return basis. They were very popular and nothing came back. This encouraged her to leave her advertising job, take out a £20,000 loan and begin her own women swear label.\n\nKal's parents were not angry about her career change and said they would support her, which really pleased her. Her clothes are now on sale in over 70 stores and her business has an income of over £500,000. Her clothes appear in fashion magazines, she designs for pop stars and she has just gained public recognition by winning this award. Her business has come a long way and she knows she is extremely lucky. 'What I do is my hobby and I get paid for it! But remember, I've worked hard for this.'",
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
        "passage": "Kal Kaur Rai has always been interested in fashion and has just won the title of Young Achiever of the Year at the Asian Business Awards. Ever since she was a child, she has drawn clothes and designed patterns. She never told her hard-working parents, who own a supermarket, that she wanted to turn her hobby into a career. She thought they expected her to go into a more established business, so she went to university to do a management degree.\n\nAfter university, she moved to London and worked in an advertising agency. She had to attend industry events but couldn't afford the designer clothes she liked. She started making skirts and tops for herself. When her friends saw her clothes, they asked her to make things for them. She then found a small shop in London willing to take her designs on a sale-or- return basis. They were very popular and nothing came back. This encouraged her to leave her advertising job, take out a £20,000 loan and begin her own women swear label.\n\nKal's parents were not angry about her career change and said they would support her, which really pleased her. Her clothes are now on sale in over 70 stores and her business has an income of over £500,000. Her clothes appear in fashion magazines, she designs for pop stars and she has just gained public recognition by winning this award. Her business has come a long way and she knows she is extremely lucky. 'What I do is my hobby and I get paid for it! But remember, I've worked hard for this.'",
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
        "passage": "Kal Kaur Rai has always been interested in fashion and has just won the title of Young Achiever of the Year at the Asian Business Awards. Ever since she was a child, she has drawn clothes and designed patterns. She never told her hard-working parents, who own a supermarket, that she wanted to turn her hobby into a career. She thought they expected her to go into a more established business, so she went to university to do a management degree.\n\nAfter university, she moved to London and worked in an advertising agency. She had to attend industry events but couldn't afford the designer clothes she liked. She started making skirts and tops for herself. When her friends saw her clothes, they asked her to make things for them. She then found a small shop in London willing to take her designs on a sale-or- return basis. They were very popular and nothing came back. This encouraged her to leave her advertising job, take out a £20,000 loan and begin her own women swear label.\n\nKal's parents were not angry about her career change and said they would support her, which really pleased her. Her clothes are now on sale in over 70 stores and her business has an income of over £500,000. Her clothes appear in fashion magazines, she designs for pop stars and she has just gained public recognition by winning this award. Her business has come a long way and she knows she is extremely lucky. 'What I do is my hobby and I get paid for it! But remember, I've worked hard for this.'",
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
        "passage": "Kal Kaur Rai has always been interested in fashion and has just won the title of Young Achiever of the Year at the Asian Business Awards. Ever since she was a child, she has drawn clothes and designed patterns. She never told her hard-working parents, who own a supermarket, that she wanted to turn her hobby into a career. She thought they expected her to go into a more established business, so she went to university to do a management degree.\n\nAfter university, she moved to London and worked in an advertising agency. She had to attend industry events but couldn't afford the designer clothes she liked. She started making skirts and tops for herself. When her friends saw her clothes, they asked her to make things for them. She then found a small shop in London willing to take her designs on a sale-or- return basis. They were very popular and nothing came back. This encouraged her to leave her advertising job, take out a £20,000 loan and begin her own women swear label.\n\nKal's parents were not angry about her career change and said they would support her, which really pleased her. Her clothes are now on sale in over 70 stores and her business has an income of over £500,000. Her clothes appear in fashion magazines, she designs for pop stars and she has just gained public recognition by winning this award. Her business has come a long way and she knows she is extremely lucky. 'What I do is my hobby and I get paid for it! But remember, I've worked hard for this.'",
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
        "passage": "Dear Students,\nI invite you to explore Philips Exeter Academy through this website www.exeter.edu. Browse through the different offerings of Exeter from the many cultural events hosted on campus, to the hundreds of courses we offer, and on to the involved and experienced faculty. See what the lives of students are like.\n\nWhether it's English or mathematics, at Exeter we call all our classes Harkness classes and our teachers Harkness teachers. Harkness identifies a table you will find at the center of every class both literally and figuratively. Harkness tables are oval and seat a dozen students and a teacher, but they are much more than a place to sit. At the Harkness table classmates learn by discussing their thoughts and ideas rather than just by taking notes. Teachers are participants in the discussion, guiding students in significant ways without lecturing.\n\nOn this website, we've tried to make it easy for you to find what you need. For new or prospective students, look at the Admissions, Academics, and Student Life sections of the site. For parents, check the information under the Parent 'gateway' located at the top of the page this gateway provides you with a short list of items of interest to you. we'll keep this page updated with items we know concern parents. For current students, look everywhere this website is about you and your Exeter experience.\n\nI invite you to let us know what you think of the website. In true Harkness learning fashion, we're always listening, always looking for the questions that get us to the really important answers.\n\nYou can contact me directly via e-mail or phone: 603-777-3401\nPrincipal Thomas E.Hassan",
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
        "passage": "Dear Students,\nI invite you to explore Philips Exeter Academy through this website www.exeter.edu. Browse through the different offerings of Exeter from the many cultural events hosted on campus, to the hundreds of courses we offer, and on to the involved and experienced faculty. See what the lives of students are like.\n\nWhether it's English or mathematics, at Exeter we call all our classes Harkness classes and our teachers Harkness teachers. Harkness identifies a table you will find at the center of every class both literally and figuratively. Harkness tables are oval and seat a dozen students and a teacher, but they are much more than a place to sit. At the Harkness table classmates learn by discussing their thoughts and ideas rather than just by taking notes. Teachers are participants in the discussion, guiding students in significant ways without lecturing.\n\nOn this website, we've tried to make it easy for you to find what you need. For new or prospective students, look at the Admissions, Academics, and Student Life sections of the site. For parents, check the information under the Parent 'gateway' located at the top of the page this gateway provides you with a short list of items of interest to you. we'll keep this page updated with items we know concern parents. For current students, look everywhere this website is about you and your Exeter experience.\n\nI invite you to let us know what you think of the website. In true Harkness learning fashion, we're always listening, always looking for the questions that get us to the really important answers.\n\nYou can contact me directly via e-mail or phone: 603-777-3401\nPrincipal Thomas E.Hassan",
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
        "passage": "Dear Students,\nI invite you to explore Philips Exeter Academy through this website www.exeter.edu. Browse through the different offerings of Exeter from the many cultural events hosted on campus, to the hundreds of courses we offer, and on to the involved and experienced faculty. See what the lives of students are like.\n\nWhether it's English or mathematics, at Exeter we call all our classes Harkness classes and our teachers Harkness teachers. Harkness identifies a table you will find at the center of every class both literally and figuratively. Harkness tables are oval and seat a dozen students and a teacher, but they are much more than a place to sit. At the Harkness table classmates learn by discussing their thoughts and ideas rather than just by taking notes. Teachers are participants in the discussion, guiding students in significant ways without lecturing.\n\nOn this website, we've tried to make it easy for you to find what you need. For new or prospective students, look at the Admissions, Academics, and Student Life sections of the site. For parents, check the information under the Parent 'gateway' located at the top of the page this gateway provides you with a short list of items of interest to you. we'll keep this page updated with items we know concern parents. For current students, look everywhere this website is about you and your Exeter experience.\n\nI invite you to let us know what you think of the website. In true Harkness learning fashion, we're always listening, always looking for the questions that get us to the really important answers.\n\nYou can contact me directly via e-mail or phone: 603-777-3401\nPrincipal Thomas E.Hassan",
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
        "passage": "Dear Students,\nI invite you to explore Philips Exeter Academy through this website www.exeter.edu. Browse through the different offerings of Exeter from the many cultural events hosted on campus, to the hundreds of courses we offer, and on to the involved and experienced faculty. See what the lives of students are like.\n\nWhether it's English or mathematics, at Exeter we call all our classes Harkness classes and our teachers Harkness teachers. Harkness identifies a table you will find at the center of every class both literally and figuratively. Harkness tables are oval and seat a dozen students and a teacher, but they are much more than a place to sit. At the Harkness table classmates learn by discussing their thoughts and ideas rather than just by taking notes. Teachers are participants in the discussion, guiding students in significant ways without lecturing.\n\nOn this website, we've tried to make it easy for you to find what you need. For new or prospective students, look at the Admissions, Academics, and Student Life sections of the site. For parents, check the information under the Parent 'gateway' located at the top of the page this gateway provides you with a short list of items of interest to you. we'll keep this page updated with items we know concern parents. For current students, look everywhere this website is about you and your Exeter experience.\n\nI invite you to let us know what you think of the website. In true Harkness learning fashion, we're always listening, always looking for the questions that get us to the really important answers.\n\nYou can contact me directly via e-mail or phone: 603-777-3401\nPrincipal Thomas E.Hassan",
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
        "passage": "Dear Students,\nI invite you to explore Philips Exeter Academy through this website www.exeter.edu. Browse through the different offerings of Exeter from the many cultural events hosted on campus, to the hundreds of courses we offer, and on to the involved and experienced faculty. See what the lives of students are like.\n\nWhether it's English or mathematics, at Exeter we call all our classes Harkness classes and our teachers Harkness teachers. Harkness identifies a table you will find at the center of every class both literally and figuratively. Harkness tables are oval and seat a dozen students and a teacher, but they are much more than a place to sit. At the Harkness table classmates learn by discussing their thoughts and ideas rather than just by taking notes. Teachers are participants in the discussion, guiding students in significant ways without lecturing.\n\nOn this website, we've tried to make it easy for you to find what you need. For new or prospective students, look at the Admissions, Academics, and Student Life sections of the site. For parents, check the information under the Parent 'gateway' located at the top of the page this gateway provides you with a short list of items of interest to you. we'll keep this page updated with items we know concern parents. For current students, look everywhere this website is about you and your Exeter experience.\n\nI invite you to let us know what you think of the website. In true Harkness learning fashion, we're always listening, always looking for the questions that get us to the really important answers.\n\nYou can contact me directly via e-mail or phone: 603-777-3401\nPrincipal Thomas E.Hassan",
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
        "passage": "At 32, I have just finished my first year at university. As well as attending lectures regularly, I have had to learn to read books quickly and write long essays.\n\nI decided to go to university after fourteen years away from the classroom. As a secretary, although I was earning a reasonable amount of money, I was bored doing something where I hardly had to think. I became more and more depressed by the idea that I was stuck in the job. I was jealous of the students at the local university, who looked happy, carefree and full of hope, and part of something that I wanted to explore further.\n\nHowever, now that I've actually become a student I find it hard to mix with younger colleagues. They are always mistaking me for a lecturer and asking me questions I can't answer. I also feel separated from the lecturers because, although we are the same age, I know so much less than them. But I am glad of this opportunity to study because I know you need a qualification to get a rewarding job, which is really important to me. Unlike most eighteen-year-olds, I much prefer a weekend with my books to one out partying. Then there are the normal student benefits of long holidays and theatre and cinema discounts. I often have doubts about what I'll do after university, but I hope that continuing my education at this late date has been a wise choice.",
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
        "passage": "At 32, I have just finished my first year at university. As well as attending lectures regularly, I have had to learn to read books quickly and write long essays.\n\nI decided to go to university after fourteen years away from the classroom. As a secretary, although I was earning a reasonable amount of money, I was bored doing something where I hardly had to think. I became more and more depressed by the idea that I was stuck in the job. I was jealous of the students at the local university, who looked happy, carefree and full of hope, and part of something that I wanted to explore further.\n\nHowever, now that I've actually become a student I find it hard to mix with younger colleagues. They are always mistaking me for a lecturer and asking me questions I can't answer. I also feel separated from the lecturers because, although we are the same age, I know so much less than them. But I am glad of this opportunity to study because I know you need a qualification to get a rewarding job, which is really important to me. Unlike most eighteen-year-olds, I much prefer a weekend with my books to one out partying. Then there are the normal student benefits of long holidays and theatre and cinema discounts. I often have doubts about what I'll do after university, but I hope that continuing my education at this late date has been a wise choice.",
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
        "passage": "At 32, I have just finished my first year at university. As well as attending lectures regularly, I have had to learn to read books quickly and write long essays.\n\nI decided to go to university after fourteen years away from the classroom. As a secretary, although I was earning a reasonable amount of money, I was bored doing something where I hardly had to think. I became more and more depressed by the idea that I was stuck in the job. I was jealous of the students at the local university, who looked happy, carefree and full of hope, and part of something that I wanted to explore further.\n\nHowever, now that I've actually become a student I find it hard to mix with younger colleagues. They are always mistaking me for a lecturer and asking me questions I can't answer. I also feel separated from the lecturers because, although we are the same age, I know so much less than them. But I am glad of this opportunity to study because I know you need a qualification to get a rewarding job, which is really important to me. Unlike most eighteen-year-olds, I much prefer a weekend with my books to one out partying. Then there are the normal student benefits of long holidays and theatre and cinema discounts. I often have doubts about what I'll do after university, but I hope that continuing my education at this late date has been a wise choice.",
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
        "passage": "At 32, I have just finished my first year at university. As well as attending lectures regularly, I have had to learn to read books quickly and write long essays.\n\nI decided to go to university after fourteen years away from the classroom. As a secretary, although I was earning a reasonable amount of money, I was bored doing something where I hardly had to think. I became more and more depressed by the idea that I was stuck in the job. I was jealous of the students at the local university, who looked happy, carefree and full of hope, and part of something that I wanted to explore further.\n\nHowever, now that I've actually become a student I find it hard to mix with younger colleagues. They are always mistaking me for a lecturer and asking me questions I can't answer. I also feel separated from the lecturers because, although we are the same age, I know so much less than them. But I am glad of this opportunity to study because I know you need a qualification to get a rewarding job, which is really important to me. Unlike most eighteen-year-olds, I much prefer a weekend with my books to one out partying. Then there are the normal student benefits of long holidays and theatre and cinema discounts. I often have doubts about what I'll do after university, but I hope that continuing my education at this late date has been a wise choice.",
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
        "passage": "At 32, I have just finished my first year at university. As well as attending lectures regularly, I have had to learn to read books quickly and write long essays.\n\nI decided to go to university after fourteen years away from the classroom. As a secretary, although I was earning a reasonable amount of money, I was bored doing something where I hardly had to think. I became more and more depressed by the idea that I was stuck in the job. I was jealous of the students at the local university, who looked happy, carefree and full of hope, and part of something that I wanted to explore further.\n\nHowever, now that I've actually become a student I find it hard to mix with younger colleagues. They are always mistaking me for a lecturer and asking me questions I can't answer. I also feel separated from the lecturers because, although we are the same age, I know so much less than them. But I am glad of this opportunity to study because I know you need a qualification to get a rewarding job, which is really important to me. Unlike most eighteen-year-olds, I much prefer a weekend with my books to one out partying. Then there are the normal student benefits of long holidays and theatre and cinema discounts. I often have doubts about what I'll do after university, but I hope that continuing my education at this late date has been a wise choice.",
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
        "passage": "Dear students:\nThis year, we plan to take at least two field trips per semester. Please be aware of the following regarding field trips.\n\nAll students who are not yet eighteen years of age must submit a permission slip signed by a parent or guardian. This permission slip indicates that the parent or guardian consents to allowing the students to go on the field trip. Failure to submit a permission slip by the day of the field trip means that the student may not accompany the others off campus.\n\nAll students must also provide proof that they have medical insurance and that their insurance covers them in case of injury while on a field trip. Students may turn in this proof at the front office anytime. If it is not provided, the student will not be able to go on the field trip.\n\nOn field trips, all students must be on their best behavior. Students are expected to listen to their teachers and to follow the rules and regulations of the places that they visit. Failure to do so will result in some sort of punishment, such as detention or suspension.\n\nDavid Prosser\nPrincipal",
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
        "passage": "Dear students:\nThis year, we plan to take at least two field trips per semester. Please be aware of the following regarding field trips.\n\nAll students who are not yet eighteen years of age must submit a permission slip signed by a parent or guardian. This permission slip indicates that the parent or guardian consents to allowing the students to go on the field trip. Failure to submit a permission slip by the day of the field trip means that the student may not accompany the others off campus.\n\nAll students must also provide proof that they have medical insurance and that their insurance covers them in case of injury while on a field trip. Students may turn in this proof at the front office anytime. If it is not provided, the student will not be able to go on the field trip.\n\nOn field trips, all students must be on their best behavior. Students are expected to listen to their teachers and to follow the rules and regulations of the places that they visit. Failure to do so will result in some sort of punishment, such as detention or suspension.\n\nDavid Prosser\nPrincipal",
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
        "passage": "Dear students:\nThis year, we plan to take at least two field trips per semester. Please be aware of the following regarding field trips.\n\nAll students who are not yet eighteen years of age must submit a permission slip signed by a parent or guardian. This permission slip indicates that the parent or guardian consents to allowing the students to go on the field trip. Failure to submit a permission slip by the day of the field trip means that the student may not accompany the others off campus.\n\nAll students must also provide proof that they have medical insurance and that their insurance covers them in case of injury while on a field trip. Students may turn in this proof at the front office anytime. If it is not provided, the student will not be able to go on the field trip.\n\nOn field trips, all students must be on their best behavior. Students are expected to listen to their teachers and to follow the rules and regulations of the places that they visit. Failure to do so will result in some sort of punishment, such as detention or suspension.\n\nDavid Prosser\nPrincipal",
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
        "passage": "Dear students:\nThis year, we plan to take at least two field trips per semester. Please be aware of the following regarding field trips.\n\nAll students who are not yet eighteen years of age must submit a permission slip signed by a parent or guardian. This permission slip indicates that the parent or guardian consents to allowing the students to go on the field trip. Failure to submit a permission slip by the day of the field trip means that the student may not accompany the others off campus.\n\nAll students must also provide proof that they have medical insurance and that their insurance covers them in case of injury while on a field trip. Students may turn in this proof at the front office anytime. If it is not provided, the student will not be able to go on the field trip.\n\nOn field trips, all students must be on their best behavior. Students are expected to listen to their teachers and to follow the rules and regulations of the places that they visit. Failure to do so will result in some sort of punishment, such as detention or suspension.\n\nDavid Prosser\nPrincipal",
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
        "passage": "One day I hopped in a taxi and we took off for the airport.\n\nWe were driving in the right lane when suddenly a black car jumped out of a parking space right in front of us. My taxi driver slammed on his brakes, skidded, and missed the other car by just inches!\n\nThe driver of the black car whipped his head around and started yelling at us. My taxi driver just smiled and waved at the guy; and I mean, he was really friendly.\n\nSo I asked, 'Why did you just do that? This guy almost ruined your car and sent us to the hospital!'\n\nThis is when my taxi driver taught me what I now call 'the Law of the Garbage Truck'.\n\nHe explained that many people are like garbage trucks. They run around full of garbage, full of frustration, full of anger, and full of disappointment. As their garbage piles up, they need a place to dump it and sometimes they'll dump it on you. don't take it personally. Just smile, wave, wish them well, and move on. Don't take their garbage and spread it to other people at work, at home, or on the streets.\n\nThe bottom line is that successful people do not let garbage trucks take over their day. Life's too short to wake up in the morning with regrets, so 'love the people who treat you right. Pray for the ones who don't'.",
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
        "passage": "One day I hopped in a taxi and we took off for the airport.\n\nWe were driving in the right lane when suddenly a black car jumped out of a parking space right in front of us. My taxi driver slammed on his brakes, skidded, and missed the other car by just inches!\n\nThe driver of the black car whipped his head around and started yelling at us. My taxi driver just smiled and waved at the guy; and I mean, he was really friendly.\n\nSo I asked, 'Why did you just do that? This guy almost ruined your car and sent us to the hospital!'\n\nThis is when my taxi driver taught me what I now call 'the Law of the Garbage Truck'.\n\nHe explained that many people are like garbage trucks. They run around full of garbage, full of frustration, full of anger, and full of disappointment. As their garbage piles up, they need a place to dump it and sometimes they'll dump it on you. don't take it personally. Just smile, wave, wish them well, and move on. Don't take their garbage and spread it to other people at work, at home, or on the streets.\n\nThe bottom line is that successful people do not let garbage trucks take over their day. Life's too short to wake up in the morning with regrets, so 'love the people who treat you right. Pray for the ones who don't'.",
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
        "passage": "One day I hopped in a taxi and we took off for the airport.\n\nWe were driving in the right lane when suddenly a black car jumped out of a parking space right in front of us. My taxi driver slammed on his brakes, skidded, and missed the other car by just inches!\n\nThe driver of the black car whipped his head around and started yelling at us. My taxi driver just smiled and waved at the guy; and I mean, he was really friendly.\n\nSo I asked, 'Why did you just do that? This guy almost ruined your car and sent us to the hospital!'\n\nThis is when my taxi driver taught me what I now call 'the Law of the Garbage Truck'.\n\nHe explained that many people are like garbage trucks. They run around full of garbage, full of frustration, full of anger, and full of disappointment. As their garbage piles up, they need a place to dump it and sometimes they'll dump it on you. don't take it personally. Just smile, wave, wish them well, and move on. Don't take their garbage and spread it to other people at work, at home, or on the streets.\n\nThe bottom line is that successful people do not let garbage trucks take over their day. Life's too short to wake up in the morning with regrets, so 'love the people who treat you right. Pray for the ones who don't'.",
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
        "passage": "One day I hopped in a taxi and we took off for the airport.\n\nWe were driving in the right lane when suddenly a black car jumped out of a parking space right in front of us. My taxi driver slammed on his brakes, skidded, and missed the other car by just inches!\n\nThe driver of the black car whipped his head around and started yelling at us. My taxi driver just smiled and waved at the guy; and I mean, he was really friendly.\n\nSo I asked, 'Why did you just do that? This guy almost ruined your car and sent us to the hospital!'\n\nThis is when my taxi driver taught me what I now call 'the Law of the Garbage Truck'.\n\nHe explained that many people are like garbage trucks. They run around full of garbage, full of frustration, full of anger, and full of disappointment. As their garbage piles up, they need a place to dump it and sometimes they'll dump it on you. don't take it personally. Just smile, wave, wish them well, and move on. Don't take their garbage and spread it to other people at work, at home, or on the streets.\n\nThe bottom line is that successful people do not let garbage trucks take over their day. Life's too short to wake up in the morning with regrets, so 'love the people who treat you right. Pray for the ones who don't'.",
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
        "passage": "One day I hopped in a taxi and we took off for the airport.\n\nWe were driving in the right lane when suddenly a black car jumped out of a parking space right in front of us. My taxi driver slammed on his brakes, skidded, and missed the other car by just inches!\n\nThe driver of the black car whipped his head around and started yelling at us. My taxi driver just smiled and waved at the guy; and I mean, he was really friendly.\n\nSo I asked, 'Why did you just do that? This guy almost ruined your car and sent us to the hospital!'\n\nThis is when my taxi driver taught me what I now call 'the Law of the Garbage Truck'.\n\nHe explained that many people are like garbage trucks. They run around full of garbage, full of frustration, full of anger, and full of disappointment. As their garbage piles up, they need a place to dump it and sometimes they'll dump it on you. don't take it personally. Just smile, wave, wish them well, and move on. Don't take their garbage and spread it to other people at work, at home, or on the streets.\n\nThe bottom line is that successful people do not let garbage trucks take over their day. Life's too short to wake up in the morning with regrets, so 'love the people who treat you right. Pray for the ones who don't'.",
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
        "passage": "Please read the following carefully as it describes my expectations of your during this class.\n\nEveryone must do the reading assignments since we will have class discussions. Your participation in these discussions will be a part (10 percent) of your grade in my class. In addition, we will have one written homework assignment each week. In most cases, it will be a short (3-page) paper on a topic we are studying. You will be graded on these assignments. We will have four tests during the semester. Each one will be worth twenty percent of your grade.\n\nThere will be times when I will on you during class. Please attempt to answer my inquiries. Do not simply confess that you do not know the correct response. I expect everybody to try hard in my class. Furthermore, I want you all to take notes during my class. I will provide you with an outline of the material we will study each day; however, you need to write down the important information that I mention in your notebooks. I welcome questions in class and urge you to ask them if you ever fail to understand something.",
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
        "passage": "Please read the following carefully as it describes my expectations of your during this class.\n\nEveryone must do the reading assignments since we will have class discussions. Your participation in these discussions will be a part (10 percent) of your grade in my class. In addition, we will have one written homework assignment each week. In most cases, it will be a short (3-page) paper on a topic we are studying. You will be graded on these assignments. We will have four tests during the semester. Each one will be worth twenty percent of your grade.\n\nThere will be times when I will on you during class. Please attempt to answer my inquiries. Do not simply confess that you do not know the correct response. I expect everybody to try hard in my class. Furthermore, I want you all to take notes during my class. I will provide you with an outline of the material we will study each day; however, you need to write down the important information that I mention in your notebooks. I welcome questions in class and urge you to ask them if you ever fail to understand something.",
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
        "passage": "Please read the following carefully as it describes my expectations of your during this class.\n\nEveryone must do the reading assignments since we will have class discussions. Your participation in these discussions will be a part (10 percent) of your grade in my class. In addition, we will have one written homework assignment each week. In most cases, it will be a short (3-page) paper on a topic we are studying. You will be graded on these assignments. We will have four tests during the semester. Each one will be worth twenty percent of your grade.\n\nThere will be times when I will on you during class. Please attempt to answer my inquiries. Do not simply confess that you do not know the correct response. I expect everybody to try hard in my class. Furthermore, I want you all to take notes during my class. I will provide you with an outline of the material we will study each day; however, you need to write down the important information that I mention in your notebooks. I welcome questions in class and urge you to ask them if you ever fail to understand something.",
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
        "passage": "Please read the following carefully as it describes my expectations of your during this class.\n\nEveryone must do the reading assignments since we will have class discussions. Your participation in these discussions will be a part (10 percent) of your grade in my class. In addition, we will have one written homework assignment each week. In most cases, it will be a short (3-page) paper on a topic we are studying. You will be graded on these assignments. We will have four tests during the semester. Each one will be worth twenty percent of your grade.\n\nThere will be times when I will on you during class. Please attempt to answer my inquiries. Do not simply confess that you do not know the correct response. I expect everybody to try hard in my class. Furthermore, I want you all to take notes during my class. I will provide you with an outline of the material we will study each day; however, you need to write down the important information that I mention in your notebooks. I welcome questions in class and urge you to ask them if you ever fail to understand something.",
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
        "passage": "Mankind has used flags for over 4,000 years. The first flags were simply wooden poles with carving at the top. About 2,000 years ago, fabric was added to the poles giving the appearance of what we know today as a flag.\n\nThe flag has become an important symbol for identifying a country. Because there are thousands of flags in existence today, many look very similar. The flag of Russia consists of three horizontal stripes that are white, red, and blue from top to bottom. The flag of Yugoslavia has a similar design, with the colors in the order of red then white then blue. Colors on flags are important since they have special meanings. Red means power and white means peace. Orange is a symbol of courage or sacrifice. Green is the color of safety and hope and yellow of caution. Black is a symbol of death and often not a color used in country flags.\n\nSymbols of flags also have meanings. The American flag has thirteen stripes, which represent the original thirteen colonies. There are also 50 stars representing 50 states in the nation. Because of the meaning that we place on our flags, they have become a symbol of our home and of ourselves.",
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
        "passage": "Mankind has used flags for over 4,000 years. The first flags were simply wooden poles with carving at the top. About 2,000 years ago, fabric was added to the poles giving the appearance of what we know today as a flag.\n\nThe flag has become an important symbol for identifying a country. Because there are thousands of flags in existence today, many look very similar. The flag of Russia consists of three horizontal stripes that are white, red, and blue from top to bottom. The flag of Yugoslavia has a similar design, with the colors in the order of red then white then blue. Colors on flags are important since they have special meanings. Red means power and white means peace. Orange is a symbol of courage or sacrifice. Green is the color of safety and hope and yellow of caution. Black is a symbol of death and often not a color used in country flags.\n\nSymbols of flags also have meanings. The American flag has thirteen stripes, which represent the original thirteen colonies. There are also 50 stars representing 50 states in the nation. Because of the meaning that we place on our flags, they have become a symbol of our home and of ourselves.",
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
        "passage": "Mankind has used flags for over 4,000 years. The first flags were simply wooden poles with carving at the top. About 2,000 years ago, fabric was added to the poles giving the appearance of what we know today as a flag.\n\nThe flag has become an important symbol for identifying a country. Because there are thousands of flags in existence today, many look very similar. The flag of Russia consists of three horizontal stripes that are white, red, and blue from top to bottom. The flag of Yugoslavia has a similar design, with the colors in the order of red then white then blue. Colors on flags are important since they have special meanings. Red means power and white means peace. Orange is a symbol of courage or sacrifice. Green is the color of safety and hope and yellow of caution. Black is a symbol of death and often not a color used in country flags.\n\nSymbols of flags also have meanings. The American flag has thirteen stripes, which represent the original thirteen colonies. There are also 50 stars representing 50 states in the nation. Because of the meaning that we place on our flags, they have become a symbol of our home and of ourselves.",
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
        "passage": "Mankind has used flags for over 4,000 years. The first flags were simply wooden poles with carving at the top. About 2,000 years ago, fabric was added to the poles giving the appearance of what we know today as a flag.\n\nThe flag has become an important symbol for identifying a country. Because there are thousands of flags in existence today, many look very similar. The flag of Russia consists of three horizontal stripes that are white, red, and blue from top to bottom. The flag of Yugoslavia has a similar design, with the colors in the order of red then white then blue. Colors on flags are important since they have special meanings. Red means power and white means peace. Orange is a symbol of courage or sacrifice. Green is the color of safety and hope and yellow of caution. Black is a symbol of death and often not a color used in country flags.\n\nSymbols of flags also have meanings. The American flag has thirteen stripes, which represent the original thirteen colonies. There are also 50 stars representing 50 states in the nation. Because of the meaning that we place on our flags, they have become a symbol of our home and of ourselves.",
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
        "passage": "Mankind has used flags for over 4,000 years. The first flags were simply wooden poles with carving at the top. About 2,000 years ago, fabric was added to the poles giving the appearance of what we know today as a flag.\n\nThe flag has become an important symbol for identifying a country. Because there are thousands of flags in existence today, many look very similar. The flag of Russia consists of three horizontal stripes that are white, red, and blue from top to bottom. The flag of Yugoslavia has a similar design, with the colors in the order of red then white then blue. Colors on flags are important since they have special meanings. Red means power and white means peace. Orange is a symbol of courage or sacrifice. Green is the color of safety and hope and yellow of caution. Black is a symbol of death and often not a color used in country flags.\n\nSymbols of flags also have meanings. The American flag has thirteen stripes, which represent the original thirteen colonies. There are also 50 stars representing 50 states in the nation. Because of the meaning that we place on our flags, they have become a symbol of our home and of ourselves.",
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
        "passage": "Rebecca Stevens was the first woman to climb Mount Everest. Before she went up the highest mountain in the world, she was a journalist and lived in a small flat in south London.\n\nIn 1993, Rebecca left her job and her family and travelled to Asia with some other climbers. She found that life on Everest is hard. 'You must carry everything on your back', she explained 'so you can only take things that you will need. You can't wash on the mountain, and in the end I didn't even take a toothbrush. I am usually a clean person but there is no water, only snow. Water is very heavy so you only take enough to drink!'\n\nWhen Rebecca reached the top of Mount Everest on May 17 1993, it was the best moment of her life. Suddenly she became famous.\n\nNow she has written a book about the trip and people often ask her to talk about it. She has a new job, too, on a science program on television.\n\nRebecca is well know today and she has more money, but she still lives in the little flat in south London among her pictures and books about mountains.",
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
        "passage": "Rebecca Stevens was the first woman to climb Mount Everest. Before she went up the highest mountain in the world, she was a journalist and lived in a small flat in south London.\n\nIn 1993, Rebecca left her job and her family and travelled to Asia with some other climbers. She found that life on Everest is hard. 'You must carry everything on your back', she explained 'so you can only take things that you will need. You can't wash on the mountain, and in the end I didn't even take a toothbrush. I am usually a clean person but there is no water, only snow. Water is very heavy so you only take enough to drink!'\n\nWhen Rebecca reached the top of Mount Everest on May 17 1993, it was the best moment of her life. Suddenly she became famous.\n\nNow she has written a book about the trip and people often ask her to talk about it. She has a new job, too, on a science program on television.\n\nRebecca is well know today and she has more money, but she still lives in the little flat in south London among her pictures and books about mountains.",
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
        "passage": "Rebecca Stevens was the first woman to climb Mount Everest. Before she went up the highest mountain in the world, she was a journalist and lived in a small flat in south London.\n\nIn 1993, Rebecca left her job and her family and travelled to Asia with some other climbers. She found that life on Everest is hard. 'You must carry everything on your back', she explained 'so you can only take things that you will need. You can't wash on the mountain, and in the end I didn't even take a toothbrush. I am usually a clean person but there is no water, only snow. Water is very heavy so you only take enough to drink!'\n\nWhen Rebecca reached the top of Mount Everest on May 17 1993, it was the best moment of her life. Suddenly she became famous.\n\nNow she has written a book about the trip and people often ask her to talk about it. She has a new job, too, on a science program on television.\n\nRebecca is well know today and she has more money, but she still lives in the little flat in south London among her pictures and books about mountains.",
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
        "passage": "Rebecca Stevens was the first woman to climb Mount Everest. Before she went up the highest mountain in the world, she was a journalist and lived in a small flat in south London.\n\nIn 1993, Rebecca left her job and her family and travelled to Asia with some other climbers. She found that life on Everest is hard. 'You must carry everything on your back', she explained 'so you can only take things that you will need. You can't wash on the mountain, and in the end I didn't even take a toothbrush. I am usually a clean person but there is no water, only snow. Water is very heavy so you only take enough to drink!'\n\nWhen Rebecca reached the top of Mount Everest on May 17 1993, it was the best moment of her life. Suddenly she became famous.\n\nNow she has written a book about the trip and people often ask her to talk about it. She has a new job, too, on a science program on television.\n\nRebecca is well know today and she has more money, but she still lives in the little flat in south London among her pictures and books about mountains.",
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
        "passage": "Rebecca Stevens was the first woman to climb Mount Everest. Before she went up the highest mountain in the world, she was a journalist and lived in a small flat in south London.\n\nIn 1993, Rebecca left her job and her family and travelled to Asia with some other climbers. She found that life on Everest is hard. 'You must carry everything on your back', she explained 'so you can only take things that you will need. You can't wash on the mountain, and in the end I didn't even take a toothbrush. I am usually a clean person but there is no water, only snow. Water is very heavy so you only take enough to drink!'\n\nWhen Rebecca reached the top of Mount Everest on May 17 1993, it was the best moment of her life. Suddenly she became famous.\n\nNow she has written a book about the trip and people often ask her to talk about it. She has a new job, too, on a science program on television.\n\nRebecca is well know today and she has more money, but she still lives in the little flat in south London among her pictures and books about mountains.",
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
        "passage": "Rebecca Stevens was the first woman to climb Mount Everest. Before she went up the highest mountain in the world, she was a journalist and lived in a small flat in south London.\n\nIn 1993, Rebecca left her job and her family and travelled to Asia with some other climbers. She found that life on Everest is hard. 'You must carry everything on your back', she explained 'so you can only take things that you will need. You can't wash on the mountain, and in the end I didn't even take a toothbrush. I am usually a clean person but there is no water, only snow. Water is very heavy so you only take enough to drink!'\n\nWhen Rebecca reached the top of Mount Everest on May 17 1993, it was the best moment of her life. Suddenly she became famous.\n\nNow she has written a book about the trip and people often ask her to talk about it. She has a new job, too, on a science program on television.\n\nRebecca is well know today and she has more money, but she still lives in the little flat in south London among her pictures and books about mountains.",
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
        "passage": "Rebecca Stevens was the first woman to climb Mount Everest. Before she went up the highest mountain in the world, she was a journalist and lived in a small flat in south London.\n\nIn 1993, Rebecca left her job and her family and travelled to Asia with some other climbers. She found that life on Everest is hard. 'You must carry everything on your back', she explained 'so you can only take things that you will need. You can't wash on the mountain, and in the end I didn't even take a toothbrush. I am usually a clean person but there is no water, only snow. Water is very heavy so you only take enough to drink!'\n\nWhen Rebecca reached the top of Mount Everest on May 17 1993, it was the best moment of her life. Suddenly she became famous.\n\nNow she has written a book about the trip and people often ask her to talk about it. She has a new job, too, on a science program on television.\n\nRebecca is well know today and she has more money, but she still lives in the little flat in south London among her pictures and books about mountains.",
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
        "passage": "Orbis is an organization which helps blind people everywhere. It has built an eye hospital inside an aeroplane and flown it all over the world with an international medical team. Samantha Graham, a fourteen-year-old schoolgirl from England, went with the plane to Mongolia, Samatha tells the story of Eukhtuul, a young Mongolian girl.\n\nLast year, when Eukhtuul was walking home from school, she was attacked by boys with sticks and her eyes were badly damaged. Dr Duffey, an Orbis doctor, said that without an operation she would never see again, I thought about all the everyday things I do that she couldn't, things like reading schoolbooks, watching television, seeing friends, and I realized how lucky I am'.\n\n'The Orbis team agreed to operate on Eukhtuul and I was allowed to watch, together with some Mongolian medical students. I prayed the operation would be successful. The next day I waited nervously with Eukhtuul while Dr Duffey removed her bandages. 'In six months your sight will be back to normal', he said. Eukhtuul smiled, her mother cried, and I had to wipe away some tears, too!'\n\n'Now Eukhtuul wants to study hard to become a doctor. Her whole future has changed, thanks to a simple operation. We should all think more about how much out sight means to us.",
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
        "passage": "Orbis is an organization which helps blind people everywhere. It has built an eye hospital inside an aeroplane and flown it all over the world with an international medical team. Samantha Graham, a fourteen-year-old schoolgirl from England, went with the plane to Mongolia, Samatha tells the story of Eukhtuul, a young Mongolian girl.\n\nLast year, when Eukhtuul was walking home from school, she was attacked by boys with sticks and her eyes were badly damaged. Dr Duffey, an Orbis doctor, said that without an operation she would never see again, I thought about all the everyday things I do that she couldn't, things like reading schoolbooks, watching television, seeing friends, and I realized how lucky I am'.\n\n'The Orbis team agreed to operate on Eukhtuul and I was allowed to watch, together with some Mongolian medical students. I prayed the operation would be successful. The next day I waited nervously with Eukhtuul while Dr Duffey removed her bandages. 'In six months your sight will be back to normal', he said. Eukhtuul smiled, her mother cried, and I had to wipe away some tears, too!'\n\n'Now Eukhtuul wants to study hard to become a doctor. Her whole future has changed, thanks to a simple operation. We should all think more about how much out sight means to us.",
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
        "passage": "Orbis is an organization which helps blind people everywhere. It has built an eye hospital inside an aeroplane and flown it all over the world with an international medical team. Samantha Graham, a fourteen-year-old schoolgirl from England, went with the plane to Mongolia, Samatha tells the story of Eukhtuul, a young Mongolian girl.\n\nLast year, when Eukhtuul was walking home from school, she was attacked by boys with sticks and her eyes were badly damaged. Dr Duffey, an Orbis doctor, said that without an operation she would never see again, I thought about all the everyday things I do that she couldn't, things like reading schoolbooks, watching television, seeing friends, and I realized how lucky I am'.\n\n'The Orbis team agreed to operate on Eukhtuul and I was allowed to watch, together with some Mongolian medical students. I prayed the operation would be successful. The next day I waited nervously with Eukhtuul while Dr Duffey removed her bandages. 'In six months your sight will be back to normal', he said. Eukhtuul smiled, her mother cried, and I had to wipe away some tears, too!'\n\n'Now Eukhtuul wants to study hard to become a doctor. Her whole future has changed, thanks to a simple operation. We should all think more about how much out sight means to us.",
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
        "passage": "Orbis is an organization which helps blind people everywhere. It has built an eye hospital inside an aeroplane and flown it all over the world with an international medical team. Samantha Graham, a fourteen-year-old schoolgirl from England, went with the plane to Mongolia, Samatha tells the story of Eukhtuul, a young Mongolian girl.\n\nLast year, when Eukhtuul was walking home from school, she was attacked by boys with sticks and her eyes were badly damaged. Dr Duffey, an Orbis doctor, said that without an operation she would never see again, I thought about all the everyday things I do that she couldn't, things like reading schoolbooks, watching television, seeing friends, and I realized how lucky I am'.\n\n'The Orbis team agreed to operate on Eukhtuul and I was allowed to watch, together with some Mongolian medical students. I prayed the operation would be successful. The next day I waited nervously with Eukhtuul while Dr Duffey removed her bandages. 'In six months your sight will be back to normal', he said. Eukhtuul smiled, her mother cried, and I had to wipe away some tears, too!'\n\n'Now Eukhtuul wants to study hard to become a doctor. Her whole future has changed, thanks to a simple operation. We should all think more about how much out sight means to us.",
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
        "passage": "Orbis is an organization which helps blind people everywhere. It has built an eye hospital inside an aeroplane and flown it all over the world with an international medical team. Samantha Graham, a fourteen-year-old schoolgirl from England, went with the plane to Mongolia, Samatha tells the story of Eukhtuul, a young Mongolian girl.\n\nLast year, when Eukhtuul was walking home from school, she was attacked by boys with sticks and her eyes were badly damaged. Dr Duffey, an Orbis doctor, said that without an operation she would never see again, I thought about all the everyday things I do that she couldn't, things like reading schoolbooks, watching television, seeing friends, and I realized how lucky I am'.\n\n'The Orbis team agreed to operate on Eukhtuul and I was allowed to watch, together with some Mongolian medical students. I prayed the operation would be successful. The next day I waited nervously with Eukhtuul while Dr Duffey removed her bandages. 'In six months your sight will be back to normal', he said. Eukhtuul smiled, her mother cried, and I had to wipe away some tears, too!'\n\n'Now Eukhtuul wants to study hard to become a doctor. Her whole future has changed, thanks to a simple operation. We should all think more about how much out sight means to us.",
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
        "passage": "In 2006, Ravi Patra started working for a music company and three years later, in 2009, got a job on the music television channel Rock TV.\n\nRevi enjoys working on television, but when he was younger he wanted to fly planes. Later, he became more interested in football. But Ravi has always loved music, so he tried to get work with Rock TV. His boss says he gave him the job because he wanted it more than anybody else!\n\nWhen he started at Rock TV, Ravi arrived first at the office and was the last to leave at 10 in the evening. Now, he starts a bit later, but he is still busy until 10 pm. Before lunch, he usually writes his words for the show and in the afternoon he has meetings or makes Rock TV advertisements.\n\nRovi has many popular bands on his show and the stars are often interesting people. But Ravi knows that everyone watches the show to hear great music. Getting that right is more important than anything else.\n\nRavi knows what questions to ask the band members. He tries to make them laugh and this is easy for him. Sometimes he cannot remember their names but he always has information about the bands to help him.",
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
        "passage": "In 2006, Ravi Patra started working for a music company and three years later, in 2009, got a job on the music television channel Rock TV.\n\nRevi enjoys working on television, but when he was younger he wanted to fly planes. Later, he became more interested in football. But Ravi has always loved music, so he tried to get work with Rock TV. His boss says he gave him the job because he wanted it more than anybody else!\n\nWhen he started at Rock TV, Ravi arrived first at the office and was the last to leave at 10 in the evening. Now, he starts a bit later, but he is still busy until 10 pm. Before lunch, he usually writes his words for the show and in the afternoon he has meetings or makes Rock TV advertisements.\n\nRovi has many popular bands on his show and the stars are often interesting people. But Ravi knows that everyone watches the show to hear great music. Getting that right is more important than anything else.\n\nRavi knows what questions to ask the band members. He tries to make them laugh and this is easy for him. Sometimes he cannot remember their names but he always has information about the bands to help him.",
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
        "passage": "In 2006, Ravi Patra started working for a music company and three years later, in 2009, got a job on the music television channel Rock TV.\n\nRevi enjoys working on television, but when he was younger he wanted to fly planes. Later, he became more interested in football. But Ravi has always loved music, so he tried to get work with Rock TV. His boss says he gave him the job because he wanted it more than anybody else!\n\nWhen he started at Rock TV, Ravi arrived first at the office and was the last to leave at 10 in the evening. Now, he starts a bit later, but he is still busy until 10 pm. Before lunch, he usually writes his words for the show and in the afternoon he has meetings or makes Rock TV advertisements.\n\nRovi has many popular bands on his show and the stars are often interesting people. But Ravi knows that everyone watches the show to hear great music. Getting that right is more important than anything else.\n\nRavi knows what questions to ask the band members. He tries to make them laugh and this is easy for him. Sometimes he cannot remember their names but he always has information about the bands to help him.",
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
        "passage": "In 2006, Ravi Patra started working for a music company and three years later, in 2009, got a job on the music television channel Rock TV.\n\nRevi enjoys working on television, but when he was younger he wanted to fly planes. Later, he became more interested in football. But Ravi has always loved music, so he tried to get work with Rock TV. His boss says he gave him the job because he wanted it more than anybody else!\n\nWhen he started at Rock TV, Ravi arrived first at the office and was the last to leave at 10 in the evening. Now, he starts a bit later, but he is still busy until 10 pm. Before lunch, he usually writes his words for the show and in the afternoon he has meetings or makes Rock TV advertisements.\n\nRovi has many popular bands on his show and the stars are often interesting people. But Ravi knows that everyone watches the show to hear great music. Getting that right is more important than anything else.\n\nRavi knows what questions to ask the band members. He tries to make them laugh and this is easy for him. Sometimes he cannot remember their names but he always has information about the bands to help him.",
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
        "passage": "In 2006, Ravi Patra started working for a music company and three years later, in 2009, got a job on the music television channel Rock TV.\n\nRevi enjoys working on television, but when he was younger he wanted to fly planes. Later, he became more interested in football. But Ravi has always loved music, so he tried to get work with Rock TV. His boss says he gave him the job because he wanted it more than anybody else!\n\nWhen he started at Rock TV, Ravi arrived first at the office and was the last to leave at 10 in the evening. Now, he starts a bit later, but he is still busy until 10 pm. Before lunch, he usually writes his words for the show and in the afternoon he has meetings or makes Rock TV advertisements.\n\nRovi has many popular bands on his show and the stars are often interesting people. But Ravi knows that everyone watches the show to hear great music. Getting that right is more important than anything else.\n\nRavi knows what questions to ask the band members. He tries to make them laugh and this is easy for him. Sometimes he cannot remember their names but he always has information about the bands to help him.",
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
        "passage": "In 2006, Ravi Patra started working for a music company and three years later, in 2009, got a job on the music television channel Rock TV.\n\nRevi enjoys working on television, but when he was younger he wanted to fly planes. Later, he became more interested in football. But Ravi has always loved music, so he tried to get work with Rock TV. His boss says he gave him the job because he wanted it more than anybody else!\n\nWhen he started at Rock TV, Ravi arrived first at the office and was the last to leave at 10 in the evening. Now, he starts a bit later, but he is still busy until 10 pm. Before lunch, he usually writes his words for the show and in the afternoon he has meetings or makes Rock TV advertisements.\n\nRovi has many popular bands on his show and the stars are often interesting people. But Ravi knows that everyone watches the show to hear great music. Getting that right is more important than anything else.\n\nRavi knows what questions to ask the band members. He tries to make them laugh and this is easy for him. Sometimes he cannot remember their names but he always has information about the bands to help him.",
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
        "passage": "In 2006, Ravi Patra started working for a music company and three years later, in 2009, got a job on the music television channel Rock TV.\n\nRevi enjoys working on television, but when he was younger he wanted to fly planes. Later, he became more interested in football. But Ravi has always loved music, so he tried to get work with Rock TV. His boss says he gave him the job because he wanted it more than anybody else!\n\nWhen he started at Rock TV, Ravi arrived first at the office and was the last to leave at 10 in the evening. Now, he starts a bit later, but he is still busy until 10 pm. Before lunch, he usually writes his words for the show and in the afternoon he has meetings or makes Rock TV advertisements.\n\nRovi has many popular bands on his show and the stars are often interesting people. But Ravi knows that everyone watches the show to hear great music. Getting that right is more important than anything else.\n\nRavi knows what questions to ask the band members. He tries to make them laugh and this is easy for him. Sometimes he cannot remember their names but he always has information about the bands to help him.",
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
        "passage": "She was still at primary school when she decided she wanted to travel. So when she was eleven, she decided to go for bike rides, and cycled or so miles every day.\n\nJosie says: 'The only good thing about secondary school was cycling there and back. I left when I was 16. I love cooking, so I started a business. I cooked three-course meals, and delivered them by bike! In 1985, as soon as I had some money, I cycled to Africa and back'.\n\nJosie has been to 40 countries and has had all kinds of interesting experiences. She has cycled through the Himalayan mountains in Nepal, then down into India. She has cycled through millions of locusts in the Moroccan desert. She has traveled through tornados in the USA. She was in Romania on Christmas Day in 1989 when President Ceausescu was executed by the Government. And she hasn't been to Egypt yet, because when she was in Turkey, a war started nearby. So she went to Greece instead.\n\nShe has sometimes traveled with friend, boyfriends and even her mother, but she has often cycled alone. She had only one really frightening experience - a man attacked her in Bulgaria.\n\nIn 1997 she hurt her knee very badly, so she started writing books about her journeys. She's written five books, and now she's on her bike again! At the moment she's planning to cycle around New Zealand.",
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
        "passage": "She was still at primary school when she decided she wanted to travel. So when she was eleven, she decided to go for bike rides, and cycled or so miles every day.\n\nJosie says: 'The only good thing about secondary school was cycling there and back. I left when I was 16. I love cooking, so I started a business. I cooked three-course meals, and delivered them by bike! In 1985, as soon as I had some money, I cycled to Africa and back'.\n\nJosie has been to 40 countries and has had all kinds of interesting experiences. She has cycled through the Himalayan mountains in Nepal, then down into India. She has cycled through millions of locusts in the Moroccan desert. She has traveled through tornados in the USA. She was in Romania on Christmas Day in 1989 when President Ceausescu was executed by the Government. And she hasn't been to Egypt yet, because when she was in Turkey, a war started nearby. So she went to Greece instead.\n\nShe has sometimes traveled with friend, boyfriends and even her mother, but she has often cycled alone. She had only one really frightening experience - a man attacked her in Bulgaria.\n\nIn 1997 she hurt her knee very badly, so she started writing books about her journeys. She's written five books, and now she's on her bike again! At the moment she's planning to cycle around New Zealand.",
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
        "passage": "She was still at primary school when she decided she wanted to travel. So when she was eleven, she decided to go for bike rides, and cycled or so miles every day.\n\nJosie says: 'The only good thing about secondary school was cycling there and back. I left when I was 16. I love cooking, so I started a business. I cooked three-course meals, and delivered them by bike! In 1985, as soon as I had some money, I cycled to Africa and back'.\n\nJosie has been to 40 countries and has had all kinds of interesting experiences. She has cycled through the Himalayan mountains in Nepal, then down into India. She has cycled through millions of locusts in the Moroccan desert. She has traveled through tornados in the USA. She was in Romania on Christmas Day in 1989 when President Ceausescu was executed by the Government. And she hasn't been to Egypt yet, because when she was in Turkey, a war started nearby. So she went to Greece instead.\n\nShe has sometimes traveled with friend, boyfriends and even her mother, but she has often cycled alone. She had only one really frightening experience - a man attacked her in Bulgaria.\n\nIn 1997 she hurt her knee very badly, so she started writing books about her journeys. She's written five books, and now she's on her bike again! At the moment she's planning to cycle around New Zealand.",
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
        "passage": "She was still at primary school when she decided she wanted to travel. So when she was eleven, she decided to go for bike rides, and cycled or so miles every day.\n\nJosie says: 'The only good thing about secondary school was cycling there and back. I left when I was 16. I love cooking, so I started a business. I cooked three-course meals, and delivered them by bike! In 1985, as soon as I had some money, I cycled to Africa and back'.\n\nJosie has been to 40 countries and has had all kinds of interesting experiences. She has cycled through the Himalayan mountains in Nepal, then down into India. She has cycled through millions of locusts in the Moroccan desert. She has traveled through tornados in the USA. She was in Romania on Christmas Day in 1989 when President Ceausescu was executed by the Government. And she hasn't been to Egypt yet, because when she was in Turkey, a war started nearby. So she went to Greece instead.\n\nShe has sometimes traveled with friend, boyfriends and even her mother, but she has often cycled alone. She had only one really frightening experience - a man attacked her in Bulgaria.\n\nIn 1997 she hurt her knee very badly, so she started writing books about her journeys. She's written five books, and now she's on her bike again! At the moment she's planning to cycle around New Zealand.",
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
        "passage": "She was still at primary school when she decided she wanted to travel. So when she was eleven, she decided to go for bike rides, and cycled or so miles every day.\n\nJosie says: 'The only good thing about secondary school was cycling there and back. I left when I was 16. I love cooking, so I started a business. I cooked three-course meals, and delivered them by bike! In 1985, as soon as I had some money, I cycled to Africa and back'.\n\nJosie has been to 40 countries and has had all kinds of interesting experiences. She has cycled through the Himalayan mountains in Nepal, then down into India. She has cycled through millions of locusts in the Moroccan desert. She has traveled through tornados in the USA. She was in Romania on Christmas Day in 1989 when President Ceausescu was executed by the Government. And she hasn't been to Egypt yet, because when she was in Turkey, a war started nearby. So she went to Greece instead.\n\nShe has sometimes traveled with friend, boyfriends and even her mother, but she has often cycled alone. She had only one really frightening experience - a man attacked her in Bulgaria.\n\nIn 1997 she hurt her knee very badly, so she started writing books about her journeys. She's written five books, and now she's on her bike again! At the moment she's planning to cycle around New Zealand.",
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
        "passage": "She was still at primary school when she decided she wanted to travel. So when she was eleven, she decided to go for bike rides, and cycled or so miles every day.\n\nJosie says: 'The only good thing about secondary school was cycling there and back. I left when I was 16. I love cooking, so I started a business. I cooked three-course meals, and delivered them by bike! In 1985, as soon as I had some money, I cycled to Africa and back'.\n\nJosie has been to 40 countries and has had all kinds of interesting experiences. She has cycled through the Himalayan mountains in Nepal, then down into India. She has cycled through millions of locusts in the Moroccan desert. She has traveled through tornados in the USA. She was in Romania on Christmas Day in 1989 when President Ceausescu was executed by the Government. And she hasn't been to Egypt yet, because when she was in Turkey, a war started nearby. So she went to Greece instead.\n\nShe has sometimes traveled with friend, boyfriends and even her mother, but she has often cycled alone. She had only one really frightening experience - a man attacked her in Bulgaria.\n\nIn 1997 she hurt her knee very badly, so she started writing books about her journeys. She's written five books, and now she's on her bike again! At the moment she's planning to cycle around New Zealand.",
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
        "passage": "She was still at primary school when she decided she wanted to travel. So when she was eleven, she decided to go for bike rides, and cycled or so miles every day.\n\nJosie says: 'The only good thing about secondary school was cycling there and back. I left when I was 16. I love cooking, so I started a business. I cooked three-course meals, and delivered them by bike! In 1985, as soon as I had some money, I cycled to Africa and back'.\n\nJosie has been to 40 countries and has had all kinds of interesting experiences. She has cycled through the Himalayan mountains in Nepal, then down into India. She has cycled through millions of locusts in the Moroccan desert. She has traveled through tornados in the USA. She was in Romania on Christmas Day in 1989 when President Ceausescu was executed by the Government. And she hasn't been to Egypt yet, because when she was in Turkey, a war started nearby. So she went to Greece instead.\n\nShe has sometimes traveled with friend, boyfriends and even her mother, but she has often cycled alone. She had only one really frightening experience - a man attacked her in Bulgaria.\n\nIn 1997 she hurt her knee very badly, so she started writing books about her journeys. She's written five books, and now she's on her bike again! At the moment she's planning to cycle around New Zealand.",
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
        "passage": "She was still at primary school when she decided she wanted to travel. So when she was eleven, she decided to go for bike rides, and cycled or so miles every day.\n\nJosie says: 'The only good thing about secondary school was cycling there and back. I left when I was 16. I love cooking, so I started a business. I cooked three-course meals, and delivered them by bike! In 1985, as soon as I had some money, I cycled to Africa and back'.\n\nJosie has been to 40 countries and has had all kinds of interesting experiences. She has cycled through the Himalayan mountains in Nepal, then down into India. She has cycled through millions of locusts in the Moroccan desert. She has traveled through tornados in the USA. She was in Romania on Christmas Day in 1989 when President Ceausescu was executed by the Government. And she hasn't been to Egypt yet, because when she was in Turkey, a war started nearby. So she went to Greece instead.\n\nShe has sometimes traveled with friend, boyfriends and even her mother, but she has often cycled alone. She had only one really frightening experience - a man attacked her in Bulgaria.\n\nIn 1997 she hurt her knee very badly, so she started writing books about her journeys. She's written five books, and now she's on her bike again! At the moment she's planning to cycle around New Zealand.",
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
        "passage": "She was still at primary school when she decided she wanted to travel. So when she was eleven, she decided to go for bike rides, and cycled or so miles every day.\n\nJosie says: 'The only good thing about secondary school was cycling there and back. I left when I was 16. I love cooking, so I started a business. I cooked three-course meals, and delivered them by bike! In 1985, as soon as I had some money, I cycled to Africa and back'.\n\nJosie has been to 40 countries and has had all kinds of interesting experiences. She has cycled through the Himalayan mountains in Nepal, then down into India. She has cycled through millions of locusts in the Moroccan desert. She has traveled through tornados in the USA. She was in Romania on Christmas Day in 1989 when President Ceausescu was executed by the Government. And she hasn't been to Egypt yet, because when she was in Turkey, a war started nearby. So she went to Greece instead.\n\nShe has sometimes traveled with friend, boyfriends and even her mother, but she has often cycled alone. She had only one really frightening experience - a man attacked her in Bulgaria.\n\nIn 1997 she hurt her knee very badly, so she started writing books about her journeys. She's written five books, and now she's on her bike again! At the moment she's planning to cycle around New Zealand.",
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
        "passage": "She was still at primary school when she decided she wanted to travel. So when she was eleven, she decided to go for bike rides, and cycled or so miles every day.\n\nJosie says: 'The only good thing about secondary school was cycling there and back. I left when I was 16. I love cooking, so I started a business. I cooked three-course meals, and delivered them by bike! In 1985, as soon as I had some money, I cycled to Africa and back'.\n\nJosie has been to 40 countries and has had all kinds of interesting experiences. She has cycled through the Himalayan mountains in Nepal, then down into India. She has cycled through millions of locusts in the Moroccan desert. She has traveled through tornados in the USA. She was in Romania on Christmas Day in 1989 when President Ceausescu was executed by the Government. And she hasn't been to Egypt yet, because when she was in Turkey, a war started nearby. So she went to Greece instead.\n\nShe has sometimes traveled with friend, boyfriends and even her mother, but she has often cycled alone. She had only one really frightening experience - a man attacked her in Bulgaria.\n\nIn 1997 she hurt her knee very badly, so she started writing books about her journeys. She's written five books, and now she's on her bike again! At the moment she's planning to cycle around New Zealand.",
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
        "passage": "She was still at primary school when she decided she wanted to travel. So when she was eleven, she decided to go for bike rides, and cycled or so miles every day.\n\nJosie says: 'The only good thing about secondary school was cycling there and back. I left when I was 16. I love cooking, so I started a business. I cooked three-course meals, and delivered them by bike! In 1985, as soon as I had some money, I cycled to Africa and back'.\n\nJosie has been to 40 countries and has had all kinds of interesting experiences. She has cycled through the Himalayan mountains in Nepal, then down into India. She has cycled through millions of locusts in the Moroccan desert. She has traveled through tornados in the USA. She was in Romania on Christmas Day in 1989 when President Ceausescu was executed by the Government. And she hasn't been to Egypt yet, because when she was in Turkey, a war started nearby. So she went to Greece instead.\n\nShe has sometimes traveled with friend, boyfriends and even her mother, but she has often cycled alone. She had only one really frightening experience - a man attacked her in Bulgaria.\n\nIn 1997 she hurt her knee very badly, so she started writing books about her journeys. She's written five books, and now she's on her bike again! At the moment she's planning to cycle around New Zealand.",
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
        "passage": "She was still at primary school when she decided she wanted to travel. So when she was eleven, she decided to go for bike rides, and cycled or so miles every day.\n\nJosie says: 'The only good thing about secondary school was cycling there and back. I left when I was 16. I love cooking, so I started a business. I cooked three-course meals, and delivered them by bike! In 1985, as soon as I had some money, I cycled to Africa and back'.\n\nJosie has been to 40 countries and has had all kinds of interesting experiences. She has cycled through the Himalayan mountains in Nepal, then down into India. She has cycled through millions of locusts in the Moroccan desert. She has traveled through tornados in the USA. She was in Romania on Christmas Day in 1989 when President Ceausescu was executed by the Government. And she hasn't been to Egypt yet, because when she was in Turkey, a war started nearby. So she went to Greece instead.\n\nShe has sometimes traveled with friend, boyfriends and even her mother, but she has often cycled alone. She had only one really frightening experience - a man attacked her in Bulgaria.\n\nIn 1997 she hurt her knee very badly, so she started writing books about her journeys. She's written five books, and now she's on her bike again! At the moment she's planning to cycle around New Zealand.",
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
        "passage": "She was still at primary school when she decided she wanted to travel. So when she was eleven, she decided to go for bike rides, and cycled or so miles every day.\n\nJosie says: 'The only good thing about secondary school was cycling there and back. I left when I was 16. I love cooking, so I started a business. I cooked three-course meals, and delivered them by bike! In 1985, as soon as I had some money, I cycled to Africa and back'.\n\nJosie has been to 40 countries and has had all kinds of interesting experiences. She has cycled through the Himalayan mountains in Nepal, then down into India. She has cycled through millions of locusts in the Moroccan desert. She has traveled through tornados in the USA. She was in Romania on Christmas Day in 1989 when President Ceausescu was executed by the Government. And she hasn't been to Egypt yet, because when she was in Turkey, a war started nearby. So she went to Greece instead.\n\nShe has sometimes traveled with friend, boyfriends and even her mother, but she has often cycled alone. She had only one really frightening experience - a man attacked her in Bulgaria.\n\nIn 1997 she hurt her knee very badly, so she started writing books about her journeys. She's written five books, and now she's on her bike again! At the moment she's planning to cycle around New Zealand.",
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
        "passage": "While Western medicine is common throughout the world, it is not the only type of medicine that people practice. Another kind of medical treatment is known as acupuncture. In general, it is considered to be an alternative type of medicine. It was developed in China well over one thousand years ago, but exactly when and how it was created remain mysteries. Acupuncture involves the inserting of multiple needles into the body. The needles are placed at certain points in the body, depending on the type of problem the patient has. According to the theory behind acupuncture, there are places on the skin that are connected to different parts of the body. By pricking the skin with needles at these points, an acupuncturist can help a patient either relieve pain or cure various problems.\n\nAcupuncture is popular in many parts of Asia. It is also becoming more common and attracting new patients in Europe and North America. But many people believe it is ineffective. The main reason they feel that way is that it is difficult to understand how the entire process works. Research into acupuncture's capabilities has yielded varying results. Some studies show that it is quite effective at relieving pain. Other ones, however, claim that it is merely like a placebo. In other words, people believe acupuncture treatment will be effective, so it winds up helping them.",
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
        "passage": "While Western medicine is common throughout the world, it is not the only type of medicine that people practice. Another kind of medical treatment is known as acupuncture. In general, it is considered to be an alternative type of medicine. It was developed in China well over one thousand years ago, but exactly when and how it was created remain mysteries. Acupuncture involves the inserting of multiple needles into the body. The needles are placed at certain points in the body, depending on the type of problem the patient has. According to the theory behind acupuncture, there are places on the skin that are connected to different parts of the body. By pricking the skin with needles at these points, an acupuncturist can help a patient either relieve pain or cure various problems.\n\nAcupuncture is popular in many parts of Asia. It is also becoming more common and attracting new patients in Europe and North America. But many people believe it is ineffective. The main reason they feel that way is that it is difficult to understand how the entire process works. Research into acupuncture's capabilities has yielded varying results. Some studies show that it is quite effective at relieving pain. Other ones, however, claim that it is merely like a placebo. In other words, people believe acupuncture treatment will be effective, so it winds up helping them.",
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
        "passage": "While Western medicine is common throughout the world, it is not the only type of medicine that people practice. Another kind of medical treatment is known as acupuncture. In general, it is considered to be an alternative type of medicine. It was developed in China well over one thousand years ago, but exactly when and how it was created remain mysteries. Acupuncture involves the inserting of multiple needles into the body. The needles are placed at certain points in the body, depending on the type of problem the patient has. According to the theory behind acupuncture, there are places on the skin that are connected to different parts of the body. By pricking the skin with needles at these points, an acupuncturist can help a patient either relieve pain or cure various problems.\n\nAcupuncture is popular in many parts of Asia. It is also becoming more common and attracting new patients in Europe and North America. But many people believe it is ineffective. The main reason they feel that way is that it is difficult to understand how the entire process works. Research into acupuncture's capabilities has yielded varying results. Some studies show that it is quite effective at relieving pain. Other ones, however, claim that it is merely like a placebo. In other words, people believe acupuncture treatment will be effective, so it winds up helping them.",
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
        "passage": "While Western medicine is common throughout the world, it is not the only type of medicine that people practice. Another kind of medical treatment is known as acupuncture. In general, it is considered to be an alternative type of medicine. It was developed in China well over one thousand years ago, but exactly when and how it was created remain mysteries. Acupuncture involves the inserting of multiple needles into the body. The needles are placed at certain points in the body, depending on the type of problem the patient has. According to the theory behind acupuncture, there are places on the skin that are connected to different parts of the body. By pricking the skin with needles at these points, an acupuncturist can help a patient either relieve pain or cure various problems.\n\nAcupuncture is popular in many parts of Asia. It is also becoming more common and attracting new patients in Europe and North America. But many people believe it is ineffective. The main reason they feel that way is that it is difficult to understand how the entire process works. Research into acupuncture's capabilities has yielded varying results. Some studies show that it is quite effective at relieving pain. Other ones, however, claim that it is merely like a placebo. In other words, people believe acupuncture treatment will be effective, so it winds up helping them.",
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
        "passage": "While Western medicine is common throughout the world, it is not the only type of medicine that people practice. Another kind of medical treatment is known as acupuncture. In general, it is considered to be an alternative type of medicine. It was developed in China well over one thousand years ago, but exactly when and how it was created remain mysteries. Acupuncture involves the inserting of multiple needles into the body. The needles are placed at certain points in the body, depending on the type of problem the patient has. According to the theory behind acupuncture, there are places on the skin that are connected to different parts of the body. By pricking the skin with needles at these points, an acupuncturist can help a patient either relieve pain or cure various problems.\n\nAcupuncture is popular in many parts of Asia. It is also becoming more common and attracting new patients in Europe and North America. But many people believe it is ineffective. The main reason they feel that way is that it is difficult to understand how the entire process works. Research into acupuncture's capabilities has yielded varying results. Some studies show that it is quite effective at relieving pain. Other ones, however, claim that it is merely like a placebo. In other words, people believe acupuncture treatment will be effective, so it winds up helping them.",
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
        "passage": "Dear Thomas,\nI am curious as to whether or not you are still planning to go on that skiing trip with your family this winter vacation. I ask because, if you are not going, you might find this program I heard about today to be interesting. Apparently, Westfield State University, our local college, is going to hold an art seminar for thirty students.\n\nAccording to the brochure I have, three of the school's top faculty members are going to teach the seminar. They are planning to focus on painting. But there will also be lessons on sculpture and etching. And here is the best part: it does not cost anything to attend the seminar. However, you have to apply for a position. You can do that by submitting a sample of your work. I know how much you love art, so this could be a great opportunity for you. You probably do not want to give up going skiing, but this is a once-in-a-lifetime event. You might not want to pass up this chance. Let me know if you need any more information.\n\nYour friend,\nSusan",
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
        "passage": "Dear Thomas,\nI am curious as to whether or not you are still planning to go on that skiing trip with your family this winter vacation. I ask because, if you are not going, you might find this program I heard about today to be interesting. Apparently, Westfield State University, our local college, is going to hold an art seminar for thirty students.\n\nAccording to the brochure I have, three of the school's top faculty members are going to teach the seminar. They are planning to focus on painting. But there will also be lessons on sculpture and etching. And here is the best part: it does not cost anything to attend the seminar. However, you have to apply for a position. You can do that by submitting a sample of your work. I know how much you love art, so this could be a great opportunity for you. You probably do not want to give up going skiing, but this is a once-in-a-lifetime event. You might not want to pass up this chance. Let me know if you need any more information.\n\nYour friend,\nSusan",
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
        "passage": "Dear Thomas,\nI am curious as to whether or not you are still planning to go on that skiing trip with your family this winter vacation. I ask because, if you are not going, you might find this program I heard about today to be interesting. Apparently, Westfield State University, our local college, is going to hold an art seminar for thirty students.\n\nAccording to the brochure I have, three of the school's top faculty members are going to teach the seminar. They are planning to focus on painting. But there will also be lessons on sculpture and etching. And here is the best part: it does not cost anything to attend the seminar. However, you have to apply for a position. You can do that by submitting a sample of your work. I know how much you love art, so this could be a great opportunity for you. You probably do not want to give up going skiing, but this is a once-in-a-lifetime event. You might not want to pass up this chance. Let me know if you need any more information.\n\nYour friend,\nSusan",
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
        "passage": "Dear Thomas,\nI am curious as to whether or not you are still planning to go on that skiing trip with your family this winter vacation. I ask because, if you are not going, you might find this program I heard about today to be interesting. Apparently, Westfield State University, our local college, is going to hold an art seminar for thirty students.\n\nAccording to the brochure I have, three of the school's top faculty members are going to teach the seminar. They are planning to focus on painting. But there will also be lessons on sculpture and etching. And here is the best part: it does not cost anything to attend the seminar. However, you have to apply for a position. You can do that by submitting a sample of your work. I know how much you love art, so this could be a great opportunity for you. You probably do not want to give up going skiing, but this is a once-in-a-lifetime event. You might not want to pass up this chance. Let me know if you need any more information.\n\nYour friend,\nSusan",
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
        "passage": "Dear Thomas,\nI am curious as to whether or not you are still planning to go on that skiing trip with your family this winter vacation. I ask because, if you are not going, you might find this program I heard about today to be interesting. Apparently, Westfield State University, our local college, is going to hold an art seminar for thirty students.\n\nAccording to the brochure I have, three of the school's top faculty members are going to teach the seminar. They are planning to focus on painting. But there will also be lessons on sculpture and etching. And here is the best part: it does not cost anything to attend the seminar. However, you have to apply for a position. You can do that by submitting a sample of your work. I know how much you love art, so this could be a great opportunity for you. You probably do not want to give up going skiing, but this is a once-in-a-lifetime event. You might not want to pass up this chance. Let me know if you need any more information.\n\nYour friend,\nSusan",
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
        "passage": "The dogsled race was about to begin. Julie's team of dogs was lined up at the starting gate. Julie stood behind them. The air was so cold that she could see her breath. Other teams were lined up, too, and the dogs were excited. Julie kept her eyes on the clock. At exactly ten o'clock, she and the other racers yelled, 'Mush!' The dogs knew that meant 'Go!' They leap forward and the race began!\n\nJulie had trained for months for this race, and she hoped she and her dogs would win. Hour after hour, day after day, Julie's dogs pulled the sled in order to get in shape for the race.\n\nNow, they ran over snowy hills and down into frozen valleys. They stopped only to rest and eat. They wanted to stay ahead of the other teams. The racers had to go a thousand miles across Alaska. Alaska is one of the coldest places on Earth. The dogs' thick fur coats helped keep them warm in the cold wind and weather. In many places along the route, the snow was deep. Pieces of ice were as sharp as a knife. The ice could cut the dogs' feet. To keep that from happening, Julie had put special booties on their feet.\n\nAt first, the dogs seemed to pull the sled very slowly. They were still getting used to the race. But on the third day out, they began to pull more quickly. They worked as a team and passed many of the other racers. Once, one of the sled's runners slid into a hole and broke. Julie could have given up then, but she didn't. She fixed it and they kept going.\n\nWhen they finally reached the finish line, they found out that they had come in first place! It was a great day for Julie and her dogs.",
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
        "passage": "The dogsled race was about to begin. Julie's team of dogs was lined up at the starting gate. Julie stood behind them. The air was so cold that she could see her breath. Other teams were lined up, too, and the dogs were excited. Julie kept her eyes on the clock. At exactly ten o'clock, she and the other racers yelled, 'Mush!' The dogs knew that meant 'Go!' They leap forward and the race began!\n\nJulie had trained for months for this race, and she hoped she and her dogs would win. Hour after hour, day after day, Julie's dogs pulled the sled in order to get in shape for the race.\n\nNow, they ran over snowy hills and down into frozen valleys. They stopped only to rest and eat. They wanted to stay ahead of the other teams. The racers had to go a thousand miles across Alaska. Alaska is one of the coldest places on Earth. The dogs' thick fur coats helped keep them warm in the cold wind and weather. In many places along the route, the snow was deep. Pieces of ice were as sharp as a knife. The ice could cut the dogs' feet. To keep that from happening, Julie had put special booties on their feet.\n\nAt first, the dogs seemed to pull the sled very slowly. They were still getting used to the race. But on the third day out, they began to pull more quickly. They worked as a team and passed many of the other racers. Once, one of the sled's runners slid into a hole and broke. Julie could have given up then, but she didn't. She fixed it and they kept going.\n\nWhen they finally reached the finish line, they found out that they had come in first place! It was a great day for Julie and her dogs.",
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
        "passage": "The dogsled race was about to begin. Julie's team of dogs was lined up at the starting gate. Julie stood behind them. The air was so cold that she could see her breath. Other teams were lined up, too, and the dogs were excited. Julie kept her eyes on the clock. At exactly ten o'clock, she and the other racers yelled, 'Mush!' The dogs knew that meant 'Go!' They leap forward and the race began!\n\nJulie had trained for months for this race, and she hoped she and her dogs would win. Hour after hour, day after day, Julie's dogs pulled the sled in order to get in shape for the race.\n\nNow, they ran over snowy hills and down into frozen valleys. They stopped only to rest and eat. They wanted to stay ahead of the other teams. The racers had to go a thousand miles across Alaska. Alaska is one of the coldest places on Earth. The dogs' thick fur coats helped keep them warm in the cold wind and weather. In many places along the route, the snow was deep. Pieces of ice were as sharp as a knife. The ice could cut the dogs' feet. To keep that from happening, Julie had put special booties on their feet.\n\nAt first, the dogs seemed to pull the sled very slowly. They were still getting used to the race. But on the third day out, they began to pull more quickly. They worked as a team and passed many of the other racers. Once, one of the sled's runners slid into a hole and broke. Julie could have given up then, but she didn't. She fixed it and they kept going.\n\nWhen they finally reached the finish line, they found out that they had come in first place! It was a great day for Julie and her dogs.",
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
        "passage": "The dogsled race was about to begin. Julie's team of dogs was lined up at the starting gate. Julie stood behind them. The air was so cold that she could see her breath. Other teams were lined up, too, and the dogs were excited. Julie kept her eyes on the clock. At exactly ten o'clock, she and the other racers yelled, 'Mush!' The dogs knew that meant 'Go!' They leap forward and the race began!\n\nJulie had trained for months for this race, and she hoped she and her dogs would win. Hour after hour, day after day, Julie's dogs pulled the sled in order to get in shape for the race.\n\nNow, they ran over snowy hills and down into frozen valleys. They stopped only to rest and eat. They wanted to stay ahead of the other teams. The racers had to go a thousand miles across Alaska. Alaska is one of the coldest places on Earth. The dogs' thick fur coats helped keep them warm in the cold wind and weather. In many places along the route, the snow was deep. Pieces of ice were as sharp as a knife. The ice could cut the dogs' feet. To keep that from happening, Julie had put special booties on their feet.\n\nAt first, the dogs seemed to pull the sled very slowly. They were still getting used to the race. But on the third day out, they began to pull more quickly. They worked as a team and passed many of the other racers. Once, one of the sled's runners slid into a hole and broke. Julie could have given up then, but she didn't. She fixed it and they kept going.\n\nWhen they finally reached the finish line, they found out that they had come in first place! It was a great day for Julie and her dogs.",
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
        "passage": "The dogsled race was about to begin. Julie's team of dogs was lined up at the starting gate. Julie stood behind them. The air was so cold that she could see her breath. Other teams were lined up, too, and the dogs were excited. Julie kept her eyes on the clock. At exactly ten o'clock, she and the other racers yelled, 'Mush!' The dogs knew that meant 'Go!' They leap forward and the race began!\n\nJulie had trained for months for this race, and she hoped she and her dogs would win. Hour after hour, day after day, Julie's dogs pulled the sled in order to get in shape for the race.\n\nNow, they ran over snowy hills and down into frozen valleys. They stopped only to rest and eat. They wanted to stay ahead of the other teams. The racers had to go a thousand miles across Alaska. Alaska is one of the coldest places on Earth. The dogs' thick fur coats helped keep them warm in the cold wind and weather. In many places along the route, the snow was deep. Pieces of ice were as sharp as a knife. The ice could cut the dogs' feet. To keep that from happening, Julie had put special booties on their feet.\n\nAt first, the dogs seemed to pull the sled very slowly. They were still getting used to the race. But on the third day out, they began to pull more quickly. They worked as a team and passed many of the other racers. Once, one of the sled's runners slid into a hole and broke. Julie could have given up then, but she didn't. She fixed it and they kept going.\n\nWhen they finally reached the finish line, they found out that they had come in first place! It was a great day for Julie and her dogs.",
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
        "passage": "The dogsled race was about to begin. Julie's team of dogs was lined up at the starting gate. Julie stood behind them. The air was so cold that she could see her breath. Other teams were lined up, too, and the dogs were excited. Julie kept her eyes on the clock. At exactly ten o'clock, she and the other racers yelled, 'Mush!' The dogs knew that meant 'Go!' They leap forward and the race began!\n\nJulie had trained for months for this race, and she hoped she and her dogs would win. Hour after hour, day after day, Julie's dogs pulled the sled in order to get in shape for the race.\n\nNow, they ran over snowy hills and down into frozen valleys. They stopped only to rest and eat. They wanted to stay ahead of the other teams. The racers had to go a thousand miles across Alaska. Alaska is one of the coldest places on Earth. The dogs' thick fur coats helped keep them warm in the cold wind and weather. In many places along the route, the snow was deep. Pieces of ice were as sharp as a knife. The ice could cut the dogs' feet. To keep that from happening, Julie had put special booties on their feet.\n\nAt first, the dogs seemed to pull the sled very slowly. They were still getting used to the race. But on the third day out, they began to pull more quickly. They worked as a team and passed many of the other racers. Once, one of the sled's runners slid into a hole and broke. Julie could have given up then, but she didn't. She fixed it and they kept going.\n\nWhen they finally reached the finish line, they found out that they had come in first place! It was a great day for Julie and her dogs.",
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
        "passage": "The dogsled race was about to begin. Julie's team of dogs was lined up at the starting gate. Julie stood behind them. The air was so cold that she could see her breath. Other teams were lined up, too, and the dogs were excited. Julie kept her eyes on the clock. At exactly ten o'clock, she and the other racers yelled, 'Mush!' The dogs knew that meant 'Go!' They leap forward and the race began!\n\nJulie had trained for months for this race, and she hoped she and her dogs would win. Hour after hour, day after day, Julie's dogs pulled the sled in order to get in shape for the race.\n\nNow, they ran over snowy hills and down into frozen valleys. They stopped only to rest and eat. They wanted to stay ahead of the other teams. The racers had to go a thousand miles across Alaska. Alaska is one of the coldest places on Earth. The dogs' thick fur coats helped keep them warm in the cold wind and weather. In many places along the route, the snow was deep. Pieces of ice were as sharp as a knife. The ice could cut the dogs' feet. To keep that from happening, Julie had put special booties on their feet.\n\nAt first, the dogs seemed to pull the sled very slowly. They were still getting used to the race. But on the third day out, they began to pull more quickly. They worked as a team and passed many of the other racers. Once, one of the sled's runners slid into a hole and broke. Julie could have given up then, but she didn't. She fixed it and they kept going.\n\nWhen they finally reached the finish line, they found out that they had come in first place! It was a great day for Julie and her dogs.",
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
        "passage": "The dogsled race was about to begin. Julie's team of dogs was lined up at the starting gate. Julie stood behind them. The air was so cold that she could see her breath. Other teams were lined up, too, and the dogs were excited. Julie kept her eyes on the clock. At exactly ten o'clock, she and the other racers yelled, 'Mush!' The dogs knew that meant 'Go!' They leap forward and the race began!\n\nJulie had trained for months for this race, and she hoped she and her dogs would win. Hour after hour, day after day, Julie's dogs pulled the sled in order to get in shape for the race.\n\nNow, they ran over snowy hills and down into frozen valleys. They stopped only to rest and eat. They wanted to stay ahead of the other teams. The racers had to go a thousand miles across Alaska. Alaska is one of the coldest places on Earth. The dogs' thick fur coats helped keep them warm in the cold wind and weather. In many places along the route, the snow was deep. Pieces of ice were as sharp as a knife. The ice could cut the dogs' feet. To keep that from happening, Julie had put special booties on their feet.\n\nAt first, the dogs seemed to pull the sled very slowly. They were still getting used to the race. But on the third day out, they began to pull more quickly. They worked as a team and passed many of the other racers. Once, one of the sled's runners slid into a hole and broke. Julie could have given up then, but she didn't. She fixed it and they kept going.\n\nWhen they finally reached the finish line, they found out that they had come in first place! It was a great day for Julie and her dogs.",
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
        "passage": "The dogsled race was about to begin. Julie's team of dogs was lined up at the starting gate. Julie stood behind them. The air was so cold that she could see her breath. Other teams were lined up, too, and the dogs were excited. Julie kept her eyes on the clock. At exactly ten o'clock, she and the other racers yelled, 'Mush!' The dogs knew that meant 'Go!' They leap forward and the race began!\n\nJulie had trained for months for this race, and she hoped she and her dogs would win. Hour after hour, day after day, Julie's dogs pulled the sled in order to get in shape for the race.\n\nNow, they ran over snowy hills and down into frozen valleys. They stopped only to rest and eat. They wanted to stay ahead of the other teams. The racers had to go a thousand miles across Alaska. Alaska is one of the coldest places on Earth. The dogs' thick fur coats helped keep them warm in the cold wind and weather. In many places along the route, the snow was deep. Pieces of ice were as sharp as a knife. The ice could cut the dogs' feet. To keep that from happening, Julie had put special booties on their feet.\n\nAt first, the dogs seemed to pull the sled very slowly. They were still getting used to the race. But on the third day out, they began to pull more quickly. They worked as a team and passed many of the other racers. Once, one of the sled's runners slid into a hole and broke. Julie could have given up then, but she didn't. She fixed it and they kept going.\n\nWhen they finally reached the finish line, they found out that they had come in first place! It was a great day for Julie and her dogs.",
        "question": "The word 'thick' in paragraph 3 is closest in meaning to",
        "options": [
            "Fat",
            "Thin",
            "Hard",
            "Skinny"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (Multiple Choice)",
        "passage": "The dogsled race was about to begin. Julie's team of dogs was lined up at the starting gate. Julie stood behind them. The air was so cold that she could see her breath. Other teams were lined up, too, and the dogs were excited. Julie kept her eyes on the clock. At exactly ten o'clock, she and the other racers yelled, 'Mush!' The dogs knew that meant 'Go!' They leap forward and the race began!\n\nJulie had trained for months for this race, and she hoped she and her dogs would win. Hour after hour, day after day, Julie's dogs pulled the sled in order to get in shape for the race.\n\nNow, they ran over snowy hills and down into frozen valleys. They stopped only to rest and eat. They wanted to stay ahead of the other teams. The racers had to go a thousand miles across Alaska. Alaska is one of the coldest places on Earth. The dogs' thick fur coats helped keep them warm in the cold wind and weather. In many places along the route, the snow was deep. Pieces of ice were as sharp as a knife. The ice could cut the dogs' feet. To keep that from happening, Julie had put special booties on their feet.\n\nAt first, the dogs seemed to pull the sled very slowly. They were still getting used to the race. But on the third day out, they began to pull more quickly. They worked as a team and passed many of the other racers. Once, one of the sled's runners slid into a hole and broke. Julie could have given up then, but she didn't. She fixed it and they kept going.\n\nWhen they finally reached the finish line, they found out that they had come in first place! It was a great day for Julie and her dogs.",
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
        "passage": "It's that time of the year for school to start again. So that means you need to start stocking up on the supplies you need for the school year. Fortunately, you don't have to visit four or five different stores to get everything necessary. Instead, take a trip to Carter's Department Store. We've got everything that a student could possibly need.\n\nWe have all kinds of standard school supplies: pens, pencils, notebooks, rulers, and more. We also carry art supplies, such as paint, paintbrushes, and easels. You can purchase all sorts of electronic equipment, including calculators, desktop computers, and notebook computers. We even sell musical instruments.\n\nAnd here's the best part: from now until the beginning of the school year, we are having a back-to-school sale. Everything we carry that is related to school is on sale for at least 25% off. Art supplies are 30% off while electronic goods are available at 40% discount. And be sure to visit our boys' and girls' clothing departments, where you will find saving up to a whopping 60% off. You simply can't beat Carter's Department Store for quality and price.",
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
        "passage": "It's that time of the year for school to start again. So that means you need to start stocking up on the supplies you need for the school year. Fortunately, you don't have to visit four or five different stores to get everything necessary. Instead, take a trip to Carter's Department Store. We've got everything that a student could possibly need.\n\nWe have all kinds of standard school supplies: pens, pencils, notebooks, rulers, and more. We also carry art supplies, such as paint, paintbrushes, and easels. You can purchase all sorts of electronic equipment, including calculators, desktop computers, and notebook computers. We even sell musical instruments.\n\nAnd here's the best part: from now until the beginning of the school year, we are having a back-to-school sale. Everything we carry that is related to school is on sale for at least 25% off. Art supplies are 30% off while electronic goods are available at 40% discount. And be sure to visit our boys' and girls' clothing departments, where you will find saving up to a whopping 60% off. You simply can't beat Carter's Department Store for quality and price.",
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
        "passage": "It's that time of the year for school to start again. So that means you need to start stocking up on the supplies you need for the school year. Fortunately, you don't have to visit four or five different stores to get everything necessary. Instead, take a trip to Carter's Department Store. We've got everything that a student could possibly need.\n\nWe have all kinds of standard school supplies: pens, pencils, notebooks, rulers, and more. We also carry art supplies, such as paint, paintbrushes, and easels. You can purchase all sorts of electronic equipment, including calculators, desktop computers, and notebook computers. We even sell musical instruments.\n\nAnd here's the best part: from now until the beginning of the school year, we are having a back-to-school sale. Everything we carry that is related to school is on sale for at least 25% off. Art supplies are 30% off while electronic goods are available at 40% discount. And be sure to visit our boys' and girls' clothing departments, where you will find saving up to a whopping 60% off. You simply can't beat Carter's Department Store for quality and price.",
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
        "passage": "It's that time of the year for school to start again. So that means you need to start stocking up on the supplies you need for the school year. Fortunately, you don't have to visit four or five different stores to get everything necessary. Instead, take a trip to Carter's Department Store. We've got everything that a student could possibly need.\n\nWe have all kinds of standard school supplies: pens, pencils, notebooks, rulers, and more. We also carry art supplies, such as paint, paintbrushes, and easels. You can purchase all sorts of electronic equipment, including calculators, desktop computers, and notebook computers. We even sell musical instruments.\n\nAnd here's the best part: from now until the beginning of the school year, we are having a back-to-school sale. Everything we carry that is related to school is on sale for at least 25% off. Art supplies are 30% off while electronic goods are available at 40% discount. And be sure to visit our boys' and girls' clothing departments, where you will find saving up to a whopping 60% off. You simply can't beat Carter's Department Store for quality and price.",
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
        "passage": "It's that time of the year for school to start again. So that means you need to start stocking up on the supplies you need for the school year. Fortunately, you don't have to visit four or five different stores to get everything necessary. Instead, take a trip to Carter's Department Store. We've got everything that a student could possibly need.\n\nWe have all kinds of standard school supplies: pens, pencils, notebooks, rulers, and more. We also carry art supplies, such as paint, paintbrushes, and easels. You can purchase all sorts of electronic equipment, including calculators, desktop computers, and notebook computers. We even sell musical instruments.\n\nAnd here's the best part: from now until the beginning of the school year, we are having a back-to-school sale. Everything we carry that is related to school is on sale for at least 25% off. Art supplies are 30% off while electronic goods are available at 40% discount. And be sure to visit our boys' and girls' clothing departments, where you will find saving up to a whopping 60% off. You simply can't beat Carter's Department Store for quality and price.",
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
        "passage": "Jann Mardenborough has loved cars since he was given a toy one as a baby. He loved them so much that when he was eight his father took him to a place where children race small cars called karts. Staff at the kart centre told Jann he drove so well he might one day become a racing driver. Unfortunately, the kart centre closed soon afterwards, and there wasn't another one near enough to his home that he could get to.\n\nAs he couldn't race karts any more, Jann decided to try computer racing games. After lots of practice, he became very good. However, he never told his parents what he was doing. Then, one day, when he was 18, he told them that he was one of the top ten winners of a computer racing competition. They were very surprised. His prize was to drive a real car in a race against the other nine top players.\n\nIt was Jann's first time in a racing car, but, amazingly, he won the race! The prize this time was a free course to learn to be a racing driver. He did really well, and has found a job driving in a racing team.",
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
        "passage": "Jann Mardenborough has loved cars since he was given a toy one as a baby. He loved them so much that when he was eight his father took him to a place where children race small cars called karts. Staff at the kart centre told Jann he drove so well he might one day become a racing driver. Unfortunately, the kart centre closed soon afterwards, and there wasn't another one near enough to his home that he could get to.\n\nAs he couldn't race karts any more, Jann decided to try computer racing games. After lots of practice, he became very good. However, he never told his parents what he was doing. Then, one day, when he was 18, he told them that he was one of the top ten winners of a computer racing competition. They were very surprised. His prize was to drive a real car in a race against the other nine top players.\n\nIt was Jann's first time in a racing car, but, amazingly, he won the race! The prize this time was a free course to learn to be a racing driver. He did really well, and has found a job driving in a racing team.",
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
        "passage": "Jann Mardenborough has loved cars since he was given a toy one as a baby. He loved them so much that when he was eight his father took him to a place where children race small cars called karts. Staff at the kart centre told Jann he drove so well he might one day become a racing driver. Unfortunately, the kart centre closed soon afterwards, and there wasn't another one near enough to his home that he could get to.\n\nAs he couldn't race karts any more, Jann decided to try computer racing games. After lots of practice, he became very good. However, he never told his parents what he was doing. Then, one day, when he was 18, he told them that he was one of the top ten winners of a computer racing competition. They were very surprised. His prize was to drive a real car in a race against the other nine top players.\n\nIt was Jann's first time in a racing car, but, amazingly, he won the race! The prize this time was a free course to learn to be a racing driver. He did really well, and has found a job driving in a racing team.",
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
        "passage": "Jann Mardenborough has loved cars since he was given a toy one as a baby. He loved them so much that when he was eight his father took him to a place where children race small cars called karts. Staff at the kart centre told Jann he drove so well he might one day become a racing driver. Unfortunately, the kart centre closed soon afterwards, and there wasn't another one near enough to his home that he could get to.\n\nAs he couldn't race karts any more, Jann decided to try computer racing games. After lots of practice, he became very good. However, he never told his parents what he was doing. Then, one day, when he was 18, he told them that he was one of the top ten winners of a computer racing competition. They were very surprised. His prize was to drive a real car in a race against the other nine top players.\n\nIt was Jann's first time in a racing car, but, amazingly, he won the race! The prize this time was a free course to learn to be a racing driver. He did really well, and has found a job driving in a racing team.",
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
        "passage": "Jann Mardenborough has loved cars since he was given a toy one as a baby. He loved them so much that when he was eight his father took him to a place where children race small cars called karts. Staff at the kart centre told Jann he drove so well he might one day become a racing driver. Unfortunately, the kart centre closed soon afterwards, and there wasn't another one near enough to his home that he could get to.\n\nAs he couldn't race karts any more, Jann decided to try computer racing games. After lots of practice, he became very good. However, he never told his parents what he was doing. Then, one day, when he was 18, he told them that he was one of the top ten winners of a computer racing competition. They were very surprised. His prize was to drive a real car in a race against the other nine top players.\n\nIt was Jann's first time in a racing car, but, amazingly, he won the race! The prize this time was a free course to learn to be a racing driver. He did really well, and has found a job driving in a racing team.",
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
        "passage": "Jann Mardenborough has loved cars since he was given a toy one as a baby. He loved them so much that when he was eight his father took him to a place where children race small cars called karts. Staff at the kart centre told Jann he drove so well he might one day become a racing driver. Unfortunately, the kart centre closed soon afterwards, and there wasn't another one near enough to his home that he could get to.\n\nAs he couldn't race karts any more, Jann decided to try computer racing games. After lots of practice, he became very good. However, he never told his parents what he was doing. Then, one day, when he was 18, he told them that he was one of the top ten winners of a computer racing competition. They were very surprised. His prize was to drive a real car in a race against the other nine top players.\n\nIt was Jann's first time in a racing car, but, amazingly, he won the race! The prize this time was a free course to learn to be a racing driver. He did really well, and has found a job driving in a racing team.",
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
        "passage": "Jann Mardenborough has loved cars since he was given a toy one as a baby. He loved them so much that when he was eight his father took him to a place where children race small cars called karts. Staff at the kart centre told Jann he drove so well he might one day become a racing driver. Unfortunately, the kart centre closed soon afterwards, and there wasn't another one near enough to his home that he could get to.\n\nAs he couldn't race karts any more, Jann decided to try computer racing games. After lots of practice, he became very good. However, he never told his parents what he was doing. Then, one day, when he was 18, he told them that he was one of the top ten winners of a computer racing competition. They were very surprised. His prize was to drive a real car in a race against the other nine top players.\n\nIt was Jann's first time in a racing car, but, amazingly, he won the race! The prize this time was a free course to learn to be a racing driver. He did really well, and has found a job driving in a racing team.",
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
        "passage": "Every year, thousands of people come to Edinburgh, the capital city of Scotland, to be part of the Edinburgh Festival. For three weeks every August and September the city Is filled with actors and artists from all over the world. They come to Edinburgh for the biggest arts festival in Britain. During this time the streets of the city are alive with music and dance from early morning until late at night. You can even see artists painting pictures on the streets. One of the best parts of the Festival is the 'Fringe', where students do comedy shows in small halls and cafés.\n\nTens of thousands of tourists come to the Festival to see new films and plays and hear music played by famous musicians. This year, you can see over five hundred performances with actors from more than forty countries.\n\nThe tickets for these performances are quite cheap and it is usually easier to see your favourite star in Edinburgh than it is in London. So come to Edinburgh next summer, but remember it can be difficult to find a room, so why not book your hotel now!",
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
        "passage": "Every year, thousands of people come to Edinburgh, the capital city of Scotland, to be part of the Edinburgh Festival. For three weeks every August and September the city Is filled with actors and artists from all over the world. They come to Edinburgh for the biggest arts festival in Britain. During this time the streets of the city are alive with music and dance from early morning until late at night. You can even see artists painting pictures on the streets. One of the best parts of the Festival is the 'Fringe', where students do comedy shows in small halls and cafés.\n\nTens of thousands of tourists come to the Festival to see new films and plays and hear music played by famous musicians. This year, you can see over five hundred performances with actors from more than forty countries.\n\nThe tickets for these performances are quite cheap and it is usually easier to see your favourite star in Edinburgh than it is in London. So come to Edinburgh next summer, but remember it can be difficult to find a room, so why not book your hotel now!",
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
        "passage": "Every year, thousands of people come to Edinburgh, the capital city of Scotland, to be part of the Edinburgh Festival. For three weeks every August and September the city Is filled with actors and artists from all over the world. They come to Edinburgh for the biggest arts festival in Britain. During this time the streets of the city are alive with music and dance from early morning until late at night. You can even see artists painting pictures on the streets. One of the best parts of the Festival is the 'Fringe', where students do comedy shows in small halls and cafés.\n\nTens of thousands of tourists come to the Festival to see new films and plays and hear music played by famous musicians. This year, you can see over five hundred performances with actors from more than forty countries.\n\nThe tickets for these performances are quite cheap and it is usually easier to see your favourite star in Edinburgh than it is in London. So come to Edinburgh next summer, but remember it can be difficult to find a room, so why not book your hotel now!",
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
        "passage": "Every year, thousands of people come to Edinburgh, the capital city of Scotland, to be part of the Edinburgh Festival. For three weeks every August and September the city Is filled with actors and artists from all over the world. They come to Edinburgh for the biggest arts festival in Britain. During this time the streets of the city are alive with music and dance from early morning until late at night. You can even see artists painting pictures on the streets. One of the best parts of the Festival is the 'Fringe', where students do comedy shows in small halls and cafés.\n\nTens of thousands of tourists come to the Festival to see new films and plays and hear music played by famous musicians. This year, you can see over five hundred performances with actors from more than forty countries.\n\nThe tickets for these performances are quite cheap and it is usually easier to see your favourite star in Edinburgh than it is in London. So come to Edinburgh next summer, but remember it can be difficult to find a room, so why not book your hotel now!",
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
        "passage": "Every year, thousands of people come to Edinburgh, the capital city of Scotland, to be part of the Edinburgh Festival. For three weeks every August and September the city Is filled with actors and artists from all over the world. They come to Edinburgh for the biggest arts festival in Britain. During this time the streets of the city are alive with music and dance from early morning until late at night. You can even see artists painting pictures on the streets. One of the best parts of the Festival is the 'Fringe', where students do comedy shows in small halls and cafés.\n\nTens of thousands of tourists come to the Festival to see new films and plays and hear music played by famous musicians. This year, you can see over five hundred performances with actors from more than forty countries.\n\nThe tickets for these performances are quite cheap and it is usually easier to see your favourite star in Edinburgh than it is in London. So come to Edinburgh next summer, but remember it can be difficult to find a room, so why not book your hotel now!",
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
        "passage": "Every year, thousands of people come to Edinburgh, the capital city of Scotland, to be part of the Edinburgh Festival. For three weeks every August and September the city Is filled with actors and artists from all over the world. They come to Edinburgh for the biggest arts festival in Britain. During this time the streets of the city are alive with music and dance from early morning until late at night. You can even see artists painting pictures on the streets. One of the best parts of the Festival is the 'Fringe', where students do comedy shows in small halls and cafés.\n\nTens of thousands of tourists come to the Festival to see new films and plays and hear music played by famous musicians. This year, you can see over five hundred performances with actors from more than forty countries.\n\nThe tickets for these performances are quite cheap and it is usually easier to see your favourite star in Edinburgh than it is in London. So come to Edinburgh next summer, but remember it can be difficult to find a room, so why not book your hotel now!",
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
        "passage": "Every year, thousands of people come to Edinburgh, the capital city of Scotland, to be part of the Edinburgh Festival. For three weeks every August and September the city Is filled with actors and artists from all over the world. They come to Edinburgh for the biggest arts festival in Britain. During this time the streets of the city are alive with music and dance from early morning until late at night. You can even see artists painting pictures on the streets. One of the best parts of the Festival is the 'Fringe', where students do comedy shows in small halls and cafés.\n\nTens of thousands of tourists come to the Festival to see new films and plays and hear music played by famous musicians. This year, you can see over five hundred performances with actors from more than forty countries.\n\nThe tickets for these performances are quite cheap and it is usually easier to see your favourite star in Edinburgh than it is in London. So come to Edinburgh next summer, but remember it can be difficult to find a room, so why not book your hotel now!",
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
        "passage": "Most house burglaries happen between 2 p.m. and 6 p.m., say the police.\n\nInspector Ian Saunders told our newspaper that the number of house burglaries has gone up by more than 30% compared with last year. He also said that 67% of burglaries happen when people have gone out and forgotten to close a door or a window.\n\nHe went on to report that night-time burglaries are unusual because families are usually at home at that time. But he said that winter afternoons are the best time for burglars because it is dark and they can't be seen easily. Also many houses are empty at that time, because people are often still at work.\n\nInspector Saunders said that it is a good idea to leave lights on in living rooms and bedrooms when you go on holiday. This will help to keep burglars away. He also asked neighbors to watch the other houses in the street when people are not at home. They should call the police if they see anything strange. 'We will also tell you how to make your house safe', Inspector Saunders said. 'This kind of help costs nothing'.",
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
        "passage": "Most house burglaries happen between 2 p.m. and 6 p.m., say the police.\n\nInspector Ian Saunders told our newspaper that the number of house burglaries has gone up by more than 30% compared with last year. He also said that 67% of burglaries happen when people have gone out and forgotten to close a door or a window.\n\nHe went on to report that night-time burglaries are unusual because families are usually at home at that time. But he said that winter afternoons are the best time for burglars because it is dark and they can't be seen easily. Also many houses are empty at that time, because people are often still at work.\n\nInspector Saunders said that it is a good idea to leave lights on in living rooms and bedrooms when you go on holiday. This will help to keep burglars away. He also asked neighbors to watch the other houses in the street when people are not at home. They should call the police if they see anything strange. 'We will also tell you how to make your house safe', Inspector Saunders said. 'This kind of help costs nothing'.",
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
        "passage": "Most house burglaries happen between 2 p.m. and 6 p.m., say the police.\n\nInspector Ian Saunders told our newspaper that the number of house burglaries has gone up by more than 30% compared with last year. He also said that 67% of burglaries happen when people have gone out and forgotten to close a door or a window.\n\nHe went on to report that night-time burglaries are unusual because families are usually at home at that time. But he said that winter afternoons are the best time for burglars because it is dark and they can't be seen easily. Also many houses are empty at that time, because people are often still at work.\n\nInspector Saunders said that it is a good idea to leave lights on in living rooms and bedrooms when you go on holiday. This will help to keep burglars away. He also asked neighbors to watch the other houses in the street when people are not at home. They should call the police if they see anything strange. 'We will also tell you how to make your house safe', Inspector Saunders said. 'This kind of help costs nothing'.",
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
        "passage": "Most house burglaries happen between 2 p.m. and 6 p.m., say the police.\n\nInspector Ian Saunders told our newspaper that the number of house burglaries has gone up by more than 30% compared with last year. He also said that 67% of burglaries happen when people have gone out and forgotten to close a door or a window.\n\nHe went on to report that night-time burglaries are unusual because families are usually at home at that time. But he said that winter afternoons are the best time for burglars because it is dark and they can't be seen easily. Also many houses are empty at that time, because people are often still at work.\n\nInspector Saunders said that it is a good idea to leave lights on in living rooms and bedrooms when you go on holiday. This will help to keep burglars away. He also asked neighbors to watch the other houses in the street when people are not at home. They should call the police if they see anything strange. 'We will also tell you how to make your house safe', Inspector Saunders said. 'This kind of help costs nothing'.",
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
        "passage": "Most house burglaries happen between 2 p.m. and 6 p.m., say the police.\n\nInspector Ian Saunders told our newspaper that the number of house burglaries has gone up by more than 30% compared with last year. He also said that 67% of burglaries happen when people have gone out and forgotten to close a door or a window.\n\nHe went on to report that night-time burglaries are unusual because families are usually at home at that time. But he said that winter afternoons are the best time for burglars because it is dark and they can't be seen easily. Also many houses are empty at that time, because people are often still at work.\n\nInspector Saunders said that it is a good idea to leave lights on in living rooms and bedrooms when you go on holiday. This will help to keep burglars away. He also asked neighbors to watch the other houses in the street when people are not at home. They should call the police if they see anything strange. 'We will also tell you how to make your house safe', Inspector Saunders said. 'This kind of help costs nothing'.",
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
        "passage": "Most house burglaries happen between 2 p.m. and 6 p.m., say the police.\n\nInspector Ian Saunders told our newspaper that the number of house burglaries has gone up by more than 30% compared with last year. He also said that 67% of burglaries happen when people have gone out and forgotten to close a door or a window.\n\nHe went on to report that night-time burglaries are unusual because families are usually at home at that time. But he said that winter afternoons are the best time for burglars because it is dark and they can't be seen easily. Also many houses are empty at that time, because people are often still at work.\n\nInspector Saunders said that it is a good idea to leave lights on in living rooms and bedrooms when you go on holiday. This will help to keep burglars away. He also asked neighbors to watch the other houses in the street when people are not at home. They should call the police if they see anything strange. 'We will also tell you how to make your house safe', Inspector Saunders said. 'This kind of help costs nothing'.",
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
        "passage": "Most house burglaries happen between 2 p.m. and 6 p.m., say the police.\n\nInspector Ian Saunders told our newspaper that the number of house burglaries has gone up by more than 30% compared with last year. He also said that 67% of burglaries happen when people have gone out and forgotten to close a door or a window.\n\nHe went on to report that night-time burglaries are unusual because families are usually at home at that time. But he said that winter afternoons are the best time for burglars because it is dark and they can't be seen easily. Also many houses are empty at that time, because people are often still at work.\n\nInspector Saunders said that it is a good idea to leave lights on in living rooms and bedrooms when you go on holiday. This will help to keep burglars away. He also asked neighbors to watch the other houses in the street when people are not at home. They should call the police if they see anything strange. 'We will also tell you how to make your house safe', Inspector Saunders said. 'This kind of help costs nothing'.",
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
        "passage": "Nick Barlow loves his work. He's a British actor and he travels around the world making TV programmes. 'People welcome me everywhere I go and when I get home I remember all the wonderful things that happened in each country.' Nick has travelled to many places but there are a few trips that he would still like to make. 'I'd love to visit South America and go back to Australia one day,' he says.\n\nOn each trip, Nick travels with a team of people. They bring the cameras and other filming equipment needed to make the program. Nick doesn't take a lot of things for himself, just a few shirts and trousers, but he always makes sure he has some books in his suitcase.\n\nNick's wife, Helen, doesn't mind him travelling for his work. She has a lot of friends and keeps busy. When he gets back, she likes to listen to all his travel stories. But sometimes there are problems. When he was in the Malaysian rain forest, Nick heard that his wife was ill in hospital. I felt terrible because I couldn't help, but she didn't want me to come home. I was so happy when I heard she was better.'",
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
        "passage": "Nick Barlow loves his work. He's a British actor and he travels around the world making TV programmes. 'People welcome me everywhere I go and when I get home I remember all the wonderful things that happened in each country.' Nick has travelled to many places but there are a few trips that he would still like to make. 'I'd love to visit South America and go back to Australia one day,' he says.\n\nOn each trip, Nick travels with a team of people. They bring the cameras and other filming equipment needed to make the program. Nick doesn't take a lot of things for himself, just a few shirts and trousers, but he always makes sure he has some books in his suitcase.\n\nNick's wife, Helen, doesn't mind him travelling for his work. She has a lot of friends and keeps busy. When he gets back, she likes to listen to all his travel stories. But sometimes there are problems. When he was in the Malaysian rain forest, Nick heard that his wife was ill in hospital. I felt terrible because I couldn't help, but she didn't want me to come home. I was so happy when I heard she was better.'",
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
        "passage": "Nick Barlow loves his work. He's a British actor and he travels around the world making TV programmes. 'People welcome me everywhere I go and when I get home I remember all the wonderful things that happened in each country.' Nick has travelled to many places but there are a few trips that he would still like to make. 'I'd love to visit South America and go back to Australia one day,' he says.\n\nOn each trip, Nick travels with a team of people. They bring the cameras and other filming equipment needed to make the program. Nick doesn't take a lot of things for himself, just a few shirts and trousers, but he always makes sure he has some books in his suitcase.\n\nNick's wife, Helen, doesn't mind him travelling for his work. She has a lot of friends and keeps busy. When he gets back, she likes to listen to all his travel stories. But sometimes there are problems. When he was in the Malaysian rain forest, Nick heard that his wife was ill in hospital. I felt terrible because I couldn't help, but she didn't want me to come home. I was so happy when I heard she was better.'",
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
        "passage": "Nick Barlow loves his work. He's a British actor and he travels around the world making TV programmes. 'People welcome me everywhere I go and when I get home I remember all the wonderful things that happened in each country.' Nick has travelled to many places but there are a few trips that he would still like to make. 'I'd love to visit South America and go back to Australia one day,' he says.\n\nOn each trip, Nick travels with a team of people. They bring the cameras and other filming equipment needed to make the program. Nick doesn't take a lot of things for himself, just a few shirts and trousers, but he always makes sure he has some books in his suitcase.\n\nNick's wife, Helen, doesn't mind him travelling for his work. She has a lot of friends and keeps busy. When he gets back, she likes to listen to all his travel stories. But sometimes there are problems. When he was in the Malaysian rain forest, Nick heard that his wife was ill in hospital. I felt terrible because I couldn't help, but she didn't want me to come home. I was so happy when I heard she was better.'",
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
        "passage": "Nick Barlow loves his work. He's a British actor and he travels around the world making TV programmes. 'People welcome me everywhere I go and when I get home I remember all the wonderful things that happened in each country.' Nick has travelled to many places but there are a few trips that he would still like to make. 'I'd love to visit South America and go back to Australia one day,' he says.\n\nOn each trip, Nick travels with a team of people. They bring the cameras and other filming equipment needed to make the program. Nick doesn't take a lot of things for himself, just a few shirts and trousers, but he always makes sure he has some books in his suitcase.\n\nNick's wife, Helen, doesn't mind him travelling for his work. She has a lot of friends and keeps busy. When he gets back, she likes to listen to all his travel stories. But sometimes there are problems. When he was in the Malaysian rain forest, Nick heard that his wife was ill in hospital. I felt terrible because I couldn't help, but she didn't want me to come home. I was so happy when I heard she was better.'",
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
        "passage": "Nick Barlow loves his work. He's a British actor and he travels around the world making TV programmes. 'People welcome me everywhere I go and when I get home I remember all the wonderful things that happened in each country.' Nick has travelled to many places but there are a few trips that he would still like to make. 'I'd love to visit South America and go back to Australia one day,' he says.\n\nOn each trip, Nick travels with a team of people. They bring the cameras and other filming equipment needed to make the program. Nick doesn't take a lot of things for himself, just a few shirts and trousers, but he always makes sure he has some books in his suitcase.\n\nNick's wife, Helen, doesn't mind him travelling for his work. She has a lot of friends and keeps busy. When he gets back, she likes to listen to all his travel stories. But sometimes there are problems. When he was in the Malaysian rain forest, Nick heard that his wife was ill in hospital. I felt terrible because I couldn't help, but she didn't want me to come home. I was so happy when I heard she was better.'",
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
        "passage": "Nick Barlow loves his work. He's a British actor and he travels around the world making TV programmes. 'People welcome me everywhere I go and when I get home I remember all the wonderful things that happened in each country.' Nick has travelled to many places but there are a few trips that he would still like to make. 'I'd love to visit South America and go back to Australia one day,' he says.\n\nOn each trip, Nick travels with a team of people. They bring the cameras and other filming equipment needed to make the program. Nick doesn't take a lot of things for himself, just a few shirts and trousers, but he always makes sure he has some books in his suitcase.\n\nNick's wife, Helen, doesn't mind him travelling for his work. She has a lot of friends and keeps busy. When he gets back, she likes to listen to all his travel stories. But sometimes there are problems. When he was in the Malaysian rain forest, Nick heard that his wife was ill in hospital. I felt terrible because I couldn't help, but she didn't want me to come home. I was so happy when I heard she was better.'",
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
        "passage": "David Johnson has loved swimming all his life. When he was 27, he swam in a race near his home in the USA. The sea was very cold and David started to feel unwell. He was taken to hospital but he soon got better and started swimming again. In 1983, he became the first person to swim from Santa Cruz Island to the Californian coast.\n\nIn January 2004, at the age of 52, David crossed New Zealand's Cook Strait in 9 hours and 38 minutes. The oldest swimmer before David was only 42 years old. David spent over a year getting ready to swim the Strait. Then, he and his wife flew to New Zealand so that David could practise for a few weeks there. But, only days after they arrived, the weather improved so David decided to start his swim. He did it with the help of a team. 'They were great' David said. 'They were in a boat next to me all the time! After a few hours, I thought about stopping but I didn't and went on swimming.'\n\nAfterwards, David and his wife travelled around New Zealand before returning to the USA.",
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
        "passage": "David Johnson has loved swimming all his life. When he was 27, he swam in a race near his home in the USA. The sea was very cold and David started to feel unwell. He was taken to hospital but he soon got better and started swimming again. In 1983, he became the first person to swim from Santa Cruz Island to the Californian coast.\n\nIn January 2004, at the age of 52, David crossed New Zealand's Cook Strait in 9 hours and 38 minutes. The oldest swimmer before David was only 42 years old. David spent over a year getting ready to swim the Strait. Then, he and his wife flew to New Zealand so that David could practise for a few weeks there. But, only days after they arrived, the weather improved so David decided to start his swim. He did it with the help of a team. 'They were great' David said. 'They were in a boat next to me all the time! After a few hours, I thought about stopping but I didn't and went on swimming.'\n\nAfterwards, David and his wife travelled around New Zealand before returning to the USA.",
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
        "passage": "David Johnson has loved swimming all his life. When he was 27, he swam in a race near his home in the USA. The sea was very cold and David started to feel unwell. He was taken to hospital but he soon got better and started swimming again. In 1983, he became the first person to swim from Santa Cruz Island to the Californian coast.\n\nIn January 2004, at the age of 52, David crossed New Zealand's Cook Strait in 9 hours and 38 minutes. The oldest swimmer before David was only 42 years old. David spent over a year getting ready to swim the Strait. Then, he and his wife flew to New Zealand so that David could practise for a few weeks there. But, only days after they arrived, the weather improved so David decided to start his swim. He did it with the help of a team. 'They were great' David said. 'They were in a boat next to me all the time! After a few hours, I thought about stopping but I didn't and went on swimming.'\n\nAfterwards, David and his wife travelled around New Zealand before returning to the USA.",
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
        "passage": "David Johnson has loved swimming all his life. When he was 27, he swam in a race near his home in the USA. The sea was very cold and David started to feel unwell. He was taken to hospital but he soon got better and started swimming again. In 1983, he became the first person to swim from Santa Cruz Island to the Californian coast.\n\nIn January 2004, at the age of 52, David crossed New Zealand's Cook Strait in 9 hours and 38 minutes. The oldest swimmer before David was only 42 years old. David spent over a year getting ready to swim the Strait. Then, he and his wife flew to New Zealand so that David could practise for a few weeks there. But, only days after they arrived, the weather improved so David decided to start his swim. He did it with the help of a team. 'They were great' David said. 'They were in a boat next to me all the time! After a few hours, I thought about stopping but I didn't and went on swimming.'\n\nAfterwards, David and his wife travelled around New Zealand before returning to the USA.",
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
        "passage": "David Johnson has loved swimming all his life. When he was 27, he swam in a race near his home in the USA. The sea was very cold and David started to feel unwell. He was taken to hospital but he soon got better and started swimming again. In 1983, he became the first person to swim from Santa Cruz Island to the Californian coast.\n\nIn January 2004, at the age of 52, David crossed New Zealand's Cook Strait in 9 hours and 38 minutes. The oldest swimmer before David was only 42 years old. David spent over a year getting ready to swim the Strait. Then, he and his wife flew to New Zealand so that David could practise for a few weeks there. But, only days after they arrived, the weather improved so David decided to start his swim. He did it with the help of a team. 'They were great' David said. 'They were in a boat next to me all the time! After a few hours, I thought about stopping but I didn't and went on swimming.'\n\nAfterwards, David and his wife travelled around New Zealand before returning to the USA.",
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
        "passage": "David Johnson has loved swimming all his life. When he was 27, he swam in a race near his home in the USA. The sea was very cold and David started to feel unwell. He was taken to hospital but he soon got better and started swimming again. In 1983, he became the first person to swim from Santa Cruz Island to the Californian coast.\n\nIn January 2004, at the age of 52, David crossed New Zealand's Cook Strait in 9 hours and 38 minutes. The oldest swimmer before David was only 42 years old. David spent over a year getting ready to swim the Strait. Then, he and his wife flew to New Zealand so that David could practise for a few weeks there. But, only days after they arrived, the weather improved so David decided to start his swim. He did it with the help of a team. 'They were great' David said. 'They were in a boat next to me all the time! After a few hours, I thought about stopping but I didn't and went on swimming.'\n\nAfterwards, David and his wife travelled around New Zealand before returning to the USA.",
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
        "passage": "David Johnson has loved swimming all his life. When he was 27, he swam in a race near his home in the USA. The sea was very cold and David started to feel unwell. He was taken to hospital but he soon got better and started swimming again. In 1983, he became the first person to swim from Santa Cruz Island to the Californian coast.\n\nIn January 2004, at the age of 52, David crossed New Zealand's Cook Strait in 9 hours and 38 minutes. The oldest swimmer before David was only 42 years old. David spent over a year getting ready to swim the Strait. Then, he and his wife flew to New Zealand so that David could practise for a few weeks there. But, only days after they arrived, the weather improved so David decided to start his swim. He did it with the help of a team. 'They were great' David said. 'They were in a boat next to me all the time! After a few hours, I thought about stopping but I didn't and went on swimming.'\n\nAfterwards, David and his wife travelled around New Zealand before returning to the USA.",
        "question": "David had to stop for a short time while swimming the Cook Strait.",
        "options": [
            "Right",
            "Wrong",
            "Doesn't say"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (T/F)",
        "passage": "Not long ago people believed that in the future we would work less, have more free time, and be more relaxed. But sadly this has not happened. Today we work harder, work longer hours, and are more stressed than ten years ago. We walk faster, talk faster, and sleep less than previous generations. And although we are obsessed with machines which save us time, we have less free time than our parents and grandparents had.\n\nBut what is this doing to our health? An American journalist James Gleick in a new book, Faster: the acceleration of just about everything, says that people who live in cities are suffering from 'hurry sickness' - we are always trying to do more things in less time. As a result, our lives are more stressful. He says that if we don't slow down, we won't live as long as our parents. For most people, faster doesn't mean better.\n\n1 No time for the news\nNewspaper articles today are shorter and the headlines are bigger. Most people don't have enough time to read the articles, they only read the headlines! On TV and the radio, newsreaders speak more quickly than ten years ago.\n\n2 No time for stories\nIn the USA there is a book called One-Minute Bedtime Stories for children. These are shorter versions of traditional stories, specially written for 'busy parents' who want to save time!\n\n3. No time to listen\nSome answerphones now have 'quick playback' buttons so that we can re-play people's messages faster - we can't waste time listening to people speaking at normal speed.\n\n4 No time to relax\nEven when we relax we do everything more quickly. Ten years ago when people went to art galleries they spent ten seconds looking at each picture. Today they spend just three seconds!\n\n5 No time for slow sports\nIn the USA the national sport, baseball, is not as popular as before it is a slow game and matches take a long time. Nowadays many people prefer faster and more dynamic sports like basketball.\n\n6...but more time in our cars\nThe only thing that is slower than before is the way we drive. Our cars are faster but the traffic is worse so we drive more slowly. We spend more time sitting in our cars, feeling stressed because we are worried that we won't arrive on time. Experts predict that in ten years' time the average speed on the road in cities will be 17 km/h.",
        "question": "The writer wrote the article to encourage us to work more and relax less.",
        "options": [
            "TRUE",
            "FALSE"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (T/F)",
        "passage": "Not long ago people believed that in the future we would work less, have more free time, and be more relaxed. But sadly this has not happened. Today we work harder, work longer hours, and are more stressed than ten years ago. We walk faster, talk faster, and sleep less than previous generations. And although we are obsessed with machines which save us time, we have less free time than our parents and grandparents had.\n\nBut what is this doing to our health? An American journalist James Gleick in a new book, Faster: the acceleration of just about everything, says that people who live in cities are suffering from 'hurry sickness' - we are always trying to do more things in less time. As a result, our lives are more stressful. He says that if we don't slow down, we won't live as long as our parents. For most people, faster doesn't mean better.\n\n1 No time for the news\nNewspaper articles today are shorter and the headlines are bigger. Most people don't have enough time to read the articles, they only read the headlines! On TV and the radio, newsreaders speak more quickly than ten years ago.\n\n2 No time for stories\nIn the USA there is a book called One-Minute Bedtime Stories for children. These are shorter versions of traditional stories, specially written for 'busy parents' who want to save time!\n\n3. No time to listen\nSome answerphones now have 'quick playback' buttons so that we can re-play people's messages faster - we can't waste time listening to people speaking at normal speed.\n\n4 No time to relax\nEven when we relax we do everything more quickly. Ten years ago when people went to art galleries they spent ten seconds looking at each picture. Today they spend just three seconds!\n\n5 No time for slow sports\nIn the USA the national sport, baseball, is not as popular as before it is a slow game and matches take a long time. Nowadays many people prefer faster and more dynamic sports like basketball.\n\n6...but more time in our cars\nThe only thing that is slower than before is the way we drive. Our cars are faster but the traffic is worse so we drive more slowly. We spend more time sitting in our cars, feeling stressed because we are worried that we won't arrive on time. Experts predict that in ten years' time the average speed on the road in cities will be 17 km/h.",
        "question": "People today are having a less stressful life than they did in the past.",
        "options": [
            "TRUE",
            "FALSE"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (T/F)",
        "passage": "Not long ago people believed that in the future we would work less, have more free time, and be more relaxed. But sadly this has not happened. Today we work harder, work longer hours, and are more stressed than ten years ago. We walk faster, talk faster, and sleep less than previous generations. And although we are obsessed with machines which save us time, we have less free time than our parents and grandparents had.\n\nBut what is this doing to our health? An American journalist James Gleick in a new book, Faster: the acceleration of just about everything, says that people who live in cities are suffering from 'hurry sickness' - we are always trying to do more things in less time. As a result, our lives are more stressful. He says that if we don't slow down, we won't live as long as our parents. For most people, faster doesn't mean better.\n\n1 No time for the news\nNewspaper articles today are shorter and the headlines are bigger. Most people don't have enough time to read the articles, they only read the headlines! On TV and the radio, newsreaders speak more quickly than ten years ago.\n\n2 No time for stories\nIn the USA there is a book called One-Minute Bedtime Stories for children. These are shorter versions of traditional stories, specially written for 'busy parents' who want to save time!\n\n3. No time to listen\nSome answerphones now have 'quick playback' buttons so that we can re-play people's messages faster - we can't waste time listening to people speaking at normal speed.\n\n4 No time to relax\nEven when we relax we do everything more quickly. Ten years ago when people went to art galleries they spent ten seconds looking at each picture. Today they spend just three seconds!\n\n5 No time for slow sports\nIn the USA the national sport, baseball, is not as popular as before it is a slow game and matches take a long time. Nowadays many people prefer faster and more dynamic sports like basketball.\n\n6...but more time in our cars\nThe only thing that is slower than before is the way we drive. Our cars are faster but the traffic is worse so we drive more slowly. We spend more time sitting in our cars, feeling stressed because we are worried that we won't arrive on time. Experts predict that in ten years' time the average speed on the road in cities will be 17 km/h.",
        "question": "People are too busy to read newspapers.",
        "options": [
            "TRUE",
            "FALSE"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (T/F)",
        "passage": "Not long ago people believed that in the future we would work less, have more free time, and be more relaxed. But sadly this has not happened. Today we work harder, work longer hours, and are more stressed than ten years ago. We walk faster, talk faster, and sleep less than previous generations. And although we are obsessed with machines which save us time, we have less free time than our parents and grandparents had.\n\nBut what is this doing to our health? An American journalist James Gleick in a new book, Faster: the acceleration of just about everything, says that people who live in cities are suffering from 'hurry sickness' - we are always trying to do more things in less time. As a result, our lives are more stressful. He says that if we don't slow down, we won't live as long as our parents. For most people, faster doesn't mean better.\n\n1 No time for the news\nNewspaper articles today are shorter and the headlines are bigger. Most people don't have enough time to read the articles, they only read the headlines! On TV and the radio, newsreaders speak more quickly than ten years ago.\n\n2 No time for stories\nIn the USA there is a book called One-Minute Bedtime Stories for children. These are shorter versions of traditional stories, specially written for 'busy parents' who want to save time!\n\n3. No time to listen\nSome answerphones now have 'quick playback' buttons so that we can re-play people's messages faster - we can't waste time listening to people speaking at normal speed.\n\n4 No time to relax\nEven when we relax we do everything more quickly. Ten years ago when people went to art galleries they spent ten seconds looking at each picture. Today they spend just three seconds!\n\n5 No time for slow sports\nIn the USA the national sport, baseball, is not as popular as before it is a slow game and matches take a long time. Nowadays many people prefer faster and more dynamic sports like basketball.\n\n6...but more time in our cars\nThe only thing that is slower than before is the way we drive. Our cars are faster but the traffic is worse so we drive more slowly. We spend more time sitting in our cars, feeling stressed because we are worried that we won't arrive on time. Experts predict that in ten years' time the average speed on the road in cities will be 17 km/h.",
        "question": "Slow sports have become unpopular.",
        "options": [
            "TRUE",
            "FALSE"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (T/F)",
        "passage": "Not long ago people believed that in the future we would work less, have more free time, and be more relaxed. But sadly this has not happened. Today we work harder, work longer hours, and are more stressed than ten years ago. We walk faster, talk faster, and sleep less than previous generations. And although we are obsessed with machines which save us time, we have less free time than our parents and grandparents had.\n\nBut what is this doing to our health? An American journalist James Gleick in a new book, Faster: the acceleration of just about everything, says that people who live in cities are suffering from 'hurry sickness' - we are always trying to do more things in less time. As a result, our lives are more stressful. He says that if we don't slow down, we won't live as long as our parents. For most people, faster doesn't mean better.\n\n1 No time for the news\nNewspaper articles today are shorter and the headlines are bigger. Most people don't have enough time to read the articles, they only read the headlines! On TV and the radio, newsreaders speak more quickly than ten years ago.\n\n2 No time for stories\nIn the USA there is a book called One-Minute Bedtime Stories for children. These are shorter versions of traditional stories, specially written for 'busy parents' who want to save time!\n\n3. No time to listen\nSome answerphones now have 'quick playback' buttons so that we can re-play people's messages faster - we can't waste time listening to people speaking at normal speed.\n\n4 No time to relax\nEven when we relax we do everything more quickly. Ten years ago when people went to art galleries they spent ten seconds looking at each picture. Today they spend just three seconds!\n\n5 No time for slow sports\nIn the USA the national sport, baseball, is not as popular as before it is a slow game and matches take a long time. Nowadays many people prefer faster and more dynamic sports like basketball.\n\n6...but more time in our cars\nThe only thing that is slower than before is the way we drive. Our cars are faster but the traffic is worse so we drive more slowly. We spend more time sitting in our cars, feeling stressed because we are worried that we won't arrive on time. Experts predict that in ten years' time the average speed on the road in cities will be 17 km/h.",
        "question": "More time is spent on stories.",
        "options": [
            "TRUE",
            "FALSE"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (T/F)",
        "passage": "1. Prince William is a member of the British royal family. He's the Queen's grandson and the eldest son of Charles and Diana. His brother's name is Harry. Diana, their mother, isn't alive now, but they have a stepmother, Camilla.\n\n2. William's wife is Kate Middleton. She's originally from an ordinary family but of course, she's now the Duchess of Cambridge and part of the royal family. Kate has a brother, James, and a sister, Pippa. Their parents, Michael and Carole, have an online business.\n\n3. In some ways, Kate and William are a normal couple. They have friends from university and they have hobbies and interests too. For example, William loves football and Kate likes photography. In the winter, they go skiing together.\n\n4. In other ways, their lives are very different from their friends' lives. William is the future King of the United Kingdom and fifteen other countries too, including Canada and Australia. Kate and William have a lot of official duties. They help charities in the UK and Africa, they visit other countries and they meet important visitors to the UK.\n\n5. The Duchess of Cambridge is expecting a baby, St James's Palace has confirmed. All the members of the royal family and the Duchess's family, the Middletons, are delighted: 'The Queen, the Duke of Edinburgh, the Prince of Wales, the Duchess of Cornwall and Prince Harry and members of both families are delighted with the news.'\n\nThe baby will be third in line to the throne, after Prince Charles and Prince William. A spokesman said the Duchess has been admitted to King Edward VII Hospital in central London with acute morning sickness and is expected to stay for several days: 'As the pregnancy is in its very early stages, her royal highness is expected to stay in hospital for several days and will require a period of rest thereafter.'\n\n6. Prince William, the Duke of Cambridge, says he and his wife 'could not be happier' after the Duchess gave birth to a baby boy, at 16:30, 22nd July 2013 UK time at St Mary's Hospital, west London. William was present at St Mary's for the birth. The young parents spent time with their son before telling the news to their families and the world. The Queen's gynecologist Marcus Setchell, who led the team that delivered the baby, described the new arrival as 'wonderful baby, beautiful baby'. A bulletin signed by him was taken by a royal aide from St Mary's to the palace under police escort. The news has been since displayed on an easel in the forecourt of Buckingham Palace in line with tradition. A palace spokesman said the names of the baby would be announced in due course. A Buckingham Palace spokesman said: 'The Queen and Duke of Edinburgh are delighted at the news.'",
        "question": "Camilla is William's mother.",
        "options": [
            "TRUE",
            "FALSE"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (T/F)",
        "passage": "1. Prince William is a member of the British royal family. He's the Queen's grandson and the eldest son of Charles and Diana. His brother's name is Harry. Diana, their mother, isn't alive now, but they have a stepmother, Camilla.\n\n2. William's wife is Kate Middleton. She's originally from an ordinary family but of course, she's now the Duchess of Cambridge and part of the royal family. Kate has a brother, James, and a sister, Pippa. Their parents, Michael and Carole, have an online business.\n\n3. In some ways, Kate and William are a normal couple. They have friends from university and they have hobbies and interests too. For example, William loves football and Kate likes photography. In the winter, they go skiing together.\n\n4. In other ways, their lives are very different from their friends' lives. William is the future King of the United Kingdom and fifteen other countries too, including Canada and Australia. Kate and William have a lot of official duties. They help charities in the UK and Africa, they visit other countries and they meet important visitors to the UK.\n\n5. The Duchess of Cambridge is expecting a baby, St James's Palace has confirmed. All the members of the royal family and the Duchess's family, the Middletons, are delighted: 'The Queen, the Duke of Edinburgh, the Prince of Wales, the Duchess of Cornwall and Prince Harry and members of both families are delighted with the news.'\n\nThe baby will be third in line to the throne, after Prince Charles and Prince William. A spokesman said the Duchess has been admitted to King Edward VII Hospital in central London with acute morning sickness and is expected to stay for several days: 'As the pregnancy is in its very early stages, her royal highness is expected to stay in hospital for several days and will require a period of rest thereafter.'\n\n6. Prince William, the Duke of Cambridge, says he and his wife 'could not be happier' after the Duchess gave birth to a baby boy, at 16:30, 22nd July 2013 UK time at St Mary's Hospital, west London. William was present at St Mary's for the birth. The young parents spent time with their son before telling the news to their families and the world. The Queen's gynecologist Marcus Setchell, who led the team that delivered the baby, described the new arrival as 'wonderful baby, beautiful baby'. A bulletin signed by him was taken by a royal aide from St Mary's to the palace under police escort. The news has been since displayed on an easel in the forecourt of Buckingham Palace in line with tradition. A palace spokesman said the names of the baby would be announced in due course. A Buckingham Palace spokesman said: 'The Queen and Duke of Edinburgh are delighted at the news.'",
        "question": "William's wife is the Duchess of Cambridge.",
        "options": [
            "TRUE",
            "FALSE"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (T/F)",
        "passage": "1. Prince William is a member of the British royal family. He's the Queen's grandson and the eldest son of Charles and Diana. His brother's name is Harry. Diana, their mother, isn't alive now, but they have a stepmother, Camilla.\n\n2. William's wife is Kate Middleton. She's originally from an ordinary family but of course, she's now the Duchess of Cambridge and part of the royal family. Kate has a brother, James, and a sister, Pippa. Their parents, Michael and Carole, have an online business.\n\n3. In some ways, Kate and William are a normal couple. They have friends from university and they have hobbies and interests too. For example, William loves football and Kate likes photography. In the winter, they go skiing together.\n\n4. In other ways, their lives are very different from their friends' lives. William is the future King of the United Kingdom and fifteen other countries too, including Canada and Australia. Kate and William have a lot of official duties. They help charities in the UK and Africa, they visit other countries and they meet important visitors to the UK.\n\n5. The Duchess of Cambridge is expecting a baby, St James's Palace has confirmed. All the members of the royal family and the Duchess's family, the Middletons, are delighted: 'The Queen, the Duke of Edinburgh, the Prince of Wales, the Duchess of Cornwall and Prince Harry and members of both families are delighted with the news.'\n\nThe baby will be third in line to the throne, after Prince Charles and Prince William. A spokesman said the Duchess has been admitted to King Edward VII Hospital in central London with acute morning sickness and is expected to stay for several days: 'As the pregnancy is in its very early stages, her royal highness is expected to stay in hospital for several days and will require a period of rest thereafter.'\n\n6. Prince William, the Duke of Cambridge, says he and his wife 'could not be happier' after the Duchess gave birth to a baby boy, at 16:30, 22nd July 2013 UK time at St Mary's Hospital, west London. William was present at St Mary's for the birth. The young parents spent time with their son before telling the news to their families and the world. The Queen's gynecologist Marcus Setchell, who led the team that delivered the baby, described the new arrival as 'wonderful baby, beautiful baby'. A bulletin signed by him was taken by a royal aide from St Mary's to the palace under police escort. The news has been since displayed on an easel in the forecourt of Buckingham Palace in line with tradition. A palace spokesman said the names of the baby would be announced in due course. A Buckingham Palace spokesman said: 'The Queen and Duke of Edinburgh are delighted at the news.'",
        "question": "Kate is one of two children.",
        "options": [
            "TRUE",
            "FALSE"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (T/F)",
        "passage": "1. Prince William is a member of the British royal family. He's the Queen's grandson and the eldest son of Charles and Diana. His brother's name is Harry. Diana, their mother, isn't alive now, but they have a stepmother, Camilla.\n\n2. William's wife is Kate Middleton. She's originally from an ordinary family but of course, she's now the Duchess of Cambridge and part of the royal family. Kate has a brother, James, and a sister, Pippa. Their parents, Michael and Carole, have an online business.\n\n3. In some ways, Kate and William are a normal couple. They have friends from university and they have hobbies and interests too. For example, William loves football and Kate likes photography. In the winter, they go skiing together.\n\n4. In other ways, their lives are very different from their friends' lives. William is the future King of the United Kingdom and fifteen other countries too, including Canada and Australia. Kate and William have a lot of official duties. They help charities in the UK and Africa, they visit other countries and they meet important visitors to the UK.\n\n5. The Duchess of Cambridge is expecting a baby, St James's Palace has confirmed. All the members of the royal family and the Duchess's family, the Middletons, are delighted: 'The Queen, the Duke of Edinburgh, the Prince of Wales, the Duchess of Cornwall and Prince Harry and members of both families are delighted with the news.'\n\nThe baby will be third in line to the throne, after Prince Charles and Prince William. A spokesman said the Duchess has been admitted to King Edward VII Hospital in central London with acute morning sickness and is expected to stay for several days: 'As the pregnancy is in its very early stages, her royal highness is expected to stay in hospital for several days and will require a period of rest thereafter.'\n\n6. Prince William, the Duke of Cambridge, says he and his wife 'could not be happier' after the Duchess gave birth to a baby boy, at 16:30, 22nd July 2013 UK time at St Mary's Hospital, west London. William was present at St Mary's for the birth. The young parents spent time with their son before telling the news to their families and the world. The Queen's gynecologist Marcus Setchell, who led the team that delivered the baby, described the new arrival as 'wonderful baby, beautiful baby'. A bulletin signed by him was taken by a royal aide from St Mary's to the palace under police escort. The news has been since displayed on an easel in the forecourt of Buckingham Palace in line with tradition. A palace spokesman said the names of the baby would be announced in due course. A Buckingham Palace spokesman said: 'The Queen and Duke of Edinburgh are delighted at the news.'",
        "question": "James is William's cousin.",
        "options": [
            "TRUE",
            "FALSE"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (T/F)",
        "passage": "1. Prince William is a member of the British royal family. He's the Queen's grandson and the eldest son of Charles and Diana. His brother's name is Harry. Diana, their mother, isn't alive now, but they have a stepmother, Camilla.\n\n2. William's wife is Kate Middleton. She's originally from an ordinary family but of course, she's now the Duchess of Cambridge and part of the royal family. Kate has a brother, James, and a sister, Pippa. Their parents, Michael and Carole, have an online business.\n\n3. In some ways, Kate and William are a normal couple. They have friends from university and they have hobbies and interests too. For example, William loves football and Kate likes photography. In the winter, they go skiing together.\n\n4. In other ways, their lives are very different from their friends' lives. William is the future King of the United Kingdom and fifteen other countries too, including Canada and Australia. Kate and William have a lot of official duties. They help charities in the UK and Africa, they visit other countries and they meet important visitors to the UK.\n\n5. The Duchess of Cambridge is expecting a baby, St James's Palace has confirmed. All the members of the royal family and the Duchess's family, the Middletons, are delighted: 'The Queen, the Duke of Edinburgh, the Prince of Wales, the Duchess of Cornwall and Prince Harry and members of both families are delighted with the news.'\n\nThe baby will be third in line to the throne, after Prince Charles and Prince William. A spokesman said the Duchess has been admitted to King Edward VII Hospital in central London with acute morning sickness and is expected to stay for several days: 'As the pregnancy is in its very early stages, her royal highness is expected to stay in hospital for several days and will require a period of rest thereafter.'\n\n6. Prince William, the Duke of Cambridge, says he and his wife 'could not be happier' after the Duchess gave birth to a baby boy, at 16:30, 22nd July 2013 UK time at St Mary's Hospital, west London. William was present at St Mary's for the birth. The young parents spent time with their son before telling the news to their families and the world. The Queen's gynecologist Marcus Setchell, who led the team that delivered the baby, described the new arrival as 'wonderful baby, beautiful baby'. A bulletin signed by him was taken by a royal aide from St Mary's to the palace under police escort. The news has been since displayed on an easel in the forecourt of Buckingham Palace in line with tradition. A palace spokesman said the names of the baby would be announced in due course. A Buckingham Palace spokesman said: 'The Queen and Duke of Edinburgh are delighted at the news.'",
        "question": "William is a football fan.",
        "options": [
            "TRUE",
            "FALSE"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (T/F)",
        "passage": "1. Prince William is a member of the British royal family. He's the Queen's grandson and the eldest son of Charles and Diana. His brother's name is Harry. Diana, their mother, isn't alive now, but they have a stepmother, Camilla.\n\n2. William's wife is Kate Middleton. She's originally from an ordinary family but of course, she's now the Duchess of Cambridge and part of the royal family. Kate has a brother, James, and a sister, Pippa. Their parents, Michael and Carole, have an online business.\n\n3. In some ways, Kate and William are a normal couple. They have friends from university and they have hobbies and interests too. For example, William loves football and Kate likes photography. In the winter, they go skiing together.\n\n4. In other ways, their lives are very different from their friends' lives. William is the future King of the United Kingdom and fifteen other countries too, including Canada and Australia. Kate and William have a lot of official duties. They help charities in the UK and Africa, they visit other countries and they meet important visitors to the UK.\n\n5. The Duchess of Cambridge is expecting a baby, St James's Palace has confirmed. All the members of the royal family and the Duchess's family, the Middletons, are delighted: 'The Queen, the Duke of Edinburgh, the Prince of Wales, the Duchess of Cornwall and Prince Harry and members of both families are delighted with the news.'\n\nThe baby will be third in line to the throne, after Prince Charles and Prince William. A spokesman said the Duchess has been admitted to King Edward VII Hospital in central London with acute morning sickness and is expected to stay for several days: 'As the pregnancy is in its very early stages, her royal highness is expected to stay in hospital for several days and will require a period of rest thereafter.'\n\n6. Prince William, the Duke of Cambridge, says he and his wife 'could not be happier' after the Duchess gave birth to a baby boy, at 16:30, 22nd July 2013 UK time at St Mary's Hospital, west London. William was present at St Mary's for the birth. The young parents spent time with their son before telling the news to their families and the world. The Queen's gynecologist Marcus Setchell, who led the team that delivered the baby, described the new arrival as 'wonderful baby, beautiful baby'. A bulletin signed by him was taken by a royal aide from St Mary's to the palace under police escort. The news has been since displayed on an easel in the forecourt of Buckingham Palace in line with tradition. A palace spokesman said the names of the baby would be announced in due course. A Buckingham Palace spokesman said: 'The Queen and Duke of Edinburgh are delighted at the news.'",
        "question": "The King or Queen of England is also the King or Queen of Australia.",
        "options": [
            "TRUE",
            "FALSE"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (T/F)",
        "passage": "1. Prince William is a member of the British royal family. He's the Queen's grandson and the eldest son of Charles and Diana. His brother's name is Harry. Diana, their mother, isn't alive now, but they have a stepmother, Camilla.\n\n2. William's wife is Kate Middleton. She's originally from an ordinary family but of course, she's now the Duchess of Cambridge and part of the royal family. Kate has a brother, James, and a sister, Pippa. Their parents, Michael and Carole, have an online business.\n\n3. In some ways, Kate and William are a normal couple. They have friends from university and they have hobbies and interests too. For example, William loves football and Kate likes photography. In the winter, they go skiing together.\n\n4. In other ways, their lives are very different from their friends' lives. William is the future King of the United Kingdom and fifteen other countries too, including Canada and Australia. Kate and William have a lot of official duties. They help charities in the UK and Africa, they visit other countries and they meet important visitors to the UK.\n\n5. The Duchess of Cambridge is expecting a baby, St James's Palace has confirmed. All the members of the royal family and the Duchess's family, the Middletons, are delighted: 'The Queen, the Duke of Edinburgh, the Prince of Wales, the Duchess of Cornwall and Prince Harry and members of both families are delighted with the news.'\n\nThe baby will be third in line to the throne, after Prince Charles and Prince William. A spokesman said the Duchess has been admitted to King Edward VII Hospital in central London with acute morning sickness and is expected to stay for several days: 'As the pregnancy is in its very early stages, her royal highness is expected to stay in hospital for several days and will require a period of rest thereafter.'\n\n6. Prince William, the Duke of Cambridge, says he and his wife 'could not be happier' after the Duchess gave birth to a baby boy, at 16:30, 22nd July 2013 UK time at St Mary's Hospital, west London. William was present at St Mary's for the birth. The young parents spent time with their son before telling the news to their families and the world. The Queen's gynecologist Marcus Setchell, who led the team that delivered the baby, described the new arrival as 'wonderful baby, beautiful baby'. A bulletin signed by him was taken by a royal aide from St Mary's to the palace under police escort. The news has been since displayed on an easel in the forecourt of Buckingham Palace in line with tradition. A palace spokesman said the names of the baby would be announced in due course. A Buckingham Palace spokesman said: 'The Queen and Duke of Edinburgh are delighted at the news.'",
        "question": "William and Kate's son will be first in line to the throne.",
        "options": [
            "TRUE",
            "FALSE"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (T/F)",
        "passage": "1. Prince William is a member of the British royal family. He's the Queen's grandson and the eldest son of Charles and Diana. His brother's name is Harry. Diana, their mother, isn't alive now, but they have a stepmother, Camilla.\n\n2. William's wife is Kate Middleton. She's originally from an ordinary family but of course, she's now the Duchess of Cambridge and part of the royal family. Kate has a brother, James, and a sister, Pippa. Their parents, Michael and Carole, have an online business.\n\n3. In some ways, Kate and William are a normal couple. They have friends from university and they have hobbies and interests too. For example, William loves football and Kate likes photography. In the winter, they go skiing together.\n\n4. In other ways, their lives are very different from their friends' lives. William is the future King of the United Kingdom and fifteen other countries too, including Canada and Australia. Kate and William have a lot of official duties. They help charities in the UK and Africa, they visit other countries and they meet important visitors to the UK.\n\n5. The Duchess of Cambridge is expecting a baby, St James's Palace has confirmed. All the members of the royal family and the Duchess's family, the Middletons, are delighted: 'The Queen, the Duke of Edinburgh, the Prince of Wales, the Duchess of Cornwall and Prince Harry and members of both families are delighted with the news.'\n\nThe baby will be third in line to the throne, after Prince Charles and Prince William. A spokesman said the Duchess has been admitted to King Edward VII Hospital in central London with acute morning sickness and is expected to stay for several days: 'As the pregnancy is in its very early stages, her royal highness is expected to stay in hospital for several days and will require a period of rest thereafter.'\n\n6. Prince William, the Duke of Cambridge, says he and his wife 'could not be happier' after the Duchess gave birth to a baby boy, at 16:30, 22nd July 2013 UK time at St Mary's Hospital, west London. William was present at St Mary's for the birth. The young parents spent time with their son before telling the news to their families and the world. The Queen's gynecologist Marcus Setchell, who led the team that delivered the baby, described the new arrival as 'wonderful baby, beautiful baby'. A bulletin signed by him was taken by a royal aide from St Mary's to the palace under police escort. The news has been since displayed on an easel in the forecourt of Buckingham Palace in line with tradition. A palace spokesman said the names of the baby would be announced in due course. A Buckingham Palace spokesman said: 'The Queen and Duke of Edinburgh are delighted at the news.'",
        "question": "Kate gave birth to a baby boy at 4:30pm, 22nd July 2013 UK time.",
        "options": [
            "TRUE",
            "FALSE"
        ],
        "answer": 0
    },
    {
        "category": "Đọc Hiểu (T/F)",
        "passage": "1. Prince William is a member of the British royal family. He's the Queen's grandson and the eldest son of Charles and Diana. His brother's name is Harry. Diana, their mother, isn't alive now, but they have a stepmother, Camilla.\n\n2. William's wife is Kate Middleton. She's originally from an ordinary family but of course, she's now the Duchess of Cambridge and part of the royal family. Kate has a brother, James, and a sister, Pippa. Their parents, Michael and Carole, have an online business.\n\n3. In some ways, Kate and William are a normal couple. They have friends from university and they have hobbies and interests too. For example, William loves football and Kate likes photography. In the winter, they go skiing together.\n\n4. In other ways, their lives are very different from their friends' lives. William is the future King of the United Kingdom and fifteen other countries too, including Canada and Australia. Kate and William have a lot of official duties. They help charities in the UK and Africa, they visit other countries and they meet important visitors to the UK.\n\n5. The Duchess of Cambridge is expecting a baby, St James's Palace has confirmed. All the members of the royal family and the Duchess's family, the Middletons, are delighted: 'The Queen, the Duke of Edinburgh, the Prince of Wales, the Duchess of Cornwall and Prince Harry and members of both families are delighted with the news.'\n\nThe baby will be third in line to the throne, after Prince Charles and Prince William. A spokesman said the Duchess has been admitted to King Edward VII Hospital in central London with acute morning sickness and is expected to stay for several days: 'As the pregnancy is in its very early stages, her royal highness is expected to stay in hospital for several days and will require a period of rest thereafter.'\n\n6. Prince William, the Duke of Cambridge, says he and his wife 'could not be happier' after the Duchess gave birth to a baby boy, at 16:30, 22nd July 2013 UK time at St Mary's Hospital, west London. William was present at St Mary's for the birth. The young parents spent time with their son before telling the news to their families and the world. The Queen's gynecologist Marcus Setchell, who led the team that delivered the baby, described the new arrival as 'wonderful baby, beautiful baby'. A bulletin signed by him was taken by a royal aide from St Mary's to the palace under police escort. The news has been since displayed on an easel in the forecourt of Buckingham Palace in line with tradition. A palace spokesman said the names of the baby would be announced in due course. A Buckingham Palace spokesman said: 'The Queen and Duke of Edinburgh are delighted at the news.'",
        "question": "William was absent from St Mary's for the birth.",
        "options": [
            "TRUE",
            "FALSE"
        ],
        "answer": 1
    },
    {
        "category": "Đọc Hiểu (T/F)",
        "passage": "1. Prince William is a member of the British royal family. He's the Queen's grandson and the eldest son of Charles and Diana. His brother's name is Harry. Diana, their mother, isn't alive now, but they have a stepmother, Camilla.\n\n2. William's wife is Kate Middleton. She's originally from an ordinary family but of course, she's now the Duchess of Cambridge and part of the royal family. Kate has a brother, James, and a sister, Pippa. Their parents, Michael and Carole, have an online business.\n\n3. In some ways, Kate and William are a normal couple. They have friends from university and they have hobbies and interests too. For example, William loves football and Kate likes photography. In the winter, they go skiing together.\n\n4. In other ways, their lives are very different from their friends' lives. William is the future King of the United Kingdom and fifteen other countries too, including Canada and Australia. Kate and William have a lot of official duties. They help charities in the UK and Africa, they visit other countries and they meet important visitors to the UK.\n\n5. The Duchess of Cambridge is expecting a baby, St James's Palace has confirmed. All the members of the royal family and the Duchess's family, the Middletons, are delighted: 'The Queen, the Duke of Edinburgh, the Prince of Wales, the Duchess of Cornwall and Prince Harry and members of both families are delighted with the news.'\n\nThe baby will be third in line to the throne, after Prince Charles and Prince William. A spokesman said the Duchess has been admitted to King Edward VII Hospital in central London with acute morning sickness and is expected to stay for several days: 'As the pregnancy is in its very early stages, her royal highness is expected to stay in hospital for several days and will require a period of rest thereafter.'\n\n6. Prince William, the Duke of Cambridge, says he and his wife 'could not be happier' after the Duchess gave birth to a baby boy, at 16:30, 22nd July 2013 UK time at St Mary's Hospital, west London. William was present at St Mary's for the birth. The young parents spent time with their son before telling the news to their families and the world. The Queen's gynecologist Marcus Setchell, who led the team that delivered the baby, described the new arrival as 'wonderful baby, beautiful baby'. A bulletin signed by him was taken by a royal aide from St Mary's to the palace under police escort. The news has been since displayed on an easel in the forecourt of Buckingham Palace in line with tradition. A palace spokesman said the names of the baby would be announced in due course. A Buckingham Palace spokesman said: 'The Queen and Duke of Edinburgh are delighted at the news.'",
        "question": "Few people in England knew about Kate giving birth to a baby boy.",
        "options": [
            "TRUE",
            "FALSE"
        ],
        "answer": 1
    }
]
# === THÊM MODULE LƯU/TẢI TIẾN TRÌNH TẠI ĐÂY ===
def save_progress():
    data = {
        "selected_category": st.session_state.selected_category,
        "current_idx": st.session_state.current_idx,
        "score": st.session_state.score,
        "user_answers": st.session_state.user_answers
    }
    try:
        with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f)
        st.sidebar.success("✅ Đã lưu tiến trình thành công!")
    except Exception as e:
        st.sidebar.error(f"Lỗi khi lưu: {e}")

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            st.session_state.selected_category = data.get("selected_category", "Tất cả")
            st.session_state.current_idx = data.get("current_idx", 0)
            st.session_state.score = data.get("score", 0)
            # Ép kiểu key của dictionary về int do json lưu key dưới dạng string
            st.session_state.user_answers = {int(k): v for k, v in data.get("user_answers", {}).items()}
            st.sidebar.success("✅ Đã khôi phục tiến trình cũ!")
        except Exception as e:
            st.sidebar.error(f"Lỗi khi tải: {e}")
    else:
        st.sidebar.warning("⚠️ Chưa có tiến trình nào được lưu.")
# ===============================================
# Danh sách các thể loại
categories = ["Tất cả"] + list(dict.fromkeys([q["category"] for q in QUIZ_DATA]))

# 1. KHỞI TẠO SESSION STATE (Bắt buộc phải nằm ở đây để sửa lỗi)
if "selected_category" not in st.session_state:
    st.session_state.selected_category = "Tất cả"
if "current_idx" not in st.session_state:
    st.session_state.current_idx = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}

# 2. GIAO DIỆN SIDEBAR
st.sidebar.title("⚙️ Cài đặt ôn tập")
selected_category = st.sidebar.selectbox("Chọn thể loại bài tập:", categories)

# 3. NÚT LƯU / TẢI TIẾN TRÌNH
st.sidebar.markdown("---")
st.sidebar.subheader("💾 Lưu / Tải Tiến Trình")
st.sidebar.write("Lưu lại câu đang làm dở để lần sau học tiếp.")
col1, col2 = st.sidebar.columns(2)
with col1:
    if st.button("Lưu Lại"):
        save_progress()
with col2:
    if st.button("Tải Lại"):
        load_progress()

# 4. RESET (Kiểm tra sự thay đổi)
if selected_category != st.session_state.selected_category:
    st.session_state.selected_category = selected_category
    st.session_state.current_idx = 0
    st.session_state.score = 0
    st.session_state.user_answers = {}
    st.rerun()
# ======================================================
# Filter
if st.session_state.selected_category == "Tất cả":
    current_quiz_data = QUIZ_DATA
else:
    current_quiz_data = [q for q in QUIZ_DATA if q["category"] == st.session_state.selected_category]

st.title("📚 Ôn Tập Tiếng Anh EHOU")
st.caption(f"Ngân hàng {len(QUIZ_DATA)} câu hỏi tổng hợp chuẩn nhất từ 13 tài liệu")

total_q = len(current_quiz_data)

if total_q == 0:
    st.warning("Không có câu hỏi nào trong chuyên mục này.")
elif st.session_state.current_idx < total_q:
    idx = st.session_state.current_idx
    q_data = current_quiz_data[idx]

    st.progress((idx) / total_q)
    st.markdown(f"**Câu {idx + 1} / {total_q}** | *Chuyên mục: {q_data['category']}*")

    if "passage" in q_data and q_data["passage"]:
        st.info(f"**Đoạn văn / Thông báo:**\n\n{q_data['passage']}")

    st.subheader(q_data["question"])

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

    if idx in st.session_state.user_answers:
        if st.button("Câu tiếp theo ➡️"):
            if st.session_state.user_answers[idx] == q_data["answer"]:
                st.session_state.score += 1
            st.session_state.current_idx += 1
            st.rerun()
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
