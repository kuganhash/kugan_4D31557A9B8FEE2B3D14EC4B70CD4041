def linearSearchProudct(productList, targetProduct):
  indices = []
  
  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)
      
  return indices


#Example usage:
products = ["shoes", "boot", "loafer", "sandal", "shoes"]
target = "shoes"
target2 = 'mango'
result = linearSearchProudct(products, target)
print(result)