class pay:
  def __init__(self, hours, rate):
    self.hours = hours
    self.rate = rate

  def myproject(self):
    if hours < 40:
      money = rate * hours
    else:
      time = hours - 40
      money = (rate * 40.0) + (1.5 * rate * time)
    print('pay : ',money)

ehours = input("enter h:")
erate = input("enter r:")
hours = int(ehours)
rate = int(erate)
pays = pay(hours, rate)
pays.myproject()