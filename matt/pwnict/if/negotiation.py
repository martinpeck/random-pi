price = 100000.00
still_negotiating = True

while still_negotiating:

    offer = float(raw_input("give me your offer in pounds "))

    how_far_away = price - offer

    how_far_away_percent = (how_far_away / price) * 100


    if how_far_away_percent > 50:
        print "no way mate!"
        still_negotiating = False
    elif how_far_away_percent >= 25 and how_far_away_percent <= 50:
        print "gimme another offer"
        still_negotiating = True 
    elif how_far_away_percent >=10 and how_far_away_percent < 25:
        print "ok i'll reduce my price by 5%"
        price = (price / 100) * 95
        print "the new price is",price
        still_negotiating = True 
    elif how_far_away_percent >=0 and how_far_away_percent < 10:
        print "DEAL!"
        still_negotiating = False
    else:
        print "DEAL! you nutter!"
        still_negotiating = False
        



