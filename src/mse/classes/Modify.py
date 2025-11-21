import random



###rules for modifying token stream as data is gathered
class Modify:


    def __init__(self, **kwargs):
        super(Modify, self).__init__(**kwargs)

        self.last_simulated = None


        #collects data acquired through events and changes that occur after initial seed. purpose is to modify the token stream to tailor output according to user-collected behavior.
        def collect_data(self):
             pass
        
        def analyze_data(self):
             pass
        
        def morph_data(self):
             pass

        def insert_change(self):
        ##based on activity, modify the ratings/seed
            pass


    def simulate_action(self, selection):
        action = random.choice(list(selection.rules.items()))
        print("\n\ncurrent ratings")    
        print(selection.ratings)
        print("\nsimulated action")
        self.last_simulated = action[0]
        print(action[0])
        print("\naction ratings")
        print(action[1])

        for rating in list(selection.ratings.keys()):
            selection.ratings[rating] += action[1][rating]
        print("\nadjusted ratings")    
        print(selection.ratings)


    def compare_actions(self, engine, original, new, last):
        new = last = engine.generate_tokens(50)
        print(original)
        print(new)

        seen = []
        old_count = []
        for j in range(len(original)):
            same = [i for i in original if i == original[j]]
            if same not in seen and same and len(same) > 0:
                seen.append(same)
                old_count.append([same[0], same[0] + ": " + str(len(same))])

        seen = []
        new_count = []
        for j in range(len(original)):
            same = [i for i in new if i == original[j]]    
            if same not in seen and same and len(same) > 0:
                seen.append(same)
                new_count.append([same[0], same[0] + ": " + str(len(same))])

        old_count = sorted(old_count)
        new_count = sorted(new_count)

        for j in range(len(new_count)):
            in_old = [i for i in original if new_count[j][0] == i]
            in_new = [i for i in new if new_count[j][0] == i]
            self.analyze_actions(new_count[j][0], len(in_old), len(in_new))


    ###compare old versus new actions based on activity. this shows how much the previous activity affects the personalization stream. prompts/goals are altered as the user completes an action. only an example
    #question: does it affect the stream too much or too little?
    def analyze_actions(self, action, old, new):
        print()
        print("last action: " + action)
        print("old freq.: " + str(old))
        print("new freq.: " + str(new))
        ratio = int(new/old * 100) if new != old else 0
        print(str(ratio) + "% of original")
        print("last simulation: " + self.last_simulated)