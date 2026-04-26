BASICS_LESSONS = [
    # ========== HOME ROW ==========
    # Left index (f)
    {"id": 1, "title": "Home Row: Left Index (F)", "target": "ffff ffff ffff", "instr": "🟢 INDEX FINGER LEFT | Place left index on F. Type F repeatedly. Do not move other fingers.", "finger": "left_index", "row": "home"},
    # Right index (j)
    {"id": 2, "title": "Home Row: Right Index (J)", "target": "jjjj jjjj jjjj", "instr": "🟢 INDEX FINGER RIGHT | Right index on J. Type J repeatedly. Keep thumbs on space bar.", "finger": "right_index", "row": "home"},
    # Both indices
    {"id": 3, "title": "Home Row: Both Indexes (F & J)", "target": "fj fjf jfj fjjf jffj", "instr": "🔁 BOTH INDEXES | Alternate between F and J. Feel the home row bumps.", "finger": "both_index", "row": "home"},
    
    # Left middle (d)
    {"id": 4, "title": "Home Row: Left Middle (D)", "target": "dddd dddd dddd", "instr": "🟡 MIDDLE FINGER LEFT | Left middle on D. Type D. Keep index on F.", "finger": "left_middle", "row": "home"},
    # Right middle (k)
    {"id": 5, "title": "Home Row: Right Middle (K)", "target": "kkkk kkkk kkkk", "instr": "🟡 MIDDLE FINGER RIGHT | Right middle on K. Type K.", "finger": "right_middle", "row": "home"},
    # Both middle
    {"id": 6, "title": "Home Row: Both Middles (D & K)", "target": "dk dk dk kd dkdk kd dkkd", "instr": "🔁 BOTH MIDDLES | Alternate D and K.", "finger": "both_middle", "row": "home"},
    
    # Left ring (s)
    {"id": 7, "title": "Home Row: Left Ring (S)", "target": "ssss ssss ssss", "instr": "🔴 RING FINGER LEFT | Left ring on S. Type S.", "finger": "left_ring", "row": "home"},
    # Right ring (l)
    {"id": 8, "title": "Home Row: Right Ring (L)", "target": "llll llll llll", "instr": "🔴 RING FINGER RIGHT | Right ring on L. Type L.", "finger": "right_ring", "row": "home"},
    # Both ring
    {"id": 9, "title": "Home Row: Both Rings (S & L)", "target": "sl sl sl ls slsl lssl", "instr": "🔁 BOTH RINGS | Alternate S and L.", "finger": "both_ring", "row": "home"},
    
    # Left pinky (a)
    {"id": 10, "title": "Home Row: Left Pinky (A)", "target": "aaaa aaaa aaaa", "instr": "⚫ PINKY LEFT | Left pinky on A. Type A.", "finger": "left_pinky", "row": "home"},
    # Right pinky (;)
    {"id": 11, "title": "Home Row: Right Pinky (;)", "target": ";;;; ;;;; ;;;;", "instr": "⚫ PINKY RIGHT | Right pinky on semicolon (;). Type ;", "finger": "right_pinky", "row": "home"},
    # Both pinky
    {"id": 12, "title": "Home Row: Both Pinkies (A & ;)", "target": "a; a; a; ;a a;a; ;aa;", "instr": "🔁 BOTH PINKIES | Alternate A and ;", "finger": "both_pinky", "row": "home"},
    
    # Home Row Exam
    {"id": 13, "title": "📝 HOME ROW EXAM", "target": "asdf jkl; fdsa ;lkj a;sldkfj fjak ls;d", "instr": "🎯 EXAM: Type the entire home row sequence. 80% accuracy required to pass.", "is_exam": True, "pass_score": 80, "row": "home"},
    
    # ========== TOP ROW ==========
    # Left index (r)
    {"id": 14, "title": "Top Row: Left Index (R)", "target": "rrrr rrrr rrrr", "instr": "🟢 INDEX LEFT (TOP) | Reach up from F to R. Return to F after each key.", "finger": "left_index", "row": "top"},
    # Right index (u)
    {"id": 15, "title": "Top Row: Right Index (U)", "target": "uuuu uuuu uuuu", "instr": "🟢 INDEX RIGHT (TOP) | Reach from J to U.", "finger": "right_index", "row": "top"},
    # Both indices (r,u)
    {"id": 16, "title": "Top Row: Both Indexes (R & U)", "target": "ru ru ur ruru urur", "instr": "🔁 BOTH INDEXES (TOP) | Alternate R and U.", "finger": "both_index", "row": "top"},
    
    # Left middle (e)
    {"id": 17, "title": "Top Row: Left Middle (E)", "target": "eeee eeee eeee", "instr": "🟡 MIDDLE LEFT (TOP) | Reach from D to E.", "finger": "left_middle", "row": "top"},
    # Right middle (i)
    {"id": 18, "title": "Top Row: Right Middle (I)", "target": "iiii iiii iiii", "instr": "🟡 MIDDLE RIGHT (TOP) | Reach from K to I.", "finger": "right_middle", "row": "top"},
    # Both middle (e,i)
    {"id": 19, "title": "Top Row: Both Middles (E & I)", "target": "ei ei ie eiei ieie", "instr": "🔁 BOTH MIDDLES (TOP) | Alternate E and I.", "finger": "both_middle", "row": "top"},
    
    # Left ring (w)
    {"id": 20, "title": "Top Row: Left Ring (W)", "target": "wwww wwww wwww", "instr": "🔴 RING LEFT (TOP) | Reach from S to W.", "finger": "left_ring", "row": "top"},
    # Right ring (o)
    {"id": 21, "title": "Top Row: Right Ring (O)", "target": "oooo oooo oooo", "instr": "🔴 RING RIGHT (TOP) | Reach from L to O.", "finger": "right_ring", "row": "top"},
    # Both ring (w,o)
    {"id": 22, "title": "Top Row: Both Rings (W & O)", "target": "wo ow wowo owow", "instr": "🔁 BOTH RINGS (TOP) | Alternate W and O.", "finger": "both_ring", "row": "top"},
    
    # Left pinky (q)
    {"id": 23, "title": "Top Row: Left Pinky (Q)", "target": "qqqq qqqq qqqq", "instr": "⚫ PINKY LEFT (TOP) | Reach from A to Q.", "finger": "left_pinky", "row": "top"},
    # Right pinky (p)
    {"id": 24, "title": "Top Row: Right Pinky (P)", "target": "pppp pppp pppp", "instr": "⚫ PINKY RIGHT (TOP) | Reach from ; to P.", "finger": "right_pinky", "row": "top"},
    # Both pinky (q,p)
    {"id": 25, "title": "Top Row: Both Pinkies (Q & P)", "target": "qp pq qpqp pqpq", "instr": "🔁 BOTH PINKIES (TOP) | Alternate Q and P.", "finger": "both_pinky", "row": "top"},
    
    # Top Row Exam
    {"id": 26, "title": "📝 TOP ROW EXAM", "target": "qwertyuiop qazwsxedc rfvbnmju", "instr": "🎯 EXAM: Type the full top row. 80% accuracy required to pass.", "is_exam": True, "pass_score": 80, "row": "top"},
    
    # ========== BOTTOM ROW ==========
    # Left index (v)
    {"id": 27, "title": "Bottom Row: Left Index (V)", "target": "vvvv vvvv vvvv", "instr": "🟢 INDEX LEFT (BOTTOM) | Reach down from F to V.", "finger": "left_index", "row": "bottom"},
    # Right index (m)
    {"id": 28, "title": "Bottom Row: Right Index (M)", "target": "mmmm mmmm mmmm", "instr": "🟢 INDEX RIGHT (BOTTOM) | Reach from J to M.", "finger": "right_index", "row": "bottom"},
    # Both indices (v,m)
    {"id": 29, "title": "Bottom Row: Both Indexes (V & M)", "target": "vm mv vmvm mvmv", "instr": "🔁 BOTH INDEXES (BOTTOM) | Alternate V and M.", "finger": "both_index", "row": "bottom"},
    
    # Left middle (c)
    {"id": 30, "title": "Bottom Row: Left Middle (C)", "target": "cccc cccc cccc", "instr": "🟡 MIDDLE LEFT (BOTTOM) | Reach from D to C.", "finger": "left_middle", "row": "bottom"},
    # Right middle (n)
    {"id": 31, "title": "Bottom Row: Right Middle (N)", "target": "nnnn nnnn nnnn", "instr": "🟡 MIDDLE RIGHT (BOTTOM) | Reach from K to N.", "finger": "right_middle", "row": "bottom"},
    # Both middle (c,n)
    {"id": 32, "title": "Bottom Row: Both Middles (C & N)", "target": "cn cn nc cncn ncnc", "instr": "🔁 BOTH MIDDLES (BOTTOM) | Alternate C and N.", "finger": "both_middle", "row": "bottom"},
    
    # Left ring (x)
    {"id": 33, "title": "Bottom Row: Left Ring (X)", "target": "xxxx xxxx xxxx", "instr": "🔴 RING LEFT (BOTTOM) | Reach from S to X.", "finger": "left_ring", "row": "bottom"},
    # Right ring (,)
    {"id": 34, "title": "Bottom Row: Right Ring (,)", "target": ",,,, ,,,, ,,,,", "instr": "🔴 RING RIGHT (BOTTOM) | Reach from L to comma (,).", "finger": "right_ring", "row": "bottom"},
    # Both ring (x,)
    {"id": 35, "title": "Bottom Row: Both Rings (X & ,)", "target": "x, ,x x,x, ,x,x", "instr": "🔁 BOTH RINGS (BOTTOM) | Alternate X and comma.", "finger": "both_ring", "row": "bottom"},
    
    # Left pinky (z)
    {"id": 36, "title": "Bottom Row: Left Pinky (Z)", "target": "zzzz zzzz zzzz", "instr": "⚫ PINKY LEFT (BOTTOM) | Reach from A to Z.", "finger": "left_pinky", "row": "bottom"},
    # Right pinky (.)
    {"id": 37, "title": "Bottom Row: Right Pinky (.)", "target": ".... .... ....", "instr": "⚫ PINKY RIGHT (BOTTOM) | Reach from ; to period (.).", "finger": "right_pinky", "row": "bottom"},
    # Both pinky (z,.)
    {"id": 38, "title": "Bottom Row: Both Pinkies (Z & .)", "target": "z. .z z.z. .z.z", "instr": "🔁 BOTH PINKIES (BOTTOM) | Alternate Z and period.", "finger": "both_pinky", "row": "bottom"},
    
    # Bottom Row Exam
    {"id": 39, "title": "📝 BOTTOM ROW EXAM", "target": "zxcvbnm zxcvbnm mnbvcxz zx./,mnb", "instr": "🎯 EXAM: Type the bottom row. 80% accuracy required to pass.", "is_exam": True, "pass_score": 80, "row": "bottom"},
    
    # ========== NUMBERS & SYMBOLS ==========
    {"id": 40, "title": "Numbers Row (1-0)", "target": "1234567890 1234567890", "instr": "🔢 NUMBERS | Reach up and left from home row. Keep fingers curved.", "row": "numbers"},
    {"id": 41, "title": "Symbols with Shift", "target": "!@#$%^&*() !@#$%^&*()", "instr": "✨ SYMBOLS | Use left/right Shift keys. Practice each symbol.", "row": "symbols"},
    {"id": 42, "title": "Mixed Punctuation", "target": ".,!?;: '\"() []{} <>", "instr": "📌 PUNCTUATION | Type all common punctuation marks.", "row": "punctuation"},
    
    # Final Exam
    {"id": 43, "title": "🎓 FINAL TYPING EXAM", "target": "The quick brown fox jumps over the lazy dog. 12345!@#$% qwertyuiop[] asdfghjkl;' zxcvbnm,./", "instr": "🏆 FINAL TEST: Type the full pangram, numbers, symbols, and all rows. 85% accuracy required to pass.", "is_exam": True, "pass_score": 85, "row": "final"}
]