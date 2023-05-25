# start with 3 heads
# 0..200 - +3 heads
# 201..300 - +2 heads
# > 300 - +1 head



class DragonManager:
    @staticmethod
    def calculate_total_heads(age):
        if isinstance(age, int) and age > 0:
            head = 3

            if age <= 200:
                head += age * 3
            elif age <= 300:
                head += 200 * 3 + (age - 200) * 2
            else:
                head += 200 * 3 + 100 * 2 + (age - 300)

            return head
        else:
            return 0
