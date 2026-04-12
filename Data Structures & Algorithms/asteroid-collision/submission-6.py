class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []

        # 2 loops
        # 1 para cada elemento, outro loop para comparar o elemento ao resto do stack
        # ordem dos elementos importa
        # apenas remover neg encontra pos, não o contrario, talvez 1 stack seja melhor
        for asteroid in asteroids:
            if asteroid > 0:
                result.append(asteroid)
            elif asteroid < 0 and result:
                temp = asteroid
                
                while result and result[-1] > 0:
                    if abs(asteroid) > result[-1]: 
                        result.pop()
                        
                    elif abs(asteroid) == result[-1]: 
                        result.pop()
                        temp = None
                        break
                    else:
                        temp = None
                        break

                if temp:
                    result.append(temp)

            else:
                result.append(asteroid)

        return result