# https://workat.tech/machine-coding/practice/splitwise-problem-0kp2yneec2q2


# SHOW
# SHOW u1
# EXPENSE u1 1000 4 u1 u2 u3 u4 EQUAL
# SHOW u4
# SHOW u1
# EXPENSE u1 1250 2 u2 u3 EXACT 370 880
# SHOW
# EXPENSE u4 1200 4 u1 u2 u3 u4 PERCENT 40 20 20 20
# SHOW u1
# SHOW
# Q
class Users:
    def __init__(self, name):
        self.name = name
        self.owe = [] # user_name, amount
        self.given = [] 
        # self.transactions = [] # owe -ve, given +ve

    def add_owe(self,user_name, amount):
        self.owe.append([user_name, amount])

    def add_given(self,user_name, amount):
        self.given.append([user_name, amount])

    def show(self,user_name_list):
        if len(self.given) == 0 and len(self.owe) == 0:
            print( "No balances")
        mapy = {}
        for i in user_name_list:
            mapy[i] = 0

        for i in self.given:
            mapy[i[0]] += i[1]

        for i in self.owe:
            mapy[i[0]] -= i[1]
        res = []
        for  i in mapy:
            if mapy[i] > 0 and i != self.name:
                res.append(f"{i} owes {self.name} : {mapy[i]} ")
            elif mapy[i] < 0 and i != self.name:
                res.append(f"{self.name} owes {i} : {-1*mapy[i]} ")
                # res.append([i, self.name, -1*mapy[i]])
        return res

    # def add_transaction(self, amount):
    #     self.add_transaction( amount)
    


class SplitWise:
    def __init__(self,):
        self.user_map = {}
        self.transaction_history = []


    def add_user(self,user_name):
        self.user_map[user_name] = Users(user_name)

    def add_transaction(self, li):
        self.transaction_history.append(li)

    def __str__(self,):
        return f"Users in group {len(self.user_map)}"
    
sp = SplitWise()
sp.add_user('u1')
sp.add_user('u2')
sp.add_user('u3')
sp.add_user('u4')

# interaction - breat with Q

while True:
    inp = input()
    inp_list = inp.split()
    # print(inp)
    if inp_list[0] == "Q":
        print("thanks for using splitwise")
        break

    if inp_list[0] == "SHOW":
        if len(inp_list) == 1: #SHOW
            if len(sp.transaction_history) == 0:
                print("No balances")
            else:
                fin = set()
                for i in sp.user_map.keys():
                    res1 = sp.user_map[i].show(sp.user_map.keys())
                    for j in res1:
                        fin.add(j)

                for i in fin:
                    print(i)

        elif len(inp_list) ==2:
            user_name = inp_list[1]
            res1 = sp.user_map[user_name].show(sp.user_map.keys())
            for i in res1:
                print(i)

    elif inp.split()[0] == "EXPENSE":
        sp.add_transaction(inp_list)
        giver = inp_list[1]
        amount = float(inp_list[2])
        split_between_users = int(inp_list[3])
        users_split = []
        counter = 3
        

        # print("split between users ",split_between_users)

        for i in range(split_between_users):
            counter+=1
            users_split.append([inp_list[counter], 0])
        
        counter +=1 # command

        if inp_list[counter] == "EQUAL":
            for i in range(split_between_users):
                users_split[i] = [users_split[i][0], amount/len(users_split)]
                # users_split[i] = amount/len(users_split)
            # print(users_split)

        elif inp_list[counter] == "EXACT":
            for i in range(split_between_users):
                counter+=1
                users_split[i] = [users_split[i][0], int(inp_list[counter])]
        
        elif inp_list[counter] == "PERCENT":
            for i in range(split_between_users):
                counter+=1
                users_split[i] = [users_split[i][0], amount*int(inp_list[counter])/100]

        # add to users.
        # print("here")
        # print("sp complete",sp.user_map)

        for i in range(split_between_users):
            # print(sp.user_map[users_split[i][0]].name)
            # if giver == users_split[i][0]:
            #     continue
            sp.user_map[giver].add_given(users_split[i][0],users_split[i][1])
            # print("added")
            sp.user_map[users_split[i][0]].add_owe(giver,users_split[i][1])

        # print("sp complete",sp.user_map)
        # print("############## START ################## ")
        # for i in sp.user_map.keys():
        #     sp.user_map[i].show(sp.user_map.keys())
        #     print("#### ")
        # print("############### END #################")

# print(sp)