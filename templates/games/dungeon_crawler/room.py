class Room:
    def __init__(self, name, player, enemy, event, desc):
        self.name = name
        self.player = player
        self.enemy = enemy
        self.con_room = None
        self.event = event
        self.desc = desc
        # self.con1 = c1
        # self.con2 = c2
        # self.con3 = c3

    def combat(self):
        print(f"you encountered {self.enemy.name}")
        while self.player.health > 0 and self.enemy.health > 0:
            print("1) gun")
            print("2) counter")
            action = input("")
            if action == "1" or action == 1:
                print("")
                self.player.attack(self.enemy)
                print("")
                if self.enemy.health > 0:
                    self.enemy.attack(self.player)
                    print("")
            elif action == "2" or action == 2:
                print("")
                self.player.counter(self.enemy)
                print("")
                if self.enemy.health > 0:
                    self.enemy.attack(self.player)
                    print("")
            else:
                print("wrong try again")

        if self.player.health < 0:
            print("you lose")
            exit()
        if self.enemy.health < 0:
            print("you win")        
            self.player.cash += self.enemy.cash
            print(f"You got {self.enemy.cash} USD")
            self.enemy = None
    
    def enter(self):
        print("")
        print(f"you're at {self.name} now")
        print("")
        print(self.desc)
        print("")
        
        if self.enemy:
            self.combat()
        if self.event:
            print("shop or sum")
        self.travel()


    def travel(self):
        if self.con_room:
            print("")
            i = 1
            for room in self.con_room:
                print(f"{i}) to go to {room.name}")
                i+=1
            next_room = int(input()) - 1
            self.con_room[next_room].enter()





    # def travel(self):
    #     print(f"1) go to {self.con1.name}")
    #     if self.con2 != "no":
    #         print(f"2) go to {self.con2.name}")
    #         if self.con3 != "no":
    #             print(f"3) go to {self.con3.name}")