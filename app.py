import streamlit as st
import json
import os

st.set_page_config(page_title="Ôn Tập Tiếng Anh EHOU", page_icon="📚", layout="centered")

PROGRESS_FILE = "progress.json"

# ==========================================
# 1. CÁC HÀM XỬ LÝ (DỊCH, LƯU TỪ, TIẾN TRÌNH)
# ==========================================

# --- HÀM DỊCH AN TOÀN ---
def safe_translate(text):
    if not text or not str(text).strip():
        return ""
    from deep_translator import GoogleTranslator, MyMemoryTranslator
    # Lọc bỏ các dấu gạch dưới điền từ để tránh lỗi máy dịch
    clean_text = str(text).replace("__", "...").replace("_(1)_", "(1)").replace("_(2)_", "(2)").replace("_(3)_", "(3)").replace("_(4)_", "(4)").replace("_(5)_", "(5)")
    
    # 1. Thử dịch qua Google Translator
    try:
        return GoogleTranslator(source='en', target='vi').translate(clean_text)
    except Exception:
        pass
        
    # 2. Dự phòng bằng MyMemory Translator nếu Google bận/lỗi
    try:
        return MyMemoryTranslator(source='en-US', target='vi-VN').translate(clean_text)
    except Exception as e:
        return f"(Chưa dịch được: {e})"

# --- HÀM QUẢN LÝ TỪ VỰNG ---
if "saved_words" not in st.session_state:
    st.session_state.saved_words = []

def add_saved_word(word, meaning="", note=""):
    word_clean = word.strip()
    if word_clean:
        if not any(w["word"].lower() == word_clean.lower() for w in st.session_state.saved_words):
            st.session_state.saved_words.append({
                "word": word_clean,
                "meaning": meaning.strip(),
                "note": note
            })
            return True
    return False

def remove_saved_word(word_to_remove):
    st.session_state.saved_words = [
        w for w in st.session_state.saved_words if w["word"].lower() != word_to_remove.lower()
    ]

# --- HÀM LƯU / TẢI TIẾN TRÌNH ---
def save_progress():
    data = {
        "selected_category": st.session_state.selected_category,
        "current_idx": st.session_state.current_idx,
        "score": st.session_state.score,
        "user_answers": st.session_state.user_answers,
        "saved_words": st.session_state.saved_words
    }
    try:
        with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f)
        st.sidebar.success("✅ Đã lưu tiến trình & sổ từ vựng!")
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
            st.session_state.user_answers = {int(k): v for k, v in data.get("user_answers", {}).items()}
            st.session_state.saved_words = data.get("saved_words", [])
            st.sidebar.success("✅ Đã khôi phục tiến trình cũ!")
        except Exception as e:
            st.sidebar.error(f"Lỗi khi tải: {e}")
    else:
        st.sidebar.warning("⚠️ Chưa có tiến trình nào được lưu.")


# ==========================================
# 2. KHỞI TẠO DỮ LIỆU BÀI HỌC (303 CÂU)
# ==========================================
quiz_data = []

# --- 1. PREFIXES ---
prefixes = [("formal", 1), ("satisfied", 2), ("honest", 2), ("polite", 3), ("practical", 3), ("considerate", 1), ("friendly", 0), ("efficient", 1), ("important", 0), ("respectful", 2), ("patient", 3), ("appropriate", 1)]
for word, ans in prefixes:
    expl = "📌 **Ngữ pháp:** Sử dụng tiền tố mang nghĩa phủ định. "
    if word in ["polite", "practical", "patient"]: expl += f"Với các tính từ bắt đầu bằng 'p' hoặc 'm', ta thường dùng tiền tố **'im-'** (VD: {word} -> im{word})."
    elif word in ["satisfied", "honest", "respectful"]: expl += f"Trường hợp này ta dùng tiền tố **'dis-'** (VD: {word} -> dis{word})."
    elif word in ["formal", "considerate", "efficient", "appropriate"]: expl += f"Trường hợp này ta dùng tiền tố **'in-'** (VD: {word} -> in{word})."
    elif word in ["friendly", "important"]: expl += f"Trường hợp này ta dùng tiền tố **'un-'** (VD: {word} -> un{word})."
    quiz_data.append({"category": "Từ Vựng - Tiền Tố", "question": f"Choose the correct prefix for '{word}':", "options": ["un-", "in-", "dis-", "im-"], "answer": ans, "explanation": expl})

# --- 2. WORD FORMS ---
wf_data = [
    ("He took up that sport for its _______", ["Popular", "Unpopular", "Popularize", "Popularity"], 3, "📌 **Ngữ pháp:** Sau tính từ sở hữu 'its' cần một **Danh từ**. 'Popularity' (sự phổ biến) là danh từ."),
    ("The _______ system in this country is rather complex.", ["Education", "Educated", "Educating", "Educate"], 0, "📌 **Ngữ pháp:** Trước danh từ 'system' cần một Danh từ hoặc Tính từ để tạo thành cụm danh từ ghép. 'Education system' = hệ thống giáo dục."),
    ("A _______ diet is one that helps maintain general health.", ["Health", "Unhealthy", "Healthy", "Healthily"], 2, "📌 **Ngữ pháp:** Sau mạo từ 'A' và trước danh từ 'diet' cần một **Tính từ**. Bối cảnh câu mang nghĩa tích cực nên chọn 'Healthy'."),
    ("_______ is necessary after hard work.", ["Relaxed", "Relaxing", "Relaxation", "Relax"], 2, "📌 **Ngữ pháp:** Vị trí đầu câu làm Chủ ngữ, cần một **Danh từ**. 'Relaxation' (sự thư giãn) là danh từ."),
    ("He _______ in at the university.", ["Specialty", "Specializes", "Special", "Specially"], 1, "📌 **Ngữ pháp:** Câu thiếu **Động từ** chính. Chủ ngữ 'He' ngôi thứ 3 số ít nên động từ chia s/es -> 'Specializes' (chuyên về)."),
    ("NUS is the _______ university of Singapore.", ["Nation", "Nationality", "National", "Nationally"], 2, "📌 **Ngữ pháp:** Giữa mạo từ 'the' và danh từ 'university' cần một **Tính từ**. 'National' (thuộc về quốc gia)."),
    ("He has a big stamp _______", ["Collection", "Collector", "Collect", "Collective"], 0, "📌 **Ngữ pháp:** Sau tính từ 'big' và danh từ bổ nghĩa 'stamp' cần một **Danh từ chính**. Cụm 'Stamp collection' (bộ sưu tập tem)."),
    ("The patient comes to the hospital in the _______ that he will be cured.", ["Believe", "Belief", "Unbelievable", "Believable"], 1, "📌 **Ngữ pháp:** Sau mạo từ 'the' cần một **Danh từ**. 'Belief' (niềm tin).")
]
for q, opts, ans, expl in wf_data:
    quiz_data.append({"category": "Ngữ Pháp - Từ Loại", "question": q, "options": opts, "answer": ans, "explanation": expl})

# --- 3. MATCHING ---
match_data = [
    ("What is the meaning of the expression 'waste time'?", ["use time badly", "last too long", "use more time", "punctual"], 0),
    ("What is the meaning of 'take a long time'?", ["last too long", "use time badly", "use more time", "don't have the time you need"], 0),
    ("What is the meaning of 'spend more time'?", ["use more time", "punctual", "last too long", "use time badly"], 0),
    ("What is the meaning of 'on time'?", ["punctual", "use time badly", "last too long", "use more time"], 0),
    ("What is the meaning of 'don't have enough time'?", ["don't have the time you need", "last too long", "punctual", "use more time"], 0),
]
for q, opts, ans in match_data: quiz_data.append({"category": "Từ Vựng - Ghép Nghĩa", "passage": "Match each expression to its meaning.", "question": q, "options": opts, "answer": ans})

# --- 4. OPPOSITES ---
opp_data = [("Princess", "Prince"), ("granddaughter", "grandson"), ("King", "Queen"), ("daughter", "son"), ("sister", "brother"), ("father", "mother"), ("stepfather", "stepmother"), ("husband", "wife")]
for word, correct in opp_data: quiz_data.append({"category": "Từ Vựng - Trái Nghĩa", "passage": "The Royal Family:\nReplace the bold words by the opposite word.", "question": f"What is the opposite of '{word}'?", "options": [correct, "uncle", "aunt", "cousin"], "answer": 0})
for item in quiz_data[-8:]:
    if item["question"].endswith("'Princess'?"): item["options"] = ["Prince", "King", "Queen", "Duke"]; item["answer"] = 0
    if item["question"].endswith("'granddaughter'?"): item["options"] = ["son", "grandson", "brother", "nephew"]; item["answer"] = 1
    if item["question"].endswith("'King'?"): item["options"] = ["Prince", "Princess", "Queen", "Duchess"]; item["answer"] = 2
    if item["question"].endswith("'daughter'?"): item["options"] = ["brother", "son", "father", "nephew"]; item["answer"] = 1
    if item["question"].endswith("'sister'?"): item["options"] = ["brother", "son", "uncle", "father"]; item["answer"] = 0
    if item["question"].endswith("'father'?"): item["options"] = ["sister", "daughter", "mother", "aunt"]; item["answer"] = 2
    if item["question"].endswith("'stepfather'?"): item["options"] = ["mother", "stepmother", "stepbrother", "aunt"]; item["answer"] = 1
    if item["question"].endswith("'husband'?"): item["options"] = ["daughter", "sister", "wife", "mother"]; item["answer"] = 2

# --- 5. SHORT READS ---
short_reads = [
    ("First of all, we need money to repair old roads and build new roads. We also need more to pay teachers' salaries and to pay for services such as trash collection. Finally, more tax money is needed to give financial help to the poor citizens of the city. It is clear that the city will have serious problems if taxes are not raised soon.", "What is the main idea?", ["We should raise city taxes.", "City taxes are too high.", "City taxes pay for new roads."], 0),
    ("One thing you must consider is the quality of the university's educational program. You also need to think about the school's size and location. Finally, you must be sure to consider the university's tuition to make sure you can afford to go to school there.", "What is the main idea?", ["There are several factors to consider when you choose a university to attend.", "You should consider getting a good education.", "It is expensive to attend a university in the United States."], 0),
    ("Color Matters for What You Wear\nClothes are like a second skin. Most likely you feel good when you wear your favorite color...", "Circle the best title for the reading text.", ["Colors and what you wear.", "Colors and kids.", "Colors and your personality."], 0),
    ("Office workers 'admit being rude'\nMost office workers say they are rude or bad-mannered at work...", "The author wants to:", ["give advice on how to behave politely at work", "give specific figures of bad manners at work", "give specific examples of bad manners at work"], 0),
    ("Office workers 'admit being rude'\nMost office workers say they are rude or bad-mannered at work...", "The aim of the texts is to:", ["reflect the fact of officer's bad manners at work with illustrations", "encourage officer's bad manners at work", "reflect the fact of officer's good manners at work with illustrations"], 0)
]
for p, q, opts, ans in short_reads: quiz_data.append({"category": "Đọc Hiểu (Short)", "passage": p, "question": q, "options": opts, "answer": ans})

# --- 6. NOTICES ---
notices = [
    ("JUNGLE CAFÉ\nSORRY!\nTables at the front of the café are reserved for a birthday party.", "What does it say?", ["Don't sit at the front of the café unless you're attending the party.", "If you're coming to the party you shouldn't use the tables at the front.", "The café says 'sorry' because of closing today.", "Only people invited to the party can come into the café."], 0),
    ("STUDENTS!\nYOUR $6 DEPOSIT FOR LOCKER KEYS WON'T BE REFUNDED IF KEYS ARE LOST.", "What does it say?", ["Lost locker keys can be replaced for a charge of $6", "We cannot return your $6 deposit if you lose your locker key.", "You will receive $6 if your locker key is lost", "You cannot collect your locker key until you have paid a $6 deposit."], 1),
    ("Becky,\nDon't forget your Aunt Jane's coming to stay tonight, so can you make sure the house is neat when you go out this afternoon?\nMum", "Why is mum writing this note?", ["To ask Becky to tidy the house before she leaves", "To remind Becky to go to her aunt's house", "To tell Becky to go out with her aunt Jane", "To tell Becky to stay at home to see aunt"], 0),
    ("Frank, Rabbit Records phoned. The CD you ordered arrived today, but someone sold it. They're really sorry! They've reordered available next Monday at the latest.", "Why did the record shop phone?", ["To apologise for a mistake with Frank's order.", "To say that Frank's CD is ready for collection.", "The earliest Frank can get his CD is next Monday.", "To suggest Frank comes in later this week."], 0),
    ("Market vehicles unload here 07.00-10.00 daily\nCustomer parking allowed at other times.", "What does it say?", ["Customers may park here at times when vehicles are not unloading.", "Customers are allowed to park here from 07.00-10.00.", "You may unload your vehicle here at any time.", "Customers may park outside the market for up to three hours."], 0),
    ("What a fantastic city. We found the restaurant you recommended but it was shut! Menu looks good value, so we'll definitely go before we leave.", "What does it say?", ["Elena and Tim think the restaurant's prices are reasonable.", "Elena and Tim have already tried the restaurant.", "Elena and Tim have discovered another good restaurant.", "Elena and Tim will have to try the restaurant on their next visit."], 0),
    ("To: Sally | From: Kim\nFeeling any better? When you're back at college, remember to register for the films course. Email me if you want any information.", "Why has Kim emailed Sally?", ["To remind her to do something.", "To borrow a film from her.", "To give her some details.", "To let her know that he's ill."], 0),
    ("Mustafa, your brother phones. He's emailed you something to read before you write that letter to the hotel. I said you'd call his mobile number today.\nJean", "How should Mustafa reply to his brother?", ["By phone", "By email", "By meeting", "By letter"], 0),
    ("HOSPITAL WAITING ROOM\nPLEASE PUT ALL CHILDREN'S TOYS BACK IN THIS ROOM BEFORE YOU LEAVE.", "What does it say?", ["Please don't leave any toys outside this room when you go.", "Don't forget to pay for the toys before you leave.", "Remember to take your children's toys with you when you leave.", "We leave some toys at the back of this room for children."], 0),
    ("Do not use this medicine for more than seven days without your doctor's advice.", "What does it say?", ["Contact your doctor if you wish to continue using this medicine after one week.", "You cannot keep this medicine for more than seven days.", "Doctors can only supply enough medicine for one week at a time.", "You can use this medicine for more than a week."], 0),
    ("SPORTS HALL\nFinal five minutes of bookings must be used to put equipment away.", "What does it say?", ["All the equipments must be put away after booking time (in the final 5 mins).", "You have five minutes after bookings have finished to return any sports equipment used.", "Bookings now include an extra five minutes for equipment to be put away.", "The hall must be cleared of equipment in the five minutes after bookings end."], 0),
    ("NO DIVING ALLOWED EXCEPT AT THE DEEP END OF THE SWIMMING POOL", "What does it say?", ["You must not dive into the pool where the water is shallow.", "The water is not deep enough in this poor for you to dive.", "Swimming is not permitted where people are diving.", "The swimming pool is too deep to swim."], 0),
    ("Patients with appointments ring once and enter. Those with enquiries ring twice and enter.", "What does it say?", ["Ring once if you have an appointment and twice if you don't.", "You should ring twice and enter unless you have an enquiry.", "If you have an appointment, you don't have to ring.", "To make an appointment, ring once and enter."], 0),
    ("CYCLISTS\nWhen this entrance is locked use side gate.", "What does it say?", ["Cyclists should use a different entrance when this one is locked.", "The only entrance is the side gate.", "If the side gate is locked, go through cycle entrance.", "Lock your cycle near this gate before entering."], 0),
    ("Please don't park within 3 metres of this vehicle - space needed for unloading.", "What does it say?", ["You are requested not to park any closer than 3 metres to this vehicle.", "This parking space is reserved for the vehicle's owner.", "If you want to load things, park beyond 3 metres.", "You should not park near here because it is an exit for vehicles."], 0),
    ("$25 RESERVES ANY PICTURES IN THE GALLERY", "What does it say?", ["We will keep any picture for you if you give us $25.", "It costs $25 to show your picture in the gallery.", "Some of the pictures in the gallery are reserved.", "A picture in the gallery costs $25."], 0),
    ("ROOM TO RENT\nUNEXPECTEDLY AVAILABLE so only $250 per month including fuel bills", "What does it say?", ["This rent includes all bills.", "The rent for this room is reduced to $250 plus bills.", "People renting this room should expect to pay extra for gas and electricity.", "This room is cheap to rent as it was not expected to be empty."], 0),
    ("WANTED: KITCHEN ASSISTANTS\nEvening or weekends. Free meals. Full training provided. Apply inside", "What does it say?", ["There are part-time opportunities for people without experience of working in a kitchen.", "Only people who are trained in kitchen work should apply for these part-time jobs.", "The kitchen assistant will be offered three free meals a day.", "We offer cheap meals to people who work part-time in our kitchen."], 0),
    ("BASKETBALL TRAINING\nProfessional coach available for pre-booked groups - 48 hours' notice required.", "What does it say?", ["A basketball coach is available if a booking is made far enough in advance.", "Those who want to attend the training group must book in 4 days.", "Basketball players are only allowed to practice here if accompanied by a professional coach.", "Basketball training for groups is cancelled until further notice."], 0),
    ("This medicine is taken between meals at six-hourly intervals, up to three times daily.", "What does it say?", ["It is essential to wait six hours before having more of this medicine.", "It is essential to take this medicine before each meal.", "It is essential to take this medicine straight after meals.", "It is essential to use this medicine more than three times a day."], 0),
    ("From: Roberto | To: Sam\nSorry I missed you yesterday. I'm not in all next week, but the following Thursday's fine. Why not see if Sven's free as well?", "What does it say?", ["Roberto is suggesting that Sam should invite Sven to their next meeting.", "Roberto is suggesting that He will join Sam in a meeting next Thursday.", "Roberto will be free the whole next week.", "Roberto is suggesting that Sven is unavailable for a meeting next week."], 0),
    ("Once opened, remove any unused soup from the tin and place in the refrigerator.", "What does it say?", ["This label gives advice on how to store the product.", "This label gives information on the ingredients of the product.", "This label gives advice on how to use the product.", "This label gives advice on how to open the product."], 0),
    ("UNIVERSITY HOLIDAYS\nFrom next Friday, the library will be closed during weekends and evenings.", "What will the library do?", ["Change its opening hours next Friday.", "Close for a long time.", "Open again to students next Friday.", "Have shorter opening hours until next Friday."], 0),
    ("TRIP TO NEW YORK\nApplication forms will be available from the school office from 1st November.", "What does it say?", ["The earliest that students can pick up their application forms is 1st November.", "Students should give in their application forms on 1st November.", "Application forms will be given on 1st November.", "Application forms are unavailable after 1st November."], 0),
    ("Mark,\nWe went on a bus sightseeing tour of the city yesterday. We didn't stop anywhere but saw more than you would on foot.\nJo", "What does it say?", ["Jo is pleased with the number of things she saw from the bus.", "Jo went sightseeing on foot yesterday.", "Jo thinks there are better sightseeing tours than the one she took.", "Jo regrets not having walked around the city to look at the sights."], 0),
    ("Having a great holiday!\nWent windsurfing today after playing beach volleyball.\nStopped for a barbecue on the way to the funfair yesterday.\nSee you soon! Louis", "What does it say?", ["Louis played beach volleyball before he went windsurfing.", "Louis went windsurfing after he went to the funfair yesterday.", "Louis went to the funfair before he had lunch.", "Louis had a barbecue before playing beach volleyball."], 0),
    ("From: Marie | To: Sylviane\nThanks for lending me that biology book - I'm glad you got it back OK. You can borrow my chemistry one and return it next week if you want.", "What does it say?", ["Marie is offering to lend Sylviane a book.", "Marie is asking Sylviane to give back a book she had borrowed.", "Marie is glad to lend Sylviane a book.", "Marie wants to return one of Sylviane's books to her."], 0),
    ("Janine my birthday meal's booked for 6.30 Saturday at Luigi's restaurant. I know there are things you can't eat, so I've attached a menu. Tell me if it's OK.\nSarah", "What does Sarah need to know?", ["If the food at the restaurant will be all right for Janine.", "If Janine wants to see the restaurant menu before Saturday.", "If Janine's birthday meal will start at 6.30 Saturday.", "If Janine will be available to go to the restaurant."], 0),
    ("MATHS HOMEWORK\nSome of you have told me the homework is a bit difficult. So if you haven't finished it by Friday, you can hand it in on Monday.\nMr Peters", "What does it say?", ["Anyone having problems with their homework may have extra time to complete it.", "Students who wish to hand in their homework on Monday should tell Mr Peters.", "The maths homework must be handed in on Friday.", "The homework given out on Friday must be returned by Monday."], 0),
    ("ONLY BOOKS ALREADY PAID FOR CAN BE TAKEN INTO THE BOOKSHOP CAFÉ.", "What does it say?", ["Do not take books which you haven't bought yet into the café.", "Do not read our books while you are eating in the café.", "Pay in the café for any books that you want to buy.", "Don't take books into the café."], 0),
    ("Mr Wright's English lesson today will be in Room 24D beside the language laboratory. He's off sick, so use the lesson to revise for the test.", "What does it say?", ["The usual English teacher cannot attend today's lesson.", "Today's English lesson will be beside the laboratory because the teacher is sick.", "The room for English lessons is changing because of the test.", "The English class must take their workbooks to the language laboratory."], 0),
    ("Class 5 Garden Party\nBecause of bad weather, tomorrow's party will now be in the School Hall.", "What has changed about Class 5's party?", ["The place", "The time", "The weather", "The refreshments"], 0),
    ("Dan,\nDon't forget to put your football shirt in the washing machine as soon as you get home from the match.\nMum", "What does Dan have to do?", ["Remember to wash his football shirt after the match.", "Dan's mum asked him not to put his shirt in the washing machine.", "Remember to make sure his football shirt is clean in time for the match.", "Remember where he put the football shirt that he needs for the match."], 0),
    ("COLLEGE STAFF/STUDENT BUS\nStudents cannot get on the bus without ID cards", "What does it say?", ["Students are not allowed on the bus unless they have ID cards.", "This bus service cannot be used by college staff unless they show ID cards.", "This bus is for students only.", "Students can get their ID cards on the bus."], 0),
    ("Jennie,\nThe garage rang - your new tyres have arrived. They can't fit them until next week. Please let them know today which day will be convenient.", "What does Jennie have to do?", ["Arrange a time for the garage to fit the new tyres.", "Ask another garage to fit her tyres.", "The garage can't fix Jennie's car next week.", "Collect the new tyres from the garage."], 0),
    ("We're staying at the Plaza hotel. It's not the hotel we wanted but it doesn't matter because this one is nearer the beach and I'm spending all my time there.", "How does Sabrina feel about the Plaza hotel?", ["She thinks it has an advantage.", "She wishes it was nearer the beach.", "She didn't want to stay there.", "She's disappointed with it."], 0),
    ("WARNING TO MOTORISTS\nRepairs to bridge start on 30/11/06\nDelays likely for four weeks", "What does it say?", ["Bridge repairs may make your journey longer from the end of November.", "Repairs will finish on 30/11/06.", "Repair work on this bridge will finish in November.", "The bridge cannot be used until the end of November."], 0),
    ("CITY BUSES\nPlease have ready the exact fare for your journey.", "What does it say?", ["You need to have the correct money when you board the bus.", "You must keep your ticket ready for checking.", "All City Bus journeys cost exactly the same.", "You need to change your money before getting on the bus."], 0),
    ("FOR SALE\nGremlins Computer Game (ages 8 and above)\nUnwanted gift - box unopened", "What does it say?", ["The owner of the computer game that is for sale has never used it.", "The game is for children only.", "The person selling the computer game no longer wants to play with it.", "The computer game is for sale because the owner is too old for it."], 0),
    ("COLLEGE OFFICE\nStudent identity cards will be available for collection from 14 January.", "What does it say?", ["The earliest students can pick up their identity cards is 14 January.", "The latest students can get their identity cards is 14 January.", "Students should bring in their identity cards on 14 January.", "Student identity cards are unavailable after 14 January."], 0),
    ("Would anyone who knows anything about the damaged window in the school library please report to my office before the end of the day.\nMrs Swan", "What does Mrs Swan want to do today?", ["Discover how a window got broken.", "Know what was wrong with the library.", "Find out who uses the library.", "Repair damage done to the library."], 0),
    ("Guess who I met on this mountain! My tennis hero! I was breathless because of the climb, so unfortunately couldn't speak to ask him for a photo of us together.", "What is Amanda sorry about?", ["That she didn't have her photograph taken with her tennis hero.", "That she didn't recognize her tennis hero from his photo.", "That she couldn't climb high enough to photograph her tennis hero.", "That she didn't climb the mountain."], 0),
    ("EVENING PERFORMANCE\nRefreshements are served only during the interval.", "What does it say?", ["You can have a drink during the break.", "You can drink after the performance.", "Help yourself to drinks after the performance.", "Snacks are available before the performance."], 0),
    ("UNIVERSITY LIBRARY\nPlease wait here while we check your books.", "What does it say?", ["Do not go away until we have checked your books.", "Come here if you want your books to be checked.", "Do not leave books here for checks without telling us.", "Check you have all your books before you leave the library."], 0),
    ("DO NOT CLIMB CASTLE WALLS - DANGER OF FALLING STONES.", "What does it say?", ["Do not climb the walls as they are dangerous.", "There is a danger of falling on to the stones.", "You should be careful with the stones when climbing.", "Check for loose stones before you climb."], 0),
    ("Passengers unable to show a ticket must pay an immediate fine of $10.", "What does it say?", ["You are fined $10 at once if you can't show us your ticket.", "You can't enter the show without a ticket.", "A $10 fine will be payable later if you travel without a ticket.", "If you lose your ticket, a new one will cost you $10."], 0),
    ("INTERNATIONAL STUDENTS' CLUB\nNext Saturday's coach trip is cancelled because of lack of interest.", "What does it say?", ["We are cancelling the trip on Saturday as numbers are too low.", "To avoid us cancelling another Saturday trip, tell us what your interests are.", "Noboday is interested in the coach trip.", "Saturday's coach trip is cancelled because there are transport problems."], 0),
    ("Hi Abdul,\nI won't be in college as I'm not well. Please call round on your way in to pick up my homework-it's due in today. Thanks, Aziz.", "What does Aziz want Abdul to do?", ["Take his homework to college for him. (Do his homework for him)", "Call their college to say that he is not well.", "Take his homework to college for him.", "Pick up any new homework given out at college today."], 0),
    ("Tony\nMaria's sorry but she's going to be late this evening. The train is delayed again! Don't forget you're meeting her at the station. She should be there at 7.15.\nAnita", "What is Anita doing?", ["Explaining that she will be late", "Asking Tony to meet her at the station.", "Reminding somebody of an arrangement", "Apologizing for missing the meeting."], 0),
    ("Casali Restaurant\nWe are open downstairs while improvements are made to this area.", "What does it say?", ["You can only eat in one part of the restaurant at the moment.", "Please come downstairs and try our recently improved restaurant.", "The restaurant will not be open due to repairs.", "The restaurant will reopen when the improvements are finished."], 0),
    ("IF YOUR SHOES ARE DIRTY, PLEASE REMOVE THEM BEFORE ENTERING THIS CHANGING ROOM.", "What does it say?", ["Clean your shoes at the entrance to the changing room before you come in.", "You can keep your shoes on in the changing room unless they are dirty.", "All shoes must be taken off and left at the changing room entrance.", "Please take off your shoes if possible."], 0)
]
for p, q, opts, ans in notices: quiz_data.append({"category": "Biển Báo & Thông Báo", "passage": p, "question": q, "options": opts, "answer": ans})

# --- 7. GAP FILL ---
bad_manners = "A recruitment firm gives this advice to new workers: It is important to (1)___ time in your relationships with others at (2)___. Get to know the people who work near you: (3)___ yourself to them and tell them something about yourself. If people ask for your help, always (4)___ positively. Don't (5)___ emails or phone calls just because you are busy. If you make a mistake, it is better to (6)___ it and then apologise. When things go wrong, stay calm and (7)___ shouting and using bad language. Remember good (8)___ help to (9)___ your working (10)___ and you will find you can enjoy your work more."
bad_manners_qa = [{"q": "(1) It is important to ___ time in your relationships...", "opts": ["invest", "Work", "introduce", "Respond"], "ans": 0}, {"q": "(2) ...with others at ___.", "opts": ["Work", "Manners", "Admit", "Avoid"], "ans": 0}, {"q": "(3) ... ___ yourself to them and tell them something about yourself.", "opts": ["introduce", "ignore", "improve", "Environment"], "ans": 0}, {"q": "(4) If people ask for your help, always ___ positively.", "opts": ["Respond", "invest", "Admit", "Work"], "ans": 0}, {"q": "(5) Don't ___ emails or phone calls just because you are busy.", "opts": ["ignore", "Avoid", "Manners", "introduce"], "ans": 0}, {"q": "(6) If you make a mistake, it is better to ___ it and then apologise.", "opts": ["Admit", "improve", "invest", "Work"], "ans": 0}, {"q": "(7) When things go wrong, stay calm and ___ shouting and using bad language.", "opts": ["Avoid", "Respond", "introduce", "ignore"], "ans": 0}, {"q": "(8) Remember good ___ help to improve your working Environment...", "opts": ["Manners", "Work", "Admit", "invest"], "ans": 0}, {"q": "(9) Remember good Manners help to ___ your working Environment...", "opts": ["improve", "ignore", "Avoid", "introduce"], "ans": 0}, {"q": "(10) ...help to improve your working ___", "opts": ["Environment", "Manners", "Work", "Admit"], "ans": 0}]
for qa in bad_manners_qa: quiz_data.append({"category": "Từ Vựng - Điền Từ", "passage": bad_manners, "question": qa["q"], "options": qa["opts"], "answer": qa["ans"]})

erik = "A: Did you read the article on Erik Weihenmayer? Isn't he a fascinating person?\nB: Yes, he really is! Imagine being blind and (1)___ a mountain!\nA: Even for people who can see, climbing a mountain is very difficult.\nB: You know, I was really surprised to learn that he is also a teacher and a (2)___ athlete.\nA: People like Erik really (3)___ people all around the world. Did you know that he is not the only person with a disability who has done amazing things?\nB: Yes! I read about Helen Keller in school. She was blind, deaf, and could not speak. Helen Keller became famous because of all the (4)___ she had in her lifetime.\nA: Right! But people who have disabilities are not the only people who face (5)___. We all have difficulties in our lives. We face challenges at home, at work, at school, and in relationships.\nB: I agree. Do you think challenges are good for us?\nA: Yes, I do. I think if a person is not (6)___ and has (7)___, then he or she can overcome most of life's challenges. I believe that challenges make us stronger.\nB: You are right! I think that people like Erik Weihenmayer and Helen Keller really (8)___ others to be brave and face life's challenges and never give up."
erik_qa = [{"q": "(1) Imagine being blind and ___ a mountain!", "opts": ["climbing", "afraid", "professional", "inspire"], "ans": 0}, {"q": "(2) I was really surprised to learn that he is also a teacher and a ___ athlete.", "opts": ["professional", "ambition", "accomplishments", "encourage"], "ans": 0}, {"q": "(3) People like Erik really ___ people all around the world.", "opts": ["inspire", "afraid", "challenges", "climbing"], "ans": 0}, {"q": "(4) Helen Keller became famous because of all the ___ she had in her lifetime.", "opts": ["accomplishments", "ambition", "professional", "encourage"], "ans": 0}, {"q": "(5) ...people who have disabilities are not the only people who face ___.", "opts": ["challenges", "inspire", "climbing", "afraid"], "ans": 0}, {"q": "(6) I think if a person is not ___ and has ambition...", "opts": ["afraid", "professional", "encourage", "accomplishments"], "ans": 0}, {"q": "(7) ...if a person is not afraid and has ___...", "opts": ["ambition", "inspire", "challenges", "climbing"], "ans": 0}, {"q": "(8) I think that people like Erik Weihenmayer and Helen Keller really ___ others to be brave...", "opts": ["encourage", "afraid", "professional", "ambition"], "ans": 0}]
for qa in erik_qa: quiz_data.append({"category": "Từ Vựng - Điền Từ", "passage": erik, "question": qa["q"], "options": qa["opts"], "answer": qa["ans"]})

rf_phrases_qa = [{"q": "In other ways, their lives are very _______ their friends' lives.", "opts": ["different from", "delighted with", "in line to", "under police escort"], "ans": 0}, {"q": "The Duchess of Cornwall and Prince Harry... are _______ the news.", "opts": ["delighted with", "in due course", "admitted to", "spent time with"], "ans": 0}, {"q": "The baby will be third _______ the throne.", "opts": ["in line to", "different from", "admitted to", "under police escort"], "ans": 0}, {"q": "A spokesman said the duchess has been _______ King Edward VII Hospital...", "opts": ["admitted to", "gave birth to", "spent time with", "in due course"], "ans": 0}, {"q": "...after the duchess _______ a baby boy.", "opts": ["gave birth to", "spent time with", "delighted with", "admitted to"], "ans": 0}, {"q": "The young parents _______ their son before telling the news...", "opts": ["spent time with", "different from", "gave birth to", "under police escort"], "ans": 0}, {"q": "A bulletin signed by him was taken... to the palace _______", "opts": ["under police escort", "in line to", "in due course", "different from"], "ans": 0}, {"q": "A Palace spokesman said the names of the baby would be announced _______", "opts": ["in due course", "under police escort", "delighted with", "admitted to"], "ans": 0}]
for qa in rf_phrases_qa: quiz_data.append({"category": "Từ Vựng - Điền Từ", "passage": "The Royal Family:\nComplete the sentences using the appropriate phrases.", "question": qa["q"], "options": qa["opts"], "answer": qa["ans"]})

# --- 8. READING COMPREHENSION ---
passages = {
    "wildlife": "Nowadays people are more aware that wildlife all over the world is in danger. Many species of animals are threatened, and could easily become _(1)_ if we do not make an effort to protect them. There are many reasons for this. In some cases, animals are hunted for their fur or for other valuable parts of their bodies. Some birds, _(2)_ as parrots are caught alive and sold as pets. For many animals and birds, the problem is that their habitat-the place where they live-is disappearing. More_ _(3)_ is used for farms, for houses or industry, and there are fewer open spaces than there once were. Farmers use powerful chemicals to help them grow better crops, but these chemicals pollute _(4)_ environment and harm wildlife. The most successful animal on earth-human beings-will soon be the only ones left, _(5)_ we can solve this problem.",
    "public_schools": "In most countries, almost all schools (1)__ private until the early 1800's. At that time, many government leaders began to encourage development of public schools to promote national progress by_(2)_ education widely available to citizens. Today, the number of public and private schools differs _ (3)__ one country to another. In many developed countries, private schools offer a general focus on __ (4)__ for college;Chào bạn, tôi rất sẵn lòng giúp bạn viết code. Tuy nhiên, bạn chưa cung cấp thông tin về bài toán hay ngôn ngữ lập trình cụ thể mà bạn đang cần.

Để đoạn code được viết chính xác và tối ưu nhất—cho dù đó là một script Python để tương tác với API của Zabbix, một đoạn bash script tự động hóa trên Rocky Linux, một mẫu cấu hình cho thiết bị Cisco, hay bất kỳ một ứng dụng nào khác—tôi cần thêm một vài chi tiết:

*   **Ngôn ngữ và môi trường:** Bạn muốn viết bằng ngôn ngữ gì và chạy trên nền tảng nào?
*   **Mục tiêu cụ thể:** Đoạn code cần giải quyết bài toán gì (thông tin đầu vào, logic xử lý và kết quả đầu ra mong muốn)?
*   **Chi tiết bổ sung:** Có thư viện cụ thể, ràng buộc hệ thống, hay đoạn code cũ nào bạn đang cần sửa lỗi không?

Bạn đang cần hoàn thiện đoạn code cho dự án hoặc tác vụ cụ thể nào hôm nay?
