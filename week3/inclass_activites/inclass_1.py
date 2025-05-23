def calc_area():
  #input the base and length of the rectangle
  a = float(input('please input the length: '))
  b = float(input('please input the width: '))



  #calculate the area, and round to 2 decimal
  area = round(a*b,2)

  #out put he area and 
  print(f'The area is {area}')

calc_area()