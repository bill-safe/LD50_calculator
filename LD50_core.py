import math
class LD50:

    def calculate_ld50_value(self, doses, Mouse_population,death_Mouse ):
        sorted_probabilities = []
        # 排序
        sorted_lists = sorted(zip(doses, Mouse_population,death_Mouse), key=lambda x: x[0])
        sorted_doses, sorted_Mouse_population,sorted_death_Mouse = zip(*sorted_lists)
        #概率计算
        for a in range(len(sorted_death_Mouse)):
            sorted_probabilities.append(sorted_death_Mouse[a]/sorted_Mouse_population[a])
        return sorted_doses,sorted_probabilities
    
    def LD50_roughly(self,sorted_doses,sorted_probabilities):
        ld50_sum = 0.0
        # ld50计算
        for i in range(len(sorted_doses) - 1):
            xi = math.log10(sorted_doses[i])
            xi1 = math.log10(sorted_doses[i + 1])
            pi = sorted_probabilities[i]
            pi1 = sorted_probabilities[i + 1]
            ld50_sum += 0.5 * (xi + xi1) * (pi1 - pi)
        ld50_roughly = math.pow(10, ld50_sum)
        return ld50_roughly
    
    def sm(self,sorted_doses,sorted_probabilities,Mouse_population):
        #计算标准差
        d = math.log10(sorted_doses[0]) - math.log10(sorted_doses[1])
        pi_sum = sum(sorted_probabilities)
        pi2_sum = sum(x**2 for x in sorted_probabilities)
        n = sum(Mouse_population) / len(Mouse_population)
        sm = d * math.sqrt((pi_sum - pi2_sum) / n)
        return sm
        
    def Ld50_maxAndLd50_min(self,sm,ld50_roughly):
        LD50_max = ld50_roughly * 10**(1.96 * sm)
        LD50_min = ld50_roughly / 10**(1.96 * sm)
        return LD50_max,LD50_min