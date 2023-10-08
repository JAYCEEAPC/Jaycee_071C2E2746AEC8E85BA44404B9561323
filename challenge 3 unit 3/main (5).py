def linearSearchProduct(productList,targetProduct):
  indices=[]
  for index,product in enumerate(productList):
     if product==targetProduct:
       indices.append(index)
  return indices
products=["shoes","boot","loafers","shoes","sandal","shoes"]
target="shoes"
target2="apple"
result1=linearSearchProduct(products,target)
result2=linearSearchProduct(products,target2)
print(result1)
print(result2)