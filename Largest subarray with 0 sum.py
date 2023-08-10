def maxLen(n, arr):
    max_length = 0

    for i in range(n):
        current_sum = 0
        count = 0
        
        for j in range(i, n):
            current_sum += arr[j]
            count += 1
            
            if current_sum == 0:
                max_length = max(max_length, count)
                
    return max_length

l = "219 442 764 -285 -893 836 59 -336 316 618 -997 -779 7 -34 -22 753 -708 826 -755 72 -79 -484 990 -543 -387 971 -840 -378 -17 -837 -249 -283 489 136 -923 -597 -112 848 -961 -109 -256 -439 887 300 -288 947 785 -849 -42 -867 193 -675 254 464 620 270 710 681 233 501 -819 -412 -28 -227 -249 -743 -617 -803 -646 440 194 849 -769 -849 860 -228 149 -987 907 -953 -368 -302 471 212 727 441 65 -525 -815 -540 79 -58 -764 405 968 -531 -407"
l = l.split()
l = list(map(int, l))
print(maxLen(len(l), l))
