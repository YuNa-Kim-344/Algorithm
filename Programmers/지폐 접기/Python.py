def solution(wallet, bill):
    answer = 0
    
    # width = 가로
    # length = 세로
    
#     while min(bill) > min(wallet) or max(bill) > max(wallet) :
#         if bill[0] > bill[1] :
#             bill[0] = bill[0]//2
#         else :
#             bill[1] = bill[1]//2
        
#         answer += 1

    wallet_width, wallet_length = wallet
    bill_width, bill_length = bill
        
    while (
        (wallet_width < bill_width or wallet_length < bill_length) and 
        (wallet_width < bill_length or wallet_length < bill_width)
    ):
        if bill_width > wallet_width or bill_length > wallet_length:
            if bill_width >= bill_length:
                bill_width //= 2
            else:
                bill_length //= 2
        answer += 1

        # 무한 루프 방지
        if bill_width == 0 or bill_length == 0:
            return -1

    return answer
