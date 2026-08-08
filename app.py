import streamlit as st

# Cấu hình trang
st.set_page_config(
    page_title="Ôn Tập Tiếng Anh EHOU",
    page_direction="ltr",
    page_icon="📚",
    layout="centered"
)

# Ngân hàng 76 câu hỏi đầy đủ từ 13 file PDF
QUIZ_DATA = [
    # --- TIỀN TỐ ---
    {"category": "Từ Vựng - Tiền Tố", "question": "Choose the correct prefix for 'formal':", "options": ["un-", "in-", "dis-", "im-"], "answer": 1},
    {"category": "Từ Vựng - Tiền Tố", "question": "Choose the correct prefix for 'satisfied':", "options": ["un-", "in-", "dis-", "im-"], "answer": 2},
    {"category": "Từ Vựng - Tiền Tố", "question": "Choose the correct prefix for 'honest':", "options": ["un-", "in-", "dis-", "im-"], "answer": 2},
    {"category": "Từ Vựng - Tiền Tố", "question": "Choose the correct prefix for 'polite':", "options": ["un-", "in-", "dis-", "im-"], "answer": 3},
    {"category": "Từ Vựng - Tiền Tố", "question": "Choose the correct prefix for 'practical':", "options": ["un-", "in-", "dis-", "im-"], "answer": 3},
    {"category": "Từ Vựng - Tiền Tố", "question": "Choose the correct prefix for 'considerate':", "options": ["un-", "in-", "dis-", "im-"], "answer": 1},
    {"category": "Từ Vựng - Tiền Tố", "question": "Choose the correct prefix for 'friendly':", "options": ["un-", "in-", "dis-", "im-"], "answer": 0},
    {"category": "Từ Vựng - Tiền Tố", "question": "Choose the correct prefix for 'efficient':", "options": ["un-", "in-", "dis-", "im-"], "answer": 1},
    {"category": "Từ Vựng - Tiền Tố", "question": "Choose the correct prefix for 'important':", "options": ["un-", "in-", "dis-", "im-"], "answer": 0},
    {"category": "Từ Vựng - Tiền Tố", "question": "Choose the correct prefix for 'respectful':", "options": ["un-", "in-", "dis-", "im-"], "answer": 2},
    {"category": "Từ Vựng - Tiền Tố", "question": "Choose the correct prefix for 'patient':", "options": ["un-", "in-", "dis-", "im-"], "answer": 3},
    {"category": "Từ Vựng - Tiền Tố", "question": "Choose the correct prefix for 'appropriate':", "options": ["un-", "in-", "dis-", "im-"], "answer": 1},

    # --- TỪ LOẠI ---
    {"category": "Ngữ Pháp - Từ Loại", "question": "He took up that sport for its _______", "options": ["Popular", "Unpopular", "Popularize", "Popularity"], "answer": 3},
    {"category": "Ngữ Pháp - Từ Loại", "question": "The _______ system in this country is rather complex.", "options": ["Education", "Educated", "Educating", "Educate"], "answer": 0},
    {"category": "Ngữ Pháp - Từ Loại", "question": "A _______ diet is one that helps maintain general health.", "options": ["Health", "Unhealthy", "Healthy", "Healthily"], "answer": 2},
    {"category": "Ngữ Pháp - Từ Loại", "question": "_______ is necessary after hard work.", "options": ["Relaxed", "Relaxing", "Relaxation", "Relax"], "answer": 2},
    {"category": "Ngữ Pháp - Từ Loại", "question": "He _______ in at the university.", "options": ["Specialty", "Specializes", "Special", "Specially"], "answer": 1},
    {"category": "Ngữ Pháp - Từ Loại", "question": "NUS is the _______ university of Singapore.", "options": ["Nation", "Nationality", "National", "Nationally"], "answer": 2},
    {"category": "Ngữ Pháp - Từ Loại", "question": "He has a big stamp _______", "options": ["Collection", "Collector", "Collect", "Collective"], "answer": 0},
    {"category": "Ngữ Pháp - Từ Loại", "question": "The patient comes to the hospital in the _______ that he will be cured.", "options": ["Believe", "Belief", "Unbelievable", "Believable"], "answer": 1},

    # --- BIỂN BÁO & THÔNG BÁO ---
    {"category": "Biển Báo & Thông Báo", "passage": "JUNGLE CAFÉ\nSORRY!\nTables at the front of the café are reserved for a birthday party.", "question": "What does it say?", "options": ["Don't sit at the front of the café unless you're attending the party.", "If you're coming to the party you shouldn't use the tables at the front.", "The café says 'sorry' because of closing today.", "Only people invited to the party can come into the café."], "answer": 0},
    {"category": "Biển Báo & Thông Báo", "passage": "STUDENTS!\nYOUR $6 DEPOSIT FOR LOCKER KEYS WON'T BE REFUNDED IF KEYS ARE LOST.", "question": "What does it say?", "options": ["Lost locker keys can be replaced for a charge of $6", "We cannot return your $6 deposit if you lose your locker key.", "You will receive $6 if your locker key is lost", "You cannot collect your locker key until you have paid a $6 deposit."], "answer": 1},
    {"category": "Biển Báo & Thông Báo", "passage": "Becky,\nDon't forget your Aunt Jane's coming to stay tonight, so can you make sure the house is neat when you go out this afternoon?\nMum", "question": "Why is mum writing this note?", "options": ["To ask Becky to tidy the house before she leaves", "To remind Becky to go to her aunt's house", "To tell Becky to go out with her aunt Jane", "To tell Becky to stay at home to see aunt"], "answer": 0},
    {"category": "Biển Báo & Thông Báo", "passage": "Frank, Rabbit Records phoned. The CD you ordered arrived today, but someone sold it. They're really sorry! They've reordered available next Monday at the latest.", "question": "Why did the record shop phone?", "options": ["To apologise for a mistake with Frank's order.", "To say that Frank's CD is ready for collection.", "The earliest Frank can get his CD is next Monday.", "To suggest Frank comes in later this week."], "answer": 0},
    {"category": "Biển Báo & Thông Báo", "passage": "Market vehicles unload here 07.00-10.00 daily\nCustomer parking allowed at other times.", "question": "What does it say?", "options": ["Customers may park here at times when vehicles are not unloading.", "Customers are allowed to park here from 07.00-10.00.", "You may unload your vehicle here at any time.", "Customers may park outside the market for up to three hours."], "answer": 0},
    {"category": "Biển Báo & Thông Báo", "passage": "What a fantastic city. We found the restaurant you recommended but it was shut! Menu looks good value, so we'll definitely go before we leave.", "question": "What does it say?", "options": ["Elena and Tim think the restaurant's prices are reasonable.", "Elena and Tim have already tried the restaurant.", "Elena and Tim have discovered another good restaurant.", "Elena and Tim will have to try the restaurant on their next visit."], "answer": 0},
    {"category": "Biển Báo & Thông Báo", "passage": "To: Sally | From: Kim\nFeeling any better? When you're back at college, remember to register for the films course. Email me if you want any information.", "question": "Why has Kim emailed Sally?", "options": ["To remind her to do something.", "To borrow a film from her.", "To give her some details.", "To let her know that he's ill."], "answer": 0},
    {"category": "Biển Báo & Thông Báo", "passage": "Mustafa, your brother phones. He's emailed you something to read before you write that letter to the hotel. I said you'd call his mobile number today.\nJean", "question": "How should Mustafa reply to his brother?", "options": ["By phone", "By email", "By meeting", "By letter"], "answer": 0},
    {"category": "Biển Báo & Thông Báo", "passage": "HOSPITAL WAITING ROOM\nPLEASE PUT ALL CHILDREN'S TOYS BACK IN THIS ROOM BEFORE YOU LEAVE.", "question": "What does it say?", "options": ["Please don't leave any toys outside this room when you go.", "Don't forget to pay for the toys before you leave.", "Remember to take your children's toys with you when you leave.", "We leave some toys at the back of this room for children."], "answer": 0},
    {"category": "Biển Báo & Thông Báo", "passage": "Do not use this medicine for more than seven days without your doctor's advice.", "question": "What does it say?", "options": ["Contact your doctor if you wish to continue using this medicine after one week.", "You cannot keep this medicine for more than seven days.", "Doctors can only supply enough medicine for one week at a time.", "You can use this medicine for more than a week."], "answer": 0},
    {"category": "Biển Báo & Thông Báo", "passage": "SPORTS HALL\nFinal five minutes of bookings must be used to put equipment away.", "question": "What does it say?", "options": ["All the equipments must be put away after booking time (in the final 5 mins).", "You have five minutes after bookings have finished to return any sports equipment used.", "Bookings now include an extra five minutes for equipment to be put away.", "The hall must be cleared of equipment in the five minutes after bookings end."], "answer": 0},
    {"category": "Biển Báo & Thông Báo", "passage": "NO DIVING ALLOWED EXCEPT AT THE DEEP END OF THE SWIMMING POOL", "question": "What does it say?", "options": ["You must not dive into the pool where the water is shallow.", "The water is not deep enough in this poor for you to dive.", "Swimming is not permitted where people are diving.", "The swimming pool is too deep to swim."], "answer": 0},
    {"category": "Biển Báo & Thông Báo", "passage": "Patients with appointments ring once and enter. Those with enquiries ring twice and enter.", "question": "What does it say?", "options": ["Ring once if you have an appointment and twice if you don't.", "You should ring twice and enter unless you have an enquiry.", "If you have an appointment, you don't have to ring.", "To make an appointment, ring once and enter."], "answer": 0},
    {"category": "Biển Báo & Thông Báo", "passage": "CYCLISTS\nWhen this entrance is locked use side gate.", "question": "What does it say?", "options": ["Cyclists should use a different entrance when this one is locked.", "The only entrance is the side gate.", "If the side gate is locked, go through cycle entrance.", "Lock your cycle near this gate before entering."], "answer": 0},
    {"category": "Biển Báo & Thông Báo", "passage": "Please don't park within 3 metres of this vehicle - space needed for unloading.", "question": "What does it say?", "options": ["You are requested not to park any closer than 3 metres to this vehicle.", "This parking space is reserved for the vehicle's owner.", "If you want to load things, park beyond 3 metres.", "You should not park near here because it is an exit for vehicles."], "answer": 0},
    {"category": "Biển Báo & Thông Báo", "passage": "$25 RESERVES ANY PICTURES IN THE GALLERY", "question": "What does it say?", "options": ["We will keep any picture for you if you give us $25.", "It costs $25 to show your picture in the gallery.", "Some of the pictures in the gallery are reserved.", "A picture in the gallery costs $25."], "answer": 0},
    {"category": "Biển Báo & Thông Báo", "passage": "ROOM TO RENT\nUNEXPECTEDLY AVAILABLE so only $250 per month including fuel bills", "question": "What does it say?", "options": ["This rent includes all bills.", "The rent for this room is reduced to $250 plus bills.", "People renting this room should expect to pay extra for gas and electricity.", "This room is cheap to rent as it was not expected to be empty."], "answer": 0},
    {"category": "Biển Báo & Thông Báo", "passage": "WANTED: KITCHEN ASSISTANTS\nEvening or weekends. Free meals. Full training provided. Apply inside", "question": "What does it say?", "options": ["There are part-time opportunities for people without experience of working in a kitchen.", "Only people who are trained in kitchen work should apply for these part-time jobs.", "The kitchen assistant will be offered three free meals a day.", "We offer cheap meals to people who work part-time in our kitchen."], "answer": 0},
    {"category": "Biển Báo & Thông Báo", "passage": "BASKETBALL TRAINING\nProfessional coach available for pre-booked groups - 48 hours' notice required.", "question": "What does it say?", "options": ["A basketball coach is available if a booking is made far enough in advance.", "Those who want to attend the training group must book in 4 days.", "Basketball players are only allowed to practice here if accompanied by a professional coach.", "Basketball training for groups is cancelled until further notice."], "answer": 0},
    {"category": "Biển Báo & Thông Báo", "passage": "This medicine is taken between meals at six-hourly intervals, up to three times daily.", "question": "What does it say?", "options": ["It is essential to wait six hours before having more of this medicine.", "It is essential to take this medicine before each meal.", "It is essential to take this medicine straight after meals.", "It is essential to use this medicine more than three times a day."], "answer": 0},
    {"category": "Biển Báo & Thông Báo", "passage": "From: Roberto | To: Sam\nSorry I missed you yesterday. I'm not in all next week, but the following Thursday's fine. Why not see if Sven's free as well?", "question": "What does it say?", "options": ["Roberto is suggesting that Sam should invite Sven to their next meeting.", "Roberto is suggesting that He will join Sam in a meeting next Thursday.", "Roberto will be free the whole next week.", "Roberto is suggesting that Sven is unavailable for a meeting next week."], "answer": 0},
    {"category": "Biển Báo & Thông Báo", "passage": "Once opened, remove any unused soup from the tin and place in the refrigerator.", "question": "What does it say?", "options": ["This label gives advice on how to store the product.", "This label gives information on the ingredients of the product.", "This label gives advice on how to use the product.", "This label gives advice on how to open the product."], "answer": 0},

    # --- ĐỌC HIỂU T/F ---
    {"category": "Đọc Hiểu (T/F)", "passage": "We're Living Faster, But Are We Living Better?", "question": "The writer wrote the article to encourage us to work more and relax less.", "options": ["TRUE", "FALSE"], "answer": 1},
    {"category": "Đọc Hiểu (T/F)", "passage": "We're Living Faster, But Are We Living Better?", "question": "People today are having a less stressful life than they did in the past.", "options": ["TRUE", "FALSE"], "answer": 1},
    {"category": "Đọc Hiểu (T/F)", "passage": "We're Living Faster, But Are We Living Better?", "question": "People are too busy to read newspapers.", "options": ["TRUE", "FALSE"], "answer": 0},
    {"category": "Đọc Hiểu (T/F)", "passage": "We're Living Faster, But Are We Living Better?", "question": "Slow sports have become unpopular.", "options": ["TRUE", "FALSE"], "answer": 0},
    {"category": "Đọc Hiểu (T/F)", "passage": "We're Living Faster, But Are We Living Better?", "question": "More time is spent on stories.", "options": ["TRUE", "FALSE"], "answer": 1},

    {"category": "Đọc Hiểu (T/F)", "passage": "The Royal Family", "question": "Camilla is William's mother.", "options": ["TRUE", "FALSE"], "answer": 1},
    {"category": "Đọc Hiểu (T/F)", "passage": "The Royal Family", "question": "William's wife is the Duchess of Cambridge.", "options": ["TRUE", "FALSE"], "answer": 0},
    {"category": "Đọc Hiểu (T/F)", "passage": "The Royal Family", "question": "Kate is one of two children.", "options": ["TRUE", "FALSE"], "answer": 1},
    {"category": "Đọc Hiểu (T/F)", "passage": "The Royal Family", "question": "James is William's cousin.", "options": ["TRUE", "FALSE"], "answer": 1},
    {"category": "Đọc Hiểu (T/F)", "passage": "The Royal Family", "question": "William is a football fan.", "options": ["TRUE", "FALSE"], "answer": 0},
    {"category": "Đọc Hiểu (T/F)", "passage": "The Royal Family", "question": "The King or Queen of England is also the King or Queen of Australia.", "options": ["TRUE", "FALSE"], "answer": 0},
    {"category": "Đọc Hiểu (T/F)", "passage": "The Royal Family", "question": "William and Kate's son will be first in line to the throne.", "options": ["TRUE", "FALSE"], "answer": 1},
    {"category": "Đọc Hiểu (T/F)", "passage": "The Royal Family", "question": "Kate gave birth to a baby boy at 4:30pm, 22nd July 2013 UK time.", "options": ["TRUE", "FALSE"], "answer": 0},
    {"category": "Đọc Hiểu (T/F)", "passage": "The Royal Family", "question": "William was absent from St Mary's for the birth.", "options": ["TRUE", "FALSE"], "answer": 1},
    {"category": "Đọc Hiểu (T/F)", "passage": "The Royal Family", "question": "Few people in England knew about Kate giving birth to a baby boy.", "options": ["TRUE", "FALSE"], "answer": 1},

    # --- ĐỌC HIỂU MULTIPLE CHOICE ---
    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "Two years ago, our 14-year-old son, Ben, asked us for a set of drums for his birthday. At first, we were very much against the idea because of the noise...", "question": "Ben asked his parents for a drum when he was:", "options": ["14 years old", "12 years old", "2 years old", "16 years old"], "answer": 0},
    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "Two years ago, our 14-year-old son, Ben, asked us for a set of drums for his birthday. At first, we were very much against the idea because of the noise...", "question": "His parents disagreed at first because:", "options": ["it was expensive", "it was noisy", "they prefer computer", "it was dangerous"], "answer": 1},
    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "Because drums are not the easiest instruments to transport, the other members of Ben's band started appearing at our home with their guitars...", "question": "Ben started playing music with:", "options": ["his friends/band members", "himself", "his neighbors", "his parents"], "answer": 0},
    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "Because drums are not the easiest instruments to transport, the other members of Ben's band started appearing at our home with their guitars...", "question": "They play / practice at:", "options": ["outside", "at Ben's house", "at Ben's friends' house", "at the park"], "answer": 1},
    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "At least Ben's hobby has been good for our health: whenever the band start practicing, my husband and I go out for a long walk.", "question": "When the band starts practicing, Ben's parents:", "options": ["go for a long walk", "go to sleep", "go shopping", "stay and listen"], "answer": 0},
    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "And I must admit that, although their music may sound a little strange, they are a friendly and polite group of young men.", "question": "Ben's parents think his friends are:", "options": ["rude", "stubborn", "well-behaved (friendly and polite)", "annoying"], "answer": 2},
    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "Our main worry is that they won't spend enough time on their school work because of their musical activities...", "question": "The writer is worried because:", "options": ["the children may quit school", "the children won't spend enough time on school work", "the children are bored", "they make too much noise"], "answer": 1},
    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "But one thing is certain Ben was right: it has kept him out of trouble and he is never bored.", "question": "The writer thinks that:", "options": ["Ben should not have joined the band", "Ben's decision to play music has kept him out of trouble", "Ben should study more", "Ben should sell the drums"], "answer": 1},

    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "David Johnson has loved swimming all his life. When he was 27, he swam in a race near his home in the USA. The sea was very cold and David started to feel unwell. He was taken to hospital...", "question": "When did David have problems?", "options": ["When driving", "During a swimming competition in the USA", "When sailing", "During his holiday"], "answer": 1},
    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "In January 2004, at the age of 52, David crossed New Zealand's Cook Strait in 9 hours and 38 minutes.", "question": "How old was David in January 2004 when he crossed Cook Strait?", "options": ["52", "48", "27", "38"], "answer": 0},
    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "David spent over a year getting ready to swim the Strait.", "question": "How much time did David spend getting ready to swim the Strait?", "options": ["Half a year", "A few weeks", "Two years", "More than 12 months (over a year)"], "answer": 3},
    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "He did it with the help of a team. 'They were great', David said. 'They were in a boat next to me all the time!'", "question": "How much time were the team with David during his swim?", "options": ["For few weeks", "For one day", "All the time", "For few hours"], "answer": 2},
    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "David Johnson has loved swimming all his life.", "question": "What has David always enjoyed doing?", "options": ["Sailing", "Swimming", "Walking", "Diving"], "answer": 1},

    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "Orbis is an organization which helps blind people everywhere. It has built an eye hospital inside an aeroplane and flown it all over the world... Samantha tells the story of Eukhtuul...", "question": "What is the writer's main purpose in writing this text?", "options": ["To describe a dangerous trip.", "To report a patient's cure.", "To explain how sight can be lost.", "To warn against playing with sticks."], "answer": 1},
    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "Orbis is an organization which helps blind people everywhere. It has built an eye hospital inside an aeroplane and flown it all over the world...", "question": "What can a reader learn about in this text?", "options": ["The life of schoolchildren in Mongolia.", "The difficulties for blind travelers.", "The international work of some eye doctors.", "The best way of studying medicine."], "answer": 2},
    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "I thought about all the everyday things I do that she couldn't... and I realized how lucky I am.", "question": "After meeting Eukhtuul, Samantha felt:", "options": ["Grateful for her own sight.", "Proud of the doctor's skill.", "Surprised by Eukhtuul's courage.", "Angry about Eukhtuul's experience."], "answer": 0},
    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "'In six months your sight will be back to normal', he said.", "question": "What is the result of Eukhtuul's operation?", "options": ["She can already see perfectly again.", "After some time she will see as well as before.", "She can see better but will never have normal eyes.", "Before she recovers, she will need another operation."], "answer": 1},
    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "We should all think more about how much our sight means to us.", "question": "Which postcard did Samantha write to an English friend?", "options": ["I've visited a Mongolian hospital...", "You may have to fly a long way...", "I'm staying with my friend Eukhtuul...", "Make sure you take care of your eyes because they're more valuable than you realize!"], "answer": 3},

    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "When the spring semester began, students at Eastern High School were met by a new science teacher. Her name is Elaine Burgess... She was kind enough to sit down for an interview with The Quill and Paper.", "question": "Which headline best summarizes the article?", "options": ["Science Classes to Features Hands-on Learning", "A Chat with the New Science Teacher", "The Education of Elaine Burgess", "Science Class: Does Anyone Enjoy it?"], "answer": 1},
    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "She was kind enough to sit down for an interview with The Quill and Paper.", "question": "Based on the article, what is The Quill and Paper?", "options": ["It is read by every student.", "It is a new textbook.", "It was written by Ms. Burgess.", "It is the name of a newspaper."], "answer": 3},
    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "Her M.A. is in chemistry, but she double majored in chemistry and biology as an undergraduate while simultaneously getting a minor in physics.", "question": "Which statement does paragraph 2 support?", "options": ["This is the second teaching job for Ms. Burgess.", "Ms. Burgess has been a teacher for six months.", "Ms. Burgess was a professor at Sanderson University.", "Ms. Burgess focused on science as an undergraduate."], "answer": 3},
    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "So she expects to conduct numerous experiments in the hope of sparking students' interest in science.", "question": "What does the author point out regarding Ms. Burgess's hope of sparking students' interest?", "options": ["Too many students have little scientific knowledge.", "She wants students to be curious about science.", "Science is one of the hardest subjects to learn.", "Some experiments can be dangerous for students to do."], "answer": 1},
    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "Finally, Ms. Burgess added that she welcomes student participation in her classes. 'Not only can students learn from their teachers, but I believe that teachers can also learn from their students.'", "question": "What can be inferred about Ms. Burgess?", "options": ["Some of her students know more about science than her.", "Her grades in graduate school were high.", "She expects her students to speak in class.", "The subject she knows the least is biology."], "answer": 2},

    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "He explained that many people are like garbage trucks. They run around full of garbage, full of frustration, full of anger, and full of disappointment... The bottom line is that successful people do not let garbage trucks take over their day.", "question": "Which title best expresses the main idea of the story?", "options": ["A weird taxi driver", "The law of the garbage truck", "A trip to the airport", "Waving to people friendly"], "answer": 1},
    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "One day I hopped in a taxi and we took off for the airport.", "question": "The word hopped is closest in meaning to:", "options": ["Jumped", "Flied", "Walked", "Lingered"], "answer": 0},
    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "They run around full of garbage, full of frustration, full of anger, and full of disappointment.", "question": "According to the author, what is NOT in the garbage truck?", "options": ["Happiness", "Anger", "Frustration", "Disappointment"], "answer": 0},
    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "Life's too short to wake up in the morning with regrets, so 'love the people who treat you right. Pray for the ones who don't'.", "question": "What does the author suggest by telling the story?", "options": ["We shouldn't take a taxi to the airport", "It is not right to whip one's head around and yell at others", "We should not pile up too much garbage in our truck", "We should love the people who treat us right and pray for the ones who don't"], "answer": 3},

    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "The dogsled race was about to begin. Julie's team of dogs was lined up at the starting gate... Hour after hour, day after day, Julie's dogs pulled the sled in order to get in shape for the race.", "question": "The author wrote the story in order to:", "options": ["Describe how dogs stay warm in cold weather", "Tell a story about a dogsled race", "Explain how cold it can be in winter", "Entertain the reader with funny stories about dogs"], "answer": 1},
    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "The racers had to go a thousand miles across Alaska. Alaska is one of the coldest places on Earth.", "question": "Where does the dogsled race take place?", "options": ["In Antarctica", "On a track", "In Alaska", "In a field"], "answer": 2},
    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "Pieces of ice were as sharp as a knife. The ice could cut the dogs' feet. To keep that from happening, Julie had put special booties on their feet.", "question": "Why did the dogs wear special booties?", "options": ["To be well recognized", "Because the booties fit their feet", "To protect their feet from ice", "To keep their feet warm"], "answer": 2},
    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "The dogs' thick fur coats helped keep them warm in the cold wind and weather.", "question": "Why don't the dogs freeze in the cold weather?", "options": ["Julie puts special booties on their feet.", "They sleep by the fire at night.", "Their thick fur coats keep them warm.", "It doesn't get very cold in Alaska."], "answer": 2},
    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "Once, one of the sled's runners slid into a hole and broke. Julie could have given up then, but she didn't. She fixed it and they kept going.", "question": "What kind of person is Julie?", "options": ["Brave and determined", "Timid and hesitant", "Interesting and careful", "Boring and careless"], "answer": 0},

    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "All students who are not yet eighteen years of age must submit a permission slip signed by a parent or guardian... All students must also provide proof that they have medical insurance...", "question": "What is the purpose of the notice?", "options": ["To inform the students about an upcoming field trip", "To let the students know about some forms they must submit", "To advise students on some punishments they may receive", "To ask for the students' opinions on where to take field trips"], "answer": 1},
    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "This permission slip indicates that the parent or guardian consents to allowing the students to go on the field trip.", "question": "The word consents is closest in meaning to:", "options": ["Responds", "Agrees", "Stresses", "Obtains"], "answer": 1},
    {"category": "Đọc Hiểu (Multiple Choice)", "passage": "Failure to do so will result in some sort of punishment, such as detention or suspension.", "question": "What will happen to students who misbehave while on field trips?", "options": ["They will not be allowed to go on future trips", "They will be punished in some way", "They will have to apologize to the teacher", "They will be forced to pay a fine"], "answer": 1}
]

# Quản lý Trạng thái ứng dụng (Session State)
if "current_idx" not in st.session_state:
    st.session_state.current_idx = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}

st.title("📚 Ôn Tập Tiếng Anh EHOU")
st.caption("Ngân hàng 76 câu hỏi tổng hợp chuẩn xác từ 13 tệp LTTN & KTTN")

total_q = len(QUIZ_DATA)

# Màn hình làm bài
if st.session_state.current_idx < total_q:
    idx = st.session_state.current_idx
    q_data = QUIZ_DATA[idx]

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
    st.header("🏁 Bạn đã hoàn thành bài ôn tập!")
    
    final_score = st.session_state.score
    accuracy = round((final_score / total_q) * 100, 1)
    
    st.metric(label="Tổng số câu đúng", value=f"{final_score} / {total_q}", delta=f"{accuracy}%")
    
    if st.button("🔄 Thi lại từ đầu"):
        st.session_state.current_idx = 0
        st.session_state.score = 0
        st.session_state.user_answers = {}
        st.rerun()
