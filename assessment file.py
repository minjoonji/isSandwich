# def isSandwich(n):
#     n = str(n)  
    
#     if len(n) < 3:
#         return False
    
#     fd = n[0]
#     ld = n[-1]
    
#     if fd == ld and fd not in n[1:-1]:
#         return True
#     else:
#         return False

# def isSandwich(n):
#     if n < 100:
#         return False
    
#     fd = n // 10
#     ld = n % 10
    
#     while fd >= 10:
#         fd //= 10
    
#     n //= 10
#     while n >= 10:
#         d = n % 10
#         if d == fd:
#             return False
#         n //= 10
    
#     return fd == ld

# print(isSandwich(222))  #FALSE

a = 2109%8
print(a)