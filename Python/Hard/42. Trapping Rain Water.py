class Solution:
    def trap(self, height) -> int:
        pointer = 0
        water_points = 0
        while pointer < len(height):
            init_hole = pointer
            hole_size = []
            if height[pointer] == 0 and pointer == 0:
                pointer += 1
                continue
            end_hole = pointer
            while len(height) - pointer:
                is_cume = False
                i = pointer + 1
                while len(height) - pointer:
                    i += 1
                    try:
                        if height[pointer] <= height[i]:
                            is_cume = False
                            break
                        is_cume = True
                    except:
                        is_cume = True
                        break
                end_hole += 1
                try:
                    if height[pointer] <= height[end_hole] or is_cume == True:
                        break
                except: 
                    break
                hole_size.append(height[end_hole])
            pointer += len(hole_size)
            init_hole = pointer if height[init_hole] > height[pointer] else init_hole
            pointer += 1
            for hole in hole_size:
                water_points += height[init_hole] - hole

Solution().trap([4,2,3])