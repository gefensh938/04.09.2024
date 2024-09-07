# start
score :  int = int(input('what is the score:'))
match score:
    case _ if 0 <= score <= 40:
        print('try harder next time..')
    case _ if 41 <=  score <=60:
        print("your getting there, need some more work")
    case _ if 61 <= score <= 80:
        print('pretty good!')
    case _ if 81 <= score <= 95:
        print('awesome!')
    case _ if 96 <= score <= 100:
        print('excellent!!! your a star!')
    case _:
        print('illegal grade')

# end
