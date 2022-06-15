mobile={
    "mobile_name":"redmi note 6",
    "display":"led",
    "price":45000,
    "ram":"6gb",
    "memory":"64",
}
print(mobile.get("mobile_name"))
print(mobile.get("ram"))
print(mobile.get("memory"))

mobile["band"] = "5g" if "band" in mobile else "4g"
if mobile["price"] >4000:
    mobile["price"]-=1000
else:
    mobile["price"]-=500
    print(mobile)