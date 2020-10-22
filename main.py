from pprint import pprint

def make_cook_book():
  cook_book ={}
  with open ("files/recipes.txt", encoding="utf8") as f:
    while True:
      line = f.readline().strip()
      if not line:
        break
      cook_book[line] = []
      number = f.readline().strip()
      for i in range(int(number)):
        dish = f.readline().strip().split(' | ')
        cook_book[line].append({'ingredient_name': dish[0], 'quantity': int(dish[1]), 'measure': dish[2]})
      f.readline().strip()
  return cook_book
def get_shop_list_by_dishes(dishes, person_count):
  cookbook = make_cook_book()
  shop_list = {}
  for dish in dishes:
    if dish in cookbook:
      for ingr in cookbook[dish]: 
        if ingr['ingredient_name'] not in shop_list.keys():
          ingr_list = {ingr['ingredient_name'] : {'measure':ingr['measure'], 'quantity':ingr['quantity'] * person_count}}
          shop_list.update(ingr_list)
        else:
          ingr_list = {ingr['ingredient_name'] : {'measure' : ingr['measure'], 'quantity' : (shop_list[ingr['ingredient_name']]['quantity'] + ingr['quantity']) * person_count}}
        shop_list.update(ingr_list)
  return shop_list

pprint(get_shop_list_by_dishes(['Омлет','Фахитос', 'Запеченный картофель', 'Бутерброд'], 2))

