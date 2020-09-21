import sense_hat

sense = sense_hat.SenseHat()
w = (255, 255, 255)
toggle = True 
sense.clear()
while True:
  for event in sense.stick.get_events():
    if event.action == "pressed" and toggle == True :
      sense.show_letter("C")
      toggle = False
    elif event.action == "pressed" and toggle == False :
      sense.show_letter("M")
      toggle = True
        
