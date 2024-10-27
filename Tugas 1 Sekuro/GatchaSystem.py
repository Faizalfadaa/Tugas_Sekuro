import random

class Genshin:
    def __init__(self, probability, pools, pity_5_star, pity_4_star, primogem):
        self.probability = probability
        self.probability = {'5_star': 0.6,
                            '4_star': 5.1,
                            '3_star': 94.3}
        self.pools = pools
        self.pools = {"5_star": ['Xiao', 'Diluc', 'Jean', 'Qiqi', 'Mona', 'Keqing', 'Dehya'],
                       '4_star': ['Faruzan', 'Bennet', 'Dori'],
                       '3_star': ['Slingshot', 'Debate Club', 'White Tassel']}
        self.pity_4_star = pity_4_star
        self.pity_5_star = pity_5_star
        self.primogem = primogem

    def increase_pity(self):
        self.pity_5_star += 1
        self.pity_4_star += 1
    
    def reset_pity_4_star(self):
        self.pity_4_star = 0

    def reset_pity_5_star(self):
        self.pity_5_star = 0

class Gatcha(Genshin):
    def gatcha_system(self):
        # Guarantee a 5-star
        if self.pity_5_star >= 90:
            reward = random.choice(self.pools['5_star'])
            self.reset_pity_5_star()
            print(f'Pulled {reward} [*****]')
            return

        # Guarantee a 4-star
        if self.pity_4_star >= 10:
            reward = random.choice(self.pools['4_star'])
            self.reset_pity_4_star()
            self.increase_pity() 
            print(f'Pulled {reward} [****]')
            return

        # Gatcha probability
        pull = random.uniform(0, 100)
        if pull <= self.probability['5_star']:
            reward = random.choice(self.pools['5_star'])
            self.reset_pity_5_star()
            print(f'Pulled {reward} [*****]')
        elif pull <= self.probability['4_star']:
            reward = random.choice(self.pools['4_star'])
            self.reset_pity_4_star()
            self.increase_pity()
            print(f'Pulled {reward} [****]')
        else:
            reward = random.choice(self.pools['3_star'])
            self.increase_pity()
            print(f'Pulled {reward} [***]')

class Pull:
    def pulling(self, gatcha): 
        ten_pull = 1600
        print('-----------------------')
        print('Lets go Gambling!')
        print('-----------------------')
        while gatcha.primogem >= 0:  
            pull = input("Do a 10 pull? (yes/no): ")
            if pull == 'yes':
                if gatcha.primogem > 1600:
                    print("You recieved:")
                    for i in range(10):
                        gatcha.gatcha_system()  
                    gatcha.primogem -= ten_pull
                    print('-----------------------')
                    print('Aw DangIt !')
                    print('-----------------------')
                    print(f'Remaining primogems: {gatcha.primogem}')
                    print('-----------------------')
                else:
                    print('-----------------------')
                    print('Insufficient Primogem!')
                    print('Use real money to buy more primogems!!')
                    print('-----------------------')
                    break
            elif pull == 'no':
                print('-----------------------')
                print('Why did you stop gambling??!')
                print('-----------------------')
                break
            else:
                print('Invalid input!')

pity_4_star = 0
pity_5_star = 0
primogem = 32000

gacha = Gatcha({}, {}, pity_5_star, pity_4_star, primogem)

pull_time = Pull()
pull_time.pulling(gacha)



